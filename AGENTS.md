# Agent Guidelines

This repository is the working record for **Ambiguity Is Not Conflict**: a
single research route on identifiable cross-modal conflict and calibrated
selective decisions. Canonical authority lives under `docs/research/`.

## Contract Supremacy

For repository operations, this is the highest local workflow rule. Platform,
system, developer, and the Commander's current explicit instructions retain
their normal precedence.

- Every new bounded repository task begins by updating
  `EXECUTION_CONTRACT.md`, reading it in full together with this file,
  `CODEX_TASK_GOVERNANCE.md`, and its named authoritative inputs, and recording
  a completed traversal. No mutation, publication, external action, or
  scientific execution may start from an informal summary alone.
- The sole pre-traversal mutation is drafting/replacing
  `EXECUTION_CONTRACT.md` from the Commander's explicit authority; only the
  read-only inspection needed to populate it may accompany that transition.
- Work only inside the active contract's authority, primary outcome, allowed
  actions, file/data/compute boundary, promotion criteria, stopping criteria,
  irreversible boundary, and required evidence. A material change requires a
  stop, contract amendment, and another full traversal before work resumes.
- Every bounded task ends by updating `HANDOFF_CONTRACT.md` with outcomes,
  changed scope, decisions, evidence, deviations, residual risks, recovery
  state, and the exact next boundary. A task is not complete before this
  contract-last record exists. Use its finite two-phase primary/closure
  workflow; never create recursive commits merely to record a commit's own
  identity.
- A `TASK_BRIEF` is still required for scientific execution and is subordinate
  to the active Execution Contract and canonical research decisions.
- Questions and discussion inside an active bounded task do not create a new
  repository task unless they materially change its objective, authority, or
  allowed boundary.

## Scientific Scope

- Treat controlled identification of cross-modal conflict relative to image
  ambiguity and text ambiguity as the first core study.
- Keep image ambiguity, text ambiguity, information loss, cross-modal conflict,
  epistemic uncertainty, output uncertainty, hallucination, calibration
  failure, and overconfident error distinct.
- Treat probabilistic embeddings, Bayesian inference, ensembles, semantic
  entropy, deterministic predictors, and conformal methods as candidates to
  compare, not predetermined winners.
- Keep chest radiography as the primary validation route unless a decision
  record changes it. Do not infer clinical benefit from retrospective evidence.
- Record null results and narrow the claim if a simpler matched baseline
  subsumes the proposed conflict component.

## Execution Gate

Do not begin core implementation, download data or models, train models, create
clinical annotations, or run confirmatory experiments until Gate 0 freezes:

1. task and prediction unit;
2. dataset, access, split, and governance;
3. intervention taxonomy and annotation protocol;
4. primary estimand, endpoint, and smallest effect of interest;
5. matched baselines and ablations;
6. compute and annotation budget;
7. promotion and stopping criteria.

Every scientific execution task must additionally use a bounded `TASK_BRIEF`
derived from the canonical protocol and linked to the active Execution
Contract. Stop when either contract is incomplete or conflicts with a decision
record.

## Evidence and Development

- Label work as literature lead, protocol, mechanism-level pilot, completed
  experiment, or promoted research evidence.
- Separate task performance, uncertainty quality, calibration, robustness, and
  decision utility.
- Use patient-level or the highest leakage-relevant split for medical data.
- Prefer proper scores, calibration diagnostics, paired intervals, repeated
  evaluation, subgroup analysis, and failure-case audits.
- Use documentation-first, reviewable changes; retain exact reproduction
  commands, versions, seeds, and numerical deltas.
- Put generated tables in `reports/tables/` and figures in `reports/figures/`.
- Run `pytest -q` and `python scripts/check_repository.py --final` before
  publishing; the checker without `--final` is only for in-progress work.

## Governance

- Never commit restricted medical data, credentials, identifiers, personal
  correspondence, visa material, protected information, or private screenshots.
- Dataset access, synthetic clinical conflict, clinician studies, and changes
  to the approved research area require their own governance gates.
- Stop before destructive, costly, external, irreversible, or scope-expanding
  actions unless an explicit bounded brief authorizes them.

## GitHub Synchronization

After an authorized bounded change passes all checks, verify remote, branch,
upstream, staged files, and remote divergence; then commit descriptively and
push unless the researcher opts out. Never force-push, rewrite published
history, explicitly override or weaken protection, or include unrelated or
sensitive changes. A normal administrator-exempt merge is permitted only when
the active Execution Contract explicitly authorizes and discloses that narrow
path.

## Codex Role Lanes

The role boundaries and handoff artifacts for Ultra, Research, Engineering,
Coding, and Operations are defined in `CODEX_TASK_GOVERNANCE.md`.
