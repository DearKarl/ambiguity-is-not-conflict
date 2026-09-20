# Pre-Access Readiness Specification

Date: 2026-09-20. Evidence class: protocol; no execution or research result.
Authority: EC-2026-09-20-001. Source baseline:
`585be42d47a86b84a16bbf986d83e96f37145306`.

This packet compiles the existing Method-A route into reviewable interfaces.
NeurIPS 2027 Main Track remains the sole objective. Gate 0 remains open.
Read with the [acceptance matrix](pre_access_acceptance_matrix.md) and
[finite decision package](pre_access_decision_package.md).

## Status and precedence

| Label | Meaning |
| --- | --- |
| `approved` | Exact internal choice recorded by DR-0018/DR-0019; no inferred external fact or execution permission. |
| `source-derived` | Faithful transcription of the named baseline source; inherits that source's approval limits. |
| `proposed` | Concrete review candidate, never a silent freeze. |
| `owner-decision` | A named accountable owner must record the exact choice before dependent work. |
| `external-evidence` | Objective dated evidence is absent or only historically reported. |
| `data-dependent` | A future bounded authorized check must establish the fact; no observation exists here. |

Package completeness means that inputs, choices, evidence and rejection rules
are reviewable. Decision-freeze readiness additionally requires all exact
choices and external prerequisites. Operational readiness requires those
freezes, a current bounded brief, approved environment and prior-stage passes.
Scientific success requires the later pre-specified empirical gates. None of
these states implies the next. This packet does not claim the latter three.

The latest approved decision record prevails over older audit language.
DR-0018 approves scope, Method-A protocol/interfaces and data/retention
readiness only. It leaves independent Gate-0 choices open. DR-0019 supersedes
historical venue alternatives. No old job or task authority resumes.

## Versioned source crosswalk

All inputs below are read at the baseline commit above; section names identify
the relied-on boundary. Source dates and old official-code identities are
historical evidence, not a fresh literature, licence or account audit.

| Source | Relied-on sections and role |
| --- | --- |
| [Decision log](decision_log.md) | DR-0018, Remaining Gate 0 Decisions and Evidence, DR-0019: approval and objective authority. |
| [Research contract](research_contract.md) | Gate 0 Closure Requirements, Promotion/Stopping Criteria: scientific hierarchy. |
| [Decision dossier](gate0_decision_dossier.md), [closure audit](gate0_closure_audit.md) | Finite Owner Decisions and one-to-one crosswalk: all 24 Gate-0 rows. |
| [Method A](method_a_identification_framework.md) | Partial Construct, primary interfaces, Score Standardization, Falsification: approved semantic boundaries. |
| [Statistical plan](statistical_analysis_plan.md) | Analysis Populations, Primary Construct Endpoint, Intervals and Multiplicity, downstream candidates. |
| [Formalization audit](estimator_formalization_audit.md) | Exact reductions, retained estimator and implementation/supervision ledger. |
| [Measurement protocol](measurement_protocol.md) | Prediction Unit, Fractional Identification Design, Pair Construction, Month-3 Kill Test. |
| [Annotation protocol](annotation_and_intervention_protocol.md), [intervention audit](intervention_option_audit.md) | Independent state precedence, reader acceptance, exact MV-1/MT-1 candidates. |
| [Reader audit](reader_measurement_and_mv1_qualification_audit.md) | Quotas, reliability intervals, finite-roster q analysis, FE/LOO veto, simulation criteria. |
| [Baselines](baselines_and_ablations.md) | Finite implementation/information budgets, six minimum ablation families; no additional mandatory point-softmax comparator. |
| [Dataset record](dataset_decision_record.md), [dataset candidate](dataset_decision_candidate.md), [governance](data_governance.md) | Four-file Stage B, joins, HMAC, screening floors, evidence and disclosure. |
| [Budget/backbone audit](execution_budget_and_backbone_audit.md) | Exposure tiers, distinct planning ceilings, local-storage constraint and timing stops. |
| [Output registry](simulation_output_and_operation_registry.md), [computational design](noncore_simulation_computational_design.md) | Owner-blocked numerics, full storage terms, conformance and generic benchmark boundary. |
| [Submission strategy](submission_strategy.md), [novelty audit](novelty_audit.md) | Main Track promotion/kill and dated prior-art threats; no fresh novelty conclusion. |
| [September 18 ledger](progress_2026-09-18.md), [preparation plan](pre_access_preparation_plan.md) | Historical administrative evidence and preparation dependencies. |

## External evidence receipt contract

Adjutant supplied the following coordination ledger on September 20, based on
DR-0018, DDR readiness requirements 1--7, governance and the September 18
ledger. It is attributed evidence triage, not a provider or institutional
verification. For every row, acceptance requires a dated, scope-matching,
non-sensitive evidence reference, accountable role, validity/expiry and
explicit disposition. Missing, expired or mismatched evidence means STOP for
the dependent stage. Private evidence stays outside Git and hosted services;
do not request or commit certificates, screenshots, account identifiers or
correspondence. No person, path or approval is invented.

