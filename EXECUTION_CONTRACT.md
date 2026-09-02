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

- Contract ID: `EC-2026-09-02-001`
- Task: record the scientific supervisor's five-point Method-A agreement as
  reported by the Commander and reconcile only directly implicated Gate-0
  owner statuses
- Status: `AUTHORIZED / IN PROGRESS`
- Authorized by: Commander, in the current Codex task on 2026-09-02
- Repository: `DearKarl/ambiguity-is-not-conflict`
- Working branch: `codex/record-supervisor-method-a-approval`
- Expected base: remote `main` at
  `34b80e4b86fa0f281fe7252ec38a46d2bed327d0`

### Primary outcome

Create one dated decision record and reconcile the canonical Gate-0 ledger to
show that, according to the Commander's report, the scientific supervisor
agreed to the five items in the private email draft: the ambiguity-versus-
conflict research distinction; Method A's intervention-based scientific
framing; the scientific roles of `PROBVLM-2ADAPTER` and
`POINT-2ADAPTER-RECON` with `POINT-INFONCE` secondary; chest radiography as the
primary validation domain; and NeurIPS 2027 Main Track as a conditional
strategic target. Preserve every approval not covered by those five questions
as open, keep Gate 0 open, and produce a finite next-owner boundary rather than
starting implementation or experiments.

### Authoritative inputs

Read these sources in full before substantive work:

- `AGENTS.md`
- `CODEX_TASK_GOVERNANCE.md`
- this active `EXECUTION_CONTRACT.md`
- `HANDOFF_CONTRACT.md`
- `README.md`
- `docs/roadmap.md`
- `docs/research/README.md`
- `docs/research/research_contract.md`
- `docs/research/scope_charter.md`
- `docs/research/research_question.md`
- `docs/research/method_a_identification_framework.md`
- `docs/research/baselines_and_ablations.md`
- `docs/research/gate0_closure_audit.md`
- `docs/research/gate0_decision_dossier.md`
- `docs/research/decision_log.md`
- `docs/research/submission_strategy.md`
- `scripts/check_repository.py`
- `tests/test_repository_contract.py`
- the Commander's 2026-09-02 statement that the supervisor agreed after being
  shown the five-point email draft; the raw correspondence is not a repository
  input and must not be requested, stored, or committed

### Frozen interpretation of the reported approval

- The evidence is the Commander's report of supervisor agreement. It is
  recorded as user-attested scientific-supervisor approval, not as an
  independently inspected email or signature.
- The approval covers exactly the five scientific-framing questions in the
  draft and the method roles stated in its plan. It does not approve an exact
  clinical task, ontology, intervention implementation, reader protocol,
  statistical estimator, inference settings, model architecture or software,
  hyperparameters, calibration procedure, checkpoint, data access, licence,
  resource budget, breadth benchmark, or experiment.
- The first question supports scientific-supervisor alignment with the
  ambiguity-versus-conflict distinction, but it did not ask the supervisor to
  choose `G0-SCOPE A` over B. The exact A boundary—determinate-conflict
  specificity primary, with natural ambiguity as veto-only observational
  falsification evidence—therefore remains Commander-approved and awaits
  formal scientific-supervisor approval.
- `G0-METHOD A` remains the Commander-selected sole route. The second and third
  questions support scientific-supervisor alignment with the intervention-
  based framework as the primary contribution and with the named method roles;
  they did not ask whether B is inactive. Formal scientific-supervisor approval
  of that sole-route boundary, plus statistical-owner and model-owner approval
  of the exact interface, inference, and executable specification, remain open.
- The primary instrument remains explicitly non-novel and paper-faithful in
  likelihood semantics; the primary comparator remains a same-selection-
  information full-route comparator, not a capacity-isolated mechanism test.
- Chest radiography is the primary validation domain, not approval of the
  provisional pleural-effusion task, any dataset, or any clinical claim.
- NeurIPS 2027 Main Track remains a conditional planning target, not an
  eligibility, acceptance, or publication claim.
- No prior scientific decision, estimand, threshold, seed, resource count,
  kill rule, or Gate-0 boundary changes in this task.
- TB-0011's approximately 613-GB conditional simulation-output core floor
  remains excluded from the Commander's local workstation; it is not the
  medical dataset size, a final upper bound, or an execution target here.

### Allowed actions

- replace this Execution Contract, complete its traversal, and create one new
  linked Handoff Contract;
- add one dated decision record to `docs/research/decision_log.md` with explicit
  fact, inference, assumption, decision, consequences, and reopening fields;
- reconcile only directly implicated approval/status wording in
  `README.md`, `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/research_contract.md`, `docs/research/scope_charter.md`,
  `docs/research/research_question.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`, and
  `docs/research/submission_strategy.md`;
- update `tests/test_repository_contract.py` only if an existing assertion
  directly hard-codes the superseded supervisor-open wording; do not weaken a
  generic governance, scientific-number, or Gate-0 test;
- run deterministic repository checks and read-only Git/GitHub verification;
- obtain independent governance and scientific-scope review;
- commit and push only the dedicated branch, open a pull request, wait for
  green CI, and merge through the standard protected-branch path. If the
  repository still has no eligible independent collaborator, a disclosed
  normal administrator-exempt merge without an explicit override flag is
  allowed; protection settings may not change;
- after the primary merge and green post-merge CI, make one completion-only
  closure change affecting only the two contracts and synchronize it through
  one final pull request.

### Forbidden actions

