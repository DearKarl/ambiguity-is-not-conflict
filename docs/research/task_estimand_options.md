# Atomic Task and Estimand Decision Packet

**Status:** Ultra-lane recommendation; pending Commander, clinical, and Gate-0
approval
**Date:** 2026-08-29
**Evidence class:** Protocol analysis; no data, model, or experiment was used

## Decision Problem

The project needs one task in which cross-modal conflict has a non-circular
meaning, within-modality ambiguity is independently measurable, a matched
deterministic method can falsify the estimator claim, and a downstream error
outcome is distinct from the conflict label.

The current documents correctly separate the constructs, but the previously
described full \(C\times A_v\times A_t\) crossing is not automatically valid.
When an image or assertion genuinely supports multiple interpretations,
binary compatibility may be undefined. Conditioning on a model-derived
ambiguity score does not repair that identification problem.

## Task Options

| Option | Exact task | Scientific advantage | Fatal risk | Verdict |
| --- | --- | --- | --- | --- |
| **A. Image-grounded binary finding prediction** | A frozen model receives one frontal chest radiograph and one atomic text assertion and predicts the image-grounded presence/absence of one finding | Conflict is a controlled auxiliary-evidence perturbation; downstream task error is distinct from the conflict label; supports selective-decision analysis | Requires independent image-only truth and proof that the finding is decidable from the exact image; the task is asymmetric | **Recommended single route** |
| B. Symmetric image--assertion compatibility classification | Predict whether image and text support the same proposition | Clean construct benchmark | Makes conflict the task label; a learned conflict estimator becomes an ordinary compatibility classifier and downstream incremental validity can become circular | Instrument or baseline only |
| C. Laterality conflict | On definitely positive cases, predict or verify left versus right while holding finding presence fixed | Minimal semantic change avoids positive/negative and negation artifacts | Bilateral disease, markers, mirroring, uncertain laterality, and smaller support threaten validity | Secondary falsification test only |
| D. Open-ended report generation | Generate a report from image and auxiliary text | High apparent realism | Entangles task accuracy, hallucination, output uncertainty, style, omissions, and conflict; ground truth is non-unique | Rejected for the first study |

## Recommended Task Unit

```text
(patient, study, exact single frontal image, singleton finding,
 atomic text assertion, intervention variant, frozen model)
```

- **Leakage unit:** patient; every derived variant inherits the same patient
  partition.
- **Clinical reference:** an independently elicited image-only judgement, not
  a label extracted from the paired report.
- **Text unit:** one fluent, atomic assertion with positive, negative,
  indeterminate, or missing semantic status under a text-only rubric.
- **Primary task output:** image-grounded presence/absence for determinate
  cases; abstention/indeterminate must be handled by a frozen rule rather than
  silently converted to a binary label.
- **Downstream error \(H\):** disagreement between the frozen task prediction
  and independent image-only reference on the eligible target cohort. The
  compatibility label itself is not \(H\).

**Provisional singleton finding:** pleural effusion presence versus absence.
This is an assumption, not a frozen decision. Before any estimator outcome is
viewed, clinical review and a post-freeze, authorized metadata-only feasibility
count must establish that it is judgeable from the exact single-frontal-image
input with adequate
positive, negative, and ambiguous support. If not, the finding must change
through a decision record before method evaluation.

## Observed Variables

For each authorized analysis unit, the schema should contain:

| Symbol | Meaning | Measurement boundary |
| --- | --- | --- |
| \(G,J\) | Patient and study linkage | Leakage control only; never a model feature |
| \(V,T,f\) | Exact image, atomic assertion, and singleton finding | Versioned, provenance-preserving inputs |
| \(Z\) | Randomized or counterbalanced intervention assignment | Generated before evaluation; concealed where feasible |
| \(\pi_v,\pi_t\) | Distributions of image-only and text-only interpretations | Independent blinded readers/raters; not candidate-model posteriors |
| \(A_v,A_t\) | Image and text ambiguity | Frozen functions of independent annotations and disagreement model |
| \(M_v,M_t\) | Missing information or corruption | Recorded separately from ambiguity and contradiction |
| \(X\) | Projection, acquisition, source, template, length, negation, prevalence, and provenance nuisances | Used for matching, blocking, and artifact audits |
| \(S_m\) | Candidate conflict score from method \(m\) | Orientation and normalization frozen on development-compatible cases |
| \(\hat Y,H\) | Frozen task prediction and independently labelled task error | Evaluated only in the declared target sample |

