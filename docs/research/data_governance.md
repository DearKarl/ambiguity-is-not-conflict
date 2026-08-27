# Data and Clinical Governance

**Status:** Candidate data route; no dataset access approved by this document

## Minimal Viable Data Route

The current candidate route is:

1. MIMIC-CXR/JPG as the patient-level source of paired chest radiographs and
   reports;
2. a patient-separated, atomic-finding subset with matched, image-ambiguous,
   text-ambiguous, conflicting, missing, and corrupted controls;
3. clinical review of the intervention construct and a confirmatory subset;
4. ReXErr only as an external error-oriented stress test if its units and
   labels match the frozen task.

A second, separately sampled **target-distribution cohort** is required for
calibration and selective-review claims. Its natural prevalence and inclusion
rules must not be replaced by the balanced intervention-cell frequencies.

Candidate status does not imply credentialing, access, licence compatibility,
scientific suitability, or permission to redistribute derived artifacts.

## Dataset Decision Record

Before any download or access, freeze:

- canonical name, version, release date, and access date;
- licence, data-use agreement, credentialing, ethics, and storage boundary;
- task, prediction unit, ontology, inclusion/exclusion criteria, and cohort
  flow;
- patient-level split, repeated-study links, duplicates, and leakage controls;
- label extraction, uncertainty, provenance, and adjudication;
- model pretraining overlap and benchmark contamination where assessable;
- subgroup definitions and minimum reporting sizes;
- permitted derived metadata, retention, deletion, and sharing rules.

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
- **external stress sample:** a separately sourced resource such as ReXErr,
  used only for the compatible frozen unit and claim.

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

The `data/` directory ignores all content except its governance README. Local
paths must be configured outside version control.

## Stop Conditions

Stop before data work if access or terms are unclear, patient separation cannot
be enforced, the atomic task is unsupported by the data, labels cannot be
defended, or intervention validity cannot be reviewed. A non-clinical pilot is
allowed only through a new bounded brief that states its limited transfer role.
