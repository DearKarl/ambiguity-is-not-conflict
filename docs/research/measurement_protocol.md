# Measurement Protocol

**Status:** Gate-0 protocol candidate; pointwise method identity remains blocked
and no execution is authorized

## Objective

Test whether conditional cross-modal conflict can be measured as a distinct
construct rather than as a mixture of unimodal ambiguity, information loss,
synthetic artifacts, representation scale, epistemic uncertainty, and output
variation.

The first feasibility task should use one image-grounded binary clinical
finding rather than open-ended report generation. A frozen model receives an
exact image and an atomic auxiliary text assertion, then predicts the
image-grounded finding state. Conflict measurement is an input construct;
downstream task error against independent image-only judgement is a separate
outcome. The exact finding, model, estimator, and sample remain Gate 0
decisions.

## Candidate Prediction Unit

A recommended candidate unit is:

```text
(source patient, radiograph study, exact single frontal image,
 singleton finding, atomic text assertion, intervention variant,
 frozen model)
```

The faithful native MIMIC pairing unit remains a study-level image set because
one report may cover multiple views. The proposed single-frontal-image
restriction is valid only if independent review confirms that the singleton
finding is assessable under the frozen exact-image rubric, the prescribed field
is adequately represented, and determinate source cases can receive independent
positive/negative states. Natural ambiguous cases need not have a unique state.
Pleural-effusion presence/absence is a provisional finding assumption, not an
approved ontology.

All variants from one source patient inherit the same split; when a constructed
pair uses multiple patients, every contributing patient must share a
leakage-safe partition. Report-derived labels may support retrieval after
access approval but cannot independently define image truth or image
ambiguity.

## Minimum Controlled Design

| Condition | Intended manipulation | Required control |
| --- | --- | --- |
| Matched clear pair | Image and report support the same clear proposition | Equivalent reconstruction without semantic change |
| Image ambiguity | Visual evidence permits multiple plausible finding interpretations | Match the text proposition and nuisance variables; leave binary compatibility undefined; distinguish ambiguity from generic degradation |
| Text ambiguity | Wording permits multiple plausible finding interpretations | Match the image/source and surface fluency where possible; leave binary compatibility undefined |
| Cross-modal conflict | One modality asserts a contrary task-relevant proposition | Linguistic/perceptual quality, length, finding prevalence, and source remain balanced |
| Missing evidence | A modality or task-relevant proposition is absent | Do not encode absence as contradiction |
| Corruption | Signal quality falls without a contrary proposition | Separate corruption severity from semantic ambiguity |
| Declared shift | A frozen population, acquisition, pathology, or model factor changes | Preserve the outcome definition and intervention logic |

Image ambiguity should preferably be defined by independent clinical
interpretability or adjudication evidence. Blur, noise, or occlusion are
corruption unless they demonstrably create multiple plausible interpretations.
Text hedging is not automatically ambiguity; the annotation protocol must
distinguish genuine underdetermination from explicit diagnostic uncertainty.

## Fractional Identification Design

The primary construct block uses only independently determinate image and text
states. It holds the image fixed and counterbalances clinically vetted positive
and negative atomic assertions across image-positive and image-negative source
blocks:

```text
clear image truth (+/-)
  x text polarity (+/-)
  -> compatible or conflicting determinate pair
```

Every text polarity must occur equally in compatible and conflicting cells so
that negation or prevalence does not reveal the condition. Conflict direction
is counterbalanced by the image-positive and image-negative sources.

Genuine image ambiguity, text ambiguity, missingness, and corruption form
separately measured negative-control arms or a declared fractional factorial.
If either modality is genuinely indeterminate or missing, binary conflict is
undefined rather than negative. A nominal full
\(C\times A_v\times A_t\) crossing is prohibited unless a clinical semantics
document first shows that compatibility is well-defined in every included
cell. Regression adjustment for model-derived ambiguity does not repair an
undefined construct.

Gate 0 must specify the exact cells, blocking/matching variables, severity
levels, independent annotation distributions, and estimable contrasts. Any
later crossed or image-substitution arm requires its own pre-data justification
and connected-component leakage rule.

## Pair Construction

Each eligible source block should generate a small family of counterbalanced
variants:

1. an independently image-adjudicated clear source—native pairing alone is not
   evidence of correctness, completeness, or image truth;
2. vetted positive and negative atomic assertions for the same singleton
   finding, counterbalanced across positive and negative sources;
3. a semantics-preserving rewrite control for every assertion family;
4. one independently validated image-information-loss `M_v` role and one text-
   information-loss `M_t` role for the proposed primary `J_id` family, with
   exact operations still requiring approval;
5. missingness, surface-form, and unrelated-finding diagnostics that cannot
   substitute for either primary control identity;
