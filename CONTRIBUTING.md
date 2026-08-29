# Contributing

This project is in protocol design. Contributions should strengthen the
falsifiability, validity, or reproducibility of the single primary research
route rather than add parallel research themes.

## Before Opening a Change

1. Update `EXECUTION_CONTRACT.md`, then read it in full together with
   `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, and every named authoritative
   input. Record the completed traversal before changing anything.
2. Identify the canonical document or frozen task brief that authorizes the
   change.
3. State whether the change is planned, protocol, pilot, completed evidence, or
   promoted evidence.
4. Confirm that no restricted data, personal correspondence, credentials, or
   identifiers are included.
5. Before marking the task complete, write its outcome and evidence to
   `HANDOFF_CONTRACT.md`.

## Pull Requests

A pull request should be small enough to review as one scientific decision. It
must state:

- active Execution Contract and linked Handoff Contract;
- objective and authoritative inputs;
- files changed and files deliberately excluded;
- scientific claim, if any, and its evidence status;
- validation command and result;
- data/model/configuration versions for experimental changes;
- deviations, negative results, and unresolved risks;
- whether a decision record or protocol amendment is required.

Run before submission:

```bash
pytest -q
python scripts/check_repository.py --final
```

Core experimental work requires a frozen task brief and a closed Gate 0. A
passing test suite is necessary engineering evidence, not evidence that a
research hypothesis is true.
