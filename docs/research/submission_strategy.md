# Submission Strategy

**Status:** Primary venue objective selected; 2027 call not yet available

## Primary Objective

Prepare one submission-quality paper for **NeurIPS 2027 Main Track**. This is a
planning target, not a prediction of acceptance. The route remains eligible
only while its scientific contribution is methodologically substantive and
supported by the frozen evidence gates.

The 2026 Main Track call explicitly included computer vision, language and
multimodal models, AI/ML for health, probabilistic methods, decision-making,
and general machine learning. It also welcomed rigorous analysis yielding new
insight into method limitations or behaviour. The 2027 call, policies,
template, dates, and subject areas must be reverified when published.

Official planning references:

- [NeurIPS 2026 Main Track call](https://neurips.cc/Conferences/2026/CallForPapers)
- [NeurIPS paper checklist](https://neurips.cc/public/guides/PaperChecklist)
- [NeurIPS code submission policy](https://neurips.cc/public/guides/CodeSubmissionPolicy)
- [NeurIPS 2026 Evaluations & Datasets call](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)

Historical dates are used only for backwards planning. They are not assumed to
be the 2027 deadlines.

## Main Track Paper Identity

The Main Track narrative should be:

1. **Problem:** existing uncertainty scores conflate within-modality ambiguity
   and between-modality conflict.
2. **Formal contribution:** define a conditional conflict estimand relative to
   compatible-pair structure and unimodal ambiguity.
3. **Method contribution:** estimate the object with a tractable framework that
   is not reducible to a renamed distance.
4. **Identification evidence:** controlled factorial interventions and negative
   controls test the intended interpretation.
5. **Incremental evidence:** matched held-out comparison with deterministic,
   probabilistic, epistemic, and output-uncertainty baselines.
6. **Decision evidence:** calibrated selective review at a frozen budget.
7. **Boundary:** retrospective chest-radiography evidence, not autonomous or
   prospective clinical benefit.

## Main Track Promotion Bar

By the submission decision, the project should have:

- a clear formal estimand and defensible estimator;
- a clinician-validated controlled design that separates ambiguity and
  conflict;
- a non-trivial matched deterministic baseline;
- patient-separated confirmatory evaluation with paired intervals;
- proper scoring, calibration, shift, subgroup, and selective-risk evidence;
- a frozen breadth test across at least two materially different backbone
  families and one independently sourced or naturally occurring stress set;
- reproducible code/configuration and a complete limitation statement;
- an ablation or negative result that clarifies why the method works or fails.

If the main contribution is only a dataset, taxonomy, or evaluation protocol,
the Main Track framing is not strong enough.

If the breadth test cannot be completed, every claim must be restricted to the
tested backbone and intervention population; the review must then decide
whether the remaining contribution still clears the Main Track bar.

## Track Decision Checkpoint

NeurIPS 2026 treated Main Track and Evaluations & Datasets as separate tracks
and prohibited simultaneous submission or later switching between them. When
the 2027 call appears, a single track must be chosen before submission.

Use **Main Track** if the central result is a new estimand/estimation method
with broad machine-learning insight. Consider **Evaluations & Datasets** only
if the enduring contribution becomes the controlled benchmark, annotation
methodology, or evaluation science and the estimator is secondary. This is a
fallback framing of the same research route, not a second project.

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
