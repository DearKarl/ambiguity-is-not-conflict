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

## Historical completed record (preserved verbatim as quotation)

> ## Handoff record `HC-2026-09-20-006`
>
> ### Identity and status
>
> - Linked Execution Contract: `EC-2026-09-20-006`
> - Task: replace the closed MIMIC access item with an open submitted Issue
> - Status: `COMPLETE`
> - Prepared by: Adjutant, sole operator
> - Handoff date: 2026-09-20
>
> ### Outcome
>
> Deleted the verified old MIMIC access issue #24 and submitted [issue #25](https://github.com/DearKarl/ambiguity-is-not-conflict/issues/25) with its concise English title/body, tracking MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 credentialing awaiting review. The replacement is open and is the sole item in Project 5 In Progress. Only EC/HC repository files change; project descriptions, science, code and tests remain unchanged.
>
> ### Facts
>
> Live board inspection found the user had converted the prior draft into closed issue #24 and moved it In Progress. Commander explicitly requested deleting/replacing it and confirmed future board items must be submitted Issues, never Drafts. This preference is recorded for future intake; each future task still requires its own bounded authority. Dataset access is not confirmed, and no new PhysioNet account verification is claimed. The same reported administrative status was preserved.
>
> ### Validation and review evidence
>
> Full contract traversal preceded mutation. Authenticated REST verified old title/body/state and the new open issue's matching body. GraphQL deleteIssue returned the expected repository; authenticated old-issue readback returned HTTP 410. Project UI readback verifies the single replacement and In Progress status before publication. All 53 existing tests passed; final repository checker and diff/privacy review passed. Browser reload confirmed counts 0/0/1/0/0, with open issue #25 in In Progress. No scientific or independent review is claimed.
>
> ### Git and external evidence
>
> Initial base e780a2c62dddcc2ce652d53e0e6902ff043e9249; origin https://github.com/DearKarl/ambiguity-is-not-conflict.git; branch codex/mimic-access-issue-2026-09-20. Primary and one closure PR follow successful checks. Any ordinary administrator-exempt merge requires fresh admin/push rights and enforce_admins=false with CI passing; no protection edit or explicit bypass. Primary commit 1771f56, PR #26 merged as cc74b26001ce0128ae717fb48abd5ad4aac31d85. PR CI 35504761105, push CI 35504759254 and post-merge CI 35504815605 all passed. Fresh admin/push and enforce_admins=false were verified; ordinary administrator exemption used with no protection edits. Closure identifies itself in Git/GitHub.
>
> ### Residual risks and recovery
>
> No scope deviation. Only sanitized administrative content was published. Metadata contains restricted identifiers and must never be treated as public or harmless. Old issue deletion is permanent and was explicitly requested. Recovery is the replacement #25, not another duplicate. Gate 0 remains open; In Progress describes administrative follow-up, not authorized scientific execution. Helpers and non-sensitive receipts are under C:/Users/karl/.codex/tmp/ec-2026-09-20-006.
>
> ### Next permitted boundary
>
> Only verification and normal synchronization of this one completion record remain; return issue and board links, then stop. No data access or research work follows.
> ### Changed boundary
>
> Only the execution/handoff contracts and the specifically authorized GitHub issue/project item changed. No scientific files, credentials, data, tests or code changed.
>
> ### Decisions recorded
>
> Use a submitted open Issue in In Progress. The Commander's continuing preference is to submit future authorized board items directly, never as drafts.
>
> ### Assumptions and unresolved items
>
> PhysioNet approval and actual dataset access remain unconfirmed. No underlying scientific task is started. No missing input prevents this administrative replacement.
>
> ### Deviations and negative results
>
> Initial contract validation found required handoff headings/date and an exact safety phrase missing; these formatting omissions were restored before publication. No checker/test was changed and no scientific scope was expanded.

## Handoff record `HC-2026-09-27-ICML`

### Identity and status
- Linked Execution Contract: `EC-2026-09-27-ICML`
- Task: record sole ICML 2027 venue transition
- Status: `READY FOR REMOTE FINALIZATION`
- Prepared by: executor — Executor (GPT-6 Astra / Low)
- Handoff date: 2026-09-27

### Outcome
DR-0020 records the Commander-authorized sole ICML 2027 main-conference target.
Active planning entries agree; the inherited calendar requires an Engineer
feasibility review. Historical scientific decisions and administrative receipts
remain dated evidence. Manuscript migration is separately owned.

### Changed boundary
Only EC/HC, README.md, docs/roadmap.md, docs/research/README.md,
submission_strategy.md, research_contract.md, scope_charter.md,
decision_log.md, pre_access_preparation_plan.md (research-relative),
Handoff/README.md and paper/README.md. No code, tests, scientific protocols,
thresholds, resources or Gate-0 approvals changed.

### Facts
Remote main had advanced from local 585be42 to 0d90d822dd7e67b7673ed20c93c3f3325843b202.
Its September 20 pre-access documents and administrative changes were retained.
Official ICML 2026 CFP checked; 2027 exact dates/template remain unconfirmed.

### Decisions recorded
DR-0020 supersedes only the prior venue choice. Intended manuscript project and
private repository names are ICML_2027_Manuscript; their completed state requires
the separate manuscript owner's receipt. Method A and all scientific gates persist.

### Assumptions and unresolved items
No new data-access evidence or submission readiness is inferred. Engineer owns
future calendar/resource feasibility review; Commander retains target authority.

### Validation and review evidence
Full mandatory traversal and targeted input reads completed. Advisor's read-only
scope recommendation was relayed by Adjutant; parent then independently
reviewed all ten substantive documentation files with no blocking findings.
Initial pytest returned 51 passed and two exact-text documentation failures:
explicit safety wording and historical call wording. Restored those accurate
statements without changing tests; repeat `pytest -q`: 53 passed. `python scripts/check_repository.py --final
--base-ref origin/main`: Repository contract: OK. `git diff --check`: passed.

### Git and external evidence
Origin is https://github.com/DearKarl/ambiguity-is-not-conflict.git; branch
codex/icml-2027-venue-transition starts at verified remote main 0d90d82.
Primary PR and CI will self-identify on publication. Only the EC narrow normal administrator-exempt merge is authorized after
parent review and passing CI; no override flag or protection change.

### Deviations and negative results
Read-only remote inspection revealed newer main; used that base rather than
stale local history. Prior HC preserved as a quotation because checker permits
exactly one active record. No scientific result was generated. Initial exact-text test failures were
resolved in documentation only; no validation rule was weakened.

### Residual risks and recovery
ICML 2027 official rules and feasibility remain unresolved. No dataset or model
download. No query of restricted data. Recovery is the verified base and branch
history; no force push or original manuscript replacement occurred here.

### Next permitted boundary
Run mandated checks, review bounded diff, publish primary PR and merge only under
the EC narrow normal administrator-exempt conditions. After primary merge and CI, one contracts-only
closure may record completion. If reviews block merge, return PR to Adjutant.
