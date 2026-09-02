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
  acceptance rule, and reference; none is yet frozen. The canonical contract
  requires exactly one primary uncertainty-aware estimator definition/interface
  and matched comparator route at Gate 0; development may fit/tune only within
  those rules, and their fitted instances lock before Month 3. Month 3 uses one-sided 90% simultaneous development
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
  plus original-BERT pair as a source/type/time-auditable strict non-VLM
  control lead, BioViL-T as a known-
  exposure diagnostic, and Qwen2.5-VL as an interface stress candidate. No
  pretrained VLM is yet unconditionally confirmatory on MIMIC. Candidate
  ceilings are 1 TB restricted storage, 300 GPU-hours through Month 3, 1,500
  cumulative GPU-hours, 400 clinical person-hours through Month 3, and 1,200
  cumulative clinical person-hours. These earlier clinical ceilings are
  superseded as planning candidates by DR-0009 after adding the independent
  `MV-1` task-relevance qualification. The cumulative worksheet explicitly
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

## DR-0009 — Finite Gate-0 Decision Package and Staged Locks

- **Date:** 2026-08-29
- **Status:** Proposed; every named owner choice remains open and non-executable
- **Verified facts:** Primary observer studies show that chest-image resolution
  and compression effects are task/severity dependent, not universally
  semantics-preserving. A calibrated dose-like simulation requires acquisition/
  detector assumptions absent from post-processed JPG. Primary radiology
  schemas distinguish positive, negative, uncertain, and missing/no-proposition
  text states. Official model documentation gives explicit MIMIC exposure for
  BioViL-T but no patient-level exclusion manifest for BiomedCLIP or SigLIP2.
  Sources and transfer limits are recorded in the
  [intervention audit](intervention_option_audit.md),
  [literature matrix](literature_matrix.md), and
  [backbone audit](execution_budget_and_backbone_audit.md).
- **Inference:** For a truly atomic binary assertion, target-state information
  cannot be removed while retaining a unique fully recoverable `Y_t`; the
  coherent primary text-loss option therefore makes `Y_t` undefined and must
  not be called ambiguity. Exact 2x2 construction balance can eliminate
  enumerated isolated-modality/process marginals, while learned probes remain
  lower-bound falsification instruments rather than proof of artifact absence.
  The canonical contract requires one exact primary estimator/interface before
  core development; development locks its fitted instance and configuration
  before the Month-3 holdout rather than choosing an estimator identity from
  protected outcomes.
- **Proposed decision package:** Approve the narrower determinate-conflict
  specificity route; provisionally retain the single-frontal pleural-effusion
  task; use only `MV-1` antialiased `224 -> 112 -> 224` resolution attenuation
  with preserved image polarity **conditional on** a disjoint reader-based
  equal-polarity `q_v,bal` task-evidence gate whose one-sided 95% lower bound is
  strictly above `0.10` with at least 108 evaluable blocks per independently
  assigned image polarity, and `MT-1` sole-polarity-slot redaction with undefined text state;
  keep natural ambiguity veto-only; use construction
  balance plus orientation-safe diagnostic recoverability
  `R=max(BA,1-BA)`; and adopt strict-confirmatory, unknown-exposure sensitivity,
  and known-exposure diagnostic model tiers.
- **Inference decision:** The finite candidate uses a nonparametric,
  patient-cluster studentized max-`t` bootstrap with exactly 9,999 fixed-seed
  resamples (seed `20270829`), common within-stratum patient resamples across
  all method-by-control means, and componentwise simultaneous bounds. The
  non-smooth `psi_mag` and `A_psi` bounds are derived from those joint component
  bounds rather than bootstrapped directly. Month 3 uses one-sided 90% bounds
  (`alpha_F=0.10`, 80% target family power); confirmation uses one-sided 97.5%
  bounds (`alpha_F=0.025`, 90% target family power), a fixed construct-to-
  advantage-to-downstream-to-decision sequence, and Holm or Romano--Wolf
  control for secondary families. Commander/statistical approval remains open;
  Month 3 cannot establish confirmation or equivalence.
- **Baseline/ablation decision:** In addition to the finite baseline identities,
  freeze removal of `C_vt`; separate removal of `A_v`, `A_t`, `M_v`, and `M_t`;
  matched point-softmax/point-embedding replacement; fixed-mean scale/covariance
  removal where applicable; raw-SD versus median/MAD normalization; and four
  modality/nuisance/provenance recovery views. Exact implementations, licences,
  and applicability mapping remain Gate-0 blockers.
- **Artifact decision:** The recommended current-budget option makes structural
  balance an instrument invariant and learned probes veto-only. Any lower bound
  for `R` above `0.55` kills; crossing `0.55` is inconclusive; an upper bound
  below it supports only the exact frozen-probe/population statement. A formal
  four-probe equivalence claim requires a separately simulated and funded
  design. Orientation-safe crude IUT planning is approximately 1,047/1,757
  evaluable Month-3/confirmation patients, already outside current ceilings;
  the Month-3 figure is a non-promotable developmental screen and cannot
  establish equivalence.
  No margin may be widened to fit budget without a prospective consequence-
  based justification.
- **Checkpoint decision:** BiomedCLIP, SigLIP2, and Qwen remain unknown-exposure
  sensitivity; BioViL-T remains known-exposure diagnostic. Strict evidence
  requires a cleared manifest/source route, development-only representation,
  or sequestered/post-checkpoint cohort. A ResNet-50 plus original-BERT pair is
  only a source/type/time-auditable strict non-VLM control lead. Without a
  strict route, prohibit clean-checkpoint/strict-heldout wording and narrow the
  generalization claim.
- **Staging decision:** Gate 0 freezes the task/unit, data/governance,
  interventions, exact estimator definition/interface, exact comparator route,
  backbone revisions, baseline/calibration implementations, partitions/
  sampling, breadth identity/snapshot, resources, and promotion/stopping logic.
  A later development brief remains bounded to HMAC bucket 0--69 and may only
  fit/tune within those rules; the fitted estimator/comparator instances,
  normalizers, probes, code, and configurations lock before bucket 70--84;
  strict evidence and full patient-clustered construct/probe/target power must
  lock before confirmation.
- **Open owners:** The complete finite Commander, clinical, statistical,
  governance, infrastructure, resource, and model-owner choices are in the
  [Gate-0 decision dossier](gate0_decision_dossier.md). No check box is signed.
- **Resource revision:** Adding the disjoint, crude 256-screened/216-evaluable
  balanced `MV-1`
  qualification without reusing the 150-unit image reliability set changes the
  proposed clinical planning ceiling to 500 hours through Month 3 and 1,350
  cumulative. This is a worksheet consequence, not
  verified availability; the Commander, clinical, resource, and infrastructure
  owners must approve or replace it.
- **Qualification partition:** Within official-train HMAC bucket 0--69, a
  separate governed `AINC/v1/mv1-qualification` rank reserves 128
  strict-single-frontal metadata candidates per positive/negative report-screen
  sampling stratum (256 total) before model fitting. They are excluded from
  reader training/reliability, fit/development, Month 3, confirmation,
  calibration, and target evidence. Report-screen polarity is not image truth;
  later independent readers must yield at least 108 evaluable blocks per intact-
  image polarity. A shortfall in either state stops `MV-1`; this rule is not
  data-access authorization.
- **Supersession note:** TB-0008/DR-0011 retains this entry as history but
  recommends replacing its crude 128-per-stratum reservation and unspecified
  reader precision with the exact 150-per-stratum `G0-MV-Q A` package. Neither
  version is approved.
- **Stop boundary:** Rejection/non-verification leaves Gate 0 open; failure of
  either exact control, construction balance, reader reliability, checkpoint
  tier, power/resources, `psi_mag`, `A_psi`, or downstream `A_BSS` invokes the
  documented kill/narrow rule. Do not select replacement controls or margins
  after candidate-score inspection.
- **Permitted claim:** The repository contains a finite blocker/choice inventory
  and staged authorization map, not a complete Gate-0 freeze package. This is not owner approval, Gate-0
  closure, ambiguity identification, intervention validity, data/model/reader
  authorization, scientific evidence, venue readiness, acceptance, or
  publication.

## DR-0010 — Pointwise Estimator Formalization Kill

- **Date:** 2026-08-29
- **Status:** Proposed kill recommendation; requires Commander, scientific-
  supervisor, statistical, and model-owner decision; not executable
- **Verified source facts:** PCME++'s Gaussian closed-form sampled distance adds
  mean squared distance and marginal variances; RCML defines projected
  probability distance times conjunctive certainty; Discounted Belief Fusion
  supplies conflict-sensitive evidential fusion; and classifier-based
  density-ratio estimation is established prior art. Exact sources and transfer
  limits are in the [formalization audit](estimator_formalization_audit.md).
- **Non-authoritative lead:** CONFER arXiv v1 reports squared scalar predictive
  disagreement divided by summed modality uncertainty. Its preprint status
  excludes it from the formal novelty kill and mandatory-baseline decision.
- **Derivations:** For binary learned model beliefs, self-corrected
  disagreement is exactly
  \((\widehat p_v-\widehat p_t)^2\). Independent-Gaussian self-spread correction
  cancels covariance and leaves mean distance. A conditional
  conflict/compatibility likelihood ratio is exactly a classifier logit minus
  the known sampling-prior log-odds. Binary evidential
  projected-distance-times-certainty is
  \(|\widehat p_v-\widehat p_t|(1-u_v)(1-u_t)\), the occupied RCML
  form.
- **Decision recommendation:** Select none of the three pointwise candidates
  and kill their new-estimator claim before implementation. Retain
  \(\widehat\psi_{mag,m}\) as the exact finite-sample plug-in estimator of the
  controlled-score-specificity population functional, not as an arbitrary-pair
  conflict score. The outer minimum makes it generally downward biased at
  finite \(n\).
- **Finite owner choice:** `G0-METHOD A` prospectively amends the paper identity
  to an intervention-defined measurement/validation framework and freezes one
  explicitly non-novel pointwise instrument plus a matched deterministic
  comparator. `G0-METHOD B` retains a new-estimator identity only if a new
  bounded pre-data theory brief supplies one non-cosmetic candidate that
  survives the same equivalence screen. A is recommended; neither is approved.
- **Link guardrail:** The compatible-reference normalization removes positive
  affine transformations, not nonlinear monotone links. Every candidate and
  matched comparator must use the identical square, sigmoid, exponential, or
  pre-link convention; otherwise `A_psi` can be manufactured by
  parameterization.
- **Inference:** The controlled intervention/reader design may remain a
  substantive evaluation-science contribution, but this audit does not prove
  that framework novel or sufficient for NeurIPS Main Track. Main Track remains
  a conditional planning target, not a publication prediction.
- **Stop boundary:** Gate 0 remains open. No data/model/reader access,
  implementation, training, inference, or Month-3 execution follows this
  record. Empirical performance cannot reverse the analytic identity or select
  among killed formulas.
- **Permitted claim:** Three finite pointwise candidate classes failed the
  pre-data novelty/equivalence screen, and the existing population specificity
  estimator now has an exact interface. This is not owner approval, empirical
  deterministic subsumption, framework novelty, construct validation, venue
  readiness, acceptance, or publication.

## DR-0011 — Reader Measurement and MV-1 Qualification Candidate

- **Date:** 2026-08-29
- **Status:** Proposed protocol recommendation; requires Commander, clinical,
  statistical, ethics, governance, infrastructure, and resource-owner
  decisions through `G0-READERS`, `G0-MV-Q`, `G0-DATA`, and `G0-RESOURCES`;
  simulation- and feasibility-blocked; not executable
- **Repository facts:** The prior protocol fixed five-reader image panels, a
  150-cluster reliability phase, at least 108 evaluable `MV-1` blocks per
  independent image polarity, and a 128-per-report-screen-stratum reservation,
  but it did not freeze the primary reliability coefficient, exact interval,
  finite-reader claim, joint polarity gate, or complete simulation contract.
- **Deterministic planning fact:** Under the explicitly idealized assumptions
  of perfect report-screen polarity and independent equal pair yield, 128
  candidates per polarity has joint probability `0.404356` of reaching both
  108 floors at 85% yield and requires approximately `0.887019` yield for 90%
  joint probability. With 150 candidates, 80% yield gives `0.986107` joint
  probability and the 90% threshold is approximately `0.773382`. This is
  synthetic arithmetic, not MIMIC, reader, or intervention evidence.
- **Inference:** The qualification target is conditional on prospective
  screening, same-polarity evaluability, the locked finite reader roster, and
  its panel schedule. It cannot support all-patient or reader-population
  generalization. A balanced attenuation can hide a null or reversed polarity,
  so polarity-specific positive guardrails are necessary.
- **Assumptions:** Candidate counts, report-screen fidelity, pair yield,
  reader credentials/availability, per-rating time, ethics, access, and budget
  are unverified. The yield table's independence and perfect-screen assumptions
  are deliberately optimistic.
- **Reader recommendation (`G0-READERS A`):** Use nominal Krippendorff alpha
  separately for every categorical gate with the exact 150-cluster marginal
  allocation, 9,999-resample patient/source-cluster percentile interval, macro
  and class-specific agreement formulas, missingness/repeat rules,
  hierarchical sensitivities, and a complete pre-reader simulation. No failed
  axis may be averaged away or rescued by a sensitivity coefficient.
- **Qualification recommendation (`G0-MV-Q A`):** Reserve 150 candidates per
  report-screen stratum (300 total); retain 108 evaluable blocks per independent
  polarity; use the selected/evaluable finite-roster estimand, cyclic disjoint
  ten-reader panels, and a 9,999-resample joint one-sided max-`t` gate requiring
  `L_bal > 0.10`, `L_present > 0`, and `L_absent > 0`, plus the frozen
  reader/panel sensitivity veto. No model score may affect screening,
  eligibility, severity, replacement, or qualification.
- **Resource consequence:** Linear scaling changes the qualification row from
  110 to 129 hours, the first-four-phase total from 467 to 486, and—if the
  cumulative 1,350-hour ceiling is retained—the unallocated reserve from 88 to
  69 hours. This balances a worksheet but does not verify capacity.
- **Kill boundary:** No annotation brief may issue until owners approve the
  instrument and roster, ethics/governance/resources are resolved, and the
  exact pre-reader simulation meets coverage, false-qualification, joint-yield,
  joint-power, and Monte-Carlo precision rules. Failure reopens or kills
  `MV-1`; it never lowers 108, weakens `0.10`, reuses sibling readers, or
  selects a replacement after scores.
- **Permitted claim:** The repository contains an exact pre-execution reader
  and `MV-1` qualification candidate plus reproducible synthetic yield
  arithmetic. This is not reader reliability, image truth, task relevance,
  clinical validity, feasibility, Gate-0 closure, venue readiness, acceptance,
  or publication.

## DR-0012 — Simulation Manifest and Resource-Qualification Boundary

- **Date:** 2026-08-29
- **Status:** Proposed protocol-compilation recommendation; requires Commander,
  clinical, statistical, resource, governance, and infrastructure decisions
  through `G0-READERS`, `G0-MV-Q`, and `G0-RESOURCES`; simulation- and
  feasibility-blocked; not executable
- **Repository facts:** Prospectively clarified canonical enumeration yields
  10,847 reliability candidates, `K_plan=4,416`, and 2,438 pre-calibration
  `MV-1` candidates. The combined sorted canonical-ID SHA-256 is
  `4e914a602b418c7fbbcccb1e98d9f09a3d339009e9c2befcdd098e34604695a0`.
  The successful full path contains up to 1,594,200,000 outer datasets and
  15,940,405,800,000 nested bootstrap analyses.
- **Inference:** These logical counts rule out calling the current contract
  resource-qualified without a non-core computational design, proposed storage
  schema, generic workload-equivalent microbenchmark, conservative scaling
  uncertainty, contingency, and explicit allocation. They do not by themselves
  prove hardware infeasibility; exact scientific implementation remains post-
  Gate-0.
- **Assumptions and bounds:** The full `MV-1` envelope assumes every candidate
  calibrates; its bootstrap-index upper bound assumes every candidate is
  evaluable in every outer replication. Calibration admissibility and realized
  yield were not generated. CPU time, RAM, scratch, persistent-result bytes,
  wall time, cost, and capacity remain unidentified.
- **Compilation decision:** Numeric lexemes, one-factor crosses, zero-
  missingness planning rows, finite inequality filtering, six null pairs, all
  three pre-calibration q distributions, and asymmetric defaults are frozen
  prospectively. A failed calibration fails the design and never deletes a
  manifest row or shrinks the family.
- **Finite owner choice:** `G0-RESOURCES A` later resource-qualifies the
  unchanged contract; B commissions a proof-preserving computational redesign
  and full re-enumeration before setting ceilings; C rejects or narrows the
  affected reader/`MV-1` route. B is recommended only as the next bounded
  design action. No option, implementation, benchmark, or run is approved.
- **Kill boundary:** No project RNG, DGP, calibration, bootstrap, simulation,
  or benchmark may run under this record. Pre-Gate-0 resource evidence is
  limited to a separately authorized non-core design and generic workload-
  equivalent microbenchmark that implements none of those project primitives.
  Exact scientific implementation requires Gate-0 freeze plus a later brief
  covering software/hardware, deterministic reduction/restart, result/storage
  schema, proof obligations, resource allocation, and applicable approvals.
  Lowering 120,000 or 9,999, deleting hard cells, weakening 108 or `0.10`, or
  pruning after outcomes is prohibited.
- **Permitted claim:** The repository contains a deterministic candidate-cell
  inventory and hardware-neutral logical-workload audit. This is not
  implementation correctness, runtime, affordability, statistical operating
  performance, resource availability, reader reliability, `MV-1` validity,
  Gate-0 closure, venue readiness, acceptance, or publication.

## DR-0013 — Static Simulation Computation and Benchmark Boundary

- **Date:** 2026-08-29
- **Status:** Proposed non-core resource-design recommendation under TB-0010;
  requires statistical, scientific, resource, infrastructure, security,
  governance, and Commander decisions; not executable
- **Facts:** TB-0009 freezes 13,285 candidate cells, 6,720 planning cells,
  120,000 outer replications per executable cell, and 9,999 analysis
  bootstraps. TB-0010 specifies a stage graph, normalized catalogue/audit/
  checkpoint proposal, deterministic restart rules, output-equivalence proof
  register, workload-to-generic-kernel crosswalk, and conservative resource
  equations. No implementation or benchmark ran.
- **Inference:** Independent cell/outer identities support restartable
  scheduling, but streaming, sufficient statistics, batching, caching, and
  parallel reduction are valid only after exact conformance to a frozen
  reference. Counters alone cannot satisfy the per-replication audit contract.
- **Assumptions and bounds:** Under the proposed packed minimum schema, the
  successful-path audit payload is approximately 572.5 decimal GB before
  permutation/output extensions, aggregate/failure records, format overhead,
  scratch, redundancy, and backups. This is not a final storage upper bound or
  allocation. Runtime, RAM, scratch, I/O, wall time, cost/energy, parallel
  efficiency, and capacity remain unmeasured.
- **Design recommendation:** Close the exact numeric/output registry and
  semantic-count ledger, then authorize only a generic artificial-buffer
  benchmark under a new brief. Test whether the unchanged contract can satisfy
  `G0-RESOURCES A` before considering a scientific redesign under B. This is a
  sequencing recommendation, not selection of A/B/C; it supersedes only
  DR-0012's recommendation that B be the immediate next action.
