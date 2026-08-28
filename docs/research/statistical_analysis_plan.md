# Statistical Analysis Plan

**Status:** Gate-0 freeze candidate; no analysis is authorized

**Date:** 2026-08-29
**Evidence class:** Protocol and design-only power calculation

## Analysis Populations

- **`MV-1` task-relevance qualification population:** within official-train
  HMAC bucket 0--69, apply a separate governed
  `AINC/v1/mv1-qualification` HMAC rank before model fitting. Reserve the first
  128 strict-single-frontal metadata candidates in each positive/negative
  report-screen sampling stratum (256 total) and remove them from every
  fit/development, Month-3, confirmation, calibration, and target population.
  Qualification also remains disjoint from reader training and locked
  reliability sets. Report-screen polarity is a sampling aid, not image truth.
  The design requires at least 108 evaluable same-polarity sibling blocks in
  each independently assigned intact-image polarity after its frozen reader/
  intervention rules; a shortfall in either polarity stops `MV-1`, with no
  outcome-driven replacement or top-up beyond the ranked 256.
- **Fit/development population:** official-train HMAC bucket 0--69 only; used
  to fit, orient, normalize, tune, and freeze candidates only after the nested
  qualification reserve above is removed.
- **Month-3 primary-candidate screen:** official-train HMAC bucket 70--84,
  opened once after the Gate-0-approved exact uncertainty-aware estimator and
  matched deterministic comparator have been fit/tuned only in development and
  their fitted instances, normalizers, orientations, code, and configurations
  are locked; used only to kill or provisionally advance those already frozen
  instances. Nothing is selected or refit there, and it cannot supply
  confirmatory evidence.
- **Construct-confirmatory population:** untouched patients with complete,
  independently accepted paired intervention blocks from official-train HMAC
  bucket 85--99. Exactly one keyed source block per patient is mandatory; all
  variants remain paired within that block.
- **Natural-ambiguity audit population:** independently labelled, otherwise
  adequate natural cases satisfying frozen overlap. It is observational and
  never enters the identified primary control family without a separately
  approved identification argument.
- **Target population:** a separate natural, patient-separated cohort for
  error risk, calibration, and decision endpoints. Balanced intervention-cell
  frequencies never stand in for target prevalence.

Patient/source partitioning occurs before variant creation. Eligibility is
decided without candidate scores. A missing sibling makes the primary source
block incomplete; it is not imputed or converted into a zero response.
Every primary block contains its compatible, conflict, and all primary control
variants on the same source unit; the magnitude endpoint is not formed by
subtracting effects from unmatched source populations.

## Frozen Score Orientation and Scale

For method `m`, orient higher values toward greater conflict using the method
definition, not the observed kill-set direction. On a disjoint,
patient-weighted development-compatible reference set, freeze:

```math
Z_{ibm}=a_m\frac{S_{ibm}-\mu^{dev}_{0m}}{\sigma^{dev}_{0m}},
\qquad a_m\in\{-1,+1\}.
```

One unit is one compatible-reference score standard deviation. The reference
patients, weights, location, scale, score version, and orientation are frozen
before evaluation. Zero or numerically unstable reference variance invalidates
the score. Raw-scale estimates and a median/MAD normalization are mandatory
sensitivity reports; neither may replace the primary scale after inspection.

For complete source block `b`:

```math
D_{C,bm}=Z^{conflict}_{bm}-Z^{compatible}_{bm},
\qquad
D_{j,bm}=Z^{j}_{bm}-Z^{reference(j)}_{bm}.
```

Every control has a frozen within-source reference. Averaging over variants
occurs within the patient block before population inference.

## Primary Construct Endpoint

The current signed endpoint is retained as a secondary diagnostic:

```math
\psi_{id,m}
=\min_j\{\mathbb E[D_C]-|\mathbb E[D_j]|\}
=\min_{j,s\in\{-,+\}}\mathbb E[D_C+sD_j].
```

It can pass when large positive and negative nuisance responses cancel. The
recommended freeze candidate therefore makes the magnitude-safe endpoint
primary:

