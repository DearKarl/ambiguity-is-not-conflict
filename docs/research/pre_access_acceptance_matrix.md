# Pre-Access Acceptance Matrix

Date: 2026-09-20. Evidence class: prospective protocol acceptance, not executed
tests or scientific evidence. Authority: EC-2026-09-20-001; source baseline
`585be42d47a86b84a16bbf986d83e96f37145306`.

The [specification](pre_access_readiness_specification.md) defines status labels
and source versions. The [decision package](pre_access_decision_package.md)
names outstanding owner choices. Documentation checks below are current-task
checks; all data/model/reader/statistical acceptance cases are future designs,
not fixtures created or run here. No acceptance row grants execution authority.

## Package and evidence acceptance

| ID | Object and review method | Acceptance evidence | Failure action |
| --- | --- | --- | --- |
| P01 | Compare all 24 dossier IDs and DR-0018 remaining rows against the decision crosswalk. | Each has source, status, owner, finite choice, dependency and stop consequence; approved rows remain bounded. | Return incomplete package; no inferred default approval. |
| P02 | Inspect every proposed executable field and number. | Exact rationale, alternative and owner gate; missing evidence is named precisely rather than filled with an arbitrary constant. | Block dependent freeze/implementation. |
| P03 | Review stage semantics and claims. | Package-complete, decision-freeze-ready, operational-ready and scientific-pass remain distinct; Method A and sole Main Track objective retained. | Correct misleading readiness or promotion wording before publication. |
| P04 | Review E01--E09 evidence ledger in the specification. | Each row accurately records present/missing/historical state, accountable role, exact required evidence and validity/expiry/stop rule. Package acceptance does not require or claim possession of all external receipts. | An omitted or inflated state fails the package review. Missing/expired/mismatched actual evidence stops the later dependent stage; full stage prerequisites are B01. |
| P05 | Verify repository boundary and existing validation. | Only seven authorized files changed; existing pytest, final checker, diff and bounded privacy review pass. | Repair within scope; never modify tests to make this packet pass. |

## Prospective Stage-B acceptance

Source: [DDR](dataset_decision_record.md), [dataset candidate](dataset_decision_candidate.md)
and [governance](data_governance.md). Status: source-derived readiness logic;
future test implementation and query require a separate contract.

| ID | Object and method | Exact expected result/evidence | Failure action |
| --- | --- | --- | --- |
| B01 | Validate command, environment, access and schema before file open. | Gate-0 record, current Stage-B EC/brief, E01--E08 scope evidence, exactly four files/allowlisted fields, query/test hashes, secure path and approved limits. | STOP before access on any missing prerequisite or extra field. |
| B02 | Schema-only future cases: duplicate image key, non-unique study mapping, cross-split patient, duplicate label key. | Each malformed case is rejected before aggregate export; no permissive deduplication. | STOP query and review the exact mapping fault. |
| B03 | Missing metadata, invalid geometry and label absence. | Split-to-metadata left join preserves all rows; count study images before eligibility; missing view is not frontal; positive geometry required; labels joined only after outcome-blind study selection. | Reject cardinality loss or label-dependent selection; retain aggregate exclusion counts. |
| B04 | Patient partition and rank conformance. | Canonical-ID/HMAC known-answer specification, full-digest unsigned big-endian conversion, no label-dependent ranking, one eligible study per patient, official validation/test roles preserved. | STOP on key/encoding/rank/split mismatch; no patient movement to fill a pool. |
| B05 | Leakage and qualification reserve. | Every source sibling/connected component has one partition; chosen qualification reserve is excluded before fitting from all development/protected/target populations. | STOP/reopen; no row-wise random split or reserve reuse. |
| B06 | Report-screen strata. | Positive agreement, negative agreement, uncertain, disagree, one-sided mention and unmentioned are exhaustive and exclusive; uncertain precedence retained; no screen label treated as image truth. | Reject unknown values or overlapping strata; review before access continues. |
| B07 | Screening-yield aggregate review. | Month-3 130+130; two-control confirmation 190+190; four-control confirmation 235+235; calibration 250; target 380 with >=50 per report-screen polarity; ambiguity recruitment 100 uncertain+disagree. These source planning floors are not observed facts or downstream power. | Shortfall stops/reopens the route; two-control yield cannot certify four controls. |
| B08 | Later independent evaluability review, distinct from B07. | Month-3 >=108+108; two-control confirmation >=160+160; four-control >=200+200; attrition <=20%; excess majority downsampled by frozen keyed rank. MV qualification has its separate >=108 per-polarity gate. | STOP on minority shortage or excessive loss; no outcome-based top-up or report-label substitution. |
| B09 | Rendered disclosure table and release-ledger attack review. | Cells <20 and reconstructing complementary cells/totals/percentages/cross-release overlaps suppressed; only approved aggregate/hash output. | Reject export if subtraction or repeated releases reveal a suppressed cell. |
| B10 | Completion record and next-stage handoff. | Actual authorized access date, immutable resource/query/test identities, aggregate cohort flow, invariant/disclosure decisions and measured resource use. | Passing screening alone cannot authorize images, readers, models or experiments. |

