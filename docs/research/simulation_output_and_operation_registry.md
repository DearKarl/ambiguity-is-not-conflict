# Simulation Output and Semantic-Operation Registry

**Status:** Complete static freeze candidate under TB-0011; owner approval,
benchmark authorization, resource qualification, and Gate-0 closure remain
open

**Registry date:** 2026-08-29

**Evidence class:** Repository-only protocol compilation; no project random
stream, scientific implementation, simulation, data/model/reader access, or
benchmark

## Executive Verdict

The unchanged pre-reader simulation now has a machine-readable logical output
registry and a hardware-neutral semantic-operation ledger. The registry names
every currently mandated reliability and `MV-1` core output, its type, fixed
slot, applicability, four-state semantics, persistence rule, aggregate rule,
and failure interpretation. It also names every known unresolved extension
rather than assigning it zero cost. The operation ledger maps every frozen
candidate cell to exact, lower-bound, upper-bound, alternative-specific, or
explicitly unresolved semantic counts without generating scientific values.

This audit rejects the prior 56-byte common prefix and 312/568-byte outer
records. They could not separately encode slot state, gate events, all reached
failure components, and a deterministic join to execution provenance. The
corrected candidate uses a 72-byte canonical scientific prefix, externalizes
mutable attempt/retry/infrastructure provenance to a keyed execution-attempt
sidecar, assigns two-bit state per payload slot, and uses 336/600-byte
reliability/`MV-1` outer records. Under the same conditional
all-candidates-success path, catalogue, locks, completion bitmaps, and core
outer records alone occupy **613,093,770,610 bytes**. That is exactly
40,601,280,000 bytes above TB-0010's superseded 572,492,490,610-byte floor.
It is still a lower bound, not a final output upper bound or allocation,
because typed static, aggregate, family, permutation, journal, failure-detail,
and owner-blocked extensions remain outside it.

The registry is a recommendation, not an executable schema. `G0-METHOD` is
scientifically prior and owner-blocked. `G0-READERS`, `G0-MV-Q`,
`G0-RESOURCES`, and Gate 0 remain open. No benchmark is authorized until the
finite blockers below are decided and a complete storage upper bound exists.

## Facts, Inferences, Assumptions, and Candidate Recommendations

### Repository-derived facts

- The frozen TB-0009 enumerator produces 10,847 reliability candidates and
  2,438 pre-calibration `MV-1` candidates. Their sorted-ID hashes remain
  `4823bd2f52547673c173aec89ecd3b3c1d416769ee9abde9e3b71bb1fb0245d6`
  and
  `1cacee1ebe5aa7b43d37a09d39285a9637c6c274012a7335998bb707bd7ee8c7`.
- The full conditional envelope contains 1,301,640,000 reliability outer
  identities and at most 292,560,000 `MV-1` outer identities. Every executable
  cell uses exactly 120,000 outer identities and every reached bootstrap
  analysis consumes all 9,999 resamples; an undefined resample is never
  redrawn.
- The output registry contains 259 rows. The operation registry contains 244
  rows. Their complete-file SHA-256 values are
  `f37aef5e8a45bb8b913039a27989ed820f78956f4333a46bec4deba10de8ebb1`
  and
  `0aa55131f8779b95281ff6a506e9119c5fe2f9faee9b8de3d601c9a723564ac0`.
- The untracked full semantic ledger contains exactly 1,242,518 data rows and
  has complete-file SHA-256
  `d1c15377bed93c297890f82acd4ff94b0e2f311324b0cd05a3ddaec2cb3cff5d`.
- No repository evidence establishes CPU time, RAM, scratch, filesystem or
  container overhead, compression, I/O, wall time, cost, energy, available
  capacity, calibration success, or scientific operating performance.

### Inferences

- A binary64 payload plus NaN sentinel cannot distinguish structural
  inapplicability, reached-but-scientifically-undefined, and not reached after
  upstream failure. Independent two-bit state is therefore required for every
  core slot.
- Gate outcomes are events, not pipeline failures. They belong in a separate
  event mask and aggregate numerator. Conflating them with a primary
  failure code would bias operating-characteristic denominators and destroy
  auditability.
- The final scientific value need not imply retention of every raw word,
  synthetic rating, bootstrap index, or bootstrap statistic. Those may be
  reconstructed only from immutable cell/outer identity after bitwise
  transcript conformance is proved. Truths, calibration locks, final outer
  outputs, events, failures, aggregate numerators/denominators, and provenance
  cannot be reconstructed from aggregate success counters alone.
- Hierarchical/Gwet/ordinal/adjudication analyses belong to the later observed-
  reader route under the current canonical simulation mandate. Multiplying
  them across every simulated outer identity would create an unapproved new
  simulation family. `MV-1` FE and all 30 leave-one-reader values are different:
  they are already part of the qualification veto and therefore remain in the
  core registry.

### Explicit assumptions used only for arithmetic

- Core slots are eight-byte typed payload positions (`F64`, `U64`, `I64`,
  `BOOL`, or enum), independent of their two-bit state. This is a packed
  logical comparison schema, not a selected file format.
- The 613.094-GB conditional floor assumes all pre-calibration `MV-1`
  candidates become outer-eligible and every named outer identity emits a
  record. Its `MV-1` component is therefore an upper envelope in candidate
  count, while the byte total is a lower bound on the complete audit payload
  conditional on that path.
- The cell catalogue remains `42 + L_i` bytes per exact canonical JSON
  identifier; the cell-static lock remains 112 bytes per candidate; the
  completion bitmap remains 15,000 bytes per candidate. These TB-0010 terms
  are retained only to isolate the record-width correction.
- Reliability repeat and ambiguity counts retain the proved zero-to-maximum
  bounds because exact axis-specific domains and abstract item identifiers are
  not frozen. `MV-1` calibration and outer work retain upper-bound labels
  because calibration eligibility and realized evaluability are unknown.

### Candidate recommendations pending owner approval

- **Candidate status:** TB-0011 freezes the registries as reviewable candidates only.
  It does not approve a serializer, implementation, benchmark, or scientific
  run.
- **Candidate recommendation:** Every unique successfully committed outer
  identity in a cell that passes its static preconditions receives one audit
  record; a permanently incomplete infrastructure identity receives no
  fabricated scientific record and remains unset in the completion bitmap. A non-value
  payload is canonical zero; NaN never encodes state. Failure components and
  events are independent masks. Infrastructure retries never alter the
  scientific identity or silently replace an outcome.
- **Candidate recommendation:** Static truths/calibration locks, outer core values and states,
  event/failure provenance, cell aggregates, family decisions, completion
  identity, and digests are persisted. Raw words, individual synthetic
  ratings, bootstrap indices, and bootstrap replicate values are calculated
  and normally reconstructed, not retained, subject to later bitwise
  conformance and approved retention policy.
- **Recommendation:** Owners freeze the five decision groups in the blocker
  register before any generic-kernel benchmark brief. If any extension is
  approved, its exact occurrence and byte upper bound must enter the compiler
  before resource qualification.

