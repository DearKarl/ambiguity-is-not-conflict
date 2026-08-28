# Reader Measurement and MV-1 Qualification Audit

**Status:** Exact pre-execution design candidate; owner, clinical, governance,
resource, and later simulation decisions remain open

**Audit date:** 2026-08-29
**Evidence class:** Protocol and deterministic synthetic design arithmetic
under TB-0008; no reader, record, dataset, model, or experiment was accessed

## Executive Decision

Independent reader measurement is upstream of both surviving project choices.
Without a defensible measurement instrument for \(Y_v,Y_t,A_v,A_t,M_v,M_t\),
neither \(C^*\) nor the controlled `psi_mag` functional is interpretable.

This audit recommends two finite packages:

1. **`G0-READERS A`:** use nominal Krippendorff alpha as the primary
   multi-reader reliability coefficient for every categorical gating axis,
   retain the existing point/lower-bound/agreement thresholds, add exact
   allocation, cluster-bootstrap, missingness, repeat, and hierarchical
   sensitivities, and state that the reliability evidence applies only to the
   locked instrument and populations tested.
2. **`G0-MV-Q A`:** increase the metadata reservation from 128 to **150
   candidates per report-screen stratum** (300 total), retain at least 108
   evaluable blocks per independently assigned image polarity, and qualify
   `MV-1` only if a joint one-sided family shows
   \(q_{v,bal}>0.10\), \(q_{v,present}>0\), and
   \(q_{v,absent}>0\).

Neither package is approved. The existing 150-unit reliability set remains
precision-unverified until the specified synthetic simulation passes. The
`MV-1` result, if later obtained, would apply to the selected/evaluable
population measured by the locked finite reader roster; it would not establish
clinical benefit, natural-image ambiguity, reader-population generalization,
or task relevance outside that population.

## Facts, Inferences, Assumptions, and Recommendations

### Repository facts

- The current protocol proposes five independent image ratings, disjoint
  sibling panels, a 150-unit locked reliability phase, a 15% repeat fraction,
  and fixed reliability thresholds, but it does not select the primary
  coefficient or supply the required precision calculation.
- The current `MV-1` gate uses disjoint five-reader panels and at least 108
  evaluable blocks per image polarity. The 108 floor is explicitly a crude
  worst-case normal approximation.
- The current metadata plan reserves 128 report-screen-positive and 128
  report-screen-negative candidates. Report-screen polarity is not independent
  image truth, and no eligibility or yield has been observed.
- All current counts, time rates, roster sizes, qualifications, access rights,
  and ethics/resource availability are unverified planning candidates.

### Audit inferences

- Conditioning on intact/transformed siblings that both retain a determinate,
  same-polarity state changes the target. The primary estimand is a
  **selected/evaluable-population** attenuation, not an all-candidate or
  all-patient effect.
- Reusing a finite reader roster across patients induces reader dependence.
  Patient resampling is valid only for an inference explicitly conditional on
  that locked roster and its counterbalanced assignment schedule.
- A balanced mean can hide harm in one polarity. Polarity-specific positive
  guardrails are therefore required alongside the `q_v,bal` margin.
- Reserving only 128 candidates per report-screen stratum is fragile: even
  under perfect polarity screening and independent equal yield, the joint
  probability of obtaining 108 evaluable blocks in both strata is only
  `0.404356` at 85% pair yield.

### Synthetic assumptions

The generated yield table assumes perfect report-screen polarity, equal and
independent pair evaluability, independent candidates, and no reader or source
clustering. These assumptions are deliberately optimistic and are not facts
about MIMIC-CXR or `MV-1`.

### Recommendations, not approvals

The allocations, coefficients, thresholds, seeds, simulation grid, and
300-candidate reservation below are prospective candidates for owner review.
They do not authorize reader contact, data access, annotation, or `MV-1` use.

## Measurement Instrument and Reliability Estimands

### Gating axes

Reliability is assessed separately; no global coefficient may average away a
failed axis.

| Instrument | Primary categorical axis | Analysis population | Forbidden collapse |
| --- | --- | --- | --- |
| Image technical state | `intact/fully gradable`, `protocol-defined loss but interpretable`, `task-critical loss/not assessable` | All intended image reliability items | Information loss may not be relabelled ambiguity |
| Image prescribed coverage | `complete prescribed field`, `task-critical field/additional view missing`, `not assessable` | All intended image reliability items | Coverage may not be absorbed into technical quality or semantic ambiguity |
| Image semantic status | `determinate`, `genuinely ambiguous`, `not assessable` | Intact/covered and deliberately sampled edge strata | Reader disagreement alone may not define ambiguity |
| Image polarity | `present` versus `absent` | Prospectively intended determinate strata only, never selected from observed agreement | Undefined/ambiguous may not be forced into a polarity |
| Text integrity/completeness | `intact/complete`, `recoverable corruption`, `task-critical incomplete`, `no proposition` | All intended text reliability items | Missing content may not be absorbed into commitment or ambiguity |
| Text target polarity | `positive`, `negative`, `no target`, `not assessable` | All intended text reliability items | No target and not assessable may not be coded negative |
| Text commitment | `definite`, prospectively pooled `uncertainty-qualified` (`possible`, `probable`, `cannot exclude`, or `other qualified`), `not assessable` | All complete/recoverable text reliability items; raw qualified subtype is also reported | Hedging may not be called linguistic ambiguity, and the qualified union may not be chosen after ratings |
| Text interpretation status | `unique reading`, `multiple clinically reasonable readings`, `not assessable` | Complete text and declared edge strata | Missing text may not be called ambiguous |
| Text derived polarity | `present` versus `absent` | Prospectively intended complete, definite, unique-reading strata | No-mention/qualified items may not enter |
| Pair validity components | Separate `accept` versus `reject` axes for atomicity, preservation, fluency, plausibility, and absence of nonsemantic cues, plus an all-components-accept axis | Prospectively balanced compatible, conflict, and seeded-invalid pair strata | A passed component or global average may not hide a failed component; pair review may not alter locked unimodal labels |

For each categorical axis \(g\), the primary coefficient is nominal
Krippendorff alpha

```math
\alpha_g=1-\frac{D_{o,g}}{D_{e,g}},
```

using unit-level multi-reader coincidences and nominal distance
\(\delta(c,c')=\mathbb 1(c\ne c')\). `Not assessable` is an explicit category;
an unrecorded response is missing. No category is pooled after results.
Ordinal-distance alpha for ordered technical severity and Gwet AC1/AC2 are
mandatory sensitivities, not alternative promotion statistics.

### Exact agreement diagnostics

For every gating class, report:

- category prevalence and the full reader-by-category table;
- macro item-level pairwise exact agreement;
- class-specific positive agreement over unordered within-item reader pairs;
- unanimous, four-of-five, and applicable three-of-three rates;
- every pairwise confusion matrix;
- missingness overall, by reader, item stratum, and presentation arm;
- intra-reader exact agreement and nominal/weighted kappa on repeats; and
- adjudication and unresolved rates.

For item \(i\), let \(n_{ic}\) be its recorded ratings in class \(c\) and
\(m_i=\sum_c n_{ic}\). The item-level pairwise exact agreement is

```math
a_i=\frac{\sum_c {n_{ic}\choose2}}{{m_i\choose2}},
```

and macro exact agreement is the unweighted mean of \(a_i\) over items with at
least two recorded ratings. For required class \(c\), class-specific positive
agreement is

```math
P_c^+=\frac{2\sum_i {n_{ic}\choose2}}
{2\sum_i {n_{ic}\choose2}+\sum_i n_{ic}(m_i-n_{ic})}.
```

