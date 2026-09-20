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

- Contract ID: `EC-2026-09-20-003`
- Task: withdraw discussion issue 15 and discuss organization with Commander
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander's explicit request on 2026-09-20 to withdraw the previously created issue and discuss here in Adjutant without other modules.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/withdraw-issue-15-2026-09-20`
- Expected base: `f5943238ba2efe3ca3e42806a85251a021b51e75`
- Linked Handoff Contract: `HC-2026-09-20-003`
- Owner: Adjutant, sole writer; no delegation.

### Primary outcome

Close issue 15 as not planned, preserving its English content and history; verify readback and discuss organization here. No Project creation or scientific change.

### Authoritative inputs

Read this contract, AGENTS.md, CODEX_TASK_GOVERNANCE.md, CODEX_ROLE_HARNESS.md, .codex/agents/adjutant.toml, prior HANDOFF_CONTRACT.md, docs/research/research_contract.md and Commander's current request in full. Existing checker and CI requirements govern publication.

### Allowed actions

Only the two contracts may change in this worktree. Read GitHub issue 15, close it with state_reason not_planned, verify and open its URL. No additional comment is needed. Use bundled Python and existing pytest target ec-2026-09-20-001-validation. Non-sensitive temporary helper files may be written under C:/Users/karl/.codex/tmp/ec-2026-09-20-003. Credentials stay in memory. Normal fetch, branch, commit, push, PR and merge for required contract records follow the finite primary and one completion closure lifecycle. Read official GitHub documentation for discussion.

### Forbidden actions

No dataset or model download. No query of restricted data. No scientific execution, new research decisions, code/test/research-document changes, issue deletion, comment creation, Project creation, or delegation to any module. No force push, history rewrite, protection changes or explicit bypass.

### Preconditions

Initial worktree clean at expected base. Verify live main and exact issue identity before mutation. Complete traversal before external actions. User's direct request authorizes Adjutant to perform this bounded administrative reversal without dispatch.

### Promotion criteria

Authenticated readback confirms issue 15 closed with not_planned; history preserved. Checks pass, only two contracts change, finite synchronization receipts recorded, and discussion returns to Commander.

### Stopping criteria

Stop affected action on target mismatch, unrelated divergence, failed checks, missing authority or uncertain external response; inspect before retry. Stop after closure and discussion; do not create a Project.

### Irreversible and external boundaries

The specific issue closure is explicitly authorized. Required contract synchronization is authorized by AGENTS. Ordinary administrator-exempt merge is allowed only with freshly verified actual permissions and enforce_admins=false after required CI, disclosed in HC. No override flags or protection changes.

### Required evidence

Issue identity and before/after readback, exact two-file diff, pytest and final checker, privacy review, remote/branch/upstream/divergence, primary PR/merge/CI receipts. Closure identity remains self-evidencing in GitHub, never recursively committed.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Initial read-only inspection verified clean worktree, expected HEAD and correct origin. All listed sources except this new draft have been read in full. This EC is the sole pre-traversal mutation.

- Adjutant completed full traversal of this new EC and all listed inputs on 2026-09-20; verified explicit authority, sole-writer scope, exact target, no science, promotion/stops, external boundaries and finite closure. No modules dispatched.
