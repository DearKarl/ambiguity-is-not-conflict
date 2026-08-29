# Non-Core Simulation Computational Design

**Status:** Static proof-obligation candidate under TB-0010; outer-record and
registry details corrected by TB-0011; no benchmark, implementation,
simulation, resource allocation, or Gate-0 approval

**Design date:** 2026-08-29

**Evidence class:** Protocol and resource-design work only

## Executive Decision

The TB-0009 simulation contract remains **not resource-qualified**. This
record reduces its next computational step to a finite design, but it neither
implements nor times that design. The 13,285 canonical candidate cells,
6,720 planning cells, manifest hashes, 120,000 outer replications per cell,
9,999 analysis bootstraps per outer replication, statistical thresholds,
multiplicity families, failure rules, and no-early-stop rule remain unchanged.

The recommended architecture has one immutable cell catalogue, independent
cell/outer-replication work units, fixed-order within-replication execution,
normalized result dictionaries, one canonical scientific audit record for
every successfully committed outer identity, separate attempt/journal/failure
records for scheduled or retried work, and atomic chunk commits. Streaming, sufficient statistics,
calibration caching, batching, and independent-cell parallelism are admissible
only after the proof obligations below establish identical scientific inputs,
streams, statistics, decisions, and audit outputs. Approximate or merely
highly correlated outputs do not qualify.

TB-0011 found that the prior 56-byte prefix and 312/568-byte records omitted
required per-slot state, a distinct event mask, failure-component retention,
and a deterministic join to separately audited execution history. Its
corrected 72-byte canonical scientific prefix, external 32-byte
execution-attempt sidecar, and 336/600-byte records
raise the conditional all-candidate catalogue/lock/bitmap/core-record floor
from a superseded 572,492,490,610 bytes to **613,093,770,610 bytes**. The new
number still excludes typed static/aggregate/family fields, permutation
payloads, journals, failure detail, owner-blocked extensions, system overhead,
scratch, redundancy, and backups. It is static arithmetic, not a storage
requirement or evidence that any current 1-TB line is available or sufficient.
Exact capacity remains blocked until the owner choices and final storage upper
bound close, a separate generic-kernel benchmark is authorized and run,
conservative scaling is reviewed, and named owners allocate CPU, RAM, scratch,
persistent storage, wall time, and any cost/energy budget.

`G0-READERS`, `G0-MV-Q`, `G0-RESOURCES`, and Gate 0 remain open. `G0-METHOD`
is scientifically prior but owner-blocked: this resource design does not choose
a pointwise instrument or change the paper's method-claim kill.

## Facts, Inferences, Assumptions, and Recommendations

### Repository-derived facts

- Reliability has 10,847 canonical candidates, including 4,416 planning
  cells. Its canonical-ID payload hash is
  `4823bd2f52547673c173aec89ecd3b3c1d416769ee9abde9e3b71bb1fb0245d6`.
- `MV-1` has 2,438 pre-calibration candidates, including 2,304 planning
  cells. Its canonical-ID payload hash is
  `1cacee1ebe5aa7b43d37a09d39285a9637c6c274012a7335998bb707bd7ee8c7`.
- The combined sorted-ID hash is
  `4e914a602b418c7fbbcccb1e98d9f09a3d339009e9c2befcdd098e34604695a0`.
  The newline-terminated canonical JSON payload occupies 5,423,005 bytes.
- The successful-path envelope contains 1,301,640,000 reliability and
  292,560,000 `MV-1` outer datasets. It reaches 15,940,405,800,000 nested
  bootstrap analyses. TB-0009 identifies exact counts or labelled upper bounds
  for bootstrap indices, calibration vector evaluations, and DGP raw words.
- The protocol already fixes seed derivation, random-word conversion,
  canonical traversal order, calibration evaluation order, bootstrap order,
  percentile/max-`t` order statistics, exact-binomial rules, and failure
  semantics. TB-0011 adds a complete static logical field/operation registry
  candidate, but it does not freeze its owner-blocked extensions,
  implementation software, file format, batch size, checkpoint size,
  hardware, or capacity.
- No CPU-core-hour, peak-RAM, scratch, simulation-storage, wall-time, energy,
  or cost allocation is verified. The repository's GPU and restricted-data
  storage ceilings are not simulation allocations.

### Design inferences

- Independent cell and outer-replication seeds permit task scheduling in any
  order, provided execution within each work unit preserves the frozen raw-word
  and reduction order and final records are canonically sorted.
- The scientific contract does not require raw synthetic observations to be
  retained forever. It does require enough versioned seed, permutation,
  algorithm, failure, and result state to reproduce and audit every attempted
  replication. A table of final success counters alone is insufficient.
- Exact integer category counts can potentially replace repeated categorical
  records, and rounded `MV-1` probabilities may admit exact integer sufficient
  statistics. Neither optimization is accepted by this document. Each must
  prove lossless reconstruction and numerical decision identity against the
  later frozen reference implementation.
- Compression ratios, parallel efficiency, cache reuse, vectorization, and
  retry rates cannot be inferred from logical counts. No resource decision may
  credit them before measurement and conformance review.

### Explicit design assumptions

- The byte calculations below use an uncompressed, packed logical payload with
  fixed-width integers and IEEE-754 binary64 slots. They are a comparison
  schema, not an implementation-format selection.
