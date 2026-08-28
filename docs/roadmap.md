# Twelve-Month Research Roadmap

**Status:** Planning schedule governed by evidence gates

**Anchor:** Month 0 begins 2026-08-27. Official 2027 venue dates are not yet
assumed; the schedule will be rebased when the call is published.

## Month 0–1 — Freeze the Research Contract

**Outcome:** a supervisor-ready and governance-ready Gate 0 protocol.

- verify novelty against current primary literature and official code;
- choose the atomic finding task, data version, cohort, and patient split;
- formalize the conflict estimand and ambiguity/conflict interventions;
- freeze the primary endpoint, smallest effect, power plan, baselines, shift,
  compute ceiling, annotation plan, and stopping rules;
- obtain required data and clinical-governance decisions.

**Promotion:** all Gate 0 items recorded without unresolved measurement
ambiguity.

**Stop:** no core implementation while the object or data route is unfrozen.

## Month 2–3 — Decisive Kill Test

**Outcome:** determine whether the one primary route deserves scale-up.

- build only the smallest authorized data/estimator pipeline;
- clinician-review a small development-only intervention set;
- compare deterministic similarity, matched deterministic compatibility, and
  at most two uncertainty-aware candidates;
- test paired conflict specificity, ambiguity separation, surface artifacts,
  and preliminary conditional value;
- write a failure audit and Month-3 decision record.

**Promote only if:** reviewers can distinguish the constructs, the intervention
is not trivial, and at least one candidate passes every necessary criterion in
the measurement protocol: stronger response to controlled incompatibility than
to matched controls; persistence after conditioning on `A_v`, `A_t`, `M_v`,
`M_t`, and source; a frozen non-trivial gain over deterministic similarity
without subsumption by the matched deterministic predictor; and artifact,
normalization, leakage, repetition, and failure-case checks.

**Kill or redesign if:** the construct, labels, access, compute, or annotation
route fails the criteria in the measurement protocol.

Passing this development-only gate is necessary but not sufficient for the
Main Track method claim; confirmatory evidence remains required.

## Month 4–5 — Confirmatory Benchmark Construction

**Outcome:** frozen patient-separated intervention benchmark and evaluation
artifact.

- scale the approved finding types and intervention cells;
- complete blinded clinical review and adjudication;
- freeze development, calibration, and final test partitions;
- audit leakage, templating, artifacts, subgroup coverage, and provenance;
- publish only governance-permitted metadata and data documentation.

**Promotion:** dataset card, intervention manifest, reliability evidence, and
cohort audit pass their frozen thresholds.

## Month 6–7 — Estimator and Decomposition Study

**Outcome:** matched comparison of the smallest sufficient estimator set.

- train/evaluate frozen deterministic and uncertainty-aware candidates;
- run required ablations, repeated seeds, and resource accounting;
- test construct specificity and stability under the declared shift;
- run the frozen cross-backbone breadth test and the separately approved second
  medical dataset or small controlled general-domain benchmark testing the same
  construct;
- lock the candidate for final outcome evaluation without inspecting final
  endpoints.

**Stop or narrow:** if the proposed component is unstable, uninterpretable, or
subsumed by a simpler baseline.

## Month 7–8 — Incremental Validity and Calibration

**Outcome:** final held-out evidence for or against the conflict component.

- compare nested risk models on the frozen primary proper score;
- assess calibration intercept/slope, reliability, ranking, shift, and
  subgroups;
- report paired intervals, smallest-effect comparison, negative results, and
  deviations;
- prohibit new method selection after final evaluation begins.

**Promotion:** non-negligible incremental value and acceptable frozen
calibration criteria.

## Month 8–9 — Selective Review and Main Paper

**Outcome:** submission-ready Main Track package, planned as Use-Inspired if an
applicable 2027 contribution type exists, only if all earlier gates pass.

- evaluate `answer | human_review` at equal review budgets or coverage;
- complete ablations, compute statement, limitations, ethics, and
  reproducibility checklist;
- write the paper around estimand, identification, matched evidence, and null
  boundaries;
- choose exactly one track after reading the official NeurIPS 2027 calls;
- prepare anonymized code and artifacts consistent with data licences.

**Submission gate:** independent internal review finds no leakage, post-hoc
endpoint switching, unsupported clinical claim, or missing decisive baseline.

## Month 10–12 — Review, Rebuttal, and Evidence-Preserving Fallback

**Outcome:** respond to review or prepare the same completed research route for
the best-fitting next venue without manufacturing new claims.

- answer reviewer questions with pre-existing or clearly labelled additional
  analysis;
- archive exact submission artifacts and decision records;
- if not accepted or if the deadline is missed, choose one fit-based venue
  family and revise the same paper;
- plan any validation beyond the frozen breadth study only after the primary
  study is complete.

Acceptance is not a milestone under the project's control. A rigorous
submission, reproducible evidence, and a defensible claim are.
