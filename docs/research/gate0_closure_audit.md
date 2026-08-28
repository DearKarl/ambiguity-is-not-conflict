# Gate 0 Closure Audit

**Status:** Freeze candidate; Gate 0 remains open

**Audit date:** 2026-08-29
**Evidence class:** Protocol and decision support under TB-0003, with
TB-0004 independent-review blocker remediation

## Bottom Line

The repository now specifies a single, falsifiable route at substantially more
detail, but it is **not execution-ready**. No approval is implied by this
document. The five scientifically material blockers are:

1. no valid image- or text-ambiguity intervention, or approved observational
   identification/transport route, has yet separated genuine interpretive
   multiplicity from information loss or epistemic qualification;
2. the proposed two-control roles have no clinically approved exact `M_v` and
   `M_t` operation, severity, acceptance rule, or within-source reference, so
   `J_id` and its power rows remain conditional rather than executable;
3. no candidate backbone has yet supplied auditable evidence that its training
   patients or source records are disjoint from the proposed MIMIC final set;
4. the proposed `chance + 0.05` four-probe artifact-equivalence claim requires
   materially more independent patients than the current construct floors
   under the conservative precision/power calculation;
5. the exact primary estimator identity, matched deterministic comparison, and
   downstream event rate/covariance remain unfrozen, so the full `A_psi`,
   `A_BSS`, calibration, and decision sequence is not yet power-ready.

The first blocker limits the identified Month-3 claim to conflict specificity
among determinate cases plus conservative natural-ambiguity falsification. It
does not justify calling blur, masking, compression, or evidence removal an
ambiguity intervention; hedging is not a text-ambiguity route. The second means
even the narrowed specificity family requires clinical/statistical freezing
before execution. The third prevents a strict held-out cross-backbone claim
until checkpoint provenance and patient exposure are resolved. The fourth
means non-significant artifact recovery cannot be called an artifact-
equivalence pass. The fifth prevents the construct sample floor from being
presented as power for the complete Main Track promotion sequence.

## Status Vocabulary

| Status | Meaning |
| --- | --- |
| **Verified** | A repository or official-source fact has been checked; it is not an approval or empirical result. |
| **Candidate** | A complete reviewable protocol option exists but has not been approved. |
| **Approval-blocked** | A named Commander, clinical, governance, supervisor, or resource decision is required. |
| **Feasibility-blocked** | The answer requires a later bounded check in an approved environment. |
| **Not specified** | The contract requirement still lacks a defensible candidate. |

## Requirement-by-Requirement Audit