- The successful-path storage envelope assumes all `MV-1` candidates calibrate
  and all 120,000 outer replications produce audit records. A failed
  calibration still produces a retained failure record and fails the proposed
  design; it does not license deletion of that cell.
- A later generic benchmark may use only artificial buffers and non-project
  contents. Dimension matching does not make those buffers scientific data or
  validate the scientific implementation.
- The future timing tolerance calculation assumes timed blocks are exchangeable
  within a declared hardware/load stratum. If this is not defensible, resource
  owners must require a stronger load/stress design rather than treating the
  tolerance bound as valid.

### Recommendations, not approvals

1. Adopt the stage graph, record identities, restart semantics, and proof
   register below as the static candidate for later review.
2. Review and approve or amend TB-0011's exact numeric/output registry; close
   every unresolved extension and finite byte upper bound before authorizing
   any benchmark. An assumed compression ratio or guessed bytes per
   replication cannot replace an unresolved row.
3. Use a later, separately authorized artificial-buffer benchmark to measure
   only generic kernels. Do not create the project RNG, DGP, calibration,
   bootstrap statistic, reliability statistic, or promotion logic while Gate
   0 is open.
4. Resource-qualify only the complete successful path plus conservative
   restart and contingency terms. Resource shortage narrows, redesigns, or
   stops the affected route; it never weakens the statistical contract.

## Immutable Inputs and Non-Negotiable Invariants

The later count compiler, benchmark manifest, implementation, and run must
carry these values as assertions rather than configurable defaults:

| Invariant | Frozen value or rule |
| --- | --- |
| Reliability cells / planning cells | `10,847 / 4,416` |
| `MV-1` cells / planning cells | `2,438 / 2,304`, all pre-calibration |
| Combined cells / planning cells | `13,285 / 6,720` |
| Outer replications | exactly `120,000` per executable pre-enumerated cell |
| Analysis bootstraps | exactly `9,999` per outer replication |
| Reliability analysis root | `20270832` through the frozen HMAC/PCG64DXSM rule |
| `MV-1` analysis root | `20270833` through the frozen HMAC/PCG64DXSM rule |
| `MV-1` calibration root | `20270834` through the frozen HMAC/PCG64DXSM rule |
| Permutation root | `20270835` through the frozen HMAC rule |
| Outer-DGP root | `20270836` through the frozen HMAC/PCG64DXSM rule |
| Calibration sizes | `2^20` common-random candidate vectors and independent `2^22` validation vectors per polarity |
| Quadrature | both 41 and 61 nodes; discrepancy greater than `1e-6` fails |
| `MV-1` yield floor | at least 108 evaluable blocks in each assigned polarity |
| `MV-1` q gate | `L_bal > 0.10`, `L_present > 0`, `L_absent > 0`, all strict |
| Replication policy | no outcome-dependent extension, early stop, cell pruning, or cell-specific count |

Changing any row requires a prospective scientific/statistical amendment and
complete manifest/workload re-enumeration. A resource design cannot make that
change.

## End-to-End Stage Graph

The graph describes semantic stages. It is not executable pseudocode.

```text
immutable protocol + TB-0009 manifests
        |
        v
[S0] catalogue/hash/software-lock verification
        |
        +---------------- reliability ----------------+
        |                                               |
        v                                               v
[R1] fixed permutations/effects                 [M1] fixed permutations/effects
[R2] missingness solve + 41/61 truth             [M2] two-polarity calibration
[R3] pre-outer admissibility                      [M3] independent validation
        |                                               |
        +----------------- pass only -------------------+
                                |
                                v
                     [O1] outer replication j
                                |
                    frozen DGP/raw-word order
                                |
                                v
                     [O2] 9,999 bootstrap analyses
                                |
              reliability percentile or MV max-t result
                                |
                                v
                 [O3] FE/LOO and gate/failure audit
                                |
                                v
                 [O4] atomic per-chunk result commit
                                |
                                v
               [C1] per-cell exact event aggregation
                                |
                                v
              [C2] Clopper--Pearson/family decisions
                                |
                                v
          canonical ordering + hashes + capacity ledger
```

### Stage semantics

| Stage | Required semantic work | Permitted failure consequence |
| --- | --- | --- |
| `S0` | Verify catalogue count, kind counts, family provenance, all three manifest hashes, canonical JSON, roots/tags, and complete software/algorithm lock. | Stop before any scientific work. A mismatch is not repairable by accepting a new hash. |
| `R1--R3` | Construct the frozen finite-roster permutations/effects; solve missingness intercepts; calculate 41/61-node integrated alpha/agreement truths; apply all bracket, residual, and quadrature checks. | Retain the exact failed-cell record and fail the design. It cannot become a manifest filter. |
| `M1--M3` | Construct fixed panels/effects; evaluate the frozen common-random calibration sequence for both polarities; validate on the independent vector stream. | Any inadmissible shape, bracket, monotonicity, residual, or validation failure fails the complete design. |
| `O1` | For each canonical `(cell,j)`, use only its named seed and consume every raw word in the frozen order, including latent/missing branches. | Infrastructure interruption is retriable with the same identity. Scientific non-estimability is retained and counted. |
| `O2` | Use a separate analysis stream; generate every bootstrap selection; recompute the complete statistic; retain undefined resamples rather than redraw them. | Any undefined/non-finite value follows the frozen failure rule. No replacement or smaller bootstrap set. |
| `O3` | Write all primary components, exact failure class, interval/gate state, and required reliability or FE/LOO diagnostics. | A veto or failed gate is an outcome, not a reason to omit the replication. |
| `O4` | Commit a complete, checksummed chunk and completion bitmap atomically. | Discard or quarantine only an incomplete temporary chunk; never double-count a committed identity. |
| `C1--C2` | Aggregate all fixed replications, calculate exact-binomial intervals, planning-family minima/family rules, and a complete failed-cell inventory. | No partial family may be promoted. A missing member fails the relevant design claim. |

