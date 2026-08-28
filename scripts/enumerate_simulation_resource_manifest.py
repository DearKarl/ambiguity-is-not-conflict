"""Enumerate the TB-0008 simulation-candidate manifests and logical work.

This script is protocol compilation only.  It uses the Python standard
library, opens no project random stream, generates no synthetic observation,
evaluates no DGP, and runs no bootstrap or hardware benchmark.  By default it
prints the aggregate resource ledger.  ``--manifest`` prints canonical cells
for independent inspection without writing a full manifest to the repository.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from dataclasses import dataclass, field
from typing import Iterable, TextIO


OUTER_REPLICATIONS = 120_000
BOOTSTRAP_RESAMPLES = 9_999
CALIBRATION_VECTORS = 2**20
VALIDATION_VECTORS = 2**22
CALIBRATION_MEAN_GRID = 1_001
CALIBRATION_BISECTIONS = 80


@dataclass(frozen=True)
class Axis:
    identifier: str
    categories: int
    included_items: int
    panel_size: int
    instrument_repeat_ratings: int


AXES = (
    Axis("image_technical", 3, 150, 5, 120),
    Axis("image_coverage", 3, 150, 5, 120),
    Axis("image_semantic", 3, 150, 5, 120),
    Axis("image_polarity", 2, 90, 5, 120),
    Axis("text_integrity", 4, 150, 5, 114),
    Axis("text_target_polarity", 4, 150, 5, 114),
    Axis("text_commitment", 3, 130, 5, 114),
    Axis("text_interpretation", 3, 150, 5, 114),
    Axis("text_derived_polarity", 2, 80, 5, 114),
    Axis("pair_atomicity", 2, 150, 3, 72),
    Axis("pair_preservation", 2, 150, 3, 72),
    Axis("pair_fluency", 2, 150, 3, 72),
    Axis("pair_plausibility", 2, 150, 3, 72),
    Axis("pair_nonsemantic_cues", 2, 150, 3, 72),
    Axis("pair_global", 2, 150, 3, 72),
)


RELIABILITY_KEYS = (
    "kind",
    "n",
    "allocation",
    "stressed_axis",
    "prevalence_class",
    "prevalence_fraction",
    "accuracy",
    "accuracy_mode",
    "accuracy_class",
    "confusion_mode",
    "reader_sd",
    "item_sd",
    "missingness_rate",
    "missingness_mode",
    "missingness_class",
    "repeat_stability",
)

MV_KEYS = (
    "kind",
    "n",
    "screen_fidelity_present",
    "screen_fidelity_absent",
    "yield_present",
    "yield_absent",
    "q_present",
    "q_absent",
    "q_distribution",
    "q_sd",
    "probability_reader_sd",
    "rating_noise_sd",
    "state_reader_sd",
    "patient_state_sd",
    "state_correct_probability",
    "opposite_error_fraction",
    "selection_slope",
)


@dataclass
class ManifestEntry:
    cell: dict[str, str]
    families: set[str] = field(default_factory=set)


@dataclass
class Manifest:
    entries: dict[str, ManifestEntry] = field(default_factory=dict)
    attempted_insertions: int = 0

    def add(self, cell: dict[str, str], family: str) -> None:
        self.attempted_insertions += 1
        identifier = canonical_cell_id(cell)
        entry = self.entries.get(identifier)
        if entry is None:
            self.entries[identifier] = ManifestEntry(dict(cell), {family})
        else:
            if entry.cell != cell:
                raise AssertionError("canonical identifier collision")
            entry.families.add(family)


def canonical_cell_id(cell: dict[str, str]) -> str:
    """Return the contract's compact, sorted UTF-8 JSON identifier."""

    return json.dumps(
        cell,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _updated(cell: dict[str, str], **updates: str) -> dict[str, str]:
    result = dict(cell)
    result.update(updates)
    return result


def _reliability_base(axis: Axis) -> dict[str, str]:
    return {
        "kind": "reliability",
        "n": "150",
        "allocation": "printed",
        "stressed_axis": axis.identifier,
        "prevalence_class": "none",
        "prevalence_fraction": "none",
        "accuracy": "0.90",
        "accuracy_mode": "common",
        "accuracy_class": "none",
        "confusion_mode": "symmetric",
        "reader_sd": "0.25",
        "item_sd": "0.50",
        "missingness_rate": "0.05",
        "missingness_mode": "mcar",
        "missingness_class": "none",
        "repeat_stability": "0.85",
    }


def _categories(axis: Axis) -> tuple[str, ...]:
    return tuple(f"{axis.identifier}:c{index}" for index in range(axis.categories))


def _missingness_modes(axis: Axis) -> tuple[tuple[str, str], ...]:
    return (
        ("mcar", "none"),
        ("reader", "none"),
        *(("class", category) for category in _categories(axis)),
    )


def build_reliability_manifest() -> Manifest:
    """Compile the prospectively clarified reliability scenario union."""

    manifest = Manifest()
    for axis in AXES:
        base = _reliability_base(axis)
        manifest.add(base, "reference")

        # One-factor family.  Accuracy crosses every printed common-accuracy
        # level with every designated-low class.  At zero missingness this
        # family keeps one behaviorally representative MCAR row; at each
        # nonzero rate it crosses all named modes and class targets.
        for category in _categories(axis):
            for fraction in ("0.10", "0.15", "0.20"):
                manifest.add(
                    _updated(
                        base,
                        allocation="designated_prevalence",
                        prevalence_class=category,
                        prevalence_fraction=fraction,
                    ),
                    "one_factor",
                )
        for accuracy in ("0.75", "0.80", "0.85", "0.90", "0.95"):
            manifest.add(_updated(base, accuracy=accuracy), "one_factor")
            for category in _categories(axis):
                manifest.add(
                    _updated(
                        base,
                        accuracy=accuracy,
                        accuracy_mode="designated_low",
                        accuracy_class=category,
                    ),
                    "one_factor",
                )
        for reader_sd in ("0.00", "0.25", "0.50", "0.75"):
            manifest.add(_updated(base, reader_sd=reader_sd), "one_factor")
        for item_sd in ("0.00", "0.50", "1.00"):
            manifest.add(_updated(base, item_sd=item_sd), "one_factor")
        manifest.add(_updated(base, missingness_rate="0.00"), "one_factor")
        for missingness_rate in ("0.05", "0.10"):
            for mode, category in _missingness_modes(axis):
                manifest.add(
                    _updated(
                        base,
                        missingness_rate=missingness_rate,
                        missingness_mode=mode,
                        missingness_class=category,
                    ),
                    "one_factor",
                )
        for repeat_stability in ("0.75", "0.85", "0.95"):
            manifest.add(
                _updated(base, repeat_stability=repeat_stability),
                "one_factor",
            )
        for confusion_mode in ("symmetric", "directed"):
            manifest.add(
                _updated(base, confusion_mode=confusion_mode),
                "one_factor",
            )

        # Adversarial family: the printed fully crossed nonzero-missingness set.
        for category in _categories(axis):
            for accuracy in ("0.80", "0.90"):
                for reader_sd in ("0.25", "0.75"):
                    for item_sd in ("0.50", "1.00"):
                        for missingness_rate in ("0.05", "0.10"):
                            for confusion_mode in ("symmetric", "directed"):
                                for mode, missing_category in _missingness_modes(axis):
                                    manifest.add(
                                        _updated(
                                            base,
                                            allocation="designated_prevalence",
                                            prevalence_class=category,
                                            prevalence_fraction="0.10",
                                            accuracy=accuracy,
                                            reader_sd=reader_sd,
                                            item_sd=item_sd,
                                            missingness_rate=missingness_rate,
                                            missingness_mode=mode,
                                            missingness_class=missing_category,
                                            confusion_mode=confusion_mode,
                                        ),
                                        "adversarial",
                                    )

        # Planning family retains the literal printed Cartesian mode labels at
        # m=0 as distinct rows because they enter K_plan and its Bonferroni
        # guarantee, even though their generated missingness is identical.
        for accuracy in ("0.90", "0.95"):
            for reader_sd in ("0.00", "0.25"):
                for item_sd in ("0.00", "0.50"):
                    for missingness_rate in ("0.00", "0.05"):
                        for repeat_stability in ("0.85", "0.95"):
                            for confusion_mode in ("symmetric", "directed"):
                                for mode, category in _missingness_modes(axis):
                                    manifest.add(
                                        _updated(
                                            base,
                                            accuracy=accuracy,
                                            reader_sd=reader_sd,
                                            item_sd=item_sd,
                                            missingness_rate=missingness_rate,
                                            missingness_mode=mode,
                                            missingness_class=category,
                                            repeat_stability=repeat_stability,
                                            confusion_mode=confusion_mode,
                                        ),
                                        "planning",
                                    )

    _assert_cell_schema(manifest, RELIABILITY_KEYS)
    return manifest


def _mv_base() -> dict[str, str]:
    return {
        "kind": "mv1",
        "n": "150",
        "screen_fidelity_present": "0.90",
        "screen_fidelity_absent": "0.90",
        "yield_present": "0.85",
        "yield_absent": "0.85",
        "q_present": "0.20",
        "q_absent": "0.20",
        "q_distribution": "beta",
        "q_sd": "0.15",
        "probability_reader_sd": "0.05",
        "rating_noise_sd": "0.07",
        "state_reader_sd": "0.25",
        "patient_state_sd": "0.50",
        "state_correct_probability": "0.95",
        "opposite_error_fraction": "0.50",
        "selection_slope": "-1",
    }


FIDELITY_PAIRS = (
    ("0.75", "0.75"),
    ("0.80", "0.80"),
    ("0.90", "0.90"),
    ("0.95", "0.95"),
    ("0.75", "0.90"),
    ("0.90", "0.75"),
)
YIELD_PAIRS = (
    ("0.70", "0.70"),
    ("0.75", "0.75"),
    ("0.80", "0.80"),
    ("0.85", "0.85"),
    ("0.90", "0.90"),
    ("0.75", "0.90"),
    ("0.90", "0.75"),
)
Q_TARGETS = (
    ("0.10", "0.10"),
    ("0.20", "0.00"),
    ("0.00", "0.20"),
    ("0.30", "0.00"),
    ("0.00", "0.30"),
    ("0.15", "0.05"),
    ("0.20", "0.20"),
    ("0.25", "0.15"),
    ("0.15", "0.25"),
    ("0.30", "0.10"),
)
Q_DISTRIBUTIONS = (
    ("beta", "0.15"),
    ("beta", "0.25"),
    ("two_point", "none"),
)


def _mv_pair(
    base: dict[str, str],
    first_key: str,
    second_key: str,
    pair: tuple[str, str],
) -> dict[str, str]:
    return _updated(base, **{first_key: pair[0], second_key: pair[1]})


def build_mv_manifest() -> Manifest:
    """Compile the pre-calibration MV candidate union.

    All three declared q-distribution parameterizations are enumerated.  A
    later authorized calibration determines which candidate cells are outer-
    eligible; this compiler never guesses that outcome.
    """

    manifest = Manifest()
    base = _mv_base()
    manifest.add(base, "reference")

    for pair in FIDELITY_PAIRS:
        manifest.add(
            _mv_pair(
                base,
                "screen_fidelity_present",
                "screen_fidelity_absent",
                pair,
            ),
            "one_factor",
        )
    for pair in YIELD_PAIRS:
        manifest.add(
            _mv_pair(base, "yield_present", "yield_absent", pair),
            "one_factor",
        )
    for pair in Q_TARGETS:
        manifest.add(
            _mv_pair(base, "q_present", "q_absent", pair),
            "one_factor",
        )
    for distribution, q_sd in Q_DISTRIBUTIONS:
        manifest.add(
            _updated(base, q_distribution=distribution, q_sd=q_sd),
            "one_factor",
        )
    scalar_factors = {
        "probability_reader_sd": ("0.00", "0.02", "0.05", "0.10"),
        "rating_noise_sd": ("0.03", "0.07", "0.10"),
        "state_reader_sd": ("0.00", "0.25", "0.50"),
        "patient_state_sd": ("0.00", "0.50"),
        "state_correct_probability": ("0.90", "0.95", "0.99"),
        "opposite_error_fraction": ("0.25", "0.50"),
        "selection_slope": ("0", "-1", "-2"),
        "n": ("128", "150"),
    }
    for factor, values in scalar_factors.items():
        for value in values:
            manifest.add(_updated(base, **{factor: value}), "one_factor")

    # Null-boundary family.  These are exactly the six printed pairs having a
    # balanced boundary of 0.10 or a zero polarity component.
    for q_pair in Q_TARGETS[:6]:
        for n in ("128", "150"):
            for distribution, q_sd in Q_DISTRIBUTIONS:
                for slope in ("0", "-1", "-2"):
                    cell = _mv_pair(base, "q_present", "q_absent", q_pair)
                    manifest.add(
                        _updated(
                            cell,
                            n=n,
                            q_distribution=distribution,
                            q_sd=q_sd,
                            selection_slope=slope,
                        ),
                        "null_boundary",
                    )

    # The prospective clarification freezes every unmentioned asymmetric-set
    # factor at the reference value.
    for fidelity in (("0.75", "0.90"), ("0.90", "0.75")):
        for pair_yield in (("0.75", "0.90"), ("0.90", "0.75")):
            for q_pair in (("0.25", "0.15"), ("0.15", "0.25")):
                cell = _mv_pair(
                    base,
                    "screen_fidelity_present",
                    "screen_fidelity_absent",
                    fidelity,
                )
                cell = _mv_pair(cell, "yield_present", "yield_absent", pair_yield)
                cell = _mv_pair(cell, "q_present", "q_absent", q_pair)
                manifest.add(cell, "asymmetric")

    for fidelity in (("0.90", "0.90"), ("0.95", "0.95")):
        for pair_yield in (("0.85", "0.85"), ("0.90", "0.90")):
            for q_pair in (("0.20", "0.20"), ("0.25", "0.15"), ("0.15", "0.25")):
                for probability_sd in ("0.00", "0.02", "0.05"):
                    for noise_sd in ("0.03", "0.07"):
                        for state_sd in ("0.00", "0.25"):
                            for patient_sd in ("0.00", "0.50"):
                                for correct in ("0.95", "0.99"):
                                    for opposite in ("0.25", "0.50"):
                                        for slope in ("0", "-1"):
                                            cell = _mv_pair(
                                                base,
                                                "screen_fidelity_present",
                                                "screen_fidelity_absent",
                                                fidelity,
                                            )
                                            cell = _mv_pair(
                                                cell,
                                                "yield_present",
                                                "yield_absent",
                                                pair_yield,
                                            )
                                            cell = _mv_pair(
                                                cell,
                                                "q_present",
                                                "q_absent",
                                                q_pair,
                                            )
                                            manifest.add(
                                                _updated(
                                                    cell,
                                                    probability_reader_sd=probability_sd,
                                                    rating_noise_sd=noise_sd,
                                                    state_reader_sd=state_sd,
                                                    patient_state_sd=patient_sd,
                                                    state_correct_probability=correct,
                                                    opposite_error_fraction=opposite,
                                                    selection_slope=slope,
                                                ),
                                                "planning",
                                            )

    _assert_cell_schema(manifest, MV_KEYS)
    return manifest


def _assert_cell_schema(manifest: Manifest, keys: tuple[str, ...]) -> None:
    expected = set(keys)
    for entry in manifest.entries.values():
        if set(entry.cell) != expected:
            raise AssertionError(
                f"schema mismatch: {sorted(entry.cell)} != {sorted(expected)}"
            )
        if not all(isinstance(value, str) for value in entry.cell.values()):
            raise AssertionError("every canonical scalar must be a JSON string")


def manifest_sha256(entries: dict[str, ManifestEntry]) -> str:
    payload = "".join(f"{identifier}\n" for identifier in sorted(entries))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _family_count(manifest: Manifest, family: str) -> int:
    return sum(family in entry.families for entry in manifest.entries.values())


def _multi_family_count(manifest: Manifest) -> int:
    return sum(len(entry.families) > 1 for entry in manifest.entries.values())


def _canonical_bytes(manifest: Manifest) -> int:
    return sum(len(identifier.encode("utf-8")) + 1 for identifier in manifest.entries)


def _axis_entries(manifest: Manifest, axis: Axis) -> list[ManifestEntry]:
    return [
        entry
        for entry in manifest.entries.values()
        if entry.cell["stressed_axis"] == axis.identifier
    ]


def _axis_cell_count(manifest: Manifest, axis: Axis, family: str | None = None) -> int:
    entries = _axis_entries(manifest, axis)
    if family is None:
        return len(entries)
    return sum(family in entry.families for entry in entries)


def _nested(count: int) -> int:
    return count * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES


def _mv_dgp_words_per_outer(n: int) -> int:
    first_presentations = 2 * n * 10
    first_words = 2 * n * 3 + first_presentations * 3
    repeats_per_reader = (3 * n + 9) // 10  # ceil(0.15 * 2n)
    repeat_words = 10 * repeats_per_reader * 4
    return first_words + repeat_words


def _row(
    scope: str,
    metric: str,
    value: int | str,
    unit: str,
    bound_type: str,
    assumption_scope: str,
) -> tuple[str, str, str, str, str, str]:
    return (
        scope,
        metric,
        str(value),
        unit,
        bound_type,
        assumption_scope,
    )


def summary_rows() -> list[tuple[str, str, str, str, str, str]]:
    reliability = build_reliability_manifest()
    mv = build_mv_manifest()
    rows: list[tuple[str, str, str, str, str, str]] = []

    rel_cells = len(reliability.entries)
    rel_plan = _family_count(reliability, "planning")
    rel_cell_items = sum(
        _axis_cell_count(reliability, axis) * axis.included_items for axis in AXES
    )
    rel_plan_items = sum(
        _axis_cell_count(reliability, axis, "planning") * axis.included_items
        for axis in AXES
    )
    rows.extend(
        (
            _row("reliability", "axis_count", len(AXES), "axes", "exact", "canonical_grid"),
            _row(
                "reliability",
                "category_count_sum",
                sum(axis.categories for axis in AXES),
                "axis_categories",
                "exact",
                "canonical_grid",
            ),
            _row("reliability", "candidate_cell_count", rel_cells, "cells", "exact", "clarified_union"),
            _row("reliability", "planning_cell_count", rel_plan, "cells", "exact", "literal_planning_cartesian"),
            _row("reliability", "reference_family_count", _family_count(reliability, "reference"), "cells", "exact", "family_membership"),
            _row("reliability", "one_factor_family_count", _family_count(reliability, "one_factor"), "cells", "exact", "family_membership"),
            _row("reliability", "adversarial_family_count", _family_count(reliability, "adversarial"), "cells", "exact", "family_membership"),
            _row("reliability", "planning_family_count", rel_plan, "cells", "exact", "family_membership"),
            _row("reliability", "attempted_insertions", reliability.attempted_insertions, "insertions", "exact", "enumerator"),
            _row("reliability", "deduplicated_insertions", reliability.attempted_insertions - rel_cells, "insertions", "exact", "canonical_id"),
            _row("reliability", "multi_family_cell_count", _multi_family_count(reliability), "cells", "exact", "family_provenance"),
            _row("reliability", "manifest_sha256", manifest_sha256(reliability.entries), "sha256", "exact", "sorted_ids_newline_terminated"),
            _row("reliability", "canonical_id_payload_bytes", _canonical_bytes(reliability), "bytes", "exact", "utf8_ids_plus_newlines"),
            _row("reliability", "cell_item_count", rel_cell_items, "cell_items", "exact", "axis_specific_included_items"),
            _row("reliability", "planning_cell_item_count", rel_plan_items, "cell_items", "exact", "axis_specific_included_items"),
            _row("reliability", "outer_dataset_count", rel_cells * OUTER_REPLICATIONS, "outer_datasets", "exact", "all_candidates_fixed_count"),
            _row("reliability", "planning_outer_dataset_count", rel_plan * OUTER_REPLICATIONS, "outer_datasets", "exact", "planning_cells_fixed_count"),
            _row("reliability", "nested_bootstrap_analysis_count", _nested(rel_cells), "bootstrap_analyses", "exact", "all_candidates_fixed_count"),
            _row("reliability", "planning_nested_bootstrap_analysis_count", _nested(rel_plan), "bootstrap_analyses", "exact", "planning_cells_fixed_count"),
            _row("reliability", "bootstrap_index_word_count", rel_cell_items * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "exact", "fixed_stratified_cluster_resamples"),
            _row("reliability", "planning_bootstrap_index_word_count", rel_plan_items * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "exact", "fixed_stratified_cluster_resamples"),
            _row("reliability", "quadrature_node_evaluation_count", rel_cells * (41 + 61), "node_evaluations", "exact", "two_declared_orders_per_cell"),
        )
    )

    rel_dgp_lower_per_sweep = 0
    rel_dgp_upper_per_sweep = 0
    rel_plan_lower_per_sweep = 0
    rel_plan_upper_per_sweep = 0
    for axis in AXES:
        axis_count = _axis_cell_count(reliability, axis)
        axis_plan = _axis_cell_count(reliability, axis, "planning")
        first_pass = axis.included_items + 2 * axis.included_items * axis.panel_size
        upper_pass = (
            first_pass
            + axis.included_items
            + 3 * axis.instrument_repeat_ratings
        )
        rel_dgp_lower_per_sweep += axis_count * first_pass
        rel_dgp_upper_per_sweep += axis_count * upper_pass
        rel_plan_lower_per_sweep += axis_plan * first_pass
        rel_plan_upper_per_sweep += axis_plan * upper_pass
        rows.extend(
            (
                _row("reliability_axis", f"{axis.identifier}_candidate_cells", axis_count, "cells", "exact", f"K={axis.categories};N={axis.included_items}"),
                _row("reliability_axis", f"{axis.identifier}_planning_cells", axis_plan, "cells", "exact", f"K={axis.categories};N={axis.included_items}"),
            )
        )
    rows.extend(
        (
            _row("reliability", "dgp_raw_word_count_lower", rel_dgp_lower_per_sweep * OUTER_REPLICATIONS, "uint64_words", "lower_bound", "first_pass_only;repeat_and_ambiguity_schedule_not_frozen_per_axis"),
            _row("reliability", "dgp_raw_word_count_upper", rel_dgp_upper_per_sweep * OUTER_REPLICATIONS, "uint64_words", "upper_bound", "all_axis_items_get_ambiguity_draw;all_instrument_repeats_consumed"),
            _row("reliability", "planning_dgp_raw_word_count_lower", rel_plan_lower_per_sweep * OUTER_REPLICATIONS, "uint64_words", "lower_bound", "first_pass_only"),
            _row("reliability", "planning_dgp_raw_word_count_upper", rel_plan_upper_per_sweep * OUTER_REPLICATIONS, "uint64_words", "upper_bound", "all_axis_items_get_ambiguity_draw;all_instrument_repeats_consumed"),
        )
    )

    mv_cells = len(mv.entries)
    mv_plan = _family_count(mv, "planning")
    n_counts = {
        n: sum(entry.cell["n"] == n for entry in mv.entries.values())
        for n in ("128", "150")
    }
    candidate_units = sum(
        2 * int(entry.cell["n"]) for entry in mv.entries.values()
    )
    planning_candidate_units = sum(
        2 * int(entry.cell["n"])
        for entry in mv.entries.values()
        if "planning" in entry.families
    )
    mv_outer_upper = mv_cells * OUTER_REPLICATIONS
    mv_plan_outer = mv_plan * OUTER_REPLICATIONS
    calibration_raw_per_cell = (
        2 * (CALIBRATION_VECTORS + VALIDATION_VECTORS) * 32
    )
    calibration_vector_evaluations_per_pass_cell = 2 * (
        (CALIBRATION_MEAN_GRID + CALIBRATION_BISECTIONS)
        * (CALIBRATION_BISECTIONS + 2)
        * CALIBRATION_VECTORS
        + VALIDATION_VECTORS
    )
    mv_dgp_upper_per_sweep = sum(
        _mv_dgp_words_per_outer(int(entry.cell["n"]))
        for entry in mv.entries.values()
    )
    mv_plan_dgp_per_sweep = sum(
        _mv_dgp_words_per_outer(int(entry.cell["n"]))
        for entry in mv.entries.values()
        if "planning" in entry.families
    )
    rows.extend(
        (
            _row("mv1", "candidate_cell_count", mv_cells, "cells", "exact", "precalibration_union"),
            _row("mv1", "outer_eligible_cell_count", "not_identifiable", "cells", "unresolved", "requires_forbidden_calibration"),
            _row("mv1", "planning_candidate_cell_count", mv_plan, "cells", "exact", "precalibration_planning_region"),
            _row("mv1", "reference_family_count", _family_count(mv, "reference"), "cells", "exact", "family_membership"),
            _row("mv1", "one_factor_family_count", _family_count(mv, "one_factor"), "cells", "exact", "family_membership"),
            _row("mv1", "null_boundary_family_count", _family_count(mv, "null_boundary"), "cells", "exact", "family_membership"),
            _row("mv1", "asymmetric_family_count", _family_count(mv, "asymmetric"), "cells", "exact", "family_membership"),
            _row("mv1", "planning_family_count", mv_plan, "cells", "exact", "family_membership"),
            _row("mv1", "attempted_insertions", mv.attempted_insertions, "insertions", "exact", "enumerator"),
            _row("mv1", "deduplicated_insertions", mv.attempted_insertions - mv_cells, "insertions", "exact", "canonical_id"),
            _row("mv1", "multi_family_cell_count", _multi_family_count(mv), "cells", "exact", "family_provenance"),
            _row("mv1", "manifest_sha256", manifest_sha256(mv.entries), "sha256", "exact", "sorted_ids_newline_terminated"),
            _row("mv1", "canonical_id_payload_bytes", _canonical_bytes(mv), "bytes", "exact", "utf8_ids_plus_newlines"),
            _row("mv1", "n128_candidate_cell_count", n_counts["128"], "cells", "exact", "precalibration_union"),
            _row("mv1", "n150_candidate_cell_count", n_counts["150"], "cells", "exact", "precalibration_union"),
            _row("mv1", "candidate_unit_count_per_cell_sweep", candidate_units, "candidates", "exact", "two_screen_strata"),
            _row("mv1", "outer_dataset_count", mv_outer_upper, "outer_datasets", "upper_bound", "all_candidate_cells_calibrate"),
            _row("mv1", "planning_outer_dataset_count", mv_plan_outer, "outer_datasets", "upper_bound", "all_planning_candidates_calibrate"),
            _row("mv1", "nested_bootstrap_analysis_count", mv_outer_upper * BOOTSTRAP_RESAMPLES, "bootstrap_analyses", "upper_bound", "all_candidate_cells_outer_eligible"),
            _row("mv1", "planning_nested_bootstrap_analysis_count", mv_plan_outer * BOOTSTRAP_RESAMPLES, "bootstrap_analyses", "upper_bound", "all_planning_cells_outer_eligible"),
            _row("mv1", "bootstrap_index_word_count", candidate_units * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "upper_bound", "every_candidate_evaluable_in_every_outer_replication"),
            _row("mv1", "planning_bootstrap_index_word_count", planning_candidate_units * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "upper_bound", "every_candidate_evaluable_in_every_outer_replication"),
            _row("mv1", "calibration_raw_words_per_candidate_cell", calibration_raw_per_cell, "uint64_words", "upper_bound", "both_polarities_calibration_plus_validation_streams"),
            _row("mv1", "calibration_raw_word_count", calibration_raw_per_cell * mv_cells, "uint64_words", "upper_bound", "every_candidate_reaches_validation"),
            _row("mv1", "planning_calibration_raw_word_count", calibration_raw_per_cell * mv_plan, "uint64_words", "upper_bound", "every_planning_candidate_reaches_validation"),
            _row("mv1", "calibration_vector_evaluations_per_pass_cell", calibration_vector_evaluations_per_pass_cell, "candidate_vector_evaluations", "exact_pass_path", "1081_alpha_solves_x82_evaluations;validation;two_polarities"),
            _row("mv1", "calibration_vector_evaluation_count", calibration_vector_evaluations_per_pass_cell * mv_cells, "candidate_vector_evaluations", "upper_bound", "every_candidate_completes_pass_path"),
            _row("mv1", "planning_calibration_vector_evaluation_count", calibration_vector_evaluations_per_pass_cell * mv_plan, "candidate_vector_evaluations", "upper_bound", "every_planning_candidate_completes_pass_path"),
            _row("mv1", "dgp_raw_word_count", mv_dgp_upper_per_sweep * OUTER_REPLICATIONS, "uint64_words", "upper_bound", "all_candidate_cells_outer_eligible"),
            _row("mv1", "planning_dgp_raw_word_count", mv_plan_dgp_per_sweep * OUTER_REPLICATIONS, "uint64_words", "upper_bound", "all_planning_cells_outer_eligible"),
        )
    )

    combined_entries = dict(reliability.entries)
    overlap = set(combined_entries).intersection(mv.entries)
    if overlap:
        raise AssertionError("kind-specific manifests unexpectedly overlap")
    combined_entries.update(mv.entries)
    combined_cells = rel_cells + mv_cells
    combined_plan = rel_plan + mv_plan
    rows.extend(
        (
            _row("combined", "candidate_cell_count", combined_cells, "cells", "exact", "reliability_plus_precalibration_mv1"),
            _row("combined", "planning_candidate_cell_count", combined_plan, "cells", "exact", "reliability_plus_precalibration_mv1"),
            _row("combined", "manifest_sha256", manifest_sha256(combined_entries), "sha256", "exact", "sorted_ids_newline_terminated"),
            _row("combined", "canonical_id_payload_bytes", _canonical_bytes(reliability) + _canonical_bytes(mv), "bytes", "exact", "utf8_ids_plus_newlines"),
            _row("combined", "outer_dataset_count", rel_cells * OUTER_REPLICATIONS + mv_outer_upper, "outer_datasets", "upper_bound", "all_mv_candidates_calibrate"),
            _row("combined", "planning_outer_dataset_count", rel_plan * OUTER_REPLICATIONS + mv_plan_outer, "outer_datasets", "upper_bound", "all_mv_planning_candidates_calibrate"),
            _row("combined", "nested_bootstrap_analysis_count", _nested(rel_cells) + mv_outer_upper * BOOTSTRAP_RESAMPLES, "bootstrap_analyses", "upper_bound", "all_mv_candidates_outer_eligible"),
            _row("combined", "planning_nested_bootstrap_analysis_count", _nested(rel_plan) + mv_plan_outer * BOOTSTRAP_RESAMPLES, "bootstrap_analyses", "upper_bound", "all_mv_planning_candidates_outer_eligible"),
            _row("combined", "bootstrap_index_word_count", (rel_cell_items + candidate_units) * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "upper_bound", "all_mv_candidates_evaluable"),
            _row("combined", "planning_bootstrap_index_word_count", (rel_plan_items + planning_candidate_units) * OUTER_REPLICATIONS * BOOTSTRAP_RESAMPLES, "uint64_words", "upper_bound", "all_mv_planning_candidates_evaluable"),
            _row("combined", "persistent_result_bytes", "not_identifiable", "bytes", "unresolved", "result_schema;precision;compression;checkpoint_policy_not_frozen"),
            _row("combined", "cpu_core_hours", "not_identifiable", "cpu_core_hours", "unresolved", "implementation_and_benchmark_required"),
            _row("combined", "peak_ram_bytes", "not_identifiable", "bytes", "unresolved", "implementation_and_batching_required"),
            _row("combined", "scratch_bytes", "not_identifiable", "bytes", "unresolved", "implementation_and_retention_required"),
            _row("combined", "wall_clock_hours", "not_identifiable", "hours", "unresolved", "hardware_and_parallelism_required"),
        )
    )
    return rows


def write_summary(handle: TextIO) -> None:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(
        (
            "scope",
            "metric",
            "value",
            "unit",
            "bound_type",
            "assumption_scope",
        )
    )
    writer.writerows(summary_rows())


def write_manifest(handle: TextIO, which: str) -> None:
    reliability = build_reliability_manifest()
    mv = build_mv_manifest()
    if which == "reliability":
        entries: Iterable[tuple[str, ManifestEntry]] = reliability.entries.items()
    elif which == "mv1":
        entries = mv.entries.items()
    else:
        entries = (*reliability.entries.items(), *mv.entries.items())
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(
        (
            "kind",
            "canonical_cell_id",
            "families",
            "planning",
            "outer_eligibility",
        )
    )
    for identifier, entry in sorted(entries):
        writer.writerow(
            (
                entry.cell["kind"],
                identifier,
                ";".join(sorted(entry.families)),
                "yes" if "planning" in entry.families else "no",
                "fixed" if entry.cell["kind"] == "reliability" else "pending_calibration",
            )
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        choices=("reliability", "mv1", "all"),
        help="print the selected canonical candidate manifest instead of the summary",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.manifest:
        write_manifest(sys.stdout, args.manifest)
    else:
        write_summary(sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
