# Handoff Contract

This file is the mandatory post-task control record for repository work. It is
paired with `EXECUTION_CONTRACT.md` and is append-only in meaning: a completed
handoff is corrected by a later dated amendment, never silently rewritten to
change historical evidence.

## Contract-last rule

Every bounded repository task must finish by recording:

1. the linked Execution Contract and authority;
2. the delivered outcome and exact changed boundary;
3. facts, decisions, assumptions, and unresolved items separately;
4. validation, independent review, Git, CI, and external-action evidence;
5. deviations, negative results, residual risks, and recovery state; and
6. the exact next permitted decision or task boundary.

A task must not be represented as complete until this record is filled and its
required evidence passes.

Closure uses two finite phases:

1. `READY FOR REMOTE FINALIZATION`: before the primary PR, replace every
   operational placeholder with local evidence or an explicit self-evidence
   boundary. The primary branch may then be pushed, reviewed, checked, and
   merged.
2. `COMPLETE`: after the primary merge and post-merge CI, make one completion-
   only change to this file and `EXECUTION_CONTRACT.md`, recording all primary-
   change and external-governance evidence. Only verification and normal
   synchronization of that closure record may follow.

The closure commit and PR identify themselves through immutable Git/GitHub
history; their own merge revision and post-merge CI are reported in the final
user handoff and are not recursively inserted into this file. No third closure
change is required or allowed.

## Handoff record `HC-2026-08-29-001`

### Identity and status

- Linked Execution Contract: `EC-2026-08-29-001`
- Task: bootstrap strict execution/handoff governance and close the current
  repository-governance stage
- Status: `READY FOR REMOTE FINALIZATION`
- Prepared by: Codex, Ultra research-planning task
- Handoff date: 2026-08-29 (Asia/Shanghai)

### Outcome

The bounded primary change is locally complete and ready for normal GitHub
finalization. It installs a strict contract-first/contract-last workflow,
reconciles the TB-0011 integration record, records the Commander's partial
`G0-SCOPE A` decision and local-storage boundary, and hardens CI and repository
governance. It does not close Gate 0, choose `G0-METHOD`, or create scientific
evidence. Primary merge evidence will be added through the one permitted
completion-only closure change.

### Changed boundary

- Files added: `EXECUTION_CONTRACT.md` and `HANDOFF_CONTRACT.md`.
- Files modified: `.github/ISSUE_TEMPLATE/experiment_proposal.md`,
  `.github/ISSUE_TEMPLATE/research_decision.md`,
  `.github/pull_request_template.md`, `.github/workflows/quality.yml`,
  `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, `CONTRIBUTING.md`, `README.md`,
  `requirements-dev.txt`, `scripts/check_repository.py`,
  `tests/test_repository_contract.py`, `docs/research/README.md`,
  `docs/research/decision_log.md`,
  `docs/research/execution_budget_and_backbone_audit.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/research_contract.md`,
  `docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md`,
  and `docs/research/templates/task_brief.md`.
- GitHub settings or metadata changed: labels `decision` and `protocol` were
  added; `main` now requires strict `repository-contract` status checks, one
  approving review, stale-review dismissal, and resolved conversations, while
  force pushes and deletion are disabled. Administrator enforcement remains
  off because `DearKarl` is the only collaborator.
- Deliberately excluded: data, models, experiments, generated scientific
  results, clinical work, and the unresolved `G0-METHOD` decision

### Facts

- The expected base, local `HEAD`, local `main`, and `origin/main` were all
  `f1fe19b38eb4d036893e79b7c27cca0344517f06` before the primary commit.
- The remote is exactly
  `https://github.com/DearKarl/ambiguity-is-not-conflict.git`; the repository
  is public and its default branch is `main`.
