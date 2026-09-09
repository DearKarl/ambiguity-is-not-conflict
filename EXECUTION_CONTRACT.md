# Execution Contract

This file is the mandatory pre-task control record for repository work. Within
the repository, it is the highest operational workflow rule. Platform,
system, developer, and the Commander's current explicit instructions retain
their normal precedence.

## Contract-first rule

For every new bounded task, before implementation, mutation, publication, or
external action:

1. update this file with one active contract;
2. read this file in full, together with `AGENTS.md`,
   `CODEX_TASK_GOVERNANCE.md`, and the listed authoritative inputs;
3. verify authority, scope, preconditions, allowed and forbidden actions,
   promotion criteria, stopping criteria, irreversible boundaries, and
   required evidence;
4. record the completed traversal below; and
5. start substantive work only while the active contract is
   `AUTHORIZED / IN PROGRESS`.

The sole pre-traversal mutation is drafting or replacing this file itself from
the Commander's explicit task authority. Read-only inspection needed to write
and verify the contract is also allowed. No other file mutation, publication,
or external action is allowed until the new traversal is complete.

The task is not complete until its outcome and evidence have been written to
`HANDOFF_CONTRACT.md`. If the task changes materially, stop and revise this
contract before continuing. A new task must replace the active contract; past
contracts remain available through Git history and the linked handoff record.

Closure is finite and two-phase. First, the primary change may be committed,
reviewed, and merged only after the Handoff Contract is
`READY FOR REMOTE FINALIZATION`. Second, after the primary merge and CI, the
same task may create one completion-only closure change that updates only the
two contracts with final primary-change evidence and sets both to `COMPLETE`.
After that transition, no substantive work is allowed: only verification,
commit, push, PR, merge, and post-merge CI for the closure record itself, plus
the final user handoff. The closure commit and PR are self-identifying in Git
and GitHub and are not recursively written into themselves.

One single-use self-hosting exception is allowed only when the first closure
validation exposes a deterministic defect in the governance checker or its
tests that prevents the valid `READY` to `COMPLETE` transition. Before any
repair, restore the contracts to their pre-completion statuses, assign and
link a unique closure-remediation ID, amend and fully re-traverse this
contract, and name the exact checker/test files. The exceptional closure may
then change only the two contracts and those named governance files, must pass
independent review and all checks, and must still use the same single closure
PR. It cannot touch scientific documents, data, models, experiments, or
GitHub protection. No unrecorded or second remediation is allowed.

## Active contract

### Identity and status

- Contract ID: `EC-2026-09-09-003`
- Task: finalize the four-role migration, recover misdirected edits, and
  synchronize the reviewed progress branch
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander (2026-09-09, Asia/Shanghai)
- Authority amendment: Commander explicitly authorized the current module to
  finish cleanup, verification, and synchronization after Spark exhausted its
  allowance. This is a bounded execution exception, not a permanent role or
  model reassignment.
- Linked Handoff Contract: `HC-2026-09-09-003`
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/four-role-harness-desktop`
- Remote repository: `https://github.com/DearKarl/ambiguity-is-not-conflict.git`
- Expected base: remote `main` at
  `d63e96abafe965ba0a59fb2c8442921fe94d0ab6`

### Primary outcome

- Finalize the nine-path role migration and its complete handoff receipt;
  retain the approved shared role/model mapping and parenthesized titles.
- Finish recovery of this task's misdirected edits in worktree `4565`, then
  verify the desktop migration and normally push its dedicated branch.
- Preserve scientific scope and Gate-0 state; no method, budget, dataset,
  or experiment decisions are introduced.
- Distinguish requested `.codex/agents/*.toml` constraints from verified runtime
  hard limits (sandbox, approval mode, tool permissions).

### Authoritative inputs

- `AGENTS.md` (read fully; hierarchy preserved)
- `CODEX_TASK_GOVERNANCE.md` (read fully; applies where present)
- `CODEX_ROLE_HARNESS.md`
- `scripts/check_repository.py`
- `tests/test_repository_contract.py`
- `.codex/agents/advisor.toml`
- `.codex/agents/adjutant.toml`
- `.codex/agents/engineer.toml`
- `.codex/agents/executor.toml`
- this amended `EXECUTION_CONTRACT.md` and current `HANDOFF_CONTRACT.md`
- both permanent contract prefaces at base
  `d63e96abafe965ba0a59fb2c8442921fe94d0ab6`
- the prior independent shared-template and integration-review receipts
- worktree `4565`'s `AGENTS.md`, current contracts, four erroneous role
  profiles, and the exact Git diff against the same base
- active repository remote branch state; the four saved projects' shared
  file hashes, and Bayesian's published branch/upstream state

### Exact migration path set (9 paths)

