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

- Contract ID: `EC-2026-09-20-002`
- Task: publish one English-only discussion issue about the probabilistic instrument
- Status: `COMPLETE`
- Authorized by: Commander explicitly requested creation of the proposed GitHub issue in the Adjutant conversation on 2026-09-20.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/probabilistic-tool-discussion-2026-09-20`
- Expected base: `9ffc751a17091441162bec9bcdfdec4da5f71309`
- Linked Handoff Contract: `HC-2026-09-20-002`
- Owner: Adjutant coordinates and bootstraps this EC; existing Executor receives sole contract-writing and deterministic publication responsibility after explicit transfer.

### Primary outcome

Create one readable English-only GitHub Issue containing the four discussion questions already proposed to Commander: what distribution the instrument predicts; why mismatch is not conflict probability; why this instrument and its deterministic comparator; and what evidence would establish incremental value. Include a short beginner explanation and immutable links to existing specifications. Mark open discussion, not an approved scientific decision, experiment or implementation request. Return and open the actual issue for Commander.

### Authoritative inputs

Read in full: this EC, AGENTS.md, CODEX_TASK_GOVERNANCE.md, CODEX_ROLE_HARNESS.md, previous HC and the assigned role profile, plus docs/research/research_contract.md and the current explicit Commander request. The issue body is the bounded editorial draft supplied by Adjutant; previously completed scientific records are context, not renewed authority. Executor reads existing checker/test and CI lifecycle requirements before publication, reusing verified source evidence without redesign. Existing specification links are pinned to the expected base.

### Allowed actions

After traversal, coordinate with the existing Executor under the harness's routine pre-approved execution lane; read remote/issues/permissions/protection to avoid duplicates and verify target; create exactly one discussion issue, apply the Commander's language correction to that same issue if already created, and verify its title/body/state/URL; open that URL. Only EXECUTION_CONTRACT.md and HANDOFF_CONTRACT.md may be changed in cd30 at C:/Users/karl/.codex/worktrees/cd30/ambiguity-is-not-conflict. Use existing bundled Python and existing pytest target C:/Users/karl/.codex/tmp/ec-2026-09-20-001-validation; ordinary pytest and final repository checker are permitted including static compiler calls only within existing tests. Temporary non-sensitive request/response drafts may be stored outside Git under C:/Users/karl/.codex/tmp/ec-2026-09-20-002. Use existing Git credentials only in memory; never print/persist them. Normal fetch/branch/commit/push/PR/merge and CI verification for the required contract record are allowed; preserve the established finite primary and one completion-only closure lifecycle. No new permanent task or automation.

### Forbidden actions

No dataset or model download. No query of restricted data. No scientific execution, simulations, standalone resource compilation, training, annotations, clinical contradiction generation, new method/threshold/budget decisions, core code/test/scientific document edits or Gate-0 closure. No labels/assignees/mentions that imply scientific approval, unsolicited messages, private correspondence or protected content. No force push, history rewrite, branch deletion, protection weakening or explicit override. Do not restart completed research work.

### Preconditions

cd30 clean at expected base before this sole bootstrap mutation; live origin main verified at the same base and origin correct. Complete coordinator traversal and explicit sole-writer transfer before dependent actions. Verify again before publication; stop affected work on unrelated divergence. Check existing issues for an exact duplicate before creating one.

### Promotion criteria

Exactly one issue exists with the intended English-only content, four questions, open-discussion boundary, and working immutable source links. No claim of approved new science or measured results. Required checks and bounded privacy/diff review pass. HC records issue identity/readback, scope and checks; normal contract publication and finite closure have honest CI receipts. User receives the issue link and browser opening. No new research task follows.

### Stopping criteria

Stop affected action on missing authority, unexpected duplicate, sensitive content, target mismatch, failed checks or divergent unrelated changes. Do not retry uncertain issue creation blindly; inspect issues first. A normal publication blocker must be reported without weakening protections. After creation, validation and contract closure, stop.

### Irreversible and external boundaries

Commander explicitly authorizes this single issue publication. Required governance contract GitHub synchronization follows AGENTS. Ordinary administrator-exempt merge is narrowly permitted only after freshly verifying existing actual permissions and enforce_admins=false, with unchanged required checks and explicit HC disclosure; no bypass/override flag or protection mutation. No paid compute, account agreements, new external recipients or scientific access.

### Required evidence

Initial and final revisions/status, exact two-file diff, issue title/body/readback/URL, tests and final checker results, privacy and staged review, remote/branch/upstream/divergence, PR and CI receipts. Record HC READY FOR REMOTE FINALIZATION before primary contract publication; after primary merge/CI use one EC/HC COMPLETE closure. Closure identity is self-evidencing and returned directly, never recursively recorded.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Adjutant initial inspection: clean cd30; HEAD and live origin main at expected base; origin https://github.com/DearKarl/ambiguity-is-not-conflict.git. Previous completed contracts confer no new execution authority. This EC is the only bootstrap mutation.

- Adjutant completed full traversal on 2026-09-20: new EC, AGENTS, governance, harness, prior HC, Adjutant profile, research contract and explicit request. Recovered truncated output with bounded reads. Verified authority, one-issue/two-contract boundary, no science, prerequisites, promotion/stops, external publication and finite closure. Executor must complete its role-specific traversal before acting.

- Executor completed full traversal on 2026-09-20 after explicit sole-writer transfer: new EC, AGENTS, governance, harness, prior HC, Executor profile, full research contract and the relayed explicit Commander request plus complete editorial draft. Re-read checker freshness and CI lifecycle requirements and reused the unchanged checker/test source evidence already fully traversed in the preceding task. Verified live main at the expected base, correct origin, and only the EC bootstrap dirty. Checked one-issue/two-contract scope, exact temporary boundary, no science, publication authority, stops and finite closure. No additional design or reviewer dispatch is required.

- Language amendment on 2026-09-20: Commander explicitly requested English only after issue #15 was created from the earlier bilingual draft. Update that same issue, never create a replacement. Sole-writer Executor rereads this amended EC in full before the authorized editorial update; all scientific and two-contract boundaries remain unchanged.
- Executor completed full reread of the language-amended EC before updating the same issue; prior mandatory-source traversal remains valid. The amendment changes editorial language only, with no scientific or recipient expansion.

### Completion record

Issue #15 was created once and corrected in place to English only, with exact
API readback and Adjutant's actual-browser verification. Primary contract
commit `036ed6530212261ca0174efd883ed74b5973cee0` merged through PR #16 as
`e818390d35bcff46fbb17fd9dd79f8d613b4e911`; branch/PR/main CI all passed.
The only remaining action is validation/publication/CI of this single
two-contract completion closure on
`codex/probabilistic-tool-discussion-closure-2026-09-20`, then final handoff
and stop. No scientific or additional issue action is authorized.
