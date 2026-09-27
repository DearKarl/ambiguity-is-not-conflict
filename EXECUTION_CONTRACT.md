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
- Contract ID: `EC-2026-09-27-ICML`
- Task: record the Commander-authorized ICML 2027 venue transition
- Status: `COMPLETE`
- Authorized by: Commander explicit venue change and GitHub synchronization request, 2026-09-27
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/icml-2027-venue-transition`
- Expected base: `0d90d822dd7e67b7673ed20c93c3f3325843b202` (remote main; local detached 585be42)
- Linked Handoff Contract: `HC-2026-09-27-ICML`
- Owner: executor — Executor (GPT-6 Astra / Low)

### Primary outcome
Record ICML 2027 main conference as the sole submission objective, superseding
DR-0019's venue choice only. Synchronize canonical active planning references.
Manuscript migration and remote rename belong to another Executor task.

### Authoritative inputs
AGENTS.md, CODEX_ROLE_HARNESS.md, CODEX_TASK_GOVERNANCE.md, this contract,
HANDOFF_CONTRACT.md; README.md, docs/roadmap.md, docs/research/README.md,
submission_strategy.md, research_contract.md, scope_charter.md,
pre_access_preparation_plan.md and decision_log.md (research-relative paths),
Handoff/README.md and paper/README.md; Commander request and parent bounded dispatch.
Read remote changes after fetch before adopting that base. Official ICML
2026 CFP is historical guidance only; 2027 dates/template are unconfirmed.

### Allowed actions
Read/fetch remote, inspect divergence, adopt verified current main on named branch,
update only contracts and named documentation inputs; add venue decision and
minimal dated coordination entry. Run pytest -q (including existing static
compiler calls), python scripts/check_repository.py --final, and diff checks.
Commit, push, PR and normal merge only after checks; finite two-contract closure.
Normal administrator-exempt merge is narrowly authorized by parent dispatch
on 2026-09-27 only after verifying sole collaborator DearKarl, existing
enforce_admins=false, passing required checks and parent diff review. Use a
normal SHA-guarded merge; never an override flag or protection change.

### Forbidden actions
No scientific method, estimand, gate, budget, resource or approval changes.
No dataset or model download. No query of restricted data.
No datasets/models, restricted records, credentials, private correspondence,
scientific execution, annotation, paid compute, standalone compilers, forced
push, history rewrite, protection changes, manuscript/browser edits or overlapping
writer work. Do not assert manuscript migration completed without owner receipt.

### Preconditions
Clean checkout except sole EC draft; verified remote base and exclusive ownership.
Fully read listed inputs and record traversal before substantive edits.

### Promotion criteria
Active venue references agree with new decision; historical evidence retained;
2026 guidance explicitly provisional; all checks pass and publication evidence
recorded without claiming scientific progress.

### Stopping criteria
Stop on remote/ownership conflict, sensitive content, scope ambiguity or failing
checks. Resolve routine bounded errors without weakening checks. If the narrow verified normal-merge conditions fail, leave PR ready and report
the blocker; do not override protection.

### Irreversible and external boundaries
Commander authorized GitHub synchronization of non-sensitive documentation.
No other account or publication action. Closure follows primary merge and CI.

### Required evidence
Exact revisions, changed paths, commands/outcomes, PR and CI receipts, deviations,
recovery state and next owner. No retrospective scientific results.

### Pre-task traversal record
- Traversal status: `COMPLETE`
- Completed 2026-09-27: mandatory governance, prior contracts and every named
  documentation input read fully; authority, scope, checks and stop boundaries
  verified. Only this EC changed before traversal. Remote inspection is the next
  allowed action; any changed authority requires another full traversal.

- Remote review: 0d90d82 adds September 20 pre-access documentation and completed
  administrative issue/board contracts. Preserve all additions; no method change.
  Latest EC/HC and changed active input sections read fully before adoption.

- Amendment: paper/README.md included for venue-policy wording only. Full amended
  contract and that input read before its edit; all other boundaries unchanged.

- Merge amendment: verified sole collaborator DearKarl with admin/push rights and
  existing enforce_admins=false, required reviews one. Full amended contract
  traversal completed before publication; parent independently reviewed the
  substantive diff with no blocking findings. CI remains a merge prerequisite.

### Completion record
Primary head 3d1282e317a5fb24e4b86353750a911134688202, PR #28,
merged as deaa3fb4faa3e577e667f158c7cec6645eaa2571. Branch CI 36355974688,
PR CI 36355987086 and post-merge CI 36356040306 all passed. Parent independently
reviewed substantive documentation with no blocking findings. Verified sole
collaborator DearKarl, admin/push rights and enforce_admins=false; ordinary
SHA-guarded REST merge used, no explicit override or protection change.
This one closure changes only EC/HC at the exact primary merge. Its identity
and CI self-identify in Git/GitHub and final receipt; no recursive closure.
Next owner: Adjutant for delivery, Engineer for a separately bounded calendar
feasibility review. No substantive or scientific work remains authorized here.
