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

## Handoff record `HC-2026-09-01-001`

### Identity and status

- Linked Execution Contract: `EC-2026-09-01-001`
- Task: adopt and formalize `G0-METHOD A`, freeze its Commander-level primary
  instrument and matched deterministic comparator interfaces, and keep Gate 0
  scientifically honest
- Status: `COMPLETE`
- Prepared by: Codex, Ultra scientific-decision task
- Handoff date: 2026-09-01 (Asia/Shanghai)

### Outcome

The Commander approved Method A as the sole project route and resolved the
instrument/comparator design decision. The bounded repository reconciliation,
independent reviews, local validation, protected pull request, primary merge,
and post-merge `main` verification are complete. No scientific execution is
included.

### Changed boundary

- The delivered durable boundary is one Method-A formalization document, one
  dated decision record, directly implicated canonical status/method/venue
  wording, the active contracts, and generic contract/semantic guard tests.
- The exact 23 paths are:
  `EXECUTION_CONTRACT.md`, `HANDOFF_CONTRACT.md`, `README.md`,
  `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/decision_log.md`,
  `docs/research/estimator_formalization_audit.md`,
  `docs/research/evaluation_protocol.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/literature_matrix.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/novelty_audit.md`,
  `docs/research/research_contract.md`,
  `docs/research/research_question.md`,
  `docs/research/scope_charter.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/submission_strategy.md`,
  `docs/research/task_briefs/TB-0006-estimator-formalization-audit.md`,
  `docs/research/task_estimand_options.md`, and
  `tests/test_repository_contract.py`.
- Deliberately excluded are personal correspondence, data, models, code for the
  scientific method, simulations, annotations, experiments, results, and
  GitHub-setting changes.
- The completion-only closure changes exactly `EXECUTION_CONTRACT.md` and this
  `HANDOFF_CONTRACT.md`; it makes no scientific-document change.

### Facts

- TB-0006 analytically killed all three proposed new pointwise-estimator
  claims; those kills are unchanged.
- `psi_mag` is a population functional of a prospectively frozen score, not a
  deployable pair-level conflict score.
- Official ProbVLM paper and code semantics are not identical; the Commander
  selected a paper-faithful project-native interface rather than code-exact
  behavior.
- `POINT-INFONCE` adds contrastive-negative assumptions and therefore cannot
  serve as the primary mean-only ablation of the probabilistic adapter.

### Decisions recorded

- `G0-METHOD A` is Commander-approved as the project's only active route;
  `G0-METHOD B` is not an active parallel route.
- The non-novel primary instrument is paper-faithful, project-native
  `PROBVLM-2ADAPTER`, scored by symmetric cross-modal generalized-Gaussian
  negative log-likelihood.
- The primary matched deterministic comparator is
  `POINT-2ADAPTER-RECON`, sharing inputs, independently verified determinate-
  compatible fitting records, mean trunks, GGD score family, prediction
  topology, optimization, and tuning budget while removing input-dependent
  scale and shape outputs. It uses global coordinatewise scale/shape constants
  fitted on the same compatible fit/development objective and frozen before
  protected outcomes; unit-scale Laplace is a sensitivity only.
- Compatible fitting-set membership is disclosed shared semantic selection
  supervision; semantic labels are neither model inputs nor loss targets.
  Removing heads changes active parameters and gradient paths, so the primary
  comparison is a same-selection-information full-route test, not a capacity-
  isolated mechanism test.
- `POINT-INFONCE` is a secondary contrastive baseline with a separately frozen
  multi-positive and false-negative policy.

### Assumptions and unresolved items

- Scientific-supervisor, statistical-owner, and model-owner co-approval of the
  Method-A package remains open.
- Gate 0 remains open; exact task, data/access, intervention acceptance,
  backbone, executable architecture, software, numerical hyperparameters,
  calibration, readers, resources, and governance remain unresolved.
- Framework-level novelty and NeurIPS 2027 Main Track fit remain hypotheses,
  not established facts or publication promises.
- `A_psi` is a difference between method-specifically standardized
  dimensionless effects, not a contrast in one shared reference-SD unit.

### Validation and review evidence

- Contract traversal is complete, including the Commander-authorized
  comparator amendment.
- Independent pre-edit theory, method-equivalence, and governance audits
  supplied the formal claim boundary and identified the corrected comparator.
