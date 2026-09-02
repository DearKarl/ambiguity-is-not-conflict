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

- Contract ID: `EC-2026-09-02-002`
- Task: reconcile the Commander's consolidated internal-owner approval, audit
  Gate-0 closure, and prepare the restricted-data readiness packet
- Status: `COMPLETE`
- Authorized by: Commander, in the current Codex task on 2026-09-02
- Linked Handoff Contract: `HC-2026-09-02-002`
- Linked Task Brief: `TB-0012`
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/gate0-data-preparation`
- Expected base: remote `main` at
  `d4ba3fa586be4881a74bee2ab5aa2493544a3414`

### Primary outcome

Record the Commander's statement that they are the consolidated accountable
internal owner and approve continued experimental preparation. Map that
authority onto every finite Gate-0 choice without fabricating external facts;
freeze only choices that are already exact and unambiguous; create one
canonical restricted-data decision/readiness record and a bounded Stage-A task
brief; and determine whether Gate 0 can close.

If any required access, training, DUA, ethics, secure-path, reader-qualification,
retention, infrastructure, capacity, or licence fact is not objectively
verifiable, Gate 0 remains open and the task must end with the exact finite
evidence or Commander input needed. This contract prepares dataset acquisition
but does not access, inspect, query, or download restricted data.

### Authority interpretation

#### Facts

- The Commander states that all internal approvals have been obtained, that the
  Commander is the accountable owner for all internal project roles, and that
  the project may proceed toward experiments and dataset preparation.
- The canonical dossier contains finite recommendations but still distinguishes
  internal decisions from external access, institutional, clinical-reader,
  licence, storage, and capacity facts.
- MIMIC-CXR and MIMIC-CXR-JPG are restricted-access resources. Their raw or
  record-level derivatives must not enter Git, GitHub, CI, Codex messages, or
  an unapproved service.
- Gate 0 was open at the expected base.

#### Decision

- Treat the Commander's statement as consolidated approval for internal choices
  only where the existing canonical record already defines one exact choice and
  no new scientific/statistical choice is required.
- Do not treat self-designation as proof of external credentialing, completed
  human-subjects training, an accepted DUA, ethics determination, clinical
  reader qualification, secure storage, infrastructure capacity, licence
  permission, or institutional retention terms.
- Do not infer approval of a conditional recommendation whose prerequisite is
  unverified, or select among A/B/C alternatives not resolved by the statement.
- Gate 0 closes only if all seven Execution Gate categories are exact,
  internally approved, and externally feasible under documented evidence.

#### Assumptions

- The Commander's report accurately represents the project's internal authority
  structure.
- No unreported external condition contradicts the approval.
- Any restricted-data execution will occur only in an approved environment
  outside Git and without transmitting record-level content to Codex.

### Authoritative inputs

Read in full before substantive work:

- `AGENTS.md`
- `CODEX_TASK_GOVERNANCE.md`
- this `EXECUTION_CONTRACT.md`
- `HANDOFF_CONTRACT.md`
- `README.md`
- `docs/roadmap.md`
- `docs/research/README.md`
- `docs/research/research_contract.md`
- `docs/research/research_question.md`
- `docs/research/scope_charter.md`
- `docs/research/problem_taxonomy.md`
- `docs/research/task_estimand_options.md`
- `docs/research/annotation_and_intervention_protocol.md`
- `docs/research/measurement_protocol.md`
- `docs/research/statistical_analysis_plan.md`
- `docs/research/method_a_identification_framework.md`
- `docs/research/baselines_and_ablations.md`
- `docs/research/execution_budget_and_backbone_audit.md`
- `docs/research/data_governance.md`
- `docs/research/dataset_decision_candidate.md`
- `docs/research/dataset_feasibility_audit.md`
- `docs/research/gate0_closure_audit.md`
- `docs/research/gate0_decision_dossier.md`
- `docs/research/decision_log.md`
- `docs/research/submission_strategy.md`
- `data/README.md`
- `docs/research/templates/task_brief.md`
- `docs/research/templates/dataset_decision_record.md`
- `scripts/check_repository.py`
- `tests/test_repository_contract.py`
- the Commander's current statement; no private approval correspondence,
  credential, training certificate, DUA document, or screenshot may be stored

After the repository traversal is complete, verify the current official
PhysioNet resource pages and MIMIC-CXR/MIMIC-CXR-JPG data-use/access
documentation as the first authorized evidence action, limited to public
non-record-level sources. This sequencing avoids treating an external web
request as part of the pre-traversal repository read.

### Allowed actions after traversal

- replace the completed Handoff Contract with `HC-2026-09-02-002`;
- add `DR-0018` to `docs/research/decision_log.md`, separating the
  consolidated internal-owner decision from unverified external facts;
- create `docs/research/dataset_decision_record.md` and
  `docs/research/task_briefs/TB-0012-gate0-owner-consolidation-data-readiness.md`;
- reconcile directly implicated status and next-boundary wording in
  `README.md`, `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/research_contract.md`,
  `docs/research/research_question.md`,
  `docs/research/scope_charter.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/data_governance.md`,
  `docs/research/dataset_decision_candidate.md`,
  `docs/research/dataset_feasibility_audit.md`,
  `docs/research/submission_strategy.md`, and `data/README.md`;
- update `tests/test_repository_contract.py` only for exact new contract,
  decision, Gate-0, and data-boundary invariants; do not weaken generic tests;
- verify current public official resource/access documentation without logging
  in, accepting terms, or accessing record-level content;
- inspect only repository structure and non-sensitive local path availability;
  do not search credential stores, browser sessions, private documents, or
  broad home-directory data;
- obtain independent scientific/governance and data-security review;
- run deterministic repository checks;
- synchronize the bounded documentation/test change through the standard
  branch/PR/CI lifecycle, including the finite two-contract closure. A
  disclosed normal administrator-exempt merge without an explicit override
  flag is allowed only if the existing single-collaborator condition persists.

### Exact file, data, model, and compute boundary

- Primary repository mutation is limited to:
  `EXECUTION_CONTRACT.md`, `HANDOFF_CONTRACT.md`, `README.md`,
  `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/research_contract.md`,
  `docs/research/research_question.md`,
  `docs/research/scope_charter.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/decision_log.md`, `docs/research/data_governance.md`,
  `docs/research/dataset_decision_candidate.md`,
  `docs/research/dataset_feasibility_audit.md`,
  `docs/research/submission_strategy.md`,
  `docs/research/dataset_decision_record.md`,
  `docs/research/task_briefs/TB-0012-gate0-owner-consolidation-data-readiness.md`,
  `data/README.md`, and `tests/test_repository_contract.py`.
- No medical data directory, record-level manifest, subject/study/image ID,
  report, image, annotation, embedding, checkpoint, model weight, credential,
  token, certificate, DUA file, private screenshot, or personal correspondence
  may be read, written, logged, staged, or committed.
- No dataset or model download, no API/login session, no PhysioNet credential
  use, no query, and no clinical record inspection.
- No GPU, paid/cloud compute, scientific simulation, model execution, training,
  tuning, annotation, or experiment.
- Only small text/test artifacts and ordinary local CPU checks are allowed.

### Forbidden actions

- no claim that consolidated internal authority proves external access,
  expertise, independence, ethics, security, capacity, or licensing;
- no Gate-0 closure while any required fact or exact choice remains unresolved;
- no silent adoption of every recommended A row when prerequisites or finite
  alternatives remain open;
- no restricted or patient-level data action, credential handling, dataset/model
  download, reader contact, annotation, intervention generation, model use, or
  experiment;
- no weakening of patient-level split, one-source-block-per-patient, independent
  image truth, natural-ambiguity veto, multiplicity, SESOI, kill, retention, or
  disclosure boundaries;
- no scientific estimand, hypothesis, endpoint, threshold, sample floor, seed,
  method role, data route, or publication-claim change;
- no force push, history rewrite, branch deletion, explicit protection
  override, GitHub-setting change, issue, release, tag, or destructive action.

### Preconditions

- dedicated worktree clean at the exact expected base;
- remote exactly
  `https://github.com/DearKarl/ambiguity-is-not-conflict.git`;
