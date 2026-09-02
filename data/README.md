# Data Boundary

This directory is a governance placeholder, not a data distribution.

No medical image, report, patient-level table, identifier, credential, model
checkpoint, or access token belongs in Git. Local data paths must remain outside
the repository. [DDR-2026-09-02-001](../docs/research/dataset_decision_record.md)
is a readiness record, not an approved path or access authorization; a local
path may be configured only after Gate-0 closure and a fresh Stage-B contract.

Permitted future committed artifacts are limited to items explicitly allowed
by the applicable data-use agreement, such as schemas, checksums, aggregate
statistics, synthetic examples with compatible licences, or non-identifying
derived metadata. Candidate access does not imply permission to redistribute.

Read [data and clinical governance](../docs/research/data_governance.md) before
any data action.
