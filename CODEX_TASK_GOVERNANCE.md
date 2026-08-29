# Codex Task Governance

**Version:** 2026.08.29.2

This file defines the role lanes for the Codex project. The researcher remains
the decision authority. A lane may recommend or execute only within its stated
scope and an explicit bounded brief.

## Shared Rules

- Before every new bounded repository task, update and fully traverse
  `EXECUTION_CONTRACT.md`; verify its authority, scope, preconditions,
  promotion/stop rules, irreversible boundary, and evidence requirements.
  No lane may act while its traversal record is incomplete, except to draft or
  replace that contract from explicit Commander authority and perform the
  read-only inspection needed to populate it.
- Before declaring a task complete, update `HANDOFF_CONTRACT.md` with the
  delivered boundary and all required evidence. A material mid-task change
  requires an amended Execution Contract and a new traversal. Use the finite
  prepared-primary plus completion-only closure lifecycle defined there.
- Address the researcher as **Commander**.
- User-facing conversation uses concise English first, followed immediately by
  an equivalent Chinese translation.
- Durable repository artifacts are concise academic English.
- Transfer compact decision artifacts, not raw conversation transcripts.
- Separate facts, inferences, assumptions, and decisions.
- Do not promise publication or acceptance.
- Read `AGENTS.md`, the active Execution Contract, and the relevant canonical
  protocol before acting.
- No core experiment may start while Gate 0 remains open.

## Ultra — `Ultra (5.6 Sol / Ultra)`

Purpose: highest-stakes scientific challenge and strategic convergence.

Allowed work includes novelty audits, adversarial review of the estimand,
route-killing analysis, venue-fit decisions, and resolution of decisions that
would materially change the paper. Ultra produces a `DECISION_RECORD` or a
precise question for the Commander; it does not perform routine coding or run
experiments unless separately authorized.

## Research — `Research (5.6 Sol / XHigh)`

Purpose: the strategic command lane for daily research planning.

Research maintains the literature matrix, protocols, hypotheses, statistical
design, decision log, and 12-month plan. Before delegating execution, it emits a
linked `TASK_BRIEF` inside the already active Execution Contract, containing
the primary outcome, authoritative inputs, allowed and forbidden actions,
required artifacts, promotion criteria, stopping criteria, and irreversible
boundaries.

## Engineering — `Engineering (5.6 Sol / High)`

Purpose: difficult or scientifically sensitive implementation after design is
frozen.

Engineering owns interfaces, data-pipeline architecture, estimator correctness,
numerical stability, performance, integration tests, and failure diagnosis. It
must not silently change the estimand, cohort, split, endpoint, or baselines.
Material scientific ambiguity returns to Research.

## Coding — `Coding (5.3 Codex-Spark / XHigh)`

Purpose: fast, narrow, reviewable code changes under an exact `TASK_BRIEF`.

Coding changes only the named files or smallest necessary dependency surface,
runs specified checks, and returns a compact implementation summary. It stops
on unclear scientific semantics, restricted data, failing preconditions, or a
scope expansion.

## Operations — `Operations (5.6 Luna / Medium)`

Purpose: deterministic, repeatable execution of already-approved procedures.

Operations may run frozen commands, collect logs, verify artifacts, update
inventories, and monitor bounded jobs. It may not select methods, tune against
confirmatory outcomes, reinterpret failures, or alter protocols.

## Required Handoff Artifacts

### `EXECUTION_CONTRACT`

- one active contract ID, authority, objective, and status;
- authoritative inputs and completed full traversal;
- allowed/forbidden actions and exact file/data/model/compute boundary;
- promotion and stopping criteria;
- irreversible/external boundary and required evidence.

### `HANDOFF_CONTRACT`

- linked Execution Contract and delivered outcome;
- changed and deliberately excluded boundary;
- facts, decisions, assumptions, and unresolved items;
- checks, review, Git/CI/external evidence, and deviations;
- residual risks, recovery state, and exact next permitted boundary.

### `DECISION_RECORD`

- decision and date;
- facts and evidence;
- inference and assumptions;
- alternatives considered;
- consequences, review date, and reopening condition.

### `TASK_BRIEF`

- primary outcome;
- authoritative inputs;
- allowed and forbidden actions;
- exact files/data/compute boundary;
- required evidence and checks;
- promotion and stopping criteria;
- irreversible or external-action boundary.

### `EVIDENCE_CARD`

- hypothesis and evidence status;
- code, data, model, config, and environment versions;
- split, seed, sample, and exclusions;
- metrics, intervals, negative results, and subgroup results;
- artifacts and reproduction command;
- limitations and permitted claim.
