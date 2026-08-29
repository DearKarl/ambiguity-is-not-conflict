import csv
import math
import subprocess
import sys
from pathlib import Path
from statistics import NormalDist

from scripts.check_repository import collect_errors
from scripts.compile_simulation_semantic_count_ledger import (
    ledger_identity,
    metric_fields,
    operation_registry,
)
from scripts.enumerate_simulation_resource_manifest import (
    build_mv_manifest,
    build_reliability_manifest,
    manifest_sha256,
)


ROOT = Path(__file__).resolve().parents[1]


def test_repository_contract_is_complete() -> None:
    assert collect_errors(ROOT) == []


def test_readme_declares_protocol_status() -> None:
    readme = " ".join(
        (ROOT / "README.md").read_text(encoding="utf-8").lower().split()
    )
    assert "protocol stage" in readme
    assert "no core experiment has been run" in readme


def test_gate_zero_blocks_core_execution() -> None:
    contract = (
        ROOT / "docs/research/research_contract.md"
    ).read_text(encoding="utf-8").lower()
    assert "gate 0 open" in contract
    assert "forbidden actions while gate 0 is open" in contract


def test_ambiguity_and_information_loss_are_separate() -> None:
    scope = (
        ROOT / "docs/research/scope_charter.md"
    ).read_text(encoding="utf-8")
    assert "A_v" in scope and "A_t" in scope
    assert "M_v" in scope and "M_t" in scope
    assert "ambiguity or information loss" not in scope.lower()