## Prospective measurement and control acceptance

All scientific results in this section are **NOT RUN**. Numeric rules are
source-derived proposals requiring the named G0 decisions, not validated
universal thresholds. Evidence means the later authorized receipt required.

| ID | Object/stage and method | Acceptance and required evidence | Source/status and failure action |
| --- | --- | --- | --- |
| R01 | Modality schema and partial construct. | Frozen precedence cases, raw ratings and undefined-state audit; pair review leaves unimodal records immutable. | Annotation protocol; proposed G0-ONTOLOGY. Reject mixed/incoherent states; never recode undefined as compatible. |
| R02 | Independence and blinding. | Patient/source disjointness; exact disjoint sibling and mutually exclusive modality/pair rosters; blinded UI and immutable presentation ledger. | Reader audit; proposed G0-READERS plus external E07. Any overlap/leak stops the affected stage. |
| R03 | Reliability, separately on every axis. | 9,999 stratified whole-cluster percentile bootstraps, seed 20270832, sorted ranks 250/9750; alpha>=0.80, lower95>=0.67, macro>=0.85, every class-positive agreement>=0.75; missingness<=0.05 and reader/arm spans<=0.05; exact intended quotas. | Reader audit, Reliability Interval and Precision Contract. Any undefined observed/resampled alpha or required denominator fails as non-estimable; no redraw, pooling, refill or sensitivity rescue. |
| R04 | Authorized 60-source timing/rubric pilot. | Median image<=2.5 minutes, text<=45 seconds, pair<=2 minutes; roster available; projected stage<=500 and cumulative<=1,350 person-hours. At most one clarification/requalification before locked reliability. | Budget/annotation protocols; proposed limits. Overrun or unavailable roster stops/reopens; rates are not measured facts. |
| R05 | Later pre-reader simulation qualification. | All 10,847 reliability and 2,438 MV candidates; 120,000 outer identities and 9,999 inner analyses. Reliability false-promotion upper CP95<=0.055; marginal-coverage lower two-sided CP95>=0.945; all 4,416 planning rows, alpha=0.05/4416 and 15-axis sum(1-L_axis_min)<=0.10. MV false-qualification upper CP95<=0.055; simultaneous-coverage lower two-sided CP95>=0.945; joint yield+q+no-veto lower two-sided CP95>=0.90 in every one of 2,304 planning cells. Full x=0..120000 exact-binomial half-width scan maximum<0.003. | Reader audit, Operating criteria; output registry. NOT RUN; only later approved implementation/run. Failed calibration retains a failed member; no pruning or smaller counts. |
| R06 | Observed MV-1 qualification. | >=108 evaluable independently image-labelled blocks per polarity; 9,999 within-polarity whole-patient max-t resamples, seed 20270833; critical max(0,9500th sorted maximum); joint L_bal>0.10, L_present>0, L_absent>0. | Reader audit, MV-1 Interval and Joint Gate. Any invalid observed/resampled SE fails; no redraw or inference from screening/pixel loss. |
| R06s | MV reader sensitivity. | Constrained patient/reader fixed-effect model, SVD cutoff 1e-12, all ten leave-one-reader analyses with full E/Y fixed. | Reader audit, Reader/panel sensitivity veto. Any FE/LOO polarity<=0, non-estimability/rank failure, or absolute balanced change>0.05 vetoes; sensitivity cannot rescue R06. |
| R07 | MT byte/token carrier audit and blind 3/3 text classification. | Target identity retained; no recoverable/contrary polarity or other state carrier; intended task-critical loss accepted. | Intervention audit, MT-1. Leakage, conventional-polarity inference or missing identity rejects/reopens; no post-score replacement. |
| R08 | Construction and artifact audit. | Each image equally paired with both compatibility states; exact strings/templates/process paths balanced across image polarities within partition; frozen image/text/nuisance/provenance probes. R=max(BA,1-BA); lower>0.55 kills, crossing 0.55 inconclusive, upper<0.55 supports only the exact probe/population. | Statistical plan, Artifact-Condition Recoverability Audit; proposed G0-ARTIFACT A. Hidden condition fields, unequal sibling processes or duplicate leakage fail before scoring; non-significance is not equivalence. Control-arm audit excludes deliberately changed modality and verifies unchanged-modality identity; manipulated-modality recovery is fidelity. |
| R09 | Natural ambiguity veto. | Independent locked labels, common score scale, frozen nuisance/support/weight audit, gamma/phi and declared sensitivity. | Task/estimand E3 plus Engineer proposal in specification. Missing support/non-estimability blocks; nonpositive phi or unstable verdict vetoes. No causal-separation claim on survival. |

