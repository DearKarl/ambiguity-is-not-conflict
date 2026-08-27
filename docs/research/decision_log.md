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
- cross-backbone breadth and independent/natural stress set;
- final NeurIPS 2027 track and deadline after the official call.
