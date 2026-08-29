# TASK_BRIEF

- **Identifier:** TB-0010 — Static proof-preserving simulation computation
  design
- **Status:** Complete; Gate 0 remains open
- **Date and owner:** 2026-08-29; Ultra scientific challenge with independent
  scientific, statistical, and governance review, under the Commander's
  continuing instruction to advance the single project
- **Evidence gate:** Gate-0 protocol and resource-design work only; no
  computational benchmark, scientific implementation, simulation, or clinical
  execution
- **Primary outcome:** Specify a hardware-neutral computation graph, proposed
  result/checkpoint schema, determinism and output-equivalence obligations, and
  a future artificial-buffer benchmark contract for the unchanged TB-0009
  workload, without implementing or timing any project primitive.
- **Authoritative inputs:** `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, the complete
  canonical record under `docs/research/`, DR-0011--DR-0012, and TB-0008--
  TB-0009.
- **Allowed actions:** Read the repository; create
  `docs/research/noncore_simulation_computational_design.md`; update only
  `README.md`, `docs/research/README.md`,
  `docs/research/simulation_resource_feasibility_audit.md`,
  `docs/research/execution_budget_and_backbone_audit.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/decision_log.md`, `scripts/check_repository.py`,
  `tests/test_repository_contract.py`, and this brief; run only local text,
  contract, and version-control checks; obtain independent read-only
  scientific, statistical, and governance reviews; and perform a normal
  non-force Git synchronization after every review passes.
- **Required questions:** Freeze as recommendations only (1) the stage and
  kernel decomposition; (2) artificial-buffer shapes for a later generic
  benchmark; (3) deterministic batching, reduction, parallelism, checkpoint,
  failure, and restart rules; (4) a proposed normalized result schema and byte
  formulas; (5) exact proof obligations for any sufficient-statistic,
  streaming, caching, or deduplication optimization; (6) conservative scaling,
  uncertainty, and contingency equations; (7) future benchmark acceptance and
  stopping rules; and (8) every quantity that still requires implementation,
  measurement, owner selection, or external verification.
- **Forbidden actions:** Implementing or executing a project RNG, DGP,
  calibration equation, bootstrap statistic, reliability coefficient,
  fixed-effect/leave-one-reader analysis, Clopper--Pearson calculation,
  scientific pipeline, benchmark, simulation, model, or experiment; generating
  project synthetic observations or calibration buffers; accessing any reader,
  record, restricted dataset, account, DUA, checkpoint, clinical example,
  hardware allocation, or paid/hosted compute; downloads; selecting a hardware
  route or `G0-RESOURCES` option; changing cells, hashes, factor grids, streams,
  thresholds, multiplicity, `120,000`, `9,999`, or no-early-stop rules; Gate-0
  closure; or promising venue acceptance or publication.
- **Exact boundary:** The new artifact is a static specification. Artificial
  buffers and kernel calls are future benchmark *descriptions*, not data,
  code, allocations, or measurements. Proposed schemas and algebraic
  optimizations remain obligations for a later post-Gate-0 implementation
  review; they are not implementation-correctness claims. TB-0009 manifests
  and hashes are immutable inputs.
- **Required evidence and checks:** Explicit facts/inferences/assumptions/
  recommendations; end-to-end stage graph; workload-to-kernel crosswalk;
  normalized schema with closed-form byte/RAM/scratch/restart formulas;
  reference-order, stream-identity, lossless-reconstruction, and atomic-restart
  proof obligations; future benchmark acceptance/kill rules; exact changed-path
  and sensitive-content review; independent reviews; `pytest -q`,
  `python scripts/check_repository.py`, and `git diff --check`.
- **Promotion criteria:** The design covers every frozen reliability and
  `MV-1` stage, preserves the TB-0009 hashes and `K_plan=4,416`, identifies no
  unbounded storage/RAM/scratch term without an explicit stop, permits no
  scientific shortcut, and reduces the next resource action to a finite
  artificial-buffer benchmark and capacity-allocation decision.
- **Stopping criteria:** Stop if any proposed optimization can change a
  canonical cell, seed/tag/raw-word sequence, bootstrap index, statistic,
  strict inequality, failure class, multiplicity family, or required audit
  output; if floating-point reassociation lacks a reference-order conformance
  obligation; if a required output cannot be reconstructed losslessly; if an
  operation, storage, RAM, scratch, or restart term lacks a defensible bound;
  or if the design requires cell pruning, outer early stopping, fewer than
  120,000/9,999 replications, or weaker gates.
- **External boundary:** No external action is authorized except the final
  normal Git synchronization. If the remote is unavailable, retain the
  reviewed commit locally and report the exact divergence; do not force or
  rewrite history.
- **Permitted claim after completion:** The repository contains a static,
  proof-obligation-based computation and future benchmark design for the
  unchanged pre-reader simulation. It does not establish implementation
  correctness, calibration admissibility, runtime, affordability, resource
  availability, operating performance, reader reliability, `MV-1` validity,
  Gate-0 closure, acceptance, or publication.

## Completion Record

- **Completed:** 2026-08-29.
- **Artifacts:** Added the static non-core computation design, canonical README
  entries, DR-0013, resource/dossier/closure reconciliations, repository-path
  enforcement, and contract tests.
- **Design result:** The record freezes a semantic stage graph, immutable
  invariants, workload-to-kernel crosswalk, proposed normalized audit/checkpoint
  schema, deterministic restart rules, P0--P11 proof register, system-wide
  concurrency equations, and future generic-benchmark acceptance/kill rules.
  It implements and times none of them.
- **Static arithmetic:** The proposed core audit schema is 572,293,215,610
  bytes; adding the successful-path completion bitmap gives
  572,492,490,610 bytes before journal, permutation/identifier dictionaries,
  extensions, aggregate/failure records, format overhead, scratch, redundancy,
  or backups. Materialized calibration produces 818,057,052,160 unique raw
  words, whereas full replay would produce 14,503,497,089,155,072; neither
  route is selected.
- **Decision state:** `G0-METHOD` remains scientifically prior and owner-
  blocked. `G0-READERS`, `G0-MV-Q`, `G0-RESOURCES`, and Gate 0 remain open.
  DR-0013 recommends testing the unchanged contract under A before considering
  a scientific redesign under B, but selects no option, resource, benchmark,
  implementation, or run.
- **Remaining resource blockers:** Exact numeric/output and semantic-count
  registries, identifier/permutation and failure bounds, numerical special-
  function domains, permitted generic RNG/surrogate timing, hardware/load/
  software locks, system-wide RAM/scratch/storage/I/O, familywise timing/tail
  evidence, hard or explicitly approved probabilistic service level, capacity,
  and named-owner approvals.
- **Independent review:** Scientific, statistical, and governance reviewers
  each returned `PASS` after percentile-to-total extrapolation, circular
  benchmark staging, raw-word/index work, retry lifecycle, multi-worker memory/
  scratch, probability-construction, and inverse/special-function domain
  blockers were remediated.
- **Verification:** `pytest -q` passed 33 tests; repository checker returned
  `Repository contract: OK`; `git diff --check`, exact changed-path review, and
  sensitive-content review passed.
- **Execution boundary:** No project RNG, DGP, calibration, bootstrap,
  statistic, simulation, benchmark, data, reader, model, checkpoint, account,
  download, environment, hardware allocation, or hosted/paid compute was
  accessed, implemented, or run. The only external action permitted after
  review is normal non-force Git synchronization.
