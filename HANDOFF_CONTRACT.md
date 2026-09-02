# Handoff Contract

This file is the mandatory post-task control record for repository work. It is
paired with `EXECUTION_CONTRACT.md` and is append-only in meaning: a completed
handoff is corrected by a later dated amendment, never silently rewritten to
change historical evidence.

## Contract-last rule

Every bounded repository task must finish by recording:

1. the linked Execution Contract and authority;
2. the delivered outcome and exact changed boundary;
3. facts, decisions, assumptions, and unresolved items separately;
4. validation, independent review, Git, CI, and external-action evidence;
5. deviations, negative results, residual risks, and recovery state; and
6. the exact next permitted decision or task boundary.

A task must not be represented as complete until this record is filled and its
required evidence passes.

Closure uses two finite phases:

1. `READY FOR REMOTE FINALIZATION`: before the primary PR, replace every
   operational placeholder with local evidence or an explicit self-evidence
   boundary. The primary branch may then be pushed, reviewed, checked, and
   merged.
2. `COMPLETE`: after the primary merge and post-merge CI, make one completion-
   only change to this file and `EXECUTION_CONTRACT.md`, recording all primary-
   change and external-governance evidence. Only verification and normal
   synchronization of that closure record may follow.

The closure commit and PR identify themselves through immutable Git/GitHub
history; their own merge revision and post-merge CI are reported in the final
user handoff and are not recursively inserted into this file. No third closure
change is required or allowed.

If the first COMPLETE-state validation exposes a deterministic self-hosting
defect in the governance checker or tests, the contracts must first return to
their pre-completion statuses. A unique remediation ID must be linked here and
in the fully re-traversed Execution Contract before one exceptional closure
may include only the exact governance files named there. The exception remains
single-use, independently reviewed, and inside the same final closure PR.

## Handoff record `HC-2026-09-02-001`

### Identity and status

- Linked Execution Contract: `EC-2026-09-02-001`
- Task: record the scientific supervisor's five-point Method-A agreement as
  reported by the Commander and reconcile directly implicated Gate-0 statuses
- Status: `COMPLETE`
- Prepared by: Codex, Ultra scientific-governance task
- Handoff date: 2026-09-02 (Asia/Shanghai)

### Outcome

The canonical reconciliation records user-attested scientific-supervisor
alignment with the ambiguity/conflict distinction, Method A's intervention-
based scientific framing and named method roles, chest radiography as primary
validation domain, and NeurIPS 2027 Main Track as a conditional target. The
email did not ask the supervisor to select `G0-SCOPE A` over B or approve Method
A as the sole route with B inactive. Those formal co-approvals and all exact
technical, statistical, model, clinical, data, governance, resource, breadth,
and execution decisions remain open. No experiment or implementation is
included.

### Changed boundary

- The delivered primary boundary contains exactly 15 paths:
  `EXECUTION_CONTRACT.md`, `HANDOFF_CONTRACT.md`, `README.md`,
  `docs/roadmap.md`, `docs/research/README.md`,
  `docs/research/research_contract.md`, `docs/research/scope_charter.md`,
  `docs/research/research_question.md`,
  `docs/research/method_a_identification_framework.md`,
  `docs/research/baselines_and_ablations.md`,
  `docs/research/gate0_closure_audit.md`,
  `docs/research/gate0_decision_dossier.md`,
  `docs/research/decision_log.md`,
  `docs/research/submission_strategy.md`, and
  `tests/test_repository_contract.py`.
- The scientific formulas, thresholds, estimands, hypotheses, tasks,
  interventions, model/data routes, resources, and kill rules are unchanged.
- Personal correspondence, raw email, data, models, implementation,
  simulation, annotation, experiment, and GitHub settings are excluded.

### Facts

- The Commander stated on 2026-09-02 that the supervisor agreed after receiving
  the five-question email draft.
- Codex did not inspect, request, quote, or store the private correspondence.
- The five questions cover the ambiguity/conflict distinction, Method-A
  framing, named method roles, chest-radiography validation domain, and the
  conditional NeurIPS 2027 strategy.
- Gate 0 was open before this task and remains open.

### Decisions recorded

- DR-0017 records user-attested supervisor alignment with the ambiguity-versus-
  conflict distinction, Method-A intervention framing, and the named roles of
  `PROBVLM-2ADAPTER`, `POINT-2ADAPTER-RECON`, and secondary `POINT-INFONCE`.
- `G0-SCOPE A` and Method A's sole-route/B-inactive boundary remain Commander-
  approved; formal scientific-supervisor approval of those exact choices is
  still open because neither was asked in the five-question draft.
