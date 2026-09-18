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

## Handoff record `HC-2026-09-18-001`

### Identity and status

- Linked Execution Contract: `EC-2026-09-18-001`
- Task: synchronize non-sensitive progress, literature and four-role configuration for the sole NeurIPS 2027 Main Track objective
- Status: `COMPLETE`
- Prepared by: Executor; Adjutant owns publication and final external archive
- Handoff date: 2026-09-18 (Europe/London)

### Outcome

Phase 1 integrates the authorized four-role configuration, explicit sole
submission objective, dated public administrative progress, safe historical
dataset explanation, portable entry and full canonical research/report index.
Additional explicit migration authority includes the already-sanitized Chinese
session recovery record with a prominent historical-status wrapper.
The pre-access plan integrates Advisor priorities and proposed management
checkpoints, Engineer's six bounded packages, and Executor readiness boundaries.
The substantive preparation, mandated pytest, final repository checker and
diff checks pass. Adjutant verified primary publication, post-merge CI and the
local migration archive at the primary merge. This finite two-contract closure
records those receipts; final archive revision refresh follows closure merge.
This is a protocol/administrative synchronization, not completed science.

### Changed boundary

The observed 23-path change set is:

- `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, `CODEX_ROLE_HARNESS.md`;
- `.codex/agents/advisor.toml`, `.codex/agents/adjutant.toml`,
  `.codex/agents/engineer.toml`, `.codex/agents/executor.toml`;
- `EXECUTION_CONTRACT.md`, `HANDOFF_CONTRACT.md`, `README.md`, `docs/roadmap.md`;
- `docs/research/README.md`, `docs/research/dataset_decision_record.md`,
  `docs/research/decision_log.md`, `docs/research/research_contract.md`,
  `docs/research/scope_charter.md`, `docs/research/submission_strategy.md`;
- `docs/research/progress_2026-09-18.md`,
  `docs/research/pre_access_preparation_plan.md`,
  `docs/research/literature_progress_index.md`;
- `Handoff/README.md`, `Handoff/dataset_preparation_note_2026-09-15.md`,
  `Handoff/session_recovery_2026-09-18.md`.

No existing
literature, scientific audit, report table, code or test is removed or changed.
The source Desktop checkout and its local contracts remain untouched.
The completion-only change is restricted to `EXECUTION_CONTRACT.md` and
`HANDOFF_CONTRACT.md`, based on the exact primary merge. Adjutant verified all
83 original paths retained, 71 original files byte-identical and 94 final
tracked paths. No new substantive artifact is introduced by closure.

### Facts

Credentialing is reported Awaiting review; both required CITI courses Passed;
full report uploaded with status Review; DUA and access unconfirmed. Gate 0
remains open. Method A remains sole route. The record contains no live-account
verification, certificate/PDF audit, new literature verification or experiment.

### Decisions recorded

DR-0019 makes NeurIPS 2027 Main Track the sole submission objective. Historical
venue alternatives carry no current authorization. All scientific kill gates
remain binding. Four runtime roles use Astra: Advisor Ultra, Adjutant Medium,
Engineer XHigh and Executor Low. Profile defaults are not runtime enforcement.

### Assumptions and unresolved items

Sanitized status receipts are accepted as reported evidence, not external
approval. Clinical unit/readers, exact executable specifications, remaining
Gate-0 choices, institutional/security/licence/capacity facts and resource
qualification remain open. No official 2027 deadline is inferred.

### Validation and review evidence

Mandatory contracts/governance and all targeted inputs were traversed.
Executor re-traversed the Adjutant-amended EC clarification allowing existing
static compilers only within mandated pytest. `pytest -q` passed all 53 tests
in 12.86 seconds; `git diff --check` passed. The targeted scan of new migration
and progress/plan/index text found no email address, private-key block, common
API/GitHub token or tokenized URL pattern. This is a bounded scan, not proof
against every possible sensitive string. The source explanation hash matches
`7bbf45fecbbcbd87a35021dd646f649d84b72ea3ee3a51c39fa911483b7aa418`.
Advisor and Engineer separately completed read-only planning receipts,
relayed by Adjutant and integrated with attribution; neither receipt is an
independent implementation review or a fresh literature search. No standalone
resource compiler ran. `python scripts/check_repository.py --final --base-ref
origin/main` returned `Repository contract: OK` after the publishable lifecycle
transition. `git diff --check` passed again. Final evidence-only HC wording
is checked once more before the direct publication handoff.

Adjutant's final primary review passed scope, protocol-objective and plan
checks plus targeted privacy, binary and size scans. For the external package,
Adjutant compared each project file against its Git blob, recorded a 98-file
manifest, verified the Git bundle and restored it offline to the exact primary
merge. Closure-state pytest, final checker and diff-check results are supplied
directly in the Executor receipt before closure publication; they do not
replace the primary evidence above.

### Git and external evidence

Executor confirmed branch `codex/neurips-2027-progress-sync`, origin URL
`https://github.com/DearKarl/ambiguity-is-not-conflict.git`, and HEAD/origin/main
`d63e96abafe965ba0a59fb2c8442921fe94d0ab6`; only EC was initially modified.
Adjutant reports 12 worktrees inventoried, no unpublished local branch commits,
and only `cc3c2ad`'s governance overlay absent from main; no unique scientific
branch content. Adjutant subsequently supplied these verified primary receipts:

