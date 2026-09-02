# Method-A Identification and Measurement Framework

**Status:** Commander-approved interface freeze with user-attested supervisor
alignment on the intervention framing and named method roles; formal
supervisor approval of the sole-route/B-inactive boundary and exact
statistical, model, inference, and executable approvals open; protocol only

**Authority:** DR-0016 and DR-0017

**Date:** 2026-09-02

## Decision Boundary

`G0-METHOD A` is the project's only active route. The paper will not claim a
new pair-level conflict estimator. It will test a partial-construct,
intervention-identified measurement and inference framework for whether a
prospectively frozen score responds specifically to determinate semantic
incompatibility rather than to approved modality-specific information-loss
controls.

This document retains the Commander-level scientific-interface freeze from
DR-0016. Based on the Commander's report, DR-0017 adds supervisor agreement
with Method A's scientific framing and the named method roles, not the exact
score, inference, architecture, or executable package. The email asked whether
the intervention framework should be the primary contribution, not whether
Method A must be the sole route with B inactive; formal supervisor approval of
that exact boundary remains open. This does not close Gate 0, approve
implementation, establish novelty, authorize data/model access, or create
scientific evidence. Exact software, backbone, data, numerical, calibration,
reader, and resource choices remain owner-blocked.

## Fact, Inference, Assumption, and Decision Ledger

### Facts

- TB-0006 killed all three proposed new pointwise-estimator claims: the
  corrected probabilistic discrepancy reduces to deterministic mean
  disagreement, the conditional density ratio is a prior-adjusted
  deterministic classifier logit, and the evidential form is already occupied.
- A learned-output tuple can be compatible with multiple underlying semantic
  or measurement states. Model outputs alone therefore need not identify the
  independently defined conflict construct.
- `psi_mag` is a population functional of a frozen score over controlled
  source blocks. It is not a pair-level score.
- The ProbVLM paper defines a generalized-Gaussian probabilistic adapter. The
  audited official code is MIT-licensed but is not textually or operationally
  identical to the displayed paper likelihood. A code-exact implementation is
  therefore a different scientific choice.
- Standard InfoNCE introduces off-diagonal negative assumptions. For repeated,
  low-cardinality atomic assertions, an off-diagonal record can be semantically
  compatible and therefore become a false negative.

### Project inference

The broad idea of measuring multimodal disagreement or separating ambiguity
from conflict is occupied. A narrower framework-level gap may survive in the
combination of independent modality-only semantic measurement, determinate-
support restriction, controlled compatibility interventions, valid paired
information-loss controls, joint inference on a population specificity
functional, matched deterministic challenge, and downstream decision gates.
This is a novelty hypothesis to keep auditing, not an established fact.

### Assumptions

- The governed modality-only measurement rules can establish determinate
  semantic states with adequate reliability without inspecting candidate
  scores.
- The approved compatibility and information-loss versions can be constructed
  without residual semantic, surface-form, provenance, or selection leakage.
- The selected/evaluable intervention population is scientifically meaningful
  and any transport claim can be stated and defended separately.
- Compatible-reference normalization and the frozen score interface remain
  stable before protected outcomes are opened.

### Decisions

- Adopt Method A as the single route and make no new pointwise-estimator claim.
- Use a paper-faithful, project-native `PROBVLM-2ADAPTER` score as the explicitly
  non-novel primary instrument.
- Use `POINT-2ADAPTER-RECON`, not `POINT-INFONCE`, as the primary matched
  deterministic comparator.
- Retain `POINT-INFONCE` only as a secondary contrastive baseline whose
  denominator, multi-positive, and false-negative rules must be frozen before
  any execution.

## Partial Construct and Support

For modality (r\in\{v,t\}), let

```math
R_r\in\{0,1,\bot\}
```

be the result of the frozen, independent, modality-only semantic measurement
rule for the atomic proposition, and define

```math
\Delta_r=\mathbf 1\{R_r\in\{0,1\}\},
\qquad
\mathcal D=\{\Delta_v=\Delta_t=1\}.
```

The operational conflict construct is

```math
C_R^*=\mathbf 1\{R_v\ne R_t\}
\quad\text{on }\mathcal D,
\qquad
C_R^*=\bot\quad\text{outside }\mathcal D.
```

This is a measurement-rule-defined partial construct, not universal semantic
truth and not a model output. Ambiguity is not coded as compatibility. A
degraded modality may remain determinate if the governed rule still assigns a
unique state; its information-loss status remains separately recorded.