## Canonical State and Failure Semantics

### Per-slot state

Every reliability and `MV-1` core payload slot carries exactly one two-bit
state:

| State | Meaning | Payload rule |
| --- | --- | --- |
| `VALUE` | The operation was reached and produced the defined scientific value. | Store the exact typed payload. |
| `INAPPLICABLE` | The field is structurally absent, for example class 4 on a three-class axis. | Canonical zero payload. |
| `SCIENTIFIC_UNDEFINED` | The operation was reached but the estimand/statistic is undefined under the frozen rule. | Canonical zero payload; increment the applicable failure/event accounting. |
| `NOT_REACHED` | An earlier frozen-precedence condition prevented evaluation. | Canonical zero payload; preserve the upstream failure. |

Quiet NaN is not a state. A non-finite scientific result follows the frozen
numeric-failure rule and never masquerades as `VALUE`. Excess fixed slots are
`INAPPLICABLE`, not zero-valued estimates.

### Candidate common prefix

| Field | Type | Bytes | Semantics |
| --- | ---: | ---: | --- |
| Cell index / outer index | `U32 / U32` | 8 | Immutable outer identity |
| Scientific status / primary failure | `ENUM16 / ENUM16` | 4 | Deterministic status and first scientific failure |
| Failure-component mask | `U64` | 8 | Every reached component failure; later failures are not erased |
| Event mask | `U64` | 8 | Gate and operating events only; distinct from failure and slot state |
| Undefined-bootstrap count | `U16` | 2 | `0..9,999`; every resample is still consumed |
| Registry version | `U16` | 2 | Immutable field/event registry version |
| Execution-provenance join key | `U64` | 8 | Deterministic `(cell_index << 32) | outer_index`; mutable attempts are external |
| Payload digest | 32 bytes | 32 | SHA-256 of the exact 336/600-byte uncompressed record with this digest slot canonical zero |
| **Total** |  | **72** | Before state mask and typed payload |

The recommended scientific precedence is schema/identity failure, static
calibration/truth failure, outer-DGP undefinedness, estimand non-estimability,
bootstrap undefinedness, and numerical-conformance failure. A complete record
has none of these. Gate pass/fail remains an event. This ordering and the exact
component enumeration require owner approval; the registry preserves that
approval blocker instead of treating the recommendation as final.

### Audit structures outside the outer core

The logical registry also names the file header (byte order, schema/registry/
content identities, record and byte counts), every catalogue field, the full
cell-static lock including `R` and `B`, identifier and permutation dictionary
headers/payloads, the 15,000-byte completion bitmap, state masks, chunk
journal, failure detail, keyed 32-byte execution-attempt sidecar, cell/family
aggregates, and event/status/failure
dictionaries. Fixed fields have exact widths or formulas. File partitioning,
dictionary/permutation payloads, typed aggregate/family extensions, journal/
attempt/retry/failure-detail occurrence, and container overhead remain explicitly
unresolved and therefore block a final storage upper bound. They are not
omitted or assigned zero.

Each execution-attempt sidecar record is `U64 first_join_key,
U32 identity_count, ENUM16 work_unit_kind, U16 attempt_ordinal, ENUM16 outcome,
U16 registry_version, U32 failure_detail_ref, U32 chunk_journal_ref,
U32 reserved_zero`. The global cell index is the zero-based lexicographic rank
in the combined reliability-plus-`MV-1` canonical manifest. An outer identity
uses `(global_cell_index << 32) | outer_index`; reserved low words identify the
static cell (`0x80000000`), present/absent `MV-1` calibration
(`0x80000001/2`), and cell aggregate (`0x80000003`). Global cell index
`0xffffffff` with low words `0`, `1`, and `2` identifies reliability family,
`MV-1` family, and global CP95 conformance work, respectively. Thus
reliability/`MV-1` indices do not collide and calibration/global retries are
auditable.

The frozen candidate `work_unit_kind` codes are `1 REL_STATIC`,
`2 REL_OUTER_RANGE`, `3 MV_STATIC`, `4 MV_CAL_PRESENT`, `5 MV_CAL_ABSENT`,
`6 MV_OUTER_RANGE`, `7 CELL_AGGREGATE`, `8 REL_FAMILY`, and `9 MV_FAMILY`.
Code `10 CP95_CONFORMANCE` identifies the mandatory global half-width scan.
Outcome codes are `1 COMMITTED`, `2 INTERRUPTED_RETRYABLE`,
`3 INFRASTRUCTURE_FAILED_FINAL`, `4 INTEGRITY_REJECTED`, and
`5 DUPLICATE_IDENTICAL_DISCARDED`; a scientifically failed but valid record is
still `COMMITTED`. The sidecar records scheduled atomic work units/ranges, not
unknowable post-crash “last reached” identities. `identity_count` is the
scheduled range and the completion bitmap plus committed chunk journal is the
authority for completed outer identities.
An outer record joins a range record iff both use the same global cell index
and `first_join_key <= outer_join_key < first_join_key + identity_count`;
`identity_count` is positive, an outer range may not cross `R=120,000` or any
reserved low-word code, and overlapping committed ranges are a schema
failure. Static, calibration, aggregate, and family work units always have
`identity_count=1`. One complete `MV-1` polarity is the atomic calibration
retry unit; named mean/endpoint/midpoint digests are integrity evidence only,
not durable restart points, so an interrupted polarity is replayed in full.

Attempt ordinals are contiguous from zero and must not exceed 65,535; overflow
is a schema failure. A zero `U32` reference means absent, positive references
are local to the named sidecar partition, and a required reference exceeding
`2^32-1` forces a new reviewed partition/schema before writing. Retry count is
derived from the attempt ordinals and causes are joined through failure-detail
references. This is a separate logical stream with its own file header and
content digest even if a later container multiplexes streams. Its chunking,
initial-attempt, retry, and failure occurrence is resource-policy dependent
and remains unresolved. A permanent infrastructure failure has sidecar/
failure records and an unset completion bit, but no fabricated scientific
outer record.
P9 must additionally prove atomic append/recovery of this sidecar: every
scheduled attempt has exactly one terminal outcome after recovery, ordinals
are contiguous, and no committed scientific range exists without the matching
sidecar and chunk journal.

One 15,000-byte completion bitmap is persisted for every one of the 13,285
manifest candidate cells. If reliability static preconditions fail or an
`MV-1` calibration fails before outer work, the bitmap remains all zero and the
separate static/calibration failure record explains why; no outer record is
invented. This reconciles restart identity with the exact 199,275,000-byte
bitmap floor.

The proposed file-content digest has a noncircular domain: SHA-256 covers the
exact uncompressed file bytes with the 32-byte content-digest slot set to its
canonical all-zero value. Registry digest, record count, byte count, and every
other header/payload byte are included. The operation ledger uses the same
domain; container partitioning and therefore the number of digest calls remain
owner-blocked.