## Workload-to-Kernel Crosswalk

Let `C_R` and `C_M` denote the frozen reliability and `MV-1` manifests,
`R=120,000`, and `B=9,999`. For cell `c`, let `N_c` be its included cluster or
candidate count, `K_c` its class count where applicable, `A_c` its assigned
rating count, `D_c` its repeat count, `I_c` its bootstrap selections,
`V_cal,c` its candidate/solve-vector evaluations, and `V_val,c` its independent
validation-vector evaluations. A later count-only
compiler must emit every symbol per canonical cell and reconcile its sums with
the TB-0009 aggregate table before a benchmark may run.
The manifest symbol `C_R` is never a completion flag: per-cell exact-`R`
completion is denoted `I_complete,c`, after bitmap, unique-record, and integrity
checks.

| Kernel class | Exact semantic workload | Future artificial-buffer shape; no project values |
| --- | --- | --- |
| Catalogue/HMAC | Every cell hash, required seed identity, permutation tag, and final record hash; the exact call count must be compiled. | Artificial ASCII messages at the observed minimum/median/maximum canonical byte lengths; ordinal lists with the same lengths as the frozen roster/item lists. |
| Raw-word production | TB-0009's DGP lower/upper counts; 2,723,199,652,800,000 combined bootstrap words (upper bound); and alternative-specific calibration counts. Materialization produces 818,057,052,160 calibration words once; full replay produces `32 sum_c(V_cal,c+V_val,c) = 14,503,497,089,155,072` words. | The current generic-only boundary does not authorize PCG64DXSM timing. A later brief must either authorize library-level engine timing on unrelated seeds/artificial outputs or supply a proved conservative non-project surrogate. Otherwise runtime remains unresolved and `G0-RESOURCES` stops. |
| Raw word to open-unit/index formation | One raw-to-open-unit conversion per consumed DGP/calibration/bootstrap word and one `floor(n_h U)` formation per bootstrap word. Counts must remain separate when calibration materializes raw words but reconverts or caches open-unit values. | Pre-filled counter-pattern `uint64` buffers and artificial stratum sizes; fixed shift/add/scale/floor operations only. No project seed, stream, DGP, or statistic. |
| Generic inverse-CDF/special function | Normal/beta transform events and exact-binomial quantile calls from the later static ledger. The reference lock must enumerate finite extrema for every open-unit input, beta/normal parameter, `(x,N,alpha)` class, and multiplicity-adjusted alpha, including `alpha=0.05/4,416`; a beta shape that can approach zero without a frozen positive bound leaves this row unresolved. | Artificial inputs spanning the complete reviewed numerical domain: open-unit tails, smallest/largest positive beta shapes, extreme/central `(x,N)`, adjusted-alpha tails, boundary/nonconvergence cases, and their enforced failure/deadline cost. A convenient interior grid is insufficient. No DGP or gate calculation. |
| Probability construction | The static ledger must count separately every `log`, `exp`, `expit`, normalization, and 2/3/4-class softmax evaluation: reliability first/repeat ratings; every assignment-weighted point in each 100-iteration missingness solve; every 41/61-node quadrature probability evaluation; all ten sibling/reader coverage and state probabilities in every `MV-1` candidate/validation vector evaluation; and every outer/repeat `MV-1` rating. | Generic artificial logit arrays at the actual scalar/vector lengths and `K in {2,3,4}`; separately timed stable log/exp/expit/log-sum-exp/softmax kernels. Inputs are unrelated bounded patterns, never project factors or equations. |
| Root/quadrature control | Exact counts of reliability bracket checks and 100 midpoint iterations, 41/61-node passes, and `MV-1` scan/endpoint/midpoint/validation control events, compiled without evaluating them. | Artificial bounded scalar residual arrays and fixed iteration/node counts; control-flow/reduction only, with no project residual, calibration, or truth calculation. |
| Categorical lookup | One cumulative lookup for every first/repeat category, coverage, state, and other declared categorical/Bernoulli DGP event after its probability vector is constructed; count supplied by the static ledger. | Artificial cumulative-probability matrices with `K in {2,3,4}` and generic rows matching the declared rating dimensions. Preformed probabilities time lookup only and cannot substitute for the probability-construction row. |
| Calibration-shaped transform/reduce | `sum_c(V_cal,c+V_val,c)`; TB-0009 gives the successful-path candidate and validation totals separately. Probability construction, inverse transforms, and raw-word costs remain in their separate rows. | Thirty-two-channel artificial arrays with `2^20` rows and a separate `2^22` validation shape; fixed affine/clip/reduce operations unrelated to the calibration equations. |
| Reliability indexed reduction | `|C_R| R (B+1)` alpha recomputation events, with `B N_c` bootstrap selections per outer replication, plus one disjoint point-descriptive assembly per committed record for macro/class agreement, prevalence, and missingness summaries. | Artificial cluster tables with actual frozen `N_c` values in the range 90--150, `K in {2,3,4}`, and generic 3/5/10-rating layouts; pre-filled indices only. |
| `MV-1` indexed reduction | At most `|C_M| R (B+1)` q/studentizer recomputation events and the TB-0009 upper-bound selection count. | Artificial two-stratum tables at boundary sizes `0, 107, 108, 128, 150, 300`; pre-filled indices; one- and three-component fixed-order reductions. |
| Fixed-effect/LOO-shaped work | At most `|C_M|R` FE fits and `10|C_M|R` leave-one-reader reductions on the complete path. | Generic matrices up to 3,000 rows and 320 columns at declared condition-number strata; ten generic delete-one vector reductions. No project design matrix or veto. |
| Order selection | One 9,999-value percentile selection per reliability interval and one 9,999-row, three-component maximum/critical-value selection per `MV-1` outer analysis, plus any registry-approved diagnostics. | Artificial binary64 arrays of length 9,999 with fixed duplicate/non-finite stress cases. |
| Exact-binomial-shaped scalar work | One approved interval call per final Monte-Carlo event probability; distinct `x/R` proportion divisions and the reliability `sum(undefined)/(RB)` division remain separate exact-once units. The exact metric registry determines all counts. | Artificial integer `(x,N)` pairs including `0`, `N`, threshold-adjacent, and central cases; no project event labels. |
| Serialization/checkpoint | One catalogue, one static cell record per cell, one canonical scientific record per successfully committed outer identity, separately unresolved execution-attempt/journal/failure records for scheduled and retried work, aggregate/extension records, and replay checks. | Artificial records of the exact proposed widths and chunk candidates; temporary-write, checksum, and readback only. |