- **Proof boundary:** Later optimized paths must preserve canonical cells and
  hashes, every seed/tag/raw word and bootstrap index, reference-order statistic
  bits, strict inequalities, failure classifications, multiplicity families,
  reconstructible audit outputs, byte-identical canonical scientific records
  under atomic restart, and execution-history-sensitive sidecar accounting.
  Mutable retry/journal/failure streams are audited separately and are not in
  the cross-schedule byte-equality domain. Failure
  retains the reference path or stops; approximate agreement is insufficient.
- **Kill boundary:** No project RNG, DGP, calibration, bootstrap statistic,
  reliability statistic, FE/LOO analysis, simulation, benchmark, model, data,
  reader, or external resource action is authorized. No capacity decision may
  use guessed compression or omit an unresolved schema/kernel term. Resource
  shortage narrows, redesigns, or stops; it never reduces 120,000/9,999,
  prunes cells, or weakens gates.
- **Permitted claim:** The repository contains a static computation,
  audit-schema, proof-obligation, and future artificial-buffer benchmark design
  for the unchanged pre-reader simulation. This is not correctness,
  calibration admissibility, feasibility, operating performance, Gate-0
  closure, acceptance, or publication.

## DR-0014 — Typed Simulation Output and Semantic-Count Registry

- **Date:** 2026-08-29
- **Status:** Complete static freeze candidate under TB-0011; requires
  scientific, statistical, resource, infrastructure, governance, and Commander
  approval or amendment; not executable
- **Facts:** The frozen TB-0009 manifests remain 10,847 reliability and 2,438
  pre-calibration `MV-1` candidates with unchanged hashes. A standard-library,
  RNG-free compiler now emits a 259-row metric registry, 244-row operation
  registry, and 1,242,518-row cell/global ledger with complete-file SHA-256
  `d1c15377bed93c297890f82acd4ff94b0e2f311324b0cd05a3ddaec2cb3cff5d`.
  No scientific value, permutation, random stream, simulation, benchmark,
  data, model, or reader output was generated.
- **Scientific inference:** Binary64 payloads and a NaN sentinel cannot
  identify structural inapplicability, reached scientific undefinedness, and
  not-reached state. Gate outcomes are also distinct from scientific and
  infrastructure failures. The TB-0010 prefix/record proposal was therefore
  insufficient for unbiased operating-characteristic accounting.
- **Registry decision:** Recommend a 72-byte canonical scientific prefix with
  separate failure-component and event masks, a deterministic key into a
  separately content-digested execution-attempt stream,
  two-bit `VALUE/INAPPLICABLE/SCIENTIFIC_UNDEFINED/NOT_REACHED` state per core
  slot, canonical-zero non-value payload, 32 reliability slots, and 64 `MV-1`
  slots. Persist static truths/calibration locks, outer core/state/events/
  failures, aggregate numerators/denominators, family decisions, identity, and
  digests. Reconstruct raw words, synthetic ratings, bootstrap indices, and
  bootstrap replicate values only after later bitwise conformance.
- **Storage correction:** Reliability and `MV-1` outer records become 336 and
  600 bytes. Under the same conditional all-candidate path, catalogue, locks,
  completion bitmaps, and core outer records total 613,093,770,610 bytes,
  exactly 40,601,280,000 above DR-0013's superseded floor. This is still a
  lower bound because typed static/aggregate/family, permutation, journal,
  failure-detail, owner-blocked extension, format, retry, redundancy, and
  retention terms lack a final upper bound.
- **Scope decision:** FE and all 30 leave-one-reader `MV-1` values remain in
  the core because they are part of the qualification veto. Hierarchical,
  Gwet, ordinal, adjudication, and complete reader-by-category diagnostics are
  observed-reader-only under the current simulation mandate. Adding them to
  every simulation replication requires a prospective canonical amendment and
  re-enumeration. Exact reliability/`MV-1` repeat outputs remain owner-blocked,
  never zero-cost.
- **Owner blockers:** Freeze the reliability truth-reference rule, missingness
  residual/bracket/update/final-selection rule, and repeat/ambiguity/item/
  permutation domains; `MV-1` numerical domain, inner-alpha and outer final-
  solution rules, target-versus-validated truth, and retained trace depth;
  primary-failure/component taxonomy; exact inverse-CDF, exact-binomial,
  FE/LOO, rounding, and any added sensitivity algorithms and software. Then
  close every extension/storage upper-bound term before a new generic
  artificial-buffer benchmark brief.
- **Kill boundary:** No benchmark or `G0-RESOURCES` choice may use the
  613.094-GB core floor as a capacity requirement or assume unresolved bytes
  are zero. No project RNG, DGP, calibration, bootstrap, statistic,
  scientific serializer, simulation, data/model/reader access, or external
  resource action is authorized. Resource shortage narrows, redesigns, or
  stops; it never reduces fixed replications/resamples, deletes cells, or
  weakens scientific gates.
- **Permitted claim:** The repository contains complete static freeze
  candidates for the simulation output registry and hardware-neutral semantic-
  operation ledger, with unresolved choices explicitly blocking any later
  benchmark or resource qualification. This is not owner approval,
  implementation correctness, runtime, capacity, feasibility, operating
  performance, Gate-0 closure, acceptance, or publication.

## DR-0015 — Commander Scope Choice and Local Storage Boundary