## Construct Definition

For determinate cases, let the independently judged image state and text state
be \(Y_v,Y_t\in\{0,1\}\). Define:

```text
C* = 0  when Y_v = Y_t and both are determinate
C* = 1  when Y_v != Y_t and both are determinate
C* = undefined when either modality is genuinely indeterminate or missing
```

An undefined conflict label is not a negative label. Those observations form
ambiguity or missingness control arms. This prevents the project from calling
weak/absent evidence a contradiction merely because a binary classifier must
choose a class.

## Primary Intervention Design

The first construct block should hold the image fixed and counterbalance a
clinically vetted positive and negative assertion:

1. independently adjudicated image-positive and image-negative source blocks;
2. one compatible and one conflicting atomic assertion per clear source;
3. equal use of positive and negative wording in compatible and conflicting
   cells;
4. semantics-preserving rewrite controls for every assertion family;
5. no change in finding, fluency, length band, template provenance, or
   decision-time metadata other than the atomic polarity;
6. variants linked to their source block and patient partition.

Image ambiguity, text ambiguity, missingness, and corruption are initially
separate negative-control arms or a declared fractional factorial. They must
not be forced into a nominal full factorial when \(C^*\) is undefined. A later
crossing is permitted only if a clinical semantics document supplies a valid
estimand for those cells before data are viewed.

## Candidate Construct Estimands

### E1 — Semantic-distribution discrepancy (diagnostic; not selected)

Let \(Y_v,Y_v'\sim\pi_v\) and \(Y_t,Y_t'\sim\pi_t\) be independent draws from
the separately elicited interpretation distributions, and let
\(L(y,y')=\mathbf 1(y\ne y')\). Define:

```math
\kappa_L(v,t)=
\mathbb E L(Y_v,Y_t)
-\frac12\mathbb E L(Y_v,Y_v')
-\frac12\mathbb E L(Y_t,Y_t').
```

For binary interpretation distributions this is

```math
\kappa_L(v,t)=\frac12\lVert\pi_v-\pi_t\rVert_2^2
             =(p_v-p_t)^2.
```

The subtraction removes average within-modality reader disagreement from raw
cross-modal disagreement. Identically ambiguous modalities have zero excess;
opposed concentrated modalities have a large value. However, this quantity is
not binary conflict \(C^*\). For example, \(p_v=0.5,p_t=1\) gives
\(\kappa_L=0.25\) even though image ambiguity makes \(C^*\) undefined.

Accordingly, \(\kappa_L\) may be interpreted as a semantic-distribution
discrepancy across all cells. It is eligible as a surrogate for determinate
conflict only on cells where \(C^*\) is defined, unless a separate formal bridge
from distribution discrepancy to conflict is established. Values in ambiguity
arms are negative-control diagnostics and must not be labelled conflict.

**Novelty boundary:** this object is energy-distance-like and reduces to a
simple squared probability difference in the binary case. It is a candidate
diagnostic quantity, not an automatically novel estimator or the selected
conflict estimand. If existing distance/decomposition work subsumes it,
novelty must come from a genuinely new identifiable estimation framework or
the method claim must be killed.

**Assumption:** the blinded reader distributions validly represent the
task-relevant semantic interpretation distributions. Reader variation caused
by skill, fatigue, or rubric failure must not be renamed input ambiguity.

### E2 — Conditional likelihood ratio (estimator framework candidate)

For features \(F_v,F_t\) and frozen nuisance stratum
\(W=(A_v,A_t,M_v,M_t,X)\), a candidate class-conditional density-ratio score is:

```math
\kappa_{LR}(F_v,F_t;W)=
\log\frac{p(F_v,F_t\mid C^*=1,W)}
          {p(F_v,F_t\mid C^*=0,W)}.
```

This makes a matched deterministic density-ratio classifier an exact
competitor, not a weak baseline. The target is identifiable only in strata
where \(C^*\) is defined and both conditions have support. It cannot be
extrapolated into genuinely ambiguous cells merely by inserting estimated
\(A_v,A_t\).

The ratio is insensitive to the constructed class prior only under the frozen
class-conditional sampling model. It remains specific to the intervention
construction, selection mechanism, feature map, and nuisance distribution. It
does not become a natural-cohort conflict probability without transport
assumptions, target-prior estimation, and separately evaluated recalibration.

**Novelty boundary:** a conditional classifier or likelihood ratio is not new
by itself. Promotion would require a non-trivial estimator or general
identification result that survives the matched deterministic comparator.

### E3 — Within-source specificity contrast (primary kill-stage estimand)

For each candidate score \(S_m\), define the clear-source paired conflict
contrast:

```math
\tau_{C,m}=\mathbb E_B
[S_m^{\mathrm{conflict}}-S_m^{\mathrm{compatible}}],
```

For any valid randomized or counterbalanced within-source control
\(j\in\mathcal J_{\mathrm{id}}\), define:

```math
\tau_{j,m}=\mathbb E_{B_j}
[S_m^{j}-S_m^{\mathrm{reference}(j)}].
```

The reference must be a semantics-checked clear, non-conflicting variant from
the same source block; the eligible block population and aggregation weights
must be frozen. \(\mathcal J_{\mathrm{id}}\) initially contains only valid
information-loss controls \(M_v,M_t\). It may include image or text ambiguity
only if a separately governed intervention creates the ambiguous variant while
preserving the declared proposition and supplies a valid within-source
reference. \(M_v,M_t\) already include missingness, truncation, corruption,
and quality loss, so corruption is not duplicated as a separate symbol.

The identified clear-source specificity margin is:

```math
\psi_{\mathrm{id},m}=
\min_{j\in\mathcal J_{\mathrm{id}}}
(\tau_{C,m}-|\tau_{j,m}|).
```

The score orientation and normalization must be frozen using development
compatible cases only. Promotion of this determinate-source claim requires the
simultaneous lower confidence bound for \(\psi_{\mathrm{id},m}\) to exceed a
pre-declared \(\delta_{\mathrm{specificity}}>0\), not merely a significant
conflict coefficient.

A natural ambiguous image or text usually lacks a valid clear within-source
counterfactual. Unless a governed ambiguity intervention is proven valid,
define an explicitly observational matched/weighted contrast:

```math
\gamma_{A_q,m}=
\mathbb E_w[S_m\mid A_q=1,C^*\ \mathrm{undefined}]
-\mathbb E_w[S_m\mid A_q=0,C^*=0],
\qquad q\in\{v,t\}.
```

The reference population, nuisance set, matching/weighting estimator, target
weights, overlap rule, and sensitivity analysis must be frozen before outcomes
are inspected. No causal interpretation is permitted for \(\gamma_{A_q,m}\).

The natural-ambiguity comparison is a separate conservative falsification
audit:

```math
\phi_{A,m}=\min_{q\in\{v,t\}}
(\tau_{C,m}-|\gamma_{A_q,m}|).
```

Because \(\gamma_{A_q,m}\) is observational, it does not enter
\(\psi_{\mathrm{id},m}\). A non-positive \(\phi_{A,m}\), failed overlap, or
strong sensitivity to the weighting rule can kill or redesign the candidate;
a positive \(\phi_{A,m}\) cannot identify causal separation from ambiguity.
The full ambiguity-separation claim requires either a valid governed ambiguity
intervention in \(\mathcal J_{\mathrm{id}}\), or a separately frozen estimand
with defensible conditional-exchangeability and transport assumptions, overlap
rules, and sensitivity analysis. Without one of those routes, the permitted
claim narrows to determinate-conflict specificity against the valid controlled
arms.

### E4 — Downstream incremental-validity estimand