- `AGENTS.md`
- `CODEX_TASK_GOVERNANCE.md`
- `CODEX_ROLE_HARNESS.md`
- `.codex/agents/advisor.toml`
- `.codex/agents/adjutant.toml`
- `.codex/agents/engineer.toml`
- `.codex/agents/executor.toml`
- `EXECUTION_CONTRACT.md`
- `HANDOFF_CONTRACT.md`

### Allowed actions

- Finalization edits in the desktop repository are limited to these two
  contracts; stage and publish only the nine-path migration listed above.
- At `/Users/dearkarl/.codex/worktrees/4565/ambiguity-is-not-conflict`,
  restore only the remaining task-created `HANDOFF_CONTRACT.md` difference
  byte-for-byte to the verified base and remove only the four task-created
  `.codex/agents/{advisor,adjutant,engineer,executor}.toml` files after their
  recorded hashes match. Do not remove directories, branches, or worktrees.
- Correct Bayesian's existing progress-branch upstream metadata, verify its
  already-published commit, and rerun its required deterministic checks.
- Verify the shared five-file package in the four saved project folders;
  do not modify the other projects' research or active jobs.
- Explicitly retain Borderless's `Research (5.6 Sol / XHigh)` task, including
  its ongoing ownership; no archive, rename, interruption, or task transfer.
- Preserve and keep untouched any unrelated scientific, data, or model
  execution work.
- Confirm and record branch, base hash, and required checker evidence.
- After the recorded review conditions and all local checks pass, make one
  descriptive commit and normal push to
  `origin/codex/four-role-harness-desktop`, then verify its GitHub Actions run.
- Budget: small text/config changes and ordinary local CPU checks only; no
  scientific execution, large outputs, or paid compute.

### Forbidden actions

- no scientific method tuning, Gate-0 closure advancement, experiment execution,
  no query or restricted-data query/downloads; no dataset or model download;
- no branch deletion or branch-protection mutation.
- no PR, merge, main update, or closure-to-COMPLETE in this bounded phase;
- no force push, history rewrite, global settings, or unrelated cleanup.

### Preconditions

- `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, and prior contracts were read in full
  before mutation.
- Working branch is `codex/four-role-harness-desktop` checked against `origin/main`.
- Desktop `HANDOFF_CONTRACT.md` has been recreated. The remaining `4565`
  changes must match the recorded task-owned residue; otherwise stop.
- No other module may write these targets during the current-module recovery.

### Promotion criteria

- Exact path and status updates are recorded consistently in both contract files.
- `git diff --check` is clean.
- The prior independent integration review's five finalization conditions are
  satisfied without scientific or permanent-workflow changes.
- `python scripts/check_repository.py --final --base-ref origin/main` reports
  `Repository contract: OK` with a ready Handoff Contract.
- `pytest -q` passes with observed deterministic count.
- The wrong checkout is clean, all five shared files match across four saved
  projects, and the staged change contains exactly the nine approved paths.
- Remote URL, branch, upstream, and divergence are checked before push; the
  pushed commit and its Actions result are verified afterward.

### Stopping criteria

- Any mismatch in role-routing fields or policy controls.
- check errors on required evidence or contract freshness.
- any scope drift into scientific execution, models, data, or protected
  material.
- unexpected worktree residue, concurrent changes, remote/base divergence,
  unresolved review findings, or failed required checks; never publish anyway.

### Irreversible and external boundaries

- Commander authorizes ordinary branch synchronization after review conditions
  and local promotion criteria pass. No PR/merge or closure completion follows.
- GitHub reads and the bounded normal branch push are the only external
  actions; no external data publication or scientific execution.
- No force operations or protection bypasses.

### Required evidence

- Verified branch, remote, and base hash (`git` outputs).
- `pytest -q` with observed test counts.
- `python scripts/check_repository.py --base-ref origin/main`.
- `git diff --check`.
- `python scripts/check_repository.py --final --base-ref origin/main`.
- Exact recovery, reviewed nine-path diff, shared hashes, staged-content scan,
  commit/upstream/divergence and GitHub Actions evidence in the final handoff.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Agent: current Codex module under Commander's explicit recovery authorization.
- Amendment date: 2026-09-09 (Asia/Shanghai).
- Completed full reading of the amended contract, project instructions,
  shared harness and four profiles, 568-line checker, 1,867-line test file,
  current/base contracts, wrong-checkout instructions/contracts/profiles and
  exact diff, and prior independent-review receipts. Earlier truncated reads
  were completed before proceeding.
- Verified the exact desktop base/remote, identified only the recorded
  task-owned residue in `4565`, and confirmed all migration writers are idle
  or stopped. Borderless's Research task remains active and untouched.
- Subsequent remote freshness and shared-hash checks remain mandatory before
  publication; traversal completion is not a claim that those checks passed.
