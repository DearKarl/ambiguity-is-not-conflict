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

- Contract ID: `EC-2026-09-20-001`
- Task: compile the pre-access specification, acceptance matrix and finite decision package
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander on 2026-09-20, explicitly relayed by Advisor task 01a0bb7b-e9b9-7f61-acb0-38a7584670b8.
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Expected base: `585be42d47a86b84a16bbf986d83e96f37145306`; verify remote before implementation.
- Working branch: `codex/pre-access-readiness-2026-09-20`
- Linked Handoff Contract: `HC-2026-09-20-001`
- Owner: Adjutant coordinates. Adjutant only bootstraps this EC in cd30. After explicit transfer Executor is the sole writer, including both contracts, in cd30; Engineer is read-only specification owner; Advisor is read-only strategic adviser.

### Primary outcome

Deliver concrete reviewable protocol specifications, prospective acceptance checks and finite Commander decisions for pre-access preparation. Preserve Method A as sole route and NeurIPS 2027 Main Track as sole strategic objective without acceptance promises. Package acceptance is separate from scientific success and operational readiness; Gate 0 remains open.

### Authoritative inputs

Adjutant fully reads AGENTS.md, CODEX_TASK_GOVERNANCE.md, CODEX_ROLE_HARNESS.md, this EC, prior HC, .codex/agents/adjutant.toml, docs/research/research_contract.md, pre_access_preparation_plan.md, progress_2026-09-18.md, and the complete DR-0018, remaining-Gate-0 list and DR-0019 sections of docs/research/decision_log.md. Research short paths in this contract are under docs/research/.
Engineer and Executor fully traverse the mandatory governance/contracts and their role profile before dependent work, then read the relevant canonical design inputs: gate0_decision_dossier.md, gate0_closure_audit.md, method_a_identification_framework.md, statistical_analysis_plan.md, estimator_formalization_audit.md, measurement_protocol.md, annotation_and_intervention_protocol.md, reader_measurement_and_mv1_qualification_audit.md, baselines_and_ablations.md, dataset_decision_record.md, data_governance.md, execution_budget_and_backbone_audit.md, simulation_output_and_operation_registry.md, noncore_simulation_computational_design.md, submission_strategy.md and novelty_audit.md. Read any further referenced source before relying on its detail. Executor additionally reads scripts/check_repository.py and tests/test_repository_contract.py to follow existing validation, without editing them.

### Allowed actions

Read-only source and Git verification; existing-module coordination; branch/fetch; documentation drafting and review; deterministic existing pytest and final checker; normal commit, push, PR and merge after checks. Exact writable surface: EXECUTION_CONTRACT.md, HANDOFF_CONTRACT.md, docs/research/pre_access_readiness_specification.md, docs/research/pre_access_acceptance_matrix.md, docs/research/pre_access_decision_package.md, docs/research/README.md and docs/research/pre_access_preparation_plan.md. Worktree: C:/Users/karl/.codex/worktrees/cd30/ambiguity-is-not-conflict. Other worktrees remain unchanged. English durable artifacts and concise Chinese dialogue. As coordinated by Adjutant on 2026-09-20, necessary reversible validation preparation may install only existing requirements-dev.txt pytest==8.4.2 and its required dependencies into C:/Users/karl/.codex/tmp/ec-2026-09-20-001-validation, using the existing bundled Python. This is the sole additional temporary filesystem boundary; no scientific dependencies/models, paid service, tracked environment files or gh installation. Record exact versions and commands. Existing Git Credential Manager credentials may be used only in memory for authorized GitHub REST operations; never print or persist credentials.

### Forbidden actions

No dataset or model download. No query of restricted data. No core code/test changes, historical decision or approved-method rewrites, Gate-0 closure, scientific execution, dataset/model download, restricted query, training, simulation, independent resource compiler, clinical contradiction generation or annotation. No new threshold/budget approval by inference, no account actions, agreements, private correspondence, credentials or identifiers. No new tasks/automations, legacy job resumption, force push, history rewrite, branch deletion, protection weakening or explicit override.

### Preconditions

Local base and origin match the stated repository; worktree initially clean. Complete traversal before delegation or mutation other than this EC bootstrap. Verify remote divergence before substantive writing. Preserve unrelated work. Executor acknowledges exclusive writing transfer before editing.

