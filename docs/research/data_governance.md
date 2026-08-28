# Data and Clinical Governance

**Status:** Candidate data route; no dataset access approved by this document

## Minimal Viable Data Route

The current candidate route is:

1. MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 as one coupled patient-level
   source: native DICOM/report linkage plus standardized JPG/metadata/reference
   splits, not two independent datasets;
2. a patient-separated, single-finding subset with independently judged image
   truth, counterbalanced compatible/conflicting atomic assertions, and
   separately measured image ambiguity, text ambiguity, missingness, and
   corruption controls;
3. clinical review of the intervention construct and a confirmatory subset;
4. ReXErr only as an MIMIC-derived synthetic report-error stress test if its
   units and labels match the frozen task;
5. after the primary instrument passes, either VisMin with added ambiguity and
   information-loss controls or a separately governed medical resource such as
   PadChest-GR for breadth.

A second, separately sampled **target-distribution cohort** is required for
calibration and selective-review claims. Its natural prevalence and inclusion
rules must not be replaced by the balanced intervention-cell frequencies.

Candidate status does not imply credentialing, access, licence compatibility,
scientific suitability, or permission to redistribute derived artifacts.
The complete official-source comparison is in the
[dataset feasibility audit](dataset_feasibility_audit.md).

## Pre-Access Gate-0 Dataset Record

Before any download or access, freeze the planned route:

- canonical name, version, release date, intended access route, and planned
  access window; the actual access date is recorded only after authorized
  access occurs;
- licence, data-use agreement, credentialing, ethics, and storage boundary;
- task, prediction unit, ontology, planned inclusion/exclusion criteria, exact
  metadata-only feasibility query/schema, minimum viable counts, and stop rules;
- planned patient-level split, repeated-study links, duplicates, and leakage
  controls;
- planned label extraction, uncertainty, provenance, and adjudication;
- model pretraining overlap and benchmark contamination where assessable;
- subgroup definitions and minimum reporting sizes;
- permitted derived metadata, retention, deletion, and sharing rules.

Gate-0 closure does not require invented observed counts or a retrospective
access date. After Gate 0 freezes, a new bounded brief may authorize only the
pre-specified metadata feasibility check in the approved environment. That
check must record the actual access date, immutable resource snapshot, observed
counts, exclusions, and cohort flow. If the frozen minimum counts or leakage
conditions fail, data work stops and Gate 0 reopens. No record inspection,
clinical annotation, model execution, or intervention generation may proceed
until the feasibility record is reviewed and the dataset decision is amended.

## Split and Leakage Rules

- Patients must not cross training, calibration, development, or final-test
  partitions.
- Studies, images, reports, paraphrases, findings, and counterfactuals from the
  same source event are linked observations.
- Every generated variant inherits its source patient's partition.
- A constructed pair involving records from multiple patients places every
  contributing patient in the same partition; splitting must operate on
  connected components of the pair-construction graph or an equivalent
  leakage-safe rule.
- Label extraction and ontology mapping must not learn from final-test data.
- Thresholds, normalizers, and calibration parameters must not be selected on
  final evaluation cases.
- Near duplicates and templated reports require explicit audits.

The native MIMIC source unit is a study-level image set because one report may
describe multiple views. A single-frontal-image restriction is permitted only
after independent visibility review confirms that the singleton finding is
decidable from that exact image; otherwise it can manufacture apparent
conflict from evidence visible only on another view.

## Label-Independence Rule

MIMIC-CXR-JPG CheXpert/NegBio fields and the v2.1 radiologist test annotations
describe report mentions. They may assist retrieval and stratification after
access is approved, but they cannot independently establish image truth, image
ambiguity, or image--text compatibility. Native pairing likewise does not
prove that a report is complete or correct.

The construct set requires blinded image-only and text-only interpretation
distributions followed by separately recorded cross-modal adjudication.
Candidate-model entropy, confidence, or embedding spread cannot define the
ambiguity variable against which that same candidate is evaluated.

## Controlled Clinical Conflict

Every synthetic or edited contradiction requires:

- the atomic proposition changed and its original/final truth status;
- provenance: natural, rule-generated, model-generated, or manually edited;
- preservation of plausible language and image quality;
- explicit separation from ambiguity, missingness, and corruption;
- expert review whenever clinical validity is claimed;
- an artifact analysis showing that condition labels are not trivially
  recoverable from surface form.

Synthetic conflict is a measurement instrument, not an estimate of real-world
conflict prevalence.

## Target-Population Sampling

The dataset record must distinguish:

- **construct sample:** deliberately balanced intervention cells for
  identification and stress testing;
- **target sample:** a natural, patient-separated cohort for proper scores,
  calibration, prevalence-sensitive metrics, and review-budget utility;
- **stress sample:** ReXErr, explicitly treated as MIMIC-derived and inheriting
  the MIMIC patient/source split, or a separately governed independent source;
  used only for the compatible frozen unit and declared stress claim.

If the target sample is enriched, case--control sampled, or otherwise differs
from the declared target population, sampling probabilities and any
prevalence-weighting or recalibration method must be frozen before evaluation.
Unweighted synthetic-cell results cannot be presented as real-world calibrated
risk or decision utility.

## Clinician Annotation Gate

Before requesting expert work, document:

- reviewer qualifications and role;
- sampling plan and blinded presentation;
- ambiguity/conflict rubric with examples and edge cases;
- independent review, adjudication, and disagreement model;
- target reliability and stopping/retraining rule;
- time burden, compensation, ethics, data handling, and withdrawal process;
- which labels are construct validation and which are outcome evaluation.

Clinical-expert availability reported in planning does not replace this gate.

## Repository Boundary

Permitted artifacts may include code, configs, hashes, aggregate outputs, and
non-identifying derived metadata explicitly allowed by the data-use agreement.
Raw medical records, images, reports, identifiers, credentials, private
correspondence, and prohibited derivations never enter Git.

Restricted MIMIC content must not be pasted into Codex/ChatGPT, sent through an
unapproved hosted API, exposed in CI, or placed on an unapproved online service.
The default later execution architecture is approved local or institutional
processing. Any exception requires written governance confirmation of zero
retention, no training, no human review, access control, and every applicable
DUA term.

PhysioNet guidance treats MIMIC-derived datasets and models as sensitive.
Pending written permission, counterfactual reports, row-level annotations,
embeddings, checkpoints, and weights remain restricted and are not public
repository artifacts. Only explicitly permitted aggregate results may cross
the secure boundary after disclosure review.

The `data/` directory ignores all content except its governance README. Local
paths must be configured outside version control.

## Checkpoint-Exposure Rule

Before any model is selected, record its release, training-corpus and split
provenance, known MIMIC/PadChest/general-benchmark exposure, and uncertainty of
that evidence. Known exposure to final patients or benchmark blocks excludes a
checkpoint from confirmatory evaluation on those units. Unknown overlap is
reported as unknown and supports sensitivity evidence only, not a strict
held-out claim. A checkpoint fine-tuned on a public benchmark cannot provide
independent evaluation on that benchmark.

## Stop Conditions

Stop before data work if access or terms are unclear, patient separation cannot
be enforced, the atomic task is unsupported by the data, labels cannot be
defended, or intervention validity cannot be reviewed. A non-clinical pilot is
allowed only through a new bounded brief that states its limited transfer role.