| ID | Current state | Accountable role and required evidence |
| --- | --- | --- |
| E01 | `external-evidence`: September 18 credential status reported Awaiting review; not live September 20 verification. | Commander supplies a dated sanitized provider-status receipt for each individual accessor. |
| E02 | `external-evidence`: both courses historically Passed; provider training report historically Review. | Commander supplies separately dated evidence of provider-accepted current training for each accessor; course completion is insufficient. |
| E03 | `external-evidence`: DUA/access unconfirmed for both resources. | Commander supplies separate scope/version-matching DUA and actual access dispositions for MIMIC-CXR and MIMIC-CXR-JPG; no account action here. |
| E04 | `external-evidence`: institutional determination absent. | Commander coordinates institutional ethics owner: determination scope, date and non-sensitive reference for screening and readers separately. |
| E05 | `external-evidence`: secure environment unverified. | Commander designates security owner; Engineer checks approved absolute path outside Git, ACL roles, encryption, network/no-hosted-service controls, backup, incident, retention, deletion and disclosure controls in the secure record. Public receipt contains only a non-sensitive reference. |
| E06 | `external-evidence`: derivative/licence/access basis absent. | Commander and institutional governance owner document permitted annotations, text, embeddings, weights, retention and release; source access alone does not permit derived release. |
| E07 | `external-evidence`: qualified independent reader capacity absent. | Commander/clinical lead document mutually exclusive qualified panels, training, access, availability and schedule. Consolidated internal ownership never replaces independent panels. |
| E08 | `external-evidence`: allocated resources absent. | Commander/resource owner documents bounded Stage-B CPU/storage separately from later models and simulation. `613093770610` bytes is only the conditional simulation-output core floor, not the Stage-B budget. |
| E09 | `data-dependent`: yield/reliability/validity not collected. | Engineer specifies prospective checks; a later authorized stage produces reviewed aggregate evidence. A planning assumption cannot satisfy this row. |

## Stage-B interface and ordered access boundary

Status: data/retention readiness logic `approved`; implementation and observed
feasibility remain blocked. The coupled resources are MIMIC-CXR/JPG v2.1.0.
Only a later Stage-B EC and TASK_BRIEF after Gate-0 closure may authorize the
restricted tabular screening query in the approved environment.

| File | Exact field allowlist |
| --- | --- |
| `mimic-cxr-2.0.0-split.csv.gz` | `dicom_id`, `study_id`, `subject_id`, `split` |
| `mimic-cxr-2.0.0-metadata.csv.gz` | `dicom_id`, `ViewPosition`, `Rows`, `Columns` |
| `mimic-cxr-2.0.0-chexpert.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |
| `mimic-cxr-2.0.0-negbio.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |

Preserve the dataset candidate's ordered algorithm: unique image keys;
cardinality-preserving split-to-metadata left join; count all study images
from split rows; derive strict-single-frontal eligibility with positive
nonmissing geometry; apply outcome-blind partition and one-study rank; only
then left-join both unique study-label tables and form exhaustive exclusive
report-screen strata. Missing metadata/labels remain visible. Report-screen
labels never establish image truth or define fit supervision.

The frozen HMAC algorithm uses the complete unsigned big-endian SHA256 digest,
canonical base-10 IDs and `AINC/v1/partition` / `AINC/v1/study-rank` domains.
Official train buckets 0--69, 70--84 and 85--99 retain development, one-time
Month-3 and confirmation roles; official validation is calibration and test
is natural target. All siblings and connected source components stay together.
The qualification reserve is removed before fitting under the separately
chosen MV-Q rule. Key creation/custody is a later approved secure operation;
only the non-secret fingerprint may leave that store.

The later brief must name query revision/hash, schema-only test evidence,
exact secure command/path, CPU/storage limits, disclosure reviewer, output
schema, access date/resource hashes and stop behavior. Dates, demographics,
reports, images, pixels, other findings, manual test labels and record exports
are excluded. Every allowed field is restricted.

Only reviewed aggregate cohort/invariant counts, resource and code hashes,
and disclosure decisions may leave. Suppress cells below 20 and all
complementary totals, percentages or cross-release refinements that reconstruct
them; use a release ledger and review the exact rendered table.

After Stage B, review yield and integrity before any fresh Stage-C brief.
Images/reports, readers/annotations, models, development, protected evaluation
and scientific simulation each retain their separate authorization. Provider
review completion and a successful screening query authorize none of them.

## Clinical unit and independent measurement

The following Engineer recommendations are `source-derived` and `proposed`,
with `owner-decision` gates G0-TASK/ONTOLOGY/READERS. Their canonical sources
are the measurement, annotation and reader audits in the crosswalk.

The task is asymmetric image-grounded pleural-effusion presence/absence. The
unit is `(patient, study, exact single frontal image, finding, atomic
assertion, variant, frozen model)`. The clinical owner must approve the
finding, prescribed coverage, edge cases, credentials and exact rendered input.
Native study-report pairing and report-screen labels cannot establish truth.
A need for a multi-view substitute reopens the task before dependent access.

Image-only records separate technical integrity, prescribed coverage, Y_v,
A_v, probability and reason. Text-only records separate integrity, target
polarity, commitment, linguistic multiplicity, Y_t and probability. Apply the
annotation protocol's precedence literally: task-critical loss or missing
prescribed field makes Y undefined, ambiguity not assessable and probability
structurally missing. Intact/complete genuine ambiguity retains an
interpretation distribution but undefined Y. Interpretable image loss and
fully recoverable text corruption may remain determinate under their own
acceptance rules. Hedging is not automatically linguistic ambiguity; no
mention is not a negative assertion.

Lock independent modality-only labels before pair review. For R_v,R_t in
{0,1}, C_R* is their inequality indicator; outside that support it is undefined,
never zero. Pair review cannot overwrite unimodal labels. A suspected error
invalidates the pair and requires a fresh same-modality blinded record.