Outer-record digests use the same noncircular convention at record scope:
hash the exact uncompressed 336-byte reliability or 600-byte `MV-1` record in
canonical field order with its own 32-byte payload-digest slot set to all zero.
Canonical header fields (including the deterministic sidecar join key), state
mask, and typed payload are included. Mutable execution-attempt sidecar bytes
are excluded from this record digest and have their own file/chunk integrity
accounting. The reliability and `MV-1` hash-operation rows name exactly this
domain.

## Persistence and Reconstruction Boundary

| Object | Action | Reason or later proof obligation |
| --- | --- | --- |
| Canonical cells, family membership, software/algorithm/permutation locks | Persist | Defines the attempted design and replay identity. |
| Reliability 41/61-node truths, discrepancies, missingness solve, final truth choice | Persist | Static classification and coverage cannot depend on a later recomputation with changed software. |
| `MV-1` calibration parameters, residuals, validation, eligibility, trace/validation digests, final truth choice | Persist | Calibration failure and outer eligibility are family members, not a filter. |
| Every canonical outer core value, state mask, event/failure mask, deterministic execution join key, and digest | Persist | Required to reproduce component and family operating characteristics independent of execution history. |
| Every realized execution attempt and infrastructure cause | Persist in keyed sidecar/failure records | Retains exact retry accounting without making canonical scientific bytes depend on a retry schedule. |
| Cell event numerators/denominators/intervals and family minima/failed-member inventories | Persist | Prevents denominator drift and partial-family promotion. |
| Raw random words and open-unit values | Calculate, then reconstruct | Retain only if a later conformance/retention decision requires it; raw-word transcript must be bitwise reproducible. |
| Individual synthetic ratings and missingness flags | Calculate, then reconstruct | Fixed identity and algorithm locks must reproduce them exactly. |
| Bootstrap index vectors and bootstrap statistic vector | Calculate, then reconstruct | All 9,999 resamples remain consumed; final interval/critical value and undefined count are persisted. |
| Repeat diagnostics and permutation payload | Owner-blocked extension | Exact estimators/domains/identifiers are not frozen; cost is not assumed zero. |
| Hierarchical/Gwet/ordinal/adjudication sensitivity | Observed-reader only under current record | Adding it to simulation requires a prospective canonical amendment and full re-enumeration. |

Reconstruction is conditional on a later reference implementation, immutable
software and algorithm locks, complete permutations, and bitwise conformance.
This document does not establish any of them.

## Global Exact-Binomial Half-Width Conformance

The canonical `R=120,000` justification is a mandatory algorithm-conformance
record, not an assumed arithmetic fact. After the exact-binomial reference
algorithm is frozen, the reviewed implementation must evaluate the two-sided
95% Clopper--Pearson interval at every success count `x=0,...,120,000`, persist
the maximum `(upper_x-lower_x)/2`, and persist the smallest `x` attaining that
maximum. The pass field is a typed Boolean and is true only when the complete
scan is finite/reference-conformant and the maximum is strictly `<0.003`.
A finite value `>=0.003` or any numerical nonconformance is a conclusive common
failure; a missing/incomplete scan is `NOT_REACHED` and makes both family
decisions `INCOMPLETE` unless another conclusive failure dominates.

The operation registry counts 120,001 composite interval calls, 120,001
half-width evaluations, 120,000 ordered max/argmax comparisons, one strict
threshold comparison, and one conformance-record serialization. The primitive
reference alternative has exactly 240,000 beta-quantile calls: two for each
interior `x` and one at each boundary. Composite interval and primitive
quantile rows are non-additive alternatives. The conformance record has its
own `CP95_CONFORMANCE` execution-attempt work-unit key; no numerical interval
was evaluated by this static compiler.

## Reliability Output Registry

### Cell-static record

The static extension persists axis identity, `K_g`, `N_g`, panel/roster sizes,
assignment/repeat/ambiguity counts and digests, the missingness intercept and
bracket/residual/iteration state, and nominal alpha, macro agreement, and
four fixed positive-agreement slots at both 41 and 61 nodes. Slots `c>=K_g`
are `INAPPLICABLE`; applicable slots have independent two-bit states. It also persists their
discrepancies, the owner-approved final truth, null/boundary classification,
planning eligibility, and static failure. The final truth-reference rule,
repeat/ambiguity domains, and assignment payload remain blockers.

The numeric missingness endpoints `-30` and `+30` retain independent reached
state. Endpoint residuals remain `NOT_REACHED` until their signed residual
direction is approved. For a required reader/class solve, bracket state,
realized iteration count, final intercept, and final residual also remain
`NOT_REACHED` until the inclusive endpoint-zero predicate, nonfinite behavior,
midpoint-zero equality, endpoint-update, post-100 cached-candidate, and tie
rules are frozen. The `not_required` bracket state remains available for
`m=0` and MCAR cells. These are owner decisions rather than inferred numerical
conventions. After those rules are frozen, a required missingness solve passes
only when its bracket and final selection are reached and finite and
`abs(selected signed residual) <= 1e-10`. A finite residual above that inclusive
tolerance remains a numeric `VALUE` for audit, but causes static failure and
`I_R3=0`; it can never be promoted as a successful solve. When the truth stage
is reached, both 41- and
61-node orders are attempted and each scalar/class element is state-masked
independently, so one failed order or class never erases another. A discrepancy
is `VALUE` only when both inputs are `VALUE`. Final truth remains `NOT_REACHED`
until the owner reference rule is frozen, becomes `VALUE` only from a valid
selected input with discrepancy `<=1e-6`, and is
`SCIENTIFIC_UNDEFINED` otherwise. Every fixed static payload includes its
explicit element-state-mask byte(s); record framing remains a storage blocker.

The reliability truth classification is deterministic over required selected
binary64 values. `ALTERNATIVE` means final alpha `>0.67`, final macro agreement
`>0.80`, and every applicable final positive agreement `>0.70`. `BOUNDARY`
means no required component is below its threshold and at least one is exactly
equal; `NULL` means any required component is below. Fixed positive-agreement
slots `c>=K_g` are `INAPPLICABLE` and ignored. For a manifest planning member,
`planning_truth_eligibility` is `true` exactly when alpha `>0.80`, macro
agreement `>0.85`, and every applicable positive agreement `>0.75`; it is
`false` for any finite threshold miss and `INAPPLICABLE` for nonmembers.
`I_R3` requires `true` for a planning member. Invalid or unavailable required
truths preserve `SCIENTIFIC_UNDEFINED` or `NOT_REACHED` rather than fabricating
a class or Boolean.

### Fixed 32-slot outer core

| Slots | Typed values | Applicability |
| --- | --- | --- |
| `0..3` | Nominal alpha; percentile lower/upper; macro agreement | Estimable outer replication |
| `4..7` | Positive agreement for classes `c0..c3` | Slots beyond `K_g` are `INAPPLICABLE` |
| `8..11` | Observed prevalence for classes `c0..c3` | Slots beyond `K_g` are `INAPPLICABLE` |
| `12..18` | Overall missingness; reader min/max/span; presentation-arm min/max/span | Reached outer replication |
| `19..25` | Alpha-point, alpha-lower, macro, and four class gate events | `VALUE` Boolean for every outer identity when structurally applicable; nonestimability is `false` |
| `26..30` | Allocation, overall-missingness, reader-span, arm-span, and complete-gate events | `VALUE` Boolean for every outer identity; not reached is `false` |
| `31` | Coverage event | `VALUE` Boolean for every outer identity; undefined interval/truth is `false` |