- Chest radiography remains the primary validation domain without freezing the
  clinical finding, dataset, or access route.
- NeurIPS 2027 Main Track remains a conditional strategic target, not a
  publication prediction.
- The full scientific-supervisor checklist remains open for every unasked
  technical, task, baseline/ablation, staging, and breadth decision.

### Assumptions and unresolved items

- The record relies on the Commander's accurate report of an unqualified
  supervisor agreement to the five questions.
- Formal scientific-supervisor confirmation of the exact `G0-SCOPE A` veto-
  only boundary and Method-A sole-route/B-inactive boundary remains open.
- Statistical-owner and model-owner review of the exact Method-A interface,
  inference package, architecture, software, hyperparameters, and calibration
  remains open.
- The exact task, ontology, interventions, readers, data/access, governance,
  licensing, checkpoints, resources, staging, and breadth benchmark remain
  open.
- Official NeurIPS 2027 eligibility and the final single-track decision remain
  unknown until the call is published and the evidence gates are evaluated.

### Validation and review evidence

- Contract traversal: complete before substantive edits.
- Independent pre-edit governance review: PASS with the guardrail that approval
  is limited to scientific framing and named roles, not the exact interface or
  executable package.
- Final independent governance review: PASS after narrowing the record to
  conceptual/framework/named-role/domain/venue alignment and leaving formal
  `G0-SCOPE A` and sole-route/B-inactive supervisor approvals open.
- Final independent scientific-scope review: PASS; no construct, estimand,
  inference, comparator-role, hard-kill, or Gate-0 drift was found.
- Deterministic local validation: `pytest -q` passed all 51 tests;
  `python scripts/check_repository.py` passed; `git diff --check` passed; the
  changed set is exactly the 15 authorized paths; sensitive-content, binary,
  untracked-file, and greater-than-5-MB artifact scans are clean.
- Primary branch CI, PR CI, and post-merge `main` CI all passed. The completion-
  state two-contract diff must independently pass the same repository, scope,
  sensitive-content, size, and diff checks before its closure commit.

### Git and external evidence

- Base revision: `34b80e4b86fa0f281fe7252ec38a46d2bed327d0`.
- Working branch: `codex/record-supervisor-method-a-approval`.
- Remote: `https://github.com/DearKarl/ambiguity-is-not-conflict.git`.
- Initial divergence: `0/0`; no remote branch of the same name existed.
- Primary commit: `e2ba73390b3943f3c8c0c293adb87d217a811294`.
- Primary branch CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33584111243`
  (`SUCCESS`).
- Primary PR: `https://github.com/DearKarl/ambiguity-is-not-conflict/pull/6`;
  PR CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33584181575`
  (`SUCCESS`).
- Primary merge revision: `8fccd5a016a2924ff42db337013d8e0c43f7ab56`;
  post-merge `main` CI:
  `https://github.com/DearKarl/ambiguity-is-not-conflict/actions/runs/33584248727`
  (`SUCCESS`).
- The merge used the disclosed normal SHA-guarded API path under the known
  single-collaborator review residual, without an explicit override flag,
  force operation, branch deletion, or protection change.
- Completion branch:
  `codex/record-supervisor-method-a-approval-completion`, based exactly on the
  primary merge revision. The closure commit and PR self-identify in Git and
  GitHub and are not recursively inserted here.

### Deviations and negative results

- The attached `codex/sync-neurips-2027-strategy` worktree was clean but nine
  commits behind `origin/main`; it was not reused. A dedicated worktree was
  created from the exact current base.
- A governance review rejected any wording that could imply supervisor approval
  of the exact score, inference, technical interface, or executable package;
  the canonical wording is restricted to framing and named roles.
- An independent scientific review identified that the five-question draft did
  not ask the exact `G0-SCOPE A` or sole-route/B-inactive choices. The record was
  narrowed accordingly rather than inferring those formal approvals.
- No scientific hypothesis was tested and no empirical result was produced.

### Residual risks and recovery

- If the Commander or supervisor later reports a qualification, DR-0017 must be
  amended prospectively and affected status rows reopened.
- User-attested approval is a durable decision input but is not independently
  verified correspondence evidence.
- Every repository change is recoverable through ordinary Git; no destructive,
  forced, or protection-changing operation is authorized.

### Next permitted boundary

No further work is authorized under this completed contract. A new explicit
Commander authorization and fresh linked contracts are required for the next
scientific boundary: explicit supervisor confirmation of the exact scope and
sole-route choices, plus statistical-owner and model-owner review of the exact
Method-A package, followed by the remaining clinical/data/governance/resource
Gate-0 decisions. No experiment follows automatically.
