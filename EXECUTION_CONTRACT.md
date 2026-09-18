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

One single-use self-hosting exception is allowed only when the first closure
validation exposes a deterministic defect in the governance checker or its
tests that prevents the valid `READY` to `COMPLETE` transition. Before any
repair, restore the contracts to their pre-completion statuses, assign and
link a unique closure-remediation ID, amend and fully re-traverse this
contract, and name the exact checker/test files. The exceptional closure may
then change only the two contracts and those named governance files, must pass
independent review and all checks, and must still use the same single closure
PR. It cannot touch scientific documents, data, models, experiments, or
GitHub protection. No unrecorded or second remediation is allowed.

## Active contract

### Identity and status

- Contract ID: `EC-2026-09-18-001`
- Task: synchronize all non-sensitive research progress and literature, consolidate the four-role architecture, and package a cross-device NeurIPS 2027 plan
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander, explicit request in the Adjutant session on 2026-09-18
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/neurips-2027-progress-sync`
- Expected base: `d63e96abafe965ba0a59fb2c8442921fe94d0ab6`, subject to read-only remote verification before branching
- Linked Handoff Contract: `HC-2026-09-18-001`
- Owner: Adjutant coordinates; Executor is sole substantive repository writer after explicit dispatch; Advisor and Engineer provide read-only bounded plans.

### Primary outcome

Publish a complete non-sensitive progress and literature snapshot to GitHub and
assemble a project-specific migration package under Desktop/Handoff. Record
NeurIPS 2027 Main Track submission as the sole project objective, without
promising acceptance or weakening scientific kill gates. Obtain complementary
Advisor, Engineer and Executor contributions to a concrete pre-access plan.
The prior opt-out for meeting/admin publication is superseded only for sanitized
progress summaries explicitly requested now, not private correspondence or data.

### Authoritative inputs

Read in full before dependent work: AGENTS.md, CODEX_TASK_GOVERNANCE.md, this
contract, the prior HANDOFF_CONTRACT.md, the current Commander request,
and the Desktop CODEX_ROLE_HARNESS.md and four .codex/agents profiles.
Targeted implementation inputs, read by their assigned owner before edits:
README.md, docs/roadmap.md, docs/research/README.md, submission_strategy.md,
research_contract.md, scope_charter.md, dataset_decision_record.md,
decision_log.md, literature_matrix.md, novelty_audit.md, scripts/check_repository.py,
and tests/test_repository_contract.py. Research paths are under docs/research.
The sanitized Desktop Adjutant handoff and dataset requirements note are
migration inputs, not scientific authority. Published four-role branch changes
may be reconciled without copying stale local task contracts wholesale.

### Allowed actions

After traversal, inspect remote/worktree/branch inventories; fetch; create a
clean bounded branch; send explicit read-only planning requests to the existing
Advisor and Engineer tasks and bounded implementation to Executor. No new tasks
are needed. Reconcile authorized governance/profile changes, submission purpose,
non-sensitive access-status summaries, plan and literature/progress indexes.
Allowed repository surface: the two contracts; AGENTS.md; CODEX_TASK_GOVERNANCE.md;
CODEX_ROLE_HARNESS.md; .codex/agents/*.toml; README.md; docs/roadmap.md;
docs/research/README.md, submission_strategy.md, research_contract.md,
scope_charter.md, decision_log.md, dataset_decision_record.md;
new docs/research progress/plan/migration records; and a portable Handoff/
folder containing only non-sensitive documentation and inventories.
Preserve existing literature, bibliography, reports, code and tests; include them
in the portable snapshot and Git completeness inventory, without rewriting their
scientific contents. Read additional tracked material as needed for inventory.
Outside Git, create a project-specific Desktop/Handoff migration package,
manifest, full safe repository snapshot and Git bundle if useful. Preserve other
projects and the existing handoff. Ordinary local validation only; no paid compute.
Existing static registry/compiler calls inside the mandated pytest suite are
permitted as deterministic validation, not scientific simulation; do not run
resource compilers independently.
Run required checks, commit, push, create and normally merge PRs after passing CI,
then use one completion-only two-contract closure. A normal administrator-exempt
merge is allowed only if the repository's existing sole-collaborator condition is
verified and disclosed; no explicit override flag or protection weakening.

### Forbidden actions

Explicit boundaries: no dataset or model download; no query of restricted data.
No restricted data/model access or download, credential export, clinical records,
private screenshots, raw personal correspondence, training reports or verification
tokens in Git or the package. No scientific execution, annotation, threshold,
method or budget changes, Gate-0 closure, experiments, force push, history rewrite,
branch deletion, protection changes, or automatic resumption of legacy work.
No overwriting unrelated dirty worktrees or other projects in Desktop/Handoff.

### Preconditions

Current worktree clean except this authorized contract draft; existing Desktop
changes preserved. Confirm exact remote and remote base before substantive edits.
Full traversal and explicit per-owner boundary before delegation or mutation.
If remote base differs, amend this contract and re-traverse before proceeding.

### Promotion criteria

Sole submission objective is consistent, current access status is not inflated,
four roles match the latest authorized configuration, literature/progress coverage
is inventoried, plans identify owners/dependencies/deliverables without execution
permission, privacy scans and required repository checks pass, and primary plus
closure publication evidence is recorded. The Desktop package includes final
repository content and exact revision identity, without recursive self-hashes.

### Stopping criteria

Stop affected work on conflicting ownership, sensitive artifacts, scientific scope
expansion, failed checks or remote divergence. Resolve bounded routine errors;
never weaken checks to publish. Keep distinct remote publication and local archive
completion states if an external blocker prevents completion.

### Irreversible and external boundaries

GitHub publication and coordination with the three existing project modules are
explicitly authorized. No other messages, applications, agreements, payments or
restricted access. Remote publication follows review/checks; ordinary merge only.

### Required evidence

Exact before/after revisions and changed files; all-worktree non-sensitive
inventory; module receipts; literature index and snapshot manifest; test/checker
results; privacy/path checks; PR/CI/merge receipts; Desktop package verification.
No claim that all legacy sessions were reviewed unless actually inspected.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Executor traversal: completed 2026-09-18 before dependent documentation work;
  read mandatory contracts/governance, Desktop role sources, every named
  targeted input, and the two sanitized migration inputs. Confirmed branch,
  origin URL, HEAD and origin/main at the expected base, with only the
  authorized EC draft initially modified. Re-read the full amended EC after
  the Adjutant clarified pytest-only static compiler calls and explicit
  download/query prohibitions. No standalone compiler is authorized.
- Completed 2026-09-18: Adjutant read the contract and mandatory governance inputs in full, including prior HC and Desktop role profiles. Authority, boundaries, promotion/stop criteria and finite closure reviewed. This contract was the sole pre-traversal mutation. Per-owner targeted reads must precede their dependent edits.