Value-slot states are component-local. After the DGP is reached, observed alpha
is `VALUE` or `SCIENTIFIC_UNDEFINED` under its own estimator; a bootstrap
failure makes only the CI endpoints `SCIENTIFIC_UNDEFINED` and does not erase a
defined observed alpha, macro agreement, prevalence, or missingness diagnostic.
For an applicable class, empty positive-agreement or prevalence denominators
make only that component `SCIENTIFIC_UNDEFINED`; classes beyond `K_g` are
`INAPPLICABLE`. Reader/arm extrema and spans require their named denominators.
An upstream DGP nonreach makes downstream applicable values `NOT_REACHED`.
Reached independent diagnostics remain `VALUE` even when another component
sets the primary scientific status.

False-promotion and planning-power applicability are reconstructed from
immutable family/static classification plus the complete-gate event. They are
persisted again in cell aggregates with explicit numerators and denominators.
The undefined-bootstrap count is in the common prefix. Repeat diagnostics are
not smuggled into an unnamed extension.

The nonestimability bit/status is construct-level, not merely a generic gate
failure. Undefined observed alpha, any undefined bootstrap alpha, a missed
intended-stratum quota, an empty required positive-agreement denominator,
overall missingness above `0.05`, or reader/arm missingness span above `0.05`
sets the applicable gate event false and sets event bit 13 with the matching
scientific status. A finite alpha, interval, agreement, or positive-agreement
value that only misses its numerical gate remains an estimable gate failure
and does not set bit 13.

### Cell and family aggregates

The cell registry covers alpha coverage, complete-gate pass, outer
non-estimability, any undefined bootstrap, every alpha/macro/class/allocation/
missingness component failure, false promotion, and planning power. Each
applicable Bernoulli event persists `successes`, `trials`, estimate, interval
kind, alpha, lower, and upper. `sum(undefined)/(R B)` is separately descriptive
and receives no binomial interval; the independent outer-level “any undefined”
event may receive one.

For every cell that passes static preconditions, every Monte Carlo denominator
is the fixed `R=120,000`; scientific nonestimability and `NOT_REACHED` count as
failed pass/coverage events, never denominator deletion. Infrastructure
incompletion makes the cell/family `INCOMPLETE` rather than fabricating a
scientific failure. The event dictionary fixes bits 0--12 for the 13 core
events and bits 13--14 for nonestimability/any-undefined. Gate inequalities
are inclusive: alpha `>=0.80`, lower bound `>=0.67`, macro `>=0.85`, each
positive agreement `>=0.75`, missingness/spans `<=0.05`, and coverage includes
both endpoints. Ordinary events use two-sided 95% Clopper--Pearson intervals;
coverage requires lower `>=0.945`; false promotion uses a one-sided 95% upper
limit `<=0.055`; planning uses a one-sided lower limit at `0.05/4,416`.
A static precondition failure stops before outer work and fails/incompletes the
design under its canonical rule; no operating interval is computed from a
smaller denominator.

The aggregate audit record still exists for every reliability manifest cell,
but its probability fields are `VALUE` with fixed `N=R=120,000` only when
`I_R3=1` and `I_complete=1`, where `I_complete` verifies all bitmap identities and exactly
one integrity-valid canonical record per identity. A static pre-outer failure
(`I_R3=0`) or failed completion/integrity audit (`I_complete=0`) sets those aggregate fields to
`NOT_REACHED`, records zero trials, and computes no Clopper--Pearson interval
or undefined-bootstrap fraction. It is a static family failure, not an
invented `x=0, N=120,000` result. A schema/integrity mismatch is a conclusive
family failure; absent/incomplete records without such a mismatch are
infrastructure missing and make the family incomplete unless another failure
dominates. Scientific nonestimability after outer
execution starts remains a failed event inside fixed `R`; it is not automatic
infrastructure incompletion.

Family output retains all 10,847 candidate outcomes, their two-sided coverage
limits or static-failure records, every final-truth-applicable one-sided
false-promotion check, all 4,416 planning checks, the 15 planning-axis minima
and argmin cells, `sum_g(1-L_g^min)`, complete-member count, and a complete
pair of disjoint conclusive-failure and infrastructure-missing inventories.
The 15-element arrays follow the frozen axis order
`image_technical,image_coverage,image_semantic,image_polarity,text_integrity,`
`text_target_polarity,text_commitment,text_interpretation,`
`text_derived_polarity,pair_atomicity,pair_preservation,pair_fluency,`
`pair_plausibility,pair_nonsemantic_cues,pair_global`. Within each axis, the
reduction scans every planning member by ascending combined-catalogue index,
updates only for a strictly smaller lower limit, and retains the first value
on exact binary64 equality. The argmin is therefore the smallest catalogue
index among tied minima.
`PASS` requires true common CP95 half-width conformance, valid static
preconditions, and exact
`R`-identity accounting for every candidate, every coverage and applicable
false-promotion criterion, and the complete planning/axis union rule.
Schema/integrity/scientific/static criterion failure is `FAIL`; missing infrastructure output
is `INCOMPLETE`. An outer scientific nonestimability remains in its fixed-`R`
event denominator and is judged by those declared criteria rather than being
silently deleted.

Family status has deterministic precedence: false/invalid common CP95
conformance or any conclusive scientific/static criterion failure yields
`FAIL` even if a different member also has missing infrastructure output;
absent such a conclusive failure, missing common conformance or any missing
infrastructure output yields `INCOMPLETE`; only the complete passing
conjunction yields `PASS`.

Manifest/required-member counts and both inventories stay `VALUE` whenever
family audit closure can determine them. The conclusive-failure inventory and
the no-conclusive-failure infrastructure-missing inventory are unique and
disjoint. Together with the un-inventoried passing remainder they partition
all 10,847 candidates and make `FAIL`-over-`INCOMPLETE` precedence
reconstructible. `complete_member_count` is instead an execution-completeness
diagnostic (static pass plus exact `R` accounting); it can overlap the failed
inventory when a complete run fails coverage, false-promotion, or planning
criteria. The 15 minima,
argmins, and their union sum are `VALUE` only when all 4,416 planning lower
limits exist; otherwise they are `NOT_REACHED`, never computed over surviving
members. The final decision itself is always a typed `VALUE` enum after audit
closure. If final-truth classification is unavailable, the false-promotion
check count is `NOT_REACHED` and the family fails rather than reclassifying a
subset.

## `MV-1` Output Registry

### Cell/polarity calibration record

