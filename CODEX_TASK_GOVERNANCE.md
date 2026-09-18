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

### Runtime module overlay roles

Use the four module role keys in `CODEX_ROLE_HARNESS.md` and `.codex/agents/*.toml` as the runtime mapping:

- `advisor` (legacy `Ultra`): strategic advice and Commander-facing tradeoff framing.
- `engineer` (legacy `Research + technical-design portions of Engineering`):
  technical strategy, specification, and delegated daily research work.
- `executor` (legacy `Coding + implementation portions of Engineering +
  authorized deterministic Operations`): implementation and deterministic
  execution steps.
- `adjutant` (legacy `coordination / intake / receipts`): routing and state
  tracking.

This mapping does not alter scientific protocols, budgets, methods, or data-
governance decisions.

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
