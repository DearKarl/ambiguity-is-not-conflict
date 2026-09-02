# Dataset Decision Record

- **Identifier:** `DDR-2026-09-02-001`
- **Owner:** Commander as consolidated internal project owner
- **Status:** Stage-A readiness record; internal preparation authorized,
  restricted access and Gate-0 closure blocked
- **Decision date:** 2026-09-02
- **Evidence class:** Repository protocol, Commander attestation, and public
  official-source verification; no restricted-data evidence

## Decision Summary

The coupled MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 route remains the sole
primary medical data candidate for the first controlled study. This record
prospectively fixes the non-executable Stage-B restricted tabular screening
query candidate for review and
records the objective evidence required before it may run. It does not claim
that access, training, DUA acceptance, institutional ethics, secure storage,
reader eligibility, or capacity exists.

The Commander's consolidated internal authority resolves the previously open
formal `G0-SCOPE A` and Method-A sole-route/B-inactive co-approval boundaries
and the named Method-A scientific interfaces. It does not silently select the
remaining independent Gate-0 A/B/C rows or convert missing external facts into
approvals. Gate 0 therefore remains open, and no download, query, image/report
inspection, annotation, model execution, or experiment is authorized.

## Fact, Inference, Assumption, and Decision Ledger

### Facts

- [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/)
  was published 2024-07-23 with DOI `10.13026/4jqj-jw95`.
