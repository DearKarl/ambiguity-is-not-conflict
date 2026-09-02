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

## Handoff record `HC-2026-09-02-002`

### Identity and status

- Linked Execution Contract: `EC-2026-09-02-002`
- Task: reconcile consolidated internal approvals, audit Gate-0 closure, and
  prepare the restricted-data readiness record
- Status: `COMPLETE`
- Prepared by: Codex, Ultra scientific-governance task
- Handoff date: 2026-09-02 (Asia/Shanghai)

### Outcome

The bounded reconciliation records consolidated internal approval of
`G0-SCOPE A`, Method A's sole-route/B-inactive boundary, and the previously
named canonical Method-A protocol/interface package. It internally selects
`G0-DATA A` and `G0-RETENTION A` for readiness while preserving their external
and feasibility blockers. `DDR-2026-09-02-001` and TB-0012 define the exact
non-executable pre-access boundary. Gate 0 remains open; no restricted query,
download, annotation, model execution, or experiment is included.

### Changed boundary

- The task is limited to the exact paths named in `EC-2026-09-02-002`.
- The observed 23-path change set is exactly:
  `EXECUTION_CONTRACT.md`, `HANDOFF_CONTRACT.md`, `README.md`,
  `data/README.md`, `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/data_governance.md`,
  `docs/research/dataset_decision_candidate.md`,
  `docs/research/dataset_decision_record.md`,
  `docs/research/dataset_feasibility_audit.md`,
  `docs/research/decision_log.md`, `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/research_contract.md`,
  `docs/research/research_question.md`, `docs/research/scope_charter.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/submission_strategy.md`,
  `docs/research/task_briefs/TB-0012-gate0-owner-consolidation-data-readiness.md`,
  and `tests/test_repository_contract.py`.
- The completion-only change is limited to `EXECUTION_CONTRACT.md` and
  `HANDOFF_CONTRACT.md`, based exactly on the primary merge revision.
- Scientific hypotheses, estimands, thresholds, sample floors, interventions,
  method roles, bootstrap counts/seeds, hard-kill rules, and venue boundaries
  are unchanged.
- Restricted data, credentials, identifiers, private approvals, certificates,
  DUA/ethics files, models, code environments, simulations, clinical work, and
  large artifacts are excluded.

### Facts

- The Commander states that the prior formal scope/method approvals have been
  obtained and that the Commander is the consolidated internal owner.
- Current official public PhysioNet pages classify both MIMIC resources as
  credentialed access and require individual credentials, current CITI
  training, and DUA acceptance.
- The current License/DUA 1.5.0 prohibits access sharing and requires physical/
  electronic security and current human-subjects/HIPAA training.
- PhysioNet's online-service guidance requires verifiable zero retention, no
  training, and no human review; unclear online services must not be used.
- No external access, institutional, reader, or capacity evidence was provided
  or independently verified in this task.

### Decisions recorded

- DR-0018 closes the internal `G0-SCOPE A` and Method-A sole-route co-approval
  gaps without reopening Method B or claiming a new pair-level estimator.
- The canonical Method-A protocol/interface roles are internally approved, but
  unstated executable details remain specification-blocked.
- `G0-DATA A` and `G0-RETENTION A` are internally selected for readiness only.
- Every other Gate-0 row retains its exact decision, specification, external,
  simulation, or feasibility blocker in the dossier and closure audit.
- The Stage-B metadata schema is a prospectively fixed non-executable candidate;
  it requires Gate-0 closure plus a fresh linked contract and brief.

### Assumptions and unresolved items

- The Commander's attestation accurately represents the internal authority
  structure and the approvals obtained.
- PhysioNet credential/training/DUA status, institutional ethics, secure path,
  ACL, encryption, network, backup, incident, retention/deletion, derivative
  permissions, reader qualifications/independence, licences, storage/compute,
  and cohort yield remain objective unknowns.
- `G0-RESOURCES A/B/C` remains a genuine unselected choice.
- Exact task, ontology, controls, reader package, estimand/inference freeze,
  executable model/baseline/probe/calibration details, target/shift, checkpoint
  tier, staging, downstream power, and breadth snapshot remain open as recorded.

