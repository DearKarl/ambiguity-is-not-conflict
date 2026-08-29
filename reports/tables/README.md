# Generated Tables

Store only governance-permitted generated tables here. Each table is tied to
the Git revision that contains it; the evidence/configuration record, bounded
task brief, compiler or independent arithmetic check, and exact verification
command are listed below. These are protocol-compilation tables, not scientific
results.

| Table | Evidence and frozen configuration | Bounded brief | Compiler or check | Exact command |
| --- | --- | --- | --- | --- |
| `gate0_power_sensitivity.csv` | [`statistical_analysis_plan.md`](../../docs/research/statistical_analysis_plan.md) and the parameters in each row | [`TB-0003`](../../docs/research/task_briefs/TB-0003-gate0-freeze-candidate.md), remediated by [`TB-0004`](../../docs/research/task_briefs/TB-0004-freeze-candidate-review-remediation.md) | Independent `NormalDist` arithmetic in `tests/test_repository_contract.py` | `pytest -q tests/test_repository_contract.py::test_power_table_reproduces_declared_union_bound` |
| `mv1_qualification_yield_sensitivity.csv` | [`reader_measurement_and_mv1_qualification_audit.md`](../../docs/research/reader_measurement_and_mv1_qualification_audit.md) | [`TB-0008`](../../docs/research/task_briefs/TB-0008-reader-measurement-mv1-qualification.md) | `scripts/calculate_mv1_qualification_design.py` | `python scripts/calculate_mv1_qualification_design.py` |
| `simulation_resource_manifest_summary.csv` | [`simulation_resource_feasibility_audit.md`](../../docs/research/simulation_resource_feasibility_audit.md) | [`TB-0009`](../../docs/research/task_briefs/TB-0009-simulation-resource-feasibility.md) | `scripts/enumerate_simulation_resource_manifest.py` | `python scripts/enumerate_simulation_resource_manifest.py` |
| `simulation_metric_registry.csv` | [`simulation_output_and_operation_registry.md`](../../docs/research/simulation_output_and_operation_registry.md) | [`TB-0011`](../../docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md) | `scripts/compile_simulation_semantic_count_ledger.py` | `python scripts/compile_simulation_semantic_count_ledger.py --registry metrics` |
| `simulation_operation_registry.csv` | Same TB-0011 registry/configuration | [`TB-0011`](../../docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md) | `scripts/compile_simulation_semantic_count_ledger.py` | `python scripts/compile_simulation_semantic_count_ledger.py --registry operations` |
| `simulation_semantic_count_ledger_summary.csv` | Same TB-0011 registry/configuration | [`TB-0011`](../../docs/research/task_briefs/TB-0011-output-metric-registry-semantic-count-ledger.md) | `scripts/compile_simulation_semantic_count_ledger.py` | `python scripts/compile_simulation_semantic_count_ledger.py` |

The full 1,242,518-row semantic ledger is intentionally untracked and can be
streamed with `--ledger`; its count and complete-file hash are retained in the
summary. These files contain identifiers, formulas, integer counts, hashes,
and bounds only. They do not contain observations, simulated values, benchmark
timings, resource measurements, or evidence that Gate 0 is closed.
