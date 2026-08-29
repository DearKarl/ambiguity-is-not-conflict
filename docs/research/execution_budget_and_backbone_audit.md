# Execution Budget and Backbone Audit

**Status:** Gate-0 planning candidate; no checkpoint, environment, compute, or
clinical work is authorized

**Date:** 2026-08-29
**Evidence class:** Official model documentation, unverified resource
ceilings, and TB-0009 deterministic simulation-workload arithmetic

## Blocking Finding

No pretrained VLM is currently unconditionally eligible for strict
confirmatory evidence on MIMIC patients. A model card can establish known
exposure, but absence of a stated MIMIC source is not proof of patient-level
non-exposure. BiomedCLIP is the strongest small conditional candidate;
SigLIP2 is the best matched general-domain dual-encoder breadth candidate;
BioViL-T supplies a useful exposure-positive diagnostic; Qwen2.5-VL is an
interface-diverse stress candidate. A source/type/time-auditable ImageNet-1K
ResNet-50 plus original BooksCorpus/Wikipedia BERT is a candidate strict
**non-VLM control**, not strict VLM breadth. Every exact checkpoint remains
unapproved.

## Official-Source Shortlist

| Candidate role | Verified public facts | Exposure and eligibility decision |
| --- | --- | --- |
| Conditional primary representation: [BiomedCLIP](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224) | Microsoft model card describes a PubMedBERT plus ViT-B/16 contrastive model trained on 15 million PubMed Central figure-caption pairs, with 224-pixel images, 256-token context, and MIT licence. | No explicit MIMIC training is stated, but no patient/block exclusion manifest is supplied and scientific papers may reproduce source images/text. Strict confirmation requires an immutable checkpoint SHA, training-snapshot provenance, and approved perceptual/text overlap audit; otherwise sensitivity only. |
| Matched general-domain dual-encoder breadth: [SigLIP2 base patch16 224](https://huggingface.co/google/siglip2-base-patch16-224) | Google card documents a ViT-B image-text encoder, 224-pixel interface, WebLI-based training, Transformers support, and Apache-2.0 licence. | No sample-level MIMIC exclusion is documented. Eligible only as unknown-exposure breadth/sensitivity unless an overlap audit clears the final blocks. |
| Lower-intent, unknown-overlap non-VLM architectural control: [TorchVision ResNet-50 V2](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html) plus [BiomedBERT abstracts](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) | Official pages describe an ImageNet-1K vision encoder and PubMed-abstract text encoder. They are not jointly pretrained and therefore are not a pretrained VLM. | No intentional MIMIC source is documented, but exact web/literature overlap is unknown. It remains unknown-exposure sensitivity unless the same audit clears it; it cannot be called contamination-negative or strict-confirmatory. Freeze inherited ImageNet, TorchVision, BiomedBERT code/weight licences and exact revisions before use. |
| Source/type/time-auditable strict-control lead: [TorchVision ResNet-50](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html) plus [original BERT](https://aclanthology.org/N19-1423/) | TorchVision documents ImageNet-1K weights; the BERT paper documents BooksCorpus and English Wikipedia pretraining. The components are not jointly pretrained, and an approved cross-modal head would be trained only on project-development patients. | Candidate strict **non-VLM** control only if immutable original weight/conversion lineage, dates, declared-source completeness, licences, and the development-only training boundary are independently cleared before download. It cannot establish strict medical-VLM or cross-VLM confirmation. |
| Known-exposure diagnostic: [BioViL-T](https://huggingface.co/microsoft/BiomedVLP-BioViL-T) | Microsoft card explicitly describes PubMed plus MIMIC/MIMIC-CXR training and an MIT-licensed radiology vision-language interface. | Categorically ineligible for primary or confirmatory MIMIC evidence; retain only as a contamination-positive diagnostic. Custom-code loading requires a separate pinned-code security review. |
| Interface-diverse stress: [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) | Official card supplies an image-text-to-text Transformers interface and Apache-2.0 licence for the 7B checkpoint. | Training overlap is not documented at sample level and the generative interface is not estimator-matched. Sensitivity/breadth only; freeze prompts, verbalizers, tokenization, pixel range, and local next-token scoring. No hosted API. |

CheXzero and any other checkpoint explicitly trained on MIMIC remain known-
exposure diagnostics unless exact training-patient disjointness from the final
partition is independently established. Newly written text variants reduce
exact-pair reuse but do not erase exposure to their source patient, image, or
report.

## Required Checkpoint Record

Before any download or environment creation, freeze for each candidate:

- exact repository, revision/tag, immutable commit and weight SHA256;
- model card, architecture, preprocessing, tokenizer, input resolution/context,
  embedding/readout interface, and dependency lock;
- code, weight, dataset, and inherited asset licences;
- training sources, dates, known/unknown patient or benchmark overlap, and role
  (`strict-confirmatory`, `unknown-exposure sensitivity`, or
  `known-exposure diagnostic`);
- approved local cache, custom-code policy, network boundary, and security
  review;
- trainable components, parameter count, tuning trials, seeds, calibration
  budget, and hardware ceiling;
- evidence that the comparator receives the same input and supervision budget.

Never use moving `main`, `latest`, or library `DEFAULT` aliases in a frozen
run. Unknown exposure is reported as unknown; it is not converted to clean by
absence of evidence.

## Candidate Exposure-Audit Sequence

1. Official-card and primary-paper audit without weights.
2. After separate authorization, record immutable repository/checkpoint hashes
   without scientific inference.
3. In the secure environment, compare final patient/block image hashes,
   perceptual hashes, report/atomic-text fingerprints, and cited-source
   provenance against any available training manifest.
4. Classify exact, near, source/patient, publication-reproduction, or unknown
   overlap under frozen tolerances.
5. Exclude exposed blocks/checkpoints only under the pre-specified rule; do not
   search for a favourable subset after results.
6. If the training manifest is unavailable or incomplete, retain
   `unknown-exposure sensitivity` status. No strict held-out wording is allowed.

The finite evidence-tier decision is:

- `strict-confirmatory`: a complete source/patient manifest and overlap audit;
  a representation whose documented source/type/time cannot contain the target
  records and whose project head uses development patients only; or a
  sequestered/post-checkpoint target cohort;
- `unknown-exposure sensitivity`: project-fit splits are respected but
  pretraining exposure remains unknown; and
- `known-exposure diagnostic`: official documentation or an audit establishes
  source/final-patient exposure.

BiomedCLIP, SigLIP2, and Qwen2.5-VL remain unknown-exposure sensitivity;
BioViL-T remains known-exposure diagnostic. The source/time-auditable generic
pair is only a strict-control lead. If no strict route is available before
confirmation, claims must be narrowed to project-split intervention response
under unknown pretraining exposure; “strict held-out,” “clean checkpoint,” and
“unseen to the model” are prohibited. The owner decision and alternatives are
in the [Gate-0 decision dossier](gate0_decision_dossier.md).

## Planning Ceilings

These are hard proposal ceilings, not statements of available resources or
measured requirements.

| Resource | Stage-1/Month-3 candidate ceiling | Cumulative paper-route candidate ceiling | Stop consequence |
| --- | ---: | ---: | --- |
| Metadata feasibility | 8 CPU-hours; 5 GB encrypted scratch; 10 MB aggregate output | Same | Any record/image/report access or larger export requires a new brief. |
| Restricted working storage | 1 TB encrypted approved storage; selected JPG/report records only | 1 TB | Full DICOM/corpus need or >1 TB reopens data approval. |
| Checkpoint cache | 50 GB | 100 GB model plus environment artifacts | No unpinned or undeclared cache growth. |
| Accelerator memory | One local/institutional GPU, at most 48 GB VRAM | At most four approved GPUs, 48 GB each; no multi-node job | Re-plan rather than changing model/interface silently. |
| Accelerator time | 300 GPU-hours total | 1,500 GPU-hours total | Exceeding either ceiling stops work pending Commander/infrastructure approval. |
| Trainable parameters | At most 20 million per matched head/adapter; encoders frozen | Same unless a new scientific decision approves backbone tuning | No full-backbone fine-tuning under this candidate. |
| Clinical time | 500 person-hours through qualification and the balanced 216-block Month-3 construct gate | 1,350 person-hours cumulative through four-control confirmation/target audit | Stop after timing pilot or allocation update if the line-item ceiling is exceeded. |
| Paid/external services | None | None unless separately approved | No remote clinical data/model inference or silent paid compute. |

The cumulative GPU ceiling is a guardrail, not an allocation. A later run
matrix must show why every backbone × method × seed cell is necessary and fit
inside it. Failed runs count. Hardware, wall time, energy where available,
peak memory, trainable parameters, and tuning attempts are retained.

## Pre-Reader Simulation Resource Status

The [simulation resource-feasibility audit](simulation_resource_feasibility_audit.md)
compiles the TB-0008 contract into 10,847 reliability candidates and 2,438
pre-calibration `MV-1` candidates. Its successful full path contains up to
1,594,200,000 outer datasets and 15,940,405,800,000 nested bootstrap analyses.
These are exact or explicitly bounded logical work units, not CPU/GPU time,
memory, storage, cost, energy, or feasibility measurements.

No row above allocates CPU-core-hours, peak RAM, scratch, persistent-output
storage, wall time, or contingency for this simulation. The metadata CPU row
cannot be repurposed, and the accelerator ceiling cannot be treated as an
available allocation. Consequently `G0-READERS`, `G0-MV-Q`, and
`G0-RESOURCES` remain simulation- and feasibility-blocked.

The [non-core computational design](noncore_simulation_computational_design.md)
now supplies a static stage graph, proposed audit schema, restart rules,
proof-obligation register, workload crosswalk, and future benchmark acceptance
equations. TB-0011's
[output/operation registry](simulation_output_and_operation_registry.md)
supersedes its 56-byte prefix and 312/568-byte record arithmetic. The corrected
conditional all-candidate catalogue/lock/bitmap/core-record floor is exactly
613,093,770,610 bytes before unresolved typed static/aggregate/family,
permutation, journal, failure-detail, format, retry, overhead, scratch,
redundancy, or backup terms. This is schema arithmetic, not measured storage,
a final upper bound, or an allocation. The logical registry is a complete
static candidate, but its named owner choices and physical extension bounds
remain open.

The recommended next resource action is to approve or amend that registry,
close every extension and the final storage upper bound, then issue a
separately bounded workload-equivalent generic-kernel benchmark brief. It may
not implement or call the project RNG, DGP,
calibration equations, bootstrap statistic, or scientific pipeline while Gate
0 is open; exact scientific implementation remains a post-Gate-0 action.
Streaming, exact sufficient statistics, canonical deduplication, and
independent-cell parallelism may reduce implementation cost only if they
preserve the frozen outputs. Any statistical replacement, staged design, or
grid change requires prospective statistical proof, a dated amendment, and
complete re-enumeration. Lowering 120,000 or 9,999, deleting hard cells, or
weakening scientific thresholds to fit a ceiling is prohibited.

## Clinical-Workload Assumptions

The stronger measurement candidate requires at least ten image readers when
original/altered image siblings each need disjoint five-reader panels, at least
six text readers for disjoint three-reader polarity panels, and at least six
cross-modal readers for disjoint unanimous three-person sibling panels. The
`G0-READERS A` reliability candidate makes the image, text, and pair rosters
mutually exclusive, so it requires at least 22 qualified people unless a new
dependence, blinding, precision, and workload design is approved.
Planning rates are at most two minutes per image rating, 30 seconds per text
rating, and two minutes per cross-modal/adjudication action. Under the locked
reliability allocation, the per-reader ceiling rule gives exactly 120 image,
114 text, and 72 pair-repeat ratings; up to 20% pair adjudication is also
budgeted.

The proposed workload worksheet is deliberately conservative:

| Phase | Frozen planning workload | Candidate person-hours |
| --- | --- | ---: |
| Qualification/timing | Training/meetings plus 60 screened sources; two image inputs × five, three text variants × three, four cross-modal pairs × three, 15% unimodal repeats, 20% pair adjudication | 80 |
| Locked reliability | Disjoint 150-unit set: image items × five, text items × five, and pair-validity items × three; exactly 120 image, 114 text, and 72 pair-repeat ratings under `ceil(0.15 N_r)` per reader; 20% pair adjudication/meetings | 60 |
| `MV-1` task-relevance qualification | Recommended `G0-MV-Q A`: all 300 ranked candidates (150 per report-screen sampling stratum) receive intact and transformed sibling panels × five so attrition is observed rather than assumed; 15% blinded image repeats, cyclic disjoint-panel balancing, audit, and meetings; independently assigned image polarity must yield at least 108 evaluable blocks per state | 129 |
| Month-3 construct | 260 original images screened × five; 216 altered `M_v` images × five; 216 × three text variants × three; 216 × four pairs × three; repeats/adjudication/meetings | 217 |
| Four-control confirmation | 470 original images screened × five; up to two altered images for each of 400 eligible sources × five; 400 × four text variants × three; 400 × six pairs × three; repeats/adjudication/meetings | 605 |
| Natural-ambiguity veto audit | After a Month-3 pass and before claim promotion: up to 100 recruited candidates; original image × five and text × five ratings, 15% blinded repeats, overlap review, adjudication, and meetings | 45 |
| Natural-target QA | Separately approved target checks, error labels, calibration/decision QA, and meetings | 145 |
| Rounding/timing contingency | Unallocated reserve after explicitly reallocating 19 hours to the enlarged `MV-1` qualification candidate; it cannot substitute for an omitted required phase | 69 |
| **Total ceiling** | Qualification through target audit | **1,350** |

The first four rows total 486 and fit under the 500-hour stage ceiling; the
natural-ambiguity audit is expressly deferred until after a Month-3 pass and is
not charged to the stage ceiling. The pre-target rows including that audit
total 1,136 hours. It is a veto-only observational audit, not an ambiguity-
identification result, and requires its own bounded authorization. A 60-source
timing/rubric pilot **would require a later bounded authorization** and stops if
median image time exceeds 2.5 minutes, text time exceeds 45 seconds, cross-
modal time exceeds two minutes, roster allocation fails, reliability/
retraining violates the annotation protocol, or the projected stage/
cumulative total exceeds 500/1,350 hours.

The 300-candidate row and 69-hour reserve are a balanced worksheet, not
verified capacity. The [reader measurement and MV-1 qualification
audit](reader_measurement_and_mv1_qualification_audit.md) derives the
synthetic yield risk, finite-roster analysis, simulation contract, and
`110(300/256)=128.9`-hour linear scaling. Any owner rejection or timing
overrun reopens `G0-MV-Q` and `G0-RESOURCES`; the scientific floor may not be
weakened to restore contingency.

The optional orientation-safe four-probe equivalence route is incompatible
with these ceilings under the current linear worksheet: its illustrative
1,047/1,757 evaluable patient requirements imply approximately 1,302 clinical
hours through Month 3 and 2,657 hours for the scaled confirmation row alone.
Those are planning extrapolations, not measured workload. The recommended
current-budget choice is therefore exact construction balance plus a
diagnostic probe veto, with no global artifact-equivalence claim. A resource
increase cannot be inferred from this audit.

Reader identities, qualifications, roster sizes, availability, compensation,
institutional ethics, and these timing assumptions are all unverified. If the
disjoint-reader design is unavailable, the project must justify a powered
incomplete-block or washout/dependence model, recompute person-hours and
reliability precision, or narrow the evidence; it may not silently replace
independent coverage with two readers plus adjudication.

## Candidate Minimal Run Matrix

Month 3 must remain a kill test, not a method zoo. Under one conditional
dual-encoder backbone and the same frozen input, splits, preprocessing,
trainable-parameter ceiling, and tuning budget:

1. raw deterministic similarity/retrieval margin;
2. matched learned deterministic compatibility or density-ratio predictor;
3. one task-valid evidential comparator;
4. one probabilistic/distributional adapter;
5. matched point-softmax adapter when covariance or scale is credited;
6. nuisance-only probes and normalization/artifact controls.

Gate 0 must name one exact uncertainty-aware estimator definition/interface
and its matched deterministic comparator before any implementation. Bucket
0--69 may fit/tune only within those rules while implementing the frozen
comparison set; the fitted primary instances and complete configurations lock
before Month-3 access. Other frozen methods remain secondary comparators and
cannot become primary because of development or protected-set performance.

Only after one candidate passes may breadth add SigLIP2 and the explicitly
labelled BioViL-T/Qwen diagnostics. The matched deterministic route must receive
the same information and at least comparable capacity/tuning opportunity.

## Approval Sequence

1. Commander approves the task, statistical margins, and 1-TB/300-to-1,500-
   GPU-hour/500-to-1,350-clinical-person-hour ceilings.
2. Clinical owner approves the ten/six/six minimum rosters, disjoint sibling
   panels, five-reader image evidence, timing pilot, adjudication, and stop
   rules.
3. Governance/infrastructure owners verify every reader's approved access
   basis, named ACL and UI/export control, secure storage, hardware, account
   isolation, retention, permitted artifacts, and no-hosted-API boundary.
4. Model owner freezes exact revisions, licences, code-security review,
   preprocessing, interfaces, and exposure roles.
5. An independent reviewer verifies the overlap-audit plan and matched run
   matrix before any checkpoint access.
6. A new bounded brief may then authorize only the named access or feasibility
   action. Scientific execution remains separately gated.

## Permitted Claim

This audit identifies a conditional backbone route, hard planning ceilings,
and a deterministic simulation-workload envelope. It does not establish
checkpoint cleanliness, model availability, secure capacity, clinician or
simulation capacity, runtime, affordability, feasibility, performance,
clinical benefit, Gate-0 closure, or venue fit.