```math
\psi_{mag,m}=\min_{j\in\mathcal J_{id}}
\mathbb E[D_C-|D_j|].
```

`J_id` contains only randomized or valid counterbalanced controls. Its proposed
Month-3 cardinality and modality roles are one image-information-loss contrast
`M_v` and one text-information-loss contrast `M_t`, each on the complete source
block. TB-0005 supplies the exact proposed `MV-1`/`MT-1` operations, severities,
acceptance rules, and within-source references, but owner approval and the
separate `MV-1` task-relevance qualification remain unresolved; consequently
the family is not executable and the two-control power grid is conditional.
Surface-form, unselected missingness, and unrelated-finding probes are
additional diagnostics and cannot substitute for either modality. A four-
control confirmatory family is permissible only if all four exact identities
and intervention-validity rules are approved before scores are inspected;
otherwise the permitted claim names only the approved `M_v` and `M_t` roles.
Natural image or text ambiguity remains `gamma_A`, a separate veto-only
falsification audit.

### Model-independent `MV-1` task-relevance qualification

Pixel removal and a visible resampling signature do not by themselves show
that `MV-1` attenuates evidence relevant to the pleural-effusion task. On a
prospectively sampled qualification population disjoint from fit/development,
Month 3, and confirmation, counterbalance reader/panel assignment across
sibling state and source polarity. Let `pbar_intact,b` and `pbar_MV-1,b` be the
mean `0--1` presence probabilities from disjoint five-reader image-only panels
for patient block `b`. Both siblings must independently retain complete prescribed
coverage, a determinate state, and the same polarity. Define:

```math
q_b=|\bar p_{intact,b}-0.5|-|\bar p_{MV-1,b}-0.5|,
\qquad q_{v,y}=\mathbb E[q_b\mid Y_v=y],
\qquad q_{v,bal}=\tfrac12(q_{v,present}+q_{v,absent}).
```

The candidate qualification rule is a patient-clustered one-sided 95% lower
bound for `q_v,bal` **strictly above `0.10`**, with at least 108 evaluable
patient blocks in each independently assigned image polarity. This requires a non-trivial movement
toward evidential indifference without changing the independently assigned
finding state. The threshold is a prospective design choice, not a clinical
constant, and no candidate-model representation or score may enter eligibility,
qualification, or severity choice.

Because each polarity stratum's `q_b` is bounded in `[-0.5,0.5]`, its worst-case
SD is `0.50`. For the equal-weight mean of two independent stratum means,
one-sided `alpha=0.05`, 90% power, null boundary `0.10`, and planning truth
`0.20` give a crude normal-approximation minimum of 108 evaluable independent
patient blocks per polarity (216 total).
Patient-clustered simulation of the complete disjoint-reader pipeline,
attrition, selection into the same-polarity population, counterbalanced panel
assignment, and reader severity/dependence
must replace that approximation before an annotation brief. Gate-0 approval
can freeze this rule; only a later authorized qualification exercise can pass
it. Failure means `MV-1` is merely fixed resolution attenuation, cannot complete
primary `J_id`, and triggers the pre-specified stop/reopen rule.

### Candidate construct thresholds

All thresholds are proposals requiring approval:

- specificity SESOI: `delta_specificity = 0.20` compatible-reference SD;
- sensitivity values: `0.15`, `0.25`, and `0.30`;
- scale-free sensitivity statistic:
  `theta = min_j {P(D_C > abs(D_j)) + 0.5 P(D_C = abs(D_j))}`, with `0.60` as a
  descriptive candidate threshold; it is not a promotion co-gate unless a
  separate multiplicity and power decision is approved;
- expected direction: every primary conflict contrast is positive;
- nuisance recoverability is governed by the separate artifact-probe design
  below; design balance plus diagnostic veto is recommended at current floors,
  while any formal orientation-safe `chance +/- 0.05` bounded-probe claim is
  feasibility-blocked and never silently assumed to pass.

The 0.20 threshold is a design choice that rejects very small standardized
separations; it is not an empirically or clinically validated constant.
Sensitivity results cannot rescue failure of the approved primary threshold.

## Deterministic Subsumption Rule

