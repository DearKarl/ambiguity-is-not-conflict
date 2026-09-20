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

## Handoff record `HC-2026-09-20-006`

### Identity and status

- Linked Execution Contract: `EC-2026-09-20-006`
- Task: replace the closed MIMIC access item with an open submitted Issue
- Status: `READY FOR REMOTE FINALIZATION`
- Prepared by: Adjutant, sole operator
- Handoff date: 2026-09-20

### Outcome

Deleted the verified old MIMIC access issue #24 and submitted [issue #25](https://github.com/DearKarl/ambiguity-is-not-conflict/issues/25) with its concise English title/body, tracking MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 credentialing awaiting review. The replacement is open and is the sole item in Project 5 In Progress. Only EC/HC repository files change; project descriptions, science, code and tests remain unchanged.

### Facts

Live board inspection found the user had converted the prior draft into closed issue #24 and moved it In Progress. Commander explicitly requested deleting/replacing it and confirmed future board items must be submitted Issues, never Drafts. This preference is recorded for future intake; each future task still requires its own bounded authority. Dataset access is not confirmed, and no new PhysioNet account verification is claimed. The same reported administrative status was preserved.

### Validation and review evidence

Full contract traversal preceded mutation. Authenticated REST verified old title/body/state and the new open issue's matching body. GraphQL deleteIssue returned the expected repository; authenticated old-issue readback returned HTTP 410. Project UI readback verifies the single replacement and In Progress status before publication. Existing pytest, final repository checker and diff/privacy review are required before publication; completion phase records final evidence. No scientific or independent review is claimed.

### Git and external evidence

Initial base e780a2c62dddcc2ce652d53e0e6902ff043e9249; origin https://github.com/DearKarl/ambiguity-is-not-conflict.git; branch codex/mimic-access-issue-2026-09-20. Primary and one closure PR follow successful checks. Any ordinary administrator-exempt merge requires fresh admin/push rights and enforce_admins=false with CI passing; no protection edit or explicit bypass. Primary merge receipts enter the completion-only record; closure identifies itself in Git/GitHub.

### Residual risks and recovery

No scope deviation. Only sanitized administrative content was published. Metadata contains restricted identifiers and must never be treated as public or harmless. Old issue deletion is permanent and was explicitly requested. Recovery is the replacement #25, not another duplicate. Gate 0 remains open; In Progress describes administrative follow-up, not authorized scientific execution. Helpers and non-sensitive receipts are under C:/Users/karl/.codex/tmp/ec-2026-09-20-006.

### Next permitted boundary

Finish verification and finite primary/completion synchronization; return issue and board links, then stop. No data access or research work follows.
### Changed boundary

Only the execution/handoff contracts and the specifically authorized GitHub issue/project item changed. No scientific files, credentials, data, tests or code changed.

### Decisions recorded

Use a submitted open Issue in In Progress. The Commander's continuing preference is to submit future authorized board items directly, never as drafts.

### Assumptions and unresolved items

PhysioNet approval and actual dataset access remain unconfirmed. No underlying scientific task is started. No missing input prevents this administrative replacement.

### Deviations and negative results

Initial contract validation found required handoff headings/date and an exact safety phrase missing; these formatting omissions were restored before publication. No checker/test was changed and no scientific scope was expanded.