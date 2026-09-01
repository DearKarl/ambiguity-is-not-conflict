# Scope Charter

**Status:** Canonical one-paper boundary

**Decision:** DR-0002, DR-0006, and DR-0016

## Title-Level Direction

**Working paper title:** *Ambiguity Is Not Conflict: Intervention-Identified
Measurement of Cross-Modal Conflict Specificity*

The paper will test whether a frozen cross-modal score has an
intervention-relative population response specific to determinate semantic
incompatibility, then whether that measured response adds calibrated and
decision-relevant information beyond simpler baselines.

The current freeze candidate does not pretend that goal is already identified.
It permits an initial determinate-conflict specificity claim against valid
paired controls, with natural ambiguity as a falsification audit. A full
ambiguity-separation claim remains blocked until a valid governed intervention
or separately defended observational identification/transport route exists.

Chest radiography is the primary validation domain, not part of the scientific
construct or title. Any breadth study must replicate the same construct and
cannot become a second research direction.

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
- controlled matched/conflicting and prospectively frozen `M_v`/`M_t`
  conditions, plus separately recruited observational image/text ambiguity
  veto audits and declared shifts;
- conditional conflict estimands and matched deterministic alternatives;
- probabilistic embeddings, ensembles, approximate-Bayesian methods, output
  semantic uncertainty, and conformal selection as comparisons;
- construct validity, proper scores, calibration, overconfident error,
  risk--coverage, fixed-budget review, and failure-case analysis;
- a pre-specified cross-backbone breadth test and, subject to its own bounded
  data/scope/governance decision, either a second medical dataset or a small
  controlled general-domain benchmark that tests the same construct;
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
| Determinate construct identification | Magnitude-safe paired response to determinate compatibility interventions against approved `M_v`, `M_t`, and artifact controls | The score behaves consistently with determinate-conflict specificity in the tested intervention population |
| Full ambiguity separation | The above plus a valid governed ambiguity intervention or approved exchangeability/transport estimand; natural ambiguity is veto-only | Separation from ambiguity only under the frozen identification assumptions |
| Incremental validity | Held-out improvement beyond frozen confidence and deterministic predictors | Conflict adds predictive information in the tested task |
| Calibration | Proper scores and calibration diagnostics in-domain and under declared shift | Estimated risk is calibrated in the tested populations |
| Decision value | Selective risk or expected utility at equal coverage/review budget | The frozen policy improves the tested retrospective decision outcome |
| Clinical value | Separate prospective or human-factors evidence | Not claimable from the initial paper alone |

## Primary Contribution Boundary

The single intended primary contribution is a partial-construct,
intervention-identified measurement and inference framework whose
interpretation can be falsified. It evaluates a prospectively frozen,
explicitly non-novel instrument and matched deterministic comparator; it does
not claim a new pair-level estimator. The benchmark alone and a new embedding
alone are each insufficient for the intended Main Track framing.

Controlled interventions provide identification evidence; matched held-out
comparisons provide incremental-validity evidence; calibration and selective
review provide downstream decision evidence. These are supports for the one
central contribution, not separate contribution claims. Method A fixes
`PROBVLM-2ADAPTER` as the non-novel primary instrument and
`POINT-2ADAPTER-RECON` as its mean-only deterministic full-route comparator at
the Commander scientific-interface level. They share independently verified
determinate-compatible selection information, the GGD score family, and target
topology; removing probabilistic heads changes capacity and gradient paths, so
no capacity-isolated mechanism claim is permitted. Other method families remain
secondary challenges, with conformal methods as candidate risk-control layers.
Required owners must still approve the executable specification before Gate 0
closes. Failure of the frozen deterministic-advantage gate kills the current
Main Track route; a qualified null or later venue decision must be recorded
without post-hoc repackaging.