| Item | Proposed acceptance rule |
| --- | --- |
| Clear image | At least 4/5 jointly agree on intact, complete field, determinate and same polarity; at most one ambiguity/critical-loss flag. |
| Natural image ambiguity | At least 4/5 agree on intact, complete and genuinely ambiguous; Y_v remains undefined. |
| Clear text | 3/3 intact, unique, definite and intended polarity in each disjoint panel. |
| Natural text ambiguity | At least 4/5 identify intact wording with multiple reasonable polarity readings; Y_t remains undefined. |
| Pair | 3/3 on each required validity component; information-loss controls use their own conditions. |
| Category/probability coherence | Present rating >=0.5, absent <=0.5; incoherence is instrument error, not repairable disagreement. |

The reader candidate requires mutually exclusive rosters of ten image, six
text and six pair readers: at least 22 qualified people. Image siblings use
disjoint five-reader panels; text/pair siblings use disjoint three-reader
panels. Reliability uses 150 source clusters with five image, five text and
three pair first ratings. Training, 60-unit timing/rubric pilot, reliability,
MV qualification and scientific populations remain disjoint. Repeat
`ceil(0.15 N_r)` per reader gives 120 image, 114 text and 72 pair reliability
repeats. Credentials and an exact clinically justified repeat washout duration
remain owner/external blockers; disjoint siblings are recommended regardless
of washout, rather than inventing a numeric interval.

Retain the reader audit's printed marginal strata and category crosswalk:
image counts 30/30/30/15/15/10/10/10, text 30/30/30/20/10/10/20 and pair
50/50/10/10/10/10/10. No post-rating pooling or quota replacement is permitted.
Fifteen axes remain separate: four image, five text, five pair components and
global pair acceptance. Nominal alpha is `1-D_o/D_e`; macro agreement is the
mean of each item's agreeing unordered reader-pair fraction; class-positive
agreement is twice the agreeing within-class pairs divided by twice those
pairs plus cross-class pairs. Empty required denominators are non-estimable.
The exact formulas, strata and assignment cycles remain the reader audit's
authoritative definitions; the acceptance matrix preserves all thresholds.

## Information-loss controls and qualification

Status: `source-derived` / `proposed` / `owner-decision` for G0-MV/MT/MV-Q.
The initial control family is exactly `{MV-1, MT-1}`. No third/fourth control
is added without a separate prospective identity, validity and power decision.

MV-1 applies deterministic area averaging from 224x224 to 112x112 and
bilinear restoration to 224x224 after frozen geometry and before channel
normalization. No cropping, added content, noise or recompression. Its
within-source reference is the exact intact compatible pair. At least 4/5
transformed readers must accept interpretable loss, full coverage and the same
determinate polarity, with at most one ambiguity/critical-loss flag. Exact
rendering software and coordinate rules still require the executable freeze.
Pixel loss is insufficient: the separate q qualification must pass.

MT-1 removes the sole status slot of the already proposed atomic carrier in
the intervention audit, retaining finding identity and no polarity carrier.
This packet creates no clinical example. Y_t/C* remain undefined and A_t not
assessable. Three blinded text readers must unanimously confirm task-critical
loss, target identity and no recoverable/contrary polarity. Pair reviewers
check intended loss and preservation, without requiring determinate text or
fluency from task-critical redaction. Polarity leakage or a second carrier
rejects the operation; scores cannot choose a replacement.

Recommended G0-MV-Q A reserves 150 candidates in each report-screen polarity
under the separate qualification rank before fitting, excluding all 300 from
other scientific sets. Assess all reserved candidates; no result-driven top-up.
Lock the ten-reader cyclic complementary panels, ranks, permutations and order
before ratings. For intact and transformed siblings, define
`h_s = a_y (pbar_s - 0.5)`, with `a_y=+1` for present and `-1` for absent.
Evaluability E=1 requires same determinate polarity, complete coverage, valid
intervention, all ten probabilities and both h_s >=0. Then
`q_b=h_intact-h_MV1`, `q_y=E_R[q_b | S=1,E=1,Y_v=y]`, and
`q_bal=(q_present+q_absent)/2`. This is conditional on selected/evaluable
patients and the finite roster, not reader-population inference. Recorded
dissenting probabilities stay in their five-person mean; a missing probability
makes the whole block non-evaluable. No q magnitude or model output determines
selection, eligibility, severity or replacement.

## Natural-ambiguity veto specification

Source: [task/estimand packet](task_estimand_options.md), E3 natural-ambiguity
contrast; measurement protocol, Month-3 Kill Test. The source defines separate
observational gamma contrasts and phi; using the same frozen Z scale on all
terms is an Engineer `proposed` operationalization, requiring owner approval.

For q in {v,t}, use
`gamma_Aq = E_w[Z | A_q=1,C* undefined] - E_w[Z | A_q=0,C*=0]` and
`phi_A = min_q(tau_C - abs(gamma_Aq))`. These contrasts never enter psi_mag
or psi_id. A nonpositive phi, absent overlap or unstable weighting verdict
falsifies/reopens; positive phi does not identify causal ambiguity separation.

Engineer proposes separate image/text audit arms, exact matching on the
non-target modality's locked determinate polarity, AP/PA, prescribed
coverage/integrity, carrier/template and renderer; length/negation descriptors
are fixed before scoring. Primary weights are ambiguity-arm stratum
frequencies; equal-overlap-stratum weights are the declared sensitivity.
Every positively weighted ambiguity stratum requires clear-compatible support.
No matching on model outputs, scores or the undefined Y of an ambiguous
modality. Missing support makes the audit non-estimable; phi<=0 under either
weight scheme or a changed veto verdict reopens the design. Exact nuisance
dictionary, minimum counts, interval adequacy and support evidence remain
explicit owner/data dependencies. No absence-of-veto result is equivalence or
transport evidence. This proposal is not a newly approved gate.

## Exact executable candidate EX-A

