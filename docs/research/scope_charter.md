# Scope Charter

**Status:** Canonical one-paper boundary

**Decision:** DR-0002 and DR-0006

## Title-Level Direction

**Working paper title:** *Ambiguity Is Not Conflict: Identifiable Cross-Modal
Conflict Estimation for Calibrated Selective Decisions*

The paper will study whether cross-modal conflict can be identified separately
from ambiguity within either modality, then test whether the identified
component adds calibrated and decision-relevant information beyond simpler
baselines.

Chest radiography is the primary validation domain, not part of the scientific
construct or title. Any breadth study must replicate the same construct and
cannot become a second research direction.

## Canonical Research Object

For paired image and text evidence, the desired decomposition is:

```math
A_v,\quad A_t,\quad M_v,\quad M_t,\quad C_{vt},\quad
U_{\mathrm{epi}},\quad U_{\mathrm{out}}.
```

- \(A_v\): multiple plausible interpretations attributable to the image;
- \(A_t\): multiple plausible interpretations attributable to the text;
- \(M_v\): missingness, corruption, or quality loss in the image;
- \(M_t\): missingness, truncation, corruption, or quality loss in the text;
- \(C_{vt}\): conditional incompatibility about a task-relevant proposition;
- \(U_{\mathrm{epi}}\): uncertainty associated with model knowledge or
  parameters;
- \(U_{\mathrm{out}}\): uncertainty across output meanings.

These are desired operational distinctions, not quantities already proven to
be identifiable.

## In Scope

- an atomic clinical-finding prediction or verification unit;
- paired radiograph--report evidence under patient-separated evaluation;
- controlled matched, image-ambiguous, text-ambiguous, conflicting, missing,
  corrupted, and shifted conditions;
- conditional conflict estimands and matched deterministic alternatives;
- probabilistic embeddings, ensembles, approximate-Bayesian methods, output
  semantic uncertainty, and conformal selection as comparisons;
- construct validity, proper scores, calibration, overconfident error,
  risk--coverage, fixed-budget review, and failure-case analysis;
- a pre-specified cross-backbone breadth test and, subject to its own bounded
  data/scope/governance decision, either a second medical dataset or a small
  controlled general-domain benchmark that tests the same construct;
- a clinician-reviewed retrospective subset after governance approval.

## Out of Scope Without a New Decision Record

- autonomous diagnosis, treatment, prospective deployment, or claims of
  clinical benefit;
- generic hallucination detection, RAG, or multi-agent orchestration as the
  primary contribution;
- open-ended report generation as the first feasibility task;
- selecting a method because it is labelled Bayesian or probabilistic;
- large-model training before measurement and data protocols are frozen;
- using ReXErr alone as the primary construct-identification benchmark;
- treating synthetic conflict frequency as real-world prevalence.

## Outcome Hierarchy

| Gate | Primary outcome | Permitted claim |
| --- | --- | --- |
| Construct identification | Specific paired response to compatibility interventions after conditioning on unimodal ambiguity | The score behaves consistently with the operational conflict construct |
| Incremental validity | Held-out improvement beyond frozen confidence and deterministic predictors | Conflict adds predictive information in the tested task |
| Calibration | Proper scores and calibration diagnostics in-domain and under declared shift | Estimated risk is calibrated in the tested populations |
| Decision value | Selective risk or expected utility at equal coverage/review budget | The frozen policy improves the tested retrospective decision outcome |
| Clinical value | Separate prospective or human-factors evidence | Not claimable from the initial paper alone |

## Primary Contribution Boundary

The single intended primary contribution is a formal conditional conflict
estimand together with an estimator or general estimation framework whose
interpretation can be falsified. The benchmark alone is insufficient for a
Main Track method paper, and a new embedding alone is insufficient for a
source-identification paper.

Controlled interventions provide identification evidence; matched held-out
comparisons provide incremental-validity evidence; calibration and selective
review provide downstream decision evidence. These are supports for the one
central contribution, not separate contribution claims. The exact estimator
remains open, and deterministic, evidential, probabilistic, Bayesian, ensemble,
and semantic-entropy methods remain candidate comparison families, with
conformal methods as candidate risk-control layers. Gate 0 must freeze the
smallest matched set capable of falsifying the claim. A negative comparison is
valid and may force a narrower evaluation-paper claim.
