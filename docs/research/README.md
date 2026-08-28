# Canonical Research Contract

This directory is authoritative for the scientific scope and evidence state of
**Ambiguity Is Not Conflict**. Read the documents in this order:

1. [Research contract](research_contract.md)
2. [Scope charter](scope_charter.md)
3. [Problem taxonomy](problem_taxonomy.md)
4. [Research question and hypotheses](research_question.md)
5. [Atomic task and estimand decision packet](task_estimand_options.md)
6. [Supervisor alignment](supervisor_alignment.md)
7. [Measurement protocol](measurement_protocol.md)
8. [Annotation and intervention protocol](annotation_and_intervention_protocol.md)
9. [Intervention option audit](intervention_option_audit.md)
10. [Reader measurement and MV-1 qualification audit](reader_measurement_and_mv1_qualification_audit.md)
11. [Simulation resource-feasibility audit](simulation_resource_feasibility_audit.md)
12. [Non-core simulation computational design](noncore_simulation_computational_design.md)
13. [Statistical analysis plan](statistical_analysis_plan.md)
14. [Evaluation protocol](evaluation_protocol.md)
15. [Data and clinical governance](data_governance.md)
16. [Dataset feasibility audit](dataset_feasibility_audit.md)
17. [Dataset decision candidate](dataset_decision_candidate.md)
18. [Execution budget and backbone audit](execution_budget_and_backbone_audit.md)
19. [Estimator formalization and equivalence audit](estimator_formalization_audit.md)
20. [Baselines and ablations](baselines_and_ablations.md)
21. [Literature matrix](literature_matrix.md)
22. [Novelty and prior-art audit](novelty_audit.md)
23. [Submission strategy](submission_strategy.md)
24. [Gate-0 decision dossier](gate0_decision_dossier.md)
25. [Gate-0 closure audit](gate0_closure_audit.md)
26. [Decision log](decision_log.md)

The [roadmap](../roadmap.md) turns these documents into evidence gates. A
planned method or experiment is not a result. Any conflict between a task brief
and this directory is resolved in favour of the most recent approved decision
record.

Bounded maintenance and execution briefs are stored under
[`task_briefs/`](task_briefs/). They authorize only their named action and do
not supersede the canonical contract or decision log.

## Evidence Labels

- **literature lead**: relevant work awaiting bibliographic or implementation
  audit;
- **protocol**: a pre-specified design with no scientific result;
- **mechanism-level pilot**: a small diagnostic run that cannot support the
  primary paper claim;
- **completed experiment**: a documented run with saved outputs;
- **promoted research evidence**: a completed experiment that passes its
  pre-specified validity, robustness, and reporting gates.

The repository currently contains **protocol only**.

The Gate-0 freeze candidate is intentionally not executable. Its finite owner
choices are listed in the [decision dossier](gate0_decision_dossier.md) and its
current blockers in the [closure audit](gate0_closure_audit.md); only an
approved dated decision record can change that status.