- **Date:** 2026-08-29
- **Status:** Commander-approved partial Gate-0 decision; supervisor and other
  owner approvals remain open; not executable
- **Fact:** The Commander explicitly selected `G0-SCOPE A`: the primary
  identified claim is determinate-conflict specificity, while natural image
  and text ambiguity remain veto-only falsification audits. This records the
  Commander's part of the joint decision; it does not imply scientific-
  supervisor approval.
- **Fact:** The Commander reports that the local workstation cannot hold the
  approximately 613-GB conditional core-output floor from TB-0011. That number
  describes a lower bound for one exhaustive simulation-output design, not the
  MIMIC dataset, the repository, a final storage upper bound, or a measured
  allocation.
- **Decision:** Adopt `G0-SCOPE A` at the Commander level. Do not make a full
  causal ambiguity-separation claim unless a later governed identification
  route is approved. Gate 0 remains open until the scientific supervisor and
  every other required owner complete their stated approvals.
- **Resource boundary:** The unchanged TB-0011 all-candidate output route may
  not be planned against local storage. `G0-RESOURCES A/B/C` remains open and
  must later choose approved external capacity, a prospectively proof-
  preserving redesign/re-enumeration, or a narrower route. The shortage does
  not authorize lower replication/resample counts, dropped cells, data/model
  downloads, or execution.
- **Method boundary:** `G0-METHOD A/B` remains open. This record neither accepts
  the framework-centered amendment nor authorizes another estimator-theory
  attempt.
- **Permitted claim:** The Commander has chosen the narrower scope and ruled
  out local storage for the current exhaustive simulation-output design. This
  is not supervisor sign-off, resource qualification, Gate-0 closure,
  implementation authorization, empirical evidence, or a publication claim.
- **Reopening condition:** Reopen the scope only if a prospective governed
  ambiguity-identification route is supplied. Reopen the local-storage
  boundary only with verified capacity evidence and a new bounded contract.

## DR-0016 — Commander Method-A and Instrument/Comparator Interface Decision

- **Date:** 2026-09-01
- **Status:** Commander-approved partial Gate-0 decision; scientific-
  supervisor, statistical-owner, and model-owner approvals remain open; not
  executable
- **Facts:** TB-0006 killed all three proposed new pointwise-estimator claims.
  The exact `psi_mag` plug-in remains an estimator of a population specificity
  functional for a frozen score, not a deployable pair-level conflict score.
  Output-only non-identification permits identical learned outputs under
  ambiguous, compatible, and incompatible independently measured states.
- **Primary-source fact:** the audited ProbVLM paper supplies generalized-
  Gaussian adapter semantics, while the official MIT-licensed source differs
  materially in its active residual/loss and path behavior. Ordinary InfoNCE
  additionally treats off-diagonal pair identities as negatives; in a repeated
  low-cardinality atomic task, some are semantic false negatives.
- **Inference:** a framework-level contribution may survive in the complete
  combination of determinate partial-construct support, independent modality-
  only measurement, controlled compatibility interventions, valid paired
  information-loss controls, joint population inference, matched deterministic
  challenge, and downstream decision gates. This remains a novelty hypothesis.
- **Decision:** adopt `G0-METHOD A` as the project's sole route. The working
  paper identity becomes *Ambiguity Is Not Conflict: Intervention-Identified
  Measurement of Cross-Modal Conflict Specificity*. Do not pursue
  `G0-METHOD B` in parallel and do not claim a new pair-level estimator.
- **Instrument decision:** freeze, at the Commander scientific-interface level,
  a project-native `PROBVLM-2ADAPTER` instrument with paper-faithful symmetric
  cross-modal generalized-Gaussian likelihood semantics. The coordinate
  reduction and complete objective weights are project choices rather than a
  paper- or code-exact training claim. The instrument is explicitly non-novel,
  uses no original ProbVLM checkpoint, and may not fit constructed
  contradictions as positive pairs.
- **Comparator decision:** freeze `POINT-2ADAPTER-RECON` as the primary matched
  deterministic full-route comparator. It shares frozen inputs, independently
  verified determinate-compatible fit records, mean trunks, intra/cross target
  topology, optimization, tuning budget, the GGD score family, and compatible-
  reference standardization while removing input-dependent scale and shape
  outputs. Global coordinatewise scale/shape constants are fitted on the same
  compatible fit/development objective and frozen before protected outcomes;
  unit-scale Laplace is a sensitivity only.
- **Supervision and capacity boundary:** compatible fitting-set membership is
  shared semantic selection supervision, although semantic labels are neither
  model inputs nor loss targets. Removing the probabilistic heads changes active
  parameters and gradient paths, so the primary comparison tests complete
  same-selection-information routes rather than a capacity-isolated mechanism;
  exact parameter and compute differences must be reported.
- **Secondary-baseline decision:** demote `POINT-INFONCE` to a secondary same-
  records contrastive baseline. Its denominator, positive multiplicity,
  patient/source exclusions, semantic false-negative mask, temperature,
  normalization, optimizer, and tuning rules require a separate pre-execution
  freeze. No CLIP-Adapter code is inherited.
