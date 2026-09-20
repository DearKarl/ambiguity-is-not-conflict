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

## Handoff record `HC-2026-09-20-001`

### Identity and status

- Linked Execution Contract: `EC-2026-09-20-001`
- Task: compile the pre-access specification, acceptance matrix and finite decision package
- Status: `COMPLETE`
- Prepared by: Executor, sole writer in cd30; Engineer read-only technical owner; Adjutant coordination
- Handoff date: 2026-09-20 (Europe/London)

### Outcome

The packet integrates canonical sources and Engineer's attributed read-only
technical recommendations into a specification, prospective acceptance matrix
and all 24 Gate-0 decisions grouped into six finite discussion sets. EX-A and
NA/PR/DY/DC completions make model, measurement, inference, resource and
decision interfaces reviewable. It is not a scientific implementation,
observed result or Gate-0 freeze. Primary PR #12 is merged with successful
post-merge CI. This is the single two-contract completion record.

### Changed boundary

Exactly seven authorized paths: EXECUTION_CONTRACT.md, HANDOFF_CONTRACT.md,
docs/research/pre_access_readiness_specification.md,
docs/research/pre_access_acceptance_matrix.md,
docs/research/pre_access_decision_package.md, docs/research/README.md, and
docs/research/pre_access_preparation_plan.md. No code, tests, historical
scientific decisions, data or model files are changed. Other worktrees are
preserved. The separately authorized temporary validation dependencies are
outside the repository.

### Facts

Gate 0 remains open. Method A is the sole scientific route and NeurIPS 2027
Main Track the sole submission objective. September 18 credential Awaiting
review, courses Passed and report Review are historical reported states;
DUA/access remain unconfirmed. No live provider or institutional verification
occurred. Package completeness, decision-freeze readiness, stage operational
readiness and scientific success remain distinct.

### Decisions recorded

No new scientific choice, threshold, budget or data access is approved.
DR-0018/DR-0019 boundaries remain intact. Engineer's concrete recommendations
are proposals, not canonical amendments. Adjutant confirmed necessary ordinary
validation preparation in a precisely named temporary directory; EC was
amended and fully re-read before it occurred.

### Assumptions and unresolved items

Open scientific selections, exact executable/software/rights freezes and
external/data-dependent E01--E09 evidence remain blockers to their respective
stages. The package carries finite owner choices, not a generic permission to
implement. No official 2027 deadline or novel contribution is established.

### Validation and review evidence

Executor completed full mandatory and dependent-source traversal, recovering
truncated output in bounded segments. Engineer separately reported complete
read-only traversal at the same source baseline; that is an attributed receipt,
not independent implementation review. Adjutant supplied E01--E09 evidence
triage; Advisor supplied claim/failure and readiness distinctions. Engineer
delivered three design batches plus the NA/PR/DY/DC addendum, with public
immutable configuration/code text inspected in memory only. No model/data
retrieval or scientific execution occurred.

Adjutant's read-only scope receipt confirms all 24 unique rows, seven-file
boundary, historical evidence labels, six decision groups, stage stops,
resource floor and hard-kill distinctions, then rechecked the addendum,
development split consistency and probability-scale calibration correction.
This is coordination/design review, not independent implementation review.
Advisor's final packet-level claim/readiness review passed, explicitly not a
scientific approval or fresh-context independent review. It confirmed estimand
order/signs, own-SD, unequal capacity, frozen-means scope, veto-only and hard
kill, deployable inputs and limited equal-review-count claim. Engineer's final
read-only technical review found no blocking inconsistency and confirmed the
same mathematical interfaces; design/review work stops. Its final bounded
correction supplies proposed CAL-A probability-scale evaluation, NA heading
tie and PR permutation statistic/evaluation split, without approval or run.
Engineer additionally read the final CAL-A/NA/PR integration, matrix I18 and
decision references and passed documentation integration/proposal status;
its requested negative-loglikelihood wording precision was applied without
changing the model or inference. No additional design work is authorized.
Advisor's final delta review also passed CAL-A/NA/PR, I18 and the decision
calibration row; the units finding is closed. Adjutant relayed final scope,
technical and claim acceptance with no additional approval gate. None is
represented as fresh-context independent implementation review.

