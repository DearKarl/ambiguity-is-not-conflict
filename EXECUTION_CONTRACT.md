# Execution Contract

This file is the mandatory pre-task control record for repository work. Within
the repository, it is the highest operational workflow rule. Platform,
system, developer, and the Commander's current explicit instructions retain
their normal precedence.

## Contract-first rule

For every new bounded task, before implementation, mutation, publication, or
external action:

1. update this file with one active contract;
2. read this file in full, together with `AGENTS.md`,
   `CODEX_TASK_GOVERNANCE.md`, and the listed authoritative inputs;
3. verify authority, scope, preconditions, allowed and forbidden actions,
   promotion criteria, stopping criteria, irreversible boundaries, and
   required evidence;
4. record the completed traversal below; and
5. start substantive work only while the active contract is
   `AUTHORIZED / IN PROGRESS`.

The sole pre-traversal mutation is drafting or replacing this file itself from
the Commander's explicit task authority. Read-only inspection needed to write
and verify the contract is also allowed. No other file mutation, publication,
or external action is allowed until the new traversal is complete.

The task is not complete until its outcome and evidence have been written to
`HANDOFF_CONTRACT.md`. If the task changes materially, stop and revise this
contract before continuing. A new task must replace the active contract; past
contracts remain available through Git history and the linked handoff record.

Closure is finite and two-phase. First, the primary change may be committed,
reviewed, and merged only after the Handoff Contract is
`READY FOR REMOTE FINALIZATION`. Second, after the primary merge and CI, the
same task may create one completion-only closure change that updates only the
two contracts with final primary-change evidence and sets both to `COMPLETE`.
After that transition, no substantive work is allowed: only verification,
commit, push, PR, merge, and post-merge CI for the closure record itself, plus
the final user handoff. The closure commit and PR are self-identifying in Git
and GitHub and are not recursively written into themselves.

## Active contract

### Identity and status

- Contract ID: `EC-2026-08-29-001`
- Task: bootstrap strict execution/handoff governance and close the current
  repository-governance stage
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander, in the current Codex task on 2026-08-29
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/contract-governance-closeout`
- Expected base: remote `main` at
  `f1fe19b38eb4d036893e79b7c27cca0344517f06`

### Primary outcome

Establish a machine-checked contract-first/contract-last workflow, reconcile
the completed TB-0011 and GitHub integration record, and record the
Commander's `G0-SCOPE A` decision without closing Gate 0 or selecting a
`G0-METHOD` route.

### Authoritative inputs

Read these sources in full or, for long decision documents, inspect every
section relevant to the bounded decisions before acting:

- `AGENTS.md`
- `CODEX_TASK_GOVERNANCE.md`
- `README.md`
- `docs/roadmap.md`
- `docs/research/README.md`
- `docs/research/research_contract.md`
- `docs/research/decision_log.md`
- `docs/research/gate0_closure_audit.md`
- `docs/research/gate0_decision_dossier.md`
- `docs/research/execution_budget_and_backbone_audit.md`
- `docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md`
- `scripts/check_repository.py`
- `tests/test_repository_contract.py`
- the Commander's current authorization and the verified Git/GitHub state

### Frozen interpretations for this task

- TB-0011 is technically and reproducibly complete; its generated artifacts
  remain preserved.
- The merged PR and green CI complete the prior branch-to-`main` integration.
- Gate 0 remains open and core implementation remains blocked.
- `G0-SCOPE A` means determinate-conflict specificity is primary and natural
  ambiguity is veto-only. The Commander approves this option; any other
  required owner or supervisor approvals remain pending.
- `G0-METHOD` is not frozen. Framework-centered validation versus one final,
  tightly time-boxed estimator-theory attempt remains a dialogue decision.
- The local machine cannot hold the approximately 613-GB conditional
  simulation-output core floor; this is a binding execution constraint, not
  the medical dataset size, a final upper bound, or authorization to download
  data.

### Allowed actions

- create `EXECUTION_CONTRACT.md` and `HANDOFF_CONTRACT.md`;
- install their mandatory workflow in `AGENTS.md`,
  `CODEX_TASK_GOVERNANCE.md`, task templates, repository checks, and tests;
- correct stale completion wording for TB-0011 without changing its results;
- record the local-storage constraint and the Commander's `G0-SCOPE A`
  approval in canonical decision/governance documents;
- clarify that `G0-METHOD` and remaining Gate 0 approvals are pending;
- create missing GitHub labels `decision` and `protocol`;
- protect `main` with required pull requests, at least one approval, the
  repository CI check, no force pushes, and no deletion; because the only
  current collaborator is the administrator, preserve administrator bypass
  unless another eligible reviewer is added;
- make narrowly necessary CI/dependency-integrity hardening changes only when
  existing behavior is preserved and all checks pass;
- run read-only audits and the repository's existing verification suite;
- commit, push the bounded branch, open a PR, wait for green CI, and merge
  without force or an explicit protection-override command. For this solo-
  collaborator bootstrap only, a normal administrator-exempt merge is allowed
  after independent review and green CI; it must be disclosed as an exemption,
  not represented as a GitHub approval;
- after the primary merge and CI, create one completion-only closure branch,
  update only `EXECUTION_CONTRACT.md` and `HANDOFF_CONTRACT.md`, verify it, and
  synchronize it through one final PR under the finite self-evidence rule;
- refresh detached role worktrees to the final `main` revision only if they
  are clean and no task state would be lost.

### Forbidden actions

- no medical-data, model-weight, or large-artifact download;
- no core experiment, simulation rerun, model training, annotation, or
  generated-result regeneration;
- no scientific-method selection, new estimator claim, Gate 0 closure, or
  promotion of proposed evidence to completed evidence;
- no claim of clinical value, deployment readiness, publication, or
  acceptance;
- no commit of restricted data, credentials, personal correspondence, or
  identifiers;
- no force push, history rewrite, disabling or weakening branch protection,
  explicit protection-override command, deletion of published branches,
  release, or tag;
- no unrelated edits and no action outside this repository and its GitHub
  settings.

### Preconditions

- canonical local `main` is clean and synchronized to the expected base;
- the working branch is dedicated to this contract;
- the configured remote is exactly
  `https://github.com/DearKarl/ambiguity-is-not-conflict.git`;