The crosswalk separates **semantic units** from processor instructions. A
reduction event cannot be counted again as every internal arithmetic operation;
each benchmark row must define its numerator exactly. Conversely, one fast
array traversal cannot stand in for raw-word production, index formation,
inverse CDF, probability construction, root/quadrature control, categorical
lookup, sorting, small linear algebra, or serialization. Preformed cumulative
probabilities cannot cover logit/expit/softmax work whose inputs change with
item, reader, latent state, trial mean, or trial intercept. Missing rows or an
unreconciled probability-construction count stop resource qualification. The
compiler must produce a separate workload for every replay/materialization/
conversion-cache candidate; it may not combine the lowest cost from
incompatible alternatives.

## Calibration Buffer and Cache Design

Each `MV-1` calibration vector contains exactly 32 base random words: `Q`, one
shared patient-state word, and three words for each of ten sibling/reader
ratings. Two implementation candidates may later be compared:

- **deterministic replay:** regenerate the identical base-word vector from the
  frozen seed for every complete trial evaluation; and
- **raw-buffer materialization:** write the `2^20 x 32` raw-word matrix once per
  cell/polarity, verify its digest, and reuse it without mutation.

The latter raw payload is exactly 268,435,456 bytes. It may be processed in
tiles; a second full transformed copy is not assumed. Across every candidate,
two polarities, and both base/validation streams, materialization produces the
TB-0009 total of 818,057,052,160 calibration raw words. Regenerating 32 words
for every declared vector evaluation instead produces exactly
5,948,932,358,144 raw words per successful cell,
14,503,497,089,155,072 for all 2,438 candidates, or
13,706,340,153,163,776 for the 2,304 planning cells. The independent `2^22`
validation stream is used once and may be tiled without persistent retention.
Neither candidate is selected. A hybrid that materializes open-unit or
transformed channels must declare separate production, conversion, inverse-
transform, RAM, and scratch counts. A later implementation review must show
identical raw-word transcripts and bitwise reference results, then a valid
later benchmark/capacity decision may choose among complete alternatives
rather than mixing their cheapest terms.

Every complete named calibration mean/endpoint/midpoint evaluation has a
fixed-order reduction and integrity digest, but these are trace/conformance
boundaries, not durable restart checkpoints. Under this candidate the atomic
restart unit is one complete polarity: interruption replays the polarity from
its beginning. The retained bisection endpoint may be cached only within that
live polarity attempt exactly as prescribed; no cross-attempt, cross-cell,
cross-polarity, approximate, interpolation, or outcome-selected reuse is
permitted. A future smaller restart unit requires a separately reviewed,
typed accumulator/checkpoint schema and new semantic/storage counts before it
can amend this rule.

## Proposed Result and Checkpoint Schema

### Encoding rules

- Multibyte fixed-width fields use one declared byte order; the proposal uses
  little-endian. Binary64 values retain their exact bit patterns. TB-0011
  supersedes the earlier NaN-sentinel proposal: every core slot has an
  independent two-bit state, every non-`VALUE` payload is canonical zero, and
  NaN never encodes inapplicability, scientific undefinedness, or reachability.
- Dictionaries normalize repeated cell JSON, permutations, software strings,
  algorithm identities, and metric names. Every outer record points to those
  immutable dictionaries. This satisfies “write to the result” without
  repeating megabytes of identical metadata in every row.
- A schema version, complete field registry, content digest, record count, and
  byte count precede every file. Optional, implicit, or silently added fields
  are prohibited.
- Compression may be an additional copy only. Capacity approval uses the
  uncompressed bound until the compressor, version, dictionary, worst-case
  expansion, random-access/restart behavior, and lossless round-trip have been
  reviewed.

### Logical records