Existing `python -m pytest -q` passed 53 tests in 20.43 seconds; final
`pytest -q` passed 53 in 19.35 seconds after integration. Final
`python scripts/check_repository.py --final --base-ref origin/main` returned
`Repository contract: OK`. `git diff --check` passed; bounded seven-file
credential/private-key/email/tokenized-URL scan found no matches, with manual
scope/privacy review. Initial final checker correctly rejected the then-
IN-PROGRESS handoff; READY-state verification passed. No tests or checker
were changed. Reproduction uses the executable above, process-only PATH
entries for its directory and the temporary dependency target's bin, plus
PYTHONPATH set to that target and PYTHONUTF8=1. Required final checker is
repeated after receipt-only edits and staged-file verification before commit.

Existing bundled Python 3.12.14 is used. PATH had no working pytest or gh;
pytest==8.4.2 and only its required dependencies were installed with
`python -m pip install --disable-pip-version-check --no-cache-dir --target
C:/Users/karl/.codex/tmp/ec-2026-09-20-001-validation -r requirements-dev.txt`.
Python absolute executable:
`C:/Users/karl/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
Installed dependencies: colorama 0.4.6, iniconfig 2.3.0, packaging 26.3,
pluggy 1.6.0 and pygments 2.21.0. No scientific environment or gh installation.

### Git and external evidence

Initial HEAD, live ls-remote main and fetched origin/main were all
`585be42d47a86b84a16bbf986d83e96f37145306`, with zero divergence; only the
Adjutant EC bootstrap was modified. Origin is
https://github.com/DearKarl/ambiguity-is-not-conflict.git. Created branch
`codex/pre-access-readiness-2026-09-20` after traversal and fetch.

Read-only GitHub REST evidence reports actual admin/push permissions,
`enforce_admins=false`, strict required `repository-contract` check and one
required approving review. The EC narrowly permits an ordinary administrator-
exempt merge under these existing settings after checks and coordination
acceptance; this path is disclosed here and will be reverified before merge.
No override, protection weakening or credential output occurred. Existing
Git Credential Manager supplied credentials in memory only. Immediately before
publication, remote main still matched the expected base, divergence was 0/0,
the seven staged paths matched scope, privacy/diff/final checks passed and the
branch had no prior upstream. Normal push established the matching origin
branch; unrelated files were not included.

Primary commit: `27c31ce73459286f20c71f4d0c5b606989f3346c`.
Primary [PR #12](https://github.com/DearKarl/ambiguity-is-not-conflict/pull/12)
was attached to the task and merged normally with an exact-head SHA guard as
`4c4c3c30fd455b259932749dc4bf0c992f9be9c7`.
Reverified protection/actual rights: admin/maintain/push true,
enforce_admins=false, strict required repository-contract, one required
approving review. The merge used the EC's disclosed ordinary administrator
exemption from that review requirement after both required runs succeeded;
no bypass flag, protection edit, forged review or review-as-independent claim.

Successful primary CI evidence:

- [Branch push run 35477920676](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35477920676).
- [PR run 35477935896](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35477935896).
- [Post-merge main run 35477981692](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/35477981692).

Fetched origin/main confirmed the merge. The clean worktree then created the
single closure branch `codex/pre-access-readiness-closure-2026-09-20` at that
revision. Only EC/HC are changed for closure. Their own final commit/PR/merge
and post-merge CI are self-evidencing in Git/GitHub and the final handoff;
they are deliberately not recursively inserted into this record. A failed
closure check stops publication for repair only under the existing finite
contract rule; no scientific scope or second closure is authorized.

### Deviations and negative results

Large read outputs required bounded recovery. Validation-runtime preparation
was explicitly bounded in the amended EC before installation. The first
direct pytest invocation used a nonexistent Scripts path; this pip target
places launchers in bin, and module invocation then passed. Review caught a
calibration units error: probability-scale 0.02 calibration-in-the-large was
incorrectly called an intercept tolerance; all three documents distinguish
it from log-odds recalibration parameters. No scientific negative result or
scientific success is inferred from this documentation work.

### Residual risks and recovery

Metadata contains restricted identifiers and must never be treated as public
or harmless. No private evidence, clinical record or restricted derivative is
included. Historical source statements are attributed, not freshly verified.
Recovery is the merged primary revision and named two-contract closure branch;
no published history has been rewritten. New scientific selections, software
conformance, external access/ethics/roster/capacity and all observed gates remain
unresolved at their explicitly named future boundaries.

### Next permitted boundary

Technical integration, coordination reviews, primary publication and main CI
are complete. Only validate and publish this one completion-only two-contract
closure, verify its post-merge CI, then stop and return to Advisor/Commander
for discussion of mathematics, instruments, matched deterministic comparison
and inference. No scientific work, new task, benchmark, download, annotation
or legacy job follows automatically. Gate 0 remains open; packet completeness
does not grant decision-freeze readiness, operational readiness or success.
