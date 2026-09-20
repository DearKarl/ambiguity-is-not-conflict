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

- Contract ID: `EC-2026-09-20-006`
- Task: replace the old MIMIC access issue and submit an open In Progress issue
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander explicitly requested deleting the old item, submitting its replacement, and placing it In Progress on 2026-09-20.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/mimic-access-issue-2026-09-20`
- Expected base: `e780a2c62dddcc2ce652d53e0e6902ff043e9249`
- Linked Handoff Contract: `HC-2026-09-20-006`
- Owner: Adjutant sole operator; no delegation.

### Primary outcome

Replace the existing closed MIMIC access issue #24 with one open repository Issue, retained as the sole Project 5 card in In Progress. Keep concise English dataset/version and awaiting-review content. Delete the old issue as expressly requested; do not alter column descriptions or other project settings.

### Authoritative inputs

Read this contract, AGENTS.md, CODEX_TASK_GOVERNANCE.md, prior HANDOFF_CONTRACT.md, and the opening administrative update/decision summary of docs/research/dataset_decision_record.md. Live Project 5 and issue #24 establish the item identity. Earlier immutable research traversal remains valid; no scientific decision is made here.

### Allowed actions

Only EC and HC repository edits; temporary non-sensitive helpers under C:/Users/karl/.codex/tmp/ec-2026-09-20-006. Inspect #24 then create one replacement with matching sanitized administrative content, delete only verified #24, add replacement to Project 5 and select In Progress. Existing GitHub credentials in memory and documented browser UI permitted. Run existing tests/final checker. Commit/push with finite primary PR and one completion-only closure PR.

### Forbidden actions

No dataset or model download. No query of restricted data. No science, dataset/model access, unrelated issue deletion, account permission change, new project/fields, delegation, sensitive information, force push, history rewrite or protection change.

### Preconditions

Clean base verified. Live board shows only closed issue #24 already in In Progress, replacing the previous draft through user edits. Verify issue title/body before deletion and preserve its relevant content in the new issue.

### Promotion criteria

Old #24 deletion confirmed, one open replacement with exact dataset versions and truthful awaiting-review status, Project In Progress count one and other columns empty. Tests/checker/diff privacy review pass. Finite contracts close.

### Stopping criteria

Stop affected action on identity mismatch, uncertain deletion, failed checks, unrelated divergence or absent permissions. Inspect before retry to avoid duplicates. User interruption stops work immediately.

### Irreversible and external boundaries

Commander explicitly authorizes deletion of the old item and submission of its replacement in the same repository. Delete only #24 after matching title/body. Normal administrator-exempt merge is allowed after fresh admin/push rights, enforce_admins=false and passing required CI; disclose in HC. No protection edit or explicit bypass.

### Required evidence

Issue identity/body/readback, replacement URL, deletion receipt, sole In Progress card, two-file diff, tests/final checker, staged-file/remote/upstream/divergence verification, primary PR/merge/CI. Closure self-identifies without recursive commits.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Read the full active EC, AGENTS, governance, prior HC and named dataset source section. Verified explicit replacement/deletion authority, precise boundary, promotion and stopping criteria, and finite closure on 2026-09-20. Commander additionally confirmed all future board items should be submitted Issues, never Drafts.
