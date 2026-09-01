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

- Contract ID: `EC-2026-09-01-001`
- Task: adopt and formalize `G0-METHOD A`, specify its primary instrument and
  same-information comparator, and prepare a private supervisor email draft
- Status: `COMPLETE`
- Authorized by: Commander, in the current Codex task on 2026-09-01
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/g0-method-a-formalization`
- Expected base: remote `main` at
  `74e6591dfe43d98dad06df2b262f8c4295455421`

### Primary outcome

Record the Commander's selection of `G0-METHOD A` as the project's single
primary method identity; formalize the intervention-identified population
measurement and inference framework without claiming a new pair-level conflict
score; and prospectively specify exactly one non-novel primary pointwise
instrument plus one same-information deterministic comparator. Keep every
remaining owner approval and Gate-0 execution blocker explicit. Prepare one
private bilingual-ready supervisor email draft for the Commander, but do not
send or persist that correspondence in the public repository.

### Authoritative inputs

Read these sources in full before substantive work:

- `AGENTS.md`
- `CODEX_TASK_GOVERNANCE.md`
- this active `EXECUTION_CONTRACT.md`
- `HANDOFF_CONTRACT.md`
- `README.md`
- `docs/roadmap.md`
- `docs/research/README.md`
- `docs/research/research_contract.md`
- `docs/research/scope_charter.md`
- `docs/research/research_question.md`
- `docs/research/measurement_protocol.md`
- `docs/research/statistical_analysis_plan.md`
- `docs/research/estimator_formalization_audit.md`
- `docs/research/baselines_and_ablations.md`
- `docs/research/novelty_audit.md`
- `docs/research/literature_matrix.md`
- `docs/research/submission_strategy.md`
- `docs/research/gate0_closure_audit.md`
- `docs/research/gate0_decision_dossier.md`
- `docs/research/decision_log.md`
- `docs/research/task_briefs/TB-0006-estimator-formalization-audit.md`
- `scripts/check_repository.py`
- `tests/test_repository_contract.py`
- the Commander's current authorization, the verified Git/GitHub state, and
  the official NeurIPS 2026 contribution-type/review guidance used only as a
  time-sensitive planning reference while the 2027 call remains unpublished

### Frozen interpretations for this task

- The Commander approves `G0-METHOD A`; the scientific supervisor,
  statistical owner, and model owner have not yet approved it.
- `G0-SCOPE A` remains unchanged: determinate-conflict specificity is primary
  and natural ambiguity is veto-only; supervisor co-approval remains open.
- The three TB-0006 pointwise method claims remain killed. No empirical result
  may reverse their analytic equivalence or occupied-form findings.
- `psi_mag` is a population specificity estimand for an already frozen score,
  not a deployable pair-level conflict score.
- The central contribution may be a domain-general identification,
  measurement, and inference framework, but its novelty and NeurIPS Main Track
  fit remain hypotheses to audit rather than established facts.
- The Commander has now resolved the instrument/comparator stop condition.
  The Commander-level scientific-interface choice is a paper-faithful,
  project-native `PROBVLM-2ADAPTER` instrument scored by symmetric cross-modal
  generalized-Gaussian negative log-likelihood, paired with a new
  `POINT-2ADAPTER-RECON` deterministic comparator that shares the frozen
  inputs, independently verified determinate-compatible fitting records, mean
  trunks, prediction topology,
  optimization, and tuning budget while removing scale and shape outputs.
  Compatibility-set membership is independently measured shared selection
  supervision for both routes, even though semantic labels are not model
  inputs. The point comparator uses prospectively fitted, frozen global
  coordinatewise GGD scale/shape constants; unit constants are sensitivity
  only.
  `POINT-INFONCE` is secondary and must receive a separately frozen
  multi-positive/false-negative policy. Scientific-supervisor, statistical-
  owner, and model-owner co-approval remains open; this is not an execution-
  ready implementation freeze. Removing the probabilistic heads also removes
  active parameters and gradient paths, so this is a same-information full-
  route comparison, not a capacity-isolated scale/shape mechanism test. Exact
  parameter counts must be reported rather than described as equal.
- Gate 0 remains open. This task creates no scientific evidence and authorizes
  no implementation, model, data, reader, simulation, pilot, or experiment.
- The Commander's local workstation remains unavailable for TB-0011's
  approximately 613-GB conditional simulation-output core floor. That floor is
  not the medical dataset size, a final upper bound, or an execution target for
  this task.

### Allowed actions

- replace this Execution Contract from the Commander's explicit authority,
  then complete and record the required traversal before any other mutation;
- create a new linked Handoff Contract for this bounded task;
- add one canonical English framework-formalization document under
  `docs/research/` and update only directly implicated status, decision,
  contribution, method, instrument/comparator, and cross-reference wording in
  `README.md`, `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/research_contract.md`, `docs/research/scope_charter.md`,
  `docs/research/research_question.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/evaluation_protocol.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/task_estimand_options.md`,
  `docs/research/estimator_formalization_audit.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/novelty_audit.md`,
  `docs/research/literature_matrix.md`,
  `docs/research/submission_strategy.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/decision_log.md`, and the TB-0006 completion record;
- update only `tests/test_repository_contract.py` where the prior test suite
  hard-codes the completed contract's single-use remediation ID or stale open-
  method wording, preserving the generic lifecycle semantics and all
  scientific-number checks; do not change the repository checker unless an
  independently reviewed deterministic defect forces a contract amendment;
- record a new dated Decision Record that separates Commander approval from
  all still-open supervisor/statistical/model-owner approvals;
- replace `POINT-INFONCE` as the primary matched comparator with the approved
  `POINT-2ADAPTER-RECON` interface, retain `POINT-INFONCE` only as a secondary
  contrastive baseline, and record the exact reason for that demotion;
- derive propositions, counterexamples, estimands, estimators, assumptions,
  inference obligations, falsification rules, and permitted claims from the
  authoritative record without changing saved numerical decisions;
- conduct targeted read-only verification of already named primary papers,
  official code pages, licences, and official NeurIPS guidance when required
  for novelty, semantic-interface, or venue-fit accuracy; do not clone, install,
  download, execute, or persist third-party code, data, or models;
- draft a private supervisor email in the final user response only; do not send
  it, create an email file, or commit personal correspondence;
- run read-only audits and the existing deterministic repository checks;
- obtain independent scientific, method-equivalence, and governance review;
- commit and push the bounded branch, open a pull request, wait for green CI,
  and merge only through the standard protected-branch path after independent
  review. If GitHub still has only one collaborator, a normal disclosed
  administrator-exempt merge without an override flag is allowed; protection
  may not be weakened;
- after the primary merge and CI, create one completion-only closure change
  that modifies only the two contracts, synchronize it through one final PR,
  and report its self-evidencing GitHub result.

### Forbidden actions

- no medical-data, model-weight, repository-clone, executable-code, or large-
  artifact download;
- no core implementation, environment installation, model execution,
  training, tuning, annotation, simulation, pilot, or experiment;
- no new pointwise estimator claim, relabelling of `psi_mag`, reversal of the
  TB-0006 kills, full causal ambiguity-separation claim, or Gate-0 closure;
- no change to the task, dataset route, intervention, hypotheses, estimand
  values, SESOIs, bootstrap counts/seeds, sample floors, resource counts,
  promotion/stop rules, or clinical claim;
- no representation of Commander approval as scientific-supervisor,
  statistical-owner, model-owner, governance-owner, or clinical-owner approval;
- no promise of NeurIPS eligibility, acceptance, publication, clinical value,
  or deployment readiness;
- no sending email or other external communication and no commit of personal
  correspondence, restricted data, credentials, identifiers, or private
  screenshots;
- no GitHub settings, label, issue, release, tag, branch-protection, or main-
  branch change except the normal PR/merge lifecycle explicitly authorized
  above;
- no force push, history rewrite, explicit protection override, branch
  deletion, destructive action, unrelated edit, or scope expansion.

### Preconditions

- the dedicated worktree is clean and based exactly on the expected remote
  `main` revision;
- the configured remote is exactly
  `https://github.com/DearKarl/ambiguity-is-not-conflict.git`;