- **Attribution boundary:** ProbVLM-versus-point performance alone cannot
  attribute benefit to learned scale or shape. A frozen-means diagnostic must
  replace input-dependent scale/shape with the point comparator's frozen global
  constants. It can isolate only the direct score path conditional on jointly
  trained means, not a training-path or causal mechanism; failure kills even the
  narrow direct-score attribution.
- **Standardization boundary:** `A_psi` subtracts two effects standardized by
  their respective method-specific compatible-reference distributions. It is a
  difference of dimensionless standardized effects, not one common reference-
  SD contrast; raw-score and median/MAD sensitivities remain required.
- **Assumptions:** independently reliable and score-blind semantic measurement,
  valid intervention/control construction, stable complete blocks, frozen
  score/link/normalizer, no leakage, and a defensible selected/evaluable target
  are required for the intervention-relative interpretation.
- **Alternatives considered:** retain `POINT-INFONCE` as the primary matched
  comparator, use the audited ProbVLM code exactly, or authorize a new-estimator
  theory route. The first two confound the intended comparison; the third
  contradicts the selected single route.
- **Consequences:** the scientific interface is no longer selected from
  development, but Gate 0 remains open. Exact task, data, intervention,
  backbone, software, numerical architecture, optimization, calibration,
  readers, resources, governance, and all required co-approvals remain blocked.
  No implementation or experiment follows from this decision.
- **Venue boundary:** NeurIPS 2027 Main Track remains the strategic target, not
  a promised outcome. The 2027 call must be rechecked, and framework novelty,
  construct validity, deterministic advantage, breadth, calibration, and
  decision evidence must survive their pre-specified gates.
- **Hard-kill boundary:** failure of the frozen `psi_mag` specificity gate or
  the `+0.10` `A_psi` probabilistic-instrument material-advantage gate kills the
  current Main Track route. Retain and report the qualified null or
  deterministic result without post-hoc repackaging; deterministic subsumption
  still requires its separate positive conditions.
- **Review date:** at scientific-supervisor/statistical/model-owner review and
  again before Gate-0 closure or after a material primary-literature update.
- **Reopening condition:** reopen only if a required owner rejects the exact
  interface, a same-information defect survives correction, a primary source
  occupies the complete framework claim, or the frozen pair cannot be made
  executable without changing its scientific meaning. Reopening requires a
  dated decision; failed results cannot select a replacement.
- **Permitted claim:** the Commander has selected Method A and its primary
  scientific interfaces. This is not other-owner approval, framework novelty,
  empirical identification, probabilistic superiority, clinical value, Gate-0
  closure, NeurIPS eligibility, acceptance, or publication.

## DR-0017 — Scientific-Supervisor Alignment on Scope and Method A

- **Date:** 2026-09-02
- **Status:** User-attested scientific-supervisor alignment at the conceptual-
  framing and named-method-role level; formal scope/sole-route co-approvals,
  remaining owners, and executable details are open; not executable
- **Evidence provenance:** The Commander reports that the scientific
  supervisor agreed after receiving a private email that asked exactly five
  questions. Codex did not inspect, request, quote, or store the correspondence.
- **Facts conveyed for approval:** The email asked whether the supervisor
  agreed with (1) ambiguity within a modality being distinct from cross-modal
  conflict; (2) Method A's intervention-based identification framework as the
  primary contribution; (3) the scientific roles of the explicitly non-novel
  `PROBVLM-2ADAPTER` instrument, matched `POINT-2ADAPTER-RECON` comparator, and
  secondary `POINT-INFONCE`; (4) chest radiography as the primary validation
  domain; and (5) NeurIPS 2027 Main Track as a conditional strategic target.
- **Inference:** The reported agreement supports scientific-supervisor
  alignment with the ambiguity/conflict distinction and with the intervention-
  based framework as the primary contribution. It also supports the named
  primary instrument/comparator roles, the chest-radiography validation-domain
  choice, and the conditional venue strategy. The first question did not ask
  the supervisor to select `G0-SCOPE A` over B or approve its veto-only
  observational boundary; the second did not ask whether Method A is the sole
  route with B inactive. Those formal co-approvals cannot be inferred.
- **Assumption:** The Commander's report accurately represents an unqualified
  agreement to the five questions. Any additional condition communicated by
  the supervisor would require a dated amendment.
- **Decision:** Keep `G0-SCOPE A` and Method A's sole-route/B-inactive boundary
  Commander-approved only. Record supervisor alignment with the ambiguity/
  conflict distinction, the intervention-based framework as the primary
  contribution, and the named roles of `PROBVLM-2ADAPTER`,
  `POINT-2ADAPTER-RECON`, and secondary `POINT-INFONCE`. Formal supervisor
  approval of those two exact boundaries, the exact interface, statistical/
  inference package, model-owner, implementation, licence, calibration, and
  other applicable approvals remain open.