On a separate natural target-distribution cohort:

```math
\Delta_m=
\mathbb E[\ell(H,r_{\mathrm{base}})
          -\ell(H,r_{\mathrm{base}+\hat\kappa_m})],
```

where \(\ell\) is a frozen proper score for the probability of task error \(H\).
This is not estimable until \(H\), the eligible cohort, baseline terms,
calibration protocol, proper score, calibration budget, multiplicity rule, and
smallest useful \(\Delta\) are frozen. “Overconfident error” should be a
diagnostic subgroup or pre-specified secondary outcome; a post-hoc confidence
threshold must not define the primary target.

## Minimum Month-3 Comparison Set

Use the same frozen encoders, data partitions, task labels, and tuning budget
where technically possible:

1. raw deterministic cosine/retrieval margin;
2. matched learned deterministic compatibility/density-ratio predictor;
3. evidential categorical heads, including a vacuity/dissonance or
   conflict-discounting comparator;
4. probabilistic/distributional adapter;
5. matched point-softmax adapter whenever scale or covariance is claimed to
   help.

Required negative controls include semantics-preserving rewrites, image-only
and text-only conflict-cell probes, an unrelated finding change, missing versus
contradictory assertions, semantics-preserving corruption, normalization and
embedding-norm checks, template/length/punctuation/provenance probes, and label
permutation.

## Identification Assumptions

- independent and sufficiently reliable image-only and text-only annotation;
- a well-defined, single atomic finding and exact image input;
- consistency of each controlled variant with its documented intervention;
- positivity for compatible and conflicting text polarity within each clear
  source stratum;
- counterbalanced polarity, source, prevalence, and template artifacts;
- no patient/source leakage and no condition label recoverable from one
  modality or nuisance metadata alone;
- no use of paired-report labels to define image truth or image ambiguity;
- fixed handling of indeterminate and missing cases;
- no estimator-driven redefinition of \(A_v,A_t,C^*\), the score, or endpoint.

## Proposed Kill Decisions

Kill or redesign construct estimation if any of these occurs:

- independent reviewers cannot reliably separate determinate truth,
  ambiguity, missingness, and corruption;
- the singleton finding is not judgeable from the frozen image input;
- either modality alone or nuisance metadata predicts the conflict cell beyond
  a pre-specified chance-equivalence tolerance;
- the simultaneous lower bound for \(\psi_{\mathrm{id},m}\) does not exceed
  the frozen smallest effect;
- no valid governed ambiguity intervention or defensible exchangeability/
  transport estimand can support the intended ambiguity-separation claim;
- the binary effect has the wrong direction, is label-dependent,
  normalization-dependent, source-dependent, or is lost under leakage-safe
  repetition; if at least three ordered conflict-severity levels are frozen,
  a non-monotone response is an additional failure.

Kill the **Main Track estimator claim**, while retaining and reporting the null
result, if the matched deterministic predictor subsumes the best
uncertainty-aware candidate at the frozen equivalence/non-inferiority margin,
or if the chosen estimand is already substantively covered by known
distance/decomposition work.

Do not proceed to calibration or selective review until \(\Delta_m\) is defined
non-circularly and the natural-cohort effect exceeds its separately frozen
smallest useful value.

## Proposed Decision

Adopt Option A as the sole narrow protocol route, with a declared fractional
design and independent modality-specific annotation. This recommendation does
**not** authorize execution. Gate 0 remains open until the Commander and the
relevant clinical/governance owner approve:

1. singleton finding and exact image input;
2. image-only and text-only rubrics plus reliability threshold;
3. governed ambiguity intervention or an explicit observational
   identification/claim-narrowing rule;
4. downstream \(H\) and proper score;
5. numerical \(\delta_{\mathrm{specificity}}\), deterministic-subsumption
   margin, and smallest useful \(\Delta\);
6. power/sample plan, compute ceiling, and annotation budget;
7. dataset access, storage, processing, and permitted-output boundary.

Passing the Month-3 scientific gate remains necessary but is never sufficient
for NeurIPS Main Track readiness, acceptance, publication, or clinical value.