def test_calibration_requires_a_target_distribution() -> None:
    evaluation = (
        ROOT / "docs/research/evaluation_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "target-distribution rule" in evaluation
    assert "balanced synthetic set" in evaluation


def test_protocol_record_is_not_a_fake_release() -> None:
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert "date-released:" not in citation
    assert "\nversion:" not in citation


def test_submission_identity_remains_conditional_and_single_route() -> None:
    strategy = " ".join(
        (ROOT / "docs/research/submission_strategy.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "use-inspired" in strategy
    assert "2027 call not yet available" in strategy
    assert "single intended primary contribution" in strategy
    assert "not a second project or a simultaneous submission" in strategy
    assert "conditioning on observational ambiguity alone is never sufficient" in strategy


def test_month_three_gate_is_not_confirmatory_evidence() -> None:
    measurement = (
        ROOT / "docs/research/measurement_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "necessary but not sufficient" in measurement
    assert "matched deterministic compatibility/failure" in measurement
    assert "cannot be promoted as confirmatory evidence" in measurement


def test_gate_zero_evidence_packet_is_non_executable() -> None:
    decision_log = (
        ROOT / "docs/research/decision_log.md"
    ).read_text(encoding="utf-8").lower()
    assert "dr-0007" in decision_log
    assert "proposed; not approved and not executable" in decision_log
    assert "it is not gate-0" in decision_log
    assert "closure, novelty proof" in decision_log


def test_ambiguous_cases_do_not_receive_fake_conflict_labels() -> None:
    packet = " ".join(
        (ROOT / "docs/research/task_estimand_options.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    measurement = (
        ROOT / "docs/research/measurement_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "c* = undefined" in packet
    assert "undefined conflict label is not a negative label" in packet
    assert "not binary conflict" in packet
    assert "does not enter" in packet
    assert "cannot identify causal separation" in packet
    assert "nominal full" in measurement and "is prohibited" in measurement


def test_restricted_mimic_content_stays_out_of_online_services() -> None:
    governance = (
        ROOT / "docs/research/data_governance.md"
    ).read_text(encoding="utf-8").lower()
    audit = " ".join(
        (ROOT / "docs/research/dataset_feasibility_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "must not be pasted into codex/chatgpt" in governance
    assert "derived datasets and models" in governance
    assert "no dataset files, record-level data" in audit
    assert "models, credentials, or restricted content" in audit


def test_broad_conflict_novelty_claim_is_rejected() -> None:
    audit = (
        ROOT / "docs/research/novelty_audit.md"
    ).read_text(encoding="utf-8").lower()
    assert "the broad claim" in audit and "is occupied" in audit
    assert "confer" in audit and "rcml" in audit
    assert "matched deterministic" in audit


def test_gate_zero_freeze_candidate_remains_non_executable() -> None:
    closure = (
        ROOT / "docs/research/gate0_closure_audit.md"
    ).read_text(encoding="utf-8").lower()
    decision_log = (
        ROOT / "docs/research/decision_log.md"
    ).read_text(encoding="utf-8").lower()
    assert "gate 0 remains open" in closure
    assert "not execution-ready" in closure
    assert "dr-0008" in decision_log
    assert "not executable" in decision_log
    assert "not approval, gate-0 closure" in decision_log


def test_primary_specificity_candidate_is_magnitude_safe() -> None:
    plan = (
        ROOT / "docs/research/statistical_analysis_plan.md"
    ).read_text(encoding="utf-8").lower()
    measurement = (
        ROOT / "docs/research/measurement_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "psi_{mag" in plan
    assert "signed control responses can cancel" in measurement
    assert "0.20" in plan
    assert "not statistically superior" in plan
    assert "d_*^2" in plan
    assert "gate 0 must already name exactly one primary pointwise instrument" in plan
    assert "a_bss" in plan

    packet = (
        ROOT / "docs/research/task_estimand_options.md"
    ).read_text(encoding="utf-8").lower()
    assert "delta_{bss,m}" in packet and "a_{bss}" in packet
    assert "never raw brier-loss units" in packet


def test_ambiguity_is_not_relabeled_information_loss() -> None:
    protocol = (
        ROOT / "docs/research/annotation_and_intervention_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "does not by itself" in protocol and "establish" in protocol
    assert "no valid image- or text-ambiguity intervention" in protocol
    assert "undefined conflict label is never recoded" in protocol


def test_metadata_stage_excludes_records_and_images() -> None:
    record = (
        ROOT / "docs/research/dataset_decision_candidate.md"
    ).read_text(encoding="utf-8").lower()
    assert "metadata-only feasibility query" in record
    assert "do not read dates/times, demographics, reports, images" in record
    assert "report-screen strata" in record and "never" in record
    assert "no access request" in record


def test_known_and_unknown_checkpoint_exposure_are_not_clean() -> None:
    audit = (
        ROOT / "docs/research/execution_budget_and_backbone_audit.md"
    ).read_text(encoding="utf-8").lower()
    assert "no pretrained vlm" in audit and "unconditionally eligible" in audit
    assert "known-exposure diagnostic" in audit
    assert "unknown exposure" in audit and "not converted to clean" in audit


def test_power_table_is_planning_only() -> None:
    plan = (
        ROOT / "docs/research/statistical_analysis_plan.md"
    ).read_text(encoding="utf-8").lower()
    table = (
        ROOT / "reports/tables/gate0_power_sensitivity.csv"
    ).read_text(encoding="utf-8")
    assert "design-only power bound" in plan
    assert "planning bounds, not observed" in plan
    assert "month3_development" in table
    assert "confirmatory_four_controls" in table


def test_power_table_reproduces_declared_union_bound() -> None:
    path = ROOT / "reports/tables/gate0_power_sensitivity.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    normal = NormalDist()
    for row in rows:
        assert row["endpoint"] in {"psi_mag", "A_psi"}
        k = int(row["K"])
        alpha_family = float(row["alpha_family"])
        power_family = float(row["power_family"])
        d = float(row["standardized_excess_d"])
        critical_sum = normal.inv_cdf(1 - alpha_family / k) + normal.inv_cdf(
            1 - (1 - power_family) / k
        )
        expected_evaluable = math.ceil((critical_sum / d) ** 2)
        assert int(row["n_evaluable"]) == expected_evaluable
        for suffix, retained_percent in (("10", 90), ("15", 85), ("20", 80), ("30", 70)):
            expected_screened = (
                expected_evaluable * 100 + retained_percent - 1
            ) // retained_percent
            assert int(row[f"n_screened_loss_{suffix}"]) == expected_screened


def test_annotation_schema_has_hard_nonassessable_precedence() -> None:
    protocol = (
        ROOT / "docs/research/annotation_and_intervention_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "a_v=not assessable" in protocol
    assert "a_t=not assessable" in protocol
    assert "y_v=undefined" in protocol
    assert "y_t=undefined" in protocol
    assert "can only accept or reject a pair" in protocol
    assert "fresh, same-modality panel" in protocol
    assert "mutually exclusive" in protocol
    assert "complete prescribed field" in protocol
    assert "protocol-defined loss but interpretable" in protocol
    assert "`m_v` exposure is not a synonym for semantic indeterminacy" in protocol
    assert "`m_t` exposure is not a synonym for semantic indeterminacy" in protocol
    assert "decidable from this image" not in protocol
    assert "exact operations" in protocol
    assert "approval blockers" in protocol
    assert "`no target`, `not assessable`" in protocol
    assert "structurally missing probability" in protocol


def test_split_roles_and_access_basis_are_explicit() -> None:
    record = " ".join(
        (ROOT / "docs/research/dataset_decision_candidate.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "ainc/v1/partition" in record
    assert "ainc/v1/study-rank" in record
    assert "no method, normalizer, or threshold is selected or refit there" in record
    assert "exactly one eligible source study per patient" in record
    assert "approved access basis for every person" in record
    assert "`n_images = count_distinct(dicom_id)` from the split rows" in record
    assert "left-join chexpert and negbio 1:1" in record
    assert "complementary cell" in record
    assert "release ledger" in record


def test_artifact_equivalence_is_not_assumed_powered() -> None:
    plan = " ".join(
        (ROOT / "docs/research/statistical_analysis_plan.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "orientation-safe" in plan
    assert "r_j=0.50+|ba_j-0.50|" in plan
    assert "1,047" in plan and "1,757" in plan
    assert "inconclusive" in plan
    assert "failure to demonstrate recovery is not an equivalence pass" in plan
    assert "upper bound strictly below 0.55" in plan
    assert "non-promotable developmental bounded-recoverability" in plan

    normal = NormalDist()
    expected = []
    for alpha_family, power_family in ((0.10, 0.80), (0.025, 0.90)):
        z_alpha = normal.inv_cdf(1 - alpha_family)
        z_power = normal.inv_cdf(1 - (1 - power_family) / 8)
        power = math.ceil(
            (
                z_alpha * math.sqrt(0.55 * 0.45)
                + z_power * math.sqrt(0.50 * 0.50)
            )
            ** 2
            / 0.05**2
        )
        expected.append(power)
    assert expected == [1047, 1757]


def test_gate_zero_dossier_is_finite_and_non_executable() -> None:
    dossier = " ".join(
        (ROOT / "docs/research/gate0_decision_dossier.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    intervention = " ".join(
        (ROOT / "docs/research/intervention_option_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "finite blocker/decision inventory" in dossier
    assert "not yet a complete gate-0 freeze package" in dossier
    assert "mv-1" in dossier and "mt-1" in dossier
    assert "r_j = 0.50 + abs(ba_j - 0.50)" in dossier
    assert "open / kill recommended" in dossier
    assert "tb-0006" in dossier and "pointwise method-claim kill" in dossier
    assert "fitted instance/config" in dossier
    assert "reader-based task-relevance" in dossier and "l_bal" in dossier
    assert "g0-inference" in dossier and "9,999 fixed-seed resamples" in dossier
    assert "g0-ablations" in dossier and "remove `c_vt`" in dossier
    assert "ainc/v1/mv1-qualification" in dossier
    assert "300-screened/216-evaluable" in dossier
    assert "g0-mv-q" in dossier
    assert "does not" in dossier and "close gate 0" in dossier
    assert "224 -> 112 -> 224" in intervention
    assert "`l_bal > 0.10`" in intervention
    assert "`l_present > 0`" in intervention
    assert "`l_absent > 0`" in intervention
    assert "108 evaluable independent" in intervention
    assert "216 total" in intervention
    assert "sole-polarity-slot redaction" in intervention
    assert "y_t=undefined" in intervention
    assert "neither operation is an ambiguity intervention" in intervention


def test_backbone_and_natural_ambiguity_resources_are_not_overclaimed() -> None:
    baseline = (
        ROOT / "docs/research/baselines_and_ablations.md"
    ).read_text(encoding="utf-8").lower()
    resources = (
        ROOT / "docs/research/execution_budget_and_backbone_audit.md"
    ).read_text(encoding="utf-8").lower()
    assert "lower-intent, unknown-overlap non-vlm" in baseline
    assert "neither contamination-negative nor strict-" in baseline
    assert "natural-ambiguity veto audit" in resources
    assert "deferred until after a month-3 pass" in resources
    assert "unallocated reserve" in resources
    assert "all 300 ranked candidates" in resources
    assert "first four rows total 486" in resources
    assert "69-hour reserve" in resources
    assert "locked reliability" in resources
    assert "1,350" in resources


def test_estimator_formalization_records_exact_kills() -> None:
    audit = " ".join(
        (ROOT / "docs/research/estimator_formalization_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "no candidate is promoted" in audit
    assert "\\kappa_l&=(\\widehat p_v-\\widehat p_t)^2" in audit
    assert "sampling-prior log-odds" in audit
    assert "s_{ev}=|\\widehat p_v-\\widehat p_t|(1-u_v)(1-u_t)" in audit
    assert "minimum of control-specific sample means" in audit
    assert "finite-sample plug-in estimator as a deployable pair-level score" in audit
    assert "generally downward biased" in audit
    assert "non-authoritative literature lead" in audit
    assert "link-function guardrail" in audit
    assert "method-claim kill" in audit


def test_baseline_supervision_and_licence_roles_are_not_conflated() -> None:
    baseline = " ".join(
        (ROOT / "docs/research/baselines_and_ablations.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "raw-cos" in baseline
    assert "det-lr" in baseline
    assert "dbf-task" in baseline
    assert "probvlm-2adapter" in baseline
    assert "point-infonce" in baseline
    assert "only `probvlm-2adapter` versus `point-infonce`" in baseline
    assert "privileged ceilings" in baseline
    assert "gpl-3.0" in baseline
    assert "no vendoring" in baseline
    assert "paper-faithful versus code-exact" in baseline
    assert "identical pre-link/post-link convention" in baseline
    assert "c9c5ab41e6fe62a85e5f6441a4dc7b568e1fa421" in baseline
    assert "08d07f8b2ecafc6f1479fe636b26d464d7a5574e" in baseline


def test_nonsmooth_advantage_uses_joint_component_bounds() -> None:
    plan = " ".join(
        (ROOT / "docs/research/statistical_analysis_plan.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "exactly 9,999 resamples and seed `20270829`" in plan
    assert "q_{uj}=+1,q_{dj}=-1" in plan
    assert "l_a=\\min_jl_{uj}-\\min_ju_{dj}" in plan
    assert "u_a=\\min_ju_{uj}-\\min_jl_{dj}" in plan
    assert "do not bootstrap either minimum directly" in plan
    assert "\\min_j(\\mu_{uj}-\\mu_{dj})" in plan


def test_confer_is_only_a_non_authoritative_lead() -> None:
    novelty = " ".join(
        (ROOT / "docs/research/novelty_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "non-authoritative preprint lead" in novelty
    assert "confer remains a non-authoritative surveillance lead" in novelty
    assert "confer-like uncertainty denominator as unadjudicated" in novelty
    assert "discounted belief fusion and confer" not in novelty
    assert "already represented by confer" not in novelty


def test_gate_zero_identity_is_not_selected_from_development() -> None:
    measurement = " ".join(
        (ROOT / "docs/research/measurement_protocol.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "named and approved at gate 0" in measurement
    assert "single fitted instance" in measurement
    assert "named from development" not in measurement


def test_reader_and_mv1_qualification_contract_is_exact_and_non_executable() -> None:
    audit = " ".join(
        (ROOT / "docs/research/reader_measurement_and_mv1_qualification_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "nominal krippendorff alpha" in audit
    assert "selected/evaluable-population" in audit
    assert "finite-roster target" in audit
    assert "h_{b,intact}-h_{b,mv1}" in audit
    assert "all ten probability ratings recorded" in audit
    assert "repeat ratings never become additional inter-reader codings" in audit
    assert "pcg64dxsm" in audit
    assert "compact utf-8 json" in audit
    assert "seed(k,c,t)" in audit
    assert "random_raw()" in audit
    assert "exact intended-class crosswalk" in audit
    assert "omit a polarity main effect" in audit
    assert "p(e=1 | y)=rho_y" in audit
    assert "opposite-polarity vote" in audit
    assert "not intervention-construction validity" in audit
    assert "(0.30,0)" in audit and "(0,0.30)" in audit
    assert "simultaneous coverage" in audit
    assert "exactly 75 first presentations" in audit
    assert "exactly 125 first presentations" in audit
    assert "l_{bal}>0.10" in audit
    assert "l_{present}>0" in audit and "l_{absent}>0" in audit
    assert "exactly 9,999" in audit
    assert "120,000 outer replications" in audit
    assert "clopper--pearson" in audit
    assert "panel/readers" in audit
    assert "does not establish reliability" in audit
    assert "no option is selected" in audit


def test_mv1_yield_table_is_reproducible_and_exposes_fragility() -> None:
    table_path = ROOT / "reports/tables/mv1_qualification_yield_sensitivity.csv"
    with table_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    keyed = {
        (int(row["screened_per_polarity"]), float(row["independent_pair_evaluable_probability"])): row
        for row in rows
    }
    assert keyed[(128, 0.85)]["probability_meet_both_polarities"] == "0.404356"
    assert keyed[(128, 0.85)][
        "minimum_equal_yield_for_90pct_joint_probability"
    ] == "0.887018868"
    assert keyed[(150, 0.80)]["probability_meet_both_polarities"] == "0.986107"
    assert keyed[(150, 0.80)][
        "minimum_equal_yield_for_90pct_joint_probability"
    ] == "0.773382117"

    generated = subprocess.run(
        [sys.executable, "scripts/calculate_mv1_qualification_design.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    assert generated == table_path.read_text(encoding="utf-8")


def test_simulation_manifest_is_exact_reproducible_and_non_executable() -> None:
    reliability = build_reliability_manifest()
    mv = build_mv_manifest()
    assert len(reliability.entries) == 10_847
    assert sum(
        "planning" in entry.families for entry in reliability.entries.values()
    ) == 4_416
    assert len(mv.entries) == 2_438
    assert sum("planning" in entry.families for entry in mv.entries.values()) == 2_304
    assert manifest_sha256(reliability.entries) == (
        "4823bd2f52547673c173aec89ecd3b3c1d416769ee9abde9e3b71bb1fb0245d6"
    )
    assert manifest_sha256(mv.entries) == (
        "1cacee1ebe5aa7b43d37a09d39285a9637c6c274012a7335998bb707bd7ee8c7"
    )

    table_path = ROOT / "reports/tables/simulation_resource_manifest_summary.csv"
    generated = subprocess.run(
        [sys.executable, "scripts/enumerate_simulation_resource_manifest.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    assert generated == table_path.read_text(encoding="utf-8")
    with table_path.open(encoding="utf-8", newline="") as handle:
        rows = {
            (row["scope"], row["metric"]): row for row in csv.DictReader(handle)
        }
    assert rows[("combined", "candidate_cell_count")]["value"] == "13285"
    assert rows[("combined", "planning_candidate_cell_count")]["value"] == "6720"
    assert rows[("combined", "nested_bootstrap_analysis_count")]["value"] == (
        "15940405800000"
    )
    assert rows[("combined", "persistent_result_bytes")]["value"] == (
        "not_identifiable"
    )

    audit = " ".join(
        (ROOT / "docs/research/simulation_resource_feasibility_audit.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "not resource-qualified" in audit
    assert "no option is selected" in audit
    assert "no project random stream" in audit
    assert "does not establish implementation correctness" in audit


def test_noncore_simulation_design_preserves_gate_and_proof_boundaries() -> None:
    design = " ".join(
        (ROOT / "docs/research/noncore_simulation_computational_design.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    brief = " ".join(
        (ROOT / "docs/research/task_briefs/TB-0010-noncore-simulation-resource-design.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "static proof-obligation candidate" in design
    assert "no benchmark" in design
    assert "k_plan=4,416" in design
    assert "613,093,770,610" in design
    assert "40,601,280,000" in design
    assert "p0-manifest" in design and "p11-resource" in design
    assert "counters alone fail" in design
    assert "1-0.99^{299}>0.95" in design
    assert "2,723,199,652,800,000" in design
    assert "14,503,497,089,155,072" in design
    assert "probability construction" in design
    assert "100-iteration missingness solve" in design
    assert "alpha=0.05/4,416" in design
    assert "numerical parameter" in design
    assert "m_{peak,system}" in design
    assert "t_{worker,hard}" in design
    assert "may not be multiplied by the workload" in design
    assert "g0-method" in design and "owner-blocked" in design
    assert "g0-resources" in design and "remain open" in design
    assert "fewer than 120,000/9,999" in brief
    assert "no external action is authorized except the final" in brief


def test_simulation_output_registry_is_typed_complete_and_reproducible() -> None:
    metrics = metric_fields()
    operations = operation_registry()
    assert len(metrics) == 259
    assert len({field.metric_code for field in metrics}) == len(metrics)
    assert len(operations) == 244
    assert len({operation.operation_code for operation in operations}) == len(
        operations
    )

    metric_by_code = {field.metric_code: field for field in metrics}
    operation_by_code = {
        operation.operation_code: operation for operation in operations
    }
    assert metric_by_code["common.cell.bootstrap_resamples"].logical_type == "U32"
    assert all(
        "N=R=120000" in field.aggregate_rule
        for field in metrics
        if field.record_scope == "cell_aggregate_event"
    )
    assert all(
        "I_complete" in field.applicability
        and "I_complete=1_iff_completion_bitmap_has_all_R_bits" in (
            field.failure_semantics
        )
        for field in metrics
        if field.kind == "reliability"
        and field.record_scope == "cell_aggregate_event"
    )
    assert all(
        "I_complete" in field.applicability
        and "I_complete=1_iff_completion_bitmap_has_all_R_bits" in (
            field.failure_semantics
        )
        for field in metrics
        if field.kind == "mv1"
        and field.record_scope == "cell_aggregate_event"
    )
    assert "I_R3=1_and_I_complete=0=>state_NOT_REACHED" in metric_by_code[
        "rel.aggregate.coverage"
    ].aggregate_rule
    assert "outer_eligibility=ELIGIBLE_and_I_complete=0=>state_NOT_REACHED" in (
        metric_by_code["mv.aggregate.coverage_bal"].aggregate_rule
    )
    rel_undefined = metric_by_code["rel.aggregate.undefined_bootstrap_fraction"]
    assert "I_R3=0_or_I_complete=0=>state_NOT_REACHED_denominator=0" in (
        rel_undefined.aggregate_rule
    )
    assert metric_by_code[
        "rel.exclusion.observed_reader_sensitivities"
    ].occurrence_formula == "0_simulated_occurrences_exact"
    assert "independent_of_SE" in metric_by_code["mv.outer.qhat_bal"].applicability
    assert "VALUE_independent_of_outer_estimability" in metric_by_code[
        "mv.outer.truth_bal"
    ].applicability
    null_false = metric_by_code["mv.aggregate.null_false_qualification"]
    assert "immutable_manifest_null_boundary_member" in null_false.applicability
    assert "I_complete=1" in null_false.applicability
    assert "manifest_target_q_bal" in null_false.aggregate_rule
    assert "membership_independent_of_selected_calibrated_truth" in (
        null_false.aggregate_rule
    )
    false_promotion = metric_by_code["rel.aggregate.false_promotion"]
    assert "alpha<=0.67" in false_promotion.aggregate_rule
    assert "macro<=0.80" in false_promotion.aggregate_rule
    assert "positive<=0.70" in false_promotion.aggregate_rule
    assert "INAPPLICABLE_only_if_resolved_strict_alternative" in (
        false_promotion.applicability
    )

    rel_truth = metric_by_code["rel.cell.truth_positive_41"]
    assert rel_truth.logical_type == "F64[4]"
    assert rel_truth.width_bytes.startswith("33_including_32_payload")
    assert "class_c>=K_g_is_INAPPLICABLE" in rel_truth.state_semantics
    assert "one_independent_2bit_state_per_named_scalar_or_fixed_class_element" in (
        rel_truth.state_semantics
    )
    mv_control = metric_by_code["mv.cell.calibration_control_counts_present"]
    assert mv_control.logical_type.startswith("PACKED40{")
    assert mv_control.width_bytes.startswith("41_including_40_payload")
    assert "discarded_retry_partial_counts_never_enter_this_field" in (
        mv_control.state_semantics
    )
    mv_truth = metric_by_code["mv.cell.truth_bal_present_absent"]
    assert "under_target_truth_choice" in mv_truth.state_semantics
    assert "under_validated_truth_choice" in mv_truth.state_semantics
    assert "inner_alpha_and_final_outer_solution_selection_rules_owner_blocked" in metric_by_code[
        "mv.cell.mu_y"
    ].applicability
    assert metric_by_code["mv.cell.admissible_mean_lower"].status == (
        "owner_blocked"
    )
    assert "signed_yield_residual=estimated_P(E=1_given_Y)-rho_Y" in (
        metric_by_code["mv.cell.candidate_yield_q_residuals"].state_semantics
    )

    required_operations = {
        "common.identifier_dictionary_serializations",
        "common.permutation_dictionary_serializations",
        "common.completion_bitmap_serializations",
        "common.completion_bitmap_bytes",
        "rel.missing_endpoint_residual_evaluations",
        "rel.missing_bracket_checks",
        "rel.missing_residual_evaluations",
        "rel.reader_effect_vector_normalizations",
        "mv.static_reader_vector_normalizations",
        "mv.outer_evaluability_block_reductions",
        "mv.outer_four_of_five_panel_reductions",
        "mv.calibration_open_unit_conversions_replay",
        "mv.calibration_open_unit_conversions_materialize_reconvert",
        "mv.calibration_open_unit_conversions_materialize_cache",
        "mv.calibration_open_unit_cache_bytes",
        "global.cp95_conformance_interval_calls",
        "global.cp95_conformance_beta_quantile_calls",
        "global.cp95_half_width_evaluations",
        "global.cp95_max_argmax_comparisons",
        "global.cp95_threshold_comparisons",
        "rel.outer_point_descriptive_reductions",
        "mv.outer_screen_assignment_tallies",
        "rel.aggregate_proportion_evaluations",
        "rel.aggregate_undefined_bootstrap_fraction_divisions",
        "mv.aggregate_proportion_evaluations",
        "mv.calibration_domain_bound_constructions",
        "mv.calibration_inner_alpha_final_selections",
        "mv.calibration_final_solution_selections",
        "mv.calibration_final_distribution_parameter_constructions",
        "mv.calibration_control_record_assemblies",
        "global.family_execution_attempt_records",
        "global.cp95_execution_attempt_records",
        "global.registry_dictionary_serializations",
        "global.registry_dictionary_bytes",
        "common.chunk_journal_bytes",
        "common.failure_detail_bytes",
        "rel.missing_final_candidate_selection_events",
    }
    assert required_operations <= operation_by_code.keys()
    assert operation_by_code["rel.outer_records"].count_formula == "I_R3*(M_c)"
    assert operation_by_code["mv.outer_records"].count_formula == "M_c"
    assert operation_by_code[
        "rel.outer_point_descriptive_reductions"
    ].count_formula == "I_R3*(M_c)"
    assert operation_by_code["mv.outer_screen_assignment_tallies"].count_formula == (
        "M_c"
    )
    assert operation_by_code["rel.dgp_words_lower"].count_formula.startswith(
        "I_R3*(R*"
    )
    assert operation_by_code["rel.bootstrap_index_words"].count_formula == (
        "I_R3*(R*B*N)"
    )
    assert operation_by_code["mv.dgp_words"].count_formula.startswith("R*")
    for code in (
        "rel.outer_payload_hashes",
        "rel.outer_record_serializations",
        "rel.completion_bitmap_updates",
        "rel.outer_classification_assemblies",
    ):
        assert "M_c" in operation_by_code[code].count_formula
    for code in (
        "mv.outer_payload_hashes",
        "mv.outer_record_serializations",
        "mv.outer_record_bytes",
        "mv.completion_bitmap_updates",
        "mv.outer_classification_assemblies",
    ):
        assert "M_c" in operation_by_code[code].count_formula
    assert operation_by_code["rel.percentile_selections"].bound_type == (
        "conditional_upper_bound"
    )
    assert operation_by_code[
        "rel.missing_endpoint_residual_evaluations"
    ].accounting_role == (
        "diagnostic_component_of_total_residual_evaluations_do_not_add"
    )
    assert operation_by_code["rel.dgp_words_lower"].accounting_role.startswith(
        "envelope_lower_do_not_sum"
    )
    assert operation_by_code[
        "mv.calibration_materialized_words"
    ].accounting_role == "exclusive_calibration_raw_alternative"
    assert operation_by_code[
        "mv.calibration_candidate_vector_evaluations"
    ].count_formula == "2*(1001+80)*(80+2)*2^20"
    assert operation_by_code[
        "mv.calibration_validation_vector_evaluations"
    ].count_formula == "2*2^22"
    assert operation_by_code[
        "mv.calibration_domain_bound_constructions"
    ].count_formula == "I_domain*2"
    assert operation_by_code[
        "mv.calibration_inner_alpha_final_selections"
    ].count_formula == "2*(1001+80)"
    assert "inner_bracket_sign_orientation" in operation_by_code[
        "mv.calibration_inner_alpha_final_selections"
    ].assumption_or_blocker
    assert operation_by_code[
        "mv.calibration_final_solution_selections"
    ].bound_type == "upper_bound"
    assert "zero_based_preceding_index_argmax" in operation_by_code[
        "mv.calibration_monotonicity_comparisons"
    ].assumption_or_blocker
    assert operation_by_code[
        "rel.aggregate_proportion_evaluations"
    ].count_formula == "I_R3*(I_complete*(11+K))"
    assert operation_by_code[
        "rel.aggregate_undefined_bootstrap_fraction_divisions"
    ].count_formula == "I_R3*(I_complete)"
    assert operation_by_code[
        "mv.aggregate_proportion_evaluations"
    ].count_formula == "I_outer*I_complete*17"

    cp95_counts = {
        "global.cp95_conformance_interval_calls": "120001",
        "global.cp95_conformance_beta_quantile_calls": "240000",
        "global.cp95_half_width_evaluations": "120001",
        "global.cp95_max_argmax_comparisons": "120000",
        "global.cp95_threshold_comparisons": "1",
    }
    assert {
        code: operation_by_code[code].count_formula for code in cp95_counts
    } == cp95_counts
    assert "strictly_less_than_0.003" in operation_by_code[
        "global.cp95_threshold_comparisons"
    ].assumption_or_blocker
    assert operation_by_code["rel.family_union_failure_complements"].count_formula == (
        "15"
    )
    assert operation_by_code["rel.family_union_failure_additions"].count_formula == (
        "14"
    )
    assert operation_by_code[
        "rel.family_union_threshold_comparisons"
    ].count_formula == "1"
    assert operation_by_code[
        "global.registry_dictionary_serializations"
    ].count_formula == "4"
    assert operation_by_code["common.chunk_journal_bytes"].bound_type == (
        "unresolved"
    )
    assert "100_midpoint_updates" in operation_by_code[
        "rel.missing_final_candidate_selection_events"
    ].assumption_or_blocker
    assert metric_by_code["rel.cell.missing_bracket_state"].status == (
        "owner_blocked"
    )
    assert metric_by_code[
        "rel.cell.missing_endpoint_lower_residual"
    ].status == "owner_blocked"
    assert "abs_residual_above_1e-10_causes_static_missingness_failure" in (
        metric_by_code["rel.cell.missing_residual"].state_semantics
    )
    assert "VALUE_ENUM8_ALTERNATIVE_iff_final_alpha>0.67" in (
        metric_by_code["rel.cell.null_boundary_class"].state_semantics
    )
    assert "VALUE_ENUM8_BOUNDARY_iff_no_required_component_is_below" in (
        metric_by_code["rel.cell.null_boundary_class"].state_semantics
    )
    assert "VALUE_true_iff_final_alpha>0.80" in metric_by_code[
        "rel.cell.planning_truth_eligibility"
    ].state_semantics
    assert "abs_selected_signed_residual_less_than_or_equal_to_1e-10" in (
        operation_by_code["rel.static_classification_assemblies"].assumption_or_blocker
    )
    assert "inclusive_endpoint_zero_predicate" in operation_by_code[
        "rel.missing_bracket_checks"
    ].assumption_or_blocker
    assert "midpoint_residual_zero_equality" in operation_by_code[
        "rel.missing_midpoint_controls"
    ].assumption_or_blocker
    assert "last_node_emits" in operation_by_code[
        "rel.quadrature_node_reductions"
    ].assumption_or_blocker
    assert "three_lower_bound_assemblies" in operation_by_code[
        "mv.max_t_selections"
    ].semantic_unit
    outer_eligibility = metric_by_code["mv.cell.outer_eligibility"]
    assert "ELIGIBLE=1_NOT_ELIGIBLE=0_INFRASTRUCTURE_INCOMPLETE=2" in (
        outer_eligibility.state_semantics
    )
    assert "I_outer=1_iff_ELIGIBLE_else_0" in outer_eligibility.state_semantics
    assert "outer_eligibility=NOT_ELIGIBLE=>state_NOT_REACHED" in (
        metric_by_code["mv.aggregate.coverage_bal"].aggregate_rule
    )
    assert "outer_eligibility=INFRASTRUCTURE_INCOMPLETE=>state_NOT_REACHED" in (
        metric_by_code["mv.aggregate.coverage_bal"].aggregate_rule
    )
    assert "n_present>=1_and_present_mean_is_finite" in metric_by_code[
        "mv.outer.qhat_present"
    ].failure_semantics
    assert "zero_VALUE_makes_max_t_nonestimable" in metric_by_code[
        "mv.outer.se_present"
    ].failure_semantics
    assert "NOT_REACHED_if_any_prerequisite_is_nonVALUE" in metric_by_code[
        "mv.outer.lower_bal"
    ].failure_semantics
    assert "rank_deficiency" in metric_by_code[
        "mv.outer.fe_present"
    ].failure_semantics
    assert "one_reader_or_component_failure_does_not_erase" in metric_by_code[
        "mv.outer.loo_reader_00_present"
    ].failure_semantics
    axis_argmin = metric_by_code["rel.family.axis_argmin"]
    assert "array_axis_order=image_technical,image_coverage" in (
        axis_argmin.applicability
    )
    assert "smallest_tied_combined_catalogue_index" in axis_argmin.applicability
    assert "never_update_on_exact_binary64_equality" in operation_by_code[
        "rel.family_axis_min_argmin_comparisons"
    ].assumption_or_blocker

    for kind, expected in (("reliability", 32), ("mv1", 64)):
        slots = [
            int(field.slot)
            for field in metrics
            if field.kind == kind and field.record_scope == "outer_core"
        ]
        assert slots == list(range(expected))
        assert all(
            "VALUE|INAPPLICABLE|SCIENTIFIC_UNDEFINED|NOT_REACHED"
            in field.state_semantics
            for field in metrics
            if field.kind == kind and field.record_scope == "outer_core"
        )

    common_codes = {
        field.metric_code
        for field in metrics
        if field.record_scope == "outer_header"
    }
    assert "common.header.failure_component_mask" in common_codes
    assert "common.header.event_mask" in common_codes
    assert "common.header.execution_provenance_key" in common_codes
    assert "common.header.retry_count" not in common_codes
    assert "common.header.attempt_count" not in common_codes
    assert "common.header.infrastructure_failure_ref" not in common_codes
    assert "mutable_attempt_retry_and_infrastructure_provenance_lives_only" in (
        metric_by_code["common.header.execution_provenance_key"].failure_semantics
    )
    assert "digest_slot_canonical_zero" in metric_by_code[
        "common.header.payload_digest"
    ].failure_semantics
    sidecar = metric_by_code["common.execution.attempt"]
    assert sidecar.logical_type.startswith("FIXED32{")
    assert sidecar.width_bytes == "32"
    for rule in (
        "outer_range_join_requires_same_global_cell_index",
        "identity_count_positive",
        "identity_count=1",
        "attempt_ordinal_is_contiguous_zero_based_U16",
        "positive_refs_are_partition_local",
    ):
        assert rule in sidecar.aggregate_rule
    assert "whole_polarity_is_atomic_calibration_retry_unit" in operation_by_code[
        "mv.execution_attempt_records"
    ].assumption_or_blocker
    assert "mutable_execution_sidecar_excluded" in operation_by_code[
        "mv.outer_payload_hashes"
    ].assumption_or_blocker
    assert "digest_slot_canonical_zero" in metric_by_code[
        "common.file.content_digest"
    ].failure_semantics
    assert "combined_manifest_sha256" in metric_by_code[
        "common.cell.catalogue_index"
    ].aggregate_rule
    assert metric_by_code["common.aggregate.record"].logical_type.startswith(
        "FIXED16{"
    )

    for code in ("rel.family.family_decision", "mv.family.family_decision"):
        assert "precedence_FAIL" in metric_by_code[code].aggregate_rule
        assert "else_INCOMPLETE" in metric_by_code[code].aggregate_rule
        assert "else_PASS" in metric_by_code[code].aggregate_rule
    assert "disjoint_from_failed_inventory" in metric_by_code[
        "rel.family.infrastructure_missing_member_inventory"
    ].aggregate_rule
    assert "disjoint_from_both_failure_inventories" in metric_by_code[
        "mv.family.infrastructure_missing_member_inventory"
    ].aggregate_rule
    assert any(
        field.status == "owner_blocked"
        and "never_assume_zero" in field.storage_action
        for field in metrics
    )

    commands = {
        "simulation_metric_registry.csv": ["--registry", "metrics"],
        "simulation_operation_registry.csv": ["--registry", "operations"],
        "simulation_semantic_count_ledger_summary.csv": [],
    }
    for filename, arguments in commands.items():
        generated = subprocess.run(
            [
                sys.executable,
                "scripts/compile_simulation_semantic_count_ledger.py",
                *arguments,
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        assert generated == (ROOT / "reports/tables" / filename).read_text(
            encoding="utf-8"
        )


def test_simulation_semantic_ledger_identity_and_storage_correction() -> None:
    row_count, digest = ledger_identity()
    assert row_count == 1_242_518
    assert digest == (
        "b25e9cdf4e61280de02d1187675023632895060c8c9c40cc60c56921a97fb507"
    )

    table_path = (
        ROOT / "reports/tables/simulation_semantic_count_ledger_summary.csv"
    )
    with table_path.open(encoding="utf-8", newline="") as handle:
        rows = {
            (row["scope"], row["metric"]): row for row in csv.DictReader(handle)
        }
    assert rows[("schema", "common_outer_prefix_bytes")]["value"] == "72"
    assert rows[("schema", "reliability_outer_record_bytes")]["value"] == "336"
    assert rows[("schema", "mv1_outer_record_bytes")]["value"] == "600"
    assert rows[("schema", "full_candidate_success_core_floor_bytes")][
        "value"
    ] == "613093770610"
    assert rows[("schema", "core_floor_increase_bytes")]["value"] == (
        "40601280000"
    )
    assert rows[("schema", "final_persistent_output_upper_bytes")][
        "value"
    ] == "not_identifiable"
    assert rows[("manifest", "combined_manifest_sha256")]["value"] == (
        "4e914a602b418c7fbbcccb1e98d9f09a3d339009e9c2befcdd098e34604695a0"
    )
    assert rows[("registry", "metric_row_count")]["value"] == "259"
    assert rows[("registry", "operation_row_count")]["value"] == "244"
    assert rows[("registry", "metric_registry_sha256")]["value"] == (
        "a8c9c1a035d595ad22d3c1d77b6f789d5f25cd61f92f23551315ec83b867baf1"
    )
    assert rows[("registry", "operation_registry_sha256")]["value"] == (
        "d1a85128cb5ab94ec64074dac21d6c53b1bcd6cd7256bf3e68a94ad8d2e347ff"
    )
    assert rows[("ledger", "per_cell_row_count")]["value"] == "1242518"
    assert rows[("ledger", "per_cell_ledger_sha256")]["value"] == (
        "b25e9cdf4e61280de02d1187675023632895060c8c9c40cc60c56921a97fb507"
    )
    assert rows[("blocker", "reliability_missingness_bisection_rule")][
        "value"
    ] == "owner_decision_required"
    assert rows[
        (
            "blocker",
            "mv1_numerical_domain_inner_and_outer_solution_truth_and_trace",
        )
    ]["value"] == "owner_decision_required"

    registry = " ".join(
        (ROOT / "docs/research/simulation_output_and_operation_registry.md")
        .read_text(encoding="utf-8")
        .lower()
        .split()
    )
    assert "complete static freeze candidate" in registry
    assert "gate outcomes are events" in registry
    assert "nan never encodes state" in registry
    assert "observed-reader only" in registry
    assert "not a final output upper bound" in registry
    assert "gate 0 remain open" in registry
    assert "i_complete=1" in registry
    assert "whole-polarity replay" in registry
    assert "state/event and retry-join semantics" in registry
