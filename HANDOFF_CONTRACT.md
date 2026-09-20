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

## Handoff record `HC-2026-09-20-004`

### Identity and status

- Linked Execution Contract: `EC-2026-09-20-004`
- Task: permanently delete issue 15 and prepare a PhD Kanban discussion
- Status: `READY FOR REMOTE FINALIZATION`
- Prepared by: Adjutant, sole writer; no delegation
- Handoff date: 2026-09-20 (Europe/London)

### Outcome

Permanently deleted the specifically authorized GitHub issue 15, Discussion: understanding PROBVLM-2ADAPTER. The official GraphQL deleteIssue mutation returned success for DearKarl/ambiguity-is-not-conflict. Subsequent authenticated REST readback returned HTTP 410 Gone while the repository remained accessible. No other issue or historical Git record was deleted.

A discussion proposal uses one research Project, a Status-based Kanban and optional decision/evidence views over the same cards. Proposed columns are Inbox, Ready, In Progress, Review, Blocked and Done. Initial contents distinguish completed protocol preparation from unapproved D1-D6 choices and future gated execution. No Project or replacement issue was created.

### Changed boundary

Only EXECUTION_CONTRACT.md and HANDOFF_CONTRACT.md change. Non-sensitive temporary API helpers are under C:/Users/karl/.codex/tmp/ec-2026-09-20-004. No scientific documents, code, tests, data or models change.

### Facts

Commander explicitly requested permanent deletion after the prior close-only action and asked to discuss a doctoral research Project/Kanban. The initial worktree was clean at f0e9ebe6cd60dc54bc7a8d420eaaaec5bfd3e15a, equal to live origin/main. The research contract and pre-access decision package confirm Gate 0 remains open; the package is protocol recommendations, not completed experiments or blanket approval.

### Decisions recorded

Delete only issue 15, without further confirmation because the current instruction is explicit. Discuss a lightweight board using English artifact titles, links to canonical research records and specific completion evidence. Proposed board status is workflow status, never scientific approval. All new fields, cards and organization choices remain discussion proposals.

### Assumptions and unresolved items

The board initially covers Ambiguity Is Not Conflict; whether it should cover the entire doctorate's additional activities is a question for Commander. No dates, commitments, new scientific choices or staffing assignments are invented. A draft card can capture a question before any repository Issue is created.

### Validation and review evidence

Full new-contract traversal completed before deletion. Exact issue number, title and URL were checked before the single deletion mutation; success, 410 Gone and repository availability were verified afterward. Official GitHub documentation verifies deletion and Projects/Kanban/draft capabilities. Before contract publication, python -m pytest -q passed 53 tests in 19.58s; python scripts/check_repository.py --final --base-ref origin/main returned Repository contract: OK. Diff and bounded privacy review passed; only two authorized administrative files change. No independent scientific review is required or claimed.

### Git and external evidence

Origin remains https://github.com/DearKarl/ambiguity-is-not-conflict.git. Primary branch codex/delete-issue-15-2026-09-20 begins at the verified expected base. Credentials remain in memory. Primary PR/merge/CI are self-identifying until the completion record captures their receipts. Ordinary administrator-exempt merge is authorized narrowly by EC after fresh permissions/protection and CI verification; no override or protection changes.

### Deviations and negative results

This request replaces the earlier close-only outcome with explicitly authorized permanent deletion. Historical Git references remain; deletion does not claim erasure of every record or cache. No module dispatch, Project creation or scientific execution.

### Residual risks and recovery

Metadata contains restricted identifiers and must never be treated as public or harmless. No restricted records or credentials are published. The issue is permanently deleted; any later recreation would be a new issue requiring authority. Preserve existing Git history. Never blindly retry a deletion after an uncertain response.

### Next permitted boundary

Finish the finite two-contract primary and completion-only synchronization, then discuss the proposed Kanban directly with Commander. Creating or populating a GitHub Project is a later boundary after this discussion; no other module is called.
