# Pre-Reader Simulation Resource-Feasibility Audit

**Status:** Deterministic pre-execution manifest and hardware-neutral workload
candidate; Gate 0, simulation feasibility, resource approval, and scientific
execution remain open

**Audit date:** 2026-08-29
**Evidence class:** Protocol compilation and deterministic integer/hash
arithmetic under TB-0009; no project random stream, synthetic observation,
DGP, calibration vector, bootstrap, simulation, performance benchmark,
reader/data/model/checkpoint/environment, or hosted/paid compute was accessed
or run

## Executive Decision

The TB-0008 statistical contract is **not resource-qualified**. Its candidate
manifest contains exactly 10,847 reliability cells and 2,438 pre-calibration
`MV-1` cells. The reliability planning family contains `K_plan=4,416` rows;
the `MV-1` planning family contains 2,304 candidate rows. If every `MV-1`
candidate calibrates, the full outer envelope is 1,594,200,000 datasets; if
every outer replication also reaches the complete analysis, the nested
bootstrap envelope is 15,940,405,800,000 analyses. Those are logical work
units, not measured runtime or storage.

TB-0009 found that the prior scenario prose admitted multiple manifest
interpretations. This audit prospectively resolves the grammar before any
simulation, publishes only aggregate counts and hashes, and retains every
fixed scientific and Monte-Carlo threshold. The resulting inventory is
reproducible with:

```bash
python scripts/enumerate_simulation_resource_manifest.py
```

The complete manifest can be streamed to standard output for inspection with
`--manifest reliability`, `--manifest mv1`, or `--manifest all`; it is not a
tracked repository artifact. The aggregate ledger is
[`simulation_resource_manifest_summary.csv`](../../reports/tables/simulation_resource_manifest_summary.csv).

This audit recommends but does not select a resource option. Exact cell
counts, deduplication provenance, manifest hashes, and declared logical
work-unit counts are repository-derived planning facts. They do not establish
implementation correctness, runtime, memory or storage demand, affordability,
hardware availability, or statistical operating performance. `G0-READERS`,
`G0-MV-Q`, and `G0-RESOURCES` remain open and simulation/feasibility-blocked.
Any implementation, benchmark, simulation, environment/account creation,
resource reservation, or hosted/paid/external compute requires a later bounded
brief and the applicable named approvals; Gate-0 approval alone authorizes none
of those actions.

## Facts, Inferences, Assumptions, and Decisions

### Repository-derived facts

- TB-0008 fixes 15 reliability axes, 120,000 outer replications per executed
  cell, 9,999 analysis bootstraps per outer replication, two declared
  quadrature orders, and a calibration/validation construction for `MV-1`.
- The locked axis populations contain eight two-class, five three-class, and
  two four-class axes, with 90--150 included clusters per axis.
- The existing budget supplies no CPU-core-hour, peak-RAM, scratch, wall-time,
  energy, or cost allocation for this simulation. Its GPU ceilings are
  guardrails for the later model route, not an allocation for this job.
- The prior protocol expressly said the fixed grid was not known to fit a
  compute ceiling.

### Audit inferences

- A large exact logical workload does not prove hardware infeasibility, but it
  makes an unbenchmarked feasibility assertion indefensible.
- Calibration admissibility is an outcome of the prohibited later synthetic
  calibration, not a pre-enumeration fact. All syntactically declared `MV-1`
  configurations must therefore remain in the candidate manifest.
- A failed calibration is a failed design cell, never permission to delete the
  cell, reduce the multiplicity family, or search for a favourable subset.
  The successful-path envelope consequently assumes that every candidate
  calibrates.
- Raw-word counts describe generated 64-bit random inputs. They do not imply
  that those words must be retained, and multiplying by eight is not a valid
  storage forecast without a frozen streaming/checkpoint schema.

### Explicit planning assumptions

- The pass-path workload assumes all `MV-1` candidates calibrate and every
  outer replication reaches the complete analysis.
- The `MV-1` bootstrap-index upper bound assumes every screened candidate is
  evaluable in every outer replication. Realized evaluable counts are
  synthetic outcomes and were not generated here.
