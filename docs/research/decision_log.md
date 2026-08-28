# Decision Log

This file records scope-changing decisions. Facts, inferences, assumptions, and
decisions are separated explicitly.

## DR-0001 — Standalone Project Identity

- **Date:** 2026-08-27
- **Status:** Approved by the Commander
- **Decision:** Create a standalone repository named
  `ambiguity-is-not-conflict` with the public title **Ambiguity Is Not
  Conflict**.
- **Reason:** The concrete paper route should not inherit unrelated Bayesian
  regression, text-only pilot, or legacy programme artifacts.
- **Boundary:** Preserve scientific continuity through sanitized canonical
  documents only; do not copy raw correspondence, private handoffs, restricted
  data, or unrelated evidence.

## DR-0002 — One Primary Scientific Route

- **Date:** 2026-08-27
- **Status:** Approved in principle by the Commander
- **Decision:** The single primary route is controlled identification of
  conditional cross-modal conflict relative to image ambiguity and text
  ambiguity, followed only upon promotion by calibration and selective-review
  evaluation.
- **Fact:** The supervisory discussion positively received uncertainty-source
  explanation, ambiguity-versus-conflict separation, distributional
  representations as a candidate, and decision use under overconfidence.
- **Inference:** A conditional estimand plus falsifying interventions offers a
  stronger novelty route than selecting a Gaussian embedding or divergence.
- **Reopening condition:** A Month 2–3 kill test shows the construct is not
  identifiable or the clinical task cannot support the contrast.

## DR-0003 — Primary Validation Route

- **Date:** 2026-08-27
- **Status:** Candidate; requires Gate 0 and governance approval
- **Decision:** Plan around atomic findings in chest radiograph--report pairs,
  with MIMIC-CXR/JPG as the candidate patient-level source, a
  clinician-reviewed controlled subset, and ReXErr only as an external stress
  test.
- **Assumptions:** Timely access, defensible finding labels, clinician time, and
  permitted derived artifacts.
- **Stop condition:** Do not access data until the dataset decision record and
  governance route are approved.

## DR-0004 — Submission Objective

- **Date:** 2026-08-27
- **Status:** Approved planning decision
- **Decision:** Target NeurIPS 2027 Main Track with a method-and-identification
  paper. Publication or acceptance is not guaranteed.
- **Fact:** The 2027 call is not yet authoritative. The 2026 call is used only
  for scope and backwards-planning evidence.
- **Track boundary:** Choose exactly one eligible NeurIPS track after the 2027
  calls are published; do not submit the same work simultaneously to Main and
  Evaluations & Datasets.
- **Reopening condition:** The scientific contribution becomes primarily an
  evaluation resource, misses the confirmed calendar, or fails the Main Track
  promotion bar.

## DR-0005 — Initial Repository and GitHub Boundary

- **Date:** 2026-08-27
- **Status:** Approved for implementation
- **Decision:** Build a formal documentation-first repository, initialize a
  fresh Git history, create a GitHub repository following the current owner's
  naming convention and public visibility, register it in Codex, and create
  the five standard role lanes.
- **Allowed:** Canonical documents, governance, CI, citation metadata,
  placeholders, and repository-contract tests.
- **Forbidden:** Core code, experiments, dataset/model downloads, clinical
  annotation, private correspondence, and inherited legacy artifacts.
- **Licence:** No open-source licence is silently granted; licensing remains a
  recorded pre-release decision.

## DR-0006 — Main Track Paper Identity and Promotion Boundary

- **Date:** 2026-08-29
- **Status:** Approved planning clarification by the Commander
- **Decision:** Keep NeurIPS 2027 Main Track as the primary strategic target
  and plan the paper as **Use-Inspired** if the official 2027 rules retain an
  applicable contribution type. The single intended primary contribution is a
  formal conditional-conflict estimand plus an estimator or general estimation
  framework; chest radiography remains the primary validation domain rather
  than part of the title or scientific construct.
- **Verified facts:** The 2026 Main Track handbook defined a Use-Inspired type
  around novel methods, tasks, or metrics associated with a real-world use
  case. The 2026 reviewer guidance did not require originality to take the
  form of a new architecture. The 2026 call prohibited track/type switching
  and simultaneous submissions across NeurIPS tracks/types. Official links and
  the evidence classification are recorded in the
  [submission strategy](submission_strategy.md#venue-fit-evidence-classification).
- **Inference:** A domain-general estimand and non-trivial estimator supported
  by controlled medical evidence is more defensible as a Main Track method
  paper than a benchmark comparison or renamed distributional distance.
- **Assumptions:** The 2027 call will retain compatible contribution and track
  rules; time, compute, dataset access, and clinical support will become
  documented resources rather than planning expectations.
- **Evidence boundary:** Controlled medical benchmarking, candidate
  probabilistic embeddings, calibration analysis, and selective review are
  evidence for or against the central contribution—not parallel contribution
  claims. Passing the Month-3 development gate is necessary but not sufficient
  for Main Track readiness and cannot be promoted as confirmatory evidence.
- **Breadth boundary:** The Main Track plan seeks replication across at least
  two materially different VLM backbone families and, after a separate bounded
  data/scope/governance decision, either a second medical dataset or a small
  controlled general-domain benchmark testing the same construct. Neither
  option is authorized for execution by this decision.
- **Track contingency:** Evaluations & Datasets is only a pre-submission
  fallback for the same route if the enduring result is evaluation science and
  the estimator is secondary. The same paper will not be submitted to both.
- **Reopening condition:** Reassess after the official 2027 calls appear, if
  the Month-3 method gate fails, if the matched deterministic predictor
  subsumes the candidate, if breadth or confirmatory evidence cannot be
  defended, or if the scientific contribution becomes primarily an evaluation
  resource.
- **Permitted claim:** This is a submission-planning decision, not evidence of
  construct identifiability, 2027 eligibility, acceptance, publication, or
  clinical benefit.

## Open Gate 0 Decisions

- atomic finding ontology and exact prediction unit;
- MIMIC resource/version and approved access route;
- natural versus edited intervention mixture;
- clinician rubric, sample, adjudication, and reliability threshold;
- primary conflict estimator and matched backbone;
- exact primary estimand, smallest effect, and power target;
- final risk outcome and calibration tolerance;
- target-distribution cohort and any prevalence weighting;
- compute ceiling and reproducibility budget;
- pre-specified distribution shift and subgroup set;
- cross-backbone breadth and the governed choice of a second medical dataset
  or small controlled general-domain benchmark;
- final NeurIPS 2027 track and deadline after the official call.