- no experiment, pilot, simulation, implementation, model execution,
  training, tuning, annotation, clinical contact, reader activity, dataset or
  model access, download, or large artifact;
- no storage or quotation of the supervisor's private correspondence and no
  claim that Codex independently inspected it;
- no expansion of supervisor approval to any question not present in the five-
  point draft, and no substitution for statistical, model, clinical,
  governance, licensing, or infrastructure-owner approval;
- no Gate-0 closure, executable-method freeze, data authorization, task freeze,
  intervention acceptance, clinical-benefit claim, or experiment authorization;
- no change to hypotheses, estimands, endpoints, SESOIs, inference settings,
  sample floors, bootstrap counts or seeds, model route, data route, resource
  floor, promotion rule, stopping rule, or hard Main Track kill;
- no promise of NeurIPS eligibility, acceptance, or publication;
- no unrelated files, credentials, identifiers, restricted content, personal
  correspondence, private screenshots, model weights, or medical data;
- no force push, history rewrite, explicit protection override, branch
  deletion, GitHub-setting change, issue, release, tag, or destructive action.

### Preconditions

- the dedicated worktree is clean and based exactly on the expected remote
  `main` revision;
- the remote is exactly
  `https://github.com/DearKarl/ambiguity-is-not-conflict.git`;
- the branch is dedicated, has no remote counterpart, and has zero divergence
  from the expected base before this contract-only transition;
- this file is the sole repository content mutation before traversal completes;
- the five approval questions and the Commander's reply are sufficiently
  specific to support only the corrected, non-inflated interpretation above.

### Promotion criteria

The primary change may enter remote finalization only when:

1. the full traversal is recorded and the new Handoff Contract is linked;
2. one dated decision record states the provenance and exact five-point scope
   of supervisor approval without storing correspondence;
3. all directly implicated canonical records agree that `G0-SCOPE A` and
   Method A's sole-route boundary remain Commander-approved, while the
   supervisor is aligned only with the ambiguity/conflict distinction,
   intervention-based framework, and named method roles; formal scope/sole-
   route co-approval and all statistical, model, clinical, governance, data,
   resource, and executable-specification decisions remain open where
   applicable;
4. chest radiography and NeurIPS 2027 are recorded only as primary validation
   and conditional strategy choices;
5. Gate 0 remains open and the next boundary is owner reconciliation, not
   experiment execution;
6. independent review finds no approval inflation, scientific drift, hidden
   execution authority, restricted content, or second route;
7. `pytest -q`, `python scripts/check_repository.py --final`, and
   `git diff --check` pass, with exact staged-file, size, and sensitive-content
   review clean;
8. branch, pull-request, and post-merge `main` CI are green before the finite
   contract-only closure.

### Stopping criteria

Stop without publication or scientific execution if:

- the base, remote, branch, worktree cleanliness, or divergence is unexpected;
- the reported approval cannot be mapped unambiguously to the five draft
  questions;
- any edit would require interpreting approval of an unasked Gate-0 item or
  changing a scientific quantity or route;
- another owner's approval is required to resolve a materially different
  scientific or executable choice;
- an unrelated user change, restricted content, large artifact, failing check,
  or unresolved independent-review blocker appears;
- GitHub authentication, protection, merge state, or CI is unexpected.

### Irreversible and external boundaries

Ordinary commits, a push of only the dedicated branch, pull requests, standard
protected merges under the disclosed solo-administrator residual, and GitHub
CI are the only authorized external mutations. No email, data/model access,
download, experiment, publication, GitHub-setting change, force operation, or
branch deletion is authorized.

### Required evidence

- pre- and post-change worktree, branch, remote, base, upstream, and divergence
  verification;
- completed traversal and exact changed-file list;
- dated supervisor-approval decision record with explicit provenance;
- cross-document status audit and remaining-owner inventory;
- independent governance/scientific-scope review;
- full tests, final repository checker, diff, staged-scope, sensitive-content,
  and tracked-size results;
- primary commit, remote branch, pull request, CI, merge, post-merge CI, and
  completion-only closure evidence;
- confirmation that no correspondence, data, model, implementation, experiment,
  simulation, annotation, or large artifact was accessed or created.

### Pre-task traversal record

- Traversal status: `COMPLETE`
- Agent: Codex, Ultra scientific-governance task
- Started: 2026-09-02 (Asia/Shanghai)
- Preconditions observed before contract replacement: the new worktree was
  created from remote `main` at `34b80e4b86fa0f281fe7252ec38a46d2bed327d0`;
  the prior attached worktree was clean but nine commits behind and was not
  reused; the remote URL was exact; and no repository file other than this
  contract was changed in the dedicated worktree.
- Completed: 2026-09-02 (Asia/Shanghai).
- Completion note: `AGENTS.md`, `CODEX_TASK_GOVERNANCE.md`, this contract,
  the prior Handoff Contract, every named canonical document, the repository
  checker, and all repository-contract tests were read in full. The
  Commander's statement was checked against the immediately preceding five-
  question email draft. It supports user-attested supervisor approval of only
  those conceptual-framing and named-role items. Because the draft did not ask
  the supervisor to select `G0-SCOPE A` over B or make Method A the sole route
  with B inactive, it does not support formal supervisor approval of either
  boundary. It also does not support approval of the provisional clinical
  task, ontology, controls, readers, statistics, executable architecture,
  data, governance, resources, breadth identity, or experiments. The exact
  remote/base/branch checks remain valid at `0/0`, and this contract remains
  the only changed repository file. Substantive status reconciliation may now
  proceed only within this contract.
