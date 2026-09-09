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

If the first COMPLETE-state validation exposes a deterministic self-hosting
defect in the governance checker or tests, the contracts must first return to
their pre-completion statuses. A unique remediation ID must be linked here and
in the fully re-traversed Execution Contract before one exceptional closure
may include only the exact governance files named there. The exception remains
single-use, independently reviewed, and inside the same final closure PR.

## Handoff record `HC-2026-09-09-003`

### Identity and status

- Linked Execution Contract: `EC-2026-09-09-003`
- Task: finalize the four-role migration, recover misdirected edits, and
  synchronize the reviewed progress branch
- Status: `READY FOR REMOTE FINALIZATION`
- Prepared by: current Codex module under Commander's explicit recovery authority
- Handoff date: 2026-09-09 (Asia/Shanghai)

### Outcome

- Installed the shared four-role harness and profiles with exact model/effort
  mappings and parenthesized display titles.
- Replaced the old five-role definitions: Advisor owns strategic advice;
  Engineer retains daily research/technical design; Adjutant coordinates;
  Executor performs approved implementation and operations.
- Restored the desktop handoff, preserved both permanent contract prefaces,
  and returned the misdirected `4565` checkout to its exact clean base.
- No scientific scope, model choice, dataset, Gate-0, or experiment decision
  changed. This delivery is branch synchronization, not main integration.

### Changed boundary

- The complete primary migration contains exactly nine paths:
  `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, `CODEX_ROLE_HARNESS.md`,
  `.codex/agents/advisor.toml`, `.codex/agents/adjutant.toml`,
  `.codex/agents/engineer.toml`, `.codex/agents/executor.toml`,
  `EXECUTION_CONTRACT.md`, and `HANDOFF_CONTRACT.md`.
- Final desktop recovery edits touch only the two contracts. In `4565`,
  tracked originals were restored and erroneous untracked role files removed;
  the cleanup contributes no committed change.
- Scientific documents, tests, compiler behavior, research tables, models,
  data, and unrelated local files are excluded.

### Facts

- The desktop handoff was temporarily deleted during a wrong-path repair and
  has been restored. Both contracts in `4565` now equal the base byte-for-byte;
  `git status --porcelain` there is empty.
- All four saved projects contain byte-identical copies of the five shared
  files; all 16 TOML model/effort/sandbox-default mappings parse correctly.
- The 16 app display titles were verified during migration. Borderless's
  `Research (5.6 Sol / XHigh)` remains active and keeps its ongoing work:
  no rename, archive, interruption, or reassignment occurred.
- Metadata contains restricted identifiers and must never be treated as public
  or harmless. No restricted data or model was accessed.
- Spark exhausted its allowance before finalization; Commander explicitly
  authorized the current module to complete this bounded task.

### Decisions recorded

- Keep the permanent role/model assignments. Current-module recovery is a
  task-specific exception, not a changed default.
- TOMLs request defaults for future sessions that actually load them; they do
  not establish retroactive sandboxing or universal tool/budget enforcement.
- Use one owner per bounded task and scoped independent review when justified;
  no mandatory four-role relay or guaranteed token-saving claim.
- Publish only the dedicated branch after checks pass. No PR, main merge,
  protection change, or contracts-to-COMPLETE transition is authorized.

### Assumptions and unresolved items

- The verified base is fixed for this delivery; remote divergence or unrelated
  changes require a stop before push.
- Runtime activation and measured token savings remain unverified.
- Main integration and finite contract closure are separate next boundaries;
  existing scientific gates remain unchanged.

### Validation and review evidence

- Independent shared-template review passed for the frozen five-file package.
- Independent integration review passed with named finalization conditions:
  align EC authority/scope, list all nine HC paths, restore the exact HC
  preface, and record actual validation results before ready-state publication.
  Recovery addresses those conditions without scientific or checker/test edits.
- Earlier recovery ran `pytest -q`: 53 passed. Base-aware and final checkers
  then rejected the IN PROGRESS handoff as required; these were not passes.
- Fresh finalization: `pytest -q` passed all 53 tests in 13.27 seconds;
  `python scripts/check_repository.py` reported `Repository contract: OK`;
  `git diff --check` passed. Bayesian's existing suite passed 17 tests in
  1.31 seconds and its worktree/upstream divergence is clean at `0/0`.
- Exact-prefix comparison passed for both contracts. The observed change set
  contains only the nine named small text files, with no science, script,
  test, or research-table changes. Shared hashes and all 16 profiles passed.
- The independent review's named documentary conditions are now satisfied.
  The final base-aware checker must run after this READY transition and pass
  immediately before commit; a failed check cancels publication. Its exact
  result, the pushed SHA, and CI are reported in the final delivery receipt.

### Git and external evidence

- Pre-commit head: `d63e96abafe965ba0a59fb2c8442921fe94d0ab6`.
- Working branch: `codex/four-role-harness-desktop`.
- Remote: `https://github.com/DearKarl/ambiguity-is-not-conflict.git`.
- Expected base: `d63e96abafe965ba0a59fb2c8442921fe94d0ab6`.
- Fresh fetch confirmed `origin/main` still equals the base; the new remote
  progress branch was absent at preflight.
- Bayesian's migration commit is
  `3d5411a3a86c696f1c480b18c471919fe27bf820`, verified on GitHub. Its clone
  fetched only main; one exact branch refspec repaired upstream tracking
  without changing remote history or main.
- This primary commit and its push/CI identify themselves through immutable
  Git/GitHub evidence, reported in the final user receipt rather than through
  recursive self-recording commits. No PR, merge, or main update is included.

### Deviations and negative results

- Initial integration misrouted legacy Research/Operations and removed
  permanent contract text. Review caught both before push; they were repaired.
- A later repair used the wrong checkout, and Spark's limit interrupted
  cleanup. Recovery restored tracked originals and removed only verified
  task-created duplicates; no user content was deleted.
- The parent-selected `-desktop` branch suffix avoided a branch checked out
  elsewhere; it was not a scientific or Commander-selected change.
- No experiment, scientific RNG/DGP/bootstrap pipeline, full persisted ledger,
  data/model download, paid compute, or large artifact was produced.

### Residual risks and recovery

- Use explicit absolute workdirs and patch paths. Do not copy contracts or
  profiles into another checkout during recovery.
- `4565` is clean at its original base. The older `492b` checkout and its local
  untracked `HANDOFF.md` are deliberately preserved and excluded from publishing.
- Correct shared profiles remain in all four saved folders. Deleted duplicates
  were erroneous task drafts, not unique user artifacts.
- No task is archived or removed. Borderless Research retains current work
  until explicit handoff.

### Next permitted boundary

- Run the final base-aware checker and staged-content review, then normally
  commit/push the nine-path branch and verify its Actions run. Stop on any
  failed required check. After delivery, no further file changes are authorized
  by this ready-state record.
- PR/main integration, closure-to-COMPLETE, and research execution require
  explicit next authority; none follows automatically from this delivery.