- Reliability DGP raw-word bounds bracket unresolved per-axis repeat and
  ambiguity-stream consumption. Their bootstrap-index count is exact because
  the frozen included-stratum sizes determine it.
- No throughput, vectorization factor, retry rate, compression ratio, parallel
  efficiency, or hardware availability is assumed.

### Prospective protocol decisions made by this audit

These are compilation decisions, not owner approval of the study or its
resources:

1. Numeric reliability prevalence and missingness lexemes are canonical
   decimal strings: `0.00`, `0.05`, `0.10`, `0.15`, and `0.20` as applicable.
   `MV-1` q zero is `0.00`. Integer `n` and slope strings retain their printed
   integer form.
2. The reliability one-factor family crosses every printed base accuracy with
   common accuracy and every designated-low class; directed confusion is a
   named one-factor level.
3. In the reliability one-factor family, zero missingness has one MCAR
   representative. Each nonzero missingness rate crosses MCAR, reader-
   dependent, and every class-dependent target. The planning family retains
   all mode labels at zero missingness as distinct canonical rows because they
   enter the printed Cartesian family and `K_plan`, despite behaviorally equal
   zero-missingness generation.
4. Planning inequalities filter only the finite levels already printed in the
   factor grid. No continuous or implicit levels are introduced.
5. The fixed `0.50/0.70` ambiguity mixture creates no new cell because the
   schema has no mixture factor and the assignment is within-cell.
6. All three syntactically declared `MV-1` q-distribution configurations enter
   the candidate manifest. The six null pairs are printed explicitly. Every
   unmentioned asymmetric-set factor stays at its reference value.
7. An `MV-1` calibration failure fails the design and cannot remove that row
   from the candidate manifest. A full successful simulation requires every
   candidate to pass calibration before receiving its fixed 120,000 outer
   replications.

## Exact Manifest Reconciliation

### Reliability inventory

For an axis with `K` classes, the clarified one-factor family including its
reference has `17+10K` unique cells. The adversarial family has
`32K(K+2)` cells. The literal planning family has `64(K+2)` cells.

| Classes | Axes | One-factor/axis | Adversarial/axis | Planning/axis | Unique union/axis |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 8 | 37 | 256 | 256 | 537 |
| 3 | 5 | 47 | 480 | 320 | 833 |
| 4 | 2 | 57 | 768 | 384 | 1,193 |

Across axes, one-factor membership is 645, adversarial membership is 5,984,
and planning membership is 4,416. One-factor intersects planning in 159 cells
and adversarial in 39; planning and adversarial do not intersect. Thus:

```math
645+5{,}984+4{,}416-159-39=10{,}847.
```

The enumerator makes 11,135 insertions, removes 288 duplicate insertions, and
retains 198 cells with more than one family provenance. The sorted,
newline-terminated canonical-ID payload has SHA-256
`4823bd2f52547673c173aec89ecd3b3c1d416769ee9abde9e3b71bb1fb0245d6`.

### `MV-1` inventory

- Reference plus one-factor union: 37.
- Null family: six q pairs × two `n` values × three q-distribution
  configurations × three slopes = 108.
- Asymmetric family: two fidelities × two yields × two q alternatives = 8.
- Planning family: `2×2×3×3×2×2×2×2×2×2=2,304`.
- One-factor/planning overlap: 13; one-factor/null overlap: 6; all other
  intersections are empty.

The pre-calibration union is therefore `37+108+8+2,304-13-6=2,438` cells.
Fifty-five use `n=128` and 2,383 use `n=150`. The enumerator makes 2,469
insertions, removes 31 duplicates, and retains 19 multi-family cells. Its
sorted canonical-ID payload has SHA-256
`1cacee1ebe5aa7b43d37a09d39285a9637c6c274012a7335998bb707bd7ee8c7`.

The executable outer-cell count is not an independently selectable number.
Either all 2,438 candidates pass calibration and the complete successful path
is run, or any failed candidate makes the proposed design fail. TB-0009 did
not run calibration and therefore cannot claim success-path eligibility.