An empty denominator is non-estimable, not perfect agreement. These exact
definitions prevent software defaults or prevalence-dependent averaging from
changing the gate.

No probability rating is calibrated against an ambiguity label. For
determinate items only, calibration against the independently locked polarity
is a reader-behaviour diagnostic and cannot define reliability or truth.

## Locked Reliability-Set Allocation Candidate

The reliability set contains 150 unique patient/source clusters. Each cluster
may contribute one image instrument item, one text instrument item, and one
pair-validity item, but all linked records remain in one bootstrap cluster and
outside every scientific population. Sampling quotas are fixed before locked
ratings; their intended strata are design controls, not gold labels.

### Image item quotas

| Intended stratum | Count |
| --- | ---: |
| Intact determinate present | 30 |
| Intact determinate absent | 30 |
| Intact natural-ambiguity candidate | 30 |
| Interpretable `MV-1`-type loss, intended present | 15 |
| Interpretable `MV-1`-type loss, intended absent | 15 |
| Task-critical technical loss/non-gradable with complete field | 10 |
| Prescribed-field/additional-view missing with otherwise gradable input | 10 |
| Prescribed coverage `not assessable` edge case | 10 |
| **Total** | **150** |

### Text item quotas

| Intended stratum | Count |
| --- | ---: |
| Complete, definite, unique-reading present | 30 |
| Complete, definite, unique-reading absent | 30 |
| Complete natural multiple-reading candidate | 30 |
| Complete, unique-reading epistemic qualification | 20 |
| Task-critical polarity-slot loss | 10 |
| Verified no-proposition/missing-assertion case | 10 |
| Fully recoverable semantic-preserving surface corruption | 20 |
| **Total** | **150** |

### Pair-validity quotas

| Intended stratum | Count |
| --- | ---: |
| Valid compatible determinate pair | 50 |
| Valid conflicting determinate pair | 50 |
| Seeded-invalid atomicity as the primary failure | 10 |
| Seeded-invalid preservation as the primary failure | 10 |
| Seeded-invalid fluency as the primary failure | 10 |
| Seeded-invalid plausibility as the primary failure | 10 |
| Seeded-invalid nonsemantic-cue control as the primary failure | 10 |
| **Total** | **150** |

### Exact intended-class crosswalk

`EXCLUDE` means the item is outside that axis's prospectively intended analysis
population; it is not a missing or negative response. The following map fixes
every reliability-DGP class before ratings.

| Image intended stratum | Technical | Coverage | Semantic | Polarity |
| --- | --- | --- | --- | --- |
| Intact determinate present | `intact/fully gradable` | `complete prescribed field` | `determinate` | `present` |
| Intact determinate absent | `intact/fully gradable` | `complete prescribed field` | `determinate` | `absent` |
| Intact natural-ambiguity candidate | `intact/fully gradable` | `complete prescribed field` | `genuinely ambiguous` | `EXCLUDE` |
| Interpretable `MV-1` loss, intended present | `protocol-defined loss but interpretable` | `complete prescribed field` | `determinate` | `present` |
| Interpretable `MV-1` loss, intended absent | `protocol-defined loss but interpretable` | `complete prescribed field` | `determinate` | `absent` |
| Task-critical technical loss/non-gradable with complete field | `task-critical loss/not assessable` | `complete prescribed field` | `not assessable` | `EXCLUDE` |
| Prescribed-field/additional-view missing, otherwise gradable | `intact/fully gradable` | `task-critical field/additional view missing` | `not assessable` | `EXCLUDE` |
| Prescribed coverage `not assessable` edge | `intact/fully gradable` | `not assessable` | `not assessable` | `EXCLUDE` |

For the two split text rows below, keyed within-stratum order assigns exactly
ten items to each stated polarity. The split is part of allocation, not a
response-dependent repair.

| Text intended stratum | Integrity | Target polarity | Commitment | Interpretation | Derived polarity |
| --- | --- | --- | --- | --- | --- |
| Complete, definite, unique-reading present | `intact/complete` | `positive` | `definite` | `unique reading` | `present` |
| Complete, definite, unique-reading absent | `intact/complete` | `negative` | `definite` | `unique reading` | `absent` |
| Complete natural multiple-reading candidate | `intact/complete` | `not assessable` | `not assessable` | `multiple clinically reasonable readings` | `EXCLUDE` |
| Complete, unique-reading epistemic qualification | `intact/complete` | `10 positive / 10 negative` | `uncertainty-qualified` | `unique reading` | `EXCLUDE` |
| Task-critical polarity-slot loss | `task-critical incomplete` | `not assessable` | `EXCLUDE` | `not assessable` | `EXCLUDE` |
| Verified no-proposition/missing-assertion case | `no proposition` | `no target` | `EXCLUDE` | `not assessable` | `EXCLUDE` |
| Recoverable semantic-preserving surface corruption | `recoverable corruption` | `10 positive / 10 negative` | `definite` | `unique reading` | `10 present / 10 absent` |

For pair items, both valid strata are intended `accept` on every component and
on the global axis. Each seeded-invalid stratum is intended `reject` only on
its named component, `accept` on the other four components, and `reject` on the
global axis. Thus each component has 10 intended rejects and 140 accepts, while
the global axis has 50 rejects and 100 accepts.

Every class printed in the primary-axis table therefore has a non-zero intended
quota. Qualified commitment subtypes and reason codes remain report-only
subcategories; the prospectively defined `uncertainty-qualified` union is the
gating class. No other raw category is pooled for a gate.

If any required quota cannot be populated without reusing a patient/source
outside the declared cluster or inventing an unapproved clinical intervention,
the reliability design is infeasible. It is not repaired by post-rating
category pooling.

### Reliability reader assignment

All assignments use a separate HMAC-derived rank and a key-fixed permutation
of reader IDs; no intended label, observed response, model output, or repeat
result may alter them.

For simulation cell `c`, set
`I=perm(c,"assignment/image/readers",["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9"])`,
`T=perm(c,"assignment/text/readers",["T0","T1","T2","T3","T4","T5"])`, and
`P=perm(c,"assignment/pair/readers",["P0","P1","P2","P3","P4","P5"])`; every template below
indexes those permuted lists. Within intended stratum number `h` in printed
zero-based order, let `instrument` be the literal `image`, `text`, or `pair`
and rank item identifiers with
`perm(c,"item_rank/"+instrument+"/"+str(h),L_h)`, where `str(h)` is base-10
without leading zeros. The later observed assignment must
use the same domains and tags under the separately governed assignment HMAC
key; it cannot borrow a simulation seed, and that future key operation is not
authorized here.

- Ten image readers `R0`--`R9` rate five of ten panels per image item. Within
  each intended stratum, cycle consecutive five-reader templates. Every
  30-item stratum gives each reader 15 ratings; the two 15-item `MV-1` strata
  each use one full ten-template cycle, then templates `0`--`4` for the first
  stratum and `5`--`9` for the second, so every reader receives 15 ratings
  across that pair; each 10-item edge stratum gives every reader five. Across
  150 image items, each reader receives exactly 75 first presentations.
- Six text readers `T0`--`T5` rate five of six panels per text item. The omitted
  reader cycles by keyed item rank. Each 30-item stratum gives every reader 25
  ratings. Concatenate the two 20-item and two 10-item strata in their printed
  order after within-stratum keyed ranking and omit reader `i mod 6`; every
  reader then receives 50 ratings across those 60 items. Across 150 text items,
  each reader receives exactly 125 first presentations.
- Six pair readers `P0`--`P5` rate three consecutive-reader templates per pair
  item. Treat each valid 50-item stratum as one assignment block and concatenate
  the five printed 10-item invalid strata, after within-stratum keyed ranking,
  into one 50-item invalid assignment block. Within each block, eight complete
  six-template cycles are followed by one key-selected complementary template
  pair `k,k+3`. For block IDs `valid_compatible`, `valid_conflict`, and
  `invalid`, set `k` to the integer value of the first element of
  `perm(c,"assignment/pair/"+block_id+"/complement",["0","1","2"])`.
  Assign the two remaining items to template `k` then `k+3`. Every reader
  therefore receives exactly 25 ratings per block and 75 overall.

No reader serves in more than one of these modality/pair rosters, sees two
linked modalities from the same source, or sees both siblings. If any linked
sibling is required for a reliability edge case, it replaces—not supplements—
an item and goes to a disjoint panel under a dated allocation amendment.

Every reader receives exactly
\(\lceil0.15N_r\rceil\) blinded repeats from that reader's own assigned items,
selected in simulation as the first items from
`perm(c,"repeat/"+instrument+"/"+reader_id,L_r)` and later under the governed
assignment-key analogue. Repeats occur after the approved washout and never
expose the other sibling. Training/qualification, 60-unit
timing pilot, 150-cluster reliability set, `MV-1` qualification set, and every
scientific population are mutually disjoint.

## Reliability Interval and Precision Contract

For each primary \(\alpha_g\):

1. For each image, text, or pair axis separately, resample complete
   patient/source clusters within that instrument's frozen intended strata,
   retaining only each reader's first presentation for primary inter-reader
   alpha and agreement. Repeat ratings never become additional inter-reader
   codings; they remain linked only for intra-reader and hierarchical repeat
   diagnostics. The other instruments attached to a sampled cluster do not
   enter that axis's coefficient. This conditions precision on the fixed
   marginal allocation rather than inventing an unplanned cross-instrument
   stratum.
2. Use exactly 9,999 bootstrap resamples and seed `20270832`. Recompute alpha
   without imputation or category pooling.
3. Use the one-indexed 250th and 9,750th sorted bootstrap values as the 95%
   percentile interval. If observed alpha or **any** bootstrap alpha is
   undefined, the pre-rating allocation misses any frozen intended-stratum
   quota, any required positive-agreement denominator is empty, overall
   missingness exceeds 5%, or reader/arm missingness differs by more
   than five percentage points, that axis is non-estimable and fails. Observed
   post-rating category prevalence is reported but never used to refill or
   reselect the sample. No
   undefined resample is removed, replaced, or assigned an order statistic.
4. Apply the existing gate to every axis separately:
   \(\widehat\alpha_g\ge0.80\), lower 95% bound \(\ge0.67\), macro exact
   agreement \(\ge0.85\), and positive agreement \(\ge0.75\) for every required
   class. A sensitivity coefficient cannot rescue primary failure.

The percentile interval is a candidate, not assumed valid. Before a reader
brief, the complete estimator must pass the simulation contract below.

### Hierarchical sensitivity

For each axis, fit a crossed item--reader categorical model with fixed intended
stratum and presentation-arm effects, reader-specific category intercepts,
item random effects, and a repeat-noise component. Genuine-ambiguity strata
remain their own item class; the model may not force all disagreement into a
single latent truth. Report reader-severity/discrimination variation and the
posterior or likelihood-based item-distribution sensitivity, but do not use it
to overwrite raw ratings or rescue a failed design coefficient.

The exact model software, convergence rule, and priors or penalties must be
frozen after owner approval and before reader access. Failure to identify the
reader/item components narrows the claim to the fixed raw-rating instrument.

## MV-1 Evaluable Population and Estimand

Let \(S=1\) denote membership in the prospectively ranked, metadata-screened
qualification population. Write \(a_y=+1\) for `present` and \(a_y=-1\) for
`absent`. Let \(E=1\) require both siblings independently to have complete
field coverage, a determinate state, the same locked polarity, all ten
probability ratings recorded, all `MV-1` acceptance rules, and non-negative
panel support for that assigned state:

```math
h_{b,s}=a_y(\bar p_{b,s}-0.5)\ge0,
\qquad s\in\{intact,MV1\}.
```

Every individual determinate rating must also obey the prospective instrument
coherence rule: a `present` rating has \(p\ge0.5\), an `absent` rating has
\(p\le0.5\), and an unassessable rating has a structurally missing probability.
An incoherent record is an instrument error and cannot be silently corrected.
The support-alignment rule is an explicit selection condition, so the target
below is survivor-specific. Neither candidate-model output nor the magnitude
or difference \(q_b\) may determine \(S\), \(E\), severity, or replacement.

For polarity \(y\in\{present,absent\}\), define the finite-roster target:

```math
q_{v,y}^{R}
=\mathbb E_R\!\left[
 h_{b,intact}-h_{b,MV1}
 \mid S=1,E=1,Y_v=y
\right],
```

where \(\mathbb E_R\) averages patients under the locked ten-reader roster and
counterbalanced assignment schedule. Then

```math
q_{v,bal}^{R}
=\tfrac12(q_{v,present}^{R}+q_{v,absent}^{R}).
```

This is a survivor/evaluable-population estimand. It does not describe rejected
items, all screened candidates, all chest radiographs, or a population of
possible readers. Generalizing over readers requires a separately powered
reader-sampling design and cannot be inferred from the fixed roster.

For \(n_y\) evaluable blocks,

```math
\widehat q_{v,y}
=\frac1{n_y}\sum_{b:Y_v=y,E_b=1}
\left(h_{b,intact}-h_{b,MV1}\right),
\qquad
\widehat q_{v,bal}
=\tfrac12(\widehat q_{v,present}+\widehat q_{v,absent}).
```

All five raw `0--1` probabilities enter each panel mean, including a
categorically dissenting but probability-recording reader on an otherwise
eligible four-of-five item. A structurally missing probability makes that
block non-evaluable; it is never imputed.

## Disjoint-Panel Assignment

The candidate roster contains ten qualified image readers with internal IDs
`R0`--`R9`. Within each report-screen stratum:

1. rank candidates with a separate
   `AINC/v1/mv1-panel-assignment` HMAC key;
2. for recommended option A with 150 candidates, assign the \(i\)-th ranked
   candidate to cyclic template \(t=i\bmod10\). For option B with 128, use 12
   complete ten-template cycles for the first 120 candidates, then assign the
   final eight in key-ranked order to every template except one key-selected
   complementary pair \(k,k+5\pmod {10}\). This gives every reader exactly 64
   intact and 64 transformed assignments in that stratum;
3. after a key-fixed permutation of reader IDs, assign the intact sibling to
   readers \(\{R_t,R_{t+1},\ldots,R_{t+4}\}\) modulo 10 and `MV-1` to the
   complementary five;
4. independently key and counterbalance presentation order, interface slot,
   and repeat placement; and
5. never change assignment using image truth, eligibility, reader response,
   \(q_b\), or model output.

For every simulation cell `c`, define the reader list exactly as

```text
J=perm(c,"panel/readers",
       ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9"]).
```

For screen stratum `s` equal to `positive` or `negative`, name candidates
`C000` through `C149` for option A or `C000` through `C127` for option B and
rank them with `perm(c,"panel/"+s+"/candidate_rank",L_s)`. Templates index
`J`. Under option B set `k` to the integer value of the first element of
`perm(c,"panel/"+s+"/omitted_pair",["0","1","2","3","4"])`; assign the
last eight ranked candidates to the remaining template integers in ascending
order. Thus the omitted pair, reader mapping, and its alignment with every
fixed reader-effect vector are deterministic. The later observed assignment
uses the governed `AINC/v1/mv1-panel-assignment` HMAC key with these same
domains/tags and records the resulting lists before ratings.

Each reader sees at most one sibling from a source. Within every complete block
the two panels are disjoint. Within each report-screen stratum, every reader
appears exactly 75 times on each sibling side under option A or exactly 64 times
under option B.
Actual-polarity imbalance is reported, never repaired after labels.

## MV-1 Interval and Joint Gate

Primary inference conditions on the locked roster. Resample whole evaluable
patients within independently assigned polarity, keeping all ratings and panel
assignments together. Use exactly 9,999 stratified patient bootstrap resamples
and seed `20270833`.

Let \(s_y^2\) be the sample variance of patient-level \(q_b\) in polarity \(y\).
Use

```math
\widehat{se}(\widehat q_{v,y})=\frac{s_y}{\sqrt{n_y}},
\qquad
\widehat{se}(\widehat q_{v,bal})
=\frac12\sqrt{\frac{s_{present}^2}{n_{present}}
              +\frac{s_{absent}^2}{n_{absent}}}.
```

Recompute all three estimates and standard errors in every bootstrap sample.
For \(k\in\{bal,present,absent\}\), define

```math
T_k^*
=\frac{\widehat q_k^*-\widehat q_k}{\widehat{se}^*(\widehat q_k)}.
```

Take \(M^*=\max_kT_k^*\), use the one-indexed 9,500th sorted maximum as the
one-sided 95% max-\(t\) critical value
\(c=\max(0,M^*_{(9500)})\), and set
\(L_k=\widehat q_k-c\widehat{se}(\widehat q_k)\). Any non-finite or zero
required observed/resampled standard error makes the gate non-estimable; no
resample is discarded or redrawn.

`MV-1` qualifies only if all conditions hold:

1. \(n_{present}\ge108\) and \(n_{absent}\ge108\);
2. every applicable reader-reliability, state-preservation, coverage, and
   intervention-validity gate passes;
3. \(L_{bal}>0.10\);
4. \(L_{present}>0\) and \(L_{absent}>0\); and
5. the reader/panel sensitivity audit below does not trigger a veto.

Month-3 or model outcomes cannot rescue failure. The polarity guardrails
prevent the balanced mean from hiding a null or reversed effect.

### Reader/panel sensitivity veto

On the frozen `E=1` blocks, fit ordinary least squares to rating-level
assigned-state support \(a_y(p_{bsr}-0.5)\) with patient fixed intercepts,
reader fixed deviations, an `MV-1` sibling indicator, the indicator multiplied
by polarity code \(a_y\), and centered reader-by-`MV-1` terms. Omit a polarity
main effect because it is absorbed exactly by the patient intercepts. Use one
intercept column per patient and no global intercept; impose sum-to-zero
constraints separately on reader deviations and reader-by-`MV-1` terms. If
\(\beta_s\) and \(\beta_{sy}\) are the sibling and sibling-by-polarity
coefficients, define

```math
q_{FE,y}=-(\beta_s+a_y\beta_{sy}),
\qquad q_{FE,bal}=-\beta_s.
```

Use the Moore--Penrose solution with relative singular-value cutoff `1e-12`;
rank deficiency under this full-rank constrained specification or a non-finite
coefficient triggers the veto. This is a deterministic fixed-roster
sensitivity, not reader-population inference.

Separately recompute the design estimator after leaving out each
reader. Freeze the full ten-rating `E`, assigned `Y_v`, and selected blocks;
remove that reader's probability from their assigned sibling, recompute only
that four-reader panel mean and the resulting q values, and do not reclassify,
drop, or replace a block when its four-reader support crosses zero. Thus the
leave-one-reader analysis measures influence on the already selected estimand,
not a different four-reader acceptance rule.

For every omitted reader, compute `q_LOO,present`, `q_LOO,absent`, and their
equal-weight mean; a missing polarity estimate is non-estimable. Stop and reopen
the measurement model if `q_FE,present <= 0`, `q_FE,absent <= 0`, any
`q_LOO,present <= 0`, or any `q_LOO,absent <= 0`; if
`abs(q_FE,bal-qhat_bal) > 0.05`; or if any
`abs(q_LOO,bal-qhat_bal) > 0.05`. These are prospective diagnostic tolerances,
not clinical constants, and cannot promote an otherwise failed primary gate.

## Deterministic Yield Audit

The reproducible table
[`mv1_qualification_yield_sensitivity.csv`](../../reports/tables/mv1_qualification_yield_sensitivity.csv)
is generated by:

```bash
python scripts/calculate_mv1_qualification_design.py
```

It computes exact binomial tail probabilities under perfect report-screen
polarity and independent equal pair yield. With 128 candidates per ideal
polarity, joint 90% probability of reaching 108 in both requires pair
evaluability of approximately `0.887019`. At 85% yield, the joint probability
is `0.404356`; at 90%, `0.968049`.

With 150 candidates per ideal polarity, 80% yield gives joint probability
`0.986107`, and the yield required for joint 90% probability falls to
approximately `0.773382`. These are synthetic benchmarks, not feasibility
evidence. Imperfect report-screen polarity, asymmetric eligibility,
patient/source dependence, and outcome-dependent state preservation can make
the real design worse or qualitatively different.

## Required Pre-Reader Simulation Contract

No annotation brief may issue until a deterministic implementation of the
complete reader and `MV-1` pipeline evaluates the following pre-data grid.

Every simulation cell uses one canonical identifier: a compact UTF-8 JSON
object whose keys are sorted lexicographically at every level and whose scalar
factor values are JSON strings exactly as printed in this contract (for
example, `"0.90"`). Arrays retain the printed factor order. The serialization
contains no optional fields, nulls, or whitespace. Reliability objects contain
exactly the keys `kind`, `n`, `allocation`, `stressed_axis`,
`prevalence_class`, `prevalence_fraction`, `accuracy`, `accuracy_mode`,
`accuracy_class`, `confusion_mode`, `reader_sd`, `item_sd`,
`missingness_rate`, `missingness_mode`, `missingness_class`, and
`repeat_stability`. MV objects contain exactly `kind`, `n`,
`screen_fidelity_present`, `screen_fidelity_absent`, `yield_present`,
`yield_absent`, `q_present`, `q_absent`, `q_distribution`, `q_sd`,
`probability_reader_sd`, `rating_noise_sd`, `state_reader_sd`,
`patient_state_sd`, `state_correct_probability`, `opposite_error_fraction`,
and `selection_slope`. Use the literal string `"none"` for inapplicable fields.
Set `kind` to `"reliability"` or `"mv1"`; reliability `n` is `"150"`,
`allocation` is `"printed"` or `"designated_prevalence"`, `accuracy_mode`
is `"common"` or `"designated_low"`, `confusion_mode` is `"symmetric"` or
`"directed"`, and `missingness_mode` is `"mcar"`, `"reader"`, or
`"class"`. MV `q_distribution` is `"beta"` or `"two_point"`, with
`q_sd="none"` for the latter. The two screen-fidelity fields mean
`P(Y=present | positive screen)` and `P(Y=absent | negative screen)`; yield
and q fields are indexed by independently assigned polarity, not screen label.
`state_reader_sd` is the exact SD used for both independently tagged coverage-
and state-category reader vectors.

TB-0009 prospectively freezes the numeric lexemes before execution.
Reliability prevalence and missingness use decimal strings `"0.00"`,
`"0.05"`, `"0.10"`, `"0.15"`, and `"0.20"` as applicable; percentages in
the explanatory factor list are not identifier lexemes. MV q zero is
`"0.00"`. Integer `n` and selection-slope strings retain their printed
integer form. Planning-region inequalities select only the finite levels
printed in the applicable factor grid; they do not introduce a continuous
grid.

Reliability axis identifiers, in order, are `image_technical`,
`image_coverage`, `image_semantic`, `image_polarity`, `text_integrity`,
`text_target_polarity`, `text_commitment`, `text_interpretation`,
`text_derived_polarity`, `pair_atomicity`, `pair_preservation`,
`pair_fluency`, `pair_plausibility`, `pair_nonsemantic_cues`, and
`pair_global`. Category IDs append `:c0`, `:c1`, and so on in the
left-to-right category order printed in the gating-axis table; for every pair
axis, `c0=accept` and `c1=reject`. Every reliability cell names exactly one of
these axes in `stressed_axis`; the reliability simulator makes no cross-axis
joint-record claim.

Define `seed(k,c,t)` as the unsigned big-endian integer represented by the
first 16 digest bytes of `HMAC-SHA256`, with UTF-8 decimal root seed `k` as the
key and UTF-8 `c + "\n" + t` as the message. Define `perm(c,t,L)` by sorting
the UTF-8 identifiers in list `L` by the full digest of
`HMAC-SHA256(key=UTF8("20270835"), message=UTF8(c + "\nperm/" + t + "\n" +
identifier))`; bytewise digest order is primary and identifier order breaks a
digest tie. Required permutation tags are
`reader_effect/<axis>/<category>`, `missingness_reader/<axis>`,
`item_rank/<instrument>/<zero-based-stratum>`,
`assignment/image/readers`, `assignment/text/readers`,
`assignment/pair/readers`, `assignment/pair/<block>/complement`,
`repeat/<instrument>/<reader>`, and `ambiguity/<axis>` for reliability. MV
uses `probability_reader`, `coverage_reader`, `state_reader`, `panel/readers`,
`panel/<screen_stratum>/candidate_rank`,
`panel/<screen_stratum>/omitted_pair`, and `repeat/<reader>`.

All calibration and outer random streams use NumPy `PCG64DXSM`. Instantiate
one engine from the named 128-bit seed and consume only successive
`random_raw()` unsigned 64-bit words. For each word set `m=x >> 12` and convert
it to the exactly representable open-unit uniform `U=(m+0.5)/2^52`; obtain
normal and beta variates by the mathematical left-continuous inverse CDF, and
categorical/Bernoulli variates by cumulative probability. No distribution
convenience method may consume a variable number of engine words. The reviewed
implementation must freeze NumPy and numerical inverse-CDF versions before
execution.

Within each outer reliability replication, use the cell's named axis and keyed
included-item order: item-difficulty uniform; the ambiguity-mixture uniform
when applicable; then, in assigned reader-ID order, category uniform and
missingness uniform. In a second pass ordered by reader ID and keyed repeated
item, consume repeat-match, alternate-category, and repeat-missingness
uniforms. Within each outer MV replication, order report-screen
strata as positive then negative and candidates by frozen rank; consume state,
`Q`, and patient-effect uniforms, then for intact followed by transformed
siblings and assigned reader-ID order consume probability-noise, coverage, and
state-category uniforms. A second MV repeat pass uses reader ID and keyed item
order and consumes fresh probability-noise, coverage, repeat-match, and
alternate-category uniforms. Draw every listed uniform even when an earlier
draw makes it latent or missing, so branching never changes subsequent
streams. The canonical cell JSON, every permutation, software lock, and
zero-based replication index must be written to the result.

The two analysis bootstraps use separate `PCG64DXSM` raw-word engines and the
same open-unit-uniform rule; they never consume the DGP engine. For the later
observed reliability analysis, initialize one engine with integer seed
`20270832`, visit axes in the canonical order above, then for bootstrap
replicates `b=0,...,9998` visit included frozen intended strata in printed
order. Within a stratum of size `n_h` ordered by frozen item rank, consume
exactly `n_h` uniforms and select index `floor(n_h U)` with replacement. Reuse
that replicate's complete cluster multiplicities for every reader and every
recomputed statistic of the axis. For outer simulation replication `j`, use
the identical procedure with a fresh engine seeded by
`seed(20270832, canonical_cell_id, "analysis_bootstrap/" + j)`; `j` is
zero-based decimal without leading zeros.

For the later observed MV analysis, initialize one engine with integer seed
`20270833`. For each of 9,999 replicates, visit assigned polarity in `present`,
`absent` order and draw exactly `n_y` indices by `floor(n_y U)` from evaluable
patients ordered by frozen patient rank. The same two index arrays are reused
for `q_present`, `q_absent`, `q_bal`, all three studentized statistics, and
their maximum. For outer simulation replication `j`, use a fresh engine seeded
by `seed(20270833, canonical_cell_id, "analysis_bootstrap/" + j)`. No index
array is shared across outer replications, discarded, redrawn, or selected by
the result.

### Reliability DGP and factor grid

- intended-class prevalence: exact crosswalk above; an axis-specific
  designated-class sensitivity at 10%, 15%, and 20%;
- reader nominal correct-category probability: `0.75`, `0.80`, `0.85`,
  `0.90`, and `0.95`, plus designated-class accuracy decrements of `0.10`;
- reader logit-severity SD: `0.00`, `0.25`, `0.50`, and `0.75`;
- item-difficulty SD: `0.00`, `0.50`, and `1.00`;
- missingness: `0%`, `5%`, and `10%`, including reader- and class-dependent
  patterns;
- repeat stability: within-reader agreement `0.75`, `0.85`, and `0.95`; and
- genuine-ambiguity mixture separated from determinate reader error.

For each primary axis `g` with `K_g` printed categories, the simulation uses
the following executable categorical DGP. The intended class `z_ig` and
inclusion are fixed by the crosswalk. Let `N_g` be the number of included items
for that axis; excluded rows never enter its coefficient. An axis-specific
prevalence sensitivity designates each required class in turn, assigns it
`floor(f N_g+0.5)` items for `f in {0.10,0.15,0.20}`, and distributes the
remaining items among other classes in proportion to their baseline crosswalk
counts by the largest-remainder rule. Printed category order breaks equal
remainders. Keyed item rank performs the reassignment for this synthetic stress
cell only; all other axes retain their baseline crosswalk. The designated class
and fraction are explicit cell fields, so no tied empirical "smallest class"
is selected.

1. Use both a symmetric confusion mode and a directed mode. In the symmetric
   mode, wrong-class weights are `w_zc=1/(K_g-1)`. In the directed mode,
   two-thirds of wrong-response mass goes to the next printed category
   cyclically and the remaining third is divided equally among other wrong
   categories; for a binary axis the sole wrong category receives all mass.
2. In a common-accuracy cell set `a_z=a` for every intended class. In each
   designated-low cell, run every intended class `z_low` in turn with
   `a_z_low=max(0.50,a-0.10)` and `a_z=a` otherwise. Set baseline mass
   `b_zz=a_z` and `b_zc=(1-a_z)w_zc`. For every reader/category pair, form
   `x_rgc=Phi^-1((rank_gc(r)+0.5)/R_g)`, where `rank_gc(r)` is reader `r`'s
   zero-based position in
   `perm(c,"reader_effect/"+axis_id+"/"+category_id,L_g)`,
   normalize it as
   `z_rgc=(x_rgc-mean_r x_rgc)/sqrt(mean_r((x_rgc-mean_r x_rgc)^2))`, and set
   the fixed finite-roster effect `u_rgc=sigma_R z_rgc`. Thus `sigma_R` is the
   exact population SD over the named roster. Effects are generated once per
   cell and held fixed across outer replications; primary simulation is
   conditional on that finite roster.
