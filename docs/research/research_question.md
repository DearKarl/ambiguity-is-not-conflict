# Research Question and Falsifiable Hypotheses

**Status:** Title-level direction selected; exact estimands remain Gate 0 items

## Narrow Research Question

At the atomic clinical-finding level, can a conflict component respond
specifically to controlled image--report incompatibility rather than image
ambiguity, text ambiguity, missingness, corruption, epistemic uncertainty, or
output uncertainty, and add held-out prediction of overconfident model errors
at a fixed review budget?

## Intended Primary Claim

A formally defined, conditionally estimated cross-modal conflict component can
be separately identified under controlled interventions and provides
non-redundant, calibrated information for selective review beyond frozen
unimodal uncertainty, ordinary confidence, output uncertainty, and matched
deterministic failure predictors.

This is the claim to test, not a result.

## H1 — Conflict Specificity

**Hypothesis.** When a task-relevant proposition is changed to make image and
text incompatible while ambiguity and surface quality are held or
counterbalanced, the pre-specified conflict estimator changes monotonically in
the expected direction and more strongly than under negative controls.

**Null interpretation.** If the response is equally explained by image
quality, text length, source identity, prevalence, embedding norm, or generic
pair dissimilarity, the estimator does not identify conflict.

## H2 — Separation from Unimodal Ambiguity

**Hypothesis.** The conflict contrast remains non-negligible after conditioning
on image-only and text-only ambiguity measurements, while those ambiguity
interventions retain distinguishable signatures.

**Null interpretation.** If a common undifferentiated uncertainty factor
explains all conditions, the proposed decomposition is not supported even if
the score detects corrupted or difficult examples.

## H3 — Held-Out Incremental Validity and Calibration

**Hypothesis.** Adding the conflict component to a frozen baseline risk model
improves a pre-specified held-out proper score by more than the smallest effect
of interest and preserves acceptable calibration under one declared shift.

**Null interpretation.** If the gain disappears with patient-level splitting,
repeated seeds, recalibration, or a matched deterministic failure predictor,
the conflict component is redundant for outcome-risk prediction.

## H4 — Fixed-Budget Decision Value

**Hypothesis.** At an equal review budget or answer coverage, a policy using
the calibrated decomposition has lower selective risk or regret than policies
using ordinary confidence or output uncertainty alone.

**Null interpretation.** If benefit depends on post-hoc thresholds,
unrealistic review costs, or information unavailable at decision time, no
decision-value claim is permitted.

## Candidate Construct Estimand

Let \(S_i(c,a_v,a_t)\) be a standardized candidate conflict score for source
case \(i\), conflict condition \(c\), image-ambiguity condition \(a_v\), and
text-ambiguity condition \(a_t\). A candidate paired contrast is:

```math
\tau_C = \mathbb E_i\left[
S_i(1,a_v,a_t)-S_i(0,a_v,a_t)
\right],
```

averaged over pre-specified ambiguity strata. A specificity analysis must
compare \(\tau_C\) with corresponding image-ambiguity, text-ambiguity,
missingness, and corruption contrasts, then assess whether \(C_{vt}\) retains
incremental value conditional on \(A_v\), \(A_t\), \(M_v\), and \(M_t\).

The score, scale, estimand, aggregation, smallest effect, and multiplicity rule
must be frozen before confirmatory data are inspected.

## Claim Ladder

1. association;
2. construct validity under controlled intervention;
3. held-out incremental validity;
4. probabilistic calibration in the tested population;
5. retrospective decision value;
6. clinical value only after separate governed human/prospective evidence.

No result may skip a rung by changing terminology.