- Prior PR #1 merged the TB-0011 integration record; its post-merge `main` CI
  passed at
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33232102476`.
- TB-0011's approximately 613-GB quantity is a conditional simulation-output
  core floor, not a dataset size, final upper bound, repository footprint, or
  download authorization.
- No file above 1 MiB, restricted artifact, data/model payload, regenerated
  scientific output, or unrelated user change was found in the bounded tree.

### Decisions recorded

- Contract-first and contract-last governance is the highest repository-local
  operational workflow rule, subject to higher platform authority and the
  Commander's current explicit instruction.
- The Commander selected `G0-SCOPE A`: determinate-conflict specificity is the
  primary intended claim and natural ambiguity is veto-only. This is a partial
  decision; scientific-supervisor and other required approvals remain open.
- `G0-METHOD A/B` remains open and no estimator, architecture, dataset, or
  experiment route was selected by this task.
- Publication CI uses immutable action revisions, `pytest==8.4.2`, strict
  placeholder/section validation, and PR-base contract freshness. New tasks
  must replace both linked IDs; the same IDs are allowed only for a two-file
  `READY FOR REMOTE FINALIZATION` to `COMPLETE` closure.

### Assumptions and unresolved items

- Gate 0 remains open.
- `G0-METHOD` remains an explicit Commander/supervisor/statistical/model-owner
  decision.
- Independent reviews are repository-local evidence, not GitHub approving
  reviews and not scientific-supervisor approval.
- With one collaborator, the configured one-review rule cannot be satisfied by
  a second eligible GitHub reviewer. The authorized closeout therefore relies
  on a disclosed normal administrator-exempt merge after independent review
  and green CI, without an explicit override command or weakened protection.

### Validation and review evidence

- Contract traversal: complete under `EC-2026-08-29-001`
- Focused checks: lifecycle pairing, active fields, placeholder punctuation,
  multiline values, non-empty sections, stale-contract rejection, valid
  closure, and CI-integrity regressions all pass inside the full suite.
- Full test suite: `pytest 8.4.2`; 45 passed in a clean temporary virtual
  environment, which was then moved recoverably to the system Trash.
- Repository checker: normal, strict-final, and strict-final against
  `origin/main` pass in the prepared worktree.
- Diff and sensitive-content review: `git diff --check` passes; no file above
  1 MiB, restricted basename/suffix, secret candidate, generated-output
  change, or out-of-repository Markdown link was found.
- Independent review: scientific-state review PASS; repository-security review
  PASS; contract/lifecycle review PASS after all identified blockers were
  corrected. These were read-only reviews and are not GitHub approvals.

### Git and external evidence

- Base revision:
  `f1fe19b38eb4d036893e79b7c27cca0344517f06`
- Working branch: `codex/contract-governance-closeout`
- Primary commit: the commit containing this prepared record is
  self-identifying in Git and will be copied into the completion-only record.
- Pull request: the primary PR will be opened only after strict local
  validation; its URL belongs to the completion-only evidence update.
- Branch CI: the pushed primary revision must pass the `repository-contract`
  job before merge; its run URL belongs to the completion-only evidence update.
- Merge and post-merge CI: both are required before the two contracts can move
  to `COMPLETE`; their immutable revisions and URLs belong to the completion-
  only evidence update.
- Labels: `decision` (`5319E7`) and `protocol` (`1D76DB`) exist with research-
  specific descriptions.
- `main` protection: strict `repository-contract`, one approval, stale-review
  dismissal, conversation resolution, no force pushes, and no deletion are
  enabled; `enforce_admins=false` is the disclosed solo-collaborator residual.
- Final clean revision: the primary merge revision will be recorded during the
  completion-only closure; that closure's own revision remains self-evidencing
  Git/GitHub metadata under the finite rule.

### Deviations and negative results

- Initial review found ambiguous 613-GB wording, a circular contract bootstrap,
  recursive closeout, hard-coded IDs, an internally blocked merge path,
  line-wrap-sensitive tests, permissive placeholder handling, empty-section
  acceptance, and stale-contract reuse. Each was corrected and covered by
  validation before this ready state.
- The first branch-protection API payload was rejected with HTTP 422; a
  corrected, non-weakened configuration was applied and read back successfully.
- No scientific hypothesis was tested, so this task produced neither a
  positive nor negative scientific result.

### Residual risks and recovery

- Administrator enforcement remains off while only one collaborator exists;
  therefore GitHub itself cannot supply the required independent approval for
  this closeout. The exemption must remain explicit and must not be described
  as a GitHub approval.
- PR-base freshness is machine-checked, but an administrator could still evade
  protection through an explicitly forbidden direct or override path. The
  repository rule, audit trail, and future Handoff Contract must continue to
  expose this boundary until an eligible reviewer is added.
- Gate 0, supervisor co-approval of `G0-SCOPE A`, `G0-METHOD`, data/access,
  task/readers/resources, and all core implementation remain open.
- Recovery is ordinary and auditable: repository changes remain in commits and
  PRs, the working branch is preserved, and GitHub labels/protection can be
  inspected or reverted through normal non-force operations if later
  authorized.

### Next permitted boundary

After this handoff is complete, the next scientific task must begin with a new
Execution Contract and a direct decision dialogue on `G0-METHOD A` versus one
tightly time-boxed `G0-METHOD B` theory attempt. No data, model, reader, or
core-experiment action follows automatically.
