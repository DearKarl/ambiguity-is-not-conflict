# TASK_BRIEF

- **Identifier:** TB-0008 — Reader measurement and MV-1 qualification design
  audit
- **Status:** Complete; Gate 0 remains open
- **Date and owner:** 2026-08-29; Ultra scientific challenge with independent
  statistical, scientific, and governance review, under the Commander's
  continuing instruction to advance the single project
- **Evidence gate:** Gate-0 protocol and synthetic design arithmetic only; no
  scientific or clinical execution
- **Primary outcome:** Convert the unspecified reader-measurement precision and
  crude `MV-1` 108-evaluable-per-polarity approximation into one exact,
  reviewable qualification-analysis contract without approving the clinical
  task, reader roster, `MV-1`, or either `G0-METHOD` route.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, the complete
  canonical record under `docs/research/`, DR-0009/DR-0010, and TB-0005 through
  TB-0007.
- **Allowed actions:** Read the repository; create
  `docs/research/reader_measurement_and_mv1_qualification_audit.md`; create one
  deterministic, synthetic-only design calculator and its aggregate
  sensitivity table; update only `README.md`, `docs/research/README.md`,
  `docs/research/annotation_and_intervention_protocol.md`,
  `docs/research/intervention_option_audit.md`,
  `docs/research/statistical_analysis_plan.md`,
  `docs/research/execution_budget_and_backbone_audit.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/decision_log.md`, `scripts/check_repository.py`,
  `scripts/calculate_mv1_qualification_design.py`,
  `reports/tables/mv1_qualification_yield_sensitivity.csv`,
  `tests/test_repository_contract.py`, and this brief; run local deterministic
  calculations and repository checks; obtain independent read-only scientific,
  statistical, and governance reviews; and perform a normal non-force Git
  synchronization after all reviews pass.
- **Required questions:** Freeze as recommendations only (1) the measurement
  axes and primary reliability coefficient; (2) the exact reliability-set
  allocation and dependence/precision analysis; (3) the `q_v` evaluable
  population, estimator, interval, polarity guardrail, and finite-reader claim
  boundary; (4) disjoint-panel counterbalancing and patient resampling; (5) a
  pre-data simulation DGP/grid with coverage, Type-I error, power, yield,
  Monte-Carlo, and workload criteria; and (6) finite approve/revise/stop
  consequences.
- **Forbidden actions:** Any real, restricted, record-level, medical, model, or
  checkpoint data; any dataset/account/DUA access or acceptance; downloads;
  clinician contact; examples or annotations; model execution; core
  implementation; training, inference, tuning, or experiment; hosted API;
  paid compute; empirical feasibility or reliability claim; task/reader/MV-1
  approval; `G0-METHOD` choice; Gate-0 closure; or promise of venue acceptance
  or publication.
- **Exact boundary:** Deterministic arithmetic may use only synthetic
  probabilities declared in the artifact. It is planning evidence, not
  promoted research evidence. The primary `q_v` inference may condition on a
  locked finite reader roster only if the claim says so explicitly; a reader-
  population claim requires a separately powered reader-sampling design.
- **Required evidence and checks:** Exact formulas and assumptions; generated
  aggregate table reproducible byte-for-byte; independent reviews;
  `pytest -q`; `python scripts/check_repository.py`; `git diff --check`; exact
  changed-path and sensitive-content review.
- **Promotion criteria:** The artifact eliminates ambiguous analysis choices,
  distinguishes finite-roster from reader-population inference, exposes rather
  than hides the 256-candidate yield fragility, and leaves only finite owner,
  external feasibility, or later authorized simulation/reader decisions.
- **Stopping criteria:** If the 256-candidate plan cannot meet the joint yield
  and `q_v` gate under a prospectively owner-approved synthetic assumption
  region, recommend reopening `G0-MV-Q`/`G0-RESOURCES` or killing `MV-1`;
  never weaken the `0.10` margin, same-polarity rule, reader independence, or
  108-per-polarity floor to fit the budget.
- **External boundary:** No external action is authorized except the final
  normal Git synchronization.
- **Permitted claim after completion:** The repository contains an exact
  pre-execution reader/`MV-1` analysis and decision contract plus synthetic
  design arithmetic. It does not establish reader reliability, clinical
  validity, `MV-1` task relevance, feasibility, Gate-0 closure, venue readiness,
  acceptance, or publication.

## Completion Record

- **Completed:** 2026-08-29.
- **Artifacts:** Added the exact reader-measurement/`MV-1` qualification audit,
  deterministic ideal-yield calculator, and byte-reproducible aggregate
  sensitivity table; reconciled the permitted canonical protocol, budget,
  dossier, decision log, repository checker, and contract tests.
- **Decision state:** Recommends `G0-READERS A` and `G0-MV-Q A` for owner
  consideration only. Neither is approved. Gate 0, compute feasibility,
  reader/clinical/governance/resource decisions, actual simulation, data/model
  access, and every execution gate remain open.
- **Scientific boundary:** The q target is selected/evaluable-population
  attenuation conditional on a locked finite roster. The contract includes
  assigned-state alignment, polarity guardrails, disjoint panels, explicit
  wrong-polarity reader errors, dependence-robust reliability-family power,
  exact nested bootstraps, fixed Monte-Carlo counts, and prospective kill
  consequences without claiming intervention validity or clinical benefit.
- **Independent review:** Scientific, statistical, and governance reviewers
  each returned `PASS` after all identified blockers were remediated.
- **Verification:** `pytest -q` passed 31 tests; repository checker returned
  `Repository contract: OK`; `git diff --check` passed; the generated CSV
  matched the tracked table byte-for-byte; changed-path and sensitive-content
  reviews passed.
- **Execution boundary:** No reader, patient record, restricted dataset, model,
  checkpoint, experiment, download, clinical annotation, or paid compute was
  accessed or run. The only external action permitted after review is the
  normal non-force Git synchronization required by this brief.