- Final scientific-identification review: PASS. It verified the GGD formula,
  partial construct, package-effect/semantic-isolation distinction, fitted
  global comparator constants, method-specific `A_psi`, componentwise max-`t`
  inference, hard kill, and non-executable Gate-0 boundary.
- Final instrument/comparator review: PASS. It verified shared selection-
  information disclosure, fitted/frozen global constants, capacity and
  gradient-path differences, the direct-score-only frozen-means diagnostic,
  `POINT-INFONCE` demotion, and licence/checkpoint boundaries.
- Final governance review: PASS. It verified the exact authorized 23-path set,
  Commander/other-owner separation, Scope-A veto-only language, hard current-
  route kill, open Gate 0, and absence of execution/publication promises.
- `pytest -q`: PASS, `51 passed`.
- `python scripts/check_repository.py`: PASS, `Repository contract: OK`.
- `git diff --check`: PASS.
- Tracked/untracked size and sensitive-content review: PASS; no path above 5 MB,
  restricted record, credential, personal correspondence, or private screenshot
  is present.
- Primary branch CI, pull-request CI, and post-merge `main` CI all passed; their
  immutable run links are recorded below.

### Git and external evidence

- Base revision:
  `74e6591dfe43d98dad06df2b262f8c4295455421`
- Working branch: `codex/g0-method-a-formalization`
- Remote: `https://github.com/DearKarl/ambiguity-is-not-conflict.git`
- Read-only fetches reconfirmed the exact remote and `0/0` divergence before
  substantive edits and again after final review; no remote branch of this name
  existed at the final local check.
- Primary commit:
  `0eb8652139c9b4e13e3c245425518e3ff6900742`.
- Remote primary branch: `origin/codex/g0-method-a-formalization`, verified at
  the exact primary commit with `0/0` divergence after push.
- Primary pull request: [#4](https://github.com/DearKarl/ambiguity-is-not-conflict/pull/4).
- Branch-push CI: [green run 33467376261](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467376261).
- Pull-request CI: [green run 33467410010](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467410010).
- Merge revision:
  `fa730efef8cd2bcf416d34282bbd97ee2bb4461b`.
- Post-merge `main` CI: [green run 33467488625](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33467488625).
- GitHub required one review, but the repository had no eligible independent
  collaborator. The disclosed standard administrator exemption was used
  without changing branch protection, passing an explicit override flag, force
  pushing, or deleting the branch.

### Deviations and negative results

- The initial proposed `PROBVLM-2ADAPTER` versus `POINT-INFONCE` primary pair
  failed independent same-information challenge because InfoNCE introduces a
  distinct contrastive-negative mechanism. No invalid freeze was committed or
  pushed.
- The Commander explicitly approved the corrected mean-only reconstruction
  comparator before substantive work resumed.
- Initial post-edit reviews blocked capacity-parity wording, hidden fit-set
  selection supervision, unit-Laplace comparator weakness, overbroad semantic-
  identification language, common-SD `A_psi` wording, and softened hard-kill
  wording. Each blocker was corrected without changing an estimand, threshold,
  owner status, route, or execution authority; the final re-reviews passed.
- No scientific hypothesis has been tested and no scientific result exists.
- The private supervisor email draft was delivered only to the Commander and
  was not persisted in the repository.

### Residual risks and recovery

- The framework identifies an intervention-relative population response of a
  frozen score under explicit assumptions; it does not identify semantic
  conflict for an arbitrary pair from model outputs alone.
- A simpler deterministic instrument may subsume the probabilistic instrument;
  that outcome kills the current Main Track route and must be reported rather
  than hidden or post-hoc repackaged.
- The required frozen-means diagnostic can support only a direct score-path
  attribution conditional on jointly trained means, not a training-path or
  causal mechanism.
- All repository changes remain recoverable through ordinary Git operations;
  no destructive or force operation is authorized.
- GitHub Actions emitted a non-blocking Node.js-20 deprecation annotation for
  the pinned checkout/setup actions while running them on Node.js 24. Every
  required job still passed; dependency-pin maintenance is a separate future
  governance task, not part of this scientific closure.

### Next permitted boundary

This bounded task is closed. The next scientific task requires a new execution
contract and is owner reconciliation of the remaining Gate-0 decisions,
starting with scientific-supervisor/statistical/model-owner review of the
Method-A package and the still-open task, data, reader, model, resource, and
governance choices. No experiment follows automatically.