Post-access screening/evaluable-yield checks are B07/B08, with the additional
150+150 MV reserve only if G0-MV-Q A is selected. They do not establish
calibration/target power or intervention validity.

## Prospective instrument, inference and claim acceptance

Status: protocol design, **NOT RUN**. Source-derived invariants retain canonical
authority; EX-A implementation fields and probe choices are proposed and need
the explicit decisions in the companion packet.

| ID | Object and method | Exact expected evidence | Failure action / claim limit |
| --- | --- | --- | --- |
| I01 | EX-A rendering, tokenizer and feature conformance. | Immutable software/config hashes; byte/tensor fixtures for geometry, MV half-pixel rule, text overflow and L2 normalization; same P/D inputs; finite 512-dimensional outputs. | Any mismatch, truncation or zero norm fails. No provider-exact preprocessing claim for proposed geometry. |
| I02 | Graph, objective and initialization audit. | Realized P=4,727,808 and D=2,627,584 excluding encoder for the proposed graph; exact four-term objective; fixed global D constants; same shared initial arrays/patient order; seeds 0/1/2 and no best-seed substitution. | Nonfinite numerical domain fails without clipping/retry rescue. Counts are currently analytic, not measured. Unequal capacity remains disclosed. |
| I03 | Fitting/development provenance. | Approved native atomic extraction, independent compatible selection, reserve exclusion, fixed fit/tune/normalizer buckets and protected roles; per-route earliest tune-minimum epoch under equal trial ceilings. | No control/error/provenance leakage, label-based reranking, test selection or post-failure search. Compatible selection is supervision. |
| I04 | Secondary POINT-INFONCE mask. | Explicit owner choice, positive/negative eligibility and same-source exclusion fixtures; empty-side batches fail; semantic mask labelled privileged if selected. | Never promote secondary result to primary or infer a general point-method deficit from false negatives. |
| I05 | Component construction and nonlinear order. | Opposite signed control responses reduce psi_mag despite psi_id cancellation; differing P/D minimizing controls produce difference of minima; patient-level minima are never averaged as psi. | Any swapped estimand fails. Preserve each method's own normalizer. |
| I06 | Bootstrap family and degeneracy. | Exactly 9,999 common within-stratum whole-patient indices, seed 20270829; fixed normalizers, weights and families; exact signed maxima/ranks and bound algebra; every identity accounted. | A single required zero/undefined observed/resampled SE fails; no redraw, epsilon or discarded samples. |
| I07 | Leakage and scale invariants. | Duplicate sibling rows cannot increase patient n; missing sibling invalidates block; positive affine score rescaling leaves standardized result invariant. | Unmatched nonlinear links or changed normalizer populations invalidate comparison. |
| I08 | Promotion logic. | Month-3 90%/80% and confirmation 97.5%/90% family inference/power; approved specificity then advantage then proper-score then utility sequence. | Failure kills current route where prescribed; framework value cannot rescue A_psi failure. Non-superiority is inconclusive, not equivalence. |
| I09 | Simpler-method conclusion. | D absolute Lpsi>0.20 plus UA<0.10 for construct noninferiority; confirmatory 95% simultaneous band within [-0.10,0.10] for equivalence; separate downstream noninferiority for subsumption. | Any missing component narrows claim; no equivalence from a nonsignificant difference. Numeric margins remain proposed until approved. |
| I10 | All six ablation families. | Frozen stage/input/output/claim ledger and valid matched substitute for any structurally absent term; no sensitivity-selected winner. | Full-route comparison cannot claim capacity parity; frozen means cannot claim training-path causal isolation. |
| I11 | Eight proposed PR-A artifact pipelines and R orientation. | Owner-approved dictionaries/Newton/CART work bounds and 999 whole-patient swaps (8,000 fit ceiling), finite later resource bounds; conditional fixed-probe Hoeffding intervals with K=8 and frozen strata, correctly transformed to R, lower=0.5 when spanning 0.5. | Wrong orientation cannot pass; missing independence/conformance/resource evidence blocks freeze; conservative intervals do not establish powered equivalence or replace psi/MV inference. |
| I12 | Decision-time feasibility. | Exact Yhat/abstention/proxy feature maps, supervised label provenance and access/cost; no unavailable reader labels or condition/provenance in automated decisions. | Either repair the feasible design or label reader-assisted/oracle explanation; no automated utility claim. |
| I13 | Natural-target scoring, calibration and power. | Independent H, frozen null/target weights, paired DeltaBSS/A_BSS, target effective n/event rate/covariance/complexity and cost; separate power lock. Proposed gates >0.02, >0.01; probability-scale absolute calibration-in-the-large error<=0.02 and slope [0.80,1.20] via approved equivalence interface; risk reduction>0.01 at 90% coverage. | Logistic recalibration intercept has log-odds units and cannot inherit probability tolerance. Exact evaluation interval needs owner freeze. Controlled-pair success/screening counts cannot establish natural-target utility, transport or clinical benefit. |
| I14 | Checkpoint and external evidence. | Exact checkpoint/tokenizer/software identity, rights, exposure statement, access/storage/resource receipts and narrow source attribution. | Unknown pretraining exposure forbids strict unseen/contamination-free claim. No checkpoint download or software freeze is implied by this packet. |
| I15 | Proposed NA-A extraction. | Earliest original-byte span selected before ratings; section/lexical/segmentation rules, no rewrite or later-span rescue; independent single-proposition text/image agreement; secure offsets and aggregate attrition only. | Clinical owner selects NA-A/NA-B before access; poor yield reopens, never manufactures compatible fitting positives. |
| I16 | Proposed DY-A dataflow and proxy complexity. | Disjoint 0-39 fit/40-49 tune/50-59 risk/60-69 normalization after reserves; common task classifier, modality-only proxies, frozen risk maps and optional finite committee; all category/support/solver/refit costs accounted. | No unavailable oracle input, task-failure-as-correct-abstention, absent-category pooling or zero-filled epistemic control. Each new supervised model needs explicit labels/budget/authorization. |
| I17 | Proposed DC-A policy. | Same eligible target and floor(0.90N) answers/review count for P/D, deterministic private-rank ties, error measured among answered, actual counts/coverage reported. | No assumed perfect reviewer or net clinical utility. DC-B needs independent loss-table evidence and new power lock. |
| I18 | Proposed CAL-A equivalence evaluation. | Unit-weight c=mean(p-H), distinct free-intercept diagnostic slope with HC0 patient sandwich; common 9,999 unstratified target resamples/domain, six-coordinate absolute-max family/rank9500; all 30,000 fits counted. | Separation/missing class/invalid SE or any failed indexed fit makes analysis inconclusive; no redraw. Whole c/slope bands must satisfy probability [-0.02,0.02]/slope [0.80,1.20] for named required maps. Owner adoption, power/operating properties/software/resources remain unapproved. |