| Gate-0 requirement | Current freeze candidate | Status | Exact remaining action |
| --- | --- | --- | --- |
| Task and prediction unit | Asymmetric image-grounded binary verification for one finding; `(patient, study, exact single frontal image, finding, atomic text assertion, intervention variant, frozen model)`. Pleural-effusion presence/absence is provisional. | Candidate; approval-blocked | Clinical owner must approve the finding and the two-part screen: reliable technical-integrity/input-coverage assessment, plus a unique image-only state for determinate-source blocks; intact natural-ambiguity blocks may retain `Y_v=undefined`. |
| Dataset, version, access, exclusions, and split | Coupled MIMIC-CXR v2.1.0 reports plus MIMIC-CXR-JPG v2.1.0 images/metadata; patient/source-graph partitions; no access yet. | Candidate; governance- and feasibility-blocked | Approve the pre-access record, secure environment, account/DUA route, and later metadata-only feasibility brief. |
| Ontology and intervention taxonomy | Separate labels for finding state, ambiguity, technical gradability/information loss, missingness, and cross-modal compatibility; conflict is defined only for determinate modality states. | Candidate | Approve the independent annotation rubric and atomic assertion grammar. |
| Image and text ambiguity | Natural ambiguity is independently annotated and used as a falsification audit. An explicit hedge is epistemic qualification, not automatically linguistic ambiguity. No defensible image- or text-ambiguity intervention is currently frozen. | Approval-blocked | Approve either a valid governed intervention/transport estimand or the narrower determinate-conflict claim. |
| Conflict estimand and construct SESOI | Recommended primary endpoint is the magnitude-safe `psi_mag = min_j E[D_C - abs(D_j)]` on a frozen compatible-reference SD scale; signed `psi_id` remains diagnostic because nuisance responses can cancel. The two modality roles are proposed, but their exact operations are unresolved. | Candidate; approval-blocked | Approve one exact `M_v` and one exact `M_t` operation, severity, acceptance rule, and reference; approve the scale, 0.20 specificity SESOI, and 0.10 uncertainty-aware material-advantage margin. `theta` remains secondary unless separately powered. |
| Endpoint, interval, and multiplicity | Month 3 uses one-sided 90% simultaneous development bounds; later confirmation uses one-sided 97.5% patient-cluster max-`t` bounds across frozen identified controls. Natural ambiguity remains outside the causal family. | Candidate | Statistical owner must validate the resampling implementation before execution. |
| Downstream outcome and calibration | Independently labelled image-grounded model error; paired Brier-skill improvement on a natural target cohort, with `A_BSS` against the matched deterministic predictor plus calibration-in-the-large and slope diagnostics. | Candidate; approval- and power-blocked | Approve outcome definition, target population, candidate 0.02 Brier-skill SESOI, 0.01 method-difference margin, event rate/covariance calculation, calibration tolerances, and review budget. |
| Baselines and ablations | Month-3 minimum set: raw similarity, matched learned deterministic predictor, evidential comparator, probabilistic/distributional comparator, and matched point-softmax adapter where applicable. | Candidate | Freeze exact implementations, licences, information budgets, and the pre-results analytic equivalence screen. |
| Backbone and checkpoint exposure | BiomedCLIP and SigLIP2 are low-friction candidates; BioViL-T and CheXzero have explicit MIMIC exposure. No audited checkpoint currently establishes disjointness from final MIMIC patients. | Feasibility-blocked | Complete official training-corpus/split audit and choose a strict-confirmatory architecture or explicitly narrow the evidence class. |
| Development, calibration, and final partitions | Exact HMAC roles separate 70% fit/development, 15% one-time Month-3 advance/kill screening for the already named primary candidate, and 15% untouched construct confirmation within official train; one keyed eligible study per patient is mandatory. | Candidate; feasibility-blocked | Approve algorithm/key custody and reconcile official validation/test roles with checkpoint exposure. |
| Construct and target sampling | Balanced intervention blocks identify the construct; a separate natural, patient-separated cohort supports prevalence-sensitive calibration and decision claims. | Candidate | Freeze natural cohort inclusion, sampling weights, shift, and subgroup minimum sizes. |
| Compute and annotation budget | Explicit planning ceilings and stop rules are proposed in the resource audit; no resource is assumed available. | Candidate; approval-blocked | Commander, clinical owner, and infrastructure owner must confirm ceilings and secure capacity. |
| Breadth | VisMin is the preferred low-friction general-domain stress candidate; PadChest-GR is the preferred independent medical reserve. Neither is a second route or authorized. | Candidate; deferred | Freeze only after the primary construct instrument passes; run a separate licence/governance decision. |
| Promotion, kill, and fallback | Construct failure, artifact recovery, unreliable labels, deterministic subsumption, exposure failure, and insufficient feasibility all have explicit stop consequences. | Candidate | Approve DR-0008; do not weaken a failed estimator into a Main Track method claim. |
| Artifacts, retention, and sharing | Restricted inputs and record-level derivatives remain in an approved environment; only specifically permitted aggregate outputs may leave after disclosure review. | Governance-blocked | Obtain a written DUA/ethics/institutional determination for annotations, embeddings, checkpoints, and counterfactual text. |

## Identification Boundary

### Fact

Randomizing a text polarity within a fixed clear source block can identify the
effect of determinate compatibility under consistency, positivity,
counterbalancing, and no artifact leakage. Image degradation, crop, masking,
compression, or evidence removal changes the information available and is an
`M_v` manipulation unless a separate argument establishes genuine ambiguity.

### Inference

The current defensible primary route is therefore a fractional design:

- identified compatible-versus-conflicting contrast in determinate blocks;
- randomized or counterbalanced surface-form and information-loss controls;
- natural image/text ambiguity as independently measured, matched or weighted
  falsification audits;
- no binary conflict label in an ambiguous or missing cell.

### Assumption Requiring Approval

The intended broad wording—conflict identified *relative to ambiguity*—can be
retained only if the project later supplies either a valid ambiguity
intervention or a separately defended conditional-exchangeability and
transport estimand. Otherwise the claim must be narrowed to controlled
determinate-conflict specificity and association under natural ambiguity.

## Approval Sequence

1. **Scientific boundary:** choose the narrower determinate route or require a
   valid ambiguity-identification route before execution.
2. **Clinical task:** approve the provisional finding, exact-image unit and
   technical-integrity/input-coverage rubric, assertion grammar,
   qualifications, and reliability gate.
3. **Statistics:** approve score normalization, magnitude-safe construct
   endpoint, SESOIs, simultaneous interval, development sample ceiling,
   downstream proper-score SESOI, and deterministic kill rule.
4. **Data/governance:** approve the pre-access MIMIC record, secure processing,
   permitted derivatives, retention, and the later metadata-only query.
5. **Model/resources:** freeze an exposure-audited backbone route and hard
   compute, storage, and annotation ceilings.
6. **Gate-0 record:** sign one dated decision record containing the above and
   issue a new bounded feasibility brief. Approval does not itself authorize
   record inspection, annotation, model use, or experiments.

## Permitted Claim

This audit establishes that the project has a reviewable Gate-0 freeze
candidate and makes its remaining blockers explicit. It does not establish
novelty, construct identifiability, dataset/model availability, annotation
reliability, empirical feasibility, clinical value, Gate-0 closure, NeurIPS
eligibility under the unpublished 2027 call, or publication.