3. Draw one item difficulty `d_ig ~ Normal(0,sigma_I^2)` per cluster/axis.
   Conditional response logits for assigned reader `r` are
   `eta_irc=log(b_zc)+u_rgc-d_ig 1(c=z)`. Draw the first-presentation category
   from the corresponding softmax. Item difficulty, reader effects, and every
   linked rating remain attached to the patient/source cluster.
4. Apply three separately reported missingness modes. MCAR uses probability
   `m`. For reader-dependent missingness, construct a separate tagged reader
   permutation `perm(c,"missingness_reader/"+axis_id,L_g)`, normalize its
   positional quantile vector to exact roster mean zero and population SD one
   as above, call it `z_r^miss`, and use
   `logit P(M_irg=1)=alpha_m+0.75 z_r^miss`. Class-dependent missingness runs
   every required class `c_miss` in turn and uses
   `alpha_m+0.75 1(z_ig=c_miss)`. Bisection chooses `alpha_m` so the frozen
   assignment-weighted marginal missingness is `m`: set no responses missing
   when `m=0`; otherwise use 100 bisection iterations on `[-30,30]` and require
   absolute residual at most `1e-10`. A missing bracket makes the cell
   inadmissible. `c_miss` is always an explicit cell field.
5. For a recorded original response, a repeat equals that response with the
   named stability probability. Otherwise it is drawn from the original
   softmax after assigning zero mass to the original category and
   renormalizing. If the original response is missing and the repeat is
   recorded, draw from the full original softmax; still consume the frozen
   repeat-match and alternate-category uniforms. Repeat missingness is drawn
   from the same frozen mode. Repeats enter only linked intra-reader/
   hierarchical diagnostics.
6. For intended genuine-ambiguity items, order IDs with
   `perm(c,"ambiguity/"+axis_id,L_amb)` and assign interpretation-mixture
   weight `0.50` at even zero-based positions and `0.70` at odd positions;
   draw a latent polarity interpretation for the probability diagnostic only.
   The categorical semantic-status response
   still follows the model above with `z=ambiguous`. Determinate-item errors
   never use this mixture, so ambiguity and reader error remain distinct.

For the normal item effect, define the finite-roster population alpha and
agreement targets by 41-node Gauss--Hermite quadrature and exact summation over
the fixed assignment/category/missingness probabilities. Quadrature is
repeated at 61 nodes; an absolute discrepancy above `1e-6` makes the cell
non-estimable. Those integrated quantities—not a very large simulated sample—
are the coverage and false-promotion truths.

The exact scenario set is the union of: (i) the reference cell
`a=0.90, sigma_R=0.25, sigma_I=0.50, m=0.05, repeat=0.85`, common accuracy,
symmetric confusion, MCAR, and printed allocation; (ii) the prospectively
clarified one-factor family with all unmentioned factors at reference: every
class crossed with each designated prevalence fraction, every printed `a`
run once in common mode and once with each class designated low, every printed
reader SD, item SD, repeat stability, and both confusion modes, plus one MCAR
row at `m=0.00` and MCAR, reader-dependent, and every class-dependent target
at each of `m in {0.05,0.10}`; and (iii) the Cartesian adversarial set
`a in {0.80,0.90}`, `sigma_R in {0.25,0.75}`,
`sigma_I in {0.50,1.00}`, `m in {0.05,0.10}`, both confusion modes, all
three missingness modes (with every required `c_miss` for the class-dependent
mode), each axis/class designated at 10% prevalence, common accuracy, and
repeat stability 0.85. Duplicate cells are run once by canonical serialized
cell ID. Add as a fourth set every Cartesian cell in the reliability planning
region specified under operating criteria below. That planning family retains
reader- and class-mode labels at `m=0.00` as distinct canonical rows entering
`K_plan`, despite behaviorally identical zero-missingness generation. The
fixed `0.50/0.70` ambiguity mixture is within-cell and creates no extra cell.
The exact inventory and workload compilation are in the
[simulation resource-feasibility audit](simulation_resource_feasibility_audit.md).

The simulation must run the complete alpha, bootstrap, missingness, and
multi-threshold gate separately for every named axis. It must report coverage,
false promotion, gate power, undefined-resample frequency, and class-specific
failure. All records for that axis attached to one patient/source remain one
bootstrap cluster. It must **not** generate independent axis responses and call
their product or empirical conjunction a joint instrument-pass probability:
the locked schema imposes deterministic cross-axis constraints that such a DGP
would violate. Dependence-robust family power is handled by the union-bound rule
below; a future joint-record DGP would require a separate approved coherent
response model.

### MV-1 DGP and factor grid

- report-screen fidelity by stratum:
  `(0.75,0.75)`, `(0.80,0.80)`, `(0.90,0.90)`, `(0.95,0.95)`,
  `(0.75,0.90)`, and `(0.90,0.75)`;
- target gradability/state-preservation evaluability pairs by assigned polarity:
  `(0.70,0.70)`, `(0.75,0.75)`, `(0.80,0.80)`, `(0.85,0.85)`,
  `(0.90,0.90)`, `(0.75,0.90)`, and `(0.90,0.75)`;
- selected-population means:
  `(q_{present},q_{absent})` in
  `{(0.10,0.10),(0.20,0.00),(0.00,0.20),(0.30,0.00),(0.00,0.30),`
  `(0.15,0.05),(0.20,0.20),(0.25,0.15),(0.15,0.25),(0.30,0.10)}`;
- patient-level \(q_b\) distribution: scaled beta on
  \([-0.5,0.5]\) with SD `0.15` and `0.25` where admissible, plus the
  mean-matched extremal two-point distribution on \(\{-0.5,0.5\}\);
- reader probability-scale severity SD:
  `0.00`, `0.02`, `0.05`, and `0.10`, centered over the locked roster;
- within-reader rating-noise SD: `0.03`, `0.07`, and `0.10`;
- finite-roster coverage/state-vote category-severity SD: `0.00`, `0.25`,
  and `0.50`;
- shared patient state-effect SD: `0.00` and `0.50`; conditional
  correct-state vote probability: `0.90`, `0.95`, and `0.99`; conditional
  error split to opposite-polarity rather than ambiguity: `0.25` and `0.50`;
- selection dependence: logit slope of pair evaluability on latent attenuation
  `0`, `-1`, and `-2`, with the intercept solved to the target marginal yield;
  and
- both 128 and 150 candidates per report-screen stratum.

The q DGP is conditional on an independently established image polarity after
the reliability instrument has passed; it does not validate that polarity.
For each fixed report-screen stratum `r`, generate assigned state `Y=r` with
the named fidelity and the opposite state otherwise. Write `a_Y=+1` for
present and `-1` for absent.

For each assigned polarity, draw a latent aligned-support attenuation `Q` on
`[-0.5,0.5]`. For the beta family, let `X=Q+0.5`,
`m=mu+0.5`, `k=m(1-m)/sigma_Q^2-1`, and draw
`X ~ Beta(m k,(1-m)k)`; a non-positive shape makes the cell inadmissible.
For the extremal family, set `P(Q=0.5)=mu+0.5` and
`P(Q=-0.5)=0.5-mu`. Define ideal state-aligned supports

```math
H_{intact}=(0.5+Q)/2,
\qquad H_{MV1}=(0.5-Q)/2.
```

Thus both supports lie in `[0,0.5]` and their difference is exactly `Q`.
Create the locked reader probability-severity vector
from `x_r=Phi^-1((r+0.5)/10)`, normalize `x_r` to roster mean zero and
population SD one, multiply by `sigma_R`, and apply
`perm(c,"probability_reader",L)` once per cell. For
reader `r` assigned to sibling `s`, draw `epsilon_bsr ~ Normal(0,sigma_e^2)`
and form the unsigned evidence magnitude