For the strongest capacity-, input-, supervision-, and tuning-matched
deterministic predictor, define:

```math
A_\psi=\psi_{mag,uncertainty}-\psi_{mag,deterministic}.
```

The proposed material-advantage margin is `0.10` reference SD, with `0.05` and
`0.15` as sensitivity values.

- An uncertainty-aware Main Track estimator candidate advances only if the
  simultaneous lower bound for `A_psi` exceeds `+0.10`.
- Deterministic non-inferiority is established only if the simultaneous upper
  bound for `A_psi` is below `+0.10` and the deterministic method itself passes
  the absolute `psi_mag > 0.20` gate.
- Formal construct equivalence is confirmatory only and requires a 95% two-
  sided simultaneous equivalence interval wholly inside `[-0.10,+0.10]`,
  corresponding to the two one-sided `alpha_F=0.025` confirmation tests.
- “Not statistically superior” is inconclusive, not equivalent or subsumed.
- Subsumption additionally requires deterministic non-inferiority on the
  separately frozen downstream proper-score endpoint.

This logic follows the distinction between superiority and equivalence; it
does not manufacture a deterministic win from an underpowered comparison.

## Intervals and Multiplicity

1. Use exactly one keyed eligible source study/block per patient for Month 3
   and confirmation, resample whole patients, and preserve finding-polarity
   blocks. Paired variants never increase the independent sample size. Any
   multi-study primary design requires an amended brief, design-effect model,
   and new power table.
2. Use a studentized patient-cluster max-`t` multiplier/bootstrap with at
   least 9,999 fixed-seed resamples. Recompute all endpoint components and
   method differences on the same resamples; do not refit the frozen
   development normalizer.
3. Report simultaneous component bounds and take their minimum as the bound
   for the intersection claim. For signed `psi_id`, report both smooth
   components `E[D_C-D_j]` and `E[D_C+D_j]` for every control.
4. Gate 0 must already name exactly one primary uncertainty-aware estimator
   definition/interface and one matched deterministic comparator definition.
   Before the Month-3 set is opened, development bucket 0--69 may fit/tune only
   within those frozen rules and must lock exactly one fitted instance of each.
   Month 3 can kill or provisionally advance only those instances; every other
   method is secondary and cannot be promoted by being the best observed
   holdout result. A change of estimator identity reopens Gate 0; an expanded
   primary method family requires a prospective contract amendment and revised
   power grid before any protected set is opened.
5. Month 3 uses one-sided 90% simultaneous screening bounds, family
   `alpha_F=0.10`, and 80% target family power. It cannot establish
   confirmatory evidence, non-inferiority, or equivalence.
6. Confirmation uses the same frozen estimator identity and prospectively
   locked fitted instance, untouched patients, one-sided 97.5% simultaneous
   bounds, `alpha_F=0.025`, and 90% target family power.
7. Claims follow a fixed sequence: construct specificity; material advantage
   over the matched deterministic predictor; downstream proper-score
   increment; fixed-budget decision value. A failed rung stops promotion.
8. Secondary methods/subgroups use Holm or Romano--Wolf familywise control.
   False-discovery-rate control cannot promote a secondary result to the
   primary claim.

## Design-Only Power Bound

For magnitude component
`mu_j = E[D_C - abs(D_j)]`, power is for the componentwise standardized excess
above the SESOI, not the effect above zero:

```math
d_*=\min_j\frac{\mu_j-\delta_{specificity}}{\sigma_j},
```

where `sigma_j` is the source-block SD of component `j`. This definition avoids
assuming that the smallest mean and largest variance occur in the same
component. With `J` primary magnitude components, set `K=J`; the conservative
union-bound planning calculation is:

```math
n_{eff}=\left\lceil
\frac{[z_{1-\alpha_F/K}+z_{1-(1-power_F)/K}]^2}{d_*^2}
\right\rceil.
```

The full reproducible grid is in
[`reports/tables/gate0_power_sensitivity.csv`](../../reports/tables/gate0_power_sensitivity.csv).
For the candidate assumption that the least favourable standardized component
has `mu_j=0.45`, `delta=0.20`, and `sigma_j=1`, hence `d_*=0.25`:

| Stage | Controls | Analytic minimum | Screened at 15% loss | Proposed operational floor |
| --- | ---: | ---: | ---: | ---: |
| Month-3 development | 2 | 138 | 163 | 216 balanced evaluable / 260 screened |
| Confirmatory construct | 2 | 242 | 285 | 320 evaluable / 380 screened |
| Confirmatory construct | 4 | 318 | 375 | 400 evaluable / 470 screened |

These are planning bounds, not observed effect, variance, attrition, or
sample-size facts.

At `d_*=0.20`, the analytic minimums become 215, 378, and 497. The operational
floors therefore do not guarantee power when the least favourable standardized
excess is smaller than assumed; that outcome reopens the sample/budget decision.
The CSV reports screening sensitivity at 10%, 15%, 20%, and 30% eligibility/QC
loss. Exactly one primary block per patient is frozen, so no clustering design-
effect grid is claimed. Clinical indeterminacy, invalid intervention, and
incomplete sibling families are eligibility failures, not ordinary random
attrition.

### Material-advantage power sensitivity

For the one pre-specified uncertainty-aware candidate and its matched
deterministic comparator, define the standardized excess over the `0.10`
material-advantage margin as:

```math
d_A=\frac{A_{\psi,true}-0.10}{\sigma_A},
```

where `sigma_A` is the patient-block standard deviation/influence scale of the
paired `A_psi` estimator under the frozen joint resampling procedure. With one
primary comparison and the fixed-sequence gate, `K=1`; the same normal planning
formula applies with `d_A`. The CSV reports sensitivity rows. At
`d_A=0.15/0.20`, the analytic requirements are 201/113 patients for Month 3
and 467/263 for confirmation, before loss. The 216/320 operational construct
floors therefore cover this rung only under explicit standardized-advantage
assumptions. The observed covariance, the non-smooth minimum, or a larger
primary method family requires simulation and a revised grid before execution.

## Artifact-Condition Recoverability Audit

The candidate primary probe family contains four condition-recovery views for
`conflict` versus `compatible`: image-only; text-only; structured nuisance-only
(length, punctuation, polarity/template, view and rendering descriptors); and
provenance/process-only. Each exact feature set, transparent/flexible model
class, capacity/tuning budget, orientation rule, permutation calibration, and
missing-value rule remains a Gate-0 freeze item. A weak probe is not evidence
of artifact absence.

### Design-first invariant

The recommended Gate-0 option is exact structural balance plus a diagnostic
probe veto, not a global artifact-equivalence prerequisite at the construct
sample floors. Within every patient partition:

1. each exact clear image is paired with both approved text polarities under
   equal weights;
2. each exact atomic string/template/polarity and recorded process path is
   crossed equally over image-positive and image-negative source blocks;
3. editor/reader pool, renderer, filename, order, punctuation/length strata,
   and provenance are randomized or exactly balanced independently of `C*`;
4. every sibling stays in its patient block, and failure of a required sibling
   removes or prospectively reconstructs the entire block; and
5. byte-level and row-level balance is verified from the construction manifest
   before any estimator or probe score is evaluated.

This controls the enumerated empirical marginals by construction. It does not
prove equality of all latent feature distributions or exclude interaction
artifacts. Frozen probes audit implementation failure and residual
recoverability:

- fit, tune, and orient them only on the 70% development pool, including the
  complete tuning pipeline in fixed-label-permutation diagnostics;
- open the Month-3 pool once for the frozen development screen and never refit
  there; reserve the untouched confirmation pool for later inference;
- use patient-level blocks and the same complete-case rule as the construct
  endpoint; and
- include every pre-specified model/feature variant in the frozen family.

These conflict-versus-compatible probes do not validate the `M_v` or `M_t`
arms. The manipulated modality is intentionally different and may trivially
identify its information-loss arm. For each control arm, separately require
exact identity of the non-target modality, identical source/process/provenance
paths, the frozen severity/reader gate, and an arm-specific audit that excludes
the manipulated modality. Any hidden condition field or process-only recovery
kills that control; recovery from the intentionally altered modality is
reported as manipulation fidelity, not leakage. The estimator's response to
the altered modality remains the primary `abs(D_j)` nuisance penalty.

