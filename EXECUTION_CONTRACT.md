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

- Contract ID: `EC-2026-09-20-005`
- Task: simplify the existing research Kanban
- Status: `COMPLETE`
- Authorized by: Commander explicitly accepted the current-research scope and requested actual Project creation with its contents on 2026-09-20.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/research-board-2026-09-20`
- Expected base: `03270a43b2ac51fbe78760b40c25bef713108280`
- Linked Handoff Contract: `HC-2026-09-20-005`
- Owner: Adjutant sole writer and operator; no delegation.

### Primary outcome

Latest Commander instruction supersedes the complex initial board: clear all current Project 5 items, retain exactly one Ready draft describing the MIMIC access application awaiting approval, and give each existing status one concise English sentence explaining its contents. Preserve the user-renamed project and existing column choices. No new planning hierarchy.

### Authoritative inputs

Read this amended EC, AGENTS.md, CODEX_TASK_GOVERNANCE.md and prior HC; reuse already-read unchanged harness/profile/research sources and draft only as history. Dataset identity/status is supported by the opening status section of docs/research/dataset_decision_record.md and the latest Commander report. Reuse the previously fully traversed immutable pre_access_decision_package.md evidence at the same research-document revision. Official GitHub API/UI documentation governs mechanics, not scientific authority.

### Allowed actions

Only EC and HC may change in this repository. Temporary non-sensitive helpers/receipts under C:/Users/karl/.codex/tmp/ec-2026-09-20-005. Operate only on existing Project 5; preserve current name, visibility and view. Inspect all items including any hidden columns before clearing. No additional views, fields, invitations or repository-link task. Remove all existing Project 5 cards as explicitly requested (including drafts and any hidden status items), then create exactly one Ready draft. Add concise existing-status descriptions and simplify the README to match. Do not delete repository Issues. Use official authenticated GitHub APIs with existing credentials in memory and browser UI via documented tools. No invented owner or deadline. Read back all items and fields; inspect saved board. Use existing bundled Python/pytest. Normal finite primary and one completion closure Git/PR/CI synchronization is allowed.

### Forbidden actions

No dataset or model download. No query of restricted data. No scientific execution, approval, decisions, or change to research/code/tests. No recreation of deleted issue 15, unsolicited comments/messages, unrelated Project edits, public visibility expansion, module dispatch, paid resources, force push, history rewrite, protection weakening or explicit bypass.

### Preconditions

Existing two dirty contracts are this interrupted task, not unrelated changes. Initial task began at expected base; inspect current Project after user edits and retraverse amendment before further mutation. User authorizes this administrative work here in Adjutant. Board tasks do not start their underlying research work.

### Promotion criteria

Project 5 contains exactly one Ready item and concise explanations for all existing statuses; other columns are empty. MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 are the planned coupled source; distinguish submitted credentialing from access granted. Gate 0 remains open. Verification and required checks pass; user receives actual Project URL; finite contracts close.

### Stopping criteria

Stop affected action on identity mismatch, unrelated divergence, failed checks, sensitive content or absent permission. Inspect uncertain results before retry; never duplicate Projects/items. No scientific task follows board creation.

### Irreversible and external boundaries

Current Commander explicitly authorizes clearing all Kanban contents and replacing them with one Ready access-status card. Use private visibility by default, no invitations or notifications to others. Required contract sync follows AGENTS. Ordinary administrator-exempt merge permitted only after fresh actual permissions, enforce_admins=false and successful required CI, disclosed in HC; no override/protection edit.

### Required evidence

Initial/final revisions, two-file diff, source/draft review, Project ID/URL/visibility/repository link, field/options and all-item readback, saved board UI, tests/final checker/privacy review, staged files/remote/upstream/divergence, PR/merge/CI. Closure self-identifies in GitHub without recursive commits.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Task paused immediately when Commander requested stop; no primary commit or PR occurred. Latest instruction resumes only the simplified boundary. Prior 19-card work is historical, not the final outcome.

- Adjutant fully retraversed amended EC, AGENTS, governance, prior HC and named current source section on 2026-09-20. Verified latest clearing/replacement authority, existing-user-edit preservation, exact boundary, no science, promotion/stops and finite closure. Prior unchanged inputs reused as specified.