- **Boundary:** This approval does not freeze the provisional pleural-effusion
  task, ontology, `MV-1`/`MT-1`, readers, estimand, inference, ablation suite,
  exact architecture/software/hyperparameters, checkpoint, data access,
  governance, resources, breadth benchmark, or any experiment. Chest
  radiography approval is a validation-domain choice, not dataset, task, or
  clinical-benefit approval. Venue alignment is not eligibility, acceptance,
  or publication evidence.
- **Alternatives considered:** Requesting or committing the private email was
  rejected as unnecessary and inconsistent with the correspondence boundary.
  Treating the response as full Gate-0 approval was rejected as approval
  inflation.
- **Consequences:** Scientific-supervisor conceptual alignment is recorded, but
  the formal supervisor blockers remain for the exact `G0-SCOPE A` veto-only
  and Method-A sole-route/B-inactive choices. Gate 0 remains open. The next
  decision work is explicit supervisor confirmation of those boundaries,
  statistical- and model-owner review of the Method-A package, and the still-
  open clinical, data, governance, resource, staging, and breadth choices.
- **Review date:** At statistical/model-owner review, before Gate-0 closure, or
  immediately if the supervisor communicates a qualification or rejection.
- **Reopening condition:** Reopen only if the Commander corrects the report,
  the supervisor adds a condition, a required owner rejects the interface, or
  new primary evidence changes the scientific framing. Results cannot be used
  to reinterpret the scope of this approval.
- **Permitted claim:** The Commander reports scientific-supervisor agreement
  with the five stated scientific-framing questions. This is not raw
  correspondence evidence, full owner sign-off, an executable freeze,
  empirical evidence, Gate-0 closure, clinical value, NeurIPS eligibility,
  acceptance, or publication.

## Open Gate 0 Decisions

- retain the Commander-approved `G0-SCOPE A` determinate-conflict-specificity
  route while H2 remains unresolved; obtain explicit supervisor approval of
  the exact veto-only boundary, and require a separately governed route for
  any broader ambiguity-identification claim;
- provisional pleural-effusion finding, strict single-frontal-image unit, and
  exact visibility/eligibility rule;
- two-stage MIMIC resource/query record, HMAC partitions including the
  recommended 300-screened/216-evaluable, equal-polarity `MV-1`
  qualification reserve, secure access route,
  aggregate outputs, screening floors, and derived-artifact terms;
- `G0-READERS A/B` and `G0-MV-Q A/B/C`: exact reader coefficient/allocation,
  finite-roster claim, text/cross-modal panels, adjudication, simulation,
  ethics, governance, yield, panel schedule, workload, and kill rules;
- `G0-RESOURCES A/B/C`: approve or amend TB-0011's registry recommendations,
  close its owner-blocked extensions and final storage upper bound, and later
  resource-qualify the unchanged 10,847-plus-2,438 candidate contract;
  commission a proof-preserving redesign and complete re-enumeration; or
  reject/narrow the affected route. No benchmark, runtime/capacity fact, or
  option approval currently exists, and the 613-GB conditional core-output
  floor cannot be assigned to the Commander's local workstation;
- explicit supervisor approval of the Method-A sole-route/B-inactive boundary,
  plus statistical-owner and model-owner approval of the Commander-frozen
  Method-A interfaces and supervisor-aligned framework/named roles for
  `PROBVLM-2ADAPTER`/`POINT-2ADAPTER-RECON`; then all
  applicable owners must freeze the exact executable backbone/baseline
  implementations, numerical values, secondary `POINT-INFONCE` policy,
  ablation/applicability map, and licences;
- magnitude-safe primary endpoint, compatible-reference scale, 0.20 construct
  threshold, secondary `theta`, the `G0-INFERENCE` max-`t`/multiplicity/fixed-
  sequence package, 0.10 `A_psi` probabilistic-instrument material-advantage
  boundary on method-specifically standardized effects, and 216/320-or-400
  operational floors;
- owner approval of exact `MV-1`/`MT-1` operations, severities/state rules,
  acceptance rules, within-source references, the `MV-1` task-evidence endpoint/
  threshold/power, and the exact frozen pointwise instrument/interface at Gate
  0; fitted instances and configurations then lock separately before Month 3;
- artifact option A (exact balance plus diagnostic veto) or B (powered bounded
  frozen-probe recoverability), orientation-safe `R=max(BA,1-BA)`, exact probe
  implementations, and the unresolved approximate 1,047/1,757 IUT burden for B;
- final task-error outcome, 0.02 Brier-skill increment, 0.01 `A_BSS` method-
  difference margin, calibration tolerances, target prevalence/covariance/
  power, 90% coverage budget, and 0.01 risk margin;
- target-distribution cohort and any prevalence weighting;
- conditional checkpoint shortlist/exposure audit and proposed 1-TB,
  300/1,500-GPU-hour, and revised 500/1,350-clinical-person-hour ceilings;
- pre-specified distribution shift and subgroup set;
- the Gate-0 breadth choice between VisMin and PadChest-GR, plus immutable
  snapshot, rights, construct-portability, and later execution boundary;
- final NeurIPS 2027 track and deadline after the official call.
