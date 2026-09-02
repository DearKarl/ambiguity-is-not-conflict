# Dataset Feasibility and Governance Audit

**Status:** Primary MIMIC route internally selected for readiness; external
access/governance evidence and Gate-0 closure remain blocked; no data accessed
**Audit date:** 2026-08-29
**Evidence class:** Official dataset pages, data-use terms, primary dataset
papers, and public repository metadata

## Executive Finding

MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 form one coupled candidate source for
the first controlled study: the former supplies native DICOM images and
reports; the latter supplies standardized model-facing images, metadata,
report-derived labels, and a reference split. They are **not execution-ready**
and must not be counted as independent datasets. Their readily available
structured labels and radiologist test annotations are derived from or
annotate the reports, not independent image truth. They therefore cannot
define image ambiguity, establish the truth of an image-side proposition, or
independently validate image--report conflict. Doing so would make the target
circular.

VisMin is the lowest-governance-friction breadth candidate for a small
controlled general-domain stress test, but it lacks ambiguity and
information-loss controls and cannot validate the complete construct without a
separate frozen supplemental protocol. PadChest-GR is the strongest
second-medical reserve because it supplies atomic bilingual finding sentences
and radiologist localization from an independent source; formal access and
derivative-work permissions are unresolved. ReXErr is useful only as a
synthetic report-error stress resource and cannot count as independent breadth
because it is derived from MIMIC-CXR.

No dataset files, record-level data, images, reports, models, credentials, or
restricted content were accessed in this audit.

## 2026-09-02 Official-Source Recheck

The public official pages still classify both exact MIMIC resources as
credentialed access and require an individual credentialed user, current CITI
`Data or Specimens Only Research` training, and project DUA acceptance. The
current PhysioNet Credentialed Health Data License/DUA 1.5.0 prohibits access
sharing, requires physical/electronic security and current human-subjects/HIPAA
training, and requires associated code to be contributed to an open research
repository when results are openly disseminated. PhysioNet's online-service
guidance requires verified zero retention, no training, and no human review;
unclear services must not be used. Its derived-resource guidance treats
MIMIC-derived datasets and models as sensitive. This public recheck verifies
terms only; it does not verify any person's credentials, training, DUA status,
ethics determination, secure environment, or access grant.

## Official-Source Feasibility Matrix