| Record | Packed payload | Required content |
| --- | ---: | --- |
| Cell catalogue | `42 + L_i` bytes per cell | `uint32` index, `uint8` kind, `uint8` family mask, 32-byte cell hash, `uint32 L_i`, and exact canonical JSON bytes. |
| Cell-static lock | 112 bytes per cell | `uint32` cell index; two `uint16` status/failure codes; `uint32 R`; `uint32 B`; and software, permutation-payload, and algorithm-lock SHA-256 values. |
| Identifier dictionary | `10 + sum_q(2 + L_q)` bytes per dictionary | `uint16` dictionary ID, `uint32` entry count, `uint32` payload-byte count, then `uint16` byte length and exact UTF-8 bytes for every identifier. An identifier exceeding 65,535 bytes fails this schema. |
| Permutation dictionary | `12 + T_p + 2L_p` bytes per permutation | `uint32` cell index, `uint16` tag byte length, `uint32` list length, `uint16` identifier-dictionary ID, exact UTF-8 tag bytes, and ordered `uint16` indices into that dictionary. Lists exceeding 65,535 elements fail this schema. |
| Reliability outer audit | 336 bytes | 72-byte common prefix, eight-byte two-bit state mask, and 32 typed eight-byte payload slots. |
| `MV-1` outer audit | 600 bytes | 72-byte common prefix, 16-byte two-bit state mask, and 64 typed eight-byte payload slots. |
| Extension scalar | 20 bytes | Cell index, outer index, metric code, type/state codes, and one 64-bit payload. |
| Completion bitmap | 15,000 bytes per manifest candidate cell | One bit for each of exactly 120,000 outer identities; the bitmap is all zero with a separately persisted static/calibration failure when outer work never begins. |
| Chunk journal | 52 bytes per committed chunk | Cell index, first outer index, count, record count, state/reserved bytes, and 32-byte payload digest. |
| Failure detail | `28 + L_f` bytes | Cell/outer identity; stage/reason/severity/state/reserved codes; `uint32` software- and algorithm-lock dictionary references; `uint32` message byte count; and canonical UTF-8 detail. |
| Execution attempt | 32 bytes per scheduled atomic attempt | First deterministic join key, scheduled identity count, work-unit kind, attempt ordinal, infrastructure outcome, registry version, failure/journal references, and canonical zero reserved word; stored in a separately content-digested logical stream. |
| Cell aggregate | `16 + ceil(2F_c/8) + P_c` bytes | `U32` cell index, `U16` registry version, `ENUM16` status, `U32` aggregate-field count `F_c`, and `U32` payload-byte count `P_c`, followed by one two-bit state per registry field and the exact ordered typed payload. `F_c`/`P_c` remain registry-format blockers. |

The corrected 72-byte outer prefix contains cell and zero-based outer indices,
scientific status and primary failure, distinct 64-bit failure-component and
event masks, undefined-bootstrap count, numeric-registry version, a
deterministic 64-bit key joining the external execution-attempt stream, and a
32-byte payload digest. Mutable attempt/retry/infrastructure fields are not
part of the canonical scientific record. Every core slot separately carries
`VALUE/INAPPLICABLE/SCIENTIFIC_UNDEFINED/NOT_REACHED`; a non-value payload is
canonical zero and NaN never encodes state. The complete fixed slot,
cell-static, aggregate, family, and owner-blocked extension definitions live in
the [TB-0011 registry](simulation_output_and_operation_registry.md).

Thirty-two and 64 slots are proposed fixed cores, not permission to omit a
required result. Before a benchmark, the statistical/scientific owners must
approve or amend every slot and close every extension occurrence. Under the
current contract, observed-reader hierarchical/Gwet/ordinal/adjudication
sensitivities are not multiplied across simulated outer records; adding them
requires a prospective canonical amendment. Exact repeat outputs,
permutations, aggregate/family widths, failure-detail/journal bounds, and
software/container overhead remain explicit blockers.

### Static byte arithmetic

The sum of canonical JSON lengths without their 13,285 newline delimiters is
5,409,720 bytes. The proposed catalogue is therefore exactly

```math
S_{catalogue}=5{,}409{,}720+42(13{,}285)=5{,}967{,}690\ \text{bytes}.
```

The corrected conditional all-candidate core audit payload before the
completion bitmap is

```math
S_{core}=S_{catalogue}+112(13{,}285)
 +336(1{,}301{,}640{,}000)+600(292{,}560{,}000)
 =612{,}894{,}495{,}610\ \text{bytes}.
```

The all-cells completion bitmap adds 199,275,000 bytes. If `b` outer records
form a chunk, the journal adds

```math
S_{journal}(b)=52(13{,}285)\left\lceil\frac{120{,}000}{b}\right\rceil.
```

Thus the conditional core floor is

```math
S_{floor}(b)=613{,}093{,}770{,}610+S_{journal}(b)
 +S_{perm}+S_{static}+S_{aggregate}+S_{family}
 +S_{attempt}+S_{failure}+S_{extension}+S_{format}.
```

The prior 572,492,490,610-byte value is superseded; its exact correction is
40,601,280,000 bytes under the same conditional path. This formula is
intentionally not collapsed to a capacity claim. Every final term must receive
a finite reviewed upper bound; `S_perm` includes every identifier dictionary
and permutation row, and `S_attempt` contains every mandatory 32-byte initial
or retry work-unit sidecar record. Any retained calibration evaluation digest,
whole-trace transcript, or raw-buffer verification metadata is included in
`S_extension`; none may be silently folded into the core floor or assigned
zero. Redundancy, backup, and two simultaneously live atomic
chunk copies are additional. The existing 1-TB restricted-working-storage
proposal is neither assigned to this simulation nor silently shared with it.