### Promotion criteria

Cover every DR-0018 and remaining Gate-0 row with approved/source-derived/proposed/owner-decision/external-evidence/data-dependent status and exact authority. Clinical unit, independent readers, construct, interventions, information-loss controls, artifact rules and natural-ambiguity veto each have object, method, threshold or explicit prior decision, evidence and failure action. Preserve psi_mag, named instrument/comparators, ablations, patient splits and inference semantics. Missing executable fields have precise gaps, recommendations, alternatives and reasons; no generic TBD substitutes. Predefine data-dependent yield, reliability, validity and resource checks. Specify Stage-B and later stage sequence without execution permission. Include claim/evidence/failure mapping and finite Commander decisions. Required checks pass; sanitized Git/publication and finite closure receipts are recorded. Neither novelty nor scientific readiness is claimed from documentation acceptance.

### Stopping criteria

Stop affected work for authority conflict, overlapping writers, sensitive content, remote divergence, failed validation, scope expansion or unsourced scientific changes. Repair only within scope; do not weaken checks. Return exact blockers if ordinary publication cannot finish. After delivery stop and return to Advisor/Commander for discussion of mathematics, instruments, comparator and inference.

### Irreversible and external boundaries

Only existing project-module coordination, read-only public source verification and normal GitHub synchronization are authorized. Before merge verify current protection and permissions. A normal administrator-exempt merge is narrowly permitted only if existing enforce_admins=false and actual account permission permit it, explicitly disclosed in HC; no override flag, protection change or inferred privilege. If unavailable, retain PR and report blocker. No paid compute; ordinary local documentation validation only. Static compiler calls are permitted only inside existing mandated pytest.

### Required evidence

Versioned input/source crosswalk; Engineer specification receipt; Adjutant historical/external-evidence ledger and scope review; Executor changed-file inventory; pytest -q, python scripts/check_repository.py --final and diff-check results; privacy review; remote/branch/upstream/staged/divergence checks; commit/PR/CI/merge status. Use existing finite primary/closure lifecycle: HC READY FOR REMOTE FINALIZATION before primary publication, then one two-contract COMPLETE closure after primary merge/CI. Closure identity remains self-evidencing, not recursive.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Initial read-only evidence: cd30 clean detached HEAD at expected base; origin https://github.com/DearKarl/ambiguity-is-not-conflict.git. Historical EC/HC COMPLETE confer no new authority. This EC is the sole bootstrap mutation.

- Adjutant completed full coordinator traversal on 2026-09-20: mandatory governance, new EC, prior HC, role profile, research contract, preparation plan, historical ledger, DR-0018, remaining-Gate-0 list and DR-0019. Recovered truncated output with bounded reads. Authority, exact scope, approval labels, preconditions, acceptance, stops, zero-paid-compute and external boundaries checked. Remote main verified at the expected base. Engineer/Executor must record their dependent-source traversals before work.

- Executor completed full traversal on 2026-09-20 after explicit sole-writer transfer: governance, EC, prior HC, Executor profile, all named canonical design inputs, research contract, plan, historical progress, DR-0018/remaining Gate-0/DR-0019, plus dataset decision candidate, intervention option audit, research index, existing checker/tests, CI workflow and requirements. Truncated reads were recovered in bounded segments. Verified HEAD and live origin main at the expected base with only the EC bootstrap modified. Scope, evidence labels, stops, no scientific execution, exact seven-file boundary and finite closure reviewed. Adjutant retains coordination; Engineer remains read-only. No other worktree is written.

- Engineer attributed read-only traversal receipt received 2026-09-20: mandatory governance/EC/HC/profile, all 17 named design inputs, research/progress/preparation, DR-0018/remaining/DR-0019, and additional dataset candidate, intervention audit and evaluation protocol fully read at the expected base; truncated reads recovered. No edits, tests, downloads, queries or research execution. Executor owns integration.
- Executor re-traversed the full amended EC on 2026-09-20 for the precisely named temporary validation-dependency boundary; retained all prior mandatory-source traversal and scientific prohibitions. Adjutant confirmed this as necessary ordinary validation preparation under the current authorization, not a scientific environment or scope expansion.