- remote divergence is zero and no unrelated user changes are present;
- the working branch is dedicated to this contract;
- the completed traversal is recorded before any mutation beyond this file;
- the approved Commander-level interface must remain distinct from the later
  owner-approved executable specification, which still requires exact
  software, optimizer values, tuning grid, calibration, and data/model
  decisions.

### Promotion criteria

The primary task may enter remote finalization only when all of the following
hold:

1. the completed traversal is recorded and the new Handoff Contract is linked;
2. a dated decision record states that the Commander selected `G0-METHOD A`
   while every other required owner approval remains open;
3. one canonical document defines the construct support, pointwise instrument,
   controlled contrasts, `psi_mag` estimand and estimator, identification and
   non-identification results, assumptions, inference boundary, falsification
   rules, and permitted claim without mathematical contradiction;
4. exactly one explicitly non-novel primary instrument and one same-information
   deterministic comparator are prospectively specified, with score/link,
   inputs, supervision, information budget, and unresolved implementation or
   licence boundaries explicit;
5. the repository makes no new pair-level estimator claim, no full ambiguity-
   separation claim, no experiment claim, and no publication promise;
6. directly implicated canonical documents agree on the Method-A paper
   identity, Gate-0 status, owner status, instrument/comparator role, and exact
   next boundary;