## Proposition 1 — Output-Only Non-Identification

Let (O_\theta(X_v,X_t)) be any learned-output tuple and let (s(O_\theta))
be any deterministic or randomized score based only on that tuple. If two
admissible latent or measurement states induce the same law of (O_\theta)
but different values of (C_R^*), including one undefined value, then
(C_R^*) is not identified by the distribution of (O_\theta).

One counterexample fixes (O_\theta=o) in three worlds:

1. (R_v=\bot,R_t=1), so (C_R^*=\bot);
2. (R_v=0,R_t=1), so (C_R^*=1);
3. (R_v=1,R_t=1), so (C_R^*=0).

The learned score is identical in all three worlds while the construct differs.
Therefore no output-only uncertainty correction, distance, density ratio, or
evidential score becomes construct-valid without an external semantic or
interventional bridge.

## Controlled Identification Target

For eligible determinate source block (b), let the controlled assertion
version (c\in\{0,1\}) satisfy

```math
R_t(c)=R_v\oplus c,
```

where (c=0) is compatible and (c=1) is incompatible. Let
(Z_{bm}(c)) be the standardized potential score for frozen instrument (m).
For each approved information-loss control (j\in\mathcal J_{id}), let
(Z_{bm}(j)) and (Z_{bm}(r_j)) denote the control and its frozen within-source
reference.

Define

```math
D_{C,bm}=Z_{bm}(1)-Z_{bm}(0),
\qquad
D_{j,bm}=Z_{bm}(j)-Z_{bm}(r_j),
```

```math
\mu_{mj}=\mathbb E[D_{C,m}-|D_{j,m}|],
\qquad
\psi_{mag,m}=\min_{j\in\mathcal J_{id}}\mu_{mj}.
```

The initial candidate family contains one valid image-information-loss control
and one valid text-information-loss control. Natural image and text ambiguity
remain separate observational veto audits and do not enter
(\mathcal J_{id}) without a later governed identification route.

## Proposition 2 — Intervention Identification

The component means (\mu_{mj}), and hence their finite-family minimum
(\psi_{mag,m}), are nonparametrically identified from the paired complete-
block law under all of the following:

1. independent, score-blind construct measurement;
2. consistency and stable intervention versions;
3. complete crossing or positive randomized/counterbalanced assignment;
4. no interference across patient/source blocks;
5. no candidate-score, split, outcome, provenance, or construction leakage;
6. stable interpretation of the assigned assertion-substitution package;
7. task-relevant, state-valid controls and references;
8. a frozen score, nonlinear link, orientation, compatible-reference
   normalizer, and target weighting rule; and
9. a prospectively defined complete-block selected/evaluable population.

If every version is evaluated within every source block, treatment
exchangeability is unnecessary for that complete-block contrast. If only one
version is observed, randomized assignment or a separately justified
exchangeability condition is additionally required. The design identifies the
whole assertion-substitution package. Interpreting that package effect as the
effect of semantic compatibility additionally requires semantic isolation or
an explicit structural-cancellation assumption that removes every other
pathway. Randomization, balance, or counterbalancing alone does not supply that
semantic interpretation.

This result identifies an intervention-relative average score response. It
does not identify (C_R^*) for an arbitrary pair, natural conflict prevalence,
or a universal latent conflict variable.

## Primary Instrument Freeze

Let the frozen backbone produce modality features (z_v,z_t\in\mathbb R^d),
and let one shared, prospectively frozen feature transform yield (u_v,u_t).
The two modality-specific ProbVLM adapters return

```math
q_v(u_v)=(\mu_v,\alpha_v,\beta_v),
\qquad
q_t(u_t)=(\mu_t,\alpha_t,\beta_t),
```

with coordinatewise positive scale and shape. For target (u), define the
mean coordinatewise generalized-Gaussian negative log-likelihood

```math
\ell_{GGD}(u;\mu,\alpha,\beta)
=\frac1d\sum_{k=1}^d
\left[
\left(\frac{|u_k-\mu_k|}{\alpha_k}\right)^{\beta_k}
+\log(2\alpha_k)+\log\Gamma(1/\beta_k)-\log\beta_k
\right].
```

The frozen pointwise instrument is

```math
S_P(v,t)=\tfrac12\left[
\ell_{GGD}(u_t;\mu_v,\alpha_v,\beta_v)
+\ell_{GGD}(u_v;\mu_t,\alpha_t,\beta_t)
\right],
```