## Prospective resource acceptance

All resource computations/benchmarks below are future checks, **NOT RUN**.
Exact R-S1--R-S8 recommendations and alternatives are in the decision package;
the canonical registry/design retain authority. These rows add no allocation.

| ID | Object and required evidence | Failure action |
| --- | --- | --- |
| C01 | Owner-signed truth/domain/solver/repeat/status/algorithm choices R-S1--R-S7; complete typed fields, finite operation/byte bounds and P0--P11 conformance plan. | Any undefined domain, reference uncertainty, enum, repeat cost or unbounded trace blocks compiler/benchmark authority. |
| C02 | Full storage upper bound above conditional 613,093,770,610-byte floor, all extensions/journal/attempt/failure/format/redundancy/backup terms; concurrent writer copies and temporary scratch separate. | One missing finite term means no capacity verdict; floor is not a complete estimate or Stage-B budget. |
| C03 | Materialization/replay/cache alternatives each include their own complete operation, storage, concurrent RAM and scratch accounting. | Do not combine the cheapest terms from incompatible strategies or assume near-zero beta shapes have bounded cheap cost. |
| C04 | Separately authorized generic benchmark with all kernel domains, tails/failures, hard attempt ceilings, restart/I/O/scheduler costs, actual named allocation and explicit service-level definition. | A 299-block tolerance diagnostic is not a completion bound; no scientific project RNG/DGP/bootstrap hidden in a benchmark. No paid compute under current EC. |
| C05 | Later unchanged full simulation manifests and all required null/coverage/power families retained; scientific failure distinct from infrastructure incompletion. | No lower outer 120,000/inner 9,999, pruned grid, weaker gate, deleted failed cell or invented scientific result from incomplete infrastructure. |