- [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
  was published 2024-03-12 with DOI `10.13026/jsn5-t979` and is derived from
  MIMIC-CXR.
- Both resources use PhysioNet Credentialed Health Data License/DUA 1.5.0 and
  require an individually credentialed user, the CITI `Data or Specimens Only
  Research` training route, and project DUA acceptance.
- The DUA prohibits sharing access, requires reasonable physical/electronic
  security, and requires up-to-date human-subjects/HIPAA training. Openly
  disseminated results require associated code to be contributed to an open
  research repository.
- PhysioNet's 2025 online-service guidance prohibits third-party disclosure and
  requires zero retention, no training, and no human review to be verified
  before any cloud/API use; unclear services must not be used.
- PhysioNet's derived-resource guidance treats MIMIC-derived datasets and
  models as sensitive and directs any sharing through PhysioNet under the
  source agreement.
- No credential, training report, DUA acceptance, access grant, secure path,
  restricted file, record, report, image, or derived row was inspected in
  producing this record.

### Inferences

- The JPG metadata route is the smallest plausible first feasibility action
  because it can test patient/study/image linkage, strict-single-frontal yield,
  view/geometry, official split membership, and report-screen strata without
  reading images or reports.
- Individual project authority cannot substitute for the resource provider's
  access controls or for institutional security and ethics facts.
- The safest architecture is deterministic execution inside an approved local
  or institutional environment, with only disclosure-cleared aggregates
  leaving that boundary.

### Assumptions requiring evidence

- An individually credentialed access holder has current accepted training and
  approved access to both exact resource versions.
- The researcher's institution permits this project and the planned reader/
  annotation work under a documented ethics determination.
- A secure, encrypted, access-controlled processing path outside the Git
  repository exists with sufficient storage, backup, incident, retention, and
  deletion controls.
- Qualified readers and the required mutually exclusive panel design are
  available under the approved access basis.
- The strict-single-frontal pleural-effusion route meets the frozen aggregate
  screening floors; this cannot be known before an authorized Stage-B query.

### Decisions

- Preserve MIMIC-CXR/JPG v2.1.0 as one coupled candidate source, not two
  independent datasets.
- Preserve report-derived CheXpert/NegBio values only as screening variables;
  they never define exact-image truth, image ambiguity, or conflict.
- Preserve patient-level leakage control, one keyed eligible source study per
  patient, and the exact HMAC partition proposal.
- Preserve a no-hosted-service default for restricted or record-level content.
- Prospectively fix the Stage-B metadata schema below as a non-executable
  candidate for later authorization, but do not
  execute it until every readiness requirement is evidenced and a fresh linked
  Execution Contract and Task Brief approve the exact environment and command.

## Resource and Access Identity

| Field | Frozen record |
| --- | --- |
| Dataset | Coupled MIMIC-CXR v2.1.0 and MIMIC-CXR-JPG v2.1.0 |
| DOI | `10.13026/4jqj-jw95`; `10.13026/jsn5-t979` |
| Planned access window | Only after Gate-0 closure and a fresh Stage-B authorization; no calendar date inferred |
| Actual access date | Not applicable before authorized access |
| Licence/DUA | PhysioNet Credentialed Health Data License and DUA 1.5.0 |
| Required training | Current accepted CITI `Data or Specimens Only Research` route |
| Credential holder | Unverified; must be individually authorized and recorded without committing credentials or private identifiers |
| Access-control list | Unverified; every researcher/reader with source or derived-record access must have an approved basis and named ACL entry |
| Ethics determination | Unverified; source-dataset IRB history does not establish this project's institutional determination |
| Secure processing path | Unverified; must be outside Git, encrypted, access-controlled, and approved for the exact workflow |
| Network/API boundary | Restricted and record-level content remains local/institutional; no Codex/ChatGPT, CI, hosted API, or online service |

## Task and Unit Boundary

The current data-readiness candidate is pleural-effusion presence/absence on
one exact strict-single-frontal chest radiograph with an atomic auxiliary text
assertion. The candidate prediction unit is:

```text
(patient, study, exact single frontal image, singleton finding,
 atomic text assertion, intervention variant, frozen model)
```

`subject_id` is the leakage unit. The native clinical source is the complete
study because a report may describe multiple views. The single-image route
remains conditional on independent input-coverage and image-only-state review;
this record does not approve a clinical item or establish its assessability.

## Frozen Stage-B Restricted Tabular Screening Boundary

A later brief may read only these files and fields inside the approved secure
environment:

| File | Permitted fields |
| --- | --- |
| `mimic-cxr-2.0.0-split.csv.gz` | `dicom_id`, `study_id`, `subject_id`, `split` |
| `mimic-cxr-2.0.0-metadata.csv.gz` | `dicom_id`, `ViewPosition`, `Rows`, `Columns` |
| `mimic-cxr-2.0.0-chexpert.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |
| `mimic-cxr-2.0.0-negbio.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |

Every listed file and field is restricted. The identifiers are restricted
linkage variables. The CheXpert and NegBio `Pleural Effusion` values are
restricted, report-derived clinical screening variables; they are not image
truth, model targets, or public metadata. Earlier repository shorthand
"metadata-only feasibility query" refers to this same restricted tabular
screening boundary and must not be read as a public or non-clinical query.

Dates/times, demographics, reports, images, DICOM pixels, other findings, the
manual test-label file, and any record-level export are forbidden in Stage B.
The query code, exact revision/hash, synthetic schema-fixture tests, secure
path, and independent reviewer remain to be created and approved under the
later Stage-B contract.

## Cohort, Split, and Stop Rules

- Assert unique `dicom_id`, one patient and official split per study, and
  cardinality-preserving joins before aggregation.
- Define `strict_single_frontal` and `reserve_multiview` exactly as in the
  [dataset decision candidate](dataset_decision_candidate.md).
- Apply eligibility before outcome-blind keyed study ranking; label values may
  not affect eligibility, partition, or rank.
- Preserve official validation and test roles. Within official train, use the
  frozen `AINC/v1/partition` and `AINC/v1/study-rank` HMAC algorithms only
  after secure secret-key custody is approved. The key never leaves the secure
  store; only its non-secret fingerprint may leave.
- Keep all siblings and connected source-patient components in one partition.
- Stop on any mapping/split invariant failure, disclosure failure, insufficient
  screening floor, inability to obtain independent image truth, or need to
  replace the unit or use report labels as image truth.

The planned aggregate floors remain protocol assumptions, not observed facts:
260 balanced Month-3 screening patients, 380 for two-control confirmation, 470
for four-control confirmation, 250 calibration candidates, 380 natural-target
candidates with at least 50 per report-screen polarity, and 100 natural-
ambiguity recruitment candidates. Exact definitions and polarity/attrition
consequences remain those in the dataset decision candidate.

## Labels, Readers, and Intervention Boundary

- Independent image-only and text-only measurement precedes cross-modal
  adjudication; report labels and native pairing cannot establish truth.
- Ambiguous, missing, or semantically indeterminate modalities retain undefined
  conflict rather than a negative label.
- `MV-1`, `MT-1`, reader qualification, reliability simulation, roster,
  compensation, timing, ethics, and intervention validation remain separate
  Gate-0 decisions or feasibility gates. No reader may receive restricted
  content through another person's account.
- Synthetic conflict is a controlled measurement instrument, not natural
  prevalence or clinical-benefit evidence.

## Permitted and Prohibited Artifacts

Only disclosure-reviewed aggregate counts, resource/checksum identities,
query/schema-test hashes, and non-sensitive code/configuration may eventually
leave the secure environment. Cells below 20 and complementary/marginal values
that could reconstruct them must be suppressed under a release ledger.

Raw images, DICOM, reports, identifiers, paths, dates, row-level labels,
partition manifests, HMAC keys, annotations, counterfactual text, embeddings,
checkpoints, model weights, screenshots, logs containing records, and private
access evidence are prohibited from Git, GitHub, CI, Codex/ChatGPT, and any
unapproved service. MIMIC-derived datasets and models remain sensitive pending
an explicit written sharing determination.

## Readiness Evidence Required Before Stage B

1. Evidence that the named individual access holder is credentialed and has
   current accepted CITI training and approved access/DUA status for both
   resources; private documents remain outside Git.
2. A documented institutional ethics determination for the restricted tabular
   screening query and
   the prospective annotation/reader workflow.
3. An approved secure absolute processing path outside the repository, named
   ACL roles, encryption, network isolation, backup, incident, retention, and
   deletion rules.
4. Confirmation that the exact local/institutional execution path does not send
   restricted or record-level content to Codex, ChatGPT, CI, or another online
   service.
5. Storage and CPU capacity for the bounded restricted tabular screening
   query, distinct from the
   unresolved 613-GB simulation-output route.
6. Explicit selection/freeze of the remaining task, data, intervention,
   reader, statistical, resource, and governance rows needed for Gate-0
   closure.
7. A fresh Stage-B Execution Contract and Task Brief naming the exact command,
   fields, path, expected aggregate schema, disclosure reviewer, and stop
   behavior.

## Reopening and Permitted Claim

Reopen this record if official terms, resource versions, the task/unit,
partition logic, permitted derivatives, or secure environment changes. Its
current permitted claim is only that the repository contains an exact,
reviewable restricted-data readiness packet and proposed restricted tabular
screening query
boundary. It does not establish access, sufficient cohort counts, reader
availability, intervention validity, Gate-0 closure, experiment authority,
clinical benefit, NeurIPS eligibility, acceptance, or publication.