7. a focused novelty audit distinguishes source facts from project inferences
   and either finds a defensible surviving framework-level gap or records the
   exact kill condition without manufacturing novelty;
8. independent reviews find no semantic drift, hidden second route,
   same-information mismatch, unlicensed implementation promise, restricted
   content, or scope expansion;
9. `pytest -q`, `python scripts/check_repository.py --final`, and
   `git diff --check` pass, and the staged-file/sensitive-content review is
   clean;
10. the primary PR and post-merge `main` CI are green under the protected-branch
    lifecycle, after which the two-contract completion-only closure is also
    verified and synchronized.

### Stopping criteria

Stop and report rather than expanding scope if any of these occurs:

- the checkout is dirty, the expected base or remote changes, remote divergence
  appears, or unrelated user work cannot be isolated;
- the framework-level novelty question requires an unbounded literature review
  or the complete contribution is clearly occupied;
- the approved `PROBVLM-2ADAPTER`/`POINT-2ADAPTER-RECON` interface cannot be
  stated as same-information without disclosing its fit-set supervision,
  score-family difference, target topology, active-capacity difference, or
  training-path boundary;
- a requested specification would reverse an analytic kill, invent a cosmetic
  estimator distinction, change a frozen scientific quantity, or require data,
  model, reader, code execution, or experiment access;
- another required owner decision is scientifically necessary to choose among
  materially different interfaces; record the exact question instead of
  choosing;
- independent review raises an unresolved blocker or any required check fails;
- GitHub authentication, protection, base freshness, or merge state is
  unexpected;
- the task requires destructive, costly, communicative, or otherwise unlisted
  external action.

### Irreversible and external boundaries

Targeted read-only official-source inspection, ordinary commits, pushing the
dedicated branch, pull requests, standard protected merges under the disclosed
solo-administrator residual, and CI are authorized external actions. They must
remain auditable and reversible through ordinary Git/GitHub operations. Email
sending, third-party downloads or execution, data/model access, GitHub-setting
changes, explicit protection overrides, force operations, history rewriting,
releases, and publication are outside authority.

### Required evidence

- pre- and post-change Git status, branch, remote, base, upstream, and divergence
  checks;
- completed traversal record and exact changed-file list;
- a concise authority decision and scientific root-cause record;
- formal definitions and derivations with explicit fact/inference/assumption/
  decision separation;