| Resource | Verified facts | Candidate role | Fatal or unresolved issues | Decision |
| --- | --- | --- | --- | --- |
| [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/) | Published 2024-07-23; DOI `10.13026/4jqj-jw95`; 377,110 DICOM images, 227,835 studies, and 65,379 patients, with one report per study and one or more images | Coupled source of reports, native images, and patient--study--image linkage | Credentialing, training, licence/DUA, secure storage, approved processing boundary, exact cohort, and permitted derivations remain unfrozen; native pairing is not proof of semantic compatibility | Leading primary candidate; not approved |
| [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) | Published 2024-03-12; DOI `10.13026/jsn5-t979`; 377,110 JPG images linked to 227,827 reports; includes `subject_id`, `study_id`, reference split, metadata, CheXpert/NegBio report-derived labels, and a report-annotated test file | Primary feasibility source for paired patient/study/image/report structure | Restricted access; report-derived labels are circular for image truth; the single-radiologist test labels annotate report mentions rather than blinded image evidence; JPG conversion is itself an information-loss choice; patient and source-graph split must be independently verified | Leading primary candidate; not approved |
| [ReXErr-v1 v1.0.0](https://physionet.org/content/rexerr-v1/1.0.0/) | Published 2025-03-19; DOI `10.13026/9dns-vd94`; open under ODC Attribution 1.0; GPT-4o-generated report- and sentence-level errors across 12 categories with clinician input; explicitly derived from MIMIC-CXR | MIMIC-derived synthetic report-error and artifact stress test after unit mapping | Synthetic errors are not natural conflict prevalence; multiple simultaneous report errors do not match an atomic single-change unit; shared MIMIC ancestry requires inherited patient/source splits, prevents independence, and creates leakage risks | Stress resource only; not breadth replication |
| [VisMin paper](https://papers.nips.cc/paper_files/paper/2024/hash/c3070c3388552a08a3326f0d28dc2af9-Abstract-Conference.html) / [author data card](https://huggingface.co/datasets/mair-lab/vismin-bench) | NeurIPS 2024 minimal-change benchmark; 2,084 public evaluation blocks in the current author release, each coupling two minimally different images and two captions; repository card declares CC BY 4.0 | Lowest-friction controlled general-domain compatibility stress test | No semantic dataset version was found; snapshot and inherited COCO/Flickr asset terms require audit; no ambiguity/missingness/corruption axes; synthetic artifacts and public-benchmark exposure threaten interpretation | Preferred breadth stress candidate; not full replication unless controls are added |
| [PadChest-GR](https://bimcv.cipf.es/bimcv-projects/padchest-gr/) | 4,555 frontal studies, 7,037 positive and 3,422 negative bilingual atomic finding sentences, with radiologist localization for positive findings; formal request required | Strongest independent second-medical atomic-construct candidate | Enriched curated sample, no ambiguity labels, GPT-4 extraction/translation provenance, formal access, and unclear permission for counterfactual or derived intervention artifacts | Preferred medical reserve; governance-blocked |
| [CheXpert Plus official page](https://aimi.stanford.edu/datasets/chexpert-plus) / [primary paper](https://arxiv.org/abs/2405.19538) | DOI `10.71718/6nvz-pm34`; the official page and paper Table 1 report 223,462 image--report pairs, while the paper's composition text reports 223,228; 187,711 studies and 64,725 patients; DICOM images, sectioned reports, and 14 pathology annotations | Large independent institutional target or replication candidate | Pair count/version discrepancy, moving-host snapshot, Redivis terms, split, label provenance, image-grounded truth, duplicates, pretraining overlap, and permitted derivations require audit; an immutable release must be frozen and scale does not solve circularity | Additional reserve candidate |
| [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/) | 160,868 labeled images, 109,931 studies, and 69,882 patients; Spanish reports; formal research-use terms prohibit redistribution without permission | Independent institutional/language-shift cohort | About 27% of reports were physician-annotated and the rest automatically labeled; processed text, storage/access burden, ontology mapping, and derivative-work restrictions weaken feasibility | Lower-priority reserve |
| [Open-i Indiana University chest X-rays](https://openi-vip.nlm.nih.gov/faq) | NLM provides links to the Indiana chest X-rays and reports and asks users not to share the dataset outside their organization | Small external medical stress route | Image-specific licence may vary; NLM states it cannot grant reuse permissions; patient identifiers/split guarantees, ontology, and report pairing require audit | Not preferred until rights and leakage are resolved |

## Primary Route: Required Decisions Before Access

### Access and environment

**Facts.** MIMIC-CXR-JPG requires a credentialed user, approved human-subjects
training, and a signed data-use agreement. The
[PhysioNet DUA](https://physionet.org/content/mimic-cxr-jpg/view-dua/2.1.0/)
prohibits sharing access and requires physical and electronic security. The
[PhysioNet online-service notice](https://physionet.org/news/post/llm-responsible-use/)
states that credentialed/restricted MIMIC data and derivatives must not be sent
through third-party APIs or online platforms unless every DUA requirement,
including zero retention and absence of unauthorized review or training, can
be verified; when practices are unclear, the service must not be used.

**Proposed boundary.** Raw MIMIC images, reports, identifiers, or record-level
derivatives must never be pasted into a Codex/ChatGPT task, unapproved remote
API, GitHub, CI log, or unapproved hosted service. The default later execution
boundary is the researcher's approved local or institutional environment. Any
exception requires written governance confirmation of every applicable DUA
condition, including zero retention and no unauthorized review or training.
Only DUA-permitted, non-identifying aggregate artifacts may cross the approved
boundary after an explicit disclosure review.

PhysioNet's
[derived-resource guidance](https://physionet.org/news/post/mimic-derived-datasets-models/)
says MIMIC-derived datasets and models should themselves be treated as
sensitive and, if shared, routed through PhysioNet under the source agreement.
Pending a written determination, this project must treat counterfactual text,
row-level annotations, embeddings, checkpoints, and weights as restricted—not
as automatically publishable derivatives. The DUA's open-code obligation for
openly disseminated results also requires reconciling the repository's current
all-rights-reserved notice before release.

### Prediction and leakage units

- **Person/leakage unit:** `subject_id`; no patient crosses development,
  calibration, target-test, or external-test partitions.
- **Faithful clinical source unit:** `study_id`, containing one report and one
  or more images. The default pairing unit is therefore the study-level image
  set.
- **Proposed kill-stage restriction:** one exact frontal image only if
  independent input-coverage review confirms that the prescribed field is
  adequately represented and determinate source cases can receive an image-
  only state. Attaching a multi-view study report to one image without this
  check can manufacture apparent conflict from evidence visible only on
  another view; natural ambiguous cases need not have a unique state.
- **Analysis unit:** one atomic finding proposition paired with one selected
  image and one controlled text proposition.
- All rewrites, counterfactual propositions, crops, corruptions, paraphrases,
  and multi-source pairs inherit the connected-component partition of every
  source patient.

The official split is a useful reference, not proof that all new constructed
pairs, near duplicates, report templates, and temporally repeated studies are
leakage-safe.

### Label and construct validity

CheXpert and NegBio labels encode what the report says. The MIMIC-CXR-JPG
documentation likewise describes the test annotations as annotations of the
radiology reports. These fields may support cohort search after access is
approved, but they cannot be the only evidence for any of the following:

- what the selected image independently shows;
- whether image evidence is clear or ambiguous;
- whether an atomic report proposition is compatible with the image;
- whether a text expression is genuinely ambiguous rather than hedged,
  incomplete, or out of ontology.

The construct sample therefore requires separate blinded image-only and
text-only review, followed by cross-modal adjudication under a frozen rubric.
Reviewers who see both modalities must not silently overwrite the independent
ambiguity labels. Reliability thresholds, disagreement handling, workload,
compensation, and ethics remain open Gate-0 items.

## Construct Sample Versus Target Sample

The controlled construct sample and natural target sample must remain
different datasets even when drawn from the same source release:

| Sample | Sampling | Allowed claim |
| --- | --- | --- |
| Construct sample | Deliberately matched positive/negative source blocks and controlled propositions; valid paired `M_v`/`M_t` controls; separately matched natural-ambiguity veto pools | Determinate-conflict specificity under the intervention distribution; natural ambiguity may falsify but cannot identify causal separation |
| Target sample | Natural patient-separated cohort with frozen inclusion and prevalence | Proper-score calibration and retrospective equal-budget selection in that declared population |
| Stress sample | ReXErr, inheriting the MIMIC patient/source split, or a separately governed independent source mapped to the same atomic unit | Robustness to the specified synthetic or institutional shift only; ReXErr is not independent breadth |

Balanced intervention cells cannot estimate clinical prevalence or calibrated
real-world risk. A synthetic conflict rate is a design parameter, not a
population quantity.

## Breadth Decision

**Inference.** VisMin is the least costly route to a controlled general-domain
compatibility stress test, but it is not a replication of conditional conflict
unless ambiguity and information-loss controls are added. PadChest-GR is the
best current second-medical atomic candidate; CheXpert Plus offers larger-scale
institutional replication but a less direct construct instrument. ReXErr is
never independent breadth. CLASH or CrossCheck-Bench may be relevant
alternatives, but their task units, licences, artifact process, and training
overlap require a separate audit.

**Proposed decision.** Freeze the breadth identity, immutable snapshot, rights,
construct-portability rule, and stop condition at Gate 0 as required by the
canonical research contract, but defer every breadth access or execution action
until the primary construct instrument passes the development gate. This
reconciles prospective claim planning with the need to avoid premature
annotation and governance burden.

## Pretraining-Contamination Rule

Actual source exposure is unknown until the backbone checkpoints are frozen.
Dataset age and public availability create plausible exposure; newly generated
variants reduce exact-pair memorization but do not erase exposure to their
source image or report.

The confirmatory rule should be frozen as follows:

- a checkpoint with known exposure to final-evaluation patients or benchmark
  blocks is ineligible for confirmatory evidence on those units;
- primary evidence requires documented training-corpus and split provenance;
- unknown overlap is reported as unknown and supports sensitivity evidence
  only, not a strict “held-out” claim;
- fine-tuning on a public benchmark disqualifies that checkpoint from an
  independent evaluation on the same benchmark;
- hashes, release dates, access dates, model cards, and contamination queries
  must be retained for every selected checkpoint.

## Gate-0 Blockers and Post-Freeze Feasibility Stop

No data access request, download, or record inspection is authorized until all
of the following are approved:

1. exact MIMIC resource (`DICOM`, `JPG`, or a justified combination), version,
   authorized account holder, storage location, and processing boundary;
2. a single atomic finding, image/report inclusion schema, exact restricted
   tabular screening
   feasibility query, minimum viable counts, and pre-specified stop rule; no
   observed count is required or claimed before access;
3. blinded image-only and text-only annotation rubrics, reliability threshold,
   adjudication process, clinician budget, and ethics determination;
4. source-graph split construction and an approved processing architecture,
   defaulting to no third-party service unless a written exception satisfies
   every DUA and governance condition;
5. permitted derived artifacts, retention/deletion plan, and disclosure check;
6. construct-sample and target-sample separation;
7. a stop rule if independent image truth, reliable ambiguity labels, or
   sufficient compatible/conflicting source blocks cannot be obtained.

After Gate 0 freezes, a separate bounded brief may authorize the frozen
restricted tabular screening query in the approved environment. It must record
the restricted linkage identifiers and report-derived clinical screening
variables it reads, and
actual access date, immutable snapshot, observed counts, exclusions, and cohort
flow. Failure of the pre-specified count or leakage thresholds stops execution
and reopens Gate 0 before any record inspection, annotation, model use, or
clinical intervention generation.

Kill the medical route before model work if independent image-grounded truth
cannot be obtained without using the paired report as its own label, if DUA
requirements cannot be met, or if the atomic intervention cannot be reviewed
reliably. Such a failure narrows or redirects the validation domain; it does
not justify manufacturing a clinical claim.
