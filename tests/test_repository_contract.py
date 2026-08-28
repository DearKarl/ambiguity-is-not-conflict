import csv
import math
import subprocess
import sys
from pathlib import Path
from statistics import NormalDist

from scripts.check_repository import collect_errors


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