- dedicated branch absent remotely before first push and divergence `0/0`;
- only this contract changes before traversal completes;
- existing canonical choices can be audited without restricted data.

### Promotion criteria

The primary change may enter remote finalization only when:

1. traversal and `HC-2026-09-02-002` are complete;
2. DR-0018 records the exact scope and limits of consolidated internal approval;
3. every Gate-0 row is classified as internally approved, externally verified,
   conditionally blocked, or still choice-blocked, with no inflated closure;
4. the dataset decision record names the exact resource/version, prediction and
   leakage units, approved/unknown access facts, secure boundary, prohibited
   exports, partition rule, cohort stop rules, reader/label boundary, retention,
   and next Stage-B evidence;
5. TB-0012 authorizes only this Stage-A reconciliation and does not authorize
   restricted-data access;
6. Gate 0 is either closed with complete evidence or explicitly remains open
   with a finite blocker list; no ambiguous partial closure;
7. independent reviews find no approval inflation, privacy/security defect,
   scientific drift, hidden execution authority, or restricted content;
8. `pytest -q`, `python scripts/check_repository.py --final`, and
   `git diff --check` pass; exact path, size, binary, untracked, and sensitive-
   content scans are clean;
9. branch, PR, and post-merge `main` CI pass before finite contract closure.