oriented so larger values indicate poorer cross-modal fit. This is a non-novel
ProbVLM-style measurement instrument. The project selects the displayed
paper-faithful likelihood semantics, not the audited code's altered/clamped
residual implementation. The `1/d` coordinate mean and the full training-
objective weights are project choices; this freeze does not claim paper- or
code-exact training. A later executable specification must freeze the feature
transform, positivity map and floors, coordinate reduction, dropout/Monte-Carlo
inference rule, objective weights, and every numerical value. No original
ProbVLM checkpoint is implied or approved.

## Primary Matched Deterministic Comparator Freeze

`POINT-2ADAPTER-RECON` uses the same (u_v,u_t), independently verified
determinate-compatible fitting records, modality-specific mean-trunk
architecture, intra/cross target topology, fit/development partitions,
optimization schedule, early-stopping information, tuning budget, GGD score
family, target topology, and compatible-reference score standardization as the
primary instrument. It exposes only deterministic means

```math
m_v(u_v),\qquad m_t(u_t)
```

and uses global coordinatewise positive scale and shape constants
(\alpha_0,\beta_0) rather than input-dependent outputs. Those constants are
jointly fitted only on the same compatible fit/development reconstruction
objective and then frozen before any protected or intervention outcome is
opened. Its score is

```math
S_D(v,t)=\tfrac12\left[
\ell_{GGD}(u_t;m_v(u_v),\alpha_0,\beta_0)
+\ell_{GGD}(u_v;m_t(u_t),\alpha_0,\beta_0)
\right].
```

The unit-scale Laplace special case (\alpha_0=\beta_0=\mathbf1) is a required
sensitivity analysis, not the primary comparator. Both routes receive the same
selection supervision: fitting-set membership is defined prospectively by an
independent determinate-compatible rule (C_R^*=0). That membership is semantic
selection information and must be disclosed, while the underlying semantic
states and labels are not model inputs or loss targets. Constructed conflict
and control variants, model-error labels, protected outcomes, provenance, and
condition metadata are forbidden during fitting; at inference neither route
may receive construction metadata.

Removing the scale/shape heads changes active parameter count and gradient
paths. Therefore the primary comparison is a same-information, same-score-
family test of the complete routes, not a capacity-matched isolation of a
probabilistic mechanism. Exact active/trainable parameter counts, fit-time
compute, and inference cost must be reported for both routes; no capacity-parity
claim is permitted.

This is a scientific-interface freeze, not executable architecture approval.
The model owner must still approve the exact feature transform, dimensions,
layer widths, optimizer values, schedules, finite tuning grid, seeds, software,
and calibration procedure before Gate 0 can close.

## Required Attribution Ablation and Secondary Contrastive Baseline

The primary ProbVLM-versus-point comparison tests the complete probabilistic-
adapter route. A required frozen-means diagnostic holds the fitted ProbVLM mean
outputs fixed and replaces the input-dependent (\alpha,\beta) with the same
frozen global (\alpha_0,\beta_0) used by the deterministic comparator. This can
isolate only the direct contribution of input-dependent scale/shape through the
frozen score conditional on jointly trained means. It cannot identify their
training-path or causal contribution. Failure kills even that narrow direct-
score attribution; passing does not justify the broader mechanism claim.

`POINT-INFONCE` remains a secondary same-records contrastive baseline, not the
primary deterministic ablation. Before execution, its positive multiplicity,
denominator/reference pool, patient/source exclusions, semantic false-negative
mask, temperature rule, normalization, optimizer, and tuning budget must be
frozen without using protected outcomes. No CLIP-Adapter code is inherited.

## Score Standardization, Estimator, and Inference

For each method (m\in\{P,D\}), use the frozen compatible-reference transform

```math
Z_{ibm}=a_m\frac{S_{ibm}-\mu^{dev}_{0m}}{\sigma^{dev}_{0m}},
\qquad a_m\in\{-1,+1\}.
```

The orientation follows the method definition, not the observed protected-set
direction. Zero or unstable reference variance invalidates the score. Nonlinear
links cannot be changed after inspection.

For equally weighted complete patient blocks,

```math
\widehat\mu_{mj}
=\frac1n\sum_{b=1}^n(D_{C,bm}-|D_{j,bm}|),
\qquad
\widehat\psi_{mag,m}=\min_j\widehat\mu_{mj}.
```