```math
g_{bsr}=clip(H_{bs}+u_r+epsilon_{bsr},0,0.5).
```

Probability direction is assigned only after the categorical state draw below.
`round_0.01` rounds half upward, and clipping always precedes rounding. This
construction allows finite-roster severity, clipping, rating noise, and
state-vote errors to change observed panel attenuation.

Generate a shared patient state effect `w_b ~ Normal(0,sigma_P^2)` and a
second vector `v_r` from the same normalized-quantile construction using
`perm(c,"coverage_reader",L)` and the named `state_reader_sd`. A reader
supplies complete/interpretable coverage with

```math
P(V_{bsr}=1 | Q,w_b)=expit(alpha_Y+beta_Q Q+w_b+v_r).
```

If `V=0`, probability is structurally missing and the coverage/state record is
not assessable. If `V=1`, draw the categorical state from `correct Y`,
`opposite Y`, and `genuinely ambiguous`. With nominal correct-state probability
`d`, opposite-error fraction `omega`, and a third independently tagged,
mean-zero vector `v'_r` from `perm(c,"state_reader",L)` and having exact roster
SD equal to the named category-severity SD, use softmax logits

```math
eta_correct=log(d)+v'_r,
\quad eta_opposite=log((1-d)omega)-v'_r/2,
\quad eta_ambiguous=log((1-d)(1-omega))-v'_r/2.
```

Record the probability only after drawing that state: use
`round_0.01(0.5+a_Y g_bsr)` for `correct Y` or `genuinely ambiguous`, and
`round_0.01(0.5-a_Y g_bsr)` for `opposite Y`. Thus every determinate vote and
probability are category-coherent, while an ambiguous vote retains its latent
evidence probability. This explicitly generates a possible fifth
opposite-polarity vote and tests the four-of-five rule. Conditional on
`Q,w_b` and the fixed reader effects, sibling/reader draws are independent.
This qualification DGP remains conditional on an independently reliable
polarity instrument; it does not assume perfect individual votes.

Apply the exact 128/150 panel schedule. A block has `E=1` only when all ten
probabilities are recorded, at least four determinate votes in each sibling
panel agree on `Y`, both panel means have non-negative aligned support, and
all other frozen acceptance rules pass. This synthetic DGP conditions the
construction-only rules it does not generate—atomic source eligibility and
registered `MV-1` implementation acceptance—to pass. It therefore tests the
reader-measurement, selection, yield, and q-analysis contract, not
intervention-construction validity. Define observed q from the two five-reader
aligned-support means. For repeat diagnostics, each reader repeats exactly
`ceil(0.15 N_r)` of that reader's assignments selected by
`perm(c,"repeat/"+reader_id,L_r)`. Fix categorical repeat stability at `0.85`.
At repeat, retain `Q` and the patient effect, draw fresh probability noise and
coverage, and—when coverage is complete—match the original recorded category
with probability `0.85`; otherwise draw from its original three-category
softmax after assigning zero mass to the original category and renormalizing.
If the original category was missing, draw directly from the full softmax.
Assign the repeated probability direction from the repeated category exactly
as above. Repeats never enter `E`, q, or the primary interval.

Because attenuation-dependent evaluability changes the survivor mean, do not
insert the requested selected-population q values as raw beta means. For each
polarity and cell, jointly calibrate `(mu_Y,alpha_Y)` to

```math
P(E=1 | Y)=rho_Y,
\qquad E(q_observed | E=1,Y)=q_Y_target.
```

Use common random numbers from exactly `2^20` NumPy `PCG64DXSM` candidate
vectors with
`seed(20270834, canonical_cell_id, polarity + "/cal")`. Each vector orders
base uniforms as `U_Q`, shared patient-state `U`, then—in intact followed by
transformed panel order and key-permuted reader-ID order—probability-noise `U`,
coverage `U`, and categorical-state `U`. Transform them by the raw-word rule
above. Cycle the exact panel templates over candidate-vector index so
calibration averages the frozen assignment.
For each trial `mu`, first evaluate both endpoints `alpha=-30,30` once, then
use exactly 80 midpoint evaluations for bisection of the yield equation,
caching the retained endpoint value at every step. Use 80 midpoint evaluations
over the admissible beta mean (or two-point mixing probability) for the q
equation. Before the outer bisection, evaluate 1,001 equally spaced admissible
means; those already include and cache its two endpoints. Any decrease in the
calibrated selected q larger than `1e-6`, or any missing bracket, makes the cell
inadmissible. Validate the solution on an independent `2^22`-vector stream
using tag `polarity + "/validate"`; both absolute residuals must be at most
`0.0005`.
No failed calibration draw is reused in the outer simulation.

The exact MV candidate scenario set is the union of: (i) the reference cell
`n=150`, fidelity `(0.90,0.90)`, yield `(0.85,0.85)`, q target
`(0.20,0.20)`, beta SD `0.15`, probability severity `0.05`, noise `0.07`,
state severity `0.25`, patient-state SD `0.50`, correct-state probability
`0.95`, opposite-error fraction `0.50`, and selection slope `-1`; (ii) every
one-factor value listed above
with other factors at reference; (iii) exactly the null pairs
`(0.10,0.10)`, `(0.20,0.00)`, `(0.00,0.20)`, `(0.30,0.00)`,
`(0.00,0.30)`, and `(0.15,0.05)`, crossed with both n values, all three
syntactically declared q-distribution configurations, and every selection
slope at other reference factors; and (iv) asymmetric fidelity pairs crossed with
yield pairs `(0.75,0.90)` and `(0.90,0.75)` and q alternatives
`(0.25,0.15)` and `(0.15,0.25)`, with every unmentioned factor—including
`n`, q distribution/SD, severities, state parameters, and slope—at reference;
and (v) every Cartesian cell in the MV planning region specified below.
Duplicate canonical cell IDs run once. All three q distributions stay in the
pre-calibration candidate manifest. A non-positive beta shape, missing
calibration bracket, nonmonotonicity, or failed validation is a failed design
cell, never a reason to delete it or reduce the family; a successful full run
requires every candidate to calibrate.

The simulation must generate individual reader probabilities, enforce the
cyclic disjoint-panel schedule and four-of-five state rules, apply selection,
apply the calibration above, and run the exact joint max-\(t\) analysis. A q-level simulation that omits
reader assignment is insufficient.

### Operating criteria

For `x` successes in `N` fixed outer replications, use exact binomial
Clopper--Pearson limits. The one-sided lower limit at error `alpha` is zero for
`x=0` and otherwise `BetaQuantile(alpha; x, N-x+1)`; the one-sided upper limit
is one for `x=N` and otherwise
`BetaQuantile(1-alpha; x+1, N-x)`. A two-sided `1-alpha` interval uses
`alpha/2` in each tail. No normal or Wilson approximation is permitted.

- **Reliability false promotion:** in every simulated cell whose integrated
  population alpha is at most `0.67`, macro exact agreement is at most `0.80`,
  or any required-class positive agreement is at most `0.70`, the one-sided
  95% Clopper--Pearson upper limit for the probability that the complete axis
  gate passes must not exceed `0.055`.
