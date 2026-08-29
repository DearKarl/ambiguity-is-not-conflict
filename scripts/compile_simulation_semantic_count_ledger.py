"""Compile the TB-0011 output registry and semantic-operation ledger.

This is static protocol compilation only.  It imports the frozen TB-0009
manifest enumerator and uses the Python standard library.  It opens no project
random stream, creates no permutation or synthetic observation, evaluates no
scientific statistic, and performs no benchmark.  The default output is the
small aggregate summary.  ``--registry`` prints a tracked registry and
``--ledger`` streams the full, untracked per-cell semantic-count ledger.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import sys
from dataclasses import dataclass, replace
from typing import Iterable, Iterator, TextIO

try:
    from scripts.enumerate_simulation_resource_manifest import (
        AXES,
        BOOTSTRAP_RESAMPLES,
        CALIBRATION_BISECTIONS,
        CALIBRATION_MEAN_GRID,
        CALIBRATION_VECTORS,
        OUTER_REPLICATIONS,
        VALIDATION_VECTORS,
        build_mv_manifest,
        build_reliability_manifest,
        manifest_sha256,
    )
except ModuleNotFoundError as error:  # Direct ``python scripts/...`` execution.
    if error.name != "scripts":
        raise
    from enumerate_simulation_resource_manifest import (  # type: ignore[no-redef]
        AXES,
        BOOTSTRAP_RESAMPLES,
        CALIBRATION_BISECTIONS,
        CALIBRATION_MEAN_GRID,
        CALIBRATION_VECTORS,
        OUTER_REPLICATIONS,
        VALIDATION_VECTORS,
        build_mv_manifest,
        build_reliability_manifest,
        manifest_sha256,
    )


METRIC_HEADER = (
    "metric_code",
    "record_scope",
    "kind",
    "slot",
    "logical_type",
    "width_bytes",
    "applicability",
    "state_semantics",
    "storage_action",
    "occurrence_formula",
    "aggregate_rule",
    "failure_semantics",
    "status",
)

OPERATION_HEADER = (
    "operation_code",
    "kind",
    "stage",
    "semantic_unit",
    "count_formula",
    "bound_type",
    "alternative",
    "assumption_or_blocker",
    "accounting_role",
)

LEDGER_HEADER = (
    "kind",
    "cell_sha256",
    "operation_code",
    "count",
    "bound_type",
    "alternative",
    "assumption_scope",
)

RELIABILITY_AXIS_ORDER = tuple(axis.identifier for axis in AXES)
RELIABILITY_AXIS_ORDER_TOKEN = ",".join(RELIABILITY_AXIS_ORDER)

SUMMARY_HEADER = (
    "scope",
    "metric",
    "value",
    "unit",
    "bound_type",
    "assumption_scope",
)

STATE_SEMANTICS = (
    "2bit:VALUE|INAPPLICABLE|SCIENTIFIC_UNDEFINED|NOT_REACHED;"
    "non-VALUE payload=canonical_zero;NaN_prohibited_as_state"
)


@dataclass(frozen=True)
class MetricField:
    metric_code: str
    record_scope: str
    kind: str
    slot: str
    logical_type: str
    width_bytes: str
    applicability: str
    state_semantics: str
    storage_action: str
    occurrence_formula: str
    aggregate_rule: str
    failure_semantics: str
    status: str = "freeze_candidate"

    def row(self) -> tuple[str, ...]:
        return tuple(str(getattr(self, name)) for name in METRIC_HEADER)


@dataclass(frozen=True)
class Operation:
    operation_code: str
    kind: str
    stage: str
    semantic_unit: str
    count_formula: str
    bound_type: str
    alternative: str
    assumption_or_blocker: str
    accounting_role: str = "standalone_semantic_unit"

    def row(self) -> tuple[str, ...]:
        return tuple(str(getattr(self, name)) for name in OPERATION_HEADER)


def _metric(
    code: str,
    scope: str,
    kind: str,
    slot: int | str,
    logical_type: str,
    applicability: str,
    storage_action: str,
    occurrence: str,
    aggregate: str,
    failure: str,
    *,
    width: int | str = 8,
    state: str = STATE_SEMANTICS,
    status: str = "freeze_candidate",
) -> MetricField:
    return MetricField(
        code,
        scope,
        kind,
        str(slot),
        logical_type,
        str(width),
        applicability,
        state,
        storage_action,
        occurrence,
        aggregate,
        failure,
        status,
    )


def _stateful_extension_width(logical_type: str) -> str:
    """Return exact payload+state-mask bytes, leaving record framing open."""

    payload_bytes = {
        "U8": 1,
        "BOOL": 1,
        "ENUM8": 1,
        "ENUM16": 2,
        "U16": 2,
        "U32": 4,
        "F64": 8,
        "BYTES32": 32,
        "F64[2]": 16,
        "U32[2]": 8,
        "ENUM8[2]": 2,
        "BYTES32[2]": 64,
        "F64[3]": 24,
        "F64[4]": 32,
    }.get(logical_type)
    if payload_bytes is None:
        return "typed_payload_and_element_state_mask_plus_record_framing_unresolved"
    element_count = {
        "F64[2]": 2,
        "U32[2]": 2,
        "ENUM8[2]": 2,
        "BYTES32[2]": 2,
        "F64[3]": 3,
        "F64[4]": 4,
    }.get(logical_type, 1)
    state_bytes = (2 * element_count + 7) // 8
    return (
        f"{payload_bytes + state_bytes}_including_{payload_bytes}_payload+"
        f"{state_bytes}_element_state_mask;record_framing_unresolved"
    )


def metric_fields() -> list[MetricField]:
    """Return the fixed logical registry; no scientific value is evaluated."""

    fields: list[MetricField] = []

    # The common prefix is deliberately explicit.  Gate outcomes are events,
    # not scientific failure codes; infrastructure provenance is separate.
    common_header = (
        ("common.header.cell_index", "U32", 4, "immutable_catalogue_reference"),
        ("common.header.outer_index", "U32", 4, "zero_based_outer_identity"),
        ("common.header.scientific_status", "ENUM16", 2, "deterministic_status_precedence"),
        ("common.header.primary_failure", "ENUM16", 2, "first_scientific_failure_only"),
        ("common.header.failure_component_mask", "U64", 8, "all_reached_component_failures"),
        ("common.header.event_mask", "U64", 8, "gate_and_operating_events_only"),
        ("common.header.undefined_bootstrap_count", "U16", 2, "0_to_9999;all_resamples_consumed"),
        ("common.header.registry_version", "U16", 2, "immutable_registry_version"),
        ("common.header.execution_provenance_key", "U64", 8, "deterministic_join_key=(cell_index<<32)|outer_index;mutable_attempt_retry_and_infrastructure_provenance_lives_only_in_execution_attempt_sidecar"),
        ("common.header.payload_digest", "BYTES32", 32, "sha256_of_exact_336_or_600_byte_uncompressed_record_with_this_digest_slot_canonical_zero"),
    )
    for code, logical_type, width, meaning in common_header:
        fields.append(
            _metric(
                code,
                "outer_header",
                "common",
                "prefix",
                logical_type,
                "every_emitted_outer_identity;no_reliability_outer_record_when_I_R3=0",
                "persist",
                "sum_rel_cells(M_c)+sum_mv_cells(M_c);0<=M_c<=R_unique_integrity_valid_committed_outer_identities",
                "identity_or_provenance;not_a_scientific_estimate",
                meaning,
                width=width,
                state="not_state_masked;field_specific_enum_or_integer_contract",
            )
        )

    # File/catalogue/audit structures are logical outputs even though their
    # final container count and physical encoding remain owner-blocked.
    file_header = (
        ("common.file.byte_order", "ENUM8", 1, "little_endian_candidate"),
        ("common.file.schema_version", "U16", 2, "immutable_schema_version"),
        ("common.file.registry_digest", "BYTES32", 32, "complete_metric_registry_sha256"),
        ("common.file.content_digest", "BYTES32", 32, "sha256_of_exact_file_bytes_with_this_digest_slot_canonical_zero"),
        ("common.file.record_count", "U64", 8, "exact_records_in_file"),
        ("common.file.byte_count", "U64", 8, "exact_uncompressed_file_bytes"),
    )
    for code, logical_type, width, meaning in file_header:
        fields.append(
            _metric(
                code,
                "file_header",
                "common",
                "header",
                logical_type,
                "every_output_file;file_partition_count_owner_blocked",
                "persist",
                "N_output_files_unresolved",
                "file_identity_and_completeness",
                meaning,
                width=width,
                state="field_specific;missing_header_is_schema_failure",
                status="owner_blocked",
            )
        )

    cp_conformance = (
        (
            "common.conformance.cp95_worst_case_half_width",
            "F64",
            "maximum_over_success_counts_x=0..120000_of_(upper_x-lower_x)/2",
            "VALUE_only_if_all_120001_two_sided_95pct_CP_intervals_are_finite_and_reference_conformant;SCIENTIFIC_UNDEFINED_if_the_complete_scan_is_reached_but_any_interval_or_half_width_is_invalid;NOT_REACHED_until_reference_algorithm_lock_and_complete_scan",
        ),
        (
            "common.conformance.cp95_worst_case_argmax_successes",
            "U32",
            "smallest_x_attaining_the_maximum_half_width",
            "VALUE_iff_the_worst_case_half_width_is_VALUE;SCIENTIFIC_UNDEFINED_with_an_invalid_completed_scan;NOT_REACHED_before_complete_scan",
        ),
        (
            "common.conformance.cp95_half_width_pass",
            "BOOL",
            "true_iff_worst_case_half_width_strictly_less_than_0.003",
            "VALUE_true_or_false_after_complete_scan;false_if_any_numerical_nonconformance_or_if_finite_maximum>=0.003;NOT_REACHED_before_complete_scan",
        ),
    )
    for code, logical_type, aggregate, state_rule in cp_conformance:
        fields.append(
            _metric(
                code,
                "global_algorithm_conformance",
                "common",
                "conformance_extension",
                logical_type,
                "one_global_R=120000_two_sided_95pct_exact_binomial_reference_scan",
                "persist",
                "one_global_conformance_record",
                aggregate,
                "false_or_invalid_conformance_is_a_conclusive_common_numerical_failure;missing_record_makes_both_family_decisions_INCOMPLETE",
                width=_stateful_extension_width(logical_type),
                state=STATE_SEMANTICS + ";" + state_rule,
                status="owner_blocked",
            )
        )

    static_common = (
        ("common.cell.catalogue_index", "U32", "cell_catalogue", "persist"),
        ("common.cell.kind", "ENUM8", "cell_catalogue", "persist"),
        ("common.cell.canonical_identity", "UTF8", "cell_catalogue", "persist"),
        ("common.cell.canonical_identity_length", "U32", "cell_catalogue", "persist"),
        ("common.cell.canonical_identity_digest", "BYTES32", "cell_catalogue", "persist"),
        ("common.cell.family_mask", "U8", "cell_catalogue", "persist"),
        ("common.cell.lock_index", "U32", "cell_static_lock", "persist"),
        ("common.cell.lock_status", "ENUM16", "cell_static_lock", "persist"),
        ("common.cell.lock_failure", "ENUM16", "cell_static_lock", "persist"),
        ("common.cell.outer_replications", "U32", "cell_static_lock", "persist"),
        ("common.cell.bootstrap_resamples", "U32", "cell_static_lock", "persist"),
        ("common.cell.software_lock_digest", "BYTES32", "cell_static_lock", "persist"),
        ("common.cell.algorithm_lock_digest", "BYTES32", "cell_static_lock", "persist"),
        ("common.cell.permutation_payload_digest", "BYTES32", "cell_static_lock", "persist"),
    )
    for code, logical_type, scope, action in static_common:
        static_rule = {
            "common.cell.catalogue_index": "zero_based_lexicographic_rank_of_canonical_identifier_in_combined_reliability_plus_mv1_manifest_anchored_by_combined_manifest_sha256",
            "common.cell.kind": "reliability_or_mv1_enum_crosschecked_against_canonical_identifier",
        }.get(code, "identity_only")
        fields.append(
            _metric(
                code,
                scope,
                "common",
                "dictionary",
                logical_type,
                "every_candidate_cell",
                action,
                "N_cells",
                static_rule,
                "cell_static_failure_if_missing_or_mismatched",
                width="variable_or_parent_schema",
                state="field_specific;no_scientific_undefined_encoding",
            )
        )

    audit_structures = (
        ("common.dictionary.identifier_header", "U16_dictionary+U32_count+U32_bytes", "identifier_dictionary", "N_identifier_dictionaries_unresolved", "owner_blocked"),
        ("common.dictionary.identifier_entry", "U16_length+UTF8", "identifier_dictionary", "sum_dictionary_entries_unresolved", "owner_blocked"),
        ("common.dictionary.permutation_header", "U32_cell+U16_tag_length+U32_list_length+U16_dictionary", "permutation_dictionary", "N_permutations_unresolved", "owner_blocked"),
        ("common.dictionary.permutation_payload", "UTF8_tag+U16[]", "permutation_dictionary", "permutation_payload_bytes_unresolved", "owner_blocked"),
        ("common.completion.bitmap", "BITSET120000", "completion_bitmap", "N_rel_cells+N_mv_candidate_cells", "freeze_candidate"),
        ("common.journal.chunk", "FIXED52", "chunk_journal", "between_N_executable_cells_and_N_executable_cells*R_before_retries", "owner_blocked"),
        ("common.failure.detail", "FIXED28+UTF8", "failure_detail", "unresolved_until_failure_and_retry_policy", "owner_blocked"),
        ("common.execution.attempt", "FIXED32{U64_first_join_key,U32_identity_count,ENUM16_work_unit_kind,U16_attempt_ordinal,ENUM16_outcome,U16_registry_version,U32_failure_detail_ref,U32_chunk_journal_ref,U32_reserved_zero}", "execution_attempt_sidecar", "one_record_per_scheduled_atomic_work_unit_attempt_including_initial_success_failure_or_retry;occurrence_unresolved", "owner_blocked"),
        ("common.aggregate.record", "FIXED16{U32_cell_index,U16_registry_version,ENUM16_status,U32_aggregate_field_count,U32_payload_byte_count}+2bit_field_state_mask+typed_registry_payload", "cell_aggregate", "N_cells", "owner_blocked"),
        ("common.family.record", "typed_registry_payload", "family_aggregate", "2", "owner_blocked"),
        ("common.state_mask.reliability", "2BIT[32]", "outer_state_mask", "sum_rel_cells(M_c)", "freeze_candidate"),
        ("common.state_mask.mv1", "2BIT[64]", "outer_state_mask", "sum_mv_cells(M_c)", "freeze_candidate"),
        ("rel.event_mask.dictionary", "BIT_DICTIONARY", "registry_dictionary", "1", "freeze_candidate"),
        ("mv.event_mask.dictionary", "BIT_DICTIONARY", "registry_dictionary", "1", "freeze_candidate"),
        ("common.failure_component.dictionary", "BIT_DICTIONARY", "registry_dictionary", "1", "owner_blocked"),
        ("common.scientific_status.dictionary", "ENUM_DICTIONARY", "registry_dictionary", "1", "owner_blocked"),
    )
    for code, logical_type, scope, occurrence, status in audit_structures:
        registry_rule = {
            "rel.event_mask.dictionary": "bits0:alpha_point,1:alpha_lower,2:macro,3-6:class_c0-c3,7:allocation,8:missing_overall,9:reader_span,10:arm_span,11:complete_gate,12:coverage,13:outer_nonestimable,14:any_undefined_bootstrap",
            "mv.event_mask.dictionary": "bits0:yield_present,1:yield_absent,2:q_bal,3:q_present,4:q_absent,5:simultaneous_coverage,6:FE_pass,7:LOO_pass,8:no_veto,9:complete_joint,10-12:marginal_coverage_bal-present-absent,13:joint_yield,14:complete_q,15:outer_nonestimable,16:any_undefined_bootstrap",
            "common.execution.attempt": "separate_content_digested_logical_stream;global_catalogue_index_is_lexicographic_rank_in_combined_manifest;outer_join_key=(global_cell_index<<32)|outer_index;reserved_low32_codes_0x80000000=static_cell,0x80000001=mv_calibration_present,0x80000002=mv_calibration_absent,0x80000003=cell_aggregate;global_cell_index_0xffffffff_with_low32_0=REL_family,1=MV_family,2=CP95_conformance;work_unit_kind_ENUM16:1=REL_STATIC,2=REL_OUTER_RANGE,3=MV_STATIC,4=MV_CAL_PRESENT,5=MV_CAL_ABSENT,6=MV_OUTER_RANGE,7=CELL_AGGREGATE,8=REL_FAMILY,9=MV_FAMILY,10=CP95_CONFORMANCE;outcome_ENUM16:1=COMMITTED,2=INTERRUPTED_RETRYABLE,3=INFRASTRUCTURE_FAILED_FINAL,4=INTEGRITY_REJECTED,5=DUPLICATE_IDENTICAL_DISCARDED;scientific_failure_can_be_COMMITTED;outer_range_join_requires_same_global_cell_index_and_first_join_key<=outer_join_key<first_join_key+identity_count;identity_count_positive_and_range_cannot_cross_R=120000_or_reserved_low32_codes;overlapping_committed_ranges_are_schema_failure;static_calibration_cell_aggregate_and_family_work_units_require_identity_count=1;attempt_ordinal_is_contiguous_zero_based_U16_per_atomic_work_identity_and_overflow_is_schema_failure;failure_detail_ref_or_chunk_journal_ref_zero_means_absent_and_positive_refs_are_partition_local;reference_above_U32_requires_new_reviewed_partition_or_schema",
        }.get(code, "identity_completion_restart_failure_or_registry_audit")
        structure_width = {
            "common.dictionary.identifier_header": "10_plus_entries",
            "common.dictionary.identifier_entry": "2_plus_UTF8_length",
            "common.dictionary.permutation_header": "12_plus_tag_and_indices",
            "common.dictionary.permutation_payload": "tag_bytes_plus_2_times_list_length",
            "common.completion.bitmap": "15000",
            "common.journal.chunk": "52",
            "common.failure.detail": "28_plus_UTF8_length",
            "common.execution.attempt": "32",
            "common.aggregate.record": "16_plus_typed_registry_payload",
            "common.family.record": "typed_family_extension_unresolved",
            "common.state_mask.reliability": "8",
            "common.state_mask.mv1": "16",
            "rel.event_mask.dictionary": "registry_extension_unresolved",
            "mv.event_mask.dictionary": "registry_extension_unresolved",
            "common.failure_component.dictionary": "registry_extension_unresolved",
            "common.scientific_status.dictionary": "registry_extension_unresolved",
        }[code]
        fields.append(
            _metric(
                code,
                scope,
                "reliability" if code.startswith("rel.") else "mv1" if code.startswith("mv.") else "common",
                "schema",
                logical_type,
                "as_named_by_record_scope",
                "persist",
                occurrence,
                registry_rule,
                "missing_or_malformed_record_is_schema_failure",
                width=structure_width,
                state="structure_specific;never_NaN_sentinel",
                status=status,
            )
        )

    rel_static = (
        ("rel.cell.axis", "ENUM16", "every_reliability_cell", "axis_dictionary"),
        ("rel.cell.category_count", "U8", "every_reliability_cell", "K_g"),
        ("rel.cell.included_item_count", "U16", "every_reliability_cell", "N_g"),
        ("rel.cell.panel_size", "U8", "every_reliability_cell", "P_g"),
        ("rel.cell.roster_size", "U8", "every_reliability_cell", "roster_g"),
        ("rel.cell.repeat_domain_count", "U16", "owner_blocked", "D_g"),
        ("rel.cell.ambiguity_domain_count", "U16", "owner_blocked", "H_g"),
        ("rel.cell.assignment_digest", "BYTES32", "owner_blocked", "abstract_item_and_assignment_payload"),
        ("rel.cell.missing_intercept", "F64", "nonzero_reader_or_class_missingness;missingness_bisection_rule_owner_blocked", "solved_intercept"),
        ("rel.cell.missing_endpoint_lower", "F64", "nonzero_reader_or_class_missingness", "frozen_bracket_lower_minus_30"),
        ("rel.cell.missing_endpoint_upper", "F64", "nonzero_reader_or_class_missingness", "frozen_bracket_upper_plus_30"),
        ("rel.cell.missing_endpoint_lower_residual", "F64", "nonzero_reader_or_class_missingness;signed_residual_rule_owner_blocked", "signed_residual_at_bracket_lower"),
        ("rel.cell.missing_endpoint_upper_residual", "F64", "nonzero_reader_or_class_missingness;signed_residual_rule_owner_blocked", "signed_residual_at_bracket_upper"),
        ("rel.cell.missing_residual", "F64", "nonzero_reader_or_class_missingness;missingness_bisection_rule_owner_blocked", "selected_final_signed_residual"),
        ("rel.cell.missing_iteration_count", "U16", "nonzero_reader_or_class_missingness;missingness_bracket_and_update_rules_owner_blocked", "realized_midpoint_iterations_zero_or_100"),
        ("rel.cell.missing_bracket_state", "ENUM8", "every_reliability_cell;required_solve_bracket_predicate_owner_blocked", "not_required|pass|fail"),
        ("rel.cell.truth_alpha_41", "F64", "every_reliability_cell_reaching_truth", "quadrature_order_41"),
        ("rel.cell.truth_alpha_61", "F64", "same_as_truth_alpha_41", "quadrature_order_61"),
        ("rel.cell.truth_alpha_delta", "F64", "same_as_truth_alpha_41", "absolute_order_difference"),
        ("rel.cell.truth_alpha_final", "F64", "truth_reference_choice_owner_blocked", "selected_truth"),
        ("rel.cell.truth_macro_41", "F64", "every_reliability_cell_reaching_truth", "quadrature_order_41"),
        ("rel.cell.truth_macro_61", "F64", "same_as_truth_macro_41", "quadrature_order_61"),
        ("rel.cell.truth_macro_delta", "F64", "same_as_truth_macro_41", "absolute_order_difference"),
        ("rel.cell.truth_macro_final", "F64", "truth_reference_choice_owner_blocked", "selected_truth"),
        ("rel.cell.truth_positive_41", "F64[4]", "four_fixed_class_slots;classes_c>=K_g_structurally_absent", "quadrature_order_41"),
        ("rel.cell.truth_positive_61", "F64[4]", "same_as_truth_positive_41", "quadrature_order_61"),
        ("rel.cell.truth_positive_delta", "F64[4]", "same_as_truth_positive_41", "absolute_order_difference"),
        ("rel.cell.truth_positive_final", "F64[4]", "truth_reference_choice_owner_blocked;classes_c>=K_g_structurally_absent", "selected_truth"),
        ("rel.cell.null_boundary_class", "ENUM8", "requires_final_truth", "null|alternative|boundary"),
        ("rel.cell.planning_truth_eligibility", "BOOL", "planning_family_and_final_truth", "family_gate_applicability"),
        ("rel.cell.static_failure", "ENUM16", "every_reliability_cell", "first_static_failure"),
    )
    static_state_prefix = (
        "2bit:VALUE|INAPPLICABLE|SCIENTIFIC_UNDEFINED|NOT_REACHED;"
        "non-VALUE_payload=canonical_zero;NaN_prohibited_as_state;"
    )

    def rel_static_state_rule(code: str) -> str:
        if code in {
            "rel.cell.axis",
            "rel.cell.category_count",
            "rel.cell.included_item_count",
            "rel.cell.panel_size",
            "rel.cell.roster_size",
        }:
            return "VALUE_after_manifest_identity_verification;never_scientifically_undefined"
        if code in {
            "rel.cell.repeat_domain_count",
            "rel.cell.ambiguity_domain_count",
            "rel.cell.assignment_digest",
        }:
            return "VALUE_only_after_owner_frozen_domain_or_payload;NOT_REACHED_while_owner_blocked;zero_is_not_a_substitute"
        if code in {
            "rel.cell.missing_endpoint_lower",
            "rel.cell.missing_endpoint_upper",
        }:
            return "INAPPLICABLE_for_m=0_or_MCAR;VALUE_for_required_reader_or_class_solve_frozen_finite_endpoint;NOT_REACHED_if_static_stage_not_entered"
        if code in {
            "rel.cell.missing_endpoint_lower_residual",
            "rel.cell.missing_endpoint_upper_residual",
        }:
            return "INAPPLICABLE_for_m=0_or_MCAR;NOT_REACHED_until_signed_residual_direction_is_owner_frozen_or_if_static_stage_not_entered;VALUE_if_required_endpoint_residual_is_finite;SCIENTIFIC_UNDEFINED_if_reached_endpoint_evaluation_is_nonfinite"
        if code == "rel.cell.missing_intercept":
            return "INAPPLICABLE_for_m=0_or_MCAR;NOT_REACHED_until_signed_residual_bracket_predicate_midpoint_equality_update_and_post_100_cached_candidate_selection_rules_are_owner_frozen_or_if_static_stage_not_entered;VALUE_if_required_bracket_passes_and_selected_candidate_is_finite_even_when_residual_tolerance_fails;SCIENTIFIC_UNDEFINED_if_selection_is_attempted_without_a_finite_candidate"
        if code == "rel.cell.missing_residual":
            return "INAPPLICABLE_for_m=0_or_MCAR;NOT_REACHED_until_signed_residual_bracket_predicate_midpoint_equality_update_and_post_100_cached_candidate_selection_rules_are_owner_frozen_or_if_bracket_fails;VALUE_if_selected_cached_candidate_residual_is_finite_even_when_abs_residual_above_1e-10;VALUE_with_abs_residual_above_1e-10_causes_static_missingness_failure_and_I_R3=0;SCIENTIFIC_UNDEFINED_if_selection_is_attempted_with_nonfinite_residual"
        if code == "rel.cell.missing_iteration_count":
            return "INAPPLICABLE_for_m=0_or_MCAR;NOT_REACHED_until_bracket_predicate_and_midpoint_equality_update_rules_are_owner_frozen_or_if_static_stage_not_entered;VALUE_zero_if_required_bracket_fails_or_100_if_bisection_runs"
        if code == "rel.cell.missing_bracket_state":
            return "VALUE_ENUM_not_required_for_m=0_or_MCAR;NOT_REACHED_for_required_reader_or_class_solve_until_signed_residual_direction_inclusive_endpoint_zero_predicate_and_nonfinite_semantics_are_owner_frozen_or_if_static_stage_not_entered;VALUE_ENUM_pass_or_fail_after_frozen_required_bracket_check;never_INAPPLICABLE_after_static_audit"
        if code.endswith(("_41", "_61")):
            return "one_independent_2bit_state_per_named_scalar_or_fixed_class_element;class_c>=K_g_is_INAPPLICABLE;applicable_element_NOT_REACHED_if_missingness_stage_fails;when_truth_stage_is_reached_both_orders_are_attempted_and_each_applicable_element_is_VALUE_if_finite_else_SCIENTIFIC_UNDEFINED;one_order_or_element_failure_does_not_erase_the_other"
        if code.endswith("_delta"):
            return "one_independent_2bit_state_per_named_scalar_or_fixed_class_element;class_c>=K_g_is_INAPPLICABLE;VALUE_iff_corresponding_41_and_61_elements_are_VALUE;SCIENTIFIC_UNDEFINED_if_either_reached_order_element_is_undefined;NOT_REACHED_if_truth_stage_not_entered"
        if code.endswith("_final"):
            return "one_independent_2bit_state_per_named_scalar_or_fixed_class_element;class_c>=K_g_is_INAPPLICABLE;NOT_REACHED_until_truth_reference_is_owner_approved_or_if_upstream_truth_stage_not_entered;VALUE_only_if_selected_input_is_VALUE_and_41_61_discrepancy<=1e-6;SCIENTIFIC_UNDEFINED_for_invalid_selected_input_or_excess_discrepancy"
        if code == "rel.cell.null_boundary_class":
            return "VALUE_ENUM8_ALTERNATIVE_iff_final_alpha>0.67_and_final_macro>0.80_and_every_applicable_final_positive>0.70;VALUE_ENUM8_BOUNDARY_iff_no_required_component_is_below_its_threshold_and_at_least_one_equals_its_threshold;VALUE_ENUM8_NULL_iff_any_required_component_is_below_its_threshold;comparisons_use_exact_binary64_selected_truth_values_and_ignore_fixed_positive_slots_c>=K_g_as_INAPPLICABLE;SCIENTIFIC_UNDEFINED_if_final_truth_was_reached_but_any_required_component_is_invalid_or_nonfinite;NOT_REACHED_if_final_truth_stage_not_entered_or_reference_not_frozen"
        if code == "rel.cell.planning_truth_eligibility":
            return "INAPPLICABLE_for_manifest_nonplanning_cell;for_manifest_planning_member_VALUE_true_iff_final_alpha>0.80_and_final_macro>0.85_and_every_applicable_final_positive>0.75_else_VALUE_false_when_all_required_selected_truths_are_finite;comparisons_use_exact_binary64_values_and_ignore_fixed_positive_slots_c>=K_g_as_INAPPLICABLE;SCIENTIFIC_UNDEFINED_if_reached_but_any_required_selected_truth_is_invalid_or_nonfinite;NOT_REACHED_if_final_truth_stage_not_entered_or_reference_not_frozen;I_R3_requires_VALUE_true_for_planning_member"
        if code == "rel.cell.static_failure":
            return "VALUE_ENUM_after_static_audit_including_NONE_or_first_failure;infrastructure_noncompletion_is_separate"
        raise AssertionError(f"missing reliability static state rule: {code}")

    for code, logical_type, applicability, meaning in rel_static:
        blocked = "owner_blocked" in applicability or "owner_blocked" in meaning
        fields.append(
            _metric(
                code,
                "cell_static_extension",
                "reliability",
                "extension",
                logical_type,
                applicability,
                "persist",
                "finite_but_unresolved_static_extension",
                "cell_lock_or_family_classification",
                meaning,
                width=_stateful_extension_width(logical_type),
                state=static_state_prefix + rel_static_state_rule(code),
                status="owner_blocked" if blocked else "freeze_candidate",
            )
        )

    rel_event_rules = {
        "event_alpha_point": "event_bit=0;VALUE_bool_every_outer;success=alpha_VALUE_and_alpha>=0.80;undefined_alpha=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_alpha_lower": "event_bit=1;VALUE_bool_every_outer;success=ci_lower_VALUE_and_ci_lower>=0.67;undefined_interval=>false_and_bit13_and_inherit_or_set_nonestimable_status;undefined_bootstrap_count>0=>also_bit14_and_status_BOOTSTRAP_UNDEFINED;numeric_threshold_miss=>false_only",
        "event_macro": "event_bit=2;VALUE_bool_every_outer;success=macro_VALUE_and_macro>=0.85;undefined_metric=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_class_c0": "event_bit=3;VALUE_bool_every_outer_when_K>0;success=positive_c0_VALUE_and_positive_c0>=0.75;empty_required_denominator=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_class_c1": "event_bit=4;VALUE_bool_every_outer_when_K>1;success=positive_c1_VALUE_and_positive_c1>=0.75;empty_required_denominator=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_class_c2": "event_bit=5;VALUE_bool_every_outer_when_K>2;success=positive_c2_VALUE_and_positive_c2>=0.75;empty_required_denominator=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_class_c3": "event_bit=6;VALUE_bool_every_outer_when_K>3;success=positive_c3_VALUE_and_positive_c3>=0.75;empty_required_denominator=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13;numeric_threshold_miss=>false_only",
        "event_allocation": "event_bit=7;VALUE_bool_every_outer;success=every_frozen_intended_stratum_quota_met;quota_miss=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13",
        "event_missing_overall": "event_bit=8;VALUE_bool_every_outer;success=missing_overall_VALUE_and_missing_overall<=0.05;undefined_or_above_0.05=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13",
        "event_missing_reader_span": "event_bit=9;VALUE_bool_every_outer;success=reader_span_VALUE_and_reader_span<=0.05;undefined_or_above_0.05=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13",
        "event_missing_arm_span": "event_bit=10;VALUE_bool_every_outer;success=arm_span_VALUE_and_arm_span<=0.05;undefined_or_above_0.05=>false_and_status_ESTIMAND_NONESTIMABLE_and_bit13",
        "event_complete_gate": "event_bit=11;VALUE_bool_every_outer;success=bits_0_to_2_and_7_to_10_and_all_applicable_class_bits_true;nonestimable_or_not_reached=false",
        "event_coverage": "event_bit=12;VALUE_bool_every_outer;success=ci_and_final_truth_VALUE_and_ci_lower<=truth_alpha_final<=ci_upper;nonestimable_or_not_reached=false",
    }
    rel_value_state_rules = {
        "alpha": "outer_DGP_reached=>VALUE_if_observed_alpha_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;component_local_failure_does_not_erase_other_reached_slots",
        "alpha_ci_lower": "outer_DGP_and_analysis_reached=>VALUE_iff_observed_alpha_and_all_9999_bootstrap_alphas_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;observed_alpha_remains_VALUE_when_only_bootstrap_fails",
        "alpha_ci_upper": "same_transition_as_alpha_ci_lower;state_is_independent_of_other_reached_descriptives",
        "macro_agreement": "outer_DGP_reached=>VALUE_if_macro_denominator_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_alpha_and_bootstrap_state",
        "missing_overall": "outer_DGP_reached=>VALUE_if_declared_assignment_denominator_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED",
        "missing_reader_min": "outer_DGP_reached=>VALUE_if_all_required_reader_denominators_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED",
        "missing_reader_max": "same_transition_as_missing_reader_min",
        "missing_reader_span": "VALUE_iff_missing_reader_min_and_max_VALUE;SCIENTIFIC_UNDEFINED_if_reached_component_missing;upstream_DGP_nonreach=>NOT_REACHED",
        "missing_arm_min": "outer_DGP_reached=>VALUE_if_all_required_presentation_arm_denominators_defined_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED",
        "missing_arm_max": "same_transition_as_missing_arm_min",
        "missing_arm_span": "VALUE_iff_missing_arm_min_and_max_VALUE;SCIENTIFIC_UNDEFINED_if_reached_component_missing;upstream_DGP_nonreach=>NOT_REACHED",
    }
    for class_index in range(4):
        rel_value_state_rules[f"positive_agreement_c{class_index}"] = (
            f"K_g<={class_index}=>INAPPLICABLE;K_g>{class_index}_and_outer_DGP_reached=>"
            "VALUE_if_required_positive_agreement_denominator_positive_else_SCIENTIFIC_UNDEFINED;"
            "upstream_DGP_nonreach=>NOT_REACHED;component_local_failure_does_not_erase_other_classes_or_descriptives"
        )
        rel_value_state_rules[f"prevalence_c{class_index}"] = (
            f"K_g<={class_index}=>INAPPLICABLE;K_g>{class_index}_and_outer_DGP_reached=>"
            "VALUE_if_declared_prevalence_denominator_positive_else_SCIENTIFIC_UNDEFINED;"
            "upstream_DGP_nonreach=>NOT_REACHED;independent_of_positive_agreement_and_bootstrap_state"
        )
    rel_slots: list[tuple[str, str, str, str]] = [
        ("alpha", "F64", "outer_DGP_reached", "coverage_truth_reference"),
        ("alpha_ci_lower", "F64", "outer_DGP_and_analysis_reached", "percentile_interval"),
        ("alpha_ci_upper", "F64", "outer_DGP_and_analysis_reached", "percentile_interval"),
        ("macro_agreement", "F64", "outer_DGP_reached", "descriptive_metric"),
    ]
    rel_slots.extend(
        (f"positive_agreement_c{i}", "F64", f"K_g>{i};outer_DGP_reached", "class_gate_and_description")
        for i in range(4)
    )
    rel_slots.extend(
        (f"prevalence_c{i}", "F64", f"K_g>{i};outer_DGP_reached", "class_gate_denominator")
        for i in range(4)
    )
    rel_slots.extend(
        (
            ("missing_overall", "F64", "every_reached_outer", "missingness_gate"),
            ("missing_reader_min", "F64", "every_reached_outer", "reader_span_component"),
            ("missing_reader_max", "F64", "every_reached_outer", "reader_span_component"),
            ("missing_reader_span", "F64", "every_reached_outer", "reader_span_gate"),
            ("missing_arm_min", "F64", "every_reached_outer", "presentation_arm_span_component"),
            ("missing_arm_max", "F64", "every_reached_outer", "presentation_arm_span_component"),
            ("missing_arm_span", "F64", "every_reached_outer", "presentation_arm_span_gate"),
            ("event_alpha_point", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_alpha_lower", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_macro", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_class_c0", "BOOL", "K_g>0;every_outer_identity", "event_mask_mirror"),
            ("event_class_c1", "BOOL", "K_g>1;every_outer_identity", "event_mask_mirror"),
            ("event_class_c2", "BOOL", "K_g>2;every_outer_identity", "event_mask_mirror"),
            ("event_class_c3", "BOOL", "K_g>3;every_outer_identity", "event_mask_mirror"),
            ("event_allocation", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_missing_overall", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_missing_reader_span", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_missing_arm_span", "BOOL", "every_outer_identity", "event_mask_mirror"),
            ("event_complete_gate", "BOOL", "every_outer_identity", "all_applicable_gate_components"),
            ("event_coverage", "BOOL", "every_outer_identity", "truth_in_percentile_interval"),
        )
    )
    if len(rel_slots) != 32:
        raise AssertionError("reliability core must contain exactly 32 slots")
    for slot, (name, logical_type, applicability, aggregate) in enumerate(rel_slots):
        fields.append(
            _metric(
                f"rel.outer.{name}",
                "outer_core",
                "reliability",
                slot,
                logical_type,
                applicability,
                "persist",
                "sum_rel_cells(M_c);M_c=0_if_I_R3=0_and_I_complete_iff_M_c=R_with_no_integrity_mismatch",
                rel_event_rules.get(name, aggregate),
                "applicable_event_is_always_VALUE_bool;scientific_nonestimability_is_false"
                if name in rel_event_rules
                else rel_value_state_rules[name],
            )
        )

    rel_aggregate = (
        "coverage",
        "complete_gate",
        "outer_nonestimable",
        "any_undefined_bootstrap",
        "failure_alpha_point",
        "failure_alpha_lower",
        "failure_macro",
        "failure_class_c0",
        "failure_class_c1",
        "failure_class_c2",
        "failure_class_c3",
        "failure_allocation",
        "failure_missing_overall",
        "failure_missing_reader_span",
        "failure_missing_arm_span",
        "false_promotion",
        "planning_power",
    )
    rel_aggregate_rules = {
        "coverage": "x=sum_j I(event_bit12=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;accept_lower>=0.945",
        "complete_gate": "x=sum_j I(event_bit11=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;descriptive",
        "outer_nonestimable": "x=sum_j I(event_bit13=true);N=R=120000;bit13_true_for_undefined_observed_or_bootstrap_statistic_quota_miss_empty_required_class_denominator_or_missingness_span_failure;CP_two_sided_alpha=0.05;ordinary_numeric_gate_threshold_miss_alone_is_not_nonestimability",
        "any_undefined_bootstrap": "x=sum_j I(undefined_bootstrap_count>0);N=R=120000;event_mask_bit14;CP_two_sided_alpha=0.05",
        "failure_alpha_point": "x=sum_j I(event_bit0=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_alpha_lower": "x=sum_j I(event_bit1=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_macro": "x=sum_j I(event_bit2=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_class_c0": "x=sum_j I(event_bit3=false);N=R=120000_when_K>0;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_class_c1": "x=sum_j I(event_bit4=false);N=R=120000_when_K>1;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_class_c2": "x=sum_j I(event_bit5=false);N=R=120000_when_K>2;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_class_c3": "x=sum_j I(event_bit6=false);N=R=120000_when_K>3;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_allocation": "x=sum_j I(event_bit7=false);N=R=120000;not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_missing_overall": "x=sum_j I(event_bit8=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_missing_reader_span": "x=sum_j I(event_bit9=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "failure_missing_arm_span": "x=sum_j I(event_bit10=false);N=R=120000;nonvalue_or_not_reached_is_failure;CP_two_sided_alpha=0.05",
        "false_promotion": "x=sum_j I(event_bit11=true);N=R=120000;applicable_if_final_truth_alpha<=0.67_or_macro<=0.80_or_any_required_positive<=0.70;CP_one_sided_upper_alpha=0.05;accept_upper<=0.055",
        "planning_power": "x=sum_j I(event_bit11=true);N=R=120000;applicable_if_planning_family_and_all_final_truths_above_gate_thresholds;CP_one_sided_lower_alpha=0.05/4416;family_accept_sum_axis(1-min_lower)<=0.10",
    }
    def rel_aggregate_state_prefix(name: str) -> str:
        class_index = {
            "failure_class_c0": 0,
            "failure_class_c1": 1,
            "failure_class_c2": 2,
            "failure_class_c3": 3,
        }.get(name)
        if class_index is not None:
            return (
                f"K_g<={class_index}=>state_INAPPLICABLE;"
                f"K_g>{class_index}_and_I_R3=0=>state_NOT_REACHED_trials=0_no_interval;"
                f"K_g>{class_index}_and_I_R3=1_and_I_complete=0=>state_NOT_REACHED_trials=0_no_interval_completion_or_integrity_failure;"
                f"K_g>{class_index}_and_I_R3=1_and_I_complete=1=>"
            )
        if name == "planning_power":
            return (
                "manifest_planning_membership=0=>state_INAPPLICABLE;"
                "manifest_planning_membership=1_and_I_R3=0=>"
                "state_NOT_REACHED_trials=0_no_interval;"
                "manifest_planning_membership=1_and_I_R3=1_and_I_complete=0=>"
                "state_NOT_REACHED_trials=0_no_interval_completion_or_integrity_failure;"
                "manifest_planning_membership=1_and_I_R3=1_and_I_complete=1=>"
            )
        if name == "false_promotion":
            return (
                "final_truth_classification_unavailable=>state_NOT_REACHED_trials=0_no_interval;"
                "final_truth_resolved_strict_alternative=>state_INAPPLICABLE;"
                "final_truth_resolved_null_or_boundary_and_I_R3=0=>state_NOT_REACHED_trials=0_no_interval;"
                "final_truth_resolved_null_or_boundary_and_I_R3=1_and_I_complete=0=>state_NOT_REACHED_trials=0_no_interval;"
                "final_truth_resolved_null_or_boundary_and_I_R3=1_and_I_complete=1=>"
            )
        return "I_R3=0=>state_NOT_REACHED_trials=0_no_interval;I_R3=1_and_I_complete=0=>state_NOT_REACHED_trials=0_no_interval_completion_or_integrity_failure;I_R3=1_and_I_complete=1=>"

    rel_aggregate_rules = {
        name: rel_aggregate_state_prefix(name) + rule
        for name, rule in rel_aggregate_rules.items()
    }
    for name in rel_aggregate:
        applicability = {
            "false_promotion": "audit_record_every_reliability_cell;VALUE_only_if_final_truth_resolved_null_or_boundary_and_I_R3=1_and_I_complete=1;NOT_REACHED_if_truth_unavailable_or_resolved_null_or_boundary_and_(I_R3=0_or_I_complete=0);INAPPLICABLE_only_if_resolved_strict_alternative",
            "planning_power": "audit_record_every_reliability_cell;VALUE_only_if_manifest_planning_member_and_I_R3=1_and_I_complete=1;NOT_REACHED_if_planning_member_and_(I_R3=0_or_I_complete=0);INAPPLICABLE_if_nonmember",
            "failure_class_c2": "audit_record_every_reliability_cell;VALUE_only_if_K_g>2_and_I_R3=1_and_I_complete=1;NOT_REACHED_if_K_g>2_and_(I_R3=0_or_I_complete=0);INAPPLICABLE_if_K_g<=2",
            "failure_class_c3": "audit_record_every_reliability_cell;VALUE_only_if_K_g>3_and_I_R3=1_and_I_complete=1;NOT_REACHED_if_K_g>3_and_(I_R3=0_or_I_complete=0);INAPPLICABLE_if_K_g<=3",
        }.get(
            name,
            "audit_record_every_reliability_cell;VALUE_only_if_I_R3=1_and_I_complete=1;NOT_REACHED_if_I_R3=0_or_I_complete=0",
        )
        fields.append(
            _metric(
                f"rel.aggregate.{name}",
                "cell_aggregate_event",
                "reliability",
                "event_registry",
                "U64_trials+U64_successes+F64_estimate+ENUM8_interval+F64_alpha+F64_lower+F64_upper",
                applicability,
                "persist",
                "one_stateful_field_per_reliability_candidate",
                rel_aggregate_rules[name],
                "I_complete=1_iff_completion_bitmap_has_all_R_bits_and_exactly_one_integrity_valid_canonical_record_per_outer_identity;I_R3_static_failure_marks_aggregate_NOT_REACHED_and_family_static_failure;I_complete=0_always_marks_aggregate_NOT_REACHED_without_imputation_or_partial_denominator;integrity_schema_or_unequal_duplicate_mismatch_is_conclusive_family_FAIL_and_failed_inventory_member;absence_or_incomplete_records_without_conclusive_mismatch_is_infrastructure_missing_and_family_INCOMPLETE_unless_another_FAIL_dominates;scientific_failure_inside_a_complete_R_run_remains_in_fixed_R_denominator",
                width="typed_aggregate_extension",
            )
        )
    fields.append(
        _metric(
            "rel.aggregate.undefined_bootstrap_fraction",
            "cell_aggregate_descriptive",
            "reliability",
            "aggregate_extension",
            "U64_sum+U64_fixed_denominator+F64_fraction",
            "audit_record_every_reliability_cell;VALUE_only_if_I_R3=1_and_I_complete=1;NOT_REACHED_if_I_R3=0_or_I_complete=0",
            "persist",
            "one_per_reliability_cell",
            "I_R3=1_and_I_complete=1=>sum_undefined/(R*B);I_R3=0_or_I_complete=0=>state_NOT_REACHED_denominator=0_no_fraction;no_binomial_interval",
            "descriptive_only;I_R3_static_failure_or_infrastructure_incompletion_is_not_a_zero_undefined_fraction",
            width="typed_aggregate_extension",
        )
    )

    rel_family = (
        ("candidate_count", "U32", "exactly_10847_manifest_candidates"),
        ("coverage_check_count", "U32", "all_10847_candidate_coverage_or_static_failure_outcomes"),
        ("false_promotion_check_count", "U32", "all_final_truth_classified_null_or_boundary_members_including_exact_threshold_equality"),
        ("planning_power_check_count", "U32", "all_4416_manifest_planning_members_or_static_failure_records"),
        ("axis_minimum", "F64[15]", "fifteen_axis_minima"),
        ("axis_argmin", "U32[15]", "canonical_cell_indices"),
        ("union_failure_sum", "F64", "sum_g(1-L_g_min)"),
        ("complete_member_count", "U32", "candidates_with_static_pass_and_exact_R_outer_accounting_complete"),
        ("failed_member_inventory", "U32[]", "unique_canonical_cell_indices_for_conclusive_schema_integrity_static_or_failed_required_coverage_applicable_false_promotion_or_planning_criterion"),
        ("infrastructure_missing_member_inventory", "U32[]", "unique_candidates_with_no_conclusive_failure_but_infrastructure_incomplete_or_missing_required_records;disjoint_from_failed_inventory"),
        ("family_decision", "ENUM8", "PASS_iff_common_cp95_half_width_pass=true_and_all_10847_static_preconditions_and_R_outer_accounting_complete_and_all_10847_coverage_checks_pass_and_every_applicable_false_promotion_check_passes_and_all_4416_planning_members_present_and_sum_15_axis_failure_minima<=0.10;precedence_FAIL_if_common_cp95_half_width_pass=false_or_any_conclusive_static_or_scientific_criterion_failure_even_with_other_infrastructure_missingness_else_INCOMPLETE_if_common_conformance_missing_or_any_infrastructure_missingness_else_PASS"),
    )
    rel_family_reachability = {
        "candidate_count": "VALUE_after_manifest_identity_verification;independent_of_execution_outcomes",
        "coverage_check_count": "VALUE_as_required_manifest_count_10847;resolved_and_missing_outcomes_are_separately_inventoried",
        "false_promotion_check_count": "VALUE_only_if_every_final_truth_classification_is_resolved;NOT_REACHED_if_any_required_classification_is_unavailable;never_count_a_survivor_subset",
        "planning_power_check_count": "VALUE_as_required_manifest_count_4416;static_failure_records_do_not_delete_members",
        "axis_minimum": f"VALUE_only_if_all_4416_planning_lower_limits_are_VALUE;otherwise_NOT_REACHED;never_minimize_over_survivors;array_axis_order={RELIABILITY_AXIS_ORDER_TOKEN}",
        "axis_argmin": f"same_reachability_as_axis_minimum;array_axis_order={RELIABILITY_AXIS_ORDER_TOKEN};within_each_axis_scan_planning_members_by_ascending_combined_catalogue_index_update_only_on_strictly_smaller_lower_limit_and_retain_first_on_exact_binary64_equality_so_argmin_is_smallest_tied_combined_catalogue_index",
        "union_failure_sum": "VALUE_only_if_all_15_axis_minima_are_VALUE;otherwise_NOT_REACHED",
        "complete_member_count": "VALUE_after_family_audit_closure_even_when_less_than_10847",
        "failed_member_inventory": "VALUE_after_family_audit_closure;contains_only_conclusive_schema_integrity_static_or_required_criterion_failures",
        "infrastructure_missing_member_inventory": "VALUE_after_family_audit_closure;contains_only_no_conclusive_failure_candidates_with_infrastructure_missingness_and_is_disjoint_from_failed_member_inventory",
        "family_decision": "VALUE_after_family_audit_closure_with_ENUM_PASS_FAIL_or_INCOMPLETE;never_NOT_REACHED_once_closure_is_evaluated",
    }
    for name, logical_type, aggregate in rel_family:
        fields.append(
            _metric(
                f"rel.family.{name}",
                "family_aggregate",
                "reliability",
                "family_extension",
                logical_type,
                rel_family_reachability[name],
                "persist",
                "one_reliability_family_record",
                aggregate,
                "outer_scientific_nonestimability_is_retained_inside_fixed_R_event_counts_not_automatic_family_incompletion;deterministic_precedence_is_conclusive_FAIL_over_INCOMPLETE_over_PASS",
                width="typed_family_extension",
            )
        )

    mv_static = (
        ("mv.cell.admissible_mean_lower", "F64[2]", "two_polarities;numerical_domain_endpoint_rule_owner_blocked"),
        ("mv.cell.admissible_mean_upper", "F64[2]", "two_polarities;numerical_domain_endpoint_rule_owner_blocked"),
        ("mv.cell.positive_beta_shape_bound", "F64[2]", "beta_candidates_only;positive_shape_margin_rule_owner_blocked"),
        ("mv.cell.calibration_trace_digest", "BYTES32[2]", "trace_depth_owner_blocked"),
        ("mv.cell.monotonicity_max_decrease", "F64[2]", "two_polarities;numerical_domain_and_inner_alpha_solution_rules_owner_blocked"),
        ("mv.cell.monotonicity_argmax", "U32[2]", "two_polarities;numerical_domain_and_inner_alpha_solution_rules_owner_blocked"),
        ("mv.cell.mu_y", "F64[2]", "two_polarities;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.alpha_y", "F64[2]", "two_polarities;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.beta_shape_parameters", "F64[4]", "beta_candidates_only;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.two_point_mixing_probability", "F64[2]", "two_point_candidates_only;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.candidate_yield_q_residuals", "F64[4]", "order=present_yield,present_q,absent_yield,absent_q;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.validation_yield_q_residuals", "F64[4]", "order=present_yield,present_q,absent_yield,absent_q;inner_alpha_and_final_outer_solution_selection_rules_owner_blocked"),
        ("mv.cell.calibration_bracket_state", "ENUM8[2]", "two_polarities;inner_and_outer_bracket_predicate_and_midpoint_equality_rules_owner_blocked"),
        ("mv.cell.validation_digest", "BYTES32[2]", "validation_digest_domain_and_encoding_owner_blocked"),
        ("mv.cell.calibration_status", "ENUM16", "every_mv_candidate"),
        ("mv.cell.truth_bal_present_absent", "F64[3]", "truth_definition_owner_blocked"),
        ("mv.cell.assignment_digest", "BYTES32", "abstract_assignment_payload_owner_blocked"),
        ("mv.cell.outer_eligibility", "ENUM8", "every_mv_candidate_after_static_calibration_audit"),
    )

    def mv_static_state_rule(code: str) -> str:
        polarity_prefix = (
            "one_independent_2bit_state_per_polarity_in_present_absent_order;"
        )
        if code in {
            "mv.cell.admissible_mean_lower",
            "mv.cell.admissible_mean_upper",
        }:
            return polarity_prefix + "NOT_REACHED_until_the_open_admissible_domain_endpoint_or_interior_margin_rule_is_owner_frozen_or_if_that_polarity_stage_is_not_entered;VALUE_if_the_approved_bound_is_finitely_determined;SCIENTIFIC_UNDEFINED_if_attempted_bound_is_invalid_or_nonfinite"
        if code == "mv.cell.positive_beta_shape_bound":
            return polarity_prefix + "INAPPLICABLE_for_two_point_candidate;for_beta_candidate_NOT_REACHED_until_a_strictly_positive_shape_margin_rule_is_owner_frozen_or_if_that_polarity_stage_is_not_entered;VALUE_if_the_approved_bound_is_finite_and_positive;SCIENTIFIC_UNDEFINED_if_attempted_but_invalid_or_nonfinite"
        if code == "mv.cell.calibration_trace_digest":
            return polarity_prefix + "VALUE_only_after_that_attempted_polarity_has_one_owner_frozen_canonical_whole_trace_transcript_and_digest;NOT_REACHED_if_polarity_not_entered_or_trace_domain_not_frozen;never_substitute_zero_digest"
        if code in {
            "mv.cell.monotonicity_max_decrease",
            "mv.cell.monotonicity_argmax",
        }:
            return polarity_prefix + "NOT_REACHED_until_the_numerical_domain_and_inner_alpha_solution_rules_are_owner_frozen_or_if_the_scan_does_not_complete;VALUE_if_that_polarity_full_scan_completes_with_finite_fixed_order_diagnostic_even_when_tolerance_fails;SCIENTIFIC_UNDEFINED_if_reached_output_is_invalid_or_nonfinite;max_decrease_is_raw_D=max_i(q_i-q_i_plus_1)_without_zero_clamping;argmax_is_zero_based_preceding_scan_point_index_i_in_0_to_999_and_smallest_i_breaks_ties_even_when_all_differences_are_nonpositive"
        if code in {"mv.cell.mu_y", "mv.cell.alpha_y"}:
            return polarity_prefix + "NOT_REACHED_until_the_inner_alpha_and_post_80_outer_midpoint_final_candidate_selection_rules_are_owner_frozen_or_if_the_solve_is_not_reached;VALUE_if_the_selected_cached_mu_and_paired_inner_solve_alpha_are_finite_even_when_later_validation_fails;SCIENTIFIC_UNDEFINED_if_selection_is_attempted_without_a_finite_pair"
        if code == "mv.cell.beta_shape_parameters":
            return "one_independent_2bit_state_per_element_in_present_alpha,present_beta,absent_alpha,absent_beta_order;INAPPLICABLE_for_two_point_candidate;within_each_beta_polarity_both_shape_elements_are_NOT_REACHED_until_the_inner_alpha_and_final_outer_solution_selection_rules_are_owner_frozen_or_if_the_solve_is_not_reached;VALUE_if_constructed_finite_and_strictly_positive;SCIENTIFIC_UNDEFINED_if_attempted_but_invalid_or_nonfinite"
        if code == "mv.cell.two_point_mixing_probability":
            return polarity_prefix + "INAPPLICABLE_for_beta_candidate;for_two_point_candidate_NOT_REACHED_until_the_inner_alpha_and_final_outer_solution_selection_rules_are_owner_frozen_or_if_the_solve_is_not_reached;VALUE_if_constructed_finite_and_in_unit_interval;SCIENTIFIC_UNDEFINED_if_attempted_but_invalid_or_nonfinite"
        if code == "mv.cell.candidate_yield_q_residuals":
            return "one_independent_2bit_state_per_element_in_present_yield,present_q,absent_yield,absent_q_order;signed_yield_residual=estimated_P(E=1_given_Y)-rho_Y;signed_q_residual=estimated_E(q_observed_given_E=1,Y)-q_Y_target;each_selected_polarity_pair_is_VALUE_if_evaluated_finite_even_when_tolerance_fails;SCIENTIFIC_UNDEFINED_per_evaluated_nonfinite_element;NOT_REACHED_until_the_inner_alpha_and_final_outer_solution_selection_rules_are_owner_frozen_or_if_that_polarity_candidate_solution_or_residual_stage_is_not_reached"
        if code == "mv.cell.validation_yield_q_residuals":
            return "one_independent_2bit_state_per_element_in_present_yield,present_q,absent_yield,absent_q_order;signed_yield_residual=validation_estimated_P(E=1_given_Y)-rho_Y;signed_q_residual=validation_estimated_E(q_observed_given_E=1,Y)-q_Y_target;each_polarity_pair_is_VALUE_if_validation_evaluates_finite_even_when_either_absolute_residual_exceeds_0.0005;SCIENTIFIC_UNDEFINED_per_evaluated_nonfinite_element;NOT_REACHED_until_the_inner_alpha_and_final_outer_solution_selection_rules_are_owner_frozen_or_if_that_polarity_validation_stage_is_not_entered"
        if code == "mv.cell.calibration_bracket_state":
            return polarity_prefix + "NOT_REACHED_until_inner_and_outer_bracket_predicates_and_midpoint_zero_equality_updates_are_owner_frozen_or_if_that_polarity_is_not_entered_or_no_conclusive_scientific_bracket_result_commits;VALUE_ENUM_pass_iff_every_required_reached_inner_alpha_bracket_and_the_outer_q_bracket_pass_else_fail_on_the_first_reached_required_bracket_failure;later_nonbracket_failure_does_not_erase_the_bracket_result;never_erase_first_polarity_when_second_is_not_reached"
        if code == "mv.cell.validation_digest":
            return polarity_prefix + "VALUE_only_after_that_polarity_validation_runs_and_one_owner_frozen_canonical_validation_transcript_is_digested;NOT_REACHED_if_validation_not_entered_or_digest_domain_not_frozen;never_substitute_zero_digest"
        if code == "mv.cell.calibration_status":
            return "one_scalar_2bit_state;VALUE_ENUM_after_cell_calibration_audit_including_pass_first_failure_or_infrastructure_incomplete;component_states_remain_independent"
        if code == "mv.cell.truth_bal_present_absent":
            return "one_independent_2bit_state_per_element_in_balanced,present,absent_order;NOT_REACHED_until_truth_definition_is_owner_frozen;under_target_truth_choice_each_finite_manifest_target_is_VALUE_after_identity_even_if_calibration_or_validation_fails;under_validated_truth_choice_each_component_is_NOT_REACHED_if_its_required_validation_is_not_reached;VALUE_if_selected_finite;SCIENTIFIC_UNDEFINED_if_selected_invalid_or_nonfinite;one_component_failure_does_not_erase_the_others"
        if code == "mv.cell.assignment_digest":
            return "one_scalar_2bit_state;VALUE_only_after_owner_frozen_assignment_payload_is_canonically_encoded_and_digested;NOT_REACHED_while_owner_blocked;never_substitute_zero_digest"
        if code == "mv.cell.outer_eligibility":
            return "one_scalar_2bit_state;VALUE_ENUM8_ELIGIBLE=1_NOT_ELIGIBLE=0_INFRASTRUCTURE_INCOMPLETE=2_after_static_calibration_audit;I_outer=1_iff_ELIGIBLE_else_0;NOT_ELIGIBLE_requires_a_conclusive_preouter_scientific_or_static_failure_and_enters_failed_calibration_inventory;INFRASTRUCTURE_INCOMPLETE_requires_no_conclusive_failure_and_enters_infrastructure_missing_member_inventory;never_inferred_from_surviving_outputs"
        raise AssertionError(f"missing MV static state rule: {code}")

    for code, logical_type, applicability in mv_static:
        blocked = "owner_blocked" in applicability
        fields.append(
            _metric(
                code,
                "cell_static_extension",
                "mv1",
                "extension",
                logical_type,
                applicability,
                "persist",
                "finite_but_unresolved_static_extension",
                "calibration_identity_or_outer_eligibility",
                "calibration_failure_stops_outer_stage",
                width=_stateful_extension_width(logical_type),
                state=static_state_prefix + mv_static_state_rule(code),
                status="owner_blocked" if blocked else "freeze_candidate",
            )
        )

    calibration_control_type = (
        "PACKED40{U32_scan_points,U32_alpha_solves,"
        "U32_alpha_bracket_checks,U32_alpha_midpoint_controls,"
        "U32_residual_evaluations,U64_candidate_vector_evaluations,"
        "U8_outer_q_bracket_checks,U16_outer_midpoints,"
        "U32_monotonicity_comparisons,U32_validation_vector_evaluations,"
        "U8_validation_passes}"
    )
    calibration_control_rule = (
        "ordered_realized_counts;counts_include_zero_after_stage_entry;"
        "candidate_and_validation_vectors_separate;"
        "no_count_inferred_from_successful_path_upper_bound"
    )
    for polarity in ("present", "absent"):
        fields.append(
            _metric(
                f"mv.cell.calibration_control_counts_{polarity}",
                "cell_static_extension",
                "mv1",
                "extension",
                calibration_control_type,
                f"{polarity}_polarity_canonical_committed_calibration_path;VALUE_for_committed_scientific_pass_or_conclusive_scientific_calibration_failure;NOT_REACHED_if_no_committed_result_due_to_infrastructure_interruption_or_exhaustion",
                "persist",
                "one_per_mv_candidate",
                calibration_control_rule
                + ";counts_exclude_discarded_or_interrupted_execution_attempts_and_are_retry_schedule_invariant",
                "persist_deterministic_counts_on_committed_scientific_calibration_failure;infrastructure_attempt_work_lives_only_in_execution_sidecar_and_resource_ledger;calibration_failure_stops_outer_stage",
                width="41_including_40_payload+1_field_state_mask;record_framing_unresolved",
                state=static_state_prefix
                + "one_scalar_2bit_state_for_the_complete_polarity_control_record;VALUE_only_for_the_deterministic_committed_scientific_path_even_if_a_later_scientific_stage_fails;NOT_REACHED_if_polarity_not_entered_or_no_committed_result_exists;discarded_retry_partial_counts_never_enter_this_field",
            )
        )

    mv_slots: list[tuple[str, str, str]] = []
    mv_slots.extend((name, "U64", "outer_DGP_reached;count_is_VALUE_even_below_108") for name in ("n_present", "n_absent"))
    mv_slots.extend(
        (
            ("qhat_bal", "F64", "outer_DGP_reached;VALUE_if_both_polarity_means_exist;independent_of_SE"),
            ("qhat_present", "F64", "outer_DGP_reached;VALUE_if_n_present>=1;independent_of_SE"),
            ("qhat_absent", "F64", "outer_DGP_reached;VALUE_if_n_absent>=1;independent_of_SE"),
            ("se_bal", "F64", "qhat_bal_VALUE_and_both_polarity_sample_variances_defined;zero_is_VALUE_but_makes_gate_nonestimable"),
            ("se_present", "F64", "qhat_present_VALUE_and_n_present>=2;zero_is_VALUE_but_makes_gate_nonestimable"),
            ("se_absent", "F64", "qhat_absent_VALUE_and_n_absent>=2;zero_is_VALUE_but_makes_gate_nonestimable"),
            ("lower_bal", "F64", "all_observed_and_9999_resampled_required_SEs_finite_and_positive_and_max_t_critical_VALUE"),
            ("lower_present", "F64", "same_complete_max_t_precondition_as_lower_bal"),
            ("lower_absent", "F64", "same_complete_max_t_precondition_as_lower_bal"),
            ("truth_bal", "F64", "outer_eligible_cell_static_truth;VALUE_independent_of_outer_estimability"),
            ("truth_present", "F64", "outer_eligible_cell_static_truth;VALUE_independent_of_outer_estimability"),
            ("truth_absent", "F64", "outer_eligible_cell_static_truth;VALUE_independent_of_outer_estimability"),
            ("fe_bal", "F64", "outer_DGP_reached;VALUE_if_constrained_FE_fit_full_rank_and_finite"),
            ("fe_present", "F64", "outer_DGP_reached;VALUE_if_constrained_FE_fit_full_rank_and_finite"),
            ("fe_absent", "F64", "outer_DGP_reached;VALUE_if_constrained_FE_fit_full_rank_and_finite"),
        )
    )
    mv_slots.extend(
        (
            ("max_t_critical", "F64", "all_observed_and_9999_resampled_required_SEs_finite_and_positive;otherwise_SCIENTIFIC_UNDEFINED"),
            ("fe_rank", "U16", "outer_DGP_reached;VALUE_even_when_rank_deficient"),
            ("fe_expected_rank", "U16", "outer_DGP_reached;fixed_design_expectation"),
        )
    )
    mv_slots.extend(
        (f"loo_reader_{reader:02d}_{component}", "F64", "outer_DGP_reached;VALUE_if_named_leave_one_reader_component_has_required_polarity_mean;independent_of_max_t_reachability")
        for reader in range(10)
        for component in ("bal", "present", "absent")
    )
    mv_slots.extend(
        (name, logical_type, "every_outer_identity;applicable_event_is_VALUE_bool_and_scientific_nonestimability_or_not_reached_is_false" if name.startswith("event_") else "outer_DGP_reached")
        for name, logical_type in (
            ("count_screen_present_assigned_present", "U64"),
            ("count_screen_present_assigned_absent", "U64"),
            ("count_screen_absent_assigned_present", "U64"),
            ("count_screen_absent_assigned_absent", "U64"),
            ("event_yield_present", "BOOL"),
            ("event_yield_absent", "BOOL"),
            ("event_q_bal", "BOOL"),
            ("event_q_present", "BOOL"),
            ("event_q_absent", "BOOL"),
            ("event_simultaneous_coverage", "BOOL"),
            ("event_fe_pass", "BOOL"),
            ("event_loo_pass", "BOOL"),
            ("event_no_veto", "BOOL"),
            ("event_complete_joint", "BOOL"),
        )
    )
    if len(mv_slots) != 64:
        raise AssertionError(f"MV-1 core must contain exactly 64 slots, got {len(mv_slots)}")
    mv_event_rules = {
        "event_yield_present": "event_bit=0;VALUE_bool_every_outer;success=n_present_VALUE_and_n_present>=108;finite_count_below_108=>false_only;DGP_not_reached=>false_and_bit15_status",
        "event_yield_absent": "event_bit=1;VALUE_bool_every_outer;success=n_absent_VALUE_and_n_absent>=108;finite_count_below_108=>false_only;DGP_not_reached=>false_and_bit15_status",
        "event_q_bal": "event_bit=2;VALUE_bool_every_outer;success=lower_bal_VALUE_and_lower_bal>0.10_strict;missing_required_mean_or_variance_nonpositive_or_nonfinite_observed_SE_or_unavailable_max_t_lower=>false_and_bit15_status;any_resampled_nonpositive_or_nonfinite_required_SE=>also_bit16_and_undefined_bootstrap_count_positive;finite_threshold_miss=>false_only",
        "event_q_present": "event_bit=3;VALUE_bool_every_outer;success=lower_present_VALUE_and_lower_present>0_strict;same_nonestimability_transition_as_q_bal;finite_threshold_miss=>false_only",
        "event_q_absent": "event_bit=4;VALUE_bool_every_outer;success=lower_absent_VALUE_and_lower_absent>0_strict;same_nonestimability_transition_as_q_bal;finite_threshold_miss=>false_only",
        "event_simultaneous_coverage": "event_bit=5;VALUE_bool_every_outer;success=all_three_lower_and_truth_VALUE_and_each_lower<=truth;nonvalue_required_lower=>false_and_bit15_status;any_undefined_bootstrap=>also_bit16;finite_noncoverage=>false_only",
        "event_fe_pass": "event_bit=6;VALUE_bool_every_outer;success=FE_full_rank_finite_and_fe_present>0_and_fe_absent>0_and_abs(fe_bal-qhat_bal)<=0.05;rank_deficient_nonfinite_or_missing_required_polarity=>false_and_bit15_status;finite_veto_threshold_miss=>false_only",
        "event_loo_pass": "event_bit=7;VALUE_bool_every_outer;success=all_30_LOO_VALUE_and_each_present>0_and_absent>0_and_abs(bal-qhat_bal)<=0.05;missing_or_nonfinite_required_LOO_polarity=>false_and_bit15_status;finite_veto_threshold_miss=>false_only",
        "event_no_veto": "event_bit=8;VALUE_bool_every_outer;success=bits6_and7_true;not_reached=false",
        "event_complete_joint": "event_bit=9;VALUE_bool_every_outer;success=bits0_to4_and8_true;nonestimable_or_not_reached=false",
    }
    mv_value_state_rules = {
        "n_present": "outer_DGP_reached=>VALUE_if_evaluable_present_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_n_absent_and_all_later_statistics",
        "n_absent": "outer_DGP_reached=>VALUE_if_evaluable_absent_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_n_present_and_all_later_statistics",
        "qhat_bal": "outer_DGP_reached=>VALUE_if_both_required_polarity_counts_are_at_least_one_and_both_means_and_balanced_combination_are_finite_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_SE_and_bootstrap_state",
        "qhat_present": "outer_DGP_reached=>VALUE_if_n_present>=1_and_present_mean_is_finite_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_SE_and_bootstrap_state",
        "qhat_absent": "outer_DGP_reached=>VALUE_if_n_absent>=1_and_absent_mean_is_finite_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_SE_and_bootstrap_state",
        "se_bal": "qhat_bal_VALUE_and_SE_stage_reached=>VALUE_if_both_required_polarity_counts_are_at_least_two_and_sample_variances_and_combined_SE_are_finite_and_nonnegative_including_zero_else_SCIENTIFIC_UNDEFINED;qhat_bal_nonVALUE_or_SE_stage_not_entered=>NOT_REACHED;zero_VALUE_makes_max_t_nonestimable",
        "se_present": "qhat_present_VALUE_and_SE_stage_reached=>VALUE_if_n_present>=2_and_sample_variance_and_SE_are_finite_and_nonnegative_including_zero_else_SCIENTIFIC_UNDEFINED;qhat_present_nonVALUE_or_SE_stage_not_entered=>NOT_REACHED;zero_VALUE_makes_max_t_nonestimable",
        "se_absent": "qhat_absent_VALUE_and_SE_stage_reached=>VALUE_if_n_absent>=2_and_sample_variance_and_SE_are_finite_and_nonnegative_including_zero_else_SCIENTIFIC_UNDEFINED;qhat_absent_nonVALUE_or_SE_stage_not_entered=>NOT_REACHED;zero_VALUE_makes_max_t_nonestimable",
        "max_t_critical": "max_t_stage_reached=>VALUE_if_all_required_observed_and_9999_resampled_SEs_are_finite_strictly_positive_and_fixed_order_selected_critical_value_is_finite_else_SCIENTIFIC_UNDEFINED;outer_DGP_or_bootstrap_stage_nonreach=>NOT_REACHED;one_invalid_required_SE_invalidates_the_common_critical_value",
        "fe_rank": "outer_DGP_reached_and_FE_fit_attempted=>VALUE_if_computed_rank_is_valid_U16_even_when_rank_deficient_else_SCIENTIFIC_UNDEFINED;outer_DGP_or_FE_fit_nonreach=>NOT_REACHED",
        "fe_expected_rank": "outer_DGP_reached=>VALUE_frozen_design_expected_rank;upstream_DGP_nonreach=>NOT_REACHED;design_identity_mismatch_is_schema_failure_not_a_scientific_value",
        "count_screen_present_assigned_present": "outer_DGP_reached=>VALUE_if_named_screen_by_assignment_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_other_tally_slots",
        "count_screen_present_assigned_absent": "outer_DGP_reached=>VALUE_if_named_screen_by_assignment_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_other_tally_slots",
        "count_screen_absent_assigned_present": "outer_DGP_reached=>VALUE_if_named_screen_by_assignment_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_other_tally_slots",
        "count_screen_absent_assigned_absent": "outer_DGP_reached=>VALUE_if_named_screen_by_assignment_count_reduction_produces_valid_U64_including_zero_else_SCIENTIFIC_UNDEFINED;upstream_DGP_nonreach=>NOT_REACHED;independent_of_other_tally_slots",
    }
    for component in ("bal", "present", "absent"):
        mv_value_state_rules[f"lower_{component}"] = (
            f"VALUE_iff_qhat_{component}_and_se_{component}_and_max_t_critical_are_VALUE_and_inclusive_lower=qhat_minus_critical_times_SE_is_finite;"
            "SCIENTIFIC_UNDEFINED_if_all_prerequisites_are_VALUE_but_lower_construction_is_nonfinite;"
            "NOT_REACHED_if_any_prerequisite_is_nonVALUE_or_lower_stage_not_entered;component_state_is_independent_after_common_max_t_reachability"
        )
        mv_value_state_rules[f"truth_{component}"] = (
            f"outer_record_reached_and_selected_cell_static_truth_{component}_VALUE=>VALUE_with_exact_finite_truth_copy;"
            f"outer_record_reached_and_selected_cell_static_truth_{component}_SCIENTIFIC_UNDEFINED=>SCIENTIFIC_UNDEFINED;"
            f"outer_record_nonreach_or_selected_cell_static_truth_{component}_NOT_REACHED=>NOT_REACHED;"
            "independent_of_outer_q_SE_max_t_FE_and_LOO_estimability"
        )
        mv_value_state_rules[f"fe_{component}"] = (
            f"outer_DGP_reached_and_FE_fit_attempted=>VALUE_if_fit_has_expected_full_rank_and_named_{component}_coefficient_is_finite_else_SCIENTIFIC_UNDEFINED;"
            "outer_DGP_or_FE_fit_nonreach=>NOT_REACHED;rank_deficiency_or_nonfinite_component_does_not_erase_qhat_or_LOO_slots"
        )
    for reader in range(10):
        for component in ("bal", "present", "absent"):
            mv_value_state_rules[f"loo_reader_{reader:02d}_{component}"] = (
                f"outer_DGP_reached_and_named_reader_{reader:02d}_LOO_fit_attempted=>VALUE_if_named_{component}_required_polarity_mean_exists_and_component_estimate_is_finite_else_SCIENTIFIC_UNDEFINED;"
                "outer_DGP_or_named_LOO_fit_nonreach_due_to_earlier_failure=>NOT_REACHED;one_reader_or_component_failure_does_not_erase_other_reached_LOO_slots"
            )
    mv_non_event_names = {name for name, _, _ in mv_slots if name not in mv_event_rules}
    if set(mv_value_state_rules) != mv_non_event_names:
        missing = sorted(mv_non_event_names - set(mv_value_state_rules))
        extra = sorted(set(mv_value_state_rules) - mv_non_event_names)
        raise AssertionError(f"MV-1 value-state map mismatch: missing={missing}, extra={extra}")
    for slot, (name, logical_type, applicability) in enumerate(mv_slots):
        fields.append(
            _metric(
                f"mv.outer.{name}",
                "outer_core",
                "mv1",
                slot,
                logical_type,
                applicability,
                "persist",
                "sum_mv_cells(M_c);M_c=0_if_not_outer_eligible_and_I_complete_iff_M_c=R_with_no_integrity_mismatch",
                mv_event_rules.get(name, "fixed_bal_present_absent_or_reader_major_order"),
                "applicable_event_is_always_VALUE_bool;scientific_nonestimability_is_false"
                if name in mv_event_rules
                else mv_value_state_rules[name],
            )
        )

    mv_aggregate = (
        "coverage_bal",
        "coverage_present",
        "coverage_absent",
        "simultaneous_coverage",
        "yield_present",
        "yield_absent",
        "joint_yield",
        "q_gate_bal",
        "q_gate_present",
        "q_gate_absent",
        "complete_q_family",
        "fe_pass",
        "loo_pass",
        "combined_no_veto",
        "complete_joint",
        "outer_nonestimable",
        "any_undefined_bootstrap",
        "null_false_qualification",
        "planning_joint_power",
    )
    mv_aggregate_rules = {
        "coverage_bal": "x=sum_j I(lower_bal_VALUE_and_truth_bal_VALUE_and_lower_bal<=truth_bal);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;event_mask_bit10;CP_two_sided_alpha=0.05;descriptive_marginal",
        "coverage_present": "x=sum_j I(lower_present_VALUE_and_truth_present_VALUE_and_lower_present<=truth_present);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;event_mask_bit11;CP_two_sided_alpha=0.05;descriptive_marginal",
        "coverage_absent": "x=sum_j I(lower_absent_VALUE_and_truth_absent_VALUE_and_lower_absent<=truth_absent);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;event_mask_bit12;CP_two_sided_alpha=0.05;descriptive_marginal",
        "simultaneous_coverage": "x=sum_j I(event_bit5=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;accept_lower>=0.945",
        "yield_present": "x=sum_j I(event_bit0=true);N=R=120000;not_reached_counts_failure;CP_two_sided_alpha=0.05;descriptive",
        "yield_absent": "x=sum_j I(event_bit1=true);N=R=120000;not_reached_counts_failure;CP_two_sided_alpha=0.05;descriptive",
        "joint_yield": "x=sum_j I(event_bits0_and1=true);N=R=120000;not_reached_counts_failure;event_mask_bit13;CP_two_sided_alpha=0.05;descriptive",
        "q_gate_bal": "x=sum_j I(event_bit2=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;strict_lower>0.10",
        "q_gate_present": "x=sum_j I(event_bit3=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;strict_lower>0",
        "q_gate_absent": "x=sum_j I(event_bit4=true);N=R=120000;scientific_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05;strict_lower>0",
        "complete_q_family": "x=sum_j I(event_bits2_to4_all_true);N=R=120000;nonestimable_or_not_reached_counts_failure;event_mask_bit14;CP_two_sided_alpha=0.05",
        "fe_pass": "x=sum_j I(event_bit6=true);N=R=120000;rank_nonfinite_nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05",
        "loo_pass": "x=sum_j I(event_bit7=true);N=R=120000;nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05",
        "combined_no_veto": "x=sum_j I(event_bit8=true);N=R=120000;nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05",
        "complete_joint": "x=sum_j I(event_bit9=true);N=R=120000;nonestimable_or_not_reached_counts_failure;CP_two_sided_alpha=0.05",
        "outer_nonestimable": "x=sum_j I(event_bit15=true);N=R=120000;bit15_true_for_DGP_nonreach_missing_required_polarity_mean_or_variance_nonpositive_or_nonfinite_required_observed_or_resampled_SE_unavailable_max_t_or_lower_FE_rank_or_nonfinite_missing_LOO_polarity_or_numerical_nonconformance;CP_two_sided_alpha=0.05;finite_yield_q_FE_or_LOO_threshold_miss_alone_is_not_nonestimability",
        "any_undefined_bootstrap": "x=sum_j I(undefined_bootstrap_count>0);N=R=120000;event_mask_bit16;CP_two_sided_alpha=0.05",
        "null_false_qualification": "x=sum_j I(event_bits2_to4_all_true);N=R=120000;applicable_if_manifest_target_q_bal=(q_present_target+q_absent_target)/2=0.10_or_q_present_target=0_or_q_absent_target=0;membership_independent_of_selected_calibrated_truth;nonestimable_or_not_reached_counts_failure;CP_one_sided_upper_alpha=0.05;accept_upper<=0.055",
        "planning_joint_power": "x=sum_j I(event_bit9=true);N=R=120000;applicable_to_all_2304_manifest_planning_members_after_calibration_or_failed_member;CP_two_sided_alpha=0.05;accept_lower>=0.90",
    }
    mv_aggregate_rules = {
        name: (
            (
                "manifest_family_membership=0=>state_INAPPLICABLE;"
                "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0;"
                "manifest_family_membership=1_and_outer_eligibility=NOT_ELIGIBLE=>"
                "state_NOT_REACHED_trials=0_no_interval_conclusive_preouter_failure_enters_family_FAIL_inventory;"
                "manifest_family_membership=1_and_outer_eligibility=INFRASTRUCTURE_INCOMPLETE=>"
                "state_NOT_REACHED_trials=0_no_interval_enters_family_INCOMPLETE_inventory_unless_another_FAIL_dominates;"
                "manifest_family_membership=1_and_outer_eligibility=ELIGIBLE_and_I_complete=0=>"
                "state_NOT_REACHED_trials=0_no_interval_completion_or_integrity_failure;"
                "manifest_family_membership=1_and_outer_eligibility=ELIGIBLE_and_I_complete=1=>"
            )
            if name in {"null_false_qualification", "planning_joint_power"}
            else (
                "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0;"
                "outer_eligibility=NOT_ELIGIBLE=>state_NOT_REACHED_trials=0_no_interval_conclusive_preouter_failure_enters_family_FAIL_inventory;"
                "outer_eligibility=INFRASTRUCTURE_INCOMPLETE=>state_NOT_REACHED_trials=0_no_interval_enters_family_INCOMPLETE_inventory_unless_another_FAIL_dominates;"
                "outer_eligibility=ELIGIBLE_and_I_complete=0=>state_NOT_REACHED_trials=0_no_interval_completion_or_integrity_failure;"
                "outer_eligibility=ELIGIBLE_and_I_complete=1=>"
            )
        )
        + rule
        for name, rule in mv_aggregate_rules.items()
    }
    for name in mv_aggregate:
        applicability = {
            "null_false_qualification": "audit_record_every_mv_candidate;VALUE_only_if_immutable_manifest_null_boundary_member_and_outer_eligibility=ELIGIBLE_and_I_complete=1;NOT_REACHED_if_manifest_null_member_and_(outer_eligibility_in_NOT_ELIGIBLE_or_INFRASTRUCTURE_INCOMPLETE_or_I_complete=0);INAPPLICABLE_if_nonmember",
            "planning_joint_power": "audit_record_every_mv_candidate;VALUE_only_if_manifest_planning_member_and_outer_eligibility=ELIGIBLE_and_I_complete=1;NOT_REACHED_if_planning_member_and_(outer_eligibility_in_NOT_ELIGIBLE_or_INFRASTRUCTURE_INCOMPLETE_or_I_complete=0);INAPPLICABLE_if_nonmember",
        }.get(
            name,
            "audit_record_every_mv_candidate;VALUE_only_if_outer_eligibility=ELIGIBLE_and_I_complete=1;NOT_REACHED_if_outer_eligibility_in_NOT_ELIGIBLE_or_INFRASTRUCTURE_INCOMPLETE_or_I_complete=0",
        )
        fields.append(
            _metric(
                f"mv.aggregate.{name}",
                "cell_aggregate_event",
                "mv1",
                "event_registry",
                "U64_trials+U64_successes+F64_estimate+ENUM8_interval+F64_alpha+F64_lower+F64_upper",
                applicability,
                "persist",
                "one_stateful_field_per_mv_candidate",
                mv_aggregate_rules[name],
                "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0;outer_eligibility=NOT_ELIGIBLE_marks_aggregate_NOT_REACHED_and_family_FAIL;outer_eligibility=INFRASTRUCTURE_INCOMPLETE_marks_aggregate_NOT_REACHED_and_family_INCOMPLETE_unless_another_FAIL_dominates;I_complete=1_iff_completion_bitmap_has_all_R_bits_and_exactly_one_integrity_valid_canonical_record_per_outer_identity;I_complete=0_always_marks_aggregate_NOT_REACHED_without_imputation_or_partial_denominator;integrity_schema_or_unequal_duplicate_mismatch_is_conclusive_family_FAIL_and_failed_outer_inventory_member;absence_or_incomplete_records_without_conclusive_mismatch_is_infrastructure_missing_and_family_INCOMPLETE_unless_another_FAIL_dominates;scientific_failure_inside_a_complete_R_run_remains_in_fixed_R_denominator",
                width="typed_aggregate_extension",
            )
        )

    mv_family = (
        ("calibration_candidate_count", "U32", "all_manifest_candidates"),
        ("failed_calibration_inventory", "U32[]", "unique_canonical_cell_indices_with_conclusive_preouter_calibration_or_static_failure"),
        ("failed_outer_or_aggregate_inventory", "U32[]", "unique_outer_eligible_canonical_cell_indices_with_conclusive_schema_or_integrity_failure_in_the_outer_record_set_or_failure_of_a_required_cell_level_aggregate_criterion;ordinary_finite_outer_gate_misses_and_outer_nonestimability_are_not_direct_family_failures_except_through_their_fixed_R_aggregate_outcome;excludes_every_preouter_failed_candidate"),
        ("infrastructure_missing_member_inventory", "U32[]", "unique_candidates_with_no_conclusive_failure_but_infrastructure_incomplete_or_missing_required_records;disjoint_from_both_failure_inventories"),
        ("null_upper_check_count", "U32", "all_108_manifest_target_null_audit_outcomes_VALUE_or_failed_member_NOT_REACHED"),
        ("coverage_check_count", "U32", "all_2438_candidate_coverage_audit_outcomes_VALUE_or_failed_member_NOT_REACHED"),
        ("planning_power_check_count", "U32", "all_2304_manifest_planning_members_or_failed_inventory"),
        ("missing_member_count", "U32", "unique_candidates_with_no_conclusive_failure_but_infrastructure_incomplete_or_missing_required_records;disjoint_from_both_failure_inventories"),
        ("family_decision", "ENUM8", "PASS_iff_common_cp95_half_width_pass=true_and_all_2438_candidates_calibrate_and_complete_R_outer_accounting_and_all_eligible_coverage_checks_pass_and_all_108_manifest_target_null_checks_pass_and_all_2304_planning_checks_pass;precedence_FAIL_if_common_cp95_half_width_pass=false_or_any_conclusive_calibration_static_or_scientific_criterion_failure_even_with_other_infrastructure_missingness_else_INCOMPLETE_if_common_conformance_missing_or_any_infrastructure_missingness_else_PASS"),
    )
    mv_family_reachability = {
        "calibration_candidate_count": "VALUE_after_manifest_identity_verification;exactly_2438_independent_of_calibration_outcomes",
        "failed_calibration_inventory": "VALUE_after_family_audit_closure;contains_conclusive_calibration_failures_not_infrastructure_missingness",
        "failed_outer_or_aggregate_inventory": "VALUE_after_family_audit_closure;contains_conclusive_outer_record_set_schema_or_integrity_failures_or_required_cell_level_aggregate_criterion_failures;never_individual_outer_gate_misses_directly",
        "infrastructure_missing_member_inventory": "VALUE_after_family_audit_closure;contains_only_no_conclusive_failure_candidates_with_infrastructure_missingness_and_is_disjoint_from_both_failure_inventories",
        "null_upper_check_count": "VALUE_as_required_manifest_count_108;failed_null_members_remain_NOT_REACHED_audit_outcomes",
        "coverage_check_count": "VALUE_as_required_candidate_count_2438;failed_members_remain_NOT_REACHED_audit_outcomes",
        "planning_power_check_count": "VALUE_as_required_manifest_count_2304;failed_planning_members_remain_NOT_REACHED_audit_outcomes",
        "missing_member_count": "VALUE_after_family_audit_closure;counts_only_no_conclusive_failure_candidates_with_infrastructure_missingness_and_is_disjoint_from_both_failure_inventories",
        "family_decision": "VALUE_after_family_audit_closure_with_ENUM_PASS_FAIL_or_INCOMPLETE;never_NOT_REACHED_once_closure_is_evaluated",
    }
    for name, logical_type, aggregate in mv_family:
        fields.append(
            _metric(
                f"mv.family.{name}",
                "family_aggregate",
                "mv1",
                "family_extension",
                logical_type,
                mv_family_reachability[name],
                "persist",
                "one_mv_family_record",
                aggregate,
                "outer_scientific_nonestimability_is_retained_inside_fixed_R_event_counts_not_automatic_family_incompletion;deterministic_precedence_is_conclusive_FAIL_over_INCOMPLETE_over_PASS",
                width="typed_family_extension",
            )
        )

    fields.append(
        _metric(
            "rel.exclusion.observed_reader_sensitivities",
            "canonical_exclusion",
            "reliability",
            "none",
            "INAPPLICABLE",
            "hierarchical_Gwet_ordinal_adjudication_and_full_reader_tables",
            "exclude_from_current_simulation;future_addition_requires_canonical_amendment_and_reenumeration",
            "0_simulated_occurrences_exact",
            "observed_reader_analysis_only",
            "not_a_storage_or_benchmark_blocker_under_unchanged_contract",
            width=0,
            state="INAPPLICABLE_to_current_simulation",
            status="canonical_exclusion",
        )
    )

    # These are deliberately not assigned zero slots or zero bytes.
    blockers = (
        ("rel.extension.repeat_diagnostics", "reliability", "exact_repeat_estimators_and_domains_not_frozen"),
        ("mv.extension.repeat_diagnostics", "mv1", "exact_probability_and_category_repeat_estimators_not_frozen"),
        ("common.extension.failure_detail", "common", "message_and_component_taxonomy_not_frozen"),
        ("common.extension.chunk_journal", "common", "chunk_and_retry_policy_not_frozen"),
        ("common.extension.permutation_dictionary", "common", "abstract_item_identifiers_and_permutations_not_frozen"),
    )
    for code, kind, blocker in blockers:
        fields.append(
            _metric(
                code,
                "owner_blocked_extension",
                kind,
                "extension",
                "UNRESOLVED",
                blocker,
                "must_persist_if_approved;never_assume_zero",
                "unresolved_positive_or_zero_by_owner_decision",
                "not_aggregated_until_frozen",
                "blocks_final_storage_upper_bound_and_benchmark",
                width="unresolved",
                status="owner_blocked",
            )
        )

    codes = [field.metric_code for field in fields]
    if len(codes) != len(set(codes)):
        raise AssertionError("metric codes must be unique")
    for kind, expected in (("reliability", 32), ("mv1", 64)):
        slots = [
            int(field.slot)
            for field in fields
            if field.kind == kind and field.record_scope == "outer_core"
        ]
        if slots != list(range(expected)):
            raise AssertionError(f"{kind} outer slots are not contiguous")
    return fields


def operation_registry() -> list[Operation]:
    """Return abstract work units; none are throughput or runtime claims."""

    rows = [
        Operation("common.cell_identifier_hash", "common", "catalogue", "sha256_calls", "1", "exact", "all", "one_exact_canonical_cell_identifier", "standalone_identity"),
        Operation("common.catalogue_serializations", "common", "catalogue", "record_serializations", "1", "exact", "all", "one_catalogue_record_per_candidate", "standalone_serialization"),
        Operation("common.catalogue_bytes", "common", "catalogue", "bytes", "42+L_i", "exact", "all", "fixed_header_plus_exact_canonical_JSON", "standalone_storage"),
        Operation("common.static_lock_serializations", "common", "static_identity", "record_serializations", "1", "exact", "all", "one_cell_static_lock_per_candidate", "standalone_serialization"),
        Operation("common.static_lock_bytes", "common", "static_identity", "bytes", "112", "exact", "all", "TB0010_fixed_cell_lock", "standalone_storage"),
        Operation("common.identifier_dictionary_serializations", "common", "static_identity", "record_serializations", "unresolved", "unresolved", "owner_choice", "identifier_dictionary_partition_and_deduplication_policy_not_frozen", "standalone_serialization_blocker"),
        Operation("common.permutation_dictionary_serializations", "common", "static_identity", "record_serializations", "unresolved", "unresolved", "owner_choice", "abstract_item_assignment_and_repeat_domains_not_frozen", "standalone_serialization_blocker"),
        Operation("common.static_extension_serializations", "common", "static_output", "record_serializations", "1", "exact", "all", "one_typed_static_extension_per_candidate", "standalone_serialization"),
        Operation("common.static_extension_bytes", "common", "static_output", "bytes", "unresolved", "unresolved", "owner_choice", "truth_calibration_trace_and_failure_fields_not_frozen", "standalone_storage_blocker"),
        Operation("common.permutation_hmac_calls", "common", "static_identity", "hmac_calls", "unresolved", "unresolved", "owner_choice", "abstract_item_assignment_and_repeat_domains_not_frozen", "standalone_identity_blocker"),
        Operation("common.permutation_payload_digest_calls", "common", "static_identity", "sha256_calls", "I_assignment*1", "conditional_exact", "all", "I_assignment=1_after_the_cell_assignment_and_permutation_payload_is_frozen", "shared_digest_for_static_lock_and_assignment_digest_aliases_do_not_double_count"),
        Operation("common.permutation_dictionary_bytes", "common", "static_identity", "bytes", "unresolved", "unresolved", "owner_choice", "identifier_and_permutation_payload_not_frozen", "standalone_storage_blocker"),
        Operation("common.chunk_payload_digest_calls", "common", "checkpoint", "sha256_calls", "unresolved", "unresolved", "chunk_policy", "one_digest_per_committed_chunk_but_chunk_count_not_frozen", "standalone_identity_blocker"),
        Operation("common.chunk_journal_bytes", "common", "checkpoint", "bytes", "52*N_chunk_journal_records", "unresolved", "chunk_policy", "one_exact_52_byte_logical_journal_record_per_realized_chunk_journal_entry_but_occurrence_and_file_framing_are_not_frozen", "standalone_persistent_audit_storage_blocker"),
        Operation("common.failure_detail_bytes", "common", "failure_audit", "bytes", "sum_failure_records(28+UTF8_message_length)", "unresolved", "failure_policy", "fixed_28_byte_logical_prefix_plus_exact_message_bytes_per_realized_failure_detail_but_occurrence_message_taxonomy_and_file_framing_are_not_frozen", "standalone_persistent_audit_storage_blocker"),
        Operation("common.completion_bitmap_serializations", "common", "checkpoint", "record_serializations", "1", "exact", "all", "one_120000_bit_bitmap_per_candidate", "standalone_serialization"),
        Operation("common.completion_bitmap_bytes", "common", "checkpoint", "bytes", "15000", "exact", "all", "one_bit_per_frozen_outer_identity", "standalone_storage"),
        Operation("common.cell_aggregate_serializations", "common", "aggregate", "record_serializations", "1", "exact", "all", "one_cell_aggregate_record_even_when_incomplete", "standalone_serialization"),
        Operation("common.cell_aggregate_bytes", "common", "aggregate", "bytes", "unresolved", "unresolved", "owner_choice", "typed_event_and_interval_payload_width_not_frozen", "standalone_storage_blocker"),
        Operation("global.manifest_hash_reductions", "global", "catalogue", "hash_reductions", "3", "exact", "all", "reliability_mv1_and_combined_sorted_identifier_hashes", "global_once"),
        Operation("global.metric_registry_digest_calls", "global", "serialization", "sha256_calls", "1", "exact", "all", "one_digest_of_the_complete_frozen_metric_registry", "global_once"),
        Operation("global.registry_dictionary_serializations", "global", "serialization", "record_serializations", "4", "exact", "all", "exactly_rel_event_mv_event_failure_component_and_scientific_status_dictionary_records", "global_once_four_named_registry_dictionaries"),
        Operation("global.registry_dictionary_bytes", "global", "serialization", "bytes", "unresolved", "unresolved", "owner_choice", "complete_record_framing_and_payload_bytes_for_exactly_the_four_named_registry_dictionaries_not_frozen;disjoint_from_identifier_and_permutation_dictionaries_and_container_headers", "global_storage_blocker"),
        Operation("global.cp95_conformance_interval_calls", "global", "algorithm_conformance", "exact_binomial_intervals", "120001", "exact", "composite_exact_binomial_path", "one_two_sided_95pct_CP_interval_for_each_success_count_x=0..120000_at_fixed_N=120000", "composite_conformance_alternative_do_not_sum_with_primitive_quantiles"),
        Operation("global.cp95_conformance_beta_quantile_calls", "global", "algorithm_conformance", "beta_quantile_calls", "240000", "exact", "primitive_exact_binomial_path", "two_calls_for_each_interior_x_and_one_call_at_each_boundary_x=0_or_120000", "primitive_conformance_alternative_do_not_sum_with_composite_interval_calls"),
        Operation("global.cp95_half_width_evaluations", "global", "algorithm_conformance", "endpoint_difference_and_halving_events", "120001", "exact", "all", "one_(upper-lower)/2_evaluation_per_success_count"),
        Operation("global.cp95_max_argmax_comparisons", "global", "algorithm_conformance", "ordered_comparisons", "120000", "exact", "all", "fixed_ascending_x_scan_with_smallest_x_tie_break", "shared_comparison_for_maximum_and_argmax_outputs"),
        Operation("global.cp95_threshold_comparisons", "global", "algorithm_conformance", "strict_threshold_comparisons", "1", "exact", "all", "worst_case_half_width_strictly_less_than_0.003"),
        Operation("global.cp95_conformance_record_serializations", "global", "algorithm_conformance", "record_serializations", "1", "exact", "all", "one_global_typed_conformance_record"),
        Operation("global.cp95_conformance_record_bytes", "global", "algorithm_conformance", "bytes", "unresolved", "unresolved", "container_choice", "three_typed_fields_have_exact_payload_and_state_bytes_but_record_framing_not_frozen", "global_storage_blocker"),
        Operation("global.cp95_execution_attempt_records", "global", "restart", "record_serializations", "unresolved", "unresolved", "resource_policy", "32_byte_execution_sidecar_records_for_CP95_CONFORMANCE_work_only;global_join_key=(0xffffffff<<32)|2;disjoint_from_family_and_per_candidate_work", "global_restart_blocker"),
        Operation("global.cp95_execution_attempt_record_bytes", "global", "restart", "bytes", "unresolved", "unresolved", "resource_policy", "32_bytes_per_CP95_CONFORMANCE_scheduled_attempt_but_retry_occurrence_not_frozen", "global_restart_blocker"),
        Operation("global.output_file_header_serializations", "global", "serialization", "record_serializations", "N_output_files", "unresolved", "container_choice", "file_partition_count_and_container_not_frozen", "global_serialization_blocker"),
        Operation("global.output_file_content_digest_calls", "global", "serialization", "sha256_calls", "N_output_files", "unresolved", "container_choice", "hash_exact_file_bytes_with_the_content_digest_slot_canonical_zero;file_partition_count_not_frozen", "global_identity_blocker"),
        Operation("global.output_file_record_count_reductions", "global", "serialization", "count_reductions", "N_output_files", "unresolved", "container_choice", "one_exact_record_count_per_output_file_but_file_partition_count_not_frozen", "global_serialization_blocker"),
        Operation("global.output_file_byte_count_reductions", "global", "serialization", "count_reductions", "N_output_files", "unresolved", "container_choice", "one_exact_uncompressed_byte_count_per_output_file_but_file_partition_count_not_frozen", "global_serialization_blocker"),
        Operation("global.software_lock_digest_calls", "global", "static_identity", "sha256_calls", "N_software_lock_payloads", "unresolved", "software_lock_choice", "software_environment_payload_and_deduplication_not_frozen", "global_identity_blocker"),
        Operation("global.algorithm_lock_digest_calls", "global", "static_identity", "sha256_calls", "N_algorithm_lock_payloads", "unresolved", "algorithm_lock_choice", "reference_algorithm_payload_and_deduplication_not_frozen", "global_identity_blocker"),
        Operation("global.family_record_serializations", "global", "family", "record_serializations", "2", "exact", "all", "one_reliability_and_one_mv1_family_record", "global_once"),
        Operation("global.family_execution_attempt_records", "global", "restart", "record_serializations", "unresolved", "unresolved", "resource_policy", "32_byte_execution_sidecar_records_for_REL_FAMILY_and_MV_FAMILY_scheduled_attempts_only;disjoint_from_per_kind_static_calibration_outer_and_cell_aggregate_attempts", "global_restart_blocker"),
        Operation("global.family_execution_attempt_record_bytes", "global", "restart", "bytes", "unresolved", "unresolved", "resource_policy", "32_bytes_per_family_work_unit_attempt_but_retry_occurrence_not_frozen", "global_restart_blocker"),
        Operation("rel.family_member_status_checks", "global", "family", "member_status_checks", "10847", "exact", "all", "all_reliability_manifest_candidates_including_static_scientific_or_infrastructure_failures", "shared_family_classification_for_candidate_complete_count_and_failure_inventory"),
        Operation("rel.family_status_inventory_appends", "global", "family", "inventory_appends", "10847", "upper_bound", "all", "total_appends_across_two_unique_disjoint_inventories:conclusive_static_or_required_criterion_failure_versus_no_conclusive_failure_with_infrastructure_missingness;at_most_one_append_per_candidate", "shared_disjoint_inventory_bound"),
        Operation("rel.family_coverage_check_evaluations", "global", "family", "check_evaluations", "10847", "exact", "all", "each_candidate_contributes_coverage_pass_or_static_failure_record", "standalone_family_reduction"),
        Operation("rel.family_false_promotion_check_evaluations", "global", "family", "check_evaluations", "10847", "upper_bound", "final_null_or_boundary_members", "inclusive_membership_uses_any_final_truth_at_or_below_its_declared_null_threshold;membership_count_waits_for_selected_final_truth_but_no_candidate_may_be_silently_deleted", "standalone_family_reduction"),
        Operation("rel.family_planning_power_check_evaluations", "global", "family", "check_evaluations", "4416", "exact", "planning_members", "all_4416_manifest_planning_members_or_their_static_failure_records", "standalone_family_reduction"),
        Operation("rel.family_axis_min_argmin_comparisons", "global", "family", "ordered_comparisons", "4401", "upper_bound", "complete_family_path", f"axis_array_order={RELIABILITY_AXIS_ORDER_TOKEN};within_each_axis_scan_all_planning_members_by_ascending_combined_catalogue_index;compare_candidate_lower_strictly_less_than_running_minimum_and_never_update_on_exact_binary64_equality_so_smallest_tied_index_is_retained;sum_over_15_axes_of_members_in_axis_minus_1", "shared_comparison_for_minimum_and_argmin_outputs"),
        Operation("rel.family_union_failure_complements", "global", "family", "one_minus_events", "15", "upper_bound", "complete_family_path", "one_1_minus_L_g_min_complement_per_axis_before_fixed_order_sum"),
        Operation("rel.family_union_failure_additions", "global", "family", "fixed_order_additions", "14", "upper_bound", "complete_family_path", f"left_associative_sum_of_fifteen_axis_terms_in_order={RELIABILITY_AXIS_ORDER_TOKEN}", "standalone_family_reduction"),
        Operation("rel.family_union_threshold_comparisons", "global", "family", "inclusive_threshold_comparisons", "1", "upper_bound", "complete_family_path", "compare_fixed_order_union_failure_sum<=0.10"),
        Operation("rel.family_decision_evaluations", "global", "family", "decision_evaluations", "1", "exact", "all", "pass_fail_or_incomplete_after_member_accounting", "global_once"),
        Operation("mv.family_candidate_status_checks", "global", "family", "member_status_checks", "2438", "exact", "all", "all_precalibration_manifest_candidates", "shared_family_classification_for_candidate_failure_and_missing_counts"),
        Operation("mv.family_status_inventory_appends", "global", "family", "inventory_appends", "2438", "upper_bound", "all", "total_appends_across_three_unique_disjoint_inventories:preouter_calibration_or_static_failure_outer_eligible_outer_or_criterion_failure_or_no_conclusive_failure_with_infrastructure_missingness;at_most_one_append_per_candidate", "shared_disjoint_inventory_bound"),
        Operation("mv.family_null_upper_check_evaluations", "global", "family", "check_evaluations", "108", "exact", "all", "every_immutable_manifest_null_member_contributes_VALUE_or_NOT_REACHED_audit_outcome", "standalone_family_reduction"),
        Operation("mv.family_coverage_check_evaluations", "global", "family", "check_evaluations", "2438", "exact", "all", "every_candidate_contributes_VALUE_or_NOT_REACHED_coverage_audit_outcome", "standalone_family_reduction"),
        Operation("mv.family_planning_power_check_evaluations", "global", "family", "check_evaluations", "2304", "exact", "planning_members", "all_2304_manifest_members_or_their_failure_records", "standalone_family_reduction"),
        Operation("mv.family_decision_evaluations", "global", "family", "decision_evaluations", "1", "exact", "all", "pass_fail_or_incomplete_after_member_accounting", "global_once"),
        Operation("global.family_record_bytes", "global", "family", "bytes", "unresolved", "unresolved", "owner_choice", "typed_minima_inventory_and_decision_widths_not_frozen", "global_storage_blocker"),
        Operation("global.container_header_bytes", "global", "serialization", "bytes", "unresolved", "unresolved", "implementation_choice", "file_container_and_identifier_or_permutation_dictionary_headers_not_frozen;excludes_the_four_named_registry_dictionary_records", "global_storage_blocker"),
        Operation("global.replay_conformance_checks", "global", "conformance", "checks", "unresolved", "unresolved", "post_gate_reference_choice", "sentinel_set_and_checkpoint_depth_not_frozen", "global_conformance_blocker"),
        Operation("global.io_bytes", "global", "io", "bytes", "unresolved", "unresolved", "implementation_and_retention_choice", "read_write_checkpoint_retry_and_readback_bytes_not_frozen", "global_resource_blocker"),
        Operation("global.redundancy_backup_bytes", "global", "retention", "bytes", "unresolved", "unresolved", "governance_and_resource_choice", "redundancy_backup_and_retention_policy_not_frozen", "global_storage_blocker"),
        Operation("global.restart_scheduler_events", "global", "restart", "events", "unresolved", "unresolved", "resource_choice", "chunk_retry_queue_and_scheduler_policy_not_frozen", "global_resource_blocker"),
        Operation("global.peak_ram_bytes", "global", "resource", "bytes", "unresolved", "unresolved", "implementation_and_worker_choice", "worker_system_and_shared_peak_RAM_not_measured_or_bounded", "global_resource_blocker"),
        Operation("global.scratch_bytes", "global", "resource", "bytes", "unresolved", "unresolved", "implementation_and_checkpoint_choice", "temporary_calibration_bootstrap_sort_and_checkpoint_storage_not_bounded", "global_resource_blocker"),
        Operation("global.worker_process_allocation", "global", "resource", "workers_and_processes", "unresolved", "unresolved", "resource_owner_choice", "hardware_worker_thread_affinity_and_concurrency_not_allocated", "global_resource_blocker"),
        Operation("global.runtime_seconds", "global", "resource", "seconds", "unresolved", "unresolved", "future_authorized_benchmark", "no_runtime_or_throughput_measurement_exists", "global_resource_blocker"),
        Operation("global.contingency_capacity", "global", "resource", "bytes_and_seconds", "unresolved", "unresolved", "resource_and_governance_choice", "retry_failure_redundancy_and_capacity_margin_not_frozen", "global_resource_blocker"),
        Operation("global.compression_work_and_bytes", "global", "serialization", "events_and_bytes", "unresolved", "unresolved", "optional_complete_alternative", "compressor_roundtrip_and_worst_case_expansion_not_frozen", "exclusive_optional_alternative"),
        Operation("rel.outer_records", "reliability", "outer", "records", "M_c", "exact", "all", "M_c_is_unique_integrity_valid_committed_outer_identity_count_between_0_and_R;I_complete_iff_M_c=R_and_no_integrity_mismatch", "shape_denominator_do_not_allocate_as_compute"),
        Operation("rel.dgp_words_lower", "reliability", "outer_dgp", "uint64_words", "R*(N+2*A)", "lower_bound", "rel_dgp_envelope", "planned_complete_path_I_complete=1;discarded_retry_work_is_separate;first_ratings_only", "envelope_lower_do_not_sum_with_upper_or_components"),
        Operation("rel.dgp_words_upper", "reliability", "outer_dgp", "uint64_words", "R*(N+2*A+N+3*Dmax)", "upper_bound", "rel_dgp_envelope", "planned_complete_path_I_complete=1;all_items_receive_ambiguity_word;all_instrument_repeats_consumed", "envelope_upper_do_not_sum_with_lower_or_components"),
        Operation("rel.open_unit_conversions_lower", "reliability", "outer_dgp", "uint64_to_open_unit", "R*(N+2*A)", "lower_bound", "rel_conversion_envelope", "planned_complete_path_I_complete=1;matches_lower_raw_word_path", "envelope_lower_do_not_sum_with_upper"),
        Operation("rel.open_unit_conversions_upper", "reliability", "outer_dgp", "uint64_to_open_unit", "R*(N+2*A+N+3*Dmax)", "upper_bound", "rel_conversion_envelope", "planned_complete_path_I_complete=1;matches_upper_raw_word_path", "envelope_upper_do_not_sum_with_lower"),
        Operation("rel.item_inverse_normal", "reliability", "outer_dgp", "inverse_normal_calls", "R*N", "exact", "planned_complete_path_I_complete=1", "one_item_effect_per_item_and_scheduled_outer"),
        Operation("rel.first_rating_softmax", "reliability", "outer_dgp", "softmax_vectors", "R*A", "exact", "planned_complete_path_I_complete=1", "one_first_rating_probability_vector_per_assignment_and_scheduled_outer", "composite_softmax_alternative_do_not_sum_with_primitive_components"),
        Operation("rel.first_rating_softmax_exp_calls", "reliability", "outer_dgp", "exp_calls", "R*A*K", "exact", "primitive_softmax_complete_path", "K_exponentials_per_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("rel.first_rating_softmax_normalizations", "reliability", "outer_dgp", "probability_normalizations", "R*A", "exact", "primitive_softmax_complete_path", "one_normalization_per_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("rel.first_rating_softmax_logsumexp_calls", "reliability", "outer_dgp", "logsumexp_calls", "R*A", "upper_bound", "optional_reference_softmax_complete_path", "zero_if_direct_stable_normalization_is_frozen", "optional_primitive_subalternative_do_not_add_without_reference_lock"),
        Operation("rel.first_rating_lookup", "reliability", "outer_dgp", "categorical_lookups", "R*A", "exact", "planned_complete_path_I_complete=1", "one_first_rating_lookup_per_assignment_and_scheduled_outer"),
        Operation("rel.missingness_lookup", "reliability", "outer_dgp", "bernoulli_lookups", "R*A", "exact", "planned_complete_path_I_complete=1", "one_missingness_lookup_per_first_assignment_and_scheduled_outer"),
        Operation("rel.baseline_log_values", "reliability", "static_probability", "log_calls", "K*K", "exact", "all", "one_frozen_baseline_logit_matrix_per_cell"),
        Operation("rel.ambiguity_draws_lower", "reliability", "outer_dgp", "draw_events", "0", "lower_bound", "all", "ambiguity_domain_not_frozen"),
        Operation("rel.ambiguity_draws_upper", "reliability", "outer_dgp", "draw_events", "R*N", "upper_bound", "planned_complete_path_I_complete=1", "all_axis_items_receive_ambiguity_draw"),
        Operation("rel.ambiguity_interpretation_lookups_upper", "reliability", "outer_dgp", "bernoulli_lookups", "R*N", "upper_bound", "planned_complete_path_I_complete=1", "all_axis_items_receive_interpretation_lookup"),
        Operation("rel.repeat_events_lower", "reliability", "outer_dgp", "repeat_events", "0", "lower_bound", "all", "included_repeat_domain_not_frozen", "shape_denominator_do_not_allocate_as_compute"),
        Operation("rel.repeat_events_upper", "reliability", "outer_dgp", "repeat_events", "R*Dmax", "upper_bound", "planned_complete_path_I_complete=1", "all_instrument_repeat_ratings_included", "shape_denominator_do_not_allocate_as_compute"),
        Operation("rel.repeat_words_lower", "reliability", "outer_dgp", "uint64_words", "0", "lower_bound", "rel_dgp_component", "included_repeat_domain_not_frozen", "diagnostic_component_of_rel_dgp_envelope_do_not_add"),
        Operation("rel.repeat_words_upper", "reliability", "outer_dgp", "uint64_words", "3*R*Dmax", "upper_bound", "rel_dgp_component_complete_path", "three_words_per_instrument_repeat", "diagnostic_component_of_rel_dgp_envelope_do_not_add"),
        Operation("rel.repeat_match_lookups_upper", "reliability", "outer_dgp", "bernoulli_lookups", "R*Dmax", "upper_bound", "planned_complete_path_I_complete=1", "all_instrument_repeats_reach_match_lookup"),
        Operation("rel.repeat_alternate_normalizations_upper", "reliability", "outer_dgp", "probability_normalizations", "R*Dmax", "upper_bound", "planned_complete_path_I_complete=1", "one_zero_mass_renormalization_per_nonmatching_recorded_repeat_at_most"),
        Operation("rel.repeat_categorical_lookups_upper", "reliability", "outer_dgp", "categorical_lookups", "R*Dmax", "upper_bound", "planned_complete_path_I_complete=1", "alternate_word_consumed_for_every_instrument_repeat"),
        Operation("rel.repeat_missingness_lookups_upper", "reliability", "outer_dgp", "bernoulli_lookups", "R*Dmax", "upper_bound", "planned_complete_path_I_complete=1", "one_repeat_missingness_lookup_per_instrument_repeat"),
        Operation("rel.bootstrap_index_words", "reliability", "bootstrap", "uint64_words", "R*B*N", "exact", "planned_complete_path_I_complete=1", "fixed_cluster_resamples;all_B_consumed"),
        Operation("rel.bootstrap_index_formations", "reliability", "bootstrap", "index_formations", "R*B*N", "exact", "planned_complete_path_I_complete=1", "one_index_formation_per_word"),
        Operation("rel.statistic_recomputations", "reliability", "analysis", "statistic_recomputations", "R*(B+1)", "exact", "planned_complete_path_I_complete=1", "point_plus_all_bootstrap_alpha_recomputations"),
        Operation("rel.percentile_selections", "reliability", "analysis", "order_selections", "R", "upper_bound", "planned_complete_path_I_complete=1", "no_order_statistic_if_any_bootstrap_alpha_is_undefined"),
        Operation("rel.outer_point_descriptive_reductions", "reliability", "analysis", "point_descriptive_reduction_assemblies", "M_c", "exact", "all", "one_per_unique_integrity_valid_committed_outer_record;computes_macro_agreement_K_applicable_positive_agreements_K_applicable_prevalences_overall_missingness_and_reader_and_presentation_arm_minima_maxima_and_spans;excludes_alpha_point_or_bootstrap_recomputation_and_classification", "composite_point_output_reduction"),
        Operation("rel.outer_classification_assemblies", "reliability", "analysis", "state_event_failure_status_assemblies", "M_c", "exact", "composite_outer_classification", "one_per_committed_outer_record;includes_all_applicable_finite_denominator_threshold_coverage_allocation_missingness_and_bootstrap_undefined_comparisons_two_bit_slot_states_event_bits_failure_component_mask_and_primary_status_precedence;excludes_estimator_computation_aggregate_tally_and_serialization", "composite_control_classification_do_not_add_future_granular_comparison_or_mask_rows"),
        Operation("rel.missing_endpoint_residual_evaluations", "reliability", "static_truth", "residual_evaluations", "2_or_0", "exact", "nonzero_reader_or_class_mode", "two_frozen_endpoints_before_any_midpoint;the_signed_residual_direction_and_nonfinite_semantics_are_owner_blocked", "diagnostic_component_of_total_residual_evaluations_do_not_add"),
        Operation("rel.missing_bracket_checks", "reliability", "static_truth", "bracket_check_and_state_emission", "1_or_0", "exact", "nonzero_reader_or_class_mode", "one_endpoint_sign_bracket_check_is_scheduled_for_each_required_solve;the_signed_residual_direction_inclusive_endpoint_zero_predicate_and_nonfinite_semantics_are_owner_blocked_so_required_pass_or_fail_state_remains_NOT_REACHED_until_frozen;not_required_for_m=0_or_MCAR_is_assembled_by_static_classification"),
        Operation("rel.missing_midpoint_controls", "reliability", "static_truth", "bisection_midpoint_and_cache_update_events", "100_or_0", "upper_bound", "nonzero_reader_or_class_mode", "zero_if_the_owner_frozen_endpoint_bracket_fails;otherwise_at_most_100_midpoint_evaluations_and_retained_bracket_cache_updates;midpoint_residual_zero_equality_endpoint_replacement_update_and_post_100_final_candidate_selection_rules_remain_owner_blocked"),
        Operation("rel.missing_residual_evaluations", "reliability", "static_truth", "residual_evaluations", "102_or_0", "upper_bound", "nonzero_reader_or_class_mode", "two_endpoints_plus_at_most_100_midpoints;the_signed_residual_direction_inclusive_bracket_predicate_midpoint_equality_and_endpoint_update_rules_are_owner_blocked"),
        Operation("rel.missing_final_candidate_selection_events", "reliability", "static_truth", "final_cached_candidate_selection_events", "1_or_0", "upper_bound", "missingness_bisection_owner_choice", "at_most_one_for_each_nonzero_reader_or_class_missingness_cell_after_an_owner_frozen_passing_bracket_and_100_midpoint_updates;selects_one_cached_intercept_and_paired_signed_residual;the_residual_sign_bracket_predicate_midpoint_equality_update_endpoint_or_midpoint_candidate_choice_and_tie_rule_are_not_frozen", "standalone_final_missingness_selection_blocker"),
        Operation("rel.missing_expit_constructions", "reliability", "static_truth", "expit_calls", "102*A_or_0", "upper_bound", "nonzero_reader_or_class_mode", "two_endpoints_plus_at_most_100_midpoints", "composite_expit_alternative_do_not_sum_with_primitive_exp"),
        Operation("rel.missing_expit_exp_calls", "reliability", "static_truth", "exp_calls", "102*A_or_0", "upper_bound", "primitive_expit_path", "one_exponential_per_expit_evaluation", "primitive_expit_alternative_do_not_sum_with_composite"),
        Operation("rel.quadrature_node_reductions", "reliability", "static_truth", "node_truth_reduction_assemblies", "I_missing*(41+61)", "conditional_exact", "all", "I_missing=1_for_no_solve_or_successful_missingness_solve;each_node_performs_fixed_order_weighted_accumulator_updates_for_integrated_alpha_macro_agreement_and_all_K_applicable_positive_agreements_and_the_last_node_emits_that_orders_final_truth_values;41_and_61_orders_are_separate", "composite_truth_output_reduction_do_not_add_future_per_metric_accumulator_rows"),
        Operation("rel.quadrature_probability_constructions", "reliability", "static_truth", "softmax_vectors", "I_missing*102*A", "conditional_exact", "all", "I_missing=1_for_no_solve_or_successful_missingness_solve;both_declared_orders", "composite_softmax_alternative_do_not_sum_with_primitive_components"),
        Operation("rel.quadrature_softmax_exp_calls", "reliability", "static_truth", "exp_calls", "I_missing*102*A*K", "conditional_exact", "primitive_softmax_path", "K_exponentials_per_assignment_weighted_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("rel.quadrature_softmax_normalizations", "reliability", "static_truth", "probability_normalizations", "I_missing*102*A", "conditional_exact", "primitive_softmax_path", "one_normalization_per_assignment_weighted_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("rel.quadrature_softmax_logsumexp_calls", "reliability", "static_truth", "logsumexp_calls", "I_missing*102*A", "conditional_upper_bound", "optional_reference_softmax_path", "zero_if_direct_stable_normalization_is_frozen", "optional_primitive_subalternative_do_not_add_without_reference_lock"),
        Operation("rel.reader_effect_inverse_normal", "reliability", "static_truth", "inverse_normal_calls", "roster*K", "exact", "all", "frozen_roster_and_axis_categories"),
        Operation("rel.reader_effect_vector_normalizations", "reliability", "static_truth", "finite_roster_normalizations", "K", "exact", "all", "one_mean_population_SD_normalization_per_category_vector"),
        Operation("rel.missing_reader_effect_inverse_normal", "reliability", "static_truth", "inverse_normal_calls", "roster_or_0", "exact", "nonzero_reader_missingness_only", "separate_tagged_reader_permutation"),
        Operation("rel.missing_reader_vector_normalizations", "reliability", "static_truth", "finite_roster_normalizations", "1_or_0", "exact", "nonzero_reader_missingness_only", "one_mean_population_SD_normalization"),
        Operation("rel.truth_reference_selection_events", "reliability", "static_classification", "truth_reference_selection_events", "unresolved", "unresolved", "truth_reference_owner_choice", "41_vs_61_or_other_prospective_selection_rule_and_per_component_behavior_not_frozen"),
        Operation("rel.static_classification_assemblies", "reliability", "static_classification", "static_state_failure_classification_assemblies", "1", "exact", "composite_static_classification", "one_per_manifest_candidate;includes_reached_41_61_delta_construction_1e-6_checks_four_fixed_class_slot_states_missingness_bracket_state_and_iteration_count_assembly_from_realized_controls_owner_blocked_final_intercept_residual_and_truth_states_required_missingness_solve_pass_iff_bracket_and_selection_are_reached_finite_and_abs_selected_signed_residual_less_than_or_equal_to_1e-10_with_finite_above_tolerance_residual_retained_as_VALUE_but_static_failure_and_I_R3=0_null_boundary_class_ALTERNATIVE_iff_alpha>0.67_macro>0.80_and_all_applicable_positive>0.70_BOUNDARY_iff_none_below_and_any_exactly_equal_else_NULL_if_any_below_using_exact_binary64_values_planning_truth_eligibility_true_iff_manifest_planning_member_and_alpha>0.80_macro>0.85_and_all_applicable_positive>0.75_else_false_for_finite_required_truths_I_R3_requires_true_for_planning_member_and_first_static_failure_precedence;excludes_numerical_bisection_quadrature_final_candidate_selection_and_owner_truth_selection_work", "composite_control_classification_do_not_add_future_granular_static_state_or_comparison_rows"),
        Operation("rel.aggregate_interval_calls_lower", "reliability", "aggregate", "exact_binomial_intervals", "I_complete*(11+K+I_planning)", "lower_bound", "rel_interval_envelope", "I_complete=1_required;false_promotion_applicability_requires_final_truth", "composite_interval_envelope_lower_do_not_sum_with_upper_or_primitive_quantiles"),
        Operation("rel.aggregate_interval_calls_upper", "reliability", "aggregate", "exact_binomial_intervals", "I_complete*(12+K+I_planning)", "upper_bound", "rel_interval_envelope", "I_complete=1_required;includes_possible_false_promotion_interval", "composite_interval_envelope_upper_do_not_sum_with_lower_or_primitive_quantiles"),
        Operation("rel.aggregate_beta_quantile_calls_upper", "reliability", "aggregate", "beta_quantile_calls", "I_complete*(2*(11+K)+I_planning+I_false)", "upper_bound", "primitive_exact_binomial_path", "I_complete=1_required;two_quantiles_per_two_sided_interval_and_one_per_one_sided_planning_or_applicable_false_promotion_interval;boundary_success_counts_can_reduce_realized_calls", "primitive_interval_alternative_do_not_sum_with_composite_interval_calls"),
        Operation("rel.aggregate_completion_identity_checks", "reliability", "aggregate", "bitmap_and_record_identity_checks", "R", "exact", "all", "one_expected_outer_identity_check_against_completion_bitmap_unique_canonical_record_and_integrity_digest;I_complete_requires_all_R"),
        Operation("rel.aggregate_base_counter_updates", "reliability", "aggregate", "boolean_counter_updates", "I_complete*R*(11+K)", "exact", "all", "I_complete=1_required_after_full_identity_scan;eleven_plus_K_unique_base_Bernoulli_counters;complete_gate_counter_is_reused_by_false_promotion_and_planning_without_second_tally", "shared_base_counter_tally"),
        Operation("rel.aggregate_undefined_bootstrap_sum_additions", "reliability", "aggregate", "integer_accumulations", "I_complete*R", "exact", "all", "I_complete=1_required_after_full_identity_scan;one_undefined_bootstrap_count_addition_per_committed_outer_record_for_descriptive_sum"),
        Operation("rel.aggregate_proportion_evaluations", "reliability", "aggregate", "binary64_divisions", "I_complete*(11+K)", "exact", "all", "I_complete=1_required;one_x_divided_by_fixed_R_for_each_distinct_base_event_proportion;complete_gate_proportion_is_reused_by_false_promotion_and_planning_outputs_without_an_extra_division", "shared_distinct_proportion_evaluations"),
        Operation("rel.aggregate_undefined_bootstrap_fraction_divisions", "reliability", "aggregate", "binary64_divisions", "I_complete", "exact", "all", "I_complete=1_required;one_sum_undefined_divided_by_fixed_R_times_B_for_the_descriptive_fraction;disjoint_from_binary_event_proportions_and_CP_intervals", "standalone_descriptive_fraction"),
        Operation("rel.aggregate_record_classification_assemblies", "reliability", "aggregate_audit", "aggregate_state_applicability_status_assemblies", "1", "exact", "composite_aggregate_classification", "one_per_manifest_candidate_even_when_I_R3=0_or_I_complete=0;assembles_all_structural_applicability_NOT_REACHED_VALUE_trials_interval_and_cell_status_fields_from_frozen_static_completion_integrity_and_numerical_outputs;excludes_tallies_proportion_evaluations_undefined_fraction_division_intervals_and_serialization", "composite_control_classification_do_not_add_future_granular_aggregate_state_rows"),
        Operation("rel.repeat_metric_evaluations", "reliability", "analysis", "metric_evaluations", "unresolved", "unresolved", "owner_choice", "repeat_estimators_not_frozen"),
        Operation("rel.outer_seed_derivations", "reliability", "outer_identity", "hmac_seed_derivations", "2*R", "exact", "planned_complete_path_I_complete=1", "one_outer_DGP_and_one_analysis_bootstrap_seed_per_scheduled_identity;discarded_retry_derivations_are_in_unresolved_attempt_work"),
        Operation("rel.outer_payload_hashes", "reliability", "serialization", "sha256_calls", "M_c", "exact", "all", "one_hash_per_committed_exact_336_byte_canonical_scientific_record_with_digest_slot_zero;mutable_execution_sidecar_excluded"),
        Operation("rel.outer_record_serializations", "reliability", "serialization", "record_serializations", "M_c", "exact", "all", "one_336_byte_record_per_unique_integrity_valid_committed_outer_identity"),
        Operation("rel.outer_record_bytes", "reliability", "serialization", "bytes", "336*M_c", "exact", "all", "fixed_TB0011_core_width_times_committed_record_count"),
        Operation("rel.completion_bitmap_updates", "reliability", "checkpoint", "bit_updates", "M_c", "exact", "all", "one_final_completion_bit_update_per_unique_integrity_valid_committed_outer_identity"),
        Operation("rel.chunk_journal_records", "reliability", "checkpoint", "record_serializations", "unresolved", "unresolved", "chunk_policy", "chunk_size_retry_and_commit_policy_not_frozen"),
        Operation("rel.failure_detail_records", "reliability", "failure_audit", "record_serializations", "unresolved", "unresolved", "realized_failures", "failure_message_taxonomy_and_realized_failures_not_frozen"),
        Operation("rel.execution_attempt_records", "reliability", "restart", "record_serializations", "unresolved", "unresolved", "resource_policy", "one_32_byte_sidecar_record_per_scheduled_REL_STATIC_REL_OUTER_RANGE_or_reliability_CELL_AGGREGATE_attempt;disjoint_from_MV_and_global_family_work;chunking_deadline_retry_and_infrastructure_failure_process_not_frozen"),
        Operation("rel.execution_attempt_record_bytes", "reliability", "restart", "bytes", "unresolved", "unresolved", "resource_policy", "32_bytes_per_scheduled_atomic_work_unit_attempt_but_attempt_occurrence_not_frozen"),
        Operation("mv.outer_records", "mv1", "outer", "records", "M_c", "conditional_exact", "all", "M_c_is_unique_integrity_valid_committed_outer_identity_count_between_0_and_R;M_c=0_if_not_outer_eligible;I_complete_iff_M_c=R_and_no_integrity_mismatch", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.dgp_words", "mv1", "outer_dgp", "uint64_words", "R*(66*n+4*D)", "upper_bound", "all_candidates_calibrate", "D=10*ceil(0.3*n)"),
        Operation("mv.open_unit_conversions", "mv1", "outer_dgp", "uint64_to_open_unit", "R*(66*n+4*D)", "upper_bound", "all_candidates_calibrate", "one_conversion_per_raw_word"),
        Operation("mv.outer_first_presentation_events", "mv1", "outer_dgp", "presentation_events", "R*20*n", "upper_bound", "all_candidates_calibrate", "ten_readers_by_two_screen_strata", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.outer_repeat_events", "mv1", "outer_dgp", "repeat_events", "R*D", "upper_bound", "all_candidates_calibrate", "D=10*ceil(0.3*n)", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.outer_evaluability_block_reductions", "mv1", "outer_dgp", "eligibility_reductions", "R*2*n", "upper_bound", "all_candidates_calibrate", "one_complete_E_predicate_per_screened_candidate"),
        Operation("mv.outer_four_of_five_panel_reductions", "mv1", "outer_dgp", "panel_vote_reductions", "R*4*n", "upper_bound", "all_candidates_calibrate", "two_sibling_panels_per_screened_candidate"),
        Operation("mv.outer_panel_mean_reductions", "mv1", "outer_dgp", "panel_mean_reductions", "R*4*n", "upper_bound", "all_candidates_calibrate", "two_five_reader_panel_means_per_screened_candidate"),
        Operation("mv.outer_patient_q_reductions", "mv1", "outer_dgp", "patient_q_reductions", "R*2*n", "upper_bound", "all_candidates_calibrate", "one_q_value_per_evaluable_candidate_at_most"),
        Operation("mv.static_reader_effect_inverse_normal", "mv1", "static_probability", "inverse_normal_calls", "30", "exact", "all", "probability_coverage_and_state_vectors_each_have_ten_readers"),
        Operation("mv.static_reader_vector_normalizations", "mv1", "static_probability", "finite_roster_normalizations", "3", "exact", "all", "probability_coverage_and_state_vectors_each_get_mean_population_SD_normalization"),
        Operation("mv.static_state_log_values", "mv1", "static_probability", "log_calls", "3", "exact", "all", "correct_opposite_ambiguous_base_logits"),
        Operation("mv.outer_screen_fidelity_lookups", "mv1", "outer_dgp", "bernoulli_lookups", "R*2*n", "upper_bound", "all_candidates_calibrate", "one_assigned_state_lookup_per_screened_candidate"),
        Operation("mv.outer_q_beta_inverse", "mv1", "outer_dgp", "beta_inverse_calls", "R*2*n_or_0", "upper_bound", "beta_candidates_only", "zero_for_two_point_candidates"),
        Operation("mv.outer_q_two_point_lookup", "mv1", "outer_dgp", "two_point_lookups", "R*2*n_or_0", "upper_bound", "two_point_candidates_only", "zero_for_beta_candidates"),
        Operation("mv.outer_patient_normal_inverse", "mv1", "outer_dgp", "inverse_normal_calls", "R*2*n", "upper_bound", "all_candidates_calibrate", "one_shared_patient_state_effect_per_candidate"),
        Operation("mv.outer_rating_normal_inverse", "mv1", "outer_dgp", "inverse_normal_calls", "R*20*n", "upper_bound", "all_candidates_calibrate", "one_probability_noise_transform_per_first_presentation"),
        Operation("mv.outer_coverage_expit", "mv1", "outer_dgp", "expit_calls", "R*20*n", "upper_bound", "all_candidates_calibrate", "one_coverage_probability_per_first_presentation", "composite_expit_alternative_do_not_sum_with_primitive_exp"),
        Operation("mv.outer_coverage_exp_calls", "mv1", "outer_dgp", "exp_calls", "R*20*n", "upper_bound", "primitive_expit_path", "one_exponential_per_coverage_expit", "primitive_expit_alternative_do_not_sum_with_composite"),
        Operation("mv.outer_coverage_lookup", "mv1", "outer_dgp", "bernoulli_lookups", "R*20*n", "upper_bound", "all_candidates_calibrate", "coverage_word_consumed_for_every_first_presentation"),
        Operation("mv.outer_state_softmax", "mv1", "outer_dgp", "softmax_vectors", "R*20*n", "upper_bound", "all_candidates_calibrate", "one_state_probability_vector_per_first_presentation", "composite_softmax_alternative_do_not_sum_with_primitive_components"),
        Operation("mv.outer_state_softmax_exp_calls", "mv1", "outer_dgp", "exp_calls", "3*R*20*n", "upper_bound", "primitive_softmax_path", "three_exponentials_per_state_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.outer_state_softmax_normalizations", "mv1", "outer_dgp", "probability_normalizations", "R*20*n", "upper_bound", "primitive_softmax_path", "one_normalization_per_state_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.outer_state_softmax_logsumexp_calls", "mv1", "outer_dgp", "logsumexp_calls", "R*20*n", "upper_bound", "optional_reference_softmax_path", "zero_if_direct_stable_normalization_is_frozen", "optional_primitive_subalternative_do_not_add_without_reference_lock"),
        Operation("mv.outer_state_lookup", "mv1", "outer_dgp", "categorical_lookups", "R*20*n", "upper_bound", "all_candidates_calibrate", "state_word_consumed_for_every_first_presentation"),
        Operation("mv.outer_clip_round", "mv1", "outer_dgp", "clip_round_events", "R*20*n", "upper_bound", "all_candidates_calibrate", "one_probability_clip_round_per_recorded_first_presentation_at_most"),
        Operation("mv.repeat_rating_normal_inverse", "mv1", "outer_dgp", "inverse_normal_calls", "R*D", "upper_bound", "all_candidates_calibrate", "fresh_probability_noise_per_repeat"),
        Operation("mv.repeat_coverage_expit", "mv1", "outer_dgp", "expit_calls", "R*D", "upper_bound", "all_candidates_calibrate", "one_coverage_probability_per_repeat", "composite_expit_alternative_do_not_sum_with_primitive_exp"),
        Operation("mv.repeat_coverage_exp_calls", "mv1", "outer_dgp", "exp_calls", "R*D", "upper_bound", "primitive_expit_path", "one_exponential_per_coverage_expit", "primitive_expit_alternative_do_not_sum_with_composite"),
        Operation("mv.repeat_coverage_lookup", "mv1", "outer_dgp", "bernoulli_lookups", "R*D", "upper_bound", "all_candidates_calibrate", "coverage_word_consumed_for_every_repeat"),
        Operation("mv.repeat_state_softmax", "mv1", "outer_dgp", "softmax_vectors", "R*D", "upper_bound", "all_candidates_calibrate", "one_original_state_probability_vector_per_repeat", "composite_softmax_alternative_do_not_sum_with_primitive_components"),
        Operation("mv.repeat_state_softmax_exp_calls", "mv1", "outer_dgp", "exp_calls", "3*R*D", "upper_bound", "primitive_softmax_path", "three_exponentials_per_state_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.repeat_state_softmax_normalizations", "mv1", "outer_dgp", "probability_normalizations", "R*D", "upper_bound", "primitive_softmax_path", "one_normalization_per_state_probability_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.repeat_state_softmax_logsumexp_calls", "mv1", "outer_dgp", "logsumexp_calls", "R*D", "upper_bound", "optional_reference_softmax_path", "zero_if_direct_stable_normalization_is_frozen", "optional_primitive_subalternative_do_not_add_without_reference_lock"),
        Operation("mv.repeat_match_lookup", "mv1", "outer_dgp", "bernoulli_lookups", "R*D", "upper_bound", "all_candidates_calibrate", "match_word_consumed_for_every_repeat"),
        Operation("mv.repeat_alternate_normalization", "mv1", "outer_dgp", "probability_normalizations", "R*D", "upper_bound", "all_candidates_calibrate", "one_zero_mass_renormalization_per_nonmatching_recorded_repeat_at_most"),
        Operation("mv.repeat_state_lookup", "mv1", "outer_dgp", "categorical_lookups", "R*D", "upper_bound", "all_candidates_calibrate", "alternate_word_consumed_for_every_repeat"),
        Operation("mv.repeat_clip_round", "mv1", "outer_dgp", "clip_round_events", "R*D", "upper_bound", "all_candidates_calibrate", "one_probability_clip_round_per_recorded_repeat_at_most"),
        Operation("mv.bootstrap_index_words", "mv1", "bootstrap", "uint64_words", "R*B*2*n", "upper_bound", "all_candidates_calibrate_and_all_units_evaluable", "realized_evaluable_total_is_at_most_2*n"),
        Operation("mv.bootstrap_index_formations", "mv1", "bootstrap", "index_formations", "R*B*2*n", "upper_bound", "all_candidates_calibrate_and_all_units_evaluable", "one_index_formation_per_word"),
        Operation("mv.q_recomputations", "mv1", "analysis", "q_studentizer_recomputations", "R*(B+1)", "upper_bound", "all_candidates_calibrate_and_are_estimable", "point_plus_all_bootstrap_recomputations"),
        Operation("mv.max_t_selections", "mv1", "analysis", "max_t_selection_and_three_lower_bound_assemblies", "R", "upper_bound", "all_candidates_calibrate_and_are_estimable", "one_per_estimable_outer_selects_the_fixed_order_max_t_critical_value_and_inclusively_constructs_lower_bal_lower_present_and_lower_absent_as_qhat_minus_critical_times_SE;no_separate_lower_bound_construction_rows"),
        Operation("mv.fe_fits", "mv1", "sensitivity", "fixed_effect_fits", "R", "upper_bound", "all_candidates_calibrate_and_are_estimable", "one_joint_FE_fit_per_outer"),
        Operation("mv.loo_reductions", "mv1", "sensitivity", "leave_one_reader_reductions", "10*R", "upper_bound", "all_candidates_calibrate_and_are_estimable", "ten_reader_omissions_per_outer"),
        Operation("mv.outer_screen_assignment_tallies", "mv1", "analysis", "four_count_tally_assemblies", "M_c", "conditional_exact", "all", "one_per_unique_integrity_valid_committed_outer_record;computes_the_four_screen_stratum_by_assigned_polarity_counts;excludes_DGP_q_studentization_and_classification", "composite_point_output_tally"),
        Operation("mv.outer_classification_assemblies", "mv1", "analysis", "state_event_failure_status_assemblies", "M_c", "conditional_exact", "composite_outer_classification", "one_per_unique_integrity_valid_committed_outer_record;includes_all_applicable_finite_denominator_yield_q_strict_threshold_three_coverage_FE_rank_and_tolerance_all_30_LOO_veto_bootstrap_undefined_comparisons_two_bit_slot_states_event_bits_failure_component_mask_and_primary_status_precedence;excludes_estimator_computation_aggregate_tally_and_serialization", "composite_control_classification_do_not_add_future_granular_comparison_or_mask_rows"),
        Operation("mv.aggregate_interval_calls", "mv1", "aggregate", "exact_binomial_intervals", "I_outer*I_complete*(17+I_null+I_planning)", "conditional_upper_bound", "all_candidates_calibrate", "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0_and_I_complete=1_required;NOT_ELIGIBLE_and_INFRASTRUCTURE_INCOMPLETE_both_produce_no_interval_but_enter_distinct_family_failure_or_incomplete_inventories;applicability_and_denominators_require_calibration", "composite_interval_alternative_do_not_sum_with_primitive_quantiles"),
        Operation("mv.aggregate_beta_quantile_calls_upper", "mv1", "aggregate", "beta_quantile_calls", "I_outer*I_complete*(2*(17+I_planning)+I_null)", "conditional_upper_bound", "primitive_exact_binomial_path", "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0_and_I_complete=1_required;two_quantiles_per_two_sided_ordinary_or_planning_interval_and_one_per_one_sided_null_interval;boundary_success_counts_can_reduce_realized_calls", "primitive_interval_alternative_do_not_sum_with_composite_interval_calls"),
        Operation("mv.aggregate_completion_identity_checks", "mv1", "aggregate", "bitmap_and_record_identity_checks", "I_outer*R", "conditional_upper_bound", "all_candidates_calibrate", "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0;one_expected_outer_identity_check_against_completion_bitmap_unique_canonical_record_and_integrity_digest;I_complete_requires_all_R"),
        Operation("mv.aggregate_base_counter_updates", "mv1", "aggregate", "boolean_counter_updates", "I_outer*I_complete*17*R", "conditional_upper_bound", "all_candidates_calibrate", "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0_and_I_complete=1_required_after_full_identity_scan;seventeen_unique_base_Bernoulli_counters;complete_q_and_complete_joint_counters_are_reused_by_null_and_planning_without_second_tally", "shared_base_counter_tally"),
        Operation("mv.aggregate_proportion_evaluations", "mv1", "aggregate", "binary64_divisions", "I_outer*I_complete*17", "conditional_exact", "all", "I_outer=1_iff_outer_eligibility=ELIGIBLE_else_0_and_I_complete=1_required;one_x_divided_by_fixed_R_for_each_distinct_base_event_proportion;complete_q_proportion_is_reused_by_null_false_qualification_and_complete_joint_proportion_by_planning_power_without_extra_divisions", "shared_distinct_proportion_evaluations"),
        Operation("mv.aggregate_record_classification_assemblies", "mv1", "aggregate_audit", "aggregate_state_applicability_status_assemblies", "1", "exact", "composite_aggregate_classification", "one_per_manifest_candidate_even_when_calibration_or_outer_eligibility_fails_or_I_complete=0;assembles_all_manifest_membership_NOT_REACHED_VALUE_trials_interval_and_cell_status_fields_from_frozen_calibration_completion_integrity_and_numerical_outputs;excludes_tallies_proportion_evaluations_intervals_and_serialization", "composite_control_classification_do_not_add_future_granular_aggregate_state_rows"),
        Operation("mv.calibration_domain_bound_constructions", "mv1", "calibration_domain", "domain_bound_construction_assemblies", "I_domain*2", "conditional_exact", "all", "I_domain=1_only_after_owner_freezes_open_admissible_mean_interval_endpoint_or_interior_margin_and_strictly_positive_beta_shape_bound_rules;one_present_and_one_absent_polarity_assembly_each_computes_admissible_mean_lower_and_upper_and_for_beta_candidates_the_positive_shape_bound;two_point_candidates_mark_the_shape_bound_INAPPLICABLE;excludes_scan_solve_vector_evaluation_and_static_classification", "composite_static_domain_output_construction"),
        Operation("mv.calibration_candidate_vector_evaluations", "mv1", "calibration", "candidate_vector_evaluations", "2*(1001+80)*(80+2)*2^20", "upper_bound", "successful_calibration_path", "both_polarities_grid_and_outer_midpoint_inner_solve_evaluations_only;excludes_independent_validation_vectors", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.calibration_validation_vector_evaluations", "mv1", "calibration", "validation_vector_evaluations", "2*2^22", "upper_bound", "successful_calibration_path", "one_independent_validation_shape_per_polarity;excludes_candidate_solve_vectors", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.calibration_alpha_solves", "mv1", "calibration", "alpha_solves", "2*(1001+80)", "upper_bound", "successful_calibration_path", "per_polarity_grid_plus_outer_midpoints", "shape_denominator_do_not_allocate_as_compute"),
        Operation("mv.calibration_alpha_bracket_checks", "mv1", "calibration", "bracket_checks", "2*(1001+80)", "upper_bound", "successful_calibration_path", "one_endpoint_bracket_check_per_inner_alpha_solve;early_failure_reduces_realized_count;finite_sign_orientation_inclusive_endpoint_equality_and_residual_zero_semantics_are_owner_blocked"),
        Operation("mv.calibration_alpha_midpoint_controls", "mv1", "calibration", "bisection_midpoint_events", "2*(1001+80)*80", "upper_bound", "successful_calibration_path", "at_most_80_inner_alpha_midpoints_per_solve;endpoint_or_earlier_failure_reduces_realized_count;midpoint_residual_zero_and_bracket_endpoint_update_equality_rules_are_owner_blocked"),
        Operation("mv.calibration_residual_evaluations", "mv1", "calibration", "residual_evaluations", "2*(1001+80)*(80+2)", "upper_bound", "successful_calibration_path", "per_alpha_endpoint_and_midpoint_signed_yield_residual=estimated_P(E=1_given_Y)-rho_Y;all_evaluated_residuals_are_cached_but_one_is_selected_for_each_trial_mean_only_after_the_inner_alpha_rule_is_owner_frozen"),
        Operation("mv.calibration_inner_alpha_final_selections", "mv1", "calibration", "inner_alpha_cached_solution_selection_events", "2*(1001+80)", "upper_bound", "inner_alpha_owner_choice", "at_most_one_per_reached_trial_mean_after_two_endpoints_and_80_midpoint_updates;selects_one_cached_alpha_and_paired_signed_yield_residual_for_the_q_evaluation;inner_bracket_sign_orientation_inclusive_endpoint_predicate_midpoint_zero_update_and_endpoint_midpoint_tie_or_final_selection_rules_are_not_frozen", "standalone_inner_alpha_solution_blocker"),
        Operation("mv.calibration_scan_points", "mv1", "calibration", "scan_point_q_residual_evaluations", "2*1001", "upper_bound", "successful_calibration_path", "one_signed_q_residual=estimated_E(q_observed_given_E=1,Y)-q_Y_target_after_an_owner_frozen_paired_inner_alpha_selection_at_each_of_1001_points_per_polarity;cached_for_monotonicity_and_outer_bracket_controls"),
        Operation("mv.calibration_outer_q_bracket_checks", "mv1", "calibration", "bracket_checks", "2", "upper_bound", "successful_calibration_path", "one_outer_q_bracket_check_after_each_completed_polarity_scan;early_failure_reduces_realized_count;finite_sign_orientation_inclusive_endpoint_equality_and_residual_zero_semantics_are_owner_blocked"),
        Operation("mv.calibration_outer_midpoints", "mv1", "calibration", "outer_bisection_midpoint_q_residual_evaluations", "2*80", "upper_bound", "successful_calibration_path", "one_signed_q_residual=estimated_E(q_observed_given_E=1,Y)-q_Y_target_after_an_owner_frozen_paired_inner_alpha_selection_per_midpoint;the_updated_outer_endpoint_candidates_and_paired_alpha_yield_and_q_residuals_are_cached_but_outer_midpoint_zero_update_and_final_selection_rules_remain_owner_blocked"),
        Operation("mv.calibration_monotonicity_comparisons", "mv1", "calibration", "adjacent_difference_test_and_running_argmax_updates", "2*1000", "upper_bound", "successful_calibration_path", "after_owner_frozen_inner_alpha_selections_for_i=0_to_999_compute_raw_selected_q_i_minus_selected_q_i_plus_1_without_zero_clamping_apply_strict_greater_than_1e-6_test_and_update_fixed_ascending_scan_running_max_and_zero_based_preceding_index_argmax_with_smallest_i_tie_break_even_if_all_differences_are_nonpositive;final_max_and_index_are_reused_by_static_outputs"),
        Operation("mv.calibration_final_solution_selections", "mv1", "calibration", "final_cached_solution_selection_events", "2", "upper_bound", "final_solution_owner_choice", "at_most_one_per_polarity_after_80_outer_midpoint_updates;selects_one_cached_mu_and_its_paired_inner_alpha_and_retains_their_signed_yield_and_q_residuals;whether_endpoint_midpoint_or_other_cached_candidate_and_the_tie_rule_are_not_frozen", "standalone_final_solution_selection_blocker"),
        Operation("mv.calibration_final_distribution_parameter_constructions", "mv1", "calibration", "final_distribution_parameter_constructions", "2", "upper_bound", "reached_final_solution", "at_most_one_per_selected_polarity;constructs_two_strictly_positive_beta_shapes_or_one_unit_interval_two_point_mixing_probability_and_marks_the_other_distribution_branch_INAPPLICABLE;excludes_inverse_CDF_vector_domain_and_selection_work", "standalone_final_parameter_output_construction"),
        Operation("mv.calibration_validation_passes", "mv1", "calibration", "validation_residual_and_pass_assemblies", "2", "upper_bound", "successful_calibration_path", "one_per_reached_polarity;retains_signed_yield_residual=validation_estimated_P(E=1_given_Y)-rho_Y_and_signed_q_residual=validation_estimated_E(q_observed_given_E=1,Y)-q_Y_target_applies_both_absolute_residual_less_than_or_equal_to_0.0005_comparisons_and_emits_pass_or_fail;vector_generation_and_reductions_are_separate"),
        Operation("mv.calibration_control_record_assemblies", "mv1", "calibration_audit", "polarity_control_record_assemblies", "2", "exact", "all", "one_present_and_one_absent_record_per_manifest_candidate;copies_the_11_realized_control_counters_in_frozen_order_preserves_zero_for_scientifically_skipped_later_stages_sets_VALUE_for_a_committed_scientific_path_or_NOT_REACHED_when_no_committed_path_exists_and_excludes_the_counted_operations_static_classification_and_serialization", "composite_control_output_assembly"),
        Operation("mv.calibration_materialized_words", "mv1", "calibration_raw", "uint64_words", "2*(2^20+2^22)*32", "upper_bound", "materialize", "complete_raw_buffers_once", "exclusive_calibration_raw_alternative"),
        Operation("mv.calibration_replay_words", "mv1", "calibration_raw", "uint64_words", "32*(V_cal+V_val)", "upper_bound", "replay", "V_cal_and_V_val_are_the_separate_candidate_and_validation_vector_rows;regenerate_raw_words_for_every_vector_evaluation", "exclusive_calibration_raw_alternative"),
        Operation("mv.calibration_open_unit_conversions_replay", "mv1", "calibration_conversion", "uint64_to_open_unit", "32*(V_cal+V_val)", "upper_bound", "replay", "convert_each_regenerated_word_for_every_candidate_or_validation_evaluation", "exclusive_conversion_alternative"),
        Operation("mv.calibration_open_unit_conversions_materialize_reconvert", "mv1", "calibration_conversion", "uint64_to_open_unit", "32*(V_cal+V_val)", "upper_bound", "materialize_raw_then_reconvert", "retain_raw_words_but_reconvert_for_every_candidate_or_validation_evaluation", "exclusive_conversion_alternative"),
        Operation("mv.calibration_open_unit_conversions_materialize_cache", "mv1", "calibration_conversion", "uint64_to_open_unit", "2*(2^20+2^22)*32", "upper_bound", "materialize_raw_and_open_unit_cache", "convert_each_materialized_word_once", "exclusive_conversion_alternative"),
        Operation("mv.calibration_open_unit_cache_bytes", "mv1", "calibration_conversion", "bytes", "8*2*(2^20+2^22)*32", "upper_bound", "materialize_raw_and_open_unit_cache", "additional_uncompressed_binary64_cache_per_candidate", "exclusive_conversion_storage_alternative"),
        Operation("mv.calibration_normal_inverse", "mv1", "calibration_transform", "inverse_normal_calls", "11*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "one_probability_plus_ten_state_channels_per_candidate_or_validation_vector"),
        Operation("mv.calibration_beta_inverse", "mv1", "calibration_transform", "beta_inverse_calls", "(V_cal+V_val)_or_0", "upper_bound", "beta_candidates_only", "zero_for_two_point_candidates"),
        Operation("mv.calibration_two_point_lookup", "mv1", "calibration_transform", "two_point_lookups", "(V_cal+V_val)_or_0", "upper_bound", "two_point_candidates_only", "zero_for_beta_candidates"),
        Operation("mv.calibration_coverage_expit", "mv1", "calibration_transform", "expit_calls", "10*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "ten_readers_per_candidate_or_validation_vector", "composite_expit_alternative_do_not_sum_with_primitive_exp"),
        Operation("mv.calibration_coverage_exp_calls", "mv1", "calibration_transform", "exp_calls", "10*(V_cal+V_val)", "upper_bound", "primitive_expit_path", "one_exponential_per_coverage_expit", "primitive_expit_alternative_do_not_sum_with_composite"),
        Operation("mv.calibration_coverage_lookup", "mv1", "calibration_transform", "bernoulli_lookups", "10*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "ten_coverage_words_per_candidate_or_validation_vector"),
        Operation("mv.calibration_state_softmax", "mv1", "calibration_transform", "softmax_vectors", "10*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "ten_readers_per_candidate_or_validation_vector", "composite_softmax_alternative_do_not_sum_with_primitive_components"),
        Operation("mv.calibration_state_softmax_exp_calls", "mv1", "calibration_transform", "exp_calls", "30*(V_cal+V_val)", "upper_bound", "primitive_softmax_path", "three_exponentials_for_each_of_ten_reader_state_vectors", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.calibration_state_softmax_normalizations", "mv1", "calibration_transform", "probability_normalizations", "10*(V_cal+V_val)", "upper_bound", "primitive_softmax_path", "one_normalization_per_reader_state_vector", "primitive_softmax_alternative_do_not_sum_with_composite"),
        Operation("mv.calibration_state_softmax_logsumexp_calls", "mv1", "calibration_transform", "logsumexp_calls", "10*(V_cal+V_val)", "upper_bound", "optional_reference_softmax_path", "zero_if_direct_stable_normalization_is_frozen", "optional_primitive_subalternative_do_not_add_without_reference_lock"),
        Operation("mv.calibration_state_lookup", "mv1", "calibration_transform", "categorical_lookups", "10*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "ten_readers_per_candidate_or_validation_vector"),
        Operation("mv.calibration_clip_round", "mv1", "calibration_transform", "clip_round_events", "10*(V_cal+V_val)", "upper_bound", "materialize_or_replay", "exact_reference_rule_owner_blocked"),
        Operation("mv.calibration_reductions", "mv1", "calibration", "fixed_order_reductions", "V_cal+V_val", "upper_bound", "materialize_or_replay", "one_declared_vector_reduction_unit_per_candidate_or_validation_vector"),
        Operation("mv.truth_reference_selection_events", "mv1", "static_classification", "truth_reference_selection_events", "unresolved", "unresolved", "truth_definition_owner_choice", "target_vs_independently_validated_calibrated_truth_and_per_component_nonreach_behavior_not_frozen"),
        Operation("mv.static_classification_assemblies", "mv1", "static_classification", "static_state_failure_classification_assemblies", "1", "exact", "composite_static_classification", "one_per_manifest_candidate;includes_all_per_polarity_and_per_residual_two_bit_states_distribution_specific_INAPPLICABLE_states_bracket_monotonicity_residual_validation_status_outer_eligibility_and_first_static_or_calibration_failure_precedence;excludes_calibration_numerics_and_owner_truth_selection_work", "composite_control_classification_do_not_add_future_granular_static_state_or_comparison_rows"),
        Operation("mv.repeat_metric_evaluations", "mv1", "analysis", "metric_evaluations", "unresolved", "unresolved", "owner_choice", "probability_and_categorical_repeat_estimators_not_frozen"),
        Operation("mv.calibration_seed_derivations", "mv1", "calibration_identity", "hmac_seed_derivations", "4", "upper_bound", "successful_calibration_path", "calibration_and_validation_seed_for_two_polarities"),
        Operation("mv.calibration_trace_digest_calls", "mv1", "calibration_identity", "sha256_calls", "2", "upper_bound", "attempted_polarities", "one_final_whole_trace_digest_per_attempted_polarity_at_most;does_not_include_checkpoint_or_raw_buffer_digests;trace_encoding_and_depth_remain_owner_blocked", "standalone_final_trace_identity_blocker_until_trace_lock"),
        Operation("mv.calibration_trace_hash_bytes", "mv1", "calibration_identity", "bytes", "unresolved", "unresolved", "trace_owner_choice", "canonical_trace_encoding_depth_and_failure_transcript_domain_not_frozen", "standalone_identity_blocker"),
        Operation("mv.calibration_evaluation_digest_calls", "mv1", "calibration_identity", "sha256_calls", "unresolved", "unresolved", "evaluation_trace_owner_choice", "one_integrity_digest_per_retained_complete_named_mean_endpoint_or_midpoint_evaluation_but_trace_depth_and_early_failure_depth_not_frozen;not_a_durable_restart_checkpoint", "standalone_evaluation_identity_blocker"),
        Operation("mv.calibration_evaluation_hash_bytes", "mv1", "calibration_identity", "bytes", "unresolved", "unresolved", "evaluation_trace_owner_choice", "complete_evaluation_transcript_domain_and_encoding_not_frozen;not_a_durable_restart_checkpoint", "standalone_evaluation_identity_blocker"),
        Operation("mv.calibration_raw_buffer_digest_calls", "mv1", "calibration_identity", "sha256_calls", "unresolved", "unresolved", "materialize_raw", "number_of_materialized_base_and_validation_buffers_and_tiling_verification_policy_not_frozen", "exclusive_materialization_identity_blocker"),
        Operation("mv.calibration_raw_buffer_hash_bytes", "mv1", "calibration_identity", "bytes", "unresolved", "unresolved", "materialize_raw", "canonical_raw_buffer_header_tiling_and_digest_domain_not_frozen", "exclusive_materialization_identity_blocker"),
        Operation("mv.outer_seed_derivations", "mv1", "outer_identity", "hmac_seed_derivations", "2*R", "upper_bound", "all_candidates_calibrate", "one_outer_DGP_and_one_analysis_bootstrap_seed_per_identity"),
        Operation("mv.calibration_validation_hashes", "mv1", "calibration_identity", "sha256_calls", "2", "upper_bound", "successful_calibration_path", "zero_to_two_calls_but_raw_word_transformed_vector_residual_or_reduction_transcript_domain_and_encoding_owner_blocked", "standalone_identity_blocker_until_validation_digest_lock"),
        Operation("mv.calibration_validation_hash_bytes", "mv1", "calibration_identity", "bytes", "unresolved", "unresolved", "validation_digest_owner_choice", "canonical_validation_transcript_domain_and_encoding_not_frozen", "standalone_identity_blocker"),
        Operation("mv.outer_payload_hashes", "mv1", "serialization", "sha256_calls", "M_c", "conditional_exact", "all", "one_hash_per_committed_exact_600_byte_canonical_scientific_record_with_digest_slot_zero;mutable_execution_sidecar_excluded"),
        Operation("mv.outer_record_serializations", "mv1", "serialization", "record_serializations", "M_c", "conditional_exact", "all", "one_600_byte_record_per_unique_integrity_valid_committed_outer_identity"),
        Operation("mv.outer_record_bytes", "mv1", "serialization", "bytes", "600*M_c", "conditional_exact", "all", "fixed_TB0011_core_width_times_committed_record_count"),
        Operation("mv.completion_bitmap_updates", "mv1", "checkpoint", "bit_updates", "M_c", "conditional_exact", "all", "one_final_completion_bit_update_per_unique_integrity_valid_committed_outer_identity"),
        Operation("mv.chunk_journal_records", "mv1", "checkpoint", "record_serializations", "unresolved", "unresolved", "chunk_policy", "chunk_size_retry_and_commit_policy_not_frozen"),
        Operation("mv.failure_detail_records", "mv1", "failure_audit", "record_serializations", "unresolved", "unresolved", "realized_failures", "failure_message_taxonomy_and_realized_failures_not_frozen"),
        Operation("mv.execution_attempt_records", "mv1", "restart", "record_serializations", "unresolved", "unresolved", "resource_policy", "one_32_byte_sidecar_record_per_scheduled_MV_STATIC_MV_CAL_PRESENT_MV_CAL_ABSENT_MV_OUTER_RANGE_or_MV_CELL_AGGREGATE_attempt;whole_polarity_is_atomic_calibration_retry_unit;disjoint_from_reliability_and_global_family_work;chunking_deadline_retry_and_infrastructure_failure_process_not_frozen"),
        Operation("mv.execution_attempt_record_bytes", "mv1", "restart", "bytes", "unresolved", "unresolved", "resource_policy", "32_bytes_per_scheduled_atomic_work_unit_attempt_but_attempt_occurrence_not_frozen"),
    ]
    conditional_stages = {
        "outer",
        "outer_dgp",
        "bootstrap",
        "analysis",
        "aggregate",
        "outer_identity",
        "serialization",
        "checkpoint",
    }
    relabel = {
        "exact": "conditional_exact",
        "lower_bound": "conditional_lower_bound",
        "upper_bound": "conditional_upper_bound",
    }
    rows = [
        replace(
            row,
            count_formula=f"I_R3*({row.count_formula})",
            bound_type=relabel[row.bound_type],
            assumption_or_blocker=(
                "missingness_solve_pass=1_for_m=0_or_MCAR_else_1_iff_owner_frozen_bracket_and_final_selection_are_reached_and_finite_and_abs_selected_signed_residual_less_than_or_equal_to_1e-10;planning_truth_eligibility=VALUE_true_iff_manifest_planning_member_and_final_alpha>0.80_and_final_macro>0.85_and_every_applicable_final_positive>0.75;I_R3=1_iff_missingness_solve_pass_and_quadrature_estimable_and_(planning=0_or_planning_truth_eligibility=VALUE_true);false_promotion_low_truth_not_pruned;"
                + row.assumption_or_blocker
            ),
        )
        if row.kind == "reliability"
        and row.stage in conditional_stages
        and row.count_formula != "unresolved"
        and row.bound_type in relabel
        else row
        for row in rows
    ]
    codes = [row.operation_code for row in rows]
    if len(codes) != len(set(codes)):
        raise AssertionError("operation codes must be unique")
    return rows


def _cell_hash(identifier: str) -> str:
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def _ledger_row(
    kind: str,
    identifier: str,
    code: str,
    count: int | str,
    bound_type: str,
    alternative: str,
    assumptions: str,
) -> tuple[str, ...]:
    return (
        kind,
        _cell_hash(identifier),
        code,
        str(count),
        bound_type,
        alternative,
        assumptions,
    )


def _require_mapped_count(
    operation: Operation, count: int | str
) -> int | str:
    if operation.bound_type != "unresolved" and count == "unresolved":
        raise AssertionError(
            f"non-unresolved operation lacks ledger mapping: {operation.operation_code}"
        )
    return count


def ledger_rows() -> Iterator[tuple[str, ...]]:
    """Yield canonical per-cell integer/formula rows without scientific work."""

    reliability = build_reliability_manifest()
    mv = build_mv_manifest()
    axis_by_name = {axis.identifier: axis for axis in AXES}
    operations = operation_registry()
    r = OUTER_REPLICATIONS
    b = BOOTSTRAP_RESAMPLES

    global_counts: dict[str, int | str] = {
        "global.manifest_hash_reductions": 3,
        "global.metric_registry_digest_calls": 1,
        "global.registry_dictionary_serializations": 4,
        "global.cp95_conformance_interval_calls": 120_001,
        "global.cp95_conformance_beta_quantile_calls": 240_000,
        "global.cp95_half_width_evaluations": 120_001,
        "global.cp95_max_argmax_comparisons": 120_000,
        "global.cp95_threshold_comparisons": 1,
        "global.cp95_conformance_record_serializations": 1,
        "global.family_record_serializations": 2,
        "rel.family_member_status_checks": 10_847,
        "rel.family_status_inventory_appends": 10_847,
        "rel.family_coverage_check_evaluations": 10_847,
        "rel.family_false_promotion_check_evaluations": 10_847,
        "rel.family_planning_power_check_evaluations": 4_416,
        "rel.family_axis_min_argmin_comparisons": 4_401,
        "rel.family_union_failure_complements": 15,
        "rel.family_union_failure_additions": 14,
        "rel.family_union_threshold_comparisons": 1,
        "rel.family_decision_evaluations": 1,
        "mv.family_candidate_status_checks": 2_438,
        "mv.family_status_inventory_appends": 2_438,
        "mv.family_null_upper_check_evaluations": 108,
        "mv.family_coverage_check_evaluations": 2_438,
        "mv.family_planning_power_check_evaluations": 2_304,
        "mv.family_decision_evaluations": 1,
    }
    for operation in operations:
        if operation.kind != "global":
            continue
        count = _require_mapped_count(
            operation,
            global_counts.get(operation.operation_code, "unresolved"),
        )
        yield _ledger_row(
            "global",
            "TB-0011/global",
            operation.operation_code,
            count,
            operation.bound_type,
            operation.alternative,
            "global_once;not_a_candidate_cell",
        )

    for identifier, entry in sorted(reliability.entries.items()):
        axis = axis_by_name[entry.cell["stressed_axis"]]
        n = axis.included_items
        k = axis.categories
        panel = axis.panel_size
        roster = 10 if entry.cell["stressed_axis"].startswith("image_") else 6
        a = n * panel
        dmax = axis.instrument_repeat_ratings
        special_missing = (
            entry.cell["missingness_rate"] != "0.00"
            and entry.cell["missingness_mode"] in {"reader", "class"}
        )
        reader_missing = (
            entry.cell["missingness_rate"] != "0.00"
            and entry.cell["missingness_mode"] == "reader"
        )
        planning = "planning" in entry.families
        fixed = {
            "common.cell_identifier_hash": 1,
            "common.catalogue_serializations": 1,
            "common.catalogue_bytes": 42 + len(identifier.encode("utf-8")),
            "common.static_lock_serializations": 1,
            "common.static_lock_bytes": 112,
            "common.permutation_payload_digest_calls": "I_assignment*(1)",
            "common.static_extension_serializations": 1,
            "common.completion_bitmap_serializations": 1,
            "common.completion_bitmap_bytes": 15_000,
            "common.cell_aggregate_serializations": 1,
            "rel.outer_records": r,
            "rel.dgp_words_lower": r * (n + 2 * a),
            "rel.dgp_words_upper": r * (n + 2 * a + n + 3 * dmax),
            "rel.open_unit_conversions_lower": r * (n + 2 * a),
            "rel.open_unit_conversions_upper": r * (n + 2 * a + n + 3 * dmax),
            "rel.item_inverse_normal": r * n,
            "rel.first_rating_softmax": r * a,
            "rel.first_rating_softmax_exp_calls": r * a * k,
            "rel.first_rating_softmax_normalizations": r * a,
            "rel.first_rating_softmax_logsumexp_calls": r * a,
            "rel.first_rating_lookup": r * a,
            "rel.missingness_lookup": r * a,
            "rel.baseline_log_values": k * k,
            "rel.ambiguity_draws_lower": 0,
            "rel.ambiguity_draws_upper": r * n,
            "rel.ambiguity_interpretation_lookups_upper": r * n,
            "rel.repeat_events_lower": 0,
            "rel.repeat_events_upper": r * dmax,
            "rel.repeat_words_lower": 0,
            "rel.repeat_words_upper": 3 * r * dmax,
            "rel.repeat_match_lookups_upper": r * dmax,
            "rel.repeat_alternate_normalizations_upper": r * dmax,
            "rel.repeat_categorical_lookups_upper": r * dmax,
            "rel.repeat_missingness_lookups_upper": r * dmax,
            "rel.bootstrap_index_words": r * b * n,
            "rel.bootstrap_index_formations": r * b * n,
            "rel.statistic_recomputations": r * (b + 1),
            "rel.percentile_selections": r,
            "rel.outer_point_descriptive_reductions": r,
            "rel.outer_classification_assemblies": r,
            "rel.missing_endpoint_residual_evaluations": 2
            if special_missing
            else 0,
            "rel.missing_bracket_checks": 1 if special_missing else 0,
            "rel.missing_midpoint_controls": 100 if special_missing else 0,
            "rel.missing_residual_evaluations": 102 if special_missing else 0,
            "rel.missing_final_candidate_selection_events": 1
            if special_missing
            else 0,
            "rel.missing_expit_constructions": 102 * a if special_missing else 0,
            "rel.missing_expit_exp_calls": 102 * a if special_missing else 0,
            "rel.quadrature_node_reductions": "I_missing*(102)",
            "rel.quadrature_probability_constructions": f"I_missing*({102 * a})",
            "rel.quadrature_softmax_exp_calls": f"I_missing*({102 * a * k})",
            "rel.quadrature_softmax_normalizations": f"I_missing*({102 * a})",
            "rel.quadrature_softmax_logsumexp_calls": f"I_missing*({102 * a})",
            "rel.reader_effect_inverse_normal": roster * k,
            "rel.reader_effect_vector_normalizations": k,
            "rel.missing_reader_effect_inverse_normal": roster
            if reader_missing
            else 0,
            "rel.missing_reader_vector_normalizations": 1 if reader_missing else 0,
            "rel.static_classification_assemblies": 1,
            "rel.aggregate_interval_calls_lower": (
                f"I_complete*({11 + k + int(planning)})"
            ),
            "rel.aggregate_interval_calls_upper": (
                f"I_complete*({12 + k + int(planning)})"
            ),
            "rel.aggregate_beta_quantile_calls_upper": (
                f"I_complete*({2 * (11 + k) + int(planning)}+I_false)"
            ),
            "rel.aggregate_completion_identity_checks": r,
            "rel.aggregate_base_counter_updates": f"I_complete*({r * (11 + k)})",
            "rel.aggregate_undefined_bootstrap_sum_additions": f"I_complete*({r})",
            "rel.aggregate_proportion_evaluations": f"I_complete*({11 + k})",
            "rel.aggregate_undefined_bootstrap_fraction_divisions": "I_complete*(1)",
            "rel.aggregate_record_classification_assemblies": 1,
            "rel.outer_seed_derivations": 2 * r,
            "rel.outer_payload_hashes": r,
            "rel.outer_record_serializations": r,
            "rel.outer_record_bytes": 336 * r,
            "rel.completion_bitmap_updates": r,
        }
        for operation in operations:
            if operation.kind not in {"common", "reliability"}:
                continue
            count: int | str = fixed.get(operation.operation_code, "unresolved")
            if "M_c" in operation.count_formula and isinstance(count, int):
                if count % r:
                    raise AssertionError(
                        f"M_c operation is not proportional to R: {operation.operation_code}"
                    )
                count = f"M_c*({count // r})"
            if (
                operation.bound_type.startswith("conditional_")
                and operation.count_formula.startswith("I_R3*")
                and count != "unresolved"
            ):
                count = f"I_R3*({count})"
            count = _require_mapped_count(operation, count)
            yield _ledger_row(
                "reliability",
                identifier,
                operation.operation_code,
                count,
                operation.bound_type,
                operation.alternative,
                f"missingness_solve_pass=1_for_m=0_or_MCAR_else_1_iff_owner_frozen_bracket_and_final_selection_reached_finite_and_abs_selected_signed_residual<=1e-10;planning_truth_eligibility=VALUE_true_iff_manifest_planning_member_and_final_alpha>0.80_and_final_macro>0.85_and_every_applicable_final_positive>0.75;I_R3=missingness_solve_pass_and_quadrature_estimable_and_(planning=0_or_planning_truth_eligibility=VALUE_true);false_promotion_low_truth_not_pruned;K={k};N={n};P={panel};A={a};Dmax={dmax};planning={int(planning)}",
            )

    calibration_candidate_evaluations = (
        2
        * (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS)
        * (CALIBRATION_BISECTIONS + 2)
        * CALIBRATION_VECTORS
    )
    calibration_validation_evaluations = 2 * VALIDATION_VECTORS
    calibration_evaluations = (
        calibration_candidate_evaluations + calibration_validation_evaluations
    )
    for identifier, entry in sorted(mv.entries.items()):
        n = int(entry.cell["n"])
        d = 10 * ((3 * n + 9) // 10)
        planning = "planning" in entry.families
        null_family = "null_boundary" in entry.families
        is_beta = entry.cell["q_distribution"] == "beta"
        fixed = {
            "common.cell_identifier_hash": 1,
            "common.catalogue_serializations": 1,
            "common.catalogue_bytes": 42 + len(identifier.encode("utf-8")),
            "common.static_lock_serializations": 1,
            "common.static_lock_bytes": 112,
            "common.permutation_payload_digest_calls": "I_assignment*(1)",
            "common.static_extension_serializations": 1,
            "common.completion_bitmap_serializations": 1,
            "common.completion_bitmap_bytes": 15_000,
            "common.cell_aggregate_serializations": 1,
            "mv.outer_records": "M_c",
            "mv.dgp_words": r * (66 * n + 4 * d),
            "mv.open_unit_conversions": r * (66 * n + 4 * d),
            "mv.outer_first_presentation_events": r * 20 * n,
            "mv.outer_repeat_events": r * d,
            "mv.outer_evaluability_block_reductions": r * 2 * n,
            "mv.outer_four_of_five_panel_reductions": r * 4 * n,
            "mv.outer_panel_mean_reductions": r * 4 * n,
            "mv.outer_patient_q_reductions": r * 2 * n,
            "mv.static_reader_effect_inverse_normal": 30,
            "mv.static_reader_vector_normalizations": 3,
            "mv.static_state_log_values": 3,
            "mv.outer_screen_fidelity_lookups": r * 2 * n,
            "mv.outer_q_beta_inverse": r * 2 * n if is_beta else 0,
            "mv.outer_q_two_point_lookup": 0 if is_beta else r * 2 * n,
            "mv.outer_patient_normal_inverse": r * 2 * n,
            "mv.outer_rating_normal_inverse": r * 20 * n,
            "mv.outer_coverage_expit": r * 20 * n,
            "mv.outer_coverage_exp_calls": r * 20 * n,
            "mv.outer_coverage_lookup": r * 20 * n,
            "mv.outer_state_softmax": r * 20 * n,
            "mv.outer_state_softmax_exp_calls": 3 * r * 20 * n,
            "mv.outer_state_softmax_normalizations": r * 20 * n,
            "mv.outer_state_softmax_logsumexp_calls": r * 20 * n,
            "mv.outer_state_lookup": r * 20 * n,
            "mv.outer_clip_round": r * 20 * n,
            "mv.repeat_rating_normal_inverse": r * d,
            "mv.repeat_coverage_expit": r * d,
            "mv.repeat_coverage_exp_calls": r * d,
            "mv.repeat_coverage_lookup": r * d,
            "mv.repeat_state_softmax": r * d,
            "mv.repeat_state_softmax_exp_calls": 3 * r * d,
            "mv.repeat_state_softmax_normalizations": r * d,
            "mv.repeat_state_softmax_logsumexp_calls": r * d,
            "mv.repeat_match_lookup": r * d,
            "mv.repeat_alternate_normalization": r * d,
            "mv.repeat_state_lookup": r * d,
            "mv.repeat_clip_round": r * d,
            "mv.bootstrap_index_words": r * b * 2 * n,
            "mv.bootstrap_index_formations": r * b * 2 * n,
            "mv.q_recomputations": r * (b + 1),
            "mv.max_t_selections": r,
            "mv.fe_fits": r,
            "mv.loo_reductions": 10 * r,
            "mv.outer_screen_assignment_tallies": "M_c",
            "mv.outer_classification_assemblies": "M_c",
            "mv.aggregate_interval_calls": (
                f"I_outer*I_complete*({17 + int(null_family) + int(planning)})"
            ),
            "mv.aggregate_beta_quantile_calls_upper": (
                f"I_outer*I_complete*({2 * (17 + int(planning)) + int(null_family)})"
            ),
            "mv.aggregate_completion_identity_checks": f"I_outer*({r})",
            "mv.aggregate_base_counter_updates": f"I_outer*I_complete*({17 * r})",
            "mv.aggregate_proportion_evaluations": "I_outer*I_complete*(17)",
            "mv.aggregate_record_classification_assemblies": 1,
            "mv.calibration_domain_bound_constructions": "I_domain*(2)",
            "mv.calibration_candidate_vector_evaluations": (
                calibration_candidate_evaluations
            ),
            "mv.calibration_validation_vector_evaluations": (
                calibration_validation_evaluations
            ),
            "mv.calibration_alpha_solves": 2 * (
                CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS
            ),
            "mv.calibration_alpha_bracket_checks": 2
            * (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS),
            "mv.calibration_alpha_midpoint_controls": 2
            * (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS)
            * CALIBRATION_BISECTIONS,
            "mv.calibration_residual_evaluations": 2
            * (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS)
            * (CALIBRATION_BISECTIONS + 2),
            "mv.calibration_inner_alpha_final_selections": 2
            * (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS),
            "mv.calibration_scan_points": 2 * CALIBRATION_MEAN_GRID,
            "mv.calibration_outer_q_bracket_checks": 2,
            "mv.calibration_outer_midpoints": 2 * CALIBRATION_BISECTIONS,
            "mv.calibration_monotonicity_comparisons": 2
            * (CALIBRATION_MEAN_GRID - 1),
            "mv.calibration_final_solution_selections": 2,
            "mv.calibration_final_distribution_parameter_constructions": 2,
            "mv.calibration_validation_passes": 2,
            "mv.calibration_control_record_assemblies": 2,
            "mv.calibration_materialized_words": 2
            * (CALIBRATION_VECTORS + VALIDATION_VECTORS)
            * 32,
            "mv.calibration_replay_words": 32 * calibration_evaluations,
            "mv.calibration_open_unit_conversions_replay": 32
            * calibration_evaluations,
            "mv.calibration_open_unit_conversions_materialize_reconvert": 32
            * calibration_evaluations,
            "mv.calibration_open_unit_conversions_materialize_cache": 2
            * (CALIBRATION_VECTORS + VALIDATION_VECTORS)
            * 32,
            "mv.calibration_open_unit_cache_bytes": 8
            * 2
            * (CALIBRATION_VECTORS + VALIDATION_VECTORS)
            * 32,
            "mv.calibration_normal_inverse": 11 * calibration_evaluations,
            "mv.calibration_beta_inverse": calibration_evaluations if is_beta else 0,
            "mv.calibration_two_point_lookup": 0 if is_beta else calibration_evaluations,
            "mv.calibration_coverage_expit": 10 * calibration_evaluations,
            "mv.calibration_coverage_exp_calls": 10 * calibration_evaluations,
            "mv.calibration_coverage_lookup": 10 * calibration_evaluations,
            "mv.calibration_state_softmax": 10 * calibration_evaluations,
            "mv.calibration_state_softmax_exp_calls": 30
            * calibration_evaluations,
            "mv.calibration_state_softmax_normalizations": 10
            * calibration_evaluations,
            "mv.calibration_state_softmax_logsumexp_calls": 10
            * calibration_evaluations,
            "mv.calibration_state_lookup": 10 * calibration_evaluations,
            "mv.calibration_clip_round": 10 * calibration_evaluations,
            "mv.calibration_reductions": calibration_evaluations,
            "mv.static_classification_assemblies": 1,
            "mv.calibration_seed_derivations": 4,
            "mv.calibration_trace_digest_calls": 2,
            "mv.outer_seed_derivations": 2 * r,
            "mv.calibration_validation_hashes": 2,
            "mv.outer_payload_hashes": "M_c",
            "mv.outer_record_serializations": "M_c",
            "mv.outer_record_bytes": "600*M_c",
            "mv.completion_bitmap_updates": "M_c",
        }
        for operation in operations:
            if operation.kind not in {"common", "mv1"}:
                continue
            count = fixed.get(operation.operation_code, "unresolved")
            count = _require_mapped_count(operation, count)
            yield _ledger_row(
                "mv1",
                identifier,
                operation.operation_code,
                count,
                operation.bound_type,
                operation.alternative,
                f"n={n};D={d};beta={int(is_beta)};planning={int(planning)};null_family={int(null_family)};I_domain=owner_frozen_open_interval_endpoint_or_interior_margin_and_positive_beta_shape_bound_rule",
            )


def _csv_bytes(header: Iterable[str], rows: Iterable[Iterable[object]]) -> bytes:
    handle = io.StringIO(newline="")
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return handle.getvalue().encode("utf-8")


class _DigestSink:
    def __init__(self) -> None:
        self.digest = hashlib.sha256()

    def write(self, value: str) -> int:
        payload = value.encode("utf-8")
        self.digest.update(payload)
        return len(value)


def ledger_identity() -> tuple[int, str]:
    sink = _DigestSink()
    writer = csv.writer(sink, lineterminator="\n")
    writer.writerow(LEDGER_HEADER)
    count = 0
    for row in ledger_rows():
        writer.writerow(row)
        count += 1
    return count, sink.digest.hexdigest()


def _catalogue_bytes(identifiers: Iterable[str]) -> int:
    return sum(42 + len(identifier.encode("utf-8")) for identifier in identifiers)


def summary_rows() -> list[tuple[str, ...]]:
    reliability = build_reliability_manifest()
    mv = build_mv_manifest()
    combined_entries = dict(reliability.entries)
    overlap = set(combined_entries).intersection(mv.entries)
    if overlap:
        raise AssertionError("reliability and MV manifest identifiers overlap")
    combined_entries.update(mv.entries)
    metrics = metric_fields()
    operations = operation_registry()
    metric_payload = _csv_bytes(METRIC_HEADER, (field.row() for field in metrics))
    operation_payload = _csv_bytes(OPERATION_HEADER, (row.row() for row in operations))
    ledger_count, ledger_hash = ledger_identity()

    rel_cells = len(reliability.entries)
    mv_cells = len(mv.entries)
    total_cells = rel_cells + mv_cells
    rel_outer = rel_cells * OUTER_REPLICATIONS
    mv_outer_upper = mv_cells * OUTER_REPLICATIONS
    prefix_bytes = 72
    rel_state_bytes = 8
    mv_state_bytes = 16
    rel_record_bytes = prefix_bytes + rel_state_bytes + 32 * 8
    mv_record_bytes = prefix_bytes + mv_state_bytes + 64 * 8
    catalogue_bytes = _catalogue_bytes(
        (*reliability.entries.keys(), *mv.entries.keys())
    )
    static_lock_bytes = 112 * total_cells
    completion_bitmap_bytes = 15_000 * total_cells
    core_outer_bytes = (
        rel_outer * rel_record_bytes + mv_outer_upper * mv_record_bytes
    )
    full_candidate_floor = (
        catalogue_bytes
        + static_lock_bytes
        + completion_bitmap_bytes
        + core_outer_bytes
    )

    def row(
        scope: str,
        metric: str,
        value: int | str,
        unit: str,
        bound_type: str,
        assumption: str,
    ) -> tuple[str, ...]:
        return (scope, metric, str(value), unit, bound_type, assumption)

    return [
        row("manifest", "reliability_cell_count", rel_cells, "cells", "exact", "frozen_TB0009_enumerator"),
        row("manifest", "mv1_candidate_cell_count", mv_cells, "cells", "exact", "precalibration_union"),
        row("manifest", "combined_cell_count", total_cells, "cells", "exact", "reliability_plus_mv1"),
        row("manifest", "reliability_manifest_sha256", manifest_sha256(reliability.entries), "sha256", "exact", "sorted_ids_newline_terminated"),
        row("manifest", "mv1_manifest_sha256", manifest_sha256(mv.entries), "sha256", "exact", "sorted_ids_newline_terminated"),
        row("manifest", "combined_manifest_sha256", manifest_sha256(combined_entries), "sha256", "exact", "sorted_ids_newline_terminated;anchors_global_catalogue_index_and_execution_join_namespace"),
        row("registry", "metric_row_count", len(metrics), "rows", "exact", "header_excluded"),
        row("registry", "metric_registry_sha256", hashlib.sha256(metric_payload).hexdigest(), "sha256", "exact", "complete_csv_including_header"),
        row("registry", "operation_row_count", len(operations), "rows", "exact", "header_excluded"),
        row("registry", "operation_registry_sha256", hashlib.sha256(operation_payload).hexdigest(), "sha256", "exact", "complete_csv_including_header"),
        row("ledger", "per_cell_row_count", ledger_count, "rows", "exact", "header_excluded;full_ledger_untracked"),
        row("ledger", "per_cell_ledger_sha256", ledger_hash, "sha256", "exact", "complete_csv_including_header"),
        row("schema", "common_outer_prefix_bytes", prefix_bytes, "bytes", "exact", "includes_distinct_failure_and_event_masks_plus_deterministic_execution_sidecar_join_key;mutable_retry_provenance_externalized"),
        row("schema", "reliability_state_mask_bytes", rel_state_bytes, "bytes", "exact", "32_slots_at_2_bits"),
        row("schema", "mv1_state_mask_bytes", mv_state_bytes, "bytes", "exact", "64_slots_at_2_bits"),
        row("schema", "reliability_outer_record_bytes", rel_record_bytes, "bytes", "exact", "72_prefix+8_state+32x8_payload"),
        row("schema", "mv1_outer_record_bytes", mv_record_bytes, "bytes", "exact", "72_prefix+16_state+64x8_payload"),
        row("schema", "cell_catalogue_bytes", catalogue_bytes, "bytes", "exact", "42_plus_exact_canonical_json_length_per_cell"),
        row("schema", "cell_static_lock_bytes", static_lock_bytes, "bytes", "exact", "112_bytes_per_candidate_cell"),
        row("schema", "completion_bitmap_bytes", completion_bitmap_bytes, "bytes", "exact", "15000_bytes_per_candidate_cell"),
        row("schema", "core_outer_record_bytes", core_outer_bytes, "bytes", "upper_bound", "all_mv_candidates_calibrate_and_all_outer_records_are_emitted"),
        row("schema", "full_candidate_success_core_floor_bytes", full_candidate_floor, "bytes", "lower_bound", "conditional_on_all_candidate_outer_records;excludes_all_typed_static_aggregate_family_permutation_journal_failure_and_owner_blocked_extensions"),
        row("schema", "prior_TB0010_core_floor_bytes", 572_492_490_610, "bytes", "superseded", "312_and_568_byte_records_lacked_state_event_and_retry_join_semantics"),
        row("schema", "core_floor_increase_bytes", full_candidate_floor - 572_492_490_610, "bytes", "exact_delta", "same_catalogue_lock_bitmap_and_all_candidate_success_path"),
        row("schema", "final_persistent_output_upper_bytes", "not_identifiable", "bytes", "unresolved", "typed_extensions_permutations_journals_failure_details_and_owner_choices_not_frozen"),
        row("blocker", "reliability_truth_reference", "owner_decision_required", "decision", "unresolved", "41_vs61_or_other_declared_selection_rule"),
        row("blocker", "reliability_repeat_and_ambiguity_domains", "owner_decision_required", "decision", "unresolved", "D_g_H_g_item_ids_permutations_and_repeat_outputs"),
        row("blocker", "reliability_missingness_bisection_rule", "owner_decision_required", "decision", "unresolved", "signed_residual_direction_inclusive_endpoint_zero_bracket_predicate_nonfinite_semantics_midpoint_zero_equality_endpoint_update_post_100_candidate_and_tie_rule"),
        row("blocker", "mv1_numerical_domain_inner_and_outer_solution_truth_and_trace", "owner_decision_required", "decision", "unresolved", "open_interval_endpoint_or_interior_margin_positive_shape_bound_inner_alpha_bracket_sign_orientation_predicate_midpoint_equality_update_and_final_selection_post_80_outer_midpoint_final_candidate_rule_target_vs_validated_truth_and_retained_trace"),
        row("blocker", "failure_precedence_and_component_taxonomy", "owner_approval_required", "decision", "unresolved", "registry_contains_recommendation_only"),
        row("blocker", "reference_algorithms_and_software", "owner_decision_required", "decision", "unresolved", "inverse_CDF_CP_FE_and_any_added_sensitivity"),
        row("blocker", "runtime_ram_scratch_capacity_feasibility", "not_identifiable", "resource", "unresolved", "requires_later_authorized_benchmark_and_allocation"),
    ]


def _write_csv(
    handle: TextIO,
    header: Iterable[str],
    rows: Iterable[Iterable[object]],
) -> None:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--registry",
        choices=("metrics", "operations"),
        help="print one small tracked registry",
    )
    group.add_argument(
        "--ledger",
        action="store_true",
        help="stream the full untracked per-cell ledger",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.registry == "metrics":
        _write_csv(sys.stdout, METRIC_HEADER, (field.row() for field in metric_fields()))
    elif args.registry == "operations":
        _write_csv(sys.stdout, OPERATION_HEADER, (row.row() for row in operation_registry()))
    elif args.ledger:
        _write_csv(sys.stdout, LEDGER_HEADER, ledger_rows())
    else:
        _write_csv(sys.stdout, SUMMARY_HEADER, summary_rows())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