The static extension covers admissible mean intervals, positive beta-shape
bounds, per-polarity realized scan/solve/residual/candidate-vector/outer-
midpoint/monotonicity-comparison/validation-vector/validation-pass counts,
trace digest, maximum monotonicity decrease and index, `mu_Y`, `alpha_Y`, beta
shapes or two-point mixing probabilities,
candidate/validation residuals in exact
`present_yield,present_q,absent_yield,absent_q` order, bracket/validation state and
digest, calibration status, three final truths in `balanced,present,absent`
order, assignment digest, and outer eligibility. Target-versus-validated truth
and trace depth remain explicit owner blockers. The signed yield-residual
definition is frozen as `estimated P(E=1|Y)-rho_Y`; each of the 2,162 nested
alpha solves still requires an approved bracket sign orientation, finite and
inclusive predicate, nonfinite behavior, midpoint-zero equality and endpoint-
update rule, and cached final-alpha/tie selection before its selected alpha may
feed a q evaluation. The canonical open condition
on beta means does not itself select closed 1,001-point-grid endpoints or a
strictly positive shape margin, and the post-80-midpoint text does not select
which cached endpoint or midpoint is the final `(mu_Y,alpha_Y)` pair or how
ties break. Those numerical-domain and final-solution rules are therefore
separate owner blockers; affected values remain `NOT_REACHED` rather than
being inferred. The validation digest is also
owner-blocked: no current decision selects raw validation words, transformed
vectors, residual/reduction outputs, or another canonical transcript as its
byte domain. Call count is bounded, but hash bytes and semantics remain
unresolved until that transcript and encoding are approved.

Every two-polarity and four-residual/shape array carries one independent
two-bit state per named element. A completed present-polarity value therefore
remains `VALUE` when absent polarity is `NOT_REACHED`. Beta-shape fields are
`INAPPLICABLE` for two-point candidates and mixing-probability fields are
`INAPPLICABLE` for beta candidates. Candidate and validation residuals use the
signed definitions `estimated P(E=1|Y)-rho_Y` and
`estimated E(q_observed|E=1,Y)-q_Y,target`, respectively on the candidate or
independent validation stream. Once the final-solution rule is approved, they
remain numeric `VALUE` when finite even if either absolute validation residual
exceeds `0.0005`; failure is a separate event/status. Unentered or owner-
blocked later stages are `NOT_REACHED`, while reached
nonfinite values are `SCIENTIFIC_UNDEFINED`. The target-truth option would make
finite manifest targets `VALUE` after identity even if validation fails; the
validated-truth option makes each component validation-dependent. This branch
remains an explicit owner choice rather than silently imposing one truth
definition.

Trace and validation digests are also per polarity. At most one final
whole-trace digest is persisted per attempted polarity, but trace encoding and
depth remain owner-blocked. Named complete evaluation digests and
materialized-raw-buffer verification calls/bytes have their own unresolved
operation rows and are not included in that two-call bound. They are integrity
evidence only; whole-polarity replay is the current atomic restart rule.

Each polarity's control record has a packed 40-byte payload plus one byte
carrying its independent two-bit field state. In order it stores scan points,
alpha solves, alpha-bracket checks, alpha-midpoint controls, residual
evaluations, candidate-vector evaluations, outer-q bracket checks, outer
midpoints, monotonicity comparisons, validation-vector evaluations, and
validation passes. It becomes `VALUE` only for the retry-invariant canonical
calibration path that commits a scientific pass or conclusive scientific
calibration failure, including zero counts for later stages skipped by that
scientific failure. If infrastructure interruption/exhaustion leaves no
committed calibration result, it is `NOT_REACHED`; discarded partial retry
counts live only in execution/resource audit records. These persisted counts
audit deterministic early exits; successful-path operation bounds may not be
substituted for them.
Exactly two control-record assemblies per manifest candidate copy these 11
realized counters and their states; they do not repeat the counted calibration
operations or static serialization.

### Fixed 64-slot outer core

| Slots | Typed values | Order |
| --- | --- | --- |
| `0..1` | Evaluable present and absent counts | `present,absent` |
| `2..16` | q estimate, SE, lower bound, truth, and FE estimate | Each in `balanced,present,absent` order |
| `17` | Max-`t` critical value | Scalar |
| `18..19` | FE rank and expected rank | Integer |
| `20..49` | Thirty leave-one-reader estimates | Reader `00..09`, then `balanced,present,absent` |
| `50..53` | Screen-stratum by assigned-polarity counts | Present/present, present/absent, absent/present, absent/absent |
| `54..63` | Two yield, three q-gate, simultaneous-coverage, FE, LOO, no-veto, and complete-joint events | Fixed event-mask order |

The common prefix retains undefined-bootstrap count, scientific status and
failure/event masks, and a deterministic execution-sidecar join key. Mutable
attempt and retry state remains exclusively in the external sidecar.
Probability and categorical repeat metrics remain blocked until their exact
estimators are frozen.

Reachability is frozen per field in the machine registry. Reached evaluability
and screen-by-assignment counts are `VALUE`, including zero, when their U64
reductions are valid; DGP non-reach makes them `NOT_REACHED`. Each q estimate
is `VALUE` only when its required polarity count/mean exists and the result is
finite; a reached missing/nonfinite required mean is `SCIENTIFIC_UNDEFINED`,
while DGP non-reach is `NOT_REACHED`. Each SE is `VALUE`, including zero, only
after its q estimate and required `n>=2` finite variance exist; a reached
invalid variance is `SCIENTIFIC_UNDEFINED`, and a non-value upstream q estimate
makes the SE `NOT_REACHED`. A zero SE remains numeric but makes the common
max-`t` critical value `SCIENTIFIC_UNDEFINED`.

The max-`t` critical value is `VALUE` only when all required observed and 9,999
resampled SEs are finite and strictly positive. Invalid reached inputs make it
`SCIENTIFIC_UNDEFINED`; a non-entered DGP/bootstrap stage makes it
`NOT_REACHED`. Each lower bound is `VALUE` only when its q estimate, SE, and
the common critical value are `VALUE` and the inclusive construction is
finite. Non-value prerequisites make it `NOT_REACHED`; nonfinite arithmetic
from value prerequisites is `SCIENTIFIC_UNDEFINED`. Each static calibrated
truth component is copied independently and never inherits q/SE/max-`t`/FE/LOO
failure. FE rank is `VALUE` even when deficient, while each FE component is
`SCIENTIFIC_UNDEFINED` for a reached deficient/nonfinite fit and `NOT_REACHED`
if the fit was never entered. Each named reader/component LOO slot is likewise
independent: a reached missing/nonfinite required polarity result is
`SCIENTIFIC_UNDEFINED`; an unentered named fit is `NOT_REACHED`. Thus one LOO
failure never erases another reached component.

Every applicable event is nevertheless a `VALUE` Boolean over the fixed outer
identity; scientific undefinedness or non-reach makes that event `false`.
Bit 15 is set for DGP non-reach, missing required polarity means or variances,
nonpositive/nonfinite required observed or resampled SEs, unavailable max-`t`
or lower values, FE rank/nonfinite failure, missing/nonfinite required LOO
polarity, or numerical nonconformance. Any undefined bootstrap also sets bit
16 and a positive undefined-bootstrap count. Finite yield, q, FE, or LOO gate/
tolerance misses set only their outcome event false; they do not create
nonestimability.