6. separately recruited and labelled natural image/text ambiguity pools used
   only for observational veto audits, never generated as source-block siblings
   or inserted into the identified control family.

Natural, rule-edited, model-generated, and clinician-edited variants must be
tagged separately. Surface cues must be audited with a condition classifier
that cannot inspect clinical semantics. If condition labels are recoverable
from trivial templates, punctuation, length, source metadata, or image
processing signatures, rebuild the intervention set before promotion.

## Candidate Estimator Families

The [formalization audit](estimator_formalization_audit.md) selected none of the
three exact pointwise candidates. The binary learned-belief/Gaussian excess
discrepancy collapses to a matched mean-distance score after self-spread
correction; the conditional likelihood ratio is a prior-adjusted deterministic
classifier logit; and evidential confident disagreement is already occupied by
RCML/Discounted Belief Fusion. These are formal method-claim kills, not
empirical equivalence or deterministic-subsumption results.

The families below therefore remain comparison instruments, diagnostics, or
the inputs to a future pre-data theory brief. None is an approved novel primary
estimator. Any later comparison should use a frozen representation backbone
wherever feasible:

1. deterministic similarity and retrieval margin;
2. learned conditional compatibility likelihood ratio;
3. probabilistic cross-modal embeddings with explicit scale or covariance;
4. energy-based or evidential disagreement;
5. ensemble or parameter-efficient ensemble decomposition;
6. Bayesian last-layer or Laplace-style epistemic approximation;
7. output semantic uncertainty when generation is part of the task.

For learned model-belief distributions \(\widehat\pi_v\) and
\(\widehat\pi_t\), a candidate pointwise discrepancy is:

```math
\kappa_L=
\mathbb E L(\widehat Y_v,\widehat Y_t)
-\tfrac12\mathbb E L(\widehat Y_v,\widehat Y_v')
-\tfrac12\mathbb E L(\widehat Y_t,\widehat Y_t').
```

With binary states and disagreement loss this reduces to
\((\widehat p_v-\widehat p_t)^2\), an energy-distance-like quantity. It is not
binary conflict: \(\widehat p_v=0.5,\widehat p_t=1\) gives a positive model
discrepancy even when the independently governed reader construct would make
\(C^*\) undefined. Applying the same algebra to external reader frequencies
\(p^R_v,p^R_t\) yields a measurement diagnostic, not a deployable pairwise
score. A learned score is eligible as a conflict surrogate only on determinate
cells unless a formal bridge is established. A conditional likelihood ratio
between conflicting and compatible determinate pairs is a second candidate,
with a matched deterministic density-ratio estimator as an exact competitor.
Neither candidate is selected or automatically novel.

Normalized symmetric KL, Wasserstein--Bures distance, overlap, and learned
density ratios remain occupied comparison choices, not approved primary
metrics. Raw latent distance is inadequate unless conditioned on the
distribution of compatible pairs because legitimate modality-specific content
can be far apart.

Every distributional method must document covariance parameterization,
positive-definiteness, regularization, latent dimension, scale, normalization,
sampling, and whether spread represents input ambiguity or parameter
uncertainty.

The compatible-reference standardization below removes positive affine score
changes but not nonlinear monotone links. Every candidate and matched
deterministic comparator must therefore use an identical square, sigmoid,
exponential, or other pre-/post-link convention. A larger `psi_mag` created
only by a different link is not a material uncertainty-aware advantage.

## Construct-Validity Tests

- held-fixed, within-source paired contrasts;
- directional response to the binary compatible/conflicting intervention; a
  monotonicity test is required only if Gate 0 freezes at least three ordered,
  clinically meaningful conflict-severity levels;
- separate response profiles for image ambiguity and text ambiguity;
- negative controls for quality, length, norm, source, prevalence, and latent
  dimension;
- image-only, text-only, and nuisance-only probes for intervention-cell
  recoverability;
- an identified specificity analysis using only valid randomized or
  counterbalanced controls; natural \(A_v,A_t\) comparisons remain separate
  conservative falsification audits and do not receive conflict labels;
- recovery of intervention labels without using those labels to define the
  evaluated score;
- repeated seeds and at least one meaningful frozen shift;
- blinded failure audit of compatible-high-conflict and
  contradictory-low-conflict pairs.

## Month 2–3 Kill Test

The feasibility study uses a development-only, patient-separated, single-
finding sample and a small independently reviewed intervention set. It
compares raw deterministic similarity, one matched deterministic
compatibility/density-ratio predictor, one evidential categorical candidate,
and one probabilistic/distributional candidate on the same frozen encoders and
budget. A matched point-softmax adapter is required whenever learned
scale/covariance is credited.

For score \(S_m\), the proposed primary kill-stage estimand starts with the
clear-source paired conflict contrast:

```math
\tau_{C,m}=\mathbb E[S_m^{conflict}-S_m^{compatible}],
```

Any control \(j\in\mathcal J_{\mathrm{id}}\) enters through a paired contrast
\(\tau_{j,m}\) only when it has a valid randomized or counterbalanced,
semantics-checked within-source reference. The set initially contains valid
\(M_v,M_t\) controls and includes ambiguity only after a separately governed
ambiguity intervention is shown valid. The signed diagnostic margin is:

```math
\psi_{\mathrm{id},m}=
\min_{j\in\mathcal J_{\mathrm{id}}}
(\tau_{C,m}-|\tau_{j,m}|).
```

Because signed control responses can cancel, the recommended primary candidate
is the magnitude-safe margin:

```math
\psi_{\mathrm{mag},m}=
\min_{j\in\mathcal J_{\mathrm{id}}}
\mathbb E[D_{C,m}-|D_{j,m}|].
```

The frozen compatible-reference score scale, candidate 0.20 smallest effect,
simultaneous patient-cluster bounds, and power grid are in the
[statistical analysis plan](statistical_analysis_plan.md). Its scale-free
`theta` statistic is secondary unless separately powered. None is approved for
execution.

For \(n\) complete, equally weighted patient blocks, the exact plug-in
estimator is:

```math
\widehat\psi_{\mathrm{mag},m}
=\min_{j\in\mathcal J_{\mathrm{id}}}
\left\{\frac1n\sum_{b=1}^n
\left(D_{C,bm}-|D_{j,bm}|\right)\right\}.
```

It is the minimum of control-specific sample means, not the mean of a
within-block minimum. It estimates the controlled population specificity of an
already frozen pointwise instrument; it is not itself a deployable pair-level
conflict score.

Genuine natural ambiguity without such a counterfactual uses a separately
pre-specified matched/weighted contrast \(\gamma_{A_v,m}\) or
\(\gamma_{A_t,m}\), with the reference population, nuisance set, weights,
overlap, and sensitivity analysis frozen before outcomes are inspected. These
observational contrasts do not enter \(\psi_{\mathrm{mag},m}\) or
\(\psi_{\mathrm{id},m}\). A large or
unstable ambiguity response may falsify the candidate, but a small response
cannot identify causal separation from ambiguity.

Promotion of the determinate-source claim requires the simultaneous lower
confidence bound for the approved magnitude-safe endpoint to exceed its
pre-declared positive smallest effect. A full ambiguity-separation claim
additionally requires a
valid governed ambiguity intervention or a separately frozen estimand with
defensible conditional-exchangeability and transport assumptions. Score
orientation and normalization use development-compatible cases only.

Promotion out of the kill-test stage requires one exact primary pointwise
instrument definition/interface to be named and approved at Gate 0. Development
may fit or tune only inside that frozen identity; its single fitted instance,
normalizer, link, and configuration must then be locked before holdout access.
That pre-locked instrument must satisfy all of the following:

1. respond more strongly to controlled incompatibility than to valid
   randomized or counterbalanced information-loss controls;
2. retain the pre-specified positive magnitude-safe specificity margin, and
   either include a valid governed ambiguity intervention in that margin or explicitly
   narrow the claim; observational ambiguity comparisons can falsify but cannot
   confirm separation;
3. exceed deterministic similarity by a pre-specified non-trivial margin and
   not be fully subsumed by the matched deterministic compatibility/failure
   predictor at the smallest effect considered meaningful;
4. survive surface-artifact, representation-scale/normalization,
   patient/source-leakage, repetition, and failure-case checks.

The route is killed or redesigned before scale-up if any required condition
fails, or if clinical reviewers cannot reliably distinguish conflict from
ambiguity, intervention cells contain obvious non-semantic artifacts, or
annotation, data access, or compute cannot support a confirmatory study.

This gate is not executable until the singleton finding, exact image input,
reader-reliability threshold, governed ambiguity intervention or explicit
identification/claim-narrowing rule, numerical specificity margin,
deterministic-subsumption margin, downstream error \(H\), sample/power plan,
and budgets are frozen.

Passing this development-only gate is necessary but not sufficient for a Main
Track method claim. The kill test cannot be promoted as confirmatory evidence,
and its outcomes cannot be used to repeatedly redefine the primary endpoint.

## Required Pre-Execution Artifacts

- dataset decision record and cohort schema;
- atomic finding ontology and annotation rubric;
- intervention manifest with provenance and allowed transformations;
- frozen estimator interface, primary score, and normalization;
- smallest effect, sample/power analysis, and statistical analysis plan;
- baseline matrix, ablation matrix, model/data versions, compute ceiling, and
  stopping rule;
- governance approval and permitted-artifact list.
