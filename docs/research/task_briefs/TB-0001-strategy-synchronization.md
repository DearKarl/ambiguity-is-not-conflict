# TASK_BRIEF

- **Identifier:** TB-0001 — Main Track strategy synchronization
- **Date and owner:** 2026-08-29; Ultra lane, authorized by the Commander
- **Evidence gate:** Gate 0 documentation maintenance; protocol only
- **Primary outcome:** Reconcile the Commander-supplied NeurIPS 2027 strategy
  with the complete repository record while preserving one scientific route,
  explicit construct boundaries, and the distinction between facts,
  inferences, assumptions, and decisions.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, the full
  canonical record under `docs/research/`, the Commander-supplied strategy,
  and official NeurIPS 2026 Main Track and Evaluations & Datasets materials
  used only as historical planning evidence.
- **Allowed actions:** Read every repository file; verify venue-dependent
  statements against official NeurIPS sources; add one decision record; edit
  `README.md`, `docs/research/README.md`, `docs/research/research_contract.md`,
  `docs/research/scope_charter.md`, `docs/research/research_question.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/submission_strategy.md`,
  `docs/research/supervisor_alignment.md`, `docs/research/decision_log.md`,
  `docs/roadmap.md`, and `tests/test_repository_contract.py`; run local
  documentation checks; commit and push only after branch, upstream, staged
  files, and divergence are verified.
- **Forbidden actions:** Literature research beyond the official venue-policy
  verification above; core implementation; experiments; data or model access,
  download, training, or inference; clinical annotation; method selection;
  claims of results, clinical benefit, 2027 eligibility, acceptance, or
  publication; unrelated repository changes.
- **Exact files/data/model/compute boundary:** Only the files named above and
  this task brief may change. No data, models, generated research artifacts,
  or research compute are permitted.
- **Required outputs and evidence:** A dated decision record; a single
  consistent Main Track/Use-Inspired planning identity conditional on the
  official 2027 call; an explicit single-contribution boundary; a
  necessary-but-not-sufficient Month-3 gate; a same-route E&D contingency;
  diff and link audit; clean local checks.
- **Validation commands:** `pytest -q`; `python scripts/check_repository.py`;
  targeted repository-wide terminology search; `git diff --check`; final Git
  status and divergence checks.
- **Promotion criteria:** All supplied strategic elements are either recorded
  in their correct evidence class or explicitly retained as unresolved; no
  canonical contradiction remains; all checks pass.
- **Stopping criteria:** Stop on unsupported venue claims, conflict with a
  stronger canonical construct/governance boundary, sensitive or unrelated
  content, unexpected worktree changes, failed checks that cannot be repaired
  within the named files, or remote divergence.
- **External, costly, or irreversible boundary:** No external write except a
  normal non-force Git push after all synchronization checks pass. No dataset,
  model, compute, clinical, or publication action is authorized.
- **Permitted claim after completion:** The protocol-stage repository records
  the Commander-approved submission strategy consistently. It does not show
  that the estimator is identifiable, that any gate has passed, that the work
  is eligible under unpublished 2027 rules, or that publication is likely.