### Cell and family aggregates

Cell events cover three marginal and simultaneous coverage probabilities, two
yield floors and joint yield, three q gates and their complete family, FE/LOO/
combined veto, complete joint qualification, non-estimability, any undefined
bootstrap, null-cell false qualification, and planning joint power. Ordinary
Monte Carlo probabilities use two-sided 95% intervals; null false
qualification uses a one-sided 95% upper limit; planning joint power records
the required lower limit. The final alpha and exact-binomial reference
algorithm remain part of the software/algorithm lock.

Null-family membership is immutable manifest metadata: it is defined from the
target q pair by `q_bal,target=(q_present,target+q_absent,target)/2=0.10`,
`q_present,target=0`, or `q_absent,target=0`. It never depends on exact equality
of the subsequently selected calibrated truth. Selected truth is used for
coverage, not for deleting a prospectively required null-family check.

All applicable cell probabilities use `N=120,000`. The event dictionary fixes
bits 0--9 for yield/q/coverage/veto/joint events, bits 10--12 for marginal
coverage, bit 13 for joint yield, bit 14 for the complete q family, and bits
15--16 for nonestimability/any-undefined. Yield uses `n_y>=108`; q gates use
strict `L_bal>0.10`, `L_present>0`, and `L_absent>0`; FE/LOO preserve their
strict-positive and absolute-`0.05` veto rules. Ordinary probabilities,
including planning joint power, use two-sided 95% Clopper--Pearson intervals;
simultaneous coverage requires lower `>=0.945`, planning joint power requires
lower `>=0.90`, and null false qualification uses a one-sided 95% upper limit
`<=0.055`. Infrastructure incompletion is `INCOMPLETE`, not a changed
denominator. Calibration failure remains a failed design member and never a
post hoc manifest filter.

An aggregate audit field exists for every `MV-1` candidate. The cell enum is
frozen as `NOT_ELIGIBLE=0`, `ELIGIBLE=1`, and
`INFRASTRUCTURE_INCOMPLETE=2`; `I_outer=1` exactly for `ELIGIBLE` and is zero
otherwise. For a structurally applicable field, `ELIGIBLE` with
`I_complete=1` permits `VALUE` with fixed `N=R=120,000`; `ELIGIBLE` with
`I_complete=0` yields `NOT_REACHED`, zero trials, and no interval. A conclusive
pre-outer scientific/static failure is `NOT_ELIGIBLE`, produces the same
aggregate non-reach, and enters the failed-calibration inventory and family
`FAIL`. Infrastructure exhaustion without a conclusive failure is
`INFRASTRUCTURE_INCOMPLETE`, also produces aggregate non-reach, and enters the
infrastructure-missing inventory and family `INCOMPLETE` unless another
conclusive `FAIL` dominates. An integrity/schema mismatch after eligibility is
conclusive `FAIL`; absence or incompletion without a mismatch is
`INCOMPLETE` unless another `FAIL` dominates.
Null and planning fields are
`INAPPLICABLE` only for immutable manifest nonmembers; a failed member is
`NOT_REACHED` and enters the family failure inventory, never a zero-success
`N=120,000` estimate or a deleted denominator.

Family output retains all 2,438 calibration candidates, failed-calibration,
outer/aggregate, and infrastructure-missing inventories, every one of the 108 immutable target-null checks,
every eligible-cell coverage check, all 2,304 manifest planning members or
their failure records, and missing-member count. `PASS` requires true common
CP95 half-width conformance, all candidates to calibrate and complete exact
`R`-identity accounting, every eligible
coverage criterion, all 108 null checks, and all 2,304 planning checks.
Schema/integrity/calibration/static/scientific criterion failure is `FAIL`; infrastructure
missingness is `INCOMPLETE`. Outer scientific nonestimability remains a failed
event in fixed `R` and is judged through these criteria. Calibration failure is
never a license to delete a cell.

The same family-status precedence applies: false/invalid common CP95
conformance or another conclusive `FAIL` dominates missing conformance or
other `INCOMPLETE`, which dominates `PASS`. The null check count is exactly the 108
immutable manifest-null audit outcomes, whether each is a `VALUE` interval or
a failed-member `NOT_REACHED` record.

Manifest counts, required 108/2,438/2,304 check counts, known failure and
infrastructure-missing identity inventories, and missing count remain typed `VALUE` after family
audit closure even when the decision is `FAIL` or `INCOMPLETE`. The two MV
failure inventories are unique and disjoint by precedence: pre-outer
calibration/static failures enter the first; only outer-eligible candidates
with conclusive outer/required-criterion failures enter the second. A candidate
is never appended to both. A third identity inventory and its equal scalar
count contain only candidates with no conclusive failure but infrastructure-
incomplete or missing required records. The three inventories and complete
passing remainder form a disjoint partition of all 2,438 candidates; “complete
outer accounting” alone is not a fourth inventory because a complete run may
still fail a required aggregate criterion. Total inventory appends are
therefore bounded by 2,438.

## Semantic-Operation Ledger

The operation table uses protocol-level events, never FLOPs, processor
instructions, throughput, or runtime. Let `R=120,000`, `B=9,999`, and let
`M_c` be the number of unique integrity-valid committed outer identities for
cell `c`, with `0<=M_c<=R`. `I_complete=1` iff `M_c=R`, all bitmap identities match,
and no integrity/schema mismatch exists. Scheduled scientific-kernel formulas
retain `R` as the prospective complete-path workload; actual persisted
outer fields, classification, hashes, serializations, bytes, and bit sets use
`M_c`. Interrupted/discarded retry work is a disjoint unresolved lifecycle
term. For a
reliability cell, `N` is included items, `K` categories, `P` panel size,
`A=NP`, and `Dmax` the existing axis instrument-repeat maximum. For an
`MV-1` cell, `n` is candidates per screen stratum and
`D=10 ceil(0.3n)`. For `MV-1`, `I_outer=1` exactly when the frozen cell enum is
`ELIGIBLE`; both `NOT_ELIGIBLE` and `INFRASTRUCTURE_INCOMPLETE` set it to zero
but retain their distinct family consequences.

### Reliability counts

Let `I_R3=1` exactly when the missingness solve passes, the 41/61 quadrature
truth is estimable, and either the cell is not a planning-family member or its
planning-truth Boolean is `VALUE true`. A nonzero reader/class missingness
solve passes only after an owner-frozen bracket and final selection are reached
and finite and `abs(selected signed residual)<=1e-10`; `m=0` and MCAR require
no solve. The planning Boolean is true exactly for final alpha `>0.80`, macro
agreement `>0.85`, and every applicable positive agreement `>0.75`. A
declared false-promotion/null cell with low truth is not pruned by this rule;
unless another stated precondition fails, it must run. All reliability outer,
bootstrap, and scheduled complete-path counts below are conditional on `I_R3`;
they are zero after a permitted pre-outer stop. Physical record work uses
`I_R3 M_c`, while scientific aggregation requires `I_R3 I_complete`. The
ledger encodes this symbol in each applicable row rather than mislabelling the
successful path as unconditional exact work.