### Combined identity

The two candidate manifests contain 13,285 cells and 6,720 planning cells.
Their combined sorted-ID hash is
`4e914a602b418c7fbbcccb1e98d9f09a3d339009e9c2befcdd098e34604695a0`.
The canonical IDs plus terminating newlines occupy exactly 5,423,005 UTF-8
bytes. That number is a manifest-identity fact, not an estimate of simulation
output storage.

## Hardware-Neutral Workload Ledger

| Work unit | Full candidate union | Planning families | Interpretation |
| --- | ---: | ---: | --- |
| Reliability outer datasets | 1,301,640,000 | 529,920,000 | Exact |
| `MV-1` outer datasets | 292,560,000 | 276,480,000 | Successful-path upper envelope |
| Combined outer datasets | 1,594,200,000 | 806,400,000 | Successful-path upper envelope |
| Reliability nested bootstrap analyses | 13,015,098,360,000 | 5,298,670,080,000 | Exact |
| `MV-1` nested bootstrap analyses | 2,925,307,440,000 | 2,764,523,520,000 | Successful-path upper envelope |
| Combined nested bootstrap analyses | 15,940,405,800,000 | 8,063,193,600,000 | Successful-path upper envelope |
| Reliability bootstrap index words | 1,848,511,130,400,000 | 747,189,273,600,000 | Exact fixed cluster selections |
| `MV-1` bootstrap index words | 874,688,522,400,000 | 829,357,056,000,000 | All-candidates-evaluable upper bound |
| Combined bootstrap index words | 2,723,199,652,800,000 | 1,576,546,329,600,000 | Upper bound |
| `MV-1` calibration raw words | 818,057,052,160 | 773,094,113,280 | All candidates reach validation |
| `MV-1` calibration vector evaluations | 453,234,284,036,096 | 428,323,129,786,368 | Full pass-path upper bound |

The byte-reproducible aggregate table is canonical for every detailed logical
count. Per `MV-1` pass cell, the exact vector-evaluation expression is

```math
2\left[(1001+80)(80+2)(2^{20})+2^{22}\right]
=185{,}904{,}136{,}192.
```

Reliability DGP generation is bounded between 1,801,581,600,000 and
2,389,453,200,000 raw words for the full union. `MV-1` DGP generation is at
most 3,411,784,800,000 raw words if every candidate reaches every outer
replication. These counts exclude the separately counted analysis-bootstrap
streams.

No persistent-output byte count follows from TB-0009 alone. TB-0010's
[non-core computational design](noncore_simulation_computational_design.md)
now proposes a normalized uncompressed audit schema and derives a minimum
successful-path payload of approximately 572.5 decimal GB before permutation
payloads, output-registry extensions, aggregate/failure records, container
overhead, scratch, redundancy, or backups. That arithmetic is neither a final
storage upper bound nor an allocation. The exact output registry, CPU-core-
hours, RAM, scratch, wall time, energy, cost, and capacity remain unidentified
without the later locks and separately authorized generic-kernel benchmark.

## Required Later Resource Evidence and Post-Gate-0 Implementation

Gate 0 cannot require core simulation implementation as its own prerequisite:
the repository execution gate forbids that implementation while Gate 0 is
open. Resource qualification must therefore use the now-documented
**non-core** pre-Gate-0 computational design and a separately authorized
workload-equivalent microbenchmark. The design freezes a stage graph, proposed
schema, restart semantics, proof register, workload crosswalk, and acceptance
equations; it does not discharge any proof or resource term. The later
benchmark may measure generic array traversal, deterministic reduction,
index-streaming, and serialization kernels with artificial buffers; it may not
implement or invoke the project RNG, DGP, calibration equations, bootstrap
statistic, promotion gate, or scientific pipeline.

Before benchmark **execution**, its bounded brief and preflight must freeze or
conservatively bound:

- immutable candidate-manifest hashes, family provenance, calibration-failure
  handling, and proof that `K_plan` remains 4,416;