### Validation and review evidence

- Contract traversal and post-amendment re-traversal are complete.
- Independent scientific review first returned NO-GO on eight status and
  finite-blocker inconsistencies. After reconciliation, its final focused
  review passed: all 24 Gate-0 rows map one-to-one; the baseline, `MV-1`, exact
  ablation, partition, authority, licence, and staging boundaries are
  consistent; no scientific drift or execution authority remains.
- Independent data-governance review passed. It concludes that no restricted
  tabular screening query is authorized, every Stage-B field is restricted,
  and the CheXpert/NegBio values are report-derived clinical screening
  variables rather than image truth, model targets, or public metadata.
- Independent repository-governance review passed subject to the now-completed
  TB status, Handoff readiness evidence, and two specification-language fixes.
- Deterministic local validation passed: `pytest -q` reports 53 passed;
  `python scripts/check_repository.py --final --base-ref origin/main` reports
  `Repository contract: OK`; and `git diff --check` reports no error.
- Completion-state validation on the two-contract diff passed the same 53-test,
  final-checker, and diff-check commands before the closure commit.
- The changed-path scan contains exactly the 23 authorized paths. Sensitive-
  content, binary-diff, untracked-file, and greater-than-1-MB scans found only
  the two intended new Markdown records and no restricted, credential, model,
  medical-data, or large artifact.

### Git and external evidence

- Base revision: `d4ba3fa586be4881a74bee2ab5aa2493544a3414`.
- Working branch: `codex/gate0-data-preparation`.
- Remote: `https://github.com/DearKarl/ambiguity-is-not-conflict.git`.
- Initial remote branch: absent; initial divergence: `0/0`.
- Public official-source verification was limited to the MIMIC-CXR/JPG v2.1.0
  resource pages, License/DUA 1.5.0, CITI instructions, online-service notice,
  and derived-resource guidance. No login or restricted page/file access
  occurred.
- Primary commit: `ddb1f018627ca060ed3f252f8b733bfeb9860038`.
- Primary branch CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590692077`
  (`SUCCESS`).
- Primary PR: `https://github.com/DearKarl/ambiguity-is-not-conflict/pull/8`;
  PR CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590757092`
  (`SUCCESS`).
- Primary merge revision: `b01c103b522b5e4c384d5d5942d8eb955f9c23d6`;
  post-merge `main` CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590838380`
  (`SUCCESS`).
- The merge used the disclosed normal SHA-guarded API path under the verified
  single-collaborator residual, without an explicit override flag, force
  operation, branch deletion, or protection change.
- Completion branch: `codex/gate0-data-preparation-completion`, based exactly
  on the primary merge revision. The closure commit and PR self-identify in Git
  and GitHub and are not recursively inserted here.

### Deviations and negative results

- Gate 0 did not close because consolidated internal approval cannot establish
  external access/security/ethics/reader/licence/capacity facts or supply
  missing executable specifications.
- The active Execution Contract initially used a singular heading where the
  repository checker requires the plural control phrase; it was corrected
  before validation and did not alter scope.
- An independent review identified stale breadth wording that deferred the
  identity decision beyond Gate 0; it was reconciled to freeze identity/rights/
  portability prospectively while deferring execution until promotion.
- No scientific hypothesis was tested and no empirical result was produced.

### Residual risks and recovery

- User-attested internal approval is a dated decision input, not independent
  correspondence or institutional evidence.
- Metadata contains restricted identifiers and must never be treated as public
  or harmless; logs, screenshots, exceptions, and aggregate marginals can leak
  information.
- Every documentation change is recoverable through ordinary Git. No force,
  protection change, destructive operation, or restricted artifact is allowed.

### Next permitted boundary

No further substantive work is authorized under this completed contract. A
new explicit Commander authorization and fresh linked contracts are required
for evidence collection and the remaining Gate-0 choices: exact access/
training/DUA, ethics, secure environment, readers, derivative/licence and
resource facts, plus the executable package. Only after dated Gate-0 closure
may a fresh Stage-B contract authorize the four-file restricted tabular
screening query. No experiment follows from this handoff.