- First-rating DGP words and open-unit conversions have conditional lower path
  `I_R3 R(N+2A)` and conditional upper path
  `I_R3 R(N+2A+N+3Dmax)`. The ambiguity and repeat
  components remain separately visible as `[0,RN]` and `[0,3RDmax]` words.
- Item inverse-normal calls are `RN`; first-rating softmax, categorical lookup,
  and missingness lookup are each `RA`. The primitive alternative separately
  records `RAK` exponentials and `RA` normalizations; optional log-sum-exp work
  stays a non-additive reference-algorithm alternative. Static baseline logits
  use `K^2` log evaluations. A nonzero reader-dependent missingness cell adds `roster`
  inverse-normal calls for its separately tagged reader vector.
- Conditional bootstrap words and index formations are each `I_R3 RBN`;
  alpha statistic recomputations are `I_R3 R(B+1)`. One disjoint composite
  point-output reduction per committed record computes macro agreement, the
  `K` applicable positive agreements and prevalences, overall missingness, and
  reader/presentation-arm minima, maxima, and spans. Percentile selections are at
  most `I_R3 R` because any undefined bootstrap alpha forbids order selection.
- A nonzero reader/class missingness path schedules two endpoint-residual
  evaluations and one bracket check, then performs at most 100 midpoint
  controls, 102 residual evaluations, at most one final cached-candidate selection,
  and `102A` expits plus an explicitly non-additive primitive-exp alternative.
  The exact counts do not approve the unresolved residual sign, inclusive
  endpoint-zero predicate, nonfinite, midpoint-zero equality, endpoint-update,
  final-candidate, or tie rules; affected states remain `NOT_REACHED`. The
  41/61 quadratures run only after an owner-frozen solve passes and
  contribute 102 node reductions and `102A` softmax vectors; primitive
  `102AK` exponentials and `102A` normalizations are recorded separately.
  Static reader-effect inverse normals are `roster*K`, followed by `K`
  explicit mean/population-SD normalizations; reader-dependent missingness
  adds one separately tagged roster vector and normalization.
- Ambiguity-interpretation lookup is bounded by `RN`. Repeat match,
  alternate-category normalization/lookup, and repeat-missingness lookup are
  each separately bounded by `R Dmax`; their lower bound remains zero until
  exact repeat domains freeze.
- Aggregate interval calls have per-cell lower/upper counts
  `I_complete(11+K+I_planning)` and
  `I_complete(12+K+I_planning)`; the gap is inclusive
  final-null-or-boundary false-promotion applicability. A full identity scan
  precedes scientific tallying. Only when `I_complete=1`, the shared base tally makes
  `R(11+K)` Boolean counter updates, reuses complete-gate counts for false
  promotion/planning, and separately adds the `R` undefined-bootstrap counts.
  Exactly `11+K` distinct event proportions are then evaluated; the reused
  false-promotion/planning estimate does not trigger another division. One
  separate division evaluates `sum(undefined)/(RB)`.
  Composite exact-binomial calls and primitive beta-quantile calls are
  non-additive alternatives. Repeat-metric and permutation bytes remain
  unresolved.
- One composite static-classification assembly per cell covers reached 41/61
  deltas, discrepancy checks, fixed four-class states, inclusive
  null-or-boundary classification, planning eligibility, `I_R3`, and failure
  precedence. One composite outer-classification assembly per committed record
  covers all states/events/failure masks/status precedence. One aggregate-
  record classification assembly exists even on static or completion failure;
  these control units exclude numerical kernels, tallies, and serialization.
- Catalogue/static/aggregate/file-header serialization, seed/HMAC and payload/
  trace/file hashes, completion bits, core bytes, exact family membership/
  coverage/null/planning reductions, and every unresolved dictionary/journal/
  failure/retry/I/O/RAM/scratch/runtime/allocation/contingency term have separate
  operation rows. The four registry dictionaries are each serialized once;
  identifier/permutation dictionaries, chunk-journal bytes, and failure-detail
  bytes retain explicit unresolved rows rather than zero cost. Shape
  denominators, composite-versus-primitive probability
  alternatives, and lower/upper envelopes carry non-additive accounting roles
  and must never be summed as independent allocation work.

### `MV-1` counts and incompatible calibration alternatives

- Outer DGP words/conversions are bounded by `R(66n+4D)`; first-presentation
  and repeat events are bounded by `20nR` and `DR`. Bootstrap words/indices are
  bounded by `2nRB`; q recomputations, max-`t`, FE, and LOO are bounded by
  `R(B+1)`, `R`, `R`, and `10R`. Every reached max-`t` selection uses fixed
  component order and inclusively constructs all three lower bounds as
  `qhat - critical*SE`; those constructions are part of the same composite
  unit and are not counted again.
- The ledger separately exposes screen-fidelity and q-distribution lookups,
  patient/rating inverse transforms, coverage expits/lookups, state
  softmax/lookups, clip/round events, and every repeat match/renormalization
  path. Three ten-reader static effect vectors contribute 30 inverse-normal
  calls and the three state base logits contribute three log calls per cell.
  Each of those three vectors also has its own mean/population-SD
  normalization. Four-of-five panel votes, panel means, complete block
  evaluability, and patient-q reductions are counted separately.
  One additional composite tally assembly per committed record computes the
  four screen-stratum-by-assigned-polarity counts; it excludes DGP,
  q-studentization, and classification work.
  Expit and three-class softmax composite counts are paired with explicit
  primitive-exp and normalization alternatives; optional log-sum-exp remains
  separately bounded. Accounting roles forbid summing a composite kernel with
  its primitive implementation.
- A successful two-polarity calibration path has separately
  `185,895,747,584` candidate/solve-vector evaluations and `8,388,608`
  independent validation-vector evaluations (`185,904,136,192` total), 2,162
  alpha solves, 2,162 alpha-bracket checks, 172,960 inner-alpha midpoint
  controls, 177,284 residual evaluations, at most 2,162 inner-alpha cached-
  solution selections, 2,002 scan points, two outer-q
  bracket checks, 160 outer midpoints, 2,000 monotonicity comparisons, and two
  validation passes.
- Before that scan, `I_domain*2` static domain-bound assemblies per candidate
  construct the present/absent admissible mean limits and, for beta candidates,
  the positive shape bounds, where `I_domain=1` only after the endpoint/interior-
  margin and strictly positive shape rules are owner-frozen. The two-point
  branch marks shape bounds structurally inapplicable; this unit excludes scan,
  solve, vector, and static-classification work.
- Each adjacent scan unit computes the raw signed decrease
  `selected_q_i-selected_q_{i+1}` without zero clamping, applies the strict
  `>1e-6` test, and updates a fixed ascending-order maximum/argmax with the
  smallest zero-based preceding adjacent index on ties, including when every
  decrease is nonpositive. Each q evaluation is
  blocked until the paired inner-alpha selection rule is frozen. At most two
  outer final-solution selections then
  choose a cached `(mu_Y,alpha_Y)` pair and retain its signed residuals; the
  selection rule remains owner-blocked. At most two subsequent parameter
  constructions emit beta shapes or a two-point mixing probability. Two exact
  control-record assemblies copy the realized per-polarity counters without
  repeating these numerical units.