- Head: `8ffc4217047c3e07000974f525f4a5626bc2ff97`.
- PR: https://github.com/DearKarl/ambiguity-is-not-conflict/pull/10.
- Merge: `156da144f097b0c817d6b351a2bd1205473c58f3`.
- Branch CI: https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35401681440 (`SUCCESS`).
- PR CI: https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35401697772 (`SUCCESS`).
- Post-merge main CI: https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35401764981 (`SUCCESS`).

The ordinary SHA-guarded REST merge used the verified sole collaborator
DearKarl condition, required review count one and `enforce_admins=false`.
No explicit override or protection change occurred. The Desktop package at
`/Users/dearkarl/Desktop/Handoff/ambiguity-is-not-conflict-2026-09-18` and its
ZIP are verified at the primary merge; the bundle includes origin/main and the
already-public four-role branch. These are Adjutant receipts, not repeated
Executor archive inspections.

Executor confirmed the clean closure branch
`codex/neurips-2027-progress-sync-completion` at the primary merge, equal to
origin/main. The closure commit/PR identity and final delivery revision belong
in the external receipt and Git history, not recursively in these contracts.

### Deviations and negative results

Adjutant's pre-commit staged check found Markdown hard-break trailing spaces
in the two new historical migration copies; the earlier unstaged diff check
had not covered those then-untracked files. Executor normalized trailing
whitespace in those copies only and documented it in their wrappers. Original
Desktop sources remain untouched. `git diff --cached --check` passed and the
final checker returned `Repository contract: OK` for this formatting-only
correction; the full pytest suite was not repeated.

Large read output was truncated and recovered through bounded output segments.
One patch context failed before any documentation changes from that patch;
it was reapplied with the exact context. No scientific negative result is
produced; no approval or execution state is promoted.

### Residual risks and recovery

Metadata contains restricted identifiers and must never be treated as public
or harmless. No private documents or restricted content are copied. Historical
source notes contain older status language, explicitly superseded by the dated
wrapper and progress ledger. Primary publication and archive verification are
supported by the Adjutant receipts above; the archive still needs its mechanical
final-revision refresh after closure merge. The original Desktop source's four
changes remain preserved; its authorized role delta is integrated in the
published repository. Data access and every scientific execution gate remain
separate and unresolved as recorded.

### Next permitted boundary

No further substantive work is authorized. Executor returns closure check
results and stops without staging, committing or publishing. Adjutant may
publish this completion-only closure, verify its CI, and mechanically refresh
the external snapshot, manifest, receipt and ZIP to the final closure revision
as delivery verification. No new substantive docs or recursive closure record
are permitted. Any later project work requires a fresh bounded contract;
core code, data/model access, simulations and research execution remain blocked.
