# Scope Charter

**Status:** Canonical one-paper boundary

**Decision:** DR-0002

## Title-Level Direction

**Working paper title:** *Ambiguity Is Not Conflict: Identifiable Cross-Modal
Conflict Estimation for Calibrated Selective Decisions*

The paper will study whether cross-modal conflict can be identified separately
from ambiguity within either modality, then test whether the identified
component adds calibrated and decision-relevant information beyond simpler
baselines.

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
- a pre-specified cross-backbone breadth test and an independent or natural
  stress set within the same scientific route;
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

The benchmark alone is insufficient for a Main Track method paper, and a new
embedding alone is insufficient for a source-identification paper. The primary
route therefore requires all three:

1. a formal conditional conflict estimand;
2. an estimator or estimation framework whose interpretation is tested by
   controlled interventions;
3. held-out evidence that the identified component matters beyond matched
   simpler predictors.

The exact estimator remains open. A negative comparison is valid and may force
a narrower evaluation-paper claim.