### Stopping criteria

Stop before commit/push or restricted-data action if:

- base, remote, branch, divergence, worktree, or file boundary is unexpected;
- the Commander's statement cannot choose a specific finite alternative without
  adding a new assumption;
- any external access/security/ethics/reader/licence/capacity fact is missing or
  contradictory;
- a restricted identifier, credential, private document, medical record, large
  artifact, or unrelated user change appears;
- a new scientific decision, implementation, data query, download, or external
  account action would be required;
- tests, checker, independent review, GitHub authentication/protection, merge,
  or CI fail.

### Irreversible and external boundaries

Public official-document verification and normal GitHub synchronization are
the only authorized external actions. No login, credential use, terms
acceptance, access request, dataset/model download, record query, clinical
contact, paid compute, or experiment is authorized. A later restricted-data
action requires Gate-0 closure plus a fresh linked Execution Contract and
Stage-B Task Brief naming the approved environment and exact commands.

### Required evidence

- exact base/branch/remote/divergence and changed-file records;
- full traversal record;
- DR-0018 fact/inference/assumption/decision fields;
- complete Gate-0 owner-versus-external-fact ledger;
- canonical dataset decision record and Stage-A Task Brief;
- official-source access/term links and verification date;
- independent scientific/governance and data-security reviews;
- full local checks and sensitive/size/binary/untracked scans;
- commit, branch, PR, CI, merge, post-merge CI, and finite closure evidence;
- explicit confirmation that no restricted data, credentials, model, download,
  clinical action, annotation, experiment, or large artifact was accessed or
  created.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Agent: Codex, Ultra scientific-governance task
- Started: 2026-09-02 (Asia/Shanghai)
- Preconditions observed before contract replacement: dedicated worktree
  created from remote `main` at
  `d4ba3fa586be4881a74bee2ab5aa2493544a3414`; remote URL exact; branch
  `codex/gate0-data-preparation` absent remotely; divergence `0/0`; no
  repository mutation other than replacing this contract.
- Completed: 2026-09-02 (Asia/Shanghai).
- Completion note: read this contract, `AGENTS.md`,
  `CODEX_TASK_GOVERNANCE.md`, the prior complete Handoff Contract, and every
  named repository input above in full. Verified the expected base, remote,
  branch isolation, absent remote branch, zero divergence, and that this
  contract is the sole pre-traversal mutation. The Commander's consolidated
  authority can resolve internal-owner sign-offs, but it cannot itself prove
  external access, training/DUA, ethics, secure processing, qualified-reader,
  retention/licensing, or capacity facts. Public official-source verification
  is therefore the next authorized evidence action; no restricted data action
  is authorized.
- Scope amendment: after traversal, the bounded status-only reconciliation was
  found to require the already-read Method-A and scope documents named in the
  mutation boundary above. They were added before substantive edits; the task,
  scientific content, external boundary, and stopping rules did not change.
- Post-amendment re-traversal: `COMPLETE` on 2026-09-02 (Asia/Shanghai). The
  amended Execution Contract was reread in full, and every added mutation path
  had already been read in full during the same pre-edit traversal. Authority,
  forbidden actions, stopping criteria, external boundaries, and evidence
  requirements remain understood and unchanged.

### Completion record

- Primary commit: `ddb1f018627ca060ed3f252f8b733bfeb9860038`.
- Primary branch: `codex/gate0-data-preparation`; local/remote divergence was
  `0/0` after push.
- Primary branch CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590692077`
  (`SUCCESS`).
- Primary pull request:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/pull/8`; its PR CI was
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590757092`
  (`SUCCESS`).
- Primary merge revision: `b01c103b522b5e4c384d5d5942d8eb955f9c23d6`.
- Post-merge `main` CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33590838380`
  (`SUCCESS`).
- GitHub reported the known single-collaborator review requirement. The merge
  used the disclosed normal SHA-guarded API path without an explicit override
  flag, force operation, branch deletion, or protection change.
- Completion-only branch: `codex/gate0-data-preparation-completion`, based
  exactly on the primary merge revision. Its closure commit, PR, merge
  revision, and post-merge CI are self-identifying external evidence and are
  not recursively written into this file.
- This contract authorizes no further substantive work. After completion-state
  verification, only ordinary synchronization of this two-contract closure
  and the final user handoff may follow.