- Materialization consumes at most 335,544,320 raw words once per candidate.
  Full replay consumes at most 5,948,932,358,144 raw words per candidate.
  These are mutually exclusive complete alternatives. A resource analysis may
  not combine materialization's raw-word count with replay's storage behavior.
- Conversion is a second exclusive choice: replay converts 32 words per
  vector evaluation; raw materialization may either reconvert those words per
  evaluation or create an additional open-unit binary64 cache by converting
  each materialized word once. The compiler retains all three conversion
  alternatives and the cache-byte term; it selects none and forbids mixing
  their cheapest components.
- Per candidate vector, the ledger separately counts 11 normal inverses, one
  beta inverse or two-point lookup, ten coverage expits, ten state softmaxes,
  ten categorical lookups, ten clip/round events, and one fixed-order reduction.
  These are semantic events, not an asserted low-level operation count.
- One MV static-classification assembly per candidate covers all per-polarity/
  residual states, distribution-specific inapplicability, calibration status,
  eligibility, and failure precedence. One outer-classification assembly per
  committed record covers yield/q/coverage/FE/30-LOO comparisons and all
  state/event/failure/status outputs. A separate aggregate-record assembly
  exists for every manifest candidate. On `I_complete=1`, exactly `17R` shared base
  counter updates feed all ordinary intervals; complete-q and complete-joint
  counts are reused for null and planning checks. Exactly 17 distinct event
  proportions are evaluated, with those two values reused rather than divided
  again for the null and planning output records.
- Realized calibration, evaluable-unit/bootstrap, interval-call, repeat-metric,
  permutation-byte, and retry work remain upper-bound or unresolved as marked.

### Reproduction

```bash
python scripts/compile_simulation_semantic_count_ledger.py
python scripts/compile_simulation_semantic_count_ledger.py --registry metrics
python scripts/compile_simulation_semantic_count_ledger.py --registry operations
python scripts/compile_simulation_semantic_count_ledger.py --ledger
```

The first three outputs must be byte-identical to the tracked summary and two
registries. The final command streams the 1,242,518-row ledger to standard
output; the repository tracks only its row count and complete-file hash.

## Storage Reconciliation

| Term | Exact or conditional value | Interpretation |
| --- | ---: | --- |
| Common prefix | 72 bytes | Includes distinct failure/event masks and deterministic execution-sidecar join key; mutable retry provenance is external |
| Reliability state/core | 8 + 256 bytes | 32 two-bit states and 32 eight-byte typed slots |
| `MV-1` state/core | 16 + 512 bytes | 64 two-bit states and 64 eight-byte typed slots |
| Reliability outer record | 336 bytes | `72 + 8 + 32*8` |
| `MV-1` outer record | 600 bytes | `72 + 16 + 64*8` |
| Cell catalogue | 5,967,690 bytes | Exact `sum_i(42+L_i)` |
| Cell-static locks | 1,487,920 bytes | Exact `13,285*112` |
| Completion bitmaps | 199,275,000 bytes | Exact `13,285*15,000` |
| Conditional all-candidate core outer records | 612,887,040,000 bytes | Upper envelope in `MV-1` outer eligibility |
| **Conditional full-candidate core floor** | **613,093,770,610 bytes** | Lower bound after adding catalogue/locks/bitmaps; extensions excluded |
| Superseded TB-0010 floor | 572,492,490,610 bytes | Missing required state/event and retry-join semantics |
| Exact correction | 40,601,280,000 bytes | Same conditional path and non-record terms |
| Final persistent upper bound | **Not identifiable** | Requires all extension counts, format/container, retry, redundancy, and retention decisions |

No TB-0010 capacity statement survives as evidence that a 1-TB allocation is
sufficient. Decimal GB is used only for readability; the registry preserves
the exact byte integer.

## Finite Blocker Register

| Blocker | Required owner decision | Consequence if unresolved |
| --- | --- | --- |
| Reliability truth reference | Select the prospective 41/61 reference rule and nonconvergence consequence. | Coverage, null classification, false-promotion applicability, and static bytes remain open. |
| Reliability ambiguity/repeat domains | Freeze abstract item identities, `H_g`, `D_g`, permutations, and exact repeat outputs. | DGP/repeat counts remain bounded; permutation and repeat-extension bytes remain unidentified. |
| Reliability missingness bisection | Freeze signed residual direction, inclusive endpoint-zero bracket predicate, nonfinite behavior, midpoint-zero equality, endpoint update, post-100 candidate, and tie rules. | Required bracket/intercept/residual states, truth reachability, and outer eligibility remain open. |
| `MV-1` numerical domain and nested/final solution | Freeze closed scan endpoints or an interior-margin rule, a strictly positive beta-shape bound, every inner-alpha residual/bracket/equality/update/final-selection rule, and the cached post-80 outer-midpoint final-candidate/tie rule. | Inner alpha, the 1,001-point q grid, beta numerical extrema, final parameters/residuals, and downstream eligibility remain open. |
| `MV-1` truth and calibration trace | Select target versus independently validated calibrated truth and exact retained trace depth. | Coverage truth, static extension size, and outer/family semantics remain open. |
| Failure precedence/component taxonomy | Approve or amend the recommended precedence, masks, retry and infrastructure rules. | Schema is not implementation-ready. |
| Reference algorithms/software | Freeze inverse CDF, exact-binomial, FE/LOO, rounding, and any owner-added sensitivity algorithms and versions. | Numerical domain, semantic-to-kernel mapping, and conformance cannot close. |
| Resources | After the above, authorize a separate generic artificial-buffer benchmark and allocate CPU/RAM/scratch/storage/I/O/wall/cost contingency. | Runtime, capacity, feasibility, and `G0-RESOURCES` remain unidentified. |

## Kill Rule and Permitted Claim

Stop before a benchmark if any required output lacks a code/type/state/
applicability/aggregate rule; any extension lacks a finite occurrence/byte
bound; a lower and upper path are mixed; a scientific choice is inferred from
cost; observed-reader diagnostics are silently added to every outer
replication; or an unresolved term is assigned zero. Stop or narrow the route
if later proof-preserving resource qualification fails. Never reduce 120,000,
9,999, the candidate family, hard cells, 108, or `0.10` after seeing outcomes
to make the design fit.

The permitted claim is limited to:

> The repository contains complete static freeze candidates for the simulation
> output registry and hardware-neutral semantic-operation ledger, with
> unresolved choices explicitly blocking any later benchmark or resource
> qualification.

This is not owner approval, scientific-implementation correctness, runtime,
capacity, allocation, feasibility, statistical operating performance, reader
reliability, `MV-1` validity, clinical benefit, Gate-0 closure, venue readiness,
acceptance, or publication.
