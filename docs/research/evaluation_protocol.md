# Evaluation Protocol

**Status:** Protocol scaffold; primary endpoint awaits Gate 0

## Evaluation Principle

Task performance, construct validity, uncertainty quality, calibration,
robustness, and decision utility are different outcomes. Improvement in one
does not establish another.

## Evaluation Sequence

1. Validate conflict specificity under controlled interventions.
2. Test incremental prediction of a frozen task-relevant model error.
3. Assess calibration in-domain and under one pre-specified shift.
4. Evaluate selective decisions at an equal review budget or answer coverage.
5. Consider clinician-in-the-loop evaluation only after separate approval.

## Candidate Risk Model

For a pre-specified binary failure outcome \(H_i\), a transparent analysis
object is:

```math
H_i \sim \operatorname{Bernoulli}(r_i),
```

```math
\operatorname{logit}(r_i)
= \alpha
+ \beta_{av} A_{v,i}
+ \beta_{at} A_{t,i}
+ \beta_{mv} M_{v,i}
+ \beta_{mt} M_{t,i}
+ \beta_c C_{vt,i}
+ \beta_e U_{\mathrm{epi},i}
+ \beta_o U_{\mathrm{out},i}
+ b_{\mathrm{model}[i]}
+ b_{\mathrm{finding}[i]}.
```

This is a candidate analysis, not a commitment to Bayesian logistic
regression. Conflict must be judged by held-out prediction and decision value,
not an in-sample coefficient alone.

## Outcome Families

| Property | Required evidence |
| --- | --- |
| Construct validity | Paired conflict contrast, specificity against ambiguity/corruption controls, severity trend, artifact audit |
| Task performance | Frozen task loss or accuracy with patient-clustered intervals |
| Probabilistic quality | NLL or another proper score; Brier score for binary risk |
| Calibration | Intercept, slope, reliability curve, subgroup calibration; ECE only as secondary evidence |
| Ranking | AUROC and AUPRC with prevalence reported |
| Selective prediction | Risk--coverage curve, area under curve, risk at fixed coverage, coverage at fixed risk |
| Decision value | Expected utility or regret under frozen review budget and loss table |
| Robustness | Paired change under declared shift, subgroup, model, and intervention source |

## Statistical Design

- Split by patient before variant creation; all derived pairs inherit the
  source split.
- Keep development, calibration, and final evaluation roles distinct.
- Freeze the primary outcome, smallest effect of interest, confidence or
  credible interval, and multiplicity family before confirmatory evaluation.
- Use paired bootstrap intervals clustered at patient level or a justified
  hierarchical model for repeated findings and variants.
- Repeat stochastic training or inference with pre-specified seeds; report
  per-run results and paired differences.
- Estimate incremental value by comparing nested frozen predictors on the same
  test cases, including calibration after the same calibration budget.
- Report effect sizes and intervals, not only significance tests.
- Pre-specify subgroup minimum sizes and suppress unsafe or uninterpretable
  estimates.
- Publish null results, failed conditions, missing outcomes, exclusions, and
  protocol deviations.

## Target-Distribution Rule

The balanced controlled-intervention set identifies constructs; it does not
represent the prevalence of conflict, ambiguity, or model error in a target
population. NLL, Brier score, calibration curves, decision utility, and review
budgets therefore require a separately defined target-distribution cohort.

The preferred design samples a patient-separated natural cohort using frozen
inclusion rules and evaluates naturally occurring outcomes without balancing
intervention cells. If outcome enrichment or case--control sampling is
necessary, the sampling probabilities and target prevalence must be specified
before evaluation and used in a justified weighting or recalibration analysis.
Unweighted calibration or utility on a deliberately balanced synthetic set may
be reported only as a stress test, never as target-population risk.

## Calibration Design

Calibration data must not overlap development or final evaluation patients.
Post-hoc calibration is applied with the same method and budget to all eligible
comparators. Aggregate ECE cannot be the primary calibration evidence because
it depends strongly on binning and can hide subgroup miscalibration.

A conflict score is not a probability of error until a risk mapping is trained
and evaluated. Calibration under a shifted distribution must be described as
observed robustness, not as a universal guarantee.

## Selective Decision Design

The first decision comparison should remain narrow:

```text
answer | human_review
```

Optional clarification or verification actions require a task in which their
cost and new information are explicitly defined. A candidate rule is:

```math
d_i^*=\arg\min_{d\in\mathcal A}
\mathbb E[L(d,H_i)\mid\text{available evidence}].
```

Thresholds, action costs, and information available at decision time must be
frozen before final evaluation. Human review is not perfect, immediate, or
cost-free. Compare policies at equal review budget, equal answer coverage, or
under the same loss table.

## Promotion Rules

- **To risk prediction:** measurement passes the construct gate.
- **To calibration claim:** held-out risk adds more than the smallest effect and
  calibration meets the frozen tolerance.
- **To decision claim:** the policy improves the primary fixed-budget endpoint
  with paired uncertainty and no material pre-specified subgroup regression.
- **To clinician study:** computational findings replicate and a separate
  human-factors and governance protocol is approved.

If ordinary confidence or a matched deterministic predictor subsumes
\(C_{vt}\), report the result and narrow the claim. Do not select a favourable
subgroup, threshold, or alternative primary score after final evaluation.