- no unrelated user changes are present;
- the active contract traversal is recorded before work continues.

### Promotion criteria

The task may be handed off as complete only when all of the following hold:

1. both contracts exist and repository policy makes their workflow mandatory;
2. automated checks fail if either contract or its essential fields are
   absent;
3. stale TB-0011 integration wording is reconciled;
4. the storage constraint, `G0-SCOPE A` Commander approval, remaining
   approvals, and pending `G0-METHOD` choice are unambiguous;
5. all pre-existing tests plus new contract tests pass, and
   `scripts/check_repository.py` passes;
6. an independent bounded review finds no blocking defect; GitHub approval is
   not falsely inferred from that review;
7. GitHub labels and `main` protection match this contract;
8. the primary bounded branch has green CI and is merged into `main` under the
   disclosed solo-administrator exemption;
9. `HANDOFF_CONTRACT.md` records the primary outcome, evidence, residual risks,
   and exact next decision boundary and is set to `COMPLETE` in a completion-
   only closure change; and
10. that closure change has green CI and is merged into `main`; its own commit,
    PR, merge revision, and post-merge CI remain self-evidencing Git/GitHub
    metadata reported in the final user handoff rather than recursively
    inserted into the record.

### Stopping criteria

Stop and report rather than expanding scope if any of these occurs:

- the checkout contains inseparable unrelated changes or the remote diverges;
- a required check fails and cannot be repaired within this bounded task;
- branch protection cannot be configured with the disclosed administrator
  exemption or another legitimate merge path;
- a proposed edit would select `G0-METHOD`, close Gate 0, alter saved numeric
  results, or require data/model access;
- GitHub authentication, permissions, or API state is unexpected;
- the task requires destructive, costly, or otherwise unlisted external
  action.

### Irreversible and external boundaries

Commits, a pull request, merge, labels, and branch-protection settings are
authorized external changes. They must be verified before application and
must remain auditable and reversible through ordinary Git/GitHub operations.
Force operations, history rewriting, releases, data acquisition, and external
communications are outside authority.

### Required evidence

- pre- and post-change Git status, branch, remote, and divergence checks;
- focused contract/checker tests and full `pytest -q` output;
- repository checker output;
- diff/stat and staged-file review;
- independent review result;
- GitHub label, protection, PR, merge, and CI evidence;
- primary finalization revision and clean-worktree evidence inside the Handoff
  Contract, plus self-evidencing closure revision/CI in GitHub and the final
  user handoff;
- completed linked entry in `HANDOFF_CONTRACT.md`.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Agent: Codex, Ultra research-planning task
- Started: 2026-08-29 (Asia/Shanghai)
- Completed: 2026-08-29 (Asia/Shanghai)
- Preconditions verified: yes; the canonical checkout, working branch, base
  revision, remote URL, and bounded one-file bootstrap diff were checked.
- Notes: `EXECUTION_CONTRACT.md`, `AGENTS.md`,
  `CODEX_TASK_GOVERNANCE.md`, and every listed authoritative input were
  traversed under the full-or-relevant-section rule. The task may now proceed
  only within this contract. After independent review identified ambiguous
  613-GB wording, the contract was corrected and re-traversed in full on
  2026-08-29 before work resumed. After independent review identified the
  contract-bootstrap circularity, recursive closure risk, hard-coded contract
  IDs, and the solo-administrator merge boundary, the finite two-phase
  lifecycle and generic validation rules were added; this amended contract
  was then re-traversed in full on 2026-08-29 before work resumed.
