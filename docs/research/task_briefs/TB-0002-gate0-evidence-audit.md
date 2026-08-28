# TASK_BRIEF

- **Identifier:** TB-0002 — Gate 0 novelty, data-route, and estimand audit
- **Date and owner:** 2026-08-29; Ultra lane, authorized by the Commander
- **Evidence gate:** Gate 0 protocol development; literature leads and
  decision-ready protocol evidence only
- **Primary outcome:** Produce a rigorous decision packet that identifies the
  closest novelty threats, audits candidate chest-radiography data routes
  without accessing data, and recommends one atomic task/estimand/baseline
  package with explicit assumptions, kill criteria, and unresolved approvals.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, DR-0001
  through DR-0006, the full canonical record under `docs/research/`, verified
  primary papers and official code, and official dataset/access/governance
  documentation.
- **Allowed actions:** Read-only public-web research; bibliographic and code
  verification from primary sources; official dataset metadata, licence,
  access, and governance review; parallel read-only subagent audits; update
  `docs/research/README.md`, `docs/research/literature_matrix.md`,
  `docs/research/data_governance.md`,
  `docs/research/measurement_protocol.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/research_question.md`, `docs/research/decision_log.md`, and
  `tests/test_repository_contract.py`; create
  `docs/research/novelty_audit.md`,
  `docs/research/dataset_feasibility_audit.md`, and
  `docs/research/task_estimand_options.md`; run local documentation checks;
  commit and normally push the bounded result after Git verification.
- **Forbidden actions:** Dataset or model download/access; credentialing,
  registration, licence acceptance, or access-request submission; inspection
  of restricted records; clinical annotation or correspondence; code or core
  implementation; training, inference, pilot, or confirmatory experiment;
  paid services; claiming novelty, identifiability, data availability,
  clinical benefit, publication, or venue acceptance as established facts.
- **Exact files/data/model/compute boundary:** Only the files named above and
  this task brief may change. Public metadata and papers may be read; no
  dataset rows, images, reports, checkpoints, API keys, GPU work, or generated
  research results are permitted.
- **Required outputs and evidence:** A source-audited novelty map with direct
  threat rankings and claim boundaries; a dataset feasibility table covering
  version, access, terms, prediction/leakage unit, labels, derived-artifact
  constraints, and blockers; a recommended atomic task and candidate estimand
  package with identification assumptions, negative controls, matched
  baselines, smallest-effect decision needs, and kill conditions; a proposed
  decision record that clearly remains unapproved where Commander or
  governance authority is required.
- **Validation commands:** `pytest -q`; `python scripts/check_repository.py`;
  `git diff --check`; repository-wide terminology/source audit; exact changed
  path and sensitive-content review; final branch/upstream/divergence checks.
- **Promotion criteria:** Every promoted citation and dataset fact is supported
  by a primary or official source; the three strongest novelty threats are
  confronted directly; the recommended route is narrower than open-ended
  report generation, uses a patient-level leakage unit, distinguishes
  construct from target-distribution samples, and can be killed by the named
  matched baselines and controls; all uncertainties and unapproved actions
  remain explicit.
- **Stopping criteria:** Stop on unresolved source identity, unavailable or
  contradictory official terms, a data route that cannot support the atomic
  construct, a novelty threat that subsumes the proposed contribution, a task
  choice requiring unsupported clinical assumptions, unexpected worktree
  changes, sensitive content, or remote divergence.
- **External, costly, or irreversible boundary:** Public read-only research and
  a normal non-force Git push are the only external actions. Any dataset-access
  request, agreement, credential, clinician contact, annotation, compute
  purchase, release, or scope expansion requires a new approved brief.
- **Permitted claim after completion:** The repository contains a verified Gate
  0 decision packet and a recommended route. It does not establish scientific
  novelty, data access, construct identifiability, empirical performance,
  clinical utility, or submission readiness.
