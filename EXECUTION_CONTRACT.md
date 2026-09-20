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

- Contract ID: `EC-2026-09-20-004`
- Task: permanently delete issue 15 and prepare a PhD Kanban discussion
- Status: `COMPLETE`
- Authorized by: Commander's explicit request on 2026-09-20 to permanently delete issue 15 and discuss a GitHub Project/Kanban for this doctoral research; no other modules.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/delete-issue-15-2026-09-20`
- Expected base: `f0e9ebe6cd60dc54bc7a8d420eaaaec5bfd3e15a`
- Linked Handoff Contract: `HC-2026-09-20-004`
- Owner: Adjutant, sole writer; no delegation.

### Primary outcome

Permanently delete the specifically authorized issue 15, verify the result, and prepare a concrete Kanban discussion proposal with statuses, fields, initial cards and acceptance criteria. Project creation remains for discussion, not part of this external mutation. No scientific change.

### Authoritative inputs

Read this contract, AGENTS.md, CODEX_TASK_GOVERNANCE.md, CODEX_ROLE_HARNESS.md, .codex/agents/adjutant.toml, prior HANDOFF_CONTRACT.md, docs/research/research_contract.md, docs/research/pre_access_decision_package.md and Commander's current request in full. Existing checker and CI requirements govern publication.

### Allowed actions

Only the two contracts may change in this worktree. Read and positively identify GitHub issue 15, permanently delete it through the official API or UI, and verify absence. No additional comment is needed. Use bundled Python and existing pytest target ec-2026-09-20-001-validation. Non-sensitive temporary helper files may be written under C:/Users/karl/.codex/tmp/ec-2026-09-20-004. Credentials stay in memory. Normal fetch, branch, commit, push, PR and merge for required contract records follow the finite primary and one completion closure lifecycle. Read official GitHub documentation for discussion.

### Forbidden actions

No dataset or model download. No query of restricted data. No scientific execution, new research decisions, code/test/research-document changes, deletion of any other issue, comment creation, Project creation, or delegation to any module. Do not rewrite historical Git records; full deletion here means the GitHub issue object, not erasure of every reference. No force push, history rewrite, protection changes or explicit bypass.

### Preconditions

Initial worktree clean at expected base. Verify live main and exact issue identity before mutation. Complete traversal before external actions. User's direct request authorizes Adjutant to perform this bounded administrative reversal without dispatch.

### Promotion criteria

Successful deletion response and subsequent authenticated readback confirm issue 15 is no longer available. A source-grounded Kanban proposal is reviewable. Checks pass, only two contracts change, finite synchronization receipts recorded, and discussion returns to Commander.

### Stopping criteria

Stop affected action on target mismatch, unrelated divergence, failed checks, missing authority or uncertain external response; inspect before retry. Stop after closure and discussion; do not create a Project.

### Irreversible and external boundaries

The irreversible permanent deletion of issue 15 is explicitly authorized by the latest user request; no renewed confirmation is needed. Required contract synchronization is authorized by AGENTS. Ordinary administrator-exempt merge is allowed only with freshly verified actual permissions and enforce_admins=false after required CI, disclosed in HC. No override flags or protection changes.

### Required evidence

Issue identity and before/after readback, exact two-file diff, pytest and final checker, privacy review, remote/branch/upstream/divergence, primary PR/merge/CI receipts. Closure identity remains self-evidencing in GitHub, never recursively committed.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Initial inspection found a clean worktree at the expected base. Mandatory governance, prior contracts, role profile and research inputs read; truncated research output recovered by bounded reads. Full new EC reread follows before action.

- Adjutant completed full new-contract traversal on 2026-09-20. Verified explicit permanent-deletion authority, exact issue and two-contract boundary, source-grounded discussion only, forbidden actions, stops, evidence and finite closure. No delegation.

### Completion record

Issue 15 deletion verified by successful mutation and HTTP 410 Gone. Kanban discussion draft prepared outside Git with 19 candidate cards. Primary PR 20 merged as a595b7e28eaf101c67e80f8c53433eb2c0ba4205 with branch, PR and main CI successful. Only validation/publication/CI of this one two-contract completion closure remain before final discussion handoff.