- **Reliability coverage and power:** for every primary alpha percentile
  interval, the lower endpoint of the two-sided 95% Clopper--Pearson interval
  for marginal coverage must be at least `0.945`. The recommended reliability
  planning region is the printed allocation with common accuracy,
  `a in {0.90,0.95}`,
  `sigma_R <= 0.25`, `sigma_I <= 0.50`, missingness at most `0.05`, repeat
  stability at least `0.85`, both confusion modes, and all three missingness
  modes, with every required class used in class-dependent mode. Every such
  axis/cell must first have integrated population metrics above all gate
  thresholds. Before simulation, enumerate the unique planning manifest and
  let `K_plan` be its number of axis/cell rows. For each row compute the
  exact one-sided Clopper--Pearson lower bound `L_g,c^MC` with
  `alpha=0.05/K_plan`; let `L_g^min` be the minimum over planning cells for
  axis `g`. Require

  ```math
  \sum_{g=1}^{15}(1-L_{g}^{min})\le0.10.
  ```

  By simultaneous Bonferroni coverage plus the union bound, this gives a
  95%-confidence lower guarantee of at least `0.90` for all 15 axis gates under
  arbitrary cross-axis dependence. An independence-based conjunction cannot
  approve `G0-READERS A`.
- **MV-1 false qualification:** at every q cell where `q_bal=0.10`,
  `q_present=0`, or `q_absent=0`—including `(0.30,0)` and `(0,0.30)`, where
  the balanced margin is strictly alternative—the one-sided 95%
  Clopper--Pearson upper limit for passing the complete joint q family must not
  exceed `0.055`.
- **MV-1 simultaneous coverage:** report all marginal coverages and the event
  `L_bal <= q_bal`, `L_present <= q_present`, and `L_absent <= q_absent`
  simultaneously. The lower endpoint of its two-sided 95% Clopper--Pearson
  interval must be at least `0.945` in every admissible MV cell.
- **MV-1 joint yield/power:** the recommended planning region is exactly
  option A (`n=150`), fidelity in `{(0.90,0.90),(0.95,0.95)}`, yield in
  `{(0.85,0.85),(0.90,0.90)}`, q target in
  `{(0.20,0.20),(0.25,0.15),(0.15,0.25)}`, beta q with SD `0.15`, probability
  severity at most `0.05`, rating noise at most `0.07`, state severity at most
  `0.25`, patient-state SD at most `0.50`, correct-state probability at least
  `0.95`, opposite-error fraction in `{0.25,0.50}`, and selection slope in
  `{0,-1}`. For every Cartesian cell in this
  region, the lower endpoint of the two-sided 95% Clopper--Pearson interval for
  the **joint** probability of both 108 yield floors, all three q gates, and no
  fixed-effect/leave-one-reader veto must be at least `0.90`.
- Except for the explicitly one-sided or multiplicity-adjusted limits above,
  report a two-sided 95% Clopper--Pearson interval for every Monte-Carlo
  probability.
  Derive each independent outer-replication stream as
  `seed(20270836, canonical_cell_id, "outer/" + j)`, where `j` is the
  zero-based decimal replication index without leading zeros.
- Use exactly **120,000 outer replications in every pre-enumerated cell**. This
  fixed count is chosen so the worst-case two-sided 95% exact-binomial interval
  half-width is below `0.003`; verify that numerical fact in the reviewed
  implementation. There is no data-dependent extension, early stop, or cell-
  specific replication count. A numerical half-width of `0.003` or greater
  fails. For `MV-1`, calibration is a mandatory precondition rather than a
  manifest filter: if any candidate cell fails calibration, the proposed
  design fails and cannot claim a successful operating-characteristic run.
  Failure-only termination cannot promote evidence or authorize pruning.
- The simulation code, seed derivation, software lock, all failed cells, and
  exact resource use must be reviewed before reader contact.

If no resource-feasible design passes the recommended planning region, `MV-1`
remains unqualified. The project must enlarge the screen/reader budget through
a dated decision, replace `MV-1` through a new pre-data option audit, narrow the
primary control family, or stop. It may not select a favourable simulation cell
after ratings.

## Workload Consequence

The existing `MV-1` qualification row assigns 110 person-hours to 256 screened
candidates. Linear scaling to 300 candidates gives approximately
`110(300/256)=128.9` hours. Replacing 110 by 129 raises the first-four-phase
worksheet from 467 to approximately **486 hours**, below but close to the
proposed 500-hour stage ceiling. This is arithmetic under unverified per-rating
times, not a resource fact; it leaves only about 14 hours of nominal headroom.

The unchanged 60-hour locked-reliability row explicitly includes 120 image,
114 text, and 72 pair-repeat ratings from the per-reader ceiling rule. If those
repeats, adjudications, or meetings do not fit during the authorized timing
pilot, the row fails resource qualification; pair repeats may not be silently
removed after ratings.

If the cumulative ceiling remains 1,350 hours, this revision must be shown as
an explicit reallocation of 19 hours from the unallocated reserve: the
qualification row becomes 129 hours and the reserve becomes 69 hours. The
cumulative total does not change, but contingency is materially smaller. No
owner approval or resource availability is implied by balancing the worksheet.

Any timing overrun, roster shortfall, repeat burden, adjudication excess,
metadata-yield shortfall, or simulation-driven design expansion can break the
ceiling. Resource owners must approve the revised row; the budget cannot be
made to fit by reducing the 108 floor or weakening the reader gate.

The fixed 120,000-replication operating-characteristic grid, including the
nested 9,999-resample analysis, is not asserted to fit any current compute
ceiling. Before implementation, a bounded brief must enumerate unique cells,
operations, storage, parallelism, software, and projected cost. If it does not
fit, `G0-READERS`/`G0-MV-Q` remain simulation-blocked until an equally valid
pre-data redesign is approved; replication counts may not be shortened after
inspecting favourable cells.

TB-0009 compiles that candidate manifest and hardware-neutral logical workload
in the [simulation resource-feasibility audit](simulation_resource_feasibility_audit.md).
It finds 10,847 reliability candidates, `K_plan=4,416`, and 2,438
pre-calibration `MV-1` candidates, but no runtime, storage, affordability, or
capacity fact. The contract therefore remains resource- and simulation-
blocked.

## Finite Owner Choice

### `G0-READERS`

- **A — recommended:** approve the axis-specific nominal-alpha package,
  150-cluster allocation, exact bootstrap/missingness rules, repeats,
  hierarchical sensitivity, and pre-reader simulation contract.
- **B:** replace the coefficient, allocation, roster, or dependence model
  prospectively and rerun the entire precision/workload design.

### `G0-MV-Q`

- **A — recommended:** reserve 150 candidates per report-screen stratum,
  retain 108 evaluable per independent polarity, approve the selected/evaluable
  finite-roster estimand, joint q/polarity gate, panel schedule, simulation
  criteria, and approximately 129-hour planning row.
- **B:** retain 128 per report-screen stratum while explicitly accepting that
  joint yield requires approximately 88.7% pair evaluability even under the
  idealized benchmark; remain feasibility-blocked until the complete approved
  simulation supports it.
- **C — reject `MV-1`:** do not lower the 108-per-polarity floor, weaken
  `0.10`, reuse sibling readers, condition eligibility on model/q results, or
  claim reader-population generalization from the fixed roster as a substitute
  for a valid qualification design.

No option is selected by this audit.

## Stop Rules and Permitted Claim

Stop before reader contact if the clinical owner rejects an axis/category,
required quota, credential rule, disjoint roster, state-preservation rule, or
probability-rating interface; if governance/ethics/compensation is unresolved;
if simulation fails operating criteria; or if the revised resource plan is not
approved.

The permitted claim is limited to:

> The repository contains a pre-specified reader-measurement and `MV-1`
> qualification analysis candidate, plus deterministic synthetic yield
> arithmetic showing that the prior 256-candidate reservation is fragile.

It does not establish reliability, image truth, `MV-1` task relevance,
evaluable yield, clinical validity, reader-population generalization,
feasibility, Gate-0 closure, Main Track fit, acceptance, or publication.