## Streaming, Batching, and Sufficient-Statistic Obligations

### Reference order

One post-Gate-0 implementation must be named the conformance reference. For
every sentinel cell/replication it writes the complete raw-word transcript
digest, permutation payload, ordered bootstrap indices or their digest,
intermediate statistic bits, final slots, flags, and failure code. An optimized
path passes only with exact equality at every declared checkpoint. Numerical
tolerance is insufficient at a strict decision boundary.

### Reliability candidate optimization

Cluster-level categorical/coincidence contributions may be cached because the
bootstrap resamples complete clusters. Before adoption, an algebraic proof
must show that multiplying each cluster contribution by its bootstrap
multiplicity reproduces, for every missingness pattern and class count, the
same nominal Krippendorff alpha, macro agreement, class-specific agreement,
undefined state, and percentile input as explicit index-order resampling.
Integer/rational accumulation is preferred where it preserves the exact
estimand. Any binary64 conversion and division order is part of the reference.

### `MV-1` candidate optimization

Rounded probabilities may be stored as exact integer cents, making five-reader
panel means and q differences rational. A multiplicity-based bootstrap may use
integer sums, squared sums, and polarity counts only if it reconstructs every
q estimate, sample variance, standard error, studentized component, maximum,
critical value, and lower bound with the reference bits and failure state.
FE and leave-one-reader outputs remain separate obligations; summary q counters
cannot reconstruct the fixed-effect design.

### Batching and parallelism

- Each worker receives immutable `(cell index, outer-index interval, software
  lock)` identities. Every outer replication initializes its own frozen stream;
  a vectorized generator spanning two outer identities is prohibited unless it
  proves identical per-identity raw words.
- Batching may change memory layout, never traversal or reduction order.
  Parallel reductions across clusters/bootstrap replicates are prohibited
  unless the later reference defines an exact associative representation or
  bitwise deterministic merge order.
- Cell and outer work may finish out of order. Final scientific records are
  sorted by catalogue index and outer index; aggregate counts follow that same
  canonical order.
- The full planning family and every non-planning diagnostic/null cell remain
  present. Scheduling priority cannot become outcome-based pruning.

## Peak RAM, Scratch, and Restart Equations

For `p` concurrent workers, let `s_w` be worker `w`'s simultaneously active
stage and let `Q` be the explicitly permitted set of stage-concurrency states.
For proposed worker-specific outer batches `b_{o,w}` and bootstrap tiles
`b_{b,w}`, the later design ledger must instantiate the **system-wide** bound:

```math
M_{peak,system}=M_{shared}+M_{OS,reserve}
 +\max_{(s_1,\ldots,s_p)\in Q}
   \sum_{w=1}^{p}
   \left[M_{s_w}(b_{o,w},b_{b,w})+M_{output,w}(b_{o,w})\right].
```

Every term is the sum of simultaneously live declared buffers, with element
type and shape—not resident-set size guessed from array payload alone. The
calibration materialization candidate contributes 268,435,456 raw-buffer bytes
**per concurrent calibration worker**, plus its tile and reduction state. The
reference bootstrap design must budget, per concurrent outer worker, both a
raw/index tile and every statistic/order buffer; an optimized multiplicity
design receives no credit until its equivalence proof passes. If the scheduler
limits calibration, FE, sorting, or writers to fewer than `p` workers, that
limit is part of `Q` and requires an enforceable queue/back-pressure proof.

For worker-specific maximum chunk payloads `S_chunk,w`, system-wide atomic
write/readback scratch requires at least

```math
S_{scratch,system}\ge S_{shared}
 +\max_{(s_1,\ldots,s_p)\in Q}\sum_{w=1}^{p}
 \left[S_{cal,w}+2S_{chunk,w}+S_{sort,w}+S_{runtime,temp,w}\right]
 +S_{journal/cache}+S_{filesystem,reserve}.
```

The factor two applies to every simultaneous writer and covers a temporary and
verified committed chunk. With `p` unconstrained writers, at least `p` such
pairs are budgeted; with `q` concurrent calibration workers, `q` calibration
scratch buffers are budgeted. Filesystem copy-on-write or compression is not
assumed. A later environment audit must measure system and per-process peak
RSS, anonymous memory, mapped files, allocator high-water mark, scratch high-
water mark, write queue, and final bytes separately.

Restart occurs only at an atomic outer-chunk boundary or an entire completed
calibration-polarity boundary; internal named evaluation digests are not
durable restart points. On recovery:

1. verify catalogue, software, algorithm, and permutation digests;
2. verify every committed chunk's identity, byte count, record count, and
   digest;
3. reconcile the completion bitmap exactly with canonical outer indices;
4. delete or quarantine only an incomplete temporary chunk, then replay its
   full identity range; and
5. stop on a completed-identity canonical-record hash mismatch or duplicate
   with unequal canonical bytes; and
6. reconcile the separately content-digested execution-attempt stream against
   scheduled work-unit ranges, contiguous attempt ordinals, failure details,
   journals, and completion bits.

