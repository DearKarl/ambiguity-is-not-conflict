"""Validate the documentation-first repository contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "CODEX_TASK_GOVERNANCE.md",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "LICENSE",
    "docs/roadmap.md",
    "docs/research/README.md",
    "docs/research/research_contract.md",
    "docs/research/scope_charter.md",
    "docs/research/problem_taxonomy.md",
    "docs/research/research_question.md",
    "docs/research/task_estimand_options.md",
    "docs/research/measurement_protocol.md",
    "docs/research/annotation_and_intervention_protocol.md",
    "docs/research/intervention_option_audit.md",
    "docs/research/statistical_analysis_plan.md",
    "docs/research/evaluation_protocol.md",
    "docs/research/data_governance.md",
    "docs/research/dataset_feasibility_audit.md",
    "docs/research/dataset_decision_candidate.md",
    "docs/research/execution_budget_and_backbone_audit.md",
    "docs/research/estimator_formalization_audit.md",
    "docs/research/gate0_decision_dossier.md",
    "docs/research/gate0_closure_audit.md",
    "docs/research/baselines_and_ablations.md",
    "docs/research/literature_matrix.md",
    "docs/research/submission_strategy.md",
    "docs/research/decision_log.md",
    "docs/research/task_briefs/TB-0003-gate0-freeze-candidate.md",
    "docs/research/task_briefs/TB-0004-freeze-candidate-review-remediation.md",
    "docs/research/task_briefs/TB-0005-gate0-decision-dossier.md",
    "docs/research/task_briefs/TB-0006-estimator-formalization-audit.md",
    "docs/research/task_briefs/TB-0007-confer-evidence-status-reconciliation.md",
    "experiments/research_core/README.md",
    "reports/tables/gate0_power_sensitivity.csv",
)

FORBIDDEN_BASENAMES = {
    "pasted-text.txt",
    "handoff.md",
    "atas_certificate.pdf",
}

FORBIDDEN_SUFFIXES = {".ckpt", ".dcm", ".pth", ".pt"}

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def _link_target(markdown_file: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>").split("#", 1)[0]
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target)
    candidate = Path(target)
    if candidate.is_absolute():
        return candidate
    return (markdown_file.parent / candidate).resolve()


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            if path.name.lower() in FORBIDDEN_BASENAMES:
                errors.append(f"forbidden sensitive/legacy file: {path.relative_to(root)}")
            if path.suffix.lower() in FORBIDDEN_SUFFIXES:
                errors.append(f"forbidden data/model artifact: {path.relative_to(root)}")

    for markdown_file in root.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        content = markdown_file.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(content):
            target = _link_target(markdown_file, raw_target)
            if target is None:
                continue
            if target.is_absolute() and root not in target.parents and target != root:
                errors.append(
                    f"absolute or out-of-repository link in "
                    f"{markdown_file.relative_to(root)}: {raw_target}"
                )
            elif not target.exists():
                errors.append(
                    f"broken link in {markdown_file.relative_to(root)}: {raw_target}"
                )

    return sorted(set(errors))


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository contract: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
