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

## Handoff record `HC-2026-09-20-005`

### Identity and status

- Linked Execution Contract: `EC-2026-09-20-005`
- Task: simplify the existing research Kanban
- Status: `COMPLETE`
- Prepared by: Adjutant, sole writer and operator
- Handoff date: 2026-09-20 (Europe/London)

### Outcome

[Project 5](https://github.com/users/DearKarl/projects/5/views/1), named ambiguity-is-not-conflict by the Commander, now contains exactly one Ready draft: MIMIC-CXR / MIMIC-CXR-JPG access — awaiting approval. The other four existing columns are empty. All 17 remaining old cards were removed after inspecting the unfiltered full item list; the user had already removed Blocked and its two items. Five existing statuses and the user's project name/view were preserved. Each status has one concise English purpose sentence, and the README is reduced to the same simple overview.

### Changed boundary

Only EC and HC change in the repository. Temporary helpers are under C:/Users/karl/.codex/tmp/ec-2026-09-20-005. External changes are confined to existing private Project 5. No repository Issue, scientific file, code, test, data or model changed.

### Facts

The dataset decision record and Commander report identify MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0. The card distinguishes credentialing awaiting review from confirmed dataset access; training is complete and its report submitted. No independent PhysioNet account verification is claimed. Initial HEAD/live main was 03270a43b2ac51fbe78760b40c25bef713108280. Gate 0 remains open.

### Decisions recorded

Keep one draft and plain English descriptions: Inbox holds questions/ideas awaiting clarification; Ready holds agreed next steps and applications awaiting prerequisites; In Progress holds active research; Review holds outputs/methods/decisions awaiting review; Done holds documented completed work. No new planning hierarchy, module dispatch, research decisions or execution.

### Assumptions and unresolved items

Dataset approval/access remains pending. Repository Projects-page linkage is excluded by the amended boundary. Existing optional fields remain unused. No further user input is needed for this administrative scope.

### Validation and review evidence

The amended contract traversal preceded resumed changes. Browser reload confirmed exactly 0/1/0/0/0 items across Inbox/Ready/In Progress/Review/Done and all five saved descriptions. The sole draft's body and Ready status were read back. 53 existing tests passed, final repository checker and diff/privacy review passed. Initial checks exposed two omitted legacy metadata-risk phrases in this handoff; both were restored before publication without changing tests or science. No independent scientific review claimed.

### Git and external evidence

Origin is https://github.com/DearKarl/ambiguity-is-not-conflict.git; branch codex/research-board-2026-09-20 begins at the expected base. Existing private visibility preserved. No account permission changes, invitations or sensitive records published. Finite synchronization uses an ordinary administrator-exempt merge only after fresh admin/push rights, enforce_admins=false and passing CI; no protection edit or explicit bypass. Primary commit 4bdd088; PR #22 merged as 7a6aa4d88209aeae3d4188a46e0c88e6afac7f82. PR CI 35503421586 and push CI 35503420298 passed; post-merge CI 35503459585 passed. Fresh admin/push rights and enforce_admins=false were verified; ordinary administrator exemption was used, with no protection change. Closure identifies itself in Git/GitHub.

### Deviations and negative results

Historical initial work created a 19-card board. Work stopped immediately at the Commander's pause request before commit/PR. The latest instruction superseded that content and authorized the simple replacement after contract amendment and traversal. Earlier HC draft described initial work and incorrectly anticipated repository linkage; this dated amendment supersedes that unfinished outcome. Project API lacked scopes, so documented browser controls were used without permission expansion. Async UI updates required saved-state readback; no duplicate Project was created.

### Residual risks and recovery

Metadata contains restricted identifiers and must never be treated as public or harmless. Only sanitized administrative text appears on the board; restricted medical data and identifiers remain excluded. Board status is not scientific authority. Open the existing Project to recover; do not recreate it. Approval must be checked before future data access work.

### Next permitted boundary

Only verification and normal synchronization of this one completion record remain; return the board URL and stop. No underlying research work is authorized by these cards.
