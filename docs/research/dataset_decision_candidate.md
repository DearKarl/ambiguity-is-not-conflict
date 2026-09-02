# Dataset Decision Candidate

**Status:** Two-stage route internally selected for readiness under DR-0018;
external evidence, remaining Gate-0 choices, and a later Stage-B authorization
are required; no access request, agreement, download, or record query is
authorized

**Date:** 2026-08-29
**Evidence class:** Official-source facts plus protocol assumptions

## Proposed Resource Identity

Treat the following as one coupled restricted source, not two replications:

- [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
  for standardized JPG images, image metadata, report-derived screening labels,
  and the reference split;
- [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/)
  for the associated study report only after a later record-level authorization.

**Verified facts.** The official JPG page reports 377,110 JPG images and
structured labels derived from 227,827 reports. The split schema contains
`dicom_id`, `study_id`, `subject_id`, and `split`; image metadata include view
and geometry; CheXpert/NegBio labels take positive, negative, uncertain, or
missing values. The test annotations and structured fields annotate report
mentions, not independent exact-image truth. Access is credentialed and
governed by PhysioNet terms.

**Inference.** JPG plus report linkage is the lowest-complexity route to the
current exact-image atomic task. Original DICOM pixels remain outside the first
candidate because downloading a full native archive increases storage and
does not remove the need to validate the exact rendered model input. This
choice must be reopened if qualified readers cannot judge the frozen JPG input
reliably.

**Assumption.** Pleural-effusion presence/absence and a strict single-frontal
study provide enough clear positive and negative patient blocks. This has not
been tested and is not a dataset fact.

## Stage A — Freeze Before Any Access

A signed record must name:

1. both resource versions and DOIs;
2. approved access basis for every person who can view restricted source or
   derived content, including individual credentials, current training and DUA
   status where applicable, a named access-control list, reader-UI/export
   controls, approved local/institutional storage, and planned access window;
3. no-hosted-API default, retention/deletion dates, backups, incident route,
   and permitted aggregate/derived outputs;
4. exact query code/version/hash, tests on synthetic schema-only fixtures, and
   independent reviewer;
5. keyed patient-partition algorithm, secure key custody, and a non-secret
   fingerprint/commitment of the 32-byte secret root key;
6. fields, derived flags, aggregate tables, small-cell suppression, minimum
   counts, and stop rules below;
7. the separate approvals needed before reports, images, clinical labels,
   counterfactual text, annotations, embeddings, or checkpoints are touched.

Gate-0 documentation does not create credentials, accept terms, claim access,
or authorize an application.

## Stage B — Restricted Tabular Screening Query

Only a later bounded brief in the approved environment may read:

| Official file | Permitted fields |
| --- | --- |
| `mimic-cxr-2.0.0-split.csv.gz` | `dicom_id`, `study_id`, `subject_id`, `split` |
| `mimic-cxr-2.0.0-metadata.csv.gz` | `dicom_id`, `ViewPosition`, `Rows`, `Columns` |
| `mimic-cxr-2.0.0-chexpert.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |
| `mimic-cxr-2.0.0-negbio.csv.gz` | `subject_id`, `study_id`, `Pleural Effusion` |

Do not read dates/times, demographics, reports, images, DICOM pixels, other
findings, or the v2.1 manual test-label file in Stage B.

### Frozen derived flags

Execute joins and derivations in this fixed order:

1. Assert one row per `dicom_id` in the split and metadata tables. Left-join
   metadata to the split 1:1 on `dicom_id`, retaining split rows with missing
   metadata and asserting the joined row count equals the split row count.
2. Within each `(subject_id, study_id)`, define
   `n_images = count_distinct(dicom_id)` from the split rows and
   `n_frontal = count_distinct(dicom_id where ViewPosition in {AP, PA})` after
   the left join. Missing view never counts as frontal.
3. Derive strict/reserve flags below and apply the keyed patient partition and
   outcome-blind one-study rank. The sole strict image must have nonmissing
   positive `Rows` and `Columns`.
4. Only after one strict eligible study per patient is selected, assert one row
   per `(subject_id, study_id)` in each label table and left-join CheXpert and
   NegBio 1:1 on that key. Assert cardinality and row count after each join;
   missing label rows remain missing rather than dropping the study.
5. Apply the mutually exclusive report-screen strata and aggregate. No label
   value may affect eligibility, partition, or study rank.

```text
frontal := ViewPosition in {AP, PA}
strict_single_frontal := n_images == 1 and n_frontal == 1
                         and sole Rows > 0 and sole Columns > 0
reserve_multiview := n_frontal >= 1 and n_images > 1

positive_agree := both labels are nonmissing and equal 1
negative_agree := both labels are nonmissing and equal 0
uncertain := either label equals -1
disagree := neither label is -1 and both are nonmissing and unequal
one_sided_mention := exactly one label is nonmissing and it is 0 or 1
unmentioned := both labels are missing
```

Report-screen strata are retrieval and yield-planning aids only. They never
define image truth, image ambiguity, or cross-modal conflict. The ordered rules
above are mutually exclusive and exhaustive. `one_sided_mention` is reported
separately and excluded from clear-polarity floors and natural-ambiguity
recruitment; only `uncertain` plus `disagree` feed the latter candidate pool.

### Required integrity invariants

- `dicom_id` is unique;
- each `study_id` maps to exactly one `subject_id` and official split;
- no `subject_id` crosses official splits or project partitions;
- missing/unknown view and invalid geometry counts are reported;
- every generated or edited sibling inherits its source patient partition;
- constructed multi-source pairs, if later approved, are split by connected
  source-patient components;
- exactly one eligible source study per patient is selected by the frozen
  outcome-blind keyed rank below for every primary Month-3 and confirmation
  analysis.

Any invariant failure stops the query and triggers review before correction or
further access.

## Candidate Patient Partitions

Preserve official validation and test membership. Within official `train`, use
this proposed HMAC-SHA256 v1 procedure, tested first on public synthetic IDs:

```text
root_key := 32 random bytes stored only in the approved secret store
partition_key := HMAC-SHA256(root_key, ASCII("AINC/v1/partition"))
study_key := HMAC-SHA256(root_key, ASCII("AINC/v1/study-rank"))
subject_bytes := ASCII("subject:" + base10_integer(subject_id))
bucket := big_endian_integer(HMAC-SHA256(partition_key, subject_bytes)) mod 100
```

`base10_integer` has no sign, whitespace, decimal point, or leading zeros. The
full 32-byte digest is converted as an unsigned big-endian integer. Record the
algorithm identifier and first 16 hex characters of `SHA256(root_key)` as the
non-secret key fingerprint; never export the key.

| Source partition | Project role |
| --- | --- |
| Official train, HMAC 0--69 | 70% method/rubric development pool |
| Official train, HMAC 70--84 | 15% one-time Month-3 kill/advance holdout for the already named primary candidate; still developmental evidence |
| Official train, HMAC 85--99 | 15% later construct-confirmation candidate |
| Official validate | calibration candidate only |
| Official test | natural target candidate only |

Fit, orient, normalize, and tune only on bucket 0--69. Name one primary
uncertainty-aware method and its matched deterministic comparator before
bucket 70--84 is opened once for the frozen Month-3 advance/kill decision; no
method, normalizer, or threshold is selected or refit there. Bucket 85--99
remains untouched for later construct confirmation.

After strict metadata eligibility is determined without labels/outcomes,
select one study per patient by minimizing the unsigned full digest
`HMAC-SHA256(study_key, subject_bytes || ASCII("|study:") ||
base10_integer(study_id))`; ties use the smaller numeric `study_id`. Apply
eligibility before ranking, never search the ranked list for a favourable
label, and record only aggregate selection counts outside the secure boundary.

Only the key digest, algorithm version, and aggregate counts may leave the
secure environment. This split is a candidate, not proof of checkpoint
non-exposure. A pretrained checkpoint known or suspected to contain a final
patient remains governed by the separate exposure rule.

## Permitted Stage-B Outputs

- resource versions and checksums;
- query and schema-fixture test hashes;
- aggregate counts by partition, `strict_single_frontal`/`reserve_multiview`,
  and report-screen stratum;
- duplicate, invariant, missing-view, and invalid-geometry counts;
- a disclosure-review decision.

Before access, freeze the exact aggregate table schema as mutually exclusive,
non-overlapping cells wherever possible. Suppress every cell below 20 and any
complementary cell, row/column total, marginal, or cross-release value from
which a suppressed cell could be recovered by subtraction. Maintain a release
ledger and do not publish overlapping refinements across successive queries.
The disclosure owner must approve the exact rendered aggregate table, including
all totals and derived percentages, before export. IDs, paths, dates, row-level
labels, HMAC key, split manifest, text, images, screenshots, embeddings, and
record-level exports stay inside the approved environment and never enter Git,
Codex/ChatGPT, CI, or an unapproved service.

## Candidate Feasibility Floors and Stops

These counts are power-linked planning assumptions, not observed yields:

| Pool | Minimum aggregate screen | Intended consequence |
| --- | ---: | --- |
| Month-3 strict pool | 130 `positive_agree` plus 130 `negative_agree` distinct patients | Screen 260 to seek at least 108 independently clear image-positive plus 108 clear image-negative blocks. |
| Construct-confirmation strict pool | 190 plus 190 distinct patients | Screen 380 to seek at least 160 independently clear blocks per image polarity (320 total) for the two-control plan. |
| Four-control confirmation | 235 plus 235 distinct patients | Screen 470 to seek at least 200 independently clear blocks per image polarity (400 total). |
| Calibration | 250 strict natural patient-studies | Feasibility only; final calibration power remains unresolved. |
| Natural target | 380 strict patient-studies and at least 50 in each report-screen polarity | Feasibility only; not downstream power. |
| Natural-ambiguity recruitment | 100 `uncertain` plus `disagree` candidates | Screening pool only; does not establish genuine ambiguity. |

Stop and reopen Gate 0 when:

- a patient crosses a split, a mapping is non-unique, or small-cell disclosure
  is not cleared;
- Month-3 independently clear balanced blocks fall below 108+108, two-control
  confirmation falls below 160+160, four-control confirmation falls below
  200+200, or attrition exceeds 20%; majority-polarity cases are downsampled by
  the frozen keyed rank and cannot replace a missing minority cell;
- technical integrity/input coverage cannot be assessed reliably, or
  determinate-source blocks cannot support a unique image-only state; intact
  natural-ambiguity blocks may retain `Y_v=undefined`;
- the downstream event/effective-sample calculation exceeds the natural target
  pool;
- success would require silently replacing the unit with a multi-view study,
  using report labels as image truth, or moving patients across partitions.

Construct samples are exactly 1:1 independently image-labelled positive versus
negative after eligibility, ensuring text polarity/template can be equally
represented in compatible and conflict cells. Natural target sampling retains
its declared prevalence. The four-control plan cannot be claimed feasible from
the two-control floor.

## Stage-C Boundary

After Stage B, a disclosure-reviewed aggregate record returns to the Commander,
clinical owner, and governance owner. They may kill the route, change and
re-freeze Gate 0, or authorize a new bounded Stage-C task. Stage C would still
need to specify the exact image/report subset, clinical access, annotation
workflow, derived artifacts, retention, and model prohibition or permission.
Passing Stage B never authorizes images, reports, annotation, intervention
generation, model access, or experiments.

## Approval Questions

1. Is pleural effusion and `strict_single_frontal` clinically acceptable, with
   multi-view studies held only as a reserve requiring a new decision?
2. Are the HMAC partitions, one-study-per-patient rule, screening strata,
   aggregate outputs, cell suppression, and numerical stops acceptable?
3. What approved access basis applies to every researcher and reader, and what
   named ACL, reader UI/export controls, secure path, retention, backup, and
   incident controls are approved?
4. May project-generated annotations, atomic propositions, embeddings,
   checkpoints, and aggregate artifacts be retained or shared, and under what
   terms?
5. Does the DUA's code-availability obligation require a licensing change
   before any result is disseminated?

## Permitted Claim

This record defines a testable two-stage data route. It does not establish
access, sufficient counts, image truth, ambiguity labels, checkpoint
disjointness, annotation feasibility, clinical value, or permission to query
or download anything.
