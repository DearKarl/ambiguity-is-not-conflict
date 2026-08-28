# Submission Strategy

**Status:** Primary venue objective and provisional contribution type selected;
2027 call not yet available

## Primary Objective

Prepare one submission-quality paper for **NeurIPS 2027 Main Track**. This is a
planning target, not a prediction of acceptance. The route remains a viable
Main Track candidate only while its scientific contribution is
methodologically substantive and supported by the frozen evidence gates.

The working contribution-type classification is **Use-Inspired**, conditional
on the official 2027 rules retaining an applicable category. The classification
does not establish eligibility or venue fit in advance; it states how the
methodological contribution is intended to be evaluated if the 2027 call
supports that framing.

The 2026 Main Track call explicitly included computer vision, language and
multimodal models, AI/ML for health, probabilistic methods, decision-making,
and general machine learning. It also welcomed rigorous analysis yielding new
insight into method limitations or behaviour. The 2027 call, policies,
template, dates, and subject areas must be reverified when published.

Official planning references:

- [NeurIPS 2026 Main Track call](https://neurips.cc/Conferences/2026/CallForPapers)
- [NeurIPS 2026 Main Track handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook)
- [NeurIPS 2026 reviewer guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines)
- [NeurIPS paper checklist](https://neurips.cc/public/guides/PaperChecklist)
- [NeurIPS code submission policy](https://neurips.cc/public/guides/CodeSubmissionPolicy)
- [NeurIPS 2026 Evaluations & Datasets call](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)
- [NeurIPS 2026 Evaluations & Datasets FAQ](https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ)

Historical dates are used only for backwards planning. They are not assumed to
be the 2027 deadlines.

## Venue-Fit Evidence Classification

- **Verified 2026 facts:** the Main Track handbook offered a Use-Inspired
  contribution type for novel methods, tasks, or metrics associated with a
  real-world use case; the reviewer guidelines allowed originality through new
  insight, problem framing, task, metric, method, or a justified combination
  rather than requiring a new architecture; and the call prohibited switching
  between or simultaneously submitting to multiple NeurIPS tracks/types.
- **Inference:** a domain-general conditional-conflict estimand and substantive
  estimator, rigorously validated in chest radiography, could fit that
  contribution logic better than a benchmark-only paper.
- **Assumptions:** an applicable contribution type and compatible track rules
  will exist in 2027, and the currently reported time, compute, data-access,
  and clinical-support plans will become documented resources.
- **Decision:** prepare one Main Track method-and-identification route; recheck
  the official 2027 call before choosing the final track and contribution type.

## Main Track Paper Identity

**Working title:** *Ambiguity Is Not Conflict: Identifiable Cross-Modal
Conflict Estimation for Calibrated Selective Decisions*

The single intended primary contribution is a formal conditional conflict
estimand and estimator or general estimation framework that measures
task-relevant cross-modal incompatibility after accounting for image
ambiguity, text ambiguity, and modality-specific information loss. The
controlled medical benchmark, probabilistic embeddings, calibration analysis,
and selective review support or falsify that contribution; they are not four
independent contributions.

The Main Track narrative should be:

1. **Problem:** existing uncertainty scores conflate within-modality ambiguity
   and between-modality conflict.
2. **Formal component:** define a conditional conflict estimand relative to
   compatible-pair structure and unimodal ambiguity.
3. **Estimation component:** estimate the object with a tractable framework that
   is not reducible to a renamed distance.
4. **Identification evidence:** controlled factorial interventions and negative
   controls test the intended interpretation.
5. **Incremental evidence:** matched held-out comparison with deterministic,
   probabilistic, epistemic, and output-uncertainty baselines.
6. **Decision evidence:** calibrated selective review at a frozen budget.
7. **Boundary:** retrospective chest-radiography evidence, not autonomous or
   prospective clinical benefit.

## Main Track Promotion Bar

By the submission decision, the project must satisfy six scientific
conditions:

1. **Formal contribution and novelty audit:** a defensible
   conditional-conflict definition, identification assumptions, and estimand,
   plus a verified primary-literature audit establishing the distinction from
   prior work—not a renamed distance between two distributions.
2. **Estimator or general framework:** a substantive estimation method that
   can be implemented and challenged by probabilistic, deterministic,
   evidential, ensemble, Bayesian, and output-uncertainty competitors.
3. **Controlled identification:** compatibility interventions change the
   score specifically while image ambiguity, text ambiguity, missingness,
   corruption, length, prevalence, source, and representation scale are held,
   balanced, conditioned on, or tested as negative controls.
4. **Incremental validity:** adding the frozen conflict component improves the
   pre-specified held-out proper score by more than the smallest effect of
   interest beyond unimodal measures, ordinary confidence, epistemic/output
   uncertainty including semantic entropy, and a matched deterministic failure
   predictor.
5. **Broader relevance:** the result replicates across at least two materially
   different VLM backbone families and, subject to a separate bounded
   data/scope/governance decision, either a second medical dataset or a small
   controlled general-domain benchmark testing the same construct.
6. **Decision evidence:** the frozen policy reduces selective risk or regret
   at equal coverage or human-review budget without claiming clinical benefit.

Cross-cutting submission requirements remain patient-separated confirmatory
evaluation with paired intervals, calibration under a declared shift,
pre-specified subgroup analysis, reproducible code/configuration, complete
limitations, and an ablation or negative result that explains where the method
works or fails.

If the main contribution is only a dataset, taxonomy, or evaluation protocol,
the Main Track framing is not strong enough.

If the breadth test cannot be completed, every claim must be restricted to the
tested backbone and intervention population; the review must then decide
whether the remaining contribution still clears the Main Track bar.

## Month-3 Main Track Kill Gate

The development-only gate in the measurement protocol is passed only if at
least one frozen candidate:

- responds more strongly to controlled incompatibility than to matched
  ambiguity, missingness, and corruption controls;
- retains a non-negligible effect after conditioning on `A_v`, `A_t`, `M_v`,
  `M_t`, and source;
- exceeds deterministic similarity by a pre-specified non-trivial margin and
  is not fully subsumed by the matched deterministic compatibility/failure
  predictor;
- survives artifact, representation-scale/normalization, leakage, repetition,
  and failure-case checks.

Failure removes the Main Track method claim rather than triggering post-hoc
repackaging. Passing is necessary but not sufficient: confirmatory,
calibration, breadth, decision, and reproducibility gates still remain.

## Track Decision Checkpoint

NeurIPS 2026 treated Main Track and Evaluations & Datasets as separate tracks
and prohibited simultaneous submission or later switching between them. When
the 2027 call appears, a single track must be chosen before submission.

Use **Main Track** if the central result is a new estimand/estimation method
with broad machine-learning insight. **Evaluations & Datasets is retained only
as a pre-submission contingency** if the enduring contribution becomes the
controlled benchmark, annotation methodology, or evaluation science and the
estimator is secondary. This is a fallback framing of the same research route,
not a second project or a simultaneous submission.

## Other Venue Families if Timing or Evidence Changes

- **ICLR or ICML:** method-first uncertainty, representation, or evaluation
  contribution with broad ML evidence;
- **UAI:** stronger probabilistic or Bayesian methodology and uncertainty
  analysis;
- **MIDL or MLHC:** medical-imaging/health-method contribution with rigorous
  clinical task definition;
- **Medical Image Analysis or Journal of Biomedical Informatics:** expanded
  medical validation and analysis when journal depth fits better.

These are contingency families, not concurrent targets. Current calls and
policies must be verified at the decision date.

## Submission Stop Conditions

Do not submit the Main Track version if the conditional conflict object is not
identifiable, the proposed estimator is subsumed by a matched deterministic
predictor, confirmatory evaluation leaks patient/source information, the main
result depends on post-hoc endpoint selection, or clinical claims exceed the
evidence. A rigorous negative paper may be redirected only through a recorded
venue-fit decision.