Evidence class: Engineer protocol recommendation, **NOT IMPLEMENTED OR RUN**.
Every new selection below is `proposed` / `owner-decision`, even where its
starting value is source-derived. G0-METHOD/MODEL/CHECKPOINT must approve a
complete profile; accepting this document approves none of these choices.

The immutable [BiomedCLIP configuration](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224/raw/9f341de24bfb00180f1b847274256e9b65a3a32e/open_clip_config.json)
supports the source-derived 512-dimensional projection, ViT-B/16 image size
224, BiomedBERT tokenizer/encoder, CLS-last-hidden-state pooler, MLP text
projection and context 256. Its mean is (0.48145466, 0.4578275, 0.40821073)
and standard deviation (0.26862954, 0.26130258, 0.27577711).
Engineer inspected only public text in memory, not checkpoint weights.
Immutable ProbVLM [networks](https://raw.githubusercontent.com/ExplainableML/ProbVLM/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/src/networks.py)
and [training driver](https://github.com/ExplainableML/ProbVLM/blob/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/src/train_probVLM.py)
provide residual-head and Adam/1e-4/100-epoch/cosine starting points. Their
wrappers differ; the disabled image/cross-modal path is not copied. EX-A is
not code-exact reproduction or a claim of suitability. Historical identities,
rights and novelty classification remain the estimator/baseline audits'.

| Field | Exact recommended candidate | Rationale, alternative and remaining gate |
| --- | --- | --- |
| Input geometry | Decode approved JPG to float32 [0,1]; replicate grayscale to three channels. Longest edge 224, other edge round-half-up; centered zero padding to 224, odd excess bottom/right. Bilinear half-pixel coordinates with downsampling antialias. No crop, mirror, random augmentation, sharpening, re-JPEG or histogram operation. Normalize after MV/no-MV branch. | Preserve prescribed clinical field; this is a proposed deviation from center-crop recipes, not provider-exact preprocessing. Clinical owner must validate field and software conformance. Alternative provider geometry needs its own field approval. Identical tensors for P/D. |
| MV kernel completion | At 224 geometry, each 112 pixel is the exact 2x2 mean; restore by half-pixel bilinear edge replication, align_corners=false, no upsampling antialias or intermediate integer rounding. | Completes MV-1 prospectively; library/numeric conformance required. Different backbone resolution requires amendment. |
| Text interface | Approved exact carrier bytes; immutable tokenizer lineage; context 256. Overlength target carrier fails, never silently truncates. Preserve supplied case/punctuation. | Tokenizer vocabulary/config hashes remain required evidence; no guessed identities. |
| Feature map | Frozen post-projection z_v,z_t in R^512; u=z/||z||2 for both P/D and RAW-COS. No logit scale, softmax, learned whitening or protected-case centering. Zero/nonfinite norm fails. | L2 map is proposed to fix coordinate scale; raw features are a finite prospective alternative requiring the numerical-domain rationale to change. Feature spread is not semantic ambiguity. |
| Shared graph | Per modality t(u)=u+W3 ReLU(W2 ReLU(W1 u+b1)+b2)+b3; mu(u)=W5 ReLU(W4 t+b4)+b5. All affines 512 to 512; independent modalities, identical P/D trunk/means. No normalization or dropout. | Fixed small residual graph avoids architecture search. A dropout alternative must name rate and identical P/D handling before freeze; no stochastic-inference/epistemic claim. |
| P scale/shape | Separate 512-to-512 ReLU-to-512 heads on t; alpha=f+softplus(a), beta=f+softplus(b), f=sqrt(2^-23). Float64 score/log-gamma reductions; no residual clamp. Zero/nonfinite output/objective fails. | Proposed precision-linked floor for unit features, not scientific threshold or proven stability. Analytic/domain and conformance review required. Alternative exp links without floor risk underflow/overflow and degeneracy; no dynamic epsilon or clipping rescue. |
| D constants | Remove input-dependent scale/shape heads; jointly fit one shared global pair of 512-vectors alpha0,beta0 with identical positivity map/objective; freeze with instance. | Approved comparison topology; no per-item or protected-control fits. Unit alpha0=beta0=1 is sensitivity only. |
| Fit eligibility | Independent, determinate-compatible native fitting records under proposed NA-A extraction below. | Clinical approval and observed yield still required. No generated contradictions, edited evaluation controls, error labels, provenance or intervention metadata in fitting. Missing eligible records stops/reopens. |
| Development subroles | After all reader/pilot/reliability/MV reserves, use train buckets 0-39 fit, 40-49 compatible-objective tune, 50-59 natural-development risk-map fit, 60-69 compatible normalizer; siblings remain together. Official validate only later calibration, test only later natural target. | Proposed DY-A subdivision of approved outer split, separating risk fitting from task/model fitting; counts are data-dependent. Shortfall triggers prospective amendment, no score-based reranking or protected-patient movement. |
| Optimization | Adam lr=1e-4, betas=(0.9,0.999), eps=1e-8, weight_decay=0, amsgrad=false; batch32 including short final batch; 100 full epochs; eta_e=0.5e-4(1+cos(pi e/100)), e=0..99. No clipping, AMP or restarts. | One configuration, equal P/D records/updates/trials. Select earliest minimum patient-weighted tune objective after all epochs separately per route. Failed runs consume existing ceiling; no automatic search/retries. Values beyond the source starting points are proposals. |
| Initialization/repetition | Seeds 0,1,2; seed0 primary, 1/2 paired sensitivities, never substitutes or ensemble. Shared P/D mean/trunk arrays; Xavier-uniform bound sqrt(6/(fan_in+fan_out)), zero biases. Final P scale/shape weights zero, biases softplus_inverse(1-f); D raw vectors same, initial alpha=beta=1. | Proposed reproducibility identifiers. Distinct named generator domains for shared means, added P heads and shuffling; same P/D patient order. Exact RNG serialization is software-lock evidence. Inference seeds remain unchanged. |
| Software | OpenCLIP 2.23.0, commit f08f25f3f226bdb538de2b4ed48a9213ba6b179e; BiomedCLIP snapshot above; institutional Linux/CUDA, float32 features/training, float64 score/statistic reference. | Before freeze require verified OS/Python/PyTorch/TorchVision/timm/Transformers/tokenizer/NumPy/SciPy/Pillow/CUDA/cuDNN/BLAS builds/hashes and deterministic settings. Choose one audited original-interface-compatible stack if security supports it, otherwise a maintained port with declared-output conformance. No untested transitive lock is asserted here. |
| Analytic capacity | P=18(512^2+512)=4,727,808; D=10(512^2+512)+2*512=2,627,584 active parameters, excluding encoder. | Derived from proposed graph, not measured. Verify realized counts/cost later. Both fit proposed 20m ceiling; this is not allocation or parameter/gradient/cost parity. |

### Likelihood and objective

Approved Method-A score interface, with coordinate mean and symmetric
cross-modal score:

`ell(u;mu,alpha,beta)=mean_k[(abs(u_k-mu_k)/alpha_k)^beta_k +
log(2 alpha_k)+lgamma(1/beta_k)-log(beta_k)]`.

`S_P=0.5[ell(u_t;q_v)+ell(u_v;q_t)]`; S_D uses its own means and global
constants. Higher is poorer fit; no added sigmoid, exponential or square.
For beta>0, zero residual contributes 0. Frozen-means sensitivity substitutes
D's same global constants into P's frozen means, isolating a direct score
path conditional on jointly trained means, not the training mechanism.

Proposed EX-A fitting objective is
`L=0.25[ell(u_v;q_v)+ell(u_t;q_t)+ell(u_t;q_v)+ell(u_v;q_t)]`, identical
for P/D on the same fitting records, with no extra L1/MSE/contrastive/semantic
label term. Equal four-term weights express the approved intra/cross topology;
they do not reproduce the original driver's defaults. A different objective
must be fully written and approved prospectively. Compatible membership is
selection supervision even without label tokens in inputs or targets.

### Secondary contrastive and artifact pipelines

POINT-INFONCE remains secondary. Engineer recommends D's point graph with
normalized mean outputs, score `-cos(m_v,m_t)` and fixed temperature 1. The
proposed semantic-safe batches have equal independently labelled polarities,
one record per patient: different-patient same-polarity opposite-modality
records are positives, opposite polarities negatives; same patient/source
including native diagonal is excluded. Missing positive/negative invalidates
the batch. Use the symmetric mean negative log of positive exp(cos) sum over
eligible exp(cos) sum, no memory bank, identical optimization/trial budget.
This mask adds semantic supervision and must be labelled privileged secondary.
Finite alternative: instance positives with exact-duplicate exclusion, known
same-polarity false negatives disclosed; never attribute its inferiority to
deterministic means generally. Model/statistical owners must choose; neither
policy becomes primary or inherits CLIP-Adapter implementation identity.

Proposed PR-A for G0-ARTIFACT A uses two fixed pipelines per four views: intercept plus
L2 logistic classifier, objective mean logloss+||w||^2/(2n), and CART Gini
depth4/minimum-leaf5, all features and deterministic lexical split ties. All
eight pipelines remain in the veto family; no search or strongest-only report.
Image/text views use respective frozen u; structured view uses length,
punctuation, approved template/polarity, AP/PA and renderer descriptors;
process view uses versioned editor/renderer/order/procedure codes, no medical
identifiers. Fit dictionaries/standardizers on 0-39, with no tuning or pipeline
deletion. The exact PR-A algorithm and resource-count proposal below require
owner adoption, software conformance and later measured capacity. Transform simultaneous BA intervals through
R=max(BA,1-BA); a BA interval spanning 0.5 has lower R=0.5. Wrong orientation
cannot manufacture a pass. Fixed probes are neither exhaustive nor proven
powerful; numerical pipeline proposals require their own power review.

## Statistical implementation interface

Source-derived Method A/SAP interface; future implementation and all numerical
cases are **NOT RUN**. Input consists of method, patient block, frozen polarity
stratum, complete sibling scores/reference mapping, independent acceptance and
split manifest, immutable per-method normalizer (mu0,sigma0), orientation a,
software/config hashes and frozen strata/weights. Row identifiers stay secure.

1. Validate patient separation, one source per patient, accepted complete
   siblings, both primary controls and finite sigma0>0. Missing blocks are not
   zero-imputed.
2. Set Z=a(S-mu0)/sigma0, D_C=Z_conflict-Z_compatible,
   D_j=Z_control_j-Z_reference_j, and G_hbmj=D_C-abs(D_j).
3. Set muhat_mj=sum_h w_h mean_b G_hbmj, with frozen w_h=n_h/n;
   se_mj=sqrt(sum_h w_h^2 s_hmj^2/n_h). Require n_h>=2 and every necessary
   finite positive SE.
4. psihat_m=min_j muhat_mj; Ahat=psihat_P-psihat_D. Each method uses its own
   compatible reference SD: dimensionless comparison, not shared raw scale.
5. Draw exactly 9,999 whole-patient within-stratum bootstrap samples, seed
   20270829, same indices for every method/control; normalizers fixed. Recompute
   means/SE. Any invalid observed or resampled required SE fails the endpoint;
   no redraw, discard or epsilon.
6. T*=(muhat*-muhat)/se*. Joint signed maximum over the frozen family uses
   one-based rank ceil((B+1)(1-alpha_F)), without interpolation, clipped below
   at zero. Lower psi uses all positive signs; lower A uses positive P and
   negative D; upper A reverses them. Equivalence uses max absolute T*.
7. Lpsi_m=min_j L_mj; Upsi_m=min_j U_mj;
   LA=min_j L_Pj-min_j U_Dj; UA=min_j U_Pj-min_j L_Dj.
   Do not bootstrap minima directly or substitute min_j(mu_Pj-mu_Dj).
8. Month 3 uses one-sided 90% family bounds/80% target family power;
   confirmation one-sided 97.5%/90%. Preserve fixed sequence: specificity,
   material advantage, proper-score increment, decision value. Existing
   proposed margins remain psi>0.20 and A>0.10; no alternate endpoint, seed or
   model rescues a failed approved hard kill.

psi_mag is the minimum of component means, not a mean of within-block minima.
Non-superiority remains inconclusive. Deterministic noninferiority requires
UA<0.10 and its own Lpsi>0.20; construct equivalence requires the confirmatory
95% simultaneous band inside [-0.10,0.10]. Subsumption additionally needs
independently passed downstream noninferiority. A_psi failure kills the current
Main Track route without logically refuting the construct definition; framework
value cannot bypass that route kill.

## Ablation and downstream boundaries

Retain all six families: remove C_vt; remove A_v,A_t,M_v,M_t separately;
replace P with primary full-route D; frozen P means with D constants; raw/SD/
median-MAD reports; four artifact-recovery views. Each needs stage/input/output/
claim applicability recorded before results. Structurally absent terms require
an exact matched substitute or narrower claim, not silent omission. Raw/MAD
are sensitivities, not alternative winners. Full-route P/D matches selection
information, score family and topology, not parameter count or gradient path.

Independent reader A/Y labels validate the construct; they are not
automatically available decision-time inputs. G0-DOWNSTREAM must choose:
(A, recommended) a governed deployment-feasible feature map from current
image/text, ordinary confidence and dev-trained proxies, with exact labels,
architecture, costs and independent validation; or (B) a reader-assisted/oracle
explanatory risk analysis with reading cost/access counted and no automated
selective-decision claim. Exact task classifier Yhat and abstention rule remain
required. GGD incompatibility is not itself a task classifier. Construction
condition/provenance and unavailable oracle labels cannot enter a deployable
risk model silently.

On eligible natural targets define H=1{Yhat differs from independent image Y}
and DeltaBSS=(BS_base-BS_aug)/BS_null, with null event probability frozen on
approved development/calibration and target weights frozen. Preserve inherited
proposed gates LDeltaBSS_P>0.02, LA_BSS>0.01; calibration equivalence for
absolute calibration-in-the-large error<=0.02 **probability** and calibration
slope [0.80,1.20]; risk reduction>0.01 at
90% coverage. Recommend intercept+slope logistic recalibration on official
validate; isotonic requires prospective complexity/power recalculation. Event
rate, paired loss covariance, effective n, complexity and review cost require
separate target-power lock. Screening 250/380 counts establish none of this.
Until classifier/proxy/cost/target details are frozen, downstream promotion and
decision-freeze readiness remain false, without blocking package completeness.
The probability-scale calibration error is distinct from the fitted logistic
recalibration intercept, which has log-odds units. Its precise evaluation
estimand/interval interface is supplied as proposed CAL-A below and remains
a statistical-owner choice; the 0.02
threshold must never be transferred to a log-odds intercept.

## Reviewable completions NA-A, PR-A, DY-A and DC-A

Engineer supplied these final `proposed` / `owner-decision` completions to make
non-data-dependent choices concrete. They are not approved defaults or tested
algorithms. External identities/security and later measurements remain separate
blockers. All original scientific thresholds remain unchanged.

### NA-A native assertion extraction

Only under later secure Stage-C authority, preserve original report bytes and
section/offset provenance. Select FINDINGS when a case-insensitive line-start
header exists, otherwise IMPRESSION; neither means exclude. Bound the section
at the next line-start all-capital heading followed by colon. Split spans only
at newline or whitespace immediately after '.', '?' or '!'; preserve bytes
inside the span. Retrieve the case-insensitive lexical sequence 'pleural
effusion' with optional final 's'. Select earliest byte offset before semantic
rating, never a later favorable span. The independent text panel must accept
exactly the single target proposition, intact/unique/definite polarity and no
second clinical assertion; independent image Y must agree. Failure excludes
the native record without further span search. Text/offsets/labels stay secure;
only approved attrition aggregates exit.

This preserves native wording and score-blind selection, supplying shared
semantic selection supervision but no label input/loss target to P/D. Clinical
owner must approve section precedence, lexical coverage and single-proposition
rule. Alternative NA-B uses the whole report with the same earliest-offset,
no-rewrite and independent-acceptance rules. Recommend bounded NA-A; no yield
or prevalence is asserted and no clinical contradiction is generated here.

Finite heading rule: LF/CRLF are line boundaries without rewriting bytes.
Recognize only full lines with optional ASCII space/tab, ASCII-case-insensitive
FINDINGS or IMPRESSION, colon and optional ASCII space/tab. Choose first
FINDINGS by byte offset, else first IMPRESSION; never concatenate repeated
sections. End at the first later full-line heading with optional space/tab,
ASCII uppercase word sequence `[A-Z][A-Z /-]*`, colon and optional space/tab,
or EOF. Unsupported forms exclude; broaden only by prospective clinical
approval. NA-B is never chosen after observing yield/model results.

### PR-A complete diagnostic algorithms

Keep all eight pipelines, with no tuning or deletion. Logistic condition1 uses
probability>=0.5; CART predicts majority, ties0. Ridge logistic starts at zero
in float64, unpenalized intercept, mean logloss+||w||^2/(2n); damped Newton
with Cholesky, step1 halved at most50 times, Armijo coefficient1/4. Stop when
full-gradient infinity norm<=sqrt(2^-52), at most100 Newton iterations.
Nonfinite values, failed factorization/line search or exhausted iterations
produce solver failure; no weaker tolerance or hidden extra regularization.
These numerical-work bounds are proposals, not scientific margins.

CART considers every feature, midpoint thresholds between consecutive finite
values, feature-index then threshold order, first maximal-gain split; positive
gain only, stop pure nodes, depth4/minimum leaf5. No random ties, feature
subsampling or pruning search. This capacity is not exhaustive detection.

Numeric dictionary: Unicode-code-point and fixed-tokenizer lengths, counts of
each ASCII punctuation character, AP/PA and prescribed renderer scalars. Fit
mean/population SD on probe-fit patients; constant columns map0 with receipt;
missing values map fit mean plus missing indicator. Categorical levels use the
schema where known, otherwise UTF-8-byte-sorted fit values plus typed MISSING
and UNSEEN. Retain all one-hot columns, no target-frequency encoding/pooling
or medical IDs. Freeze dictionary/code hashes before protected access. Actual
fit vocabulary is data-dependent under this deterministic rule.

Development diagnostics propose 999 independently seeded whole-patient
condition swaps, seed0/domain 'artifact-permutation', swapping sibling labels
together and refitting preprocessing plus all eight pipelines. Report
`p=(1+#permuted statistic>=observed)/1000` for transparency, with no new p gate.
The statistic is T_perm=max_j R_j over all eight, using the same balanced,
frozen-stratum-weighted BA. Fit each realization on 0-39 and evaluate only on
independent development 40-49, with no tuning or fitting to evaluation labels.
Independently swap each patient's sibling labels with probability1/2 within
each split, rerun the full fit/score path and retain all individual observed R
and indexed permutation maxima. This diagnostic assumes label exchangeability;
no protected 70-84/85-99 permutation diagnostics. Constant views remain in the
family without fabricated variability or deletion.
The exact workload ceiling is 8*(999+1)=8,000 fitted pipelines, failures
accounted. A later brief must approve finite CPU/wall/scratch bounds; if
unaffordable retain unready status or prospectively choose PR-B with recalculated
precision, never automatically reduce repetitions.

For fixed fitted probes, propose conservative simultaneous bounded-mean
intervals instead of an unfrozen bootstrap-SE procedure. Patient
`x_b=0.5(correct compatible sibling+correct conflict sibling)` lies in [0,1].
`BA_j=sum_h w_h mean_b x_hbj`; K=8 and
`h_alpha=sqrt(0.5 log(2K/alpha_F) sum_h w_h^2/n_h)`.
Intervals are `[max(0,BA_j-h_alpha),min(1,BA_j+h_alpha)]`, stage alpha_F=0.10
or 0.025. This Hoeffding/union-bound proposal assumes independently sampled
patient blocks within frozen strata, conditional on locked probe fits. It
remains defined at constant BA=0.5, is conservative and establishes no powered
equivalence. Transform endpoints through R; lower is0.5 if interval spans0.5,
otherwise minimum transformed endpoint; upper is maximum. Preserve 0.55
kill/inconclusive/limited-evidence meanings. This does not replace 9,999 max-t
psi/A, reader or MV inference, nor approve artifact option B. Owner approval of
features/independence, bounds for 8,000 fits and later kernel conformance remain.

### DY-A task, proxy and risk interfaces

Use the EX-A subpools 0-39 fitting, 40-49 objective tuning, 50-59 risk fitting,
60-69 normalization, after reserves. One common ridge-logistic task classifier
on [u_v,u_t] uses PR-A objective/solver and independent image Y only in fitting.
Yhat=1 iff p_task>=0.5. Supported finite inputs yield binary answers before
selection; missing/unsupported/nonfinite inputs are task failures, not correct
abstentions. H exists only for determinate independent target image Y; report
all exclusions/undefined outcomes. This separate task-model supervision never
enters the P/D reconstruction loss.

Fit modality-only multinomial ridge proxies on separately authorized
independently labelled fitting-development records: image 3-class integrity,
3-class coverage, 3-class semantic status; text 4-class integrity and 3-class
interpretation. Use raw protocol categories, including not-assessable, without
relabeling ambiguity. Same regularized cross-entropy/Newton work bounds,
last printed category as identifiable reference, penalty on nonreference
coefficients. Missing required training class or nonconvergence means unready,
not silent pooling. Retain frozen models/dictionaries and exact subset ledger.

A_v is image genuine-ambiguity probability; A_t text multiple-readings
probability. M_v comprises two non-intact technical and two non-complete
coverage probabilities; M_t the three non-intact text-integrity probabilities.
These are measurement proxies, not oracle labels or uncertainty identities.
Ordinary confidence=max(p_task,1-p_task); output uncertainty is Bernoulli
entropy, not semantic-generation entropy.

Optional proposed U_epi is population variance (divisor3) of p_task from three
fixed patient-bootstrap task-model refits, seeds0/1/2 in 'task-bootstrap'
domain. This is a finite-committee proxy, not epistemic truth; later budget
must include all refits/labels. If declined/unavailable, mark structurally
absent and narrow claim, never insert0 as if controlled.

On natural-development 50-59, baseline ridge-logistic risk uses confidence,
binary entropy, U_epi if approved, A_v/A_t/M_v/M_t. P augmentation adds Z_P,
D adds Z_D; same patients/H, preprocessing/solver and capacity opportunity.
Each removal refits only that risk model on the same subpool; task/proxy/P/D
instances remain fixed. Normalizers use disjoint 60-69 compatible references,
never risk labels. C_vt in this interface is the frozen score Z, not oracle C*.

Official-validation recalibration fits unpenalized intercept+slope binomial
likelihood to each fixed risk logit and H, with both classes required. Nonfinite,
separated or unidentifiable fit fails; no automatic Firth/isotonic rescue.
Official-test eligible natural target has unit weights unless prospectively
changed. Independent A/Y validate outcomes, never compute runtime risk;
identifiers/provenance/condition are excluded. A frozen private patient rank
may only resolve policy ties. Clinical eligibility, statistical complexity,
exact labelled subsets/refit costs and software conformance require approval;
class support, proxy fidelity, event covariance and calibration support require
later data. Explicit equations do not establish power readiness.

### DC-A equal-review-count decision endpoint

For N eligible target patients, answer floor(0.90N) with smallest calibrated
error risk and send remainder to review; ties use frozen private rank. Report
actual counts/coverage, compare identical patients and integer review count;
full risk-coverage curve is secondary. Measure error among answered patients,
never assume review repairs all referred errors or credit unmeasured accuracy.
DC-A supports retrospective equal-review-count risk, not net clinical utility.
Actual reviews still need measured minutes, queue capacity/access and authority.
Alternative DC-B expected utility requires a prospectively justified loss table
for correct/incorrect answer, review delay/time and residual review error with
units/evidence and recalculated power. Recommend DC-A without inventing
clinical-economic constants or claiming clinical benefit.

### CAL-A probability-scale evaluation and joint intervals

This Engineer correction supersedes the erroneous draft intercept tolerance.
The public methods article [Calibration: the Achilles heel of predictive analytics](https://doi.org/10.1186/s12916-019-1466-7)
distinguishes mean predicted risk versus event rate from intercept/slope
assessment. This narrow source check supplies no new margins and validates
none of CAL-A's proposed bootstrap operating characteristics.

For each frozen calibrated baseline/P/D risk map, retain p_im and finite
pre-sigmoid eta_im. Never refit predictors, proxies, risk maps or validation
recalibrators on target. For DY-A unit-weight natural-prevalence independent
patients define c_m=E[p_m-H], chat=mean(p-H), SE=sampleSD(p-H)/sqrt(N).
Positive c is overprediction. The inherited gate is c in [-0.02,0.02], not
log-odds intercept or mean absolute individual error. Enriched/weighted targets
require a prospectively specified sampling-aware replacement and power review.

Diagnostic slope beta is the unpenalized logistic projection of H on stored
eta with a free intercept, used solely for evaluation, never to update p.
It does not assert a linear full calibration curve. Minimize float64 mean
negative loglikelihood `mean[logaddexp(0,a+beta*eta)-H*(a+beta*eta)]`
from (a,beta)=(0,1) using PR-A Newton/Armijo/100-step/
50-halving/full-gradient tolerance. Both H classes and full-rank design are
required. Reject constant eta or either ordered-range separation condition:
max(eta|H=0)<=min(eta|H=1), or max(eta|H=1)<=min(eta|H=0).
No small-gradient acceptance of divergence, probability clipping, Firth,
ridge or isotonic rescue. The diagnostic intercept has no 0.02 gate.

With x_i=(1,eta_i), fitted pi_i, use A=sum pi_i(1-pi_i)x_i x_i^T,
B=sum(H_i-pi_i)^2 x_i x_i^T, V=A^-1 B A^-1 and SE_beta=sqrt(V_22).
This is HC0 patient sandwich with one record/patient; A must be nonsingular,
all necessary SE finite/positive. It does not assume model-correct Fisher SE.

Proposed joint family theta=(c_base,beta_base,c_P,beta_P,c_D,beta_D) uses
9,999 **unstratified** whole-patient target resamples of N, common indices for
all coordinates; seed20270829 in distinct serialized domain
'target-calibration', not construct draws. Refit only three diagnostic slopes
and recompute signed means/SE per draw. T*=(theta*-thetahat)/SE*, M*=max|T*|;
alpha=0.05, one-based sorted rank9500, critical=max(0,M*_(9500)); bands
thetahat +/- critical*SEhat. Any failed fit, missing class, separation,
nonfinite value or invalid required SE in any indexed draw makes analysis
non-estimable/inconclusive. Preserve failed identities; no dropping/redraw or
epsilon. This is an asymptotic proposal requiring future power/operating
validation, not finite-sample exact coverage.

For each map claimed calibrated, its simultaneous c band must lie wholly in
[-0.02,0.02] and slope band in [0.80,1.20]. D4 must name which maps must pass;
recommend all three in the symmetric interval family. Failed required P
calibration stops its downstream promotion; failed D calibration prevents
downstream subsumption without changing the prior construct verdict. These
are retrospective planning tolerances, not clinical safety.

Workload is 3*(9999+1)=30,000 two-parameter diagnostic fits plus six scalar
reductions per sample, requiring a later target-compute brief and allocation.
Screening 250/380 counts establish no power. If burden/degeneracy is
unacceptable, choose a fully specified alternative prospectively and re-power;
never reduce B after results. CAL-A is available for review, unapproved and
unrun; source/software/security, operating properties and data support remain
distinct unresolved evidence.