- targeted primary-source verification notes where used;
- independent scientific, method-equivalence, and governance review results;
- full test, final repository-checker, diff, staged-file, sensitive-content,
  and tracked-size results;
- commit, pull-request, CI, merge, post-merge, and completion-only closure
  evidence;
- a completed linked `HANDOFF_CONTRACT.md` and the private, unsent supervisor
  email draft delivered only to the Commander.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Agent: Codex, Ultra scientific-decision task
- Started: 2026-09-01 (Asia/Shanghai)
- Completed: 2026-09-01 (Asia/Shanghai), including the Commander-authorized
  comparator amendment.
- Preconditions verified: yes; the dedicated worktree is clean at
  `74e6591dfe43d98dad06df2b262f8c4295455421`, the remote URL is exact, remote
  divergence is `0/0`, and this one-file replacement is the sole repository
  mutation before traversal.
- Amendment authority: on 2026-09-01 the Commander explicitly approved the
  paper-faithful `PROBVLM-2ADAPTER` instrument, the new matched
  `POINT-2ADAPTER-RECON` comparator, and the demotion of `POINT-INFONCE` to a
  secondary baseline while keeping all other-owner approvals and Gate 0 open.
- Notes: before the amendment, this contract, `AGENTS.md`,
  `CODEX_TASK_GOVERNANCE.md`, the prior Handoff Contract, every named
  repository input, and the official NeurIPS 2026 planning guidance were
  traversed in full. After the Commander's comparator decision, the amended
  contract was re-read in full together with the governing rules and directly
  implicated method, baseline, inference, novelty, Gate-0, decision, checker,
  and test sources. A read-only fetch reconfirmed the exact remote, base, and
  `0/0` divergence. No file other than this contract was mutated before the
  amendment traversal returned to `COMPLETE`. Substantive work may now resume
  only within `EC-2026-09-01-001`. A post-edit equivalence review then required
  three non-expansive precision corrections: disclose active-capacity and
  gradient-path differences rather than assert parity, count independently verified compatible-set
  membership as shared selection supervision, and restrict the fixed-means
  ablation to the direct score path conditional on jointly trained means. The
  contract and directly implicated method/baseline/inference sources were
  re-read after this amendment. The governance cross-document review then
  required two additional directly implicated wording repairs in
  `evaluation_protocol.md` and `task_estimand_options.md`: identify only the
  intervention-relative score-response functional, and preserve the existing
  hard current-route Main Track kill without the stale estimator-novelty label.
  The Commander had approved the ensuing bounded reconciliation; both files and
  this amended contract were read in full before those repairs. No scientific
  quantity, stop rule, or owner status changed.

### Completion evidence

- Primary commit:
  `0eb8652139c9b4e13e3c245425518e3ff6900742` on
  `codex/g0-method-a-formalization`.
- Primary pull request: [#4](https://github.com/DearKarl/ambiguity-is-not-conflict/pull/4),
  merged through the standard solo-administrator exemption without changing
  protection settings, using an explicit override flag, or deleting a branch.
- Primary branch and pull-request checks passed:
  [run 33467376261](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467376261)
  and [run 33467410010](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467410010).
- Primary merge revision:
  `fa730efef8cd2bcf416d34282bbd97ee2bb4461b`.
- Post-merge `main` verification passed in
  [run 33467488625](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467488625).
- The final local primary boundary passed 51 tests, final repository-contract
  validation against the then-current `origin/main`, diff validation,
  independent scientific/instrument/governance review, sensitive-content
  review, and size review.
- This completion-only closure changes exactly `EXECUTION_CONTRACT.md` and
  `HANDOFF_CONTRACT.md`. Its commit, pull request, merge revision, and final
  post-merge check identify themselves through immutable Git/GitHub history.
- No data, model, simulation, annotation, implementation, experiment, private
  correspondence, or large artifact was created or accessed under this task.
