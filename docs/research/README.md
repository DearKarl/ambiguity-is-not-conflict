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
13. [Simulation output and semantic-operation registry](simulation_output_and_operation_registry.md)
14. [Statistical analysis plan](statistical_analysis_plan.md)
15. [Evaluation protocol](evaluation_protocol.md)
16. [Data and clinical governance](data_governance.md)
17. [Dataset feasibility audit](dataset_feasibility_audit.md)
18. [Dataset decision candidate](dataset_decision_candidate.md)
19. [Execution budget and backbone audit](execution_budget_and_backbone_audit.md)
20. [Estimator formalization and equivalence audit](estimator_formalization_audit.md)
21. [Method-A identification framework](method_a_identification_framework.md)
22. [Baselines and ablations](baselines_and_ablations.md)
23. [Literature matrix](literature_matrix.md)
24. [Novelty and prior-art audit](novelty_audit.md)
25. [Submission strategy](submission_strategy.md)
26. [Gate-0 decision dossier](gate0_decision_dossier.md)
27. [Gate-0 closure audit](gate0_closure_audit.md)
28. [Decision log](decision_log.md)

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

DR-0015 records the Commander's partial `G0-SCOPE A` decision. DR-0016 records
the Commander's selection of `G0-METHOD A` as the sole route and freezes the
paper-faithful-likelihood `PROBVLM-2ADAPTER` and fitted-global-constant
`POINT-2ADAPTER-RECON` scientific interfaces; `POINT-INFONCE` is secondary.
Scientific-supervisor, statistical-owner, and
model-owner co-approval and all other Gate-0 requirements remain open. DR-0015
also rules out the Commander's local workstation for TB-0011's approximately
613-GB conditional simulation-output floor; that number is not the dataset
size or a final upper bound.
