# TASK_BRIEF

- **Identifier:** TB-0003 — Gate 0 freeze-candidate and closure audit
- **Date and owner:** 2026-08-29; Research protocol lane with Ultra challenge,
  authorized by the Commander's continuing Gate-0 instruction
- **Evidence gate:** Gate 0 protocol development only; no scientific execution
- **Primary outcome:** Produce a requirement-by-requirement Gate-0 closure
  audit and a reviewable freeze candidate covering the unresolved clinical
  task, annotation/intervention design, estimands and numerical decision
  thresholds, statistical power, data/access record, backbone and resource
  ceilings, promotion rules, and approval sequence without representing any
  proposal as approved or empirically validated.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, the full
  canonical record under `docs/research/`, `docs/roadmap.md`, DR-0001 through
  DR-0007 with their recorded statuses, verified primary methodological papers,
  official dataset documentation, and official model cards/repositories.
- **Allowed actions:** Read-only primary-source and official-document web
  research; closed-form or deterministic design-only power and sensitivity
  calculations using no real data; parallel read-only scientific challenge;
  create `docs/research/gate0_closure_audit.md`,
  `docs/research/annotation_and_intervention_protocol.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/execution_budget_and_backbone_audit.md`,
  `docs/research/dataset_decision_candidate.md`, and
  `reports/tables/gate0_power_sensitivity.csv`; update `README.md`,
  `docs/research/README.md`, `docs/research/scope_charter.md`,
  `docs/research/research_question.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/evaluation_protocol.md`,
  `docs/research/data_governance.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/literature_matrix.md`, `docs/research/decision_log.md`,
  `docs/research/templates/dataset_decision_record.md`, `docs/roadmap.md`,
  `scripts/check_repository.py`, and `tests/test_repository_contract.py`; run
  local documentation and repository checks; commit and normally push only
  after exact-path, sensitive-content, branch, and remote-divergence review.
- **Forbidden actions:** Dataset, record, image, report, or model access or
  download; checkpoint inspection; repository cloning; credentials,
  registration, licence acceptance, or access requests; clinician contact,
  annotation, or synthetic clinical editing; implementation, training,
  inference, tuning, pilot, or confirmatory experiment; paid compute; fixing a
  clinical task, model, budget, or data route without the required Commander,
  clinical, governance, and supervisor approvals; claiming novelty,
  identifiability, feasibility, performance, clinical value, publication, or
  venue acceptance as established.
- **Exact files/data/model/compute boundary:** Only the files named above and
  this task brief may change. Public papers, documentation, model cards, and
  repository metadata may be read. No dataset row, restricted field, image,
  report, checkpoint, weight, API key, accelerator job, or scientific result is
  permitted.
- **Required outputs and evidence:** A closure matrix marking each contractual
  requirement as verified, candidate, approval-blocked, feasibility-blocked,
  or not yet specified; a blinded annotation and intervention protocol with
  construct labels, reader roles, reliability and stop rules, and an explicit
  ambiguity-identification boundary; a statistical plan with normalized
  endpoints, numerical candidate smallest effects, simultaneous intervals,
  multiplicity, power assumptions, sensitivity grid, and deterministic
  subsumption rule; a two-stage pre-access dataset decision candidate; a
  backbone/contamination/compute/annotation budget audit; and one proposed
  decision record containing precise approval questions and no execution
  authority.
- **Validation commands:** `pytest -q`; `python scripts/check_repository.py`;
  `git diff --check`; repository-wide Gate-0 terminology and status audit;
  independent blocker-only reviews of intervention validity, statistical
  design, and model/data/resource feasibility; exact changed-path and
  sensitive-content review; final branch, upstream, remote hash, divergence,
  push, and CI checks.
- **Promotion criteria:** Every numerical threshold has an explicit scale,
  rationale, sensitivity range, and decision consequence; power claims state
  all independence, clustering, multiplicity, attrition, and estimand
  assumptions; natural ambiguity is not promoted as a randomized intervention;
  report-derived labels do not define image truth; checkpoint exposure is not
  guessed away; resource figures remain ceilings or planning assumptions; all
  Commander/clinical/governance decisions remain visibly unapproved.
- **Stopping criteria:** Stop or leave the field approval-blocked if a proposed
  ambiguity intervention conflates ambiguity with information loss, if a
  numerical effect has no defensible scale, if power cannot be related to the
  declared estimand, if a model's training exposure makes the primary evidence
  circular, if official access/licence facts conflict, if clinical expertise
  is required to resolve a choice, or if any worktree/remote/sensitive-content
  anomaly appears.
- **External, costly, or irreversible boundary:** Read-only public research and
  a normal non-force Git push are the only external actions. Dataset/model
  access, agreements, requests, clinician work, compute purchase, public data
  release, or Gate-0 closure requires a later explicit authorization.
- **Permitted claim after completion:** The repository contains an
  independently challenged Gate-0 freeze candidate and identifies the exact
  remaining approvals. It does not establish Gate-0 closure, scientific
  identifiability, data/model availability, empirical feasibility, clinical
  utility, or submission readiness.
- **Completion status:** Completed as protocol on 2026-08-29. The closure
  matrix, annotation/intervention protocol, statistical plan and design-only
  power table, two-stage dataset candidate, backbone/resource audit, and
  proposed DR-0008 were produced. Independent audits exposed signed-control
  cancellation, ambiguity/information-loss conflation, and checkpoint-exposure
  blockers. No data, model, clinical workflow, implementation, or scientific
  experiment was accessed or run; Gate 0 remains open.
