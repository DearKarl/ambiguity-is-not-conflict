"""Validate the documentation-first repository contract."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "CODEX_TASK_GOVERNANCE.md",
    "EXECUTION_CONTRACT.md",
    "HANDOFF_CONTRACT.md",
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
    "docs/research/reader_measurement_and_mv1_qualification_audit.md",
    "docs/research/simulation_resource_feasibility_audit.md",
    "docs/research/noncore_simulation_computational_design.md",
    "docs/research/simulation_output_and_operation_registry.md",
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
    "docs/research/task_briefs/TB-0008-reader-measurement-mv1-qualification.md",
    "docs/research/task_briefs/TB-0009-simulation-resource-feasibility.md",
    "docs/research/task_briefs/TB-0010-noncore-simulation-resource-design.md",
    "docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md",
    "experiments/research_core/README.md",
    "reports/tables/gate0_power_sensitivity.csv",
    "reports/tables/mv1_qualification_yield_sensitivity.csv",
    "reports/tables/simulation_resource_manifest_summary.csv",
    "reports/tables/simulation_metric_registry.csv",
    "reports/tables/simulation_operation_registry.csv",
    "reports/tables/simulation_semantic_count_ledger_summary.csv",
    "scripts/calculate_mv1_qualification_design.py",
    "scripts/enumerate_simulation_resource_manifest.py",
    "scripts/compile_simulation_semantic_count_ledger.py",
)

FORBIDDEN_BASENAMES = {
    "pasted-text.txt",
    "handoff.md",
    "atas_certificate.pdf",
}

FORBIDDEN_SUFFIXES = {".ckpt", ".dcm", ".pth", ".pt"}

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXECUTION_ID_PATTERN = re.compile(r"^- Contract ID: `([^`]+)`$", re.MULTILINE)
HANDOFF_ID_PATTERN = re.compile(
    r"^## Handoff record `([^`]+)`$", re.MULTILINE
)
HANDOFF_LINK_PATTERN = re.compile(
    r"^- Linked Execution Contract: `([^`]+)`$", re.MULTILINE
)
STATUS_PATTERN = re.compile(r"^- Status: `([^`]+)`$", re.MULTILINE)
FINAL_PLACEHOLDER_PATTERN = re.compile(
    r"(?im)^(?:"
    r"[ \t]*(?:[-*][ \t]+)?pending(?:[ \t]|[.:]|$).*"
    r"|[ \t]*[-*][ \t]+[^:\n]+:[ \t]*"
    r"(?:pending|tbd|todo|to be determined|to be recorded)?[.!?]*[ \t]*"
    r"(?!\n[ \t]{2,}\S)"
    r")$"
)

EXECUTION_STATUSES = {"AUTHORIZED / IN PROGRESS", "COMPLETE"}
HANDOFF_STATUSES = {
    "IN PROGRESS",
    "READY FOR REMOTE FINALIZATION",
    "COMPLETE",
}

REQUIRED_HANDOFF_SECTIONS = (
    "Identity and status",
    "Outcome",
    "Changed boundary",
    "Facts",
    "Decisions recorded",
    "Assumptions and unresolved items",
    "Validation and review evidence",
    "Git and external evidence",
    "Deviations and negative results",
    "Residual risks and recovery",
    "Next permitted boundary",
)

REQUIRED_ACTIVE_FIELD_PATTERNS = {
    "EXECUTION_CONTRACT.md": {
        "task": re.compile(r"^- Task:[ \t]+\S.*$", re.MULTILINE),
        "authority": re.compile(
            r"^- Authorized by:[ \t]+\S.*$", re.MULTILINE
        ),
        "repository": re.compile(
            r"^- Repository:[ \t]+\S.*$", re.MULTILINE
        ),
        "working branch": re.compile(
            r"^- Working branch:[ \t]+\S.*$", re.MULTILINE
        ),
        "expected base": re.compile(
            r"^- Expected base:[ \t]+\S.*$", re.MULTILINE
        ),
    },
    "HANDOFF_CONTRACT.md": {
        "task": re.compile(r"^- Task:[ \t]+\S.*$", re.MULTILINE),
        "prepared by": re.compile(
            r"^- Prepared by:[ \t]+\S.*$", re.MULTILINE
        ),
        "handoff date": re.compile(
            r"^- Handoff date:[ \t]+\S.*$", re.MULTILINE
        ),
    },
}

REQUIRED_CONTROL_PHRASES = {
    "AGENTS.md": (
        "## Contract Supremacy",
        "`EXECUTION_CONTRACT.md`",
        "`HANDOFF_CONTRACT.md`",
    ),
    "CODEX_TASK_GOVERNANCE.md": (
        "### `EXECUTION_CONTRACT`",
        "### `HANDOFF_CONTRACT`",
    ),
    "EXECUTION_CONTRACT.md": (
        "# Execution Contract",
        "## Contract-first rule",
        "## Active contract",
        "### Identity and status",
        "### Primary outcome",
        "### Authoritative inputs",
        "### Allowed actions",
        "### Forbidden actions",
        "### Preconditions",
        "### Promotion criteria",
        "### Stopping criteria",
        "### Irreversible and external boundaries",
        "### Required evidence",
        "### Pre-task traversal record",
        "- Traversal status: `COMPLETE`",
    ),
    "HANDOFF_CONTRACT.md": (
        "# Handoff Contract",
        "## Contract-last rule",
        "### Identity and status",
        "### Outcome",
        "### Changed boundary",
        "### Facts",
        "### Decisions recorded",
        "### Assumptions and unresolved items",
        "### Validation and review evidence",
        "### Git and external evidence",
        "### Deviations and negative results",
        "### Residual risks and recovery",
        "### Next permitted boundary",
    ),
}


def _link_target(markdown_file: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>").split("#", 1)[0]
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target)
    candidate = Path(target)
    if candidate.is_absolute():
        return candidate
    return (markdown_file.parent / candidate).resolve()


def _section_bodies(content: str, heading: str) -> list[str]:
    pattern = re.compile(
        rf"^### {re.escape(heading)}[ \t]*$\n(.*?)(?=^### |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.findall(content)


def _git_output(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )


def _contract_freshness_errors(
    root: Path,
    base_ref: str,
    execution: str,
    handoff: str,
) -> list[str]:
    prefix = "contract freshness: "
    errors: list[str] = []
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", base_ref):
        return [f"{prefix}base ref has an unsupported format"]
    base_commit = _git_output(root, "rev-parse", "--verify", f"{base_ref}^{{commit}}")
    if base_commit.returncode != 0:
        return [f"{prefix}base ref is unavailable: {base_ref}"]

    base_execution_result = _git_output(
        root, "show", f"{base_ref}:EXECUTION_CONTRACT.md"
    )
    base_handoff_result = _git_output(root, "show", f"{base_ref}:HANDOFF_CONTRACT.md")
    base_has_execution = base_execution_result.returncode == 0
    base_has_handoff = base_handoff_result.returncode == 0
    if base_has_execution != base_has_handoff:
        return [f"{prefix}base must contain both contracts or neither"]

    current_execution_ids = EXECUTION_ID_PATTERN.findall(execution)
    current_handoff_ids = HANDOFF_ID_PATTERN.findall(handoff)
    current_execution_statuses = STATUS_PATTERN.findall(execution)
    current_handoff_statuses = STATUS_PATTERN.findall(handoff)
    if not all(
        len(values) == 1
        for values in (
            current_execution_ids,
            current_handoff_ids,
            current_execution_statuses,
            current_handoff_statuses,
        )
    ):
        return [f"{prefix}current contract identity or status is invalid"]

    current_ids = (current_execution_ids[0], current_handoff_ids[0])
    current_statuses = (
        current_execution_statuses[0],
        current_handoff_statuses[0],
    )
    primary_statuses = (
        "AUTHORIZED / IN PROGRESS",
        "READY FOR REMOTE FINALIZATION",
    )
    complete_statuses = ("COMPLETE", "COMPLETE")

    if not base_has_execution:
        if current_statuses != primary_statuses:
            errors.append(
                f"{prefix}bootstrap PR must carry an in-progress Execution "
                "Contract and ready Handoff Contract"
            )
        return errors

    base_execution = base_execution_result.stdout
    base_handoff = base_handoff_result.stdout
    base_execution_ids = EXECUTION_ID_PATTERN.findall(base_execution)
    base_handoff_ids = HANDOFF_ID_PATTERN.findall(base_handoff)
    base_execution_statuses = STATUS_PATTERN.findall(base_execution)
    base_handoff_statuses = STATUS_PATTERN.findall(base_handoff)
    if not all(
        len(values) == 1
        for values in (
            base_execution_ids,
            base_handoff_ids,
            base_execution_statuses,
            base_handoff_statuses,
        )
    ):
        return [f"{prefix}base contract identity or status is invalid"]

    base_ids = (base_execution_ids[0], base_handoff_ids[0])
    base_statuses = (base_execution_statuses[0], base_handoff_statuses[0])
    changed_result = _git_output(root, "diff", "--name-only", base_ref, "--")
    if changed_result.returncode != 0:
        return [f"{prefix}cannot inspect changed paths against {base_ref}"]
    changed_paths = {
        line.strip() for line in changed_result.stdout.splitlines() if line.strip()
    }

    if current_ids == base_ids:
        if not (
            base_statuses
            == ("AUTHORIZED / IN PROGRESS", "READY FOR REMOTE FINALIZATION")
            and current_statuses == complete_statuses
        ):
            errors.append(
                f"{prefix}unchanged contract IDs are allowed only for the "
                "READY-to-COMPLETE closure transition"
            )
        allowed_closure_paths = {
            "EXECUTION_CONTRACT.md",
            "HANDOFF_CONTRACT.md",
        }
        if changed_paths != allowed_closure_paths:
            errors.append(
                f"{prefix}closure PR may change only both contract files"
            )
        return errors

    if current_ids[0] == base_ids[0] or current_ids[1] == base_ids[1]:
        errors.append(f"{prefix}a new task must replace both linked contract IDs")
    if base_statuses != complete_statuses:
        errors.append(f"{prefix}a new task requires a COMPLETE base handoff")
    if current_statuses != primary_statuses:
        errors.append(
            f"{prefix}a primary PR must carry an in-progress Execution "
            "Contract and ready Handoff Contract"
        )
    if not {
        "EXECUTION_CONTRACT.md",
        "HANDOFF_CONTRACT.md",
    }.issubset(changed_paths):
        errors.append(f"{prefix}a primary PR must change both contract files")
    return errors


def collect_errors(
    root: Path = ROOT,
    *,
    require_final: bool = False,
    base_ref: str | None = None,
) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for relative, required_phrases in REQUIRED_CONTROL_PHRASES.items():
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in content:
                errors.append(
                    f"missing required control field in {relative}: {phrase}"
                )

    for relative, field_patterns in REQUIRED_ACTIVE_FIELD_PATTERNS.items():
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        for field_name, pattern in field_patterns.items():
            if len(pattern.findall(content)) != 1:
                errors.append(
                    f"missing, empty, or duplicate active field in {relative}: "
                    f"{field_name}"
                )

    execution_path = root / "EXECUTION_CONTRACT.md"
    handoff_path = root / "HANDOFF_CONTRACT.md"
    if execution_path.is_file() and handoff_path.is_file():
        execution = execution_path.read_text(encoding="utf-8")
        handoff = handoff_path.read_text(encoding="utf-8")
        execution_ids = EXECUTION_ID_PATTERN.findall(execution)
        handoff_ids = HANDOFF_ID_PATTERN.findall(handoff)
        linked_ids = HANDOFF_LINK_PATTERN.findall(handoff)
        execution_statuses = STATUS_PATTERN.findall(execution)
        handoff_statuses = STATUS_PATTERN.findall(handoff)
        if len(execution_ids) != 1:
            errors.append(
                "execution contract must contain exactly one active Contract ID"
            )
        if len(handoff_ids) != 1:
            errors.append(
                "handoff contract must contain exactly one active Handoff record ID"
            )
        if len(linked_ids) != 1:
            errors.append(
                "handoff contract must contain exactly one linked Execution Contract"
            )
        if len(execution_ids) == 1 and len(linked_ids) == 1:
            if execution_ids[0] != linked_ids[0]:
                errors.append(
                    "handoff contract does not link to the active Execution Contract"
                )
        if len(execution_statuses) != 1:
            errors.append("execution contract must contain exactly one Status")
        elif execution_statuses[0] not in EXECUTION_STATUSES:
            errors.append(
                f"invalid execution contract Status: {execution_statuses[0]}"
            )
        if len(handoff_statuses) != 1:
            errors.append("handoff contract must contain exactly one Status")
        elif handoff_statuses[0] not in HANDOFF_STATUSES:
            errors.append(f"invalid handoff contract Status: {handoff_statuses[0]}")
        if len(execution_statuses) == 1 and len(handoff_statuses) == 1:
            execution_status = execution_statuses[0]
            handoff_status = handoff_statuses[0]
            valid_pair = (
                execution_status == "AUTHORIZED / IN PROGRESS"
                and handoff_status
                in {"IN PROGRESS", "READY FOR REMOTE FINALIZATION"}
            ) or (
                execution_status == "COMPLETE" and handoff_status == "COMPLETE"
            )
            if not valid_pair:
                errors.append(
                    "execution and handoff contract Status values are incompatible"
                )
            if require_final:
                if handoff_status not in {
                    "READY FOR REMOTE FINALIZATION",
                    "COMPLETE",
                }:
                    errors.append(
                        "final validation requires a ready or complete handoff"
                    )
                if FINAL_PLACEHOLDER_PATTERN.search(handoff):
                    errors.append(
                        "final validation rejects pending handoff placeholders"
                    )
                for heading in REQUIRED_HANDOFF_SECTIONS:
                    bodies = _section_bodies(handoff, heading)
                    if len(bodies) != 1 or not re.search(r"\w", bodies[0]):
                        errors.append(
                            "final validation requires one non-empty Handoff "
                            f"section: {heading}"
                        )

        if base_ref is not None:
            errors.extend(
                _contract_freshness_errors(root, base_ref, execution, handoff)
            )

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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--final",
        action="store_true",
        help="require a placeholder-free handoff ready for remote finalization",
    )
    parser.add_argument(
        "--base-ref",
        help="require a fresh primary or finite closure contract against this Git ref",
    )
    args = parser.parse_args()
    errors = collect_errors(require_final=args.final, base_ref=args.base_ref)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository contract: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
