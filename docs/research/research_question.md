# Research Question and Falsifiable Hypotheses

**Status:** Method A is Commander-approved; the supervisor is aligned with the
intervention framework and named roles, while formal sole-route co-approval,
the exact task, estimand package, executable specification, and remaining
owner approvals remain open

## Narrow Research Question

For one image-grounded atomic clinical finding, can a prospectively frozen
cross-modal score respond specifically when a determinate auxiliary assertion
opposes the independently judged image state rather than under the approved
image/text information-loss controls, survive a separate natural-ambiguity
veto audit, and add held-out prediction of a frozen model's task error at a
fixed review budget?

## Intended Claim Structure

**Central claim to test.** The Method-A partial-construct, intervention-
identified measurement and inference framework can use independent modality-
specific semantic measurements to test whether a frozen score is specifically
responsive to determinate incompatibility rather than approved modality-
specific information-loss controls. Natural ambiguity remains a separate
veto-only audit. The framework must not be represented as an output-only,
pair-level conflict identifier.

**Downstream support claims to test.** If the intervention-relative specificity
gate passes, the frozen instrument score provides non-redundant calibrated
information and selective-review value beyond unimodal ambiguity measures, ordinary
confidence, epistemic uncertainty, output uncertainty, and matched
deterministic failure predictors.

These are hypotheses, not results. The downstream claims support the central
contribution and cannot substitute for failed construct identification.

## H1 — Conflict Specificity

**Hypothesis.** When a task-relevant atomic assertion is counterbalanced to
oppose rather than match a determinate, independently judged image state, the
pre-specified frozen score changes in the expected direction and more
strongly than under the valid randomized or counterbalanced `M_v` and `M_t`
information-loss controls. Semantic-preserving form variants are prospectively
counterbalanced and evaluated as artifact diagnostics, not inserted into the
primary `J_id` family. Natural-ambiguity comparisons are governed separately by
H2's identification boundary.

**Null interpretation.** If the response is equally explained by image
quality, text length, source identity, prevalence, embedding norm, or generic
pair dissimilarity, the intervention-relative specificity interpretation fails.

## H2 — Separation from Unimodal Ambiguity

**Hypothesis, identified form.** Under a valid governed ambiguity intervention,
or a separately justified conditional-exchangeability and transport estimand,
the determinate conflict contrast exceeds the corresponding image-only and
text-only ambiguity contrasts by the frozen smallest effect. Ambiguity cases
retain distinct labels and are not forced into a binary compatibility state
when that relation is undefined.

**Protocol boundary.** Matched or weighted natural-ambiguity differences are
conservative falsification audits only. Passing them cannot establish causal
separation from ambiguity; without a valid identification route, H2 remains
unresolved and the permitted claim narrows to determinate-conflict specificity.

**Null interpretation.** If a common undifferentiated uncertainty factor
explains all conditions, the proposed decomposition is not supported even if
the score detects corrupted or difficult examples.

## H3 — Held-Out Incremental Validity and Calibration

**Hypothesis.** Adding the frozen instrument score to a baseline risk model
for independently labelled image-grounded task error improves a pre-specified
held-out proper score by more than the smallest effect of interest and
preserves acceptable calibration under one declared shift.

**Null interpretation.** If the gain disappears with patient-level splitting,
repeated seeds, recalibration, or a matched deterministic failure predictor,
the frozen score is redundant for outcome-risk prediction.

## H4 — Fixed-Budget Decision Value

**Hypothesis.** At an equal review budget or answer coverage, a policy using
the calibrated decomposition has lower selective risk or regret than policies
using ordinary confidence, output uncertainty, or the matched deterministic
failure/risk predictor.

**Null interpretation.** If benefit depends on post-hoc thresholds,
unrealistic review costs, or information unavailable at decision time, no
decision-value claim is permitted.

## Candidate Construct and Validation Estimands

For independently elicited image-only and text-only interpretation
distributions \(\pi_v,\pi_t\), a candidate semantic-distribution discrepancy
is:

```math
\kappa_L(v,t)=
\mathbb E L(Y_v,Y_t)
-\frac12\mathbb E L(Y_v,Y_v')
-\frac12\mathbb E L(Y_t,Y_t').
```

With binary states and disagreement loss this reduces to
\((p_v-p_t)^2\). It is energy-distance-like and is not automatically novel.
It is not binary conflict: for example, \(p_v=0.5,p_t=1\) yields a positive
value although \(C^*\) is undefined. Outside determinate cells it is only a
distribution-discrepancy diagnostic, and its interpretation depends on whether
blinded reader distributions validly measure task-relevant semantics.

For candidate score \(S_m\), the signed kill-stage diagnostic uses only valid
randomized or counterbalanced within-source controls:

```math
\tau_{C,m}=\mathbb E[S_m^{conflict}-S_m^{compatible}],
\qquad
\psi_{\mathrm{id},m}=
\min_{j\in\mathcal J_{\mathrm{id}}}
(\tau_{C,m}-|\tau_{j,m}|),
```

but this signed form can conceal bidirectional nuisance responses. The
recommended primary freeze candidate is:

```math
\psi_{\mathrm{mag},m}=
\min_{j\in\mathcal J_{\mathrm{id}}}
\mathbb E[D_{C,m}-|D_{j,m}|].
```

where \(\mathcal J_{\mathrm{id}}\) initially contains valid paired
information-loss controls \(M_v,M_t\) and includes ambiguity only if its
intervention and reference are governed and valid. A pre-specified
matched/weighted natural-ambiguity difference \(\gamma_{A_q,m}\) is reported
separately and does not enter either specificity endpoint. The reference
populations, overlap rule, weights, score, scale, aggregation, simultaneous
interval, positive smallest effect, and multiplicity rule must be frozen before
outcomes are inspected.

Compatibility is defined only when both independently judged modality states
are determinate. Ambiguous or missing cases are controls, not silently coded
compatible examples. The full definition, assumptions, alternatives, and kill
rules are recorded in the [task and estimand packet](task_estimand_options.md)
and [statistical analysis plan](statistical_analysis_plan.md).

## Claim Ladder

1. association;
2. intervention-relative measurement validity;
3. held-out incremental validity;
4. probabilistic calibration in the tested population;
5. retrospective decision value;
6. clinical value only after separate governed human/prospective evidence.

No result may skip a rung by changing terminology.