For raw held-out balanced accuracy `BA_j`, define orientation-safe
recoverability:

```math
R_j=0.50+|BA_j-0.50|=\max(BA_j,1-BA_j).
```

A raw `BA_j` well below 0.50 remains recoverable after label flipping and must
not pass. A lower bound for any `R_j` above 0.55 is instrument failure. An
interval crossing 0.55 is inconclusive. An upper bound strictly below 0.55
supports only bounded recoverability for that exact frozen probe algorithm,
feature view, and population—not artifact absence, distributional equality,
Bayes unrecoverability, or transfer.

Under the recommended diagnostic-veto option, demonstrated recovery kills the
instrument, but failure to demonstrate recovery is not an equivalence pass.
The route may advance only with the narrower construction-balance and exact-
probe report. This choice requires Commander/statistical approval in the
[decision dossier](gate0_decision_dossier.md).

### Optional powered bounded-probe claim

If a formal four-probe statement is required, define the global claim and null
as:

```math
H_1:\max_j R_j<0.55,
\qquad
H_0:\max_j R_j\geq0.55.
```

Equivalently, every raw `BA_j` must be strictly inside `(0.45,0.55)`. This is a
conjunctive intersection--union decision: each component equivalence test may
use the stage's nominal alpha without alpha/K correction for the global Type-I
error, while joint power remains a separate design requirement. With `K=4`, a
centered Bernoulli-like approximation, truth `BA=0.50`, two-sided equivalence,
and conservative beta allocation over `2K` directional failures uses:

```math
n_{IUT}=\left\lceil
\frac{[z_{1-\alpha_F}\sqrt{0.55(0.45)}+
z_{1-(1-power_F)/(2K)}\sqrt{0.50(0.50)}]^2}{0.05^2}
\right\rceil.
```

This gives illustrative minima of 1,047 Month-3 and 1,757 confirmatory
independent patients, or approximately 1,232 and 2,068 screened at 15% loss.
The 1,047 figure is only a non-promotable developmental bounded-recoverability
screen: Month 3 cannot establish equivalence or turn an artifact result into
confirmatory evidence. Only a later untouched confirmatory design could
support the bounded four-probe statement, and only after the complete patient-
clustered probe-selection pipeline is simulation-powered.
Linear scaling of the current reader worksheet gives approximately 1,302
clinical hours through Month 3 and 2,657 hours for the confirmation row alone;
this is an unverified planning approximation. The former exceeds the revised
500-hour stage ceiling, while the confirmation row alone exceeds the 1,350-hour
cumulative ceiling.
If separately simultaneous two-sided component intervals are required,
replacing `alpha_F` with `alpha_F/(2K)` gives crude minima of 1,756 and 2,463
before loss. These replace the older orientation-unsafe one-sided
1,293/1,976 approximation.

All of these calculations omit balanced-accuracy stratification,
trained-probe/tuning variability, patient dependence, permutation calibration,
the folded non-smooth statistic, and model selection. A patient-clustered
simulation of the complete pipeline is mandatory before a powered claim. The
present 216/320-or-400 construct floors cannot certify `chance +/- 0.05`
bounded-probe equivalence. A wider margin requires a prospective
consequence-based bias argument; budget convenience is not a justification.

## Downstream Risk, Calibration, and Decision Candidates

These values remain approval-blocked until error prevalence, model complexity,
target sampling, and clinical review costs are frozen. The construct power
grid cannot be reused for them.

- Outcome `H`: independently labelled image-grounded binary task error from a
  frozen model; an overconfidence subgroup cannot define the primary outcome.
- Proper-score endpoint for method `m`: paired Brier-skill increment of its
  augmented risk model over the frozen baseline on the natural target cohort,
  `Delta_BSS_m = (BS_base - BS_augmented,m) / BS_null`. `BS_null` is the
  weighted target-test Brier score of a constant event probability estimated
  and frozen on the approved development/calibration population; its
  transport/weighting rule is fixed before final evaluation.
