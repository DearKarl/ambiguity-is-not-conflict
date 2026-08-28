# Execution Budget and Backbone Audit

**Status:** Gate-0 planning candidate; no checkpoint, environment, compute, or
clinical work is authorized

**Date:** 2026-08-29
**Evidence class:** Official model documentation plus unverified resource
ceilings

## Blocking Finding

No pretrained VLM is currently unconditionally eligible for strict
confirmatory evidence on MIMIC patients. A model card can establish known
exposure, but absence of a stated MIMIC source is not proof of patient-level
non-exposure. BiomedCLIP is the strongest small conditional candidate;
SigLIP2 is the best matched general-domain dual-encoder breadth candidate;
BioViL-T supplies a useful exposure-positive diagnostic; Qwen2.5-VL is an
interface-diverse stress candidate. Every exact checkpoint remains unapproved.

## Official-Source Shortlist

| Candidate role | Verified public facts | Exposure and eligibility decision |
| --- | --- | --- |
| Conditional primary representation: [BiomedCLIP](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224) | Microsoft model card describes a PubMedBERT plus ViT-B/16 contrastive model trained on 15 million PubMed Central figure-caption pairs, with 224-pixel images, 256-token context, and MIT licence. | No explicit MIMIC training is stated, but no patient/block exclusion manifest is supplied and scientific papers may reproduce source images/text. Strict confirmation requires an immutable checkpoint SHA, training-snapshot provenance, and approved perceptual/text overlap audit; otherwise sensitivity only. |
| Matched general-domain dual-encoder breadth: [SigLIP2 base patch16 224](https://huggingface.co/google/siglip2-base-patch16-224) | Google card documents a ViT-B image-text encoder, 224-pixel interface, WebLI-based training, Transformers support, and Apache-2.0 licence. | No sample-level MIMIC exclusion is documented. Eligible only as unknown-exposure breadth/sensitivity unless an overlap audit clears the final blocks. |
| Lower-intent, unknown-overlap non-VLM architectural control: [TorchVision ResNet-50 V2](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html) plus [BiomedBERT abstracts](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) | Official pages describe an ImageNet-1K vision encoder and PubMed-abstract text encoder. They are not jointly pretrained and therefore are not a pretrained VLM. | No intentional MIMIC source is documented, but exact web/literature overlap is unknown. It remains unknown-exposure sensitivity unless the same audit clears it; it cannot be called contamination-negative or strict-confirmatory. Freeze inherited ImageNet, TorchVision, BiomedBERT code/weight licences and exact revisions before use. |
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
| Clinical time | 400 person-hours through qualification and the balanced 216-block Month-3 construct gate | 1,200 person-hours cumulative through four-control confirmation/target audit | Stop after timing pilot or allocation update if the line-item ceiling is exceeded. |
| Paid/external services | None | None unless separately approved | No remote clinical data/model inference or silent paid compute. |

The cumulative GPU ceiling is a guardrail, not an allocation. A later run
matrix must show why every backbone × method × seed cell is necessary and fit
inside it. Failed runs count. Hardware, wall time, energy where available,
peak memory, trainable parameters, and tuning attempts are retained.

## Clinical-Workload Assumptions

The stronger measurement candidate requires at least ten image readers when
original/altered image siblings each need disjoint five-reader panels, at least
six text readers for disjoint three-reader polarity panels, and at least six
cross-modal readers for disjoint unanimous three-person sibling panels.
Planning rates are at most two minutes per image rating, 30 seconds per text
rating, and two minutes per cross-modal/adjudication action, with a 15% blinded
unimodal repeat and up to 20% adjudication.

The proposed workload worksheet is deliberately conservative:

| Phase | Frozen planning workload | Candidate person-hours |
| --- | --- | ---: |
| Qualification/timing | Training/meetings plus 60 screened sources; two image inputs × five, three text variants × three, four cross-modal pairs × three, 15% unimodal repeats, 20% pair adjudication | 80 |
| Locked reliability | 150 image items × five; 150 text items × up to five (five for natural-ambiguity items, disjoint three-reader panels for polarity siblings); 150 pair-validity items × three; 15% unimodal repeats; 20% adjudication/meetings | 60 |
| Month-3 construct | 260 original images screened × five; 216 altered `M_v` images × five; 216 × three text variants × three; 216 × four pairs × three; repeats/adjudication/meetings | 217 |
| Four-control confirmation | 470 original images screened × five; up to two altered images for each of 400 eligible sources × five; 400 × four text variants × three; 400 × six pairs × three; repeats/adjudication/meetings | 605 |
| Natural-ambiguity veto audit | After a Month-3 pass and before claim promotion: up to 100 recruited candidates; original image × five and text × five ratings, 15% blinded repeats, overlap review, adjudication, and meetings | 45 |
| Natural-target QA | Separately approved target checks, error labels, calibration/decision QA, and meetings | 145 |
| Rounding/timing contingency | Unallocated reserve; it cannot substitute for an omitted required phase | 48 |
| **Total ceiling** | Qualification through target audit | **1,200** |

The first three rows total 357 and fit under the 400-hour stage ceiling; the
natural-ambiguity audit is expressly deferred until after a Month-3 pass and is
not charged to the stage ceiling. The pre-target rows including that audit
total 1,007 hours. It is a veto-only observational audit, not an ambiguity-
identification result, and requires its own bounded authorization. A 60-source
timing/rubric pilot **would require a later bounded authorization** and stops if
median image time exceeds 2.5 minutes, text time exceeds 45 seconds, cross-
modal time exceeds two minutes, roster allocation fails, reliability/
retraining violates the annotation protocol, or the projected stage/
cumulative total exceeds 400/1,200 hours.

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

All candidates may be developed in bucket 0--69, but exactly one uncertainty-
aware candidate must be named primary before Month-3 holdout access; the rest
are secondary unless the multiplicity and power family is prospectively
expanded. The matched deterministic route remains its primary comparator.

Only after one candidate passes may breadth add SigLIP2 and the explicitly
labelled BioViL-T/Qwen diagnostics. The matched deterministic route must receive
the same information and at least comparable capacity/tuning opportunity.

## Approval Sequence

1. Commander approves the task, statistical margins, and 1-TB/300-to-1,500-
   GPU-hour/400-to-1,200-clinical-person-hour ceilings.
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

This audit identifies a conditional backbone route and hard planning ceilings.
It does not establish checkpoint cleanliness, model availability, secure
capacity, clinician capacity, feasibility, performance, clinical benefit,
Gate-0 closure, or venue fit.
