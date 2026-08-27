# Measurement Protocol

**Status:** Protocol scaffold; not frozen for execution

## Objective

Test whether conditional cross-modal conflict can be measured as a distinct
construct rather than as a mixture of unimodal ambiguity, information loss,
synthetic artifacts, representation scale, epistemic uncertainty, and output
variation.

The first feasibility task should use atomic clinical findings rather than
open-ended report generation. The exact ontology, model, estimator, and sample
remain Gate 0 decisions.

## Candidate Prediction Unit

A candidate unit is:

```text
(source patient, radiograph study, atomic finding proposition,
 report proposition, intervention cell)
```

Examples of finding types may include presence, absence, location, severity,
or temporal change, but only categories with defensible labels and controlled
counterfactuals may enter the confirmatory set. All variants from one source
patient inherit the same split; when a constructed pair uses multiple patients,
every contributing patient must share a leakage-safe partition.

## Minimum Controlled Design

| Condition | Intended manipulation | Required control |
| --- | --- | --- |
| Matched clear pair | Image and report support the same clear proposition | Equivalent reconstruction without semantic change |
| Image ambiguity | Visual evidence permits multiple plausible finding interpretations | Report proposition and compatibility remain fixed; distinguish ambiguity from generic degradation |
| Text ambiguity | Wording permits multiple plausible finding interpretations | Image evidence and surface fluency remain fixed |
| Cross-modal conflict | One modality asserts a contrary task-relevant proposition | Linguistic/perceptual quality, length, finding prevalence, and source remain balanced |
| Missing evidence | A modality or task-relevant proposition is absent | Do not encode absence as contradiction |
| Corruption | Signal quality falls without a contrary proposition | Separate corruption severity from semantic ambiguity |
| Declared shift | A frozen population, acquisition, pathology, or model factor changes | Preserve the outcome definition and intervention logic |

Image ambiguity should preferably be defined by independent clinical
interpretability or adjudication evidence. Blur, noise, or occlusion are
corruption unless they demonstrably create multiple plausible interpretations.
Text hedging is not automatically ambiguity; the annotation protocol must
distinguish genuine underdetermination from explicit diagnostic uncertainty.

## Crossed Identification Design

The planned construct block is a pre-specified crossed design:

```text
C (compatible/conflicting)
  x A_v (image clear/ambiguous)
  x A_t (text clear/ambiguous)
```

Conflict direction is counterbalanced within conflicting cells: one arm holds
the image fixed and changes the report proposition; the other holds the report
fixed and substitutes a verified contrary image matched on declared nuisance
variables. Missingness and corruption variables \(M_v,M_t\) form separate
negative-control arms and are not treated as ambiguity.

Gate 0 must specify the exact crossed cells, blocking/matching variables,
conflict direction, severity levels, and estimable contrasts. If clinically
valid full crossing cannot be built, the design must become a declared
fractional factorial and the estimand and “factorial” claim must be narrowed
before execution—not after outcomes are observed.

## Pair Construction

Each eligible source block should generate a small family of counterbalanced
variants:

1. a clinician- or adjudication-verified matched reference pair—native pairing
   alone is not evidence of correctness or completeness;
2. semantics-preserving rewrite or reconstruction control;
3. the frozen \(C\times A_v\times A_t\) cells supported by that block;
4. conflicting variants in each approved direction at the same proposition;
5. one missingness or corruption control at matched severity where possible.

Natural, rule-edited, model-generated, and clinician-edited variants must be
tagged separately. Surface cues must be audited with a condition classifier
that cannot inspect clinical semantics. If condition labels are recoverable
from trivial templates, punctuation, length, source metadata, or image
processing signatures, rebuild the intervention set before promotion.

## Candidate Estimator Families

The comparison should use a frozen representation backbone wherever feasible:

1. deterministic similarity and retrieval margin;
2. learned conditional compatibility likelihood ratio;
3. probabilistic cross-modal embeddings with explicit scale or covariance;
4. energy-based or evidential disagreement;
5. ensemble or parameter-efficient ensemble decomposition;
6. Bayesian last-layer or Laplace-style epistemic approximation;
7. output semantic uncertainty when generation is part of the task.

For distributions \(q_v\) and \(q_t\), normalized symmetric KL,
Wasserstein--Bures distance, overlap, and learned density ratios are candidates,
not approved primary metrics. Raw latent distance is inadequate unless
conditioned on the distribution of compatible pairs because legitimate
modality-specific content can be far apart.

Every distributional method must document covariance parameterization,
positive-definiteness, regularization, latent dimension, scale, normalization,
sampling, and whether spread represents input ambiguity or parameter
uncertainty.

## Construct-Validity Tests

- held-fixed, within-source paired contrasts;
- monotonic response to pre-specified conflict severity;
- separate response profiles for image ambiguity and text ambiguity;
- negative controls for quality, length, norm, source, prevalence, and latent
  dimension;
- conditional analysis including \(A_v\), \(A_t\), \(M_v\), and \(M_t\)
  before assessing
  \(C_{vt}\);
- recovery of intervention labels without using those labels to define the
  evaluated score;
- repeated seeds and at least one meaningful frozen shift;
- blinded failure audit of compatible-high-conflict and
  contradictory-low-conflict pairs.

## Month 2–3 Kill Test

The feasibility study uses a development-only, patient-separated sample and a
small clinician-reviewed intervention set. It compares one deterministic
similarity baseline, one matched deterministic compatibility predictor, and at
most two tractable uncertainty-aware candidates.

The route is killed or redesigned before scale-up if any of the following
holds:

- clinical reviewers cannot reliably distinguish conflict from ambiguity;
- intervention cells contain obvious non-semantic artifacts;
- no candidate shows the pre-specified conflict-specific paired response;
- the response disappears after controlling for \(A_v\), \(A_t\), \(M_v\),
  \(M_t\), and source;
- the matched deterministic predictor fully subsumes the candidate at the
  smallest effect considered meaningful;
- annotation, data access, or compute cannot support a confirmatory study.

The kill test cannot be promoted as confirmatory evidence, and its outcomes
cannot be used to repeatedly redefine the primary endpoint.

## Required Pre-Execution Artifacts

- dataset decision record and cohort schema;
- atomic finding ontology and annotation rubric;
- intervention manifest with provenance and allowed transformations;
- frozen estimator interface, primary score, and normalization;
- smallest effect, sample/power analysis, and statistical analysis plan;
- baseline matrix, ablation matrix, model/data versions, compute ceiling, and
  stopping rule;
- governance approval and permitted-artifact list.