For fixed strata, use the frozen stratum-weighted component means in the
statistical analysis plan. With finite fixed (\mathcal J_{id}), the plug-in
estimator is consistent; because the minimum is concave, it is generally
downward biased in finite samples. It is a minimum of control-specific sample
means, never a mean of per-block minima.

Inference remains the already specified whole-patient, common-index,
studentized max-(t) procedure with exactly 9,999 resamples and seed
`20270829`. Infer jointly on the smooth (\mu_{mj}) components, then derive

```math
L_{\psi,m}=\min_jL_{mj}.
```

Never bootstrap the non-smooth minimum directly. The material-advantage
functional is

```math
A_\psi=\psi_{mag,P}-\psi_{mag,D},
```

where each component is standardized by that method's own frozen compatible-
reference mean and standard deviation. Thus `A_psi` is a difference between
method-specifically standardized dimensionless effects, not a contrast in one
shared reference-SD unit. Its bounds must be derived from the joint method-by-
control component bounds exactly as specified in the statistical analysis plan;
raw-score and median/MAD sensitivities remain required.

## Falsification and Kill Rules

- Unreliable, score-informed, or non-independent (R_v,R_t) measurement kills
  the construct interpretation.
- Invalid, incomplete, semantically drifting, or artifact-recoverable
  intervention blocks kill or rebuild the affected design before promotion.
- Invalid task relevance or state preservation for the approved image/text
  controls blocks the primary specificity family.
- A simultaneous lower bound for `psi_mag` at or below the approved SESOI,
  unstable orientation/normalization, leakage, or a failed natural-ambiguity
  veto kills both the claimed narrow specificity interpretation and the current
  Main Track route.
- Failure of the approved `A_psi` material-advantage gate kills the current
  Main Track route. The qualified null or deterministic result must be retained
  without post-hoc repackaging. Non-superiority is not equivalence;
  deterministic subsumption requires the separate positive conditions in the
  statistical analysis plan.
- Failure of the frozen-means diagnostic kills any direct score-path
  attribution to input-dependent spread or shape. Passing cannot establish a
  training-path or causal mechanism.
- If the framework-level contribution is occupied or too narrow for the Main
  Track bar, stop the current route. Any later venue redirection requires a
  separate recorded decision; do not revive a killed estimator, reuse a failed
  claim, or create an unrecorded second research route.

## Permitted Claim

After a successful confirmatory gate, the strongest construct statement is:

> Within the pre-specified selected/evaluable determinate-source population,
> for frozen instrument (m) and the exact intervention/control versions, the
> simultaneous lower bound showed that the mean score response to assigned
> incompatible versus compatible assertions exceeded the mean absolute
> response to every approved image/text information-loss control by more than
> the approved compatible-reference-SD margin.

It must be followed by this boundary:

> This identifies an intervention-relative population score-response
> functional. It does not identify conflict for an arbitrary pair, causally
> separate natural ambiguity, estimate natural conflict prevalence, establish
> clinical benefit, or guarantee publication.

Natural ambiguity may only be reported as a pre-specified observational veto
that did or did not falsify the narrow specificity interpretation.

## Owner and Execution Boundary

| Boundary | Commander | Other required owners | Execution status |
| --- | --- | --- | --- |
| Method A as sole route | Approved | Scientific-supervisor approval of the sole-route/B-inactive boundary open; statistical and model owners open | Not executable |
| Partial-construct and intervention framework | Approved | Scientific supervisor aligned with primary-contribution framing; statistical owner open | Not executable |
| `PROBVLM-2ADAPTER` scientific interface | Approved | Scientific supervisor aligned with named role, not exact interface; model owner open | Not executable |
| `POINT-2ADAPTER-RECON` matched interface | Approved | Scientific supervisor aligned with named role, not exact interface; statistical and model owners open | Not executable |
| `POINT-INFONCE` secondary role | Approved | Scientific supervisor aligned with named role; statistical and model owners open; negative policy unresolved | Not executable |
| Task, data, readers, backbone, software, calibration, and resources | Open | Named owners open | Gate 0 blocked |

The next permitted action is explicit supervisor confirmation of the exact
scope and sole-route boundaries, plus owner reconciliation of this interface
together with the remaining Gate-0 task, data, intervention, inference, model,
reader, resource, and governance choices. A later bounded brief is required
even after Gate 0 closes; no experiment begins from this document alone.
