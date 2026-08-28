# Ambiguity Is Not Conflict

[![Protocol status](https://img.shields.io/badge/evidence-protocol%20only-blue)](docs/research/research_contract.md)
[![Repository checks](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/workflows/quality.yml/badge.svg)](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/workflows/quality.yml)

**Identifiable cross-modal conflict estimation for calibrated selective
decisions.**

This repository is the standalone research home for a single question:

> At the atomic clinical-finding level, can a cross-modal conflict component
> respond specifically to controlled image--report incompatibility, rather
> than image ambiguity, text ambiguity, missingness, corruption, epistemic
> uncertainty, or output uncertainty, and add held-out decision value at a
> fixed review budget?

The project is currently at **protocol stage**. No core experiment has been
run, no candidate method has been promoted, and nothing here establishes
clinical benefit or deployment readiness.

## Intended Contribution

The single intended primary contribution is a formal conditional conflict
estimand and an estimator or estimation framework that can be falsified under
controlled interventions after accounting for ambiguity and information loss
within each modality. The controlled medical benchmark, probabilistic
embeddings, calibration analysis, and selective review are supporting evidence
or candidate implementations—not four parallel contribution claims.

The paper's identity is **not** “Gaussian embeddings” or any single distance.
Probabilistic embeddings, deterministic compatibility models, evidential
methods, ensembles, approximate-Bayesian methods, semantic entropy, generic
failure predictors, and conformal selection remain candidates to compare under
matched conditions.

The current [formalization audit](docs/research/estimator_formalization_audit.md)
selected no pointwise uncertainty-aware estimator: the three exact candidates
collapsed to deterministic or already published forms. The new pointwise-
estimator claim is therefore under a formal kill recommendation. The controlled
specificity estimand remains a possible measurement-framework contribution,
subject to an explicit owner-approved claim amendment and a separate novelty
assessment; Gate 0 remains open.

The [reader and MV-1 qualification audit](docs/research/reader_measurement_and_mv1_qualification_audit.md)
now supplies an exact finite-roster measurement candidate, joint polarity gate,
simulation contract, and deterministic yield audit. It recommends 150 screened
candidates per report-screen stratum because the prior 128-per-stratum plan is
fragile across the declared synthetic attrition sensitivity. This is a
proposed owner choice, not reader evidence, feasibility, or authorization.

```text
controlled image--report interventions
        -> controlled construct-specificity test
        -> held-out calibrated error risk
        -> selective or human-review value
```

## Research Objects

For image input \(x_v\), text input \(x_t\), model parameters \(\theta\), and
output \(\hat y\), the programme keeps the following objects distinct:

```math
A_v = A(x_v), \qquad
A_t = A(x_t), \qquad
M_v = M(x_v), \qquad
M_t = M(x_t), \qquad
C_{vt} = C(x_v,x_t), \qquad
U_{\mathrm{epi}} = U(\theta\mid\mathcal D), \qquad
U_{\mathrm{out}} = U(\hat y).
```

Here \(A_v,A_t\) denote within-modality ambiguity, while \(M_v,M_t\)
denote missingness or quality loss. They are not interchangeable.

Cross-modal conflict is an input relationship. Hallucination is an output
failure. Calibration failure and overconfident error are separate outcome
properties. The [problem taxonomy](docs/research/problem_taxonomy.md) defines
the permitted terminology.

## Current Decisions and Open Gates

| Item | Current status |
| --- | --- |
| Project identity | **Decided:** `Ambiguity Is Not Conflict` |
| Primary route | **Decided in principle:** controlled identification of image--report conflict before calibration or decision claims |
| Validation domain | **Primary route:** chest radiography at atomic finding level; the exact task and dataset remain Gate 0 decisions |
| Data route | **Candidate:** coupled MIMIC-CXR/JPG; clinician-reviewed controlled subset; ReXErr only as a MIMIC-derived synthetic stress test, never independent breadth |
| Representation | **Open comparison:** no probabilistic or Bayesian method is presumed superior |
| Pointwise estimator | **Blocked / kill recommended:** no TB-0006 candidate survived analytic equivalence; owners must narrow to the measurement framework or supply a new pre-data candidate |
| Submission target | **Planning decision:** NeurIPS 2027 Main Track; acceptance is not assumed |
| Contribution type | **Planning classification:** Use-Inspired if the official 2027 rules retain an applicable category |
| Core execution | **Blocked by Gate 0:** task, estimand, interventions, endpoint, smallest effect, baselines, data governance, and stopping rules must be frozen |

The current [Gate-0 closure audit](docs/research/gate0_closure_audit.md) supplies
a freeze candidate, not approval. The
[decision dossier](docs/research/gate0_decision_dossier.md) reduces the
remaining intervention, artifact, checkpoint, and staging questions to finite
owner choices. It recommends narrowing the first identified claim to
determinate-conflict specificity while natural ambiguity remains a
falsification audit. A valid ambiguity-identification route or explicit claim
narrowing, owner-approved controls, and a strict confirmatory evidence tier
remain unresolved blockers.

See the [research contract](docs/research/research_contract.md),
[roadmap](docs/roadmap.md), and [decision log](docs/research/decision_log.md)
for the authoritative state.

## Repository Map

```text
docs/research/               canonical scientific contract and protocols
docs/research/templates/     frozen-brief and evidence-record templates
docs/roadmap.md              evidence gates and 12-month submission plan
experiments/research_core/   reserved; no core experiment is implemented
configs/                     reserved for frozen experiment configurations
src/                         reserved until the protocol defines an interface
tests/                       repository-contract tests
scripts/                     lightweight validation utilities
data/                        governance-only placeholder; raw data are ignored
reports/tables/              permitted generated tables after authorization
reports/figures/             permitted generated figures after authorization
paper/                       manuscript workspace after evidence promotion
```

## Canonical Reading Order

1. [Research contract](docs/research/research_contract.md)
2. [Scope charter](docs/research/scope_charter.md)
3. [Problem taxonomy](docs/research/problem_taxonomy.md)
4. [Research question and hypotheses](docs/research/research_question.md)
5. [Atomic task and estimand packet](docs/research/task_estimand_options.md)
6. [Measurement protocol](docs/research/measurement_protocol.md)
7. [Annotation and intervention protocol](docs/research/annotation_and_intervention_protocol.md)
8. [Intervention option audit](docs/research/intervention_option_audit.md)
9. [Reader measurement and MV-1 qualification audit](docs/research/reader_measurement_and_mv1_qualification_audit.md)
10. [Statistical analysis plan](docs/research/statistical_analysis_plan.md)
11. [Evaluation protocol](docs/research/evaluation_protocol.md)
12. [Data and clinical governance](docs/research/data_governance.md)
13. [Dataset feasibility audit](docs/research/dataset_feasibility_audit.md)
14. [Dataset decision candidate](docs/research/dataset_decision_candidate.md)
15. [Backbone and resource audit](docs/research/execution_budget_and_backbone_audit.md)
16. [Estimator formalization audit](docs/research/estimator_formalization_audit.md)
17. [Baseline and ablation matrix](docs/research/baselines_and_ablations.md)
18. [Literature matrix](docs/research/literature_matrix.md)
19. [Novelty audit](docs/research/novelty_audit.md)
20. [Submission strategy](docs/research/submission_strategy.md)
21. [Gate-0 decision dossier](docs/research/gate0_decision_dossier.md)
22. [Gate-0 closure audit](docs/research/gate0_closure_audit.md)
23. [Decision log](docs/research/decision_log.md)

## Repository Checks

The initial repository contains governance tests, not scientific tests:

```bash
python -m pip install -r requirements-dev.txt
pytest -q
python scripts/check_repository.py
```

These checks verify structure and internal documentation links. They do not
validate a scientific claim.

## Data, Privacy, and Clinical Boundary

No restricted medical data, credentials, identifiers, personal
correspondence, or private supervisor messages may be committed. Dataset
access, synthetic clinical contradictions, clinician annotation, and human
studies each require their own approval and decision record. See
[data/README.md](data/README.md).

## Citation and Reuse

The repository has a machine-readable [citation record](CITATION.cff), but it
does not yet represent a published paper or released scientific result. No
open-source licence has been selected; see
[the licensing status](docs/licensing.md) before reusing material.
