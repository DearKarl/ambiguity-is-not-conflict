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

## Handoff record `HC-2026-09-20-003`

### Identity and status

- Linked Execution Contract: `EC-2026-09-20-003`
- Task: withdraw discussion issue 15 and discuss organization with Commander
- Status: `COMPLETE`
- Prepared by: Adjutant, sole writer; no other module dispatched
- Handoff date: 2026-09-20 (Europe/London)

### Outcome

Issue [15](https://github.com/DearKarl/ambiguity-is-not-conflict/issues/15), titled Discussion: understanding PROBVLM-2ADAPTER, is closed as not_planned at 2026-09-20T09:03:08Z. Authenticated API readback verified both fields and unchanged body. Opening its URL in Codex was queued. No comment or replacement issue was created.

### Changed boundary

Only EXECUTION_CONTRACT.md and HANDOFF_CONTRACT.md change. A non-sensitive API helper is outside Git at C:/Users/karl/.codex/tmp/ec-2026-09-20-003/github.py. No scientific or Project changes.

### Facts

Commander explicitly requested withdrawal and direct Adjutant discussion without other modules. Initial issue was open. Initial HEAD and live main were f5943238ba2efe3ca3e42806a85251a021b51e75. Gate 0 remains open.

### Decisions recorded

Interpret withdrawal as reversible closure with not_planned, preserving history. No deletion or rollback of research documents or prior PRs. Organization discussion conveys no authority to create a Project.

### Assumptions and unresolved items

Whether to use a GitHub Project remains Commander's choice. Primary publication and CI are complete. The single completion-only closure identifies itself through Git and GitHub; no recursive third record is permitted.

### Validation and review evidence

Full traversal completed before substantive action. Authenticated before/after issue readback passed, including exact body equality. Only administrative records are changed; no independent scientific review is needed or claimed. Before contract publication, python -m pytest -q passed 53 tests in 21.68s; python scripts/check_repository.py --final --base-ref origin/main returned Repository contract: OK; git diff --check passed. Bounded privacy and diff review found only authorized administrative content.

### Git and external evidence

Origin is https://github.com/DearKarl/ambiguity-is-not-conflict.git. Working branch codex/withdraw-issue-15-2026-09-20 starts at the verified expected base. Credentials are held only in memory. Primary PR identity and CI are externally self-identifying until the single completion record captures them. Ordinary administrator-exempt merge is narrowly allowed by EC only after fresh permissions/protection verification and required CI; no override or protection edits.

### Deviations and negative results

No other module was dispatched. The explicit user instruction to handle this administrative reversal here governs sole Adjutant execution. No scientific execution or claim promotion occurred.

### Residual risks and recovery

Metadata contains restricted identifiers and must never be treated as public or harmless. No restricted metadata or credentials enter these records. Issue history remains intact and can be reopened only on later authority. On uncertain API result inspect before retrying.

### Next permitted boundary

Validate and synchronize the two administrative records, perform one completion-only closure and return to direct discussion. No Project or new issue creation, delegation, or research execution.

### Primary completion evidence

Primary commit e3ccd6d was published in [PR 18](https://github.com/DearKarl/ambiguity-is-not-conflict/pull/18), attached to this task, and merged as 7d028daadb91318a6d2f011f7b0b50e57ad029a7. Push CI 35501300987, PR CI 35501302416 and post-merge main CI 35501352650 all completed successfully. Remote/base divergence was 0/0 before publication; exact staged paths were the two contracts. Fresh permissions confirmed admin and push true, enforce_admins=false, strict repository-contract and one approving review. The ordinary existing administrator exemption was used with exact SHA guard after CI, without override or protection edits. No independent review is claimed. The issue remains closed, not deleted; a later capability question about deletion does not authorize it. Commander was told permanent deletion is possible but was not performed. Only validation/publication/CI of this completion closure remains; return to Adjutant discussion afterward.
