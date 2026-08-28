from pathlib import Path

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
    strategy = (
        ROOT / "docs/research/submission_strategy.md"
    ).read_text(encoding="utf-8").lower()
    assert "use-inspired" in strategy
    assert "2027 call not yet available" in strategy
    assert "single intended primary contribution" in strategy
    assert "not a second project or a simultaneous submission" in strategy


def test_month_three_gate_is_not_confirmatory_evidence() -> None:
    measurement = (
        ROOT / "docs/research/measurement_protocol.md"
    ).read_text(encoding="utf-8").lower()
    assert "necessary but not sufficient" in measurement
    assert "matched deterministic compatibility/failure" in measurement
    assert "cannot be promoted as confirmatory evidence" in measurement