- Candidate Brier-skill SESOI: `0.02`, sensitivity values `0.01` and `0.05`;
  candidate method-difference equivalence band `[-0.01,+0.01]`.
- For the same primary uncertainty-aware method and matched deterministic
  comparator, define
  `A_BSS = Delta_BSS_uncertainty - Delta_BSS_deterministic`, so positive values
  favour the uncertainty-aware component. Its advancement requires both the
  uncertainty-aware method's lower bound for `Delta_BSS` above `0.02` and the
  one-sided 97.5% simultaneous lower bound for `A_BSS` above `+0.01`.
  Deterministic downstream
  non-inferiority requires the corresponding upper bound below `+0.01` and the
  deterministic method's own lower bound for `Delta_BSS` above `0.02`.
  Confirmatory equivalence requires a 95% two-sided simultaneous interval for
  `A_BSS` wholly inside `[-0.01,+0.01]`. This test follows construct validity in
  the fixed sequence and uses the same frozen primary method identity.
- Calibration candidates: absolute calibration-in-the-large error at most
  `0.02` probability and calibration slope inside `[0.80,1.20]`, demonstrated
  by equivalence intervals rather than favourable point estimates. These are
  planning tolerances, not clinical safety limits.
- Decision candidate: task error risk at 90% answer coverage (10% review),
  compared at the same review budget; candidate SESOI `0.01` absolute risk.
  Report the full risk--coverage curve, but do not select another coverage
  after final evaluation.

A separate target-cohort calculation must account for outcome event rate,
paired proper-loss variance and covariance for `Delta_BSS`/`A_BSS`,
calibration-model parameters, calibration sample, review policy, and subgroup
minima. Until those values, the primary method family, and its multiplicity are
approved, H3/H4 and downstream deterministic subsumption are not power-ready;
Gate 0 cannot be represented as closed.

## Missingness, Deviations, and Stop Rules

- Freeze eligibility and exclusion reason codes before any candidate score is
  computed; report cohort flow and every missing sibling.
- No endpoint switching, threshold tuning, normalizer refitting, or method
  replacement follows evaluation inspection.
- Too few independent patient blocks yields `inconclusive`, not a favourable
  null or equivalence result.
- Kill or redesign the score if `psi_mag` fails, direction reverses, a nuisance
  probe demonstrates leakage, or results depend materially on the frozen
  normalization sensitivity. `theta` is a scale-free sensitivity report and
  cannot rescue failure; it becomes a gate only after separate power approval.
- Kill the Main Track estimator claim if the uncertainty-aware method fails
  the `+0.10` material-advantage gate over deterministic; declare deterministic subsumption
  only when its positive conditions are actually met.
- Do not reuse Month-3 patients, covariance estimates, thresholds, or
  advance/kill outcomes as untouched confirmatory evidence.

## Methodological Anchors

- Gneiting and Raftery,
  [Strictly Proper Scoring Rules, Prediction, and Estimation](https://doi.org/10.1198/016214506000001437).
- Romano and Wolf,
  [Exact and Approximate Stepdown Methods for Multiple Hypothesis Testing](https://doi.org/10.1198/016214504000000539).
- Schuirmann,
  [two one-sided tests for equivalence](https://pubmed.ncbi.nlm.nih.gov/3450848/).
- Lopez-Paz and Oquab,
  [classifier two-sample testing](https://arxiv.org/abs/1610.06545), and Ojala
  and Garriga,
  [classifier permutation testing](https://www.jmlr.org/beta/papers/v11/ojala10a.html).
- Eaton and Muirhead,
  [intersection--union testing](https://doi.org/10.1016/j.jspi.2007.03.021).
- Eldridge, Ashby, and Kerry,
  [sample-size effects of unequal cluster size](https://pubmed.ncbi.nlm.nih.gov/16943232/).
- Riley and colleagues,
  [minimum sample size for binary prediction models](https://www.bmj.com/content/368/bmj.m441).

These sources motivate methods, not the project's unapproved numerical
thresholds.