- static per-cell counts for random words, generated ratings and repeats, quadrature,
  calibration vector passes, bootstrap selections/statistic recomputations,
  fixed-effect/leave-one-reader fits, and exact-binomial calls;
- the complete persistent result/output registry, byte widths, metadata
  normalization, checkpoint and restart policy, retention/compression,
  artificial-buffer shapes, batch candidates, system-wide RAM/scratch
  equations, and I/O schema; and
- candidate hardware, load strata, workers, numeric precision, relevant
  numerical-library versions, deterministic chunk/reduction order, retry/
  deadline treatment, independent-stream preservation, exact kernel
  numerators, and the permitted non-project RNG/surrogate boundary.

The output/metric registry and semantic-count ledger must close before timing;
their compiler/harness work, if any, requires the benchmark brief's exact
authorization. The non-core microbenchmark requires statistical, resource,
infrastructure, security, and governance pre-review. Its **outputs** must then
include measured generic-kernel throughput and failures, familywise timing/
tail evidence, a conservative mapping to CPU/RAM/scratch/storage/wall time,
cost/energy where applicable, scaling/dependence uncertainty, failed-cell and
retry cost, contingency, and explicit capacity. It supplies
resource-planning evidence only and cannot validate implementation or operating
performance. Only after Gate 0 freezes may a separate core-implementation brief
realize the exact scientific RNG/DGP/calibration/bootstrap pipeline, freeze its
software and result schema, and undergo code review. A still later execution
brief is required to run that pipeline. No reader, record, model, or checkpoint
is needed or authorized for any simulation stage.

## Finite `G0-RESOURCES` Choice

- **A — unchanged contract:** allocate sufficient resources only after a
  reviewed non-core computational design, workload-equivalent generic-kernel
  benchmark, conservative scaling bound, storage plan, uncertainty/contingency
  calculation, and explicit named-owner approval demonstrate that the complete
  successful path fits. Exact scientific implementation remains post-Gate-0.
- **B — prospective redesign, not selected:** TB-0010 records the static design
  needed to test the unchanged contract under A; it does not instantiate B. If
  the completed registry and later generic benchmark reject A, a separately
  authorized proof-preserving redesign may use canonical
  deduplication, deterministic streaming/batching, algebraically exact
  sufficient statistics, restartable independent-cell parallelism, and
  pre-outer failure-only staging. A calibration failure, a 41/61-node
  quadrature non-estimability failure, or a planning-family cell that fails its
  required above-threshold truth precondition may stop before outer simulation
  with the gates blocked; it cannot promote evidence. Low integrated alpha or
  agreement in a declared false-promotion cell is its intended null condition,
  not a stopping trigger, and that cell must run. Once outer simulation begins,
  the current contract permits no early stop or cell-specific replication
  count. Any change to intervals, Monte-Carlo design, family control, grid, or
  that no-early-stop rule requires a pre-data statistical proof of equal-or-
  stronger guarantees, a dated protocol amendment, and complete re-enumeration
  before results.
- **C — reject or narrow before execution:** reject `MV-1`, replace the reader
  design through a new audit, narrow the primary control family for substantive
  rather than computational reasons, enlarge approved resources, or stop the
  affected route.

No option is selected. Lowering 120,000 or 9,999, dropping hard cells/classes/
axes, loosening coverage/error/precision thresholds, changing 108 or `0.10`,
or pruning after calibration or outer outcomes is prohibited.

## Stop Rule and Permitted Claim

Stop before implementation if owners do not approve an exact resource route;
if the successful-path envelope cannot fit a defensible allocation; if a
redesign lacks output-equivalence or equal-or-stronger statistical proof; or if
storage, restart, numeric determinism, external-compute governance, or
contingency remains unspecified.

The permitted claim is limited to:

> The repository contains a deterministic candidate-cell inventory and
> hardware-neutral logical-workload audit for the proposed pre-reader
> simulation.

It does not establish implementation correctness, calibration admissibility,
runtime, affordability, resource availability, statistical operating
performance, reader reliability, `MV-1` validity, clinical benefit, Gate-0
closure, venue readiness, acceptance, or publication.
