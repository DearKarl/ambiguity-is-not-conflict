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
  clinician-reviewed controlled subset, and ReXErr only as a MIMIC-derived
  synthetic stress test.
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

## DR-0007 — Gate-0 Atomic Route Recommendation

- **Date:** 2026-08-29
- **Status:** Proposed; not approved and not executable
- **Verified literature facts:** Existing work already defines modality
  conflict, uncertainty-adjusted confident disagreement, evidential
  conflict/vacuity, dissent-versus-ambiguity regimes, controlled conflict under
  varying unimodal difficulty, and paired conflict/degradation benchmarks. The
  audited primary sources and explicit claim boundaries are recorded in the
  [novelty audit](novelty_audit.md).
- **Verified data facts:** MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 are one
  restricted coupled source. Their structured labels and test annotations are
  report-derived or report-annotated. ReXErr is MIMIC-derived. Official-source
  access and rights findings are recorded in the
  [dataset feasibility audit](dataset_feasibility_audit.md).
- **Inference:** Those prior works make the broad “first conflict estimator
  after accounting for modality uncertainty” claim unavailable. Report-side
  labels cannot independently define image truth or image ambiguity, and ReXErr
  cannot supply independent breadth. The narrowest defensible first route is
  an asymmetric, image-grounded, single-finding task requiring independent
  verification that the prescribed exact frontal input is complete and that
  determinate source cases can receive an image-only state, with a
  counterbalanced atomic text assertion. Pleural-effusion
  presence/absence is provisional. Conflict is defined only for determinate
  image and text states; genuine ambiguity, missingness, and corruption form
  separate controls in a declared fractional design.
- **Proposed construct package:** Independently elicit image-only and text-only
  interpretation distributions; treat ambiguity-adjusted excess disagreement
  only as a semantic-distribution diagnostic pending an analytic equivalence
  screen, not as conflict in ambiguous cells; validate every candidate through
  a within-source conflict contrast and an identified specificity margin using
  only valid randomized or counterbalanced controls; keep natural-ambiguity
  comparisons as separate conservative falsification audits; and use a matched
  deterministic compatibility/density-ratio predictor as an exact kill
  comparator. Full ambiguity-separation identification requires a valid
  governed intervention or separately defended exchangeability and transport
  assumptions. The energy-distance-like quantity is not itself a novelty claim
  or a selected estimator.
- **Proposed data package:** Treat coupled MIMIC as the conditional primary
  route, VisMin as the preferred low-friction general-domain stress candidate
  only with added construct controls, PadChest-GR as the preferred independent
  medical reserve pending rights clarification, and ReXErr as stress evidence
  only.
- **Governance boundary:** No data/model access, download, unapproved
  hosted-API use, clinical annotation, synthetic clinical editing,
  implementation, or experiment is authorized. Restricted MIMIC content and
  record-level derivatives must not enter Codex/ChatGPT, GitHub, or CI. Derived
  datasets, annotations, embeddings, checkpoints, and weights remain restricted
  pending written permission.
- **Approval required:** The Commander and relevant clinical/governance owner
  must approve the exact finding/image input, annotation and reliability
  thresholds, governed ambiguity intervention or explicit
  identification/claim-narrowing rule, downstream error outcome, numerical
  smallest effects, deterministic-subsumption margin, power and budget, data
  versions/access and secure environment, permitted artifacts, and breadth
  route in a later dated decision.
- **Kill boundary:** Reject before implementation any score that is a monotone
  transform or minor parameterization of known uncertainty-adjusted
  disagreement. Kill the Main Track estimator claim if existing evidential or
  matched deterministic methods meet the frozen specificity and downstream
  equivalence margins. Passing Month 3 remains necessary, not sufficient.
- **Permitted claim:** This record is a decision packet only. It is not Gate-0
  closure, novelty proof, research evidence, data authorization, publication
  prediction, or clinical-value evidence.

## DR-0008 — Gate-0 Freeze Candidate and Explicit Claim-Narrowing Choice

- **Date:** 2026-08-29
- **Status:** Proposed; requires Commander, clinical, governance, statistical,
  and resource approval; not executable
- **Verified facts:** MIMIC report-derived labels cannot independently define
  exact-image truth or ambiguity. Explicit model documentation places BioViL-T
  in MIMIC/MIMIC-CXR pretraining, while BiomedCLIP and SigLIP2 do not provide a
  patient-level MIMIC exclusion manifest. Signed nuisance responses can cancel
  in `abs(E[D_j])`. Multi-reader disagreement can reflect reader error rather
  than genuine item ambiguity. The evidence and boundaries are recorded in the
  [dataset decision candidate](dataset_decision_candidate.md),
  [backbone audit](execution_budget_and_backbone_audit.md),
  [annotation protocol](annotation_and_intervention_protocol.md), and
  [statistical plan](statistical_analysis_plan.md).
- **Inference:** The strongest currently defensible first claim is controlled
  determinate-conflict specificity against valid paired information-loss and
  surface controls, with natural ambiguity retained as an independently
  measured falsification audit. Blur, crop, compression, truncation, evidence
  removal, and an explicit hedge cannot be relabelled as genuine ambiguity.
  Full H2 ambiguity-separation identification remains unresolved unless a
  valid governed intervention or separately justified exchangeability/
  transport estimand is approved.
- **Proposed task/data decision:** Use pleural-effusion presence/absence as the
  provisional single finding and a strict one-image, one-frontal-view MIMIC
  study as the candidate unit. Before any record access, freeze coupled
  MIMIC-CXR/JPG v2.1.0, a secure environment, exact restricted metadata fields,
  keyed patient partitions, aggregate-only outputs, and screening floors. A
  later Stage-B brief may authorize only the frozen metadata feasibility query;
  it does not authorize images, reports, annotation, model use, or experiments.
- **Proposed measurement decision:** Use five-reader image evidence per locked
  item with disjoint sibling panels where required, a total image roster of at
  least ten for two image siblings, and total text/cross-modal rosters of at
  least six for disjoint unanimous three-reader polarity panels. Preserve raw independent
  distributions and label `C*` undefined whenever either modality is
  ambiguous, missing, task-critically corrupted/lost, or semantically
  indeterminate. A prospectively frozen interpretable/recoverable loss may
  retain its determinate semantic state; `M_v/M_t` exposure is recorded
  separately and cannot be relabelled ambiguity. Candidate
  reliability gates are primary coefficient at least 0.80, lower 95% bound at
  least 0.67, observed agreement at least 0.85, and class-specific positive
  agreement at least 0.75 on every gating axis.
- **Proposed statistical decision:** Make
  `psi_mag = min_j E[D_C - abs(D_j)]` the primary construct endpoint on the
  frozen compatible-reference SD scale; retain signed `psi_id` as a diagnostic.
  Candidate specificity SESOI is 0.20 and material advantage over the matched
  deterministic predictor is 0.10; scale-free `theta` is secondary unless
  separately powered. The proposed two-control cardinality requires one exact
  clinically approved `M_v` and one exact `M_t` operation, severity,
  acceptance rule, and reference; none is yet frozen. Exactly one primary
  uncertainty-aware method must be named from development before Month 3, with
  every other candidate secondary. Month 3 uses one-sided 90% simultaneous development
  bounds and an operational floor of 216 balanced evaluable independent
  patients under the stated assumptions; confirmation
  uses one-sided 97.5% bounds and approximately 320 patients for two controls
  or 400 for four. These are planning assumptions, not power facts.
- **Proposed downstream decision:** Use Brier-skill increment for independently
  labelled image-grounded task error, with candidate SESOI 0.02; require an
  uncertainty-minus-deterministic `A_BSS` margin of 0.01; require an
  equivalence-based calibration gate; and use risk at 90% answer coverage as
  the candidate decision endpoint with 0.01 absolute-risk SESOI. This portion
  is not power-ready until target prevalence, paired loss variance/covariance,
  model complexity, calibration sample, loss, and review cost are frozen.
- **Proposed model/resource decision:** Treat BiomedCLIP as a conditional
  primary candidate, SigLIP2 as unknown-exposure matched breadth, a ResNet-50
  plus BiomedBERT pair as a lower-intent unknown-overlap non-VLM architectural
  control, BioViL-T as a known-
  exposure diagnostic, and Qwen2.5-VL as an interface stress candidate. No
  pretrained VLM is yet unconditionally confirmatory on MIMIC. Candidate
  ceilings are 1 TB restricted storage, 300 GPU-hours through Month 3, 1,500
  cumulative GPU-hours, 400 clinical person-hours through Month 3, and 1,200
  cumulative clinical person-hours. The cumulative worksheet explicitly
  reserves 45 hours for a veto-only natural-ambiguity audit after a Month-3
  pass; that audit is not part of the Month-3 stage ceiling and is not an
  ambiguity-identification result.
- **Assumptions:** Qualified readers can distinguish ambiguity from their own
  uncertainty; strict single-frontal MIMIC pools meet the screening floors;
  secure storage, clinical effort, and compute are actually available; and an
  exposure-audited backbone or explicitly narrowed evidence route can be
  obtained. None is verified.
- **Approval questions:** Approve or reject (1) explicit determinate-claim
  narrowing, (2) finding and exact-image unit, (3) reader roles/rubric/gates,
  (4) magnitude-safe endpoint and all numerical margins, (5) data query,
  partitions, floors, and secure/derived-artifact boundary, (6) checkpoint
  roles and exposure rule, (7) resource ceilings, and (8) downstream target,
  calibration, and decision specifications.
- **Stop boundary:** If explicit claim narrowing is rejected and no valid
  ambiguity route exists, Gate 0 cannot close. If data, reader, artifact,
  exposure, power, or uncertainty-aware material-advantage gates fail, stop or narrow the
  paper; do not manufacture a Main Track method claim.
- **Permitted claim:** A high-rigor Gate-0 freeze candidate now exists. This is
  not approval, Gate-0 closure, data/model/clinical authorization, novelty or
  identifiability proof, empirical evidence, venue readiness, clinical value,
  acceptance, or publication.

## Open Gate 0 Decisions

- approve or reject explicit claim narrowing to determinate-conflict
  specificity while H2 remains unresolved;
- provisional pleural-effusion finding, strict single-frontal-image unit, and
  exact visibility/eligibility rule;
- two-stage MIMIC resource/query record, HMAC partitions, secure access route,
  aggregate outputs, screening floors, and derived-artifact terms;
- five-reader image protocol, text/cross-modal panels, sample, reader model,
  adjudication, reliability thresholds, ethics, and workload;
- primary conflict estimator, matched backbone, and pre-implementation
  equivalence screen against the closest published scores;
- magnitude-safe primary endpoint, compatible-reference scale, 0.20 construct
  threshold, secondary `theta`, simultaneous interval, 0.10 uncertainty-aware
  material-advantage boundary, and 216/320-or-400 operational floors;
- exact one-per-modality `M_v/M_t` operations, severities, acceptance rules,
  and within-source references, plus the single primary method identity before
  Month 3;
- four-probe artifact family, exact probe implementations, `chance + 0.05`
  equivalence margin, and the unresolved 385/624 precision or 1,293/1,976
  family-power burden;
- final task-error outcome, 0.02 Brier-skill increment, 0.01 `A_BSS` method-
  difference margin, calibration tolerances, target prevalence/covariance/
  power, 90% coverage budget, and 0.01 risk margin;
- target-distribution cohort and any prevalence weighting;
- conditional checkpoint shortlist/exposure audit and proposed 1-TB,
  300/1,500-GPU-hour, and 400/1,200-clinical-person-hour ceilings;
- pre-specified distribution shift and subgroup set;
- cross-backbone breadth and the governed choice of a second medical dataset
  or small controlled general-domain benchmark;
- final NeurIPS 2027 track and deadline after the official call.
