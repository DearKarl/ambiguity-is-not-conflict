# Agent Guidelines

This repository is the working record for **Ambiguity Is Not Conflict**: a
single research route on identifiable cross-modal conflict and calibrated
selective decisions. Canonical authority lives under `docs/research/`.

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

Every execution task must use a bounded `TASK_BRIEF` derived from the canonical
protocol. Stop when the brief is incomplete or conflicts with a decision
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
- Run `pytest -q` and `python scripts/check_repository.py` before publishing.

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
history, bypass protection, or include unrelated or sensitive changes.

## Codex Role Lanes

The role boundaries and handoff artifacts for Ultra, Research, Engineering,
Coding, and Operations are defined in `CODEX_TASK_GOVERNANCE.md`.
