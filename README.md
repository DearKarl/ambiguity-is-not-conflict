# Ambiguity Is Not Conflict

[![Protocol status](https://img.shields.io/badge/evidence-protocol%20only-blue)](docs/research/research_contract.md)
[![Repository checks](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/workflows/quality.yml/badge.svg)](https://github.com/DearKarl/ambiguity-is-not-conflict/actions/workflows/quality.yml)

**Intervention-identified measurement of cross-modal conflict specificity.**

This repository is the standalone research home for a single question:

> At the atomic clinical-finding level, can a frozen cross-modal score respond
> specifically to controlled image--report incompatibility rather than approved
> image/text information-loss controls, survive separate ambiguity and nuisance
> veto audits, and add held-out decision value at a fixed review budget?

The project is currently at **protocol stage**. No core experiment has been
run, no candidate method has been promoted, and nothing here establishes
clinical benefit or deployment readiness.

## Intended Contribution

The single intended primary contribution is a partial-construct,
intervention-identified measurement and inference framework that can falsify
whether a frozen cross-modal score is specific to determinate semantic
incompatibility rather than approved modality-specific information-loss
controls. The controlled medical benchmark, candidate instruments,
calibration analysis, and selective review are supporting evidence—not four
parallel contribution claims.

The paper's identity is **not** “Gaussian embeddings” or any single distance.
Probabilistic embeddings, deterministic compatibility models, evidential
methods, ensembles, approximate-Bayesian methods, semantic entropy, generic
failure predictors, and conformal selection remain candidates to compare under
matched conditions.

The [formalization audit](docs/research/estimator_formalization_audit.md)
selected no novel pointwise estimator: the three exact candidates collapsed to
deterministic or already published forms. The Commander has therefore selected
[Method A](docs/research/method_a_identification_framework.md) as the sole
route. DR-0018 records consolidated internal approval of the scope and
Method-A protocol/interface boundaries. DR-0016 freezes a non-novel paper-
faithful `PROBVLM-2ADAPTER` instrument and the mean-only
`POINT-2ADAPTER-RECON` comparator; `POINT-INFONCE` remains secondary. Exact
executable specifications and every other Gate-0 choice or external fact remain
open.

The [reader and MV-1 qualification audit](docs/research/reader_measurement_and_mv1_qualification_audit.md)
now supplies an exact finite-roster measurement candidate, joint polarity gate,
simulation contract, and deterministic yield audit. It recommends 150 screened
candidates per report-screen stratum because the prior 128-per-stratum plan is
fragile across the declared synthetic attrition sensitivity. This is a
proposed owner choice, not reader evidence, feasibility, or authorization.

The [simulation resource-feasibility audit](docs/research/simulation_resource_feasibility_audit.md)
compiles that contract into 10,847 reliability candidates and 2,438
pre-calibration `MV-1` candidates. Its exact hashes and logical-work counts
show that the design is not resource-qualified; they are not runtime,
affordability, capacity, or statistical-performance evidence.

The [non-core simulation computational design](docs/research/noncore_simulation_computational_design.md)
now specifies the stage graph, proposed audit schema, deterministic restart and
output-equivalence obligations, and a future artificial-buffer benchmark
contract. It ran no benchmark or scientific code; TB-0011 supplies the later
static registry candidate, while measured resources, named capacity, and the
`G0-RESOURCES` decision remain open.

The [simulation output and semantic-operation registry](docs/research/simulation_output_and_operation_registry.md)
now compiles 259 logical metric fields and 244 operation classes into a
1,242,518-row hashed cell/global ledger without evaluating a scientific value. Its
typed-state correction raises the conditional all-candidate core audit floor
from a superseded 572.5 GB to 613,093,770,610 bytes before unresolved
extensions. This is a static lower bound, not a storage allocation, benchmark,
runtime, feasibility result, or permission to execute the simulation.

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
| Primary route | **Decided in principle:** identification of an intervention-relative frozen-score response within determinate image--report blocks before calibration or decision claims; not arbitrary-pair conflict identification |
| Scope boundary | **Internally approved `G0-SCOPE A`:** determinate-conflict specificity is primary and natural ambiguity is veto-only; H2 remains unresolved. |
| Validation domain | **Commander and supervisor aligned:** chest radiography is primary; the exact task and dataset remain Gate 0 decisions |
| Data route | **Internally selected for readiness, externally blocked:** coupled MIMIC-CXR/JPG v2.1.0 under `DDR-2026-09-02-001`; no credential, query, download, or record access is authorized |
| Method identity | **Internally approved `G0-METHOD A`:** sole route with B inactive; exact executable specification and remaining Gate-0 rows are open |
| Primary instrument | **Protocol/interface approved:** explicitly non-novel paper-faithful `PROBVLM-2ADAPTER`; no probabilistic advantage is presumed |
| Matched comparator | **Protocol/interface approved:** `POINT-2ADAPTER-RECON`; `POINT-INFONCE` is secondary, while executable and negative-policy specifications remain open |
| Local storage | **Binding constraint:** the approximately 613-GB conditional simulation-output floor cannot run locally; this is not the medical dataset size, and `G0-RESOURCES` remains open |
| Submission target | **Commander/supervisor-aligned planning decision:** NeurIPS 2027 Main Track, conditional on evidence and the official call; acceptance is not assumed |
| Contribution type | **Planning classification:** Use-Inspired if the official 2027 rules retain an applicable category |
| Core execution | **Blocked by Gate 0:** remaining finite choices plus access, ethics, security, reader, licence, capacity, and feasibility evidence must be closed |

The current [Gate-0 closure audit](docs/research/gate0_closure_audit.md) records
partial internal approval, not execution readiness. The
[decision dossier](docs/research/gate0_decision_dossier.md) reduces the
remaining intervention, artifact, checkpoint, and staging questions to finite
owner choices. The [dataset decision record](docs/research/dataset_decision_record.md)
defines the non-executable MIMIC readiness boundary. The dossier retains the
first identified claim as
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
10. [Simulation resource-feasibility audit](docs/research/simulation_resource_feasibility_audit.md)
11. [Non-core simulation computational design](docs/research/noncore_simulation_computational_design.md)
12. [Simulation output and semantic-operation registry](docs/research/simulation_output_and_operation_registry.md)
13. [Statistical analysis plan](docs/research/statistical_analysis_plan.md)
14. [Evaluation protocol](docs/research/evaluation_protocol.md)
15. [Data and clinical governance](docs/research/data_governance.md)
16. [Dataset feasibility audit](docs/research/dataset_feasibility_audit.md)
17. [Dataset decision candidate](docs/research/dataset_decision_candidate.md)
18. [Dataset decision/readiness record](docs/research/dataset_decision_record.md)
19. [Backbone and resource audit](docs/research/execution_budget_and_backbone_audit.md)
20. [Estimator formalization audit](docs/research/estimator_formalization_audit.md)
21. [Method-A identification framework](docs/research/method_a_identification_framework.md)
22. [Baseline and ablation matrix](docs/research/baselines_and_ablations.md)
23. [Literature matrix](docs/research/literature_matrix.md)
24. [Novelty audit](docs/research/novelty_audit.md)
25. [Submission strategy](docs/research/submission_strategy.md)
26. [Gate-0 decision dossier](docs/research/gate0_decision_dossier.md)
27. [Gate-0 closure audit](docs/research/gate0_closure_audit.md)
28. [Decision log](docs/research/decision_log.md)

## Repository Checks

The initial repository contains governance tests, not scientific tests:

```bash
python -m pip install -r requirements-dev.txt
pytest -q
python scripts/check_repository.py
```

These checks verify structure and internal documentation links. They do not
validate a scientific claim. Before opening a pull request, the stricter
`python scripts/check_repository.py --final` command additionally requires a
placeholder-free Handoff Contract in a publishable lifecycle state.

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
