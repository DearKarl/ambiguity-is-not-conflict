# TASK_BRIEF

- **Identifier:** TB-0012 — Gate-0 owner consolidation and restricted-data
  readiness
- **Execution Contract ID:** `EC-2026-09-02-002`
- **Handoff Contract ID:** `HC-2026-09-02-002`
- **Status:** Complete for Stage-A readiness; Gate 0, restricted data, and
  experiments remain unauthorized
- **Date and owner:** 2026-09-02; Commander as consolidated internal project
  owner, executed by the Ultra scientific-governance lane
- **Evidence gate:** Repository-only Gate-0 reconciliation plus public official-
  source verification
- **Primary outcome:** Record the exact scope of consolidated internal approval,
  audit whether Gate 0 can close without inventing external facts or unresolved
  choices, and produce a canonical Stage-A dataset readiness record for the
  coupled MIMIC-CXR/JPG v2.1.0 route.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`,
  `EXECUTION_CONTRACT.md`, the complete canonical research record named there,
  the Commander's 2026-09-02 statement, and current public official PhysioNet
  resource, license/DUA, CITI-training, online-service, and derived-resource
  guidance.
- **Allowed actions:** Read and reconcile the authorized documentation/test
  paths; verify public official pages without login; create DR-0018, the
  dataset decision record, and this brief; obtain independent read-only
  scientific/governance/data-security review; run deterministic repository and
  sensitive-artifact checks; and synchronize the reviewed bounded change by
  normal branch/PR/CI workflow.
- **Forbidden actions:** Credential or browser-session inspection; access
  application or DUA acceptance; dataset query/download; reading images,
  reports, identifiers, or record-level derivatives; creating data directories,
  row manifests, clinical annotations, intervention items, models, checkpoints,
  environments, simulations, experiments, or large artifacts; contacting
  readers; using paid/cloud compute; changing scientific estimands, hypotheses,
  thresholds, sample floors, method roles, or kill rules; or claiming Gate-0
  closure without complete evidence.
- **Exact files/data/model/compute boundary:** Only the paths enumerated in
  `EC-2026-09-02-002` may change. No medical data, model, credential, private
  approval correspondence, or record-level content may be read or created.
  Ordinary local CPU checks and public page reads are the only compute/network
  actions before GitHub synchronization.
- **Required outputs and evidence:** DR-0018 with facts/inferences/assumptions/
  decisions; row-by-row Gate-0 classification; `DDR-2026-09-02-001`; exact
  official-source links and verification date; finite Stage-B readiness list;
  independent reviews; changed-path, sensitive-content, binary, size, and
  untracked scans; repository tests/checker/diff checks; and branch/PR/CI/merge
  evidence.
- **Validation commands:** `pytest -q`; `python scripts/check_repository.py
  --final --base-ref origin/main`; `git diff --check`; exact changed-path and
  artifact scans recorded in the Handoff Contract.
- **Promotion criteria:** Internal approval is not inflated; every Gate-0 row
  is classified; the data record is exact but non-executable; no restricted
  content exists; independent review passes; all checks and GitHub CI pass.
- **Stopping criteria:** Stop if the user statement would require guessing an
  A/B/C choice, any external fact is unavailable, a secure boundary cannot be
  documented, unrelated changes appear, a restricted artifact is encountered,
  or any review/check fails.
- **External, costly, or irreversible boundary:** Public official-source reads
  and normal GitHub synchronization only. No login, credential use, access
  request, download, query, clinical contact, compute purchase, force operation,
  or protection change.
- **Permitted claim after completion:** The repository records consolidated
  internal Method-A/scope approval and a complete pre-access readiness packet,
  while identifying the exact evidence and remaining decisions blocking Gate
  0 and Stage B. It does not establish access, clinical feasibility, dataset
  yield, experiment results, venue readiness, acceptance, or publication.

## Completion Record

- **Completion status:** Complete for the bounded Stage-A scientific/governance
  work. Remote synchronization evidence is governed separately by
  `HC-2026-09-02-002` and does not change this non-executable conclusion.
- **Outcome:** DR-0018 records the exact consolidated internal scope/Method-A
  approvals and partial baseline boundary. `DDR-2026-09-02-001` freezes a
  reviewable, non-executable restricted-tabular screening candidate and the
  finite evidence needed before Stage B.
- **Decision:** Gate 0 remains open. Missing executable specifications,
  unresolved finite choices, and objective access/ethics/security/reader/
  licence/resource/feasibility evidence prevent data access and experiments.
- **Independent review:** Scientific/governance review passed after the 24-row
  crosswalk, baseline, `MV-1`, ablation, data-query, partition, authority, and
  licence wording were reconciled. Data/privacy review passed with every
  Stage-B field classified as restricted and no access authority implied.
- **Local evidence:** `pytest -q` passed 53 tests;
  `python scripts/check_repository.py --final --base-ref origin/main` passed;
  `git diff --check` passed.
- **Boundary evidence:** The 23 changed paths match the Execution Contract.
  Scans found no medical record, identifier value, credential, private path,
  model artifact, binary diff, or file larger than 1 MB. No data/model
  download, query, login, annotation, simulation, or experiment occurred.