Replayed canonical scientific records—header, state mask, event/failure masks,
and typed payload—must be byte-identical to the no-interruption reference. The
execution-attempt sidecar, journal, failure detail, and their file digests are
expected to differ across retry schedules and are excluded from that equality
domain; they must instead exactly match the injected execution history. The
sidecar uses the combined-manifest global cell index, range-aware join keys,
frozen work-unit/outcome enums, zero-based contiguous `U16` attempt ordinals,
and explicit reference partition rules in TB-0011. Retries count toward
resource use. No checkpoint/restart rule may reclassify a scientific failure
as an infrastructure failure or vice versa.
Range reconciliation uses same-cell containment
`first_join_key <= outer_join_key < first_join_key + identity_count`, never
key equality alone. P9 also requires atomic sidecar recovery: every scheduled
attempt has exactly one terminal outcome and no committed range lacks its
sidecar/journal. Whole-polarity replay is the only `MV-1` calibration restart
unit in this candidate; internal evaluation digests are integrity evidence.

## Proof-Obligation Register

No obligation is discharged by this static record.

| ID | Obligation | Passing evidence required later | Failure consequence |
| --- | --- | --- | --- |
| `P0-MANIFEST` | Catalogue identity | Counts, all three hashes, family membership, `K_plan=4,416`, and byte-identical canonical JSON reconcile with TB-0009. | Stop; complete re-enumeration and protocol review. |
| `P1-STREAM` | Raw-word identity | Reference versus tiled/batched transcript digests match for boundary and adversarial sentinel cells, including latent branches and retries. | Use the reference path or stop. |
| `P2-PERM` | Permutation identity | Every tag, input identifier dictionary, output ordering, and digest round-trips exactly. | Stop before DGP/analysis. |
| `P3-CAL` | Calibration cache/replay identity | All 1,001 scan points, 80 outer midpoints, endpoint-plus-80 inner evaluations, residuals, monotonicity checks, and validation bits match. | Use full reference evaluation or fail the cell/design. |
| `P4-REL-SUFF` | Reliability sufficient statistics | Exhaustive small categorical/missingness cases and frozen sentinel cases match explicit resampling for all outputs/failures. | Retain explicit index-order reference. |
| `P5-MV-SUFF` | `MV-1` sufficient statistics | Exact q/variance/studentizer/max-`t`/order-statistic equality, including zero/non-finite SE cases. | Retain explicit index-order reference. |
| `P6-FE-LOO` | FE/LOO design identity | Matrix, constraints, `1e-12` cutoff, coefficients, rank/failure state, and all ten omissions match the frozen reference. | No optimized FE/LOO path; unresolved failure blocks `MV-1`. |
| `P7-REDUCE` | Floating-point order | Every parallel/vector path has a declared exact representation or merge order and bitwise conformance evidence. | Single-thread/fixed-order reference or stop. |
| `P8-SCHEMA` | Lossless reconstruction | Every reported statistic, event, gate, failure, seed, permutation, and software identity reconstructs and round-trips from the uncompressed records. | Enlarge schema and recalculate capacity. Counters alone fail. |
| `P9-RESTART` | Atomic restart | Forced interruption at every checkpoint class produces byte-identical canonical scientific records and record digests, no missing/duplicate identity, and an execution-history-sensitive sidecar/journal/failure stream exactly matching the injected retries. Whole output files are not expected to match across retry schedules. | Reduce checkpoint scope or stop. |
| `P10-FAMILY` | Complete family aggregation | All cells and fixed replications contribute once; CP limits, minima, union rule, and strict inequalities match independent reference calculations. | No operating-characteristic claim. |
| `P11-RESOURCE` | Bound completeness | Every kernel—including raw-word/index formation and every log/exp/expit/softmax/root/quadrature event—plus byte, RAM, scratch, I/O, restart, scheduler, and contingency term maps exactly once to an allocation. | `G0-RESOURCES` remains open. |

## Future Generic-Kernel Benchmark Contract

The benchmark is a later task, not authorized here. Its brief must name exact
hardware, load strata, worker counts, thread/affinity settings, software and
numerical-library versions, artificial-buffer generator, buffer digests,
kernel numerator, repetitions, logs, and output paths. It must not import or
call project scientific code.

Before timing, enumerate all `H` kernel/shape/hardware/load strata. For stratum
`k`, measure seconds per explicitly declared semantic unit. A proposed tail
diagnostic is 299 timed blocks after warm-up. Under independent exchangeable
blocks, their maximum is a one-sided nonparametric 95% upper tolerance limit
for the 99th runtime percentile because

```math
1-0.99^{299}>0.95.
```

This limit describes a percentile only. It is **not** an upper bound on every
future unit, the mean, or `W_k` units, and it may not be multiplied by the
workload to resource-qualify the run. The exchangeability assumption, clock
resolution, thermal/load drift, process startup, dependence, and outliers must
be audited. Failed, timed-out, or interrupted blocks are retained as costs;
they are not removed to improve throughput.

A finite capacity calculation requires a separately frozen support/deadline
contract. For each pre-enumerated stratum, a pilot may propose a per-attempt
hard deadline `d_k` and maximum number of attempts `a_k`, but an independent
qualification phase must freeze and test them. Each attempt is forcibly
terminated at `d_k` and records the full `d_k` cost; a lifecycle requiring more
than `a_k` attempts rejects the resource candidate. During later execution,
every timed-out attempt counts and exhausting `a_k` stops the complete run
rather than dropping the unit. Define one qualification observation `t_ki` as
the complete
per-semantic-unit lifecycle cost, including every allowed failed attempt,
restart, and successful final attempt, so `0 <= t_ki <= D_k=a_k d_k`. With
that support, a simultaneous 95% distribution-free upper confidence bound on
stratum mean lifecycle costs may use Bonferroni allocation `alpha_k=0.05/H`
and Hoeffding's bound

```math
\mu_k^U=\min\left\{D_k,
 \bar t_k+D_k\sqrt{\frac{\log(H/0.05)}{2n_k}}\right\}.
```

This is an expected-work planning bound under independent observations within
each declared stratum; it is not a hard completion-time guarantee. The
familywise expected worker-time bound is

```math
T_{worker,mean}^{U}=\sum_k W_k\mu_k^U.
```

The finite hard worker-time envelope, including the maximum allowed attempts,
is instead

```math
T_{worker,hard}^{U}=\sum_k W_k a_k d_k+T_{fixed,hard}^{U}.
```

Without a reviewed parallel DAG/critical-path and scheduler proof, the only
valid hard wall bound gives no speedup:

```math
T_{wall,hard}^{U}\le T_{worker,hard}^{U}
 +T_{I/O,hard}^{U}+T_{restart,hard}^{U}+T_{scheduler,hard}^{U}.
```

A later approved `p`-worker design may replace that bound with a proved
work/critical-path inequality plus separately bounded I/O, restart, queue, and
scheduler terms. Measured efficiency alone is not a hard wall-time bound.
Every deadline, retry, I/O, scheduler, and fixed-overhead term must have an
enforceable failure consequence. If the hard envelope is too conservative to
fit and owners instead accept a probabilistic service level, that level,
familywise error, tail model, dependence/stress assumptions, and contingency
must be an explicit `G0-RESOURCES` decision; it cannot be inferred from the
99th-percentile diagnostic or the mean bound.

Resource acceptance requires all of the following, jointly:

1. every workload row maps once to a measured generic kernel or a separately
   bounded fixed overhead;
2. all timing, deadline/support, RAM, scratch, persistent-byte, I/O, restart,
   scheduling, wall-time, and cost/energy terms have reviewed finite bounds;
3. artificial-buffer dimensions, access patterns, and numerical parameter
   domains conservatively cover every project shape and inverse/special-
   function tail, shape, alpha, and boundary/failure case, while contents
   contain no project DGP or statistic; an open or not finitely covered domain
   stops resource qualification;
4. the uncompressed schema plus redundancy/backup fits an explicitly assigned
   storage allocation, and peak RAM/scratch fit simultaneously;
5. the complete successful path plus failed-cell/retry and owner-approved
   contingency fits the explicit wall/cost allocation under either the hard
   envelope or an explicitly approved familywise probabilistic service level;
   and
6. statistical, resource, infrastructure, security, and governance owners
   approve the mapping and its limitations.

If no valid resource bound fits, owners may allocate more resources,
commission a prospective proof-preserving redesign and re-enumeration, narrow
the substantive route, or stop. They may not reduce `R`, `B`, the grid,
hard cells, thresholds, output registry, or failure records to fit.

## Remaining Unknowns and Finite Next Actions

### Still unknown

- owner approval of TB-0011's logical registry, reliability truth reference,
  repeat/ambiguity domains, `MV-1` truth/trace depth, and failure precedence;
- exact permutation/identifier payload, typed static/aggregate/family fields, failure-detail
  bound, container overhead, redundancy, retention, and backup policy;
- the reference scientific algorithms, software versions, inverse-CDF and
  linear-algebra implementations, numerical conformance, and proof results;
- candidate CPU/GPU architecture, threads/workers, RAM, scratch, persistent
  storage, wall time, cost/energy, load, and availability;
- measured generic-kernel throughput, I/O, restart overhead, and parallel
  efficiency; and
- every named owner approval under `G0-READERS`, `G0-MV-Q`, and
  `G0-RESOURCES`.

### Finite sequence

1. Statistical and scientific owners approve or amend TB-0011's output/metric
   registry recommendations and close every extension/count/storage blocker
   without changing the scientific contract.
2. A later bounded pre-Gate-0 brief may implement only a generic artificial-
   buffer benchmark harness after the complete static ledger and storage upper
   bound close, then obtains infrastructure, security, statistical, and
   governance review before any benchmark run.
3. A distinct execution brief runs that benchmark on an approved resource and
   records conservative bounds and allocations.
4. Owners choose `G0-RESOURCES A/B/C`; this document makes no selection.
5. Only after all Gate-0 decisions freeze may a post-Gate-0 brief implement the
   exact project scientific pipeline. A still later brief is required to run
   it.

The sequence cannot bypass the scientifically prior `G0-METHOD` decision or
any data, reader, model, checkpoint, ethics, or governance gate.

## Stop Rule and Permitted Claim

Stop before the next resource action if the output registry is incomplete; a
schema term lacks a finite upper bound; an optimization lacks exact
conformance; a generic benchmark cannot cover a workload row; capacity is not
explicitly assigned; or any owner proposes pruning, approximation, weaker
thresholds, changed streams, fewer replications, or hidden compression credit.

The permitted claim is limited to:

> The repository contains a static computation, audit-schema, proof-obligation,
> and future artificial-buffer benchmark design for the unchanged pre-reader
> simulation contract.

It does not establish implementation correctness, calibration admissibility,
runtime, affordability, resource availability, statistical operating
performance, reader reliability, `MV-1` validity, clinical benefit, Gate-0
closure, venue readiness, acceptance, or publication.
