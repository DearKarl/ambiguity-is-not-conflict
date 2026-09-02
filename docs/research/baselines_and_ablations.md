# Baselines and Ablations

**Status:** Method-A Commander-level interfaces frozen; supervisor agrees with
the named primary/secondary roles; statistical/model, full baseline/ablation,
and exact implementation approvals await Gate 0

The scientific comparison asks whether a frozen score's intervention-relative
response adds information beyond simpler predictors under the same backbone,
split, preprocessing, task output, and calibration budget wherever technically
possible.

TB-0006 selected no new pointwise estimator. Self-corrected learned-belief/
Gaussian disagreement collapses to a matched deterministic mean score,
conditional density ratio is a prior-adjusted deterministic classifier logit,
and evidential confident disagreement is an occupied RCML/Discounted-Belief-
Fusion form. These methods can remain instruments or comparators, but none may
be promoted as a novel estimator from development results.

## Required Baseline Families

| Family | Candidate role | Question it answers |
| --- | --- | --- |
| Task confidence | Logit margin, sequence confidence, or task probability | Does ordinary confidence already rank failures? |
| Deterministic compatibility | Cosine similarity, retrieval margin, or pair score | Is generic image--text mismatch sufficient? |
| Matched deterministic failure predictor | Same inputs/capacity/training budget as the proposed estimator | Does uncertainty structure add value beyond supervised prediction? |
| Image-only uncertainty | Frozen image-only predictor or ambiguity model | Is the signal driven by visual difficulty? |
| Text-only uncertainty | Frozen text-only predictor or ambiguity model | Is the signal driven by wording difficulty? |
| Output semantic uncertainty | Semantic entropy or related meaning-level dispersion when generation is used | Is input conflict redundant with output variation? |
| Probabilistic embedding | PCME/PCME++/ProbVLM-style candidate, plus ICPE where task-valid | Does distributional representation improve source separation after a matched point-softmax and modality-gap/embedding-scale audit? |
| Evidential vacuity/dissonance and reliability | Subjective-logic lack-of-evidence/conflicting-evidence measures and RCML conflict degree/reliability, or exact task-valid analogues on matched categorical heads | Is the claimed ambiguity/conflict split already captured by a known evidential decomposition or reliability-adjusted conflict score? |
| Conflict-discounted evidence fusion | Discounted Belief Fusion or an exactly documented task-valid reimplementation | Does a published uncertainty-based conflict detector subsume the candidate? |
| Uncertainty-adjusted compatibility | Project-native uncertainty-normalized compatibility sensitivity; CONFER is a non-authoritative preprint lead only | Is conditional conflict already captured by confidence-adjusted modality compatibility? |
| Conflict-risk fusion | CoRiM's predictive-distribution conflict-risk principle or an exactly documented task-valid comparator | Is the score or downstream decision effect already explained by conflict-aware dynamic fusion? |
| Relative entropy and source following | Relative unimodal entropy and source-reliance diagnostics from *When Modalities Conflict* | Is the proposed signal merely relative confidence or source preference under conflict? |
| Paired shift diagnostics | SIGNPOST-style Original/Blank/Similar/Random/Adversarial shifts and *Which Source Wins*-style legibility adjustments where task-valid | Can missing, unrelated, adversarial, or degraded inputs explain the claimed specificity? |
| Published task-matched conflict method | MMMC-style conflict/hallucination, CrossCheck-style conflict resolution, or CLASH-style contradiction-detection supervision where the frozen unit and information budget can be matched | Is an existing task-matched conflict method sufficient without the proposed decomposition? |
| Medical phrase fact checking | Phrase-grounded chest-radiograph fact checking when its inputs, supervision, and information budget can be matched | Is the atomic medical compatibility signal already captured by a task-specific fact checker? |
| Epistemic approximation | Ensemble, parameter-efficient ensemble, Bayesian last layer, or Laplace approximation | Is the apparent conflict actually model uncertainty? |
| Generic VLM failure prediction | ViLU and Adaptive Confidence Regularization (ACR), or the closest reproducible task-matched implementations | Is the component useful beyond strong published failure predictors? |
| Finding-level medical failure prediction | ReXTrust or the closest task-valid finding-level medical failure predictor when its frozen unit and interface permit | Does conflict add information beyond a medical hallucination/failure-risk score? |
| Risk control | Post-hoc calibration and conformal/risk-controlling selection where assumptions fit | Does the final selection policy add value beyond score ranking? |

The exact list should be reduced to the smallest matched set that can falsify
the primary claim. A broad method zoo with mismatched backbones is not a strong
comparison.

For the Month-3 gate, freeze only raw deterministic similarity, one matched
learned deterministic compatibility/density-ratio predictor, one evidential
candidate, and one probabilistic/distributional candidate. Require a matched
point-softmax adapter whenever learned scale or covariance is credited. The
closest published conflict methods above must either be represented fairly or
excluded with a pre-results technical and licence justification.

Before the Month-3 holdout is opened, every remaining required owner must
approve the Commander-frozen, supervisor-role-aligned pair: the explicitly
non-novel `PROBVLM-2ADAPTER`
instrument and `POINT-2ADAPTER-RECON` matched deterministic comparator. Method
A is the sole route; development may fit only those frozen identities and
cannot promote another candidate because it performs best. Declaring multiple
primary instruments requires a prospectively expanded method-by-control and
method-difference multiplicity/power family.

The peer-reviewed expanded rows are mandatory threats for the confirmatory
comparison plan, not permission to turn the Month-3 kill test into a method
zoo. Preprint-only rows are surveillance leads and are not formal kill evidence
or mandatory baselines unless their status changes before the prospective
freeze. Method identity, official implementation, licence, and task-valid
porting must be frozen before outcomes are inspected; see the [novelty
audit](novelty_audit.md).

The current [backbone/resource freeze candidate](execution_budget_and_backbone_audit.md)
places those Month-3 heads on one conditional dual-encoder candidate with
frozen encoders, at most 20 million trainable parameters per matched
head/adapter, and a shared 300-GPU-hour stage ceiling. BiomedCLIP is only a
conditional primary candidate; SigLIP2 is an unknown-exposure matched breadth
candidate; BioViL-T is a known-MIMIC-exposure diagnostic; and a ResNet-50 plus
BiomedBERT pair is a lower-intent, unknown-overlap non-VLM architectural/
sensitivity control; it is neither contamination-negative nor strict-
confirmatory. No checkpoint is approved or presumed clean.

## Finite Implementation and Information-Budget Candidate

The read-only TB-0006 audit reduces the Month-3 implementation roles to the
following candidate identities. They are not approved or executable:

| ID | Frozen role candidate | Supervision class | Implementation/licence boundary |
| --- | --- | --- | --- |
| `RAW-COS` | \(1-\) cosine of normalized frozen post-projection BiomedCLIP features, without logit scale or softmax | No trainables or project labels | Project-native arithmetic; zero-capacity reference |
| `DET-LR` | Project-native binary-log-loss classifier over \([z_v,z_t,|z_v-z_t|,z_v\odot z_t,W]\), reported as classifier logit plus known sampling-prior correction | Explicit determinate \(C^*\) labels | Privileged supervised ceiling unless every claimed matched method receives the same labels; exact \(W\), architecture, weights, and calibration remain open |
| `DBF-TASK` | Two task-aligned binary evidential heads and the published DBF fusion/conflict quantities, trained on clear compatible pairs | Shared semantic finding \(Y\) | Official [DBF code](https://github.com/bezirganyan/DBF_uncertainty/commit/79b7d56b0cfa53c98a93f29f9d9c59768177ad17) is GPL-3.0 and credits RCML code; the audited [RCML snapshot](https://github.com/jiajunsi/RCML/tree/c9c5ab41e6fe62a85e5f6441a4dc7b568e1fa421) exposes no explicit licence file. No vendoring. Requires an approved clean-room formula port or separately governed GPL runner subject to licensing/provenance approval |
| `PROBVLM-2ADAPTER` | Paper-faithful-likelihood, project-native two-adapter symmetric cross-modal generalized-Gaussian negative log-likelihood at official [ProbVLM commit](https://github.com/ExplainableML/ProbVLM/commit/cb69f28b1ab23142a1c671e004b09b5cb5d8a204) | Independently verified determinate-compatible fitting-set membership, shared with the point route; this is disclosed semantic selection supervision, while semantic labels are not inputs or loss targets | MIT; Commander selected paper-faithful likelihood rather than code-exact semantics. The coordinate reduction and complete objective are project choices. No original checkpoint or constructed contradiction as a positive fit pair; executable details remain owner-blocked |
| `POINT-2ADAPTER-RECON` | Project-native two-branch mean-only reconstruction adapter with the same frozen inputs, verified-compatible records, mean trunks, target topology, optimization/tuning budget, and GGD score family; global coordinatewise scale/shape constants are fitted on the same compatible fit/development objective and frozen before protected outcomes | Exactly the same fitting-set selection information as `PROBVLM-2ADAPTER`; no semantic label is an input or loss target | Primary deterministic full-route comparator; unit-scale Laplace is a sensitivity only. Removing scale/shape heads changes active capacity and gradient paths, so this is not a capacity-isolated mechanism test. No inherited third-party adapter code; executable architecture and numbers remain owner-blocked |
| `POINT-INFONCE` | Project-native two-branch point adapter on the same native records; contrastive paired logit | Same records but additional off-diagonal negative assumptions | Secondary baseline only. The closest [CLIP-Adapter snapshot](https://github.com/gaopengcuhk/CLIP-Adapter/tree/08d07f8b2ecafc6f1479fe636b26d464d7a5574e) is a different classifier and exposes no explicit licence file at the audited snapshot; exclude its code and separately freeze denominator, multi-positive/false-negative, temperature, optimizer, and tuning rules |

The proposed common feature identity is BiomedCLIP snapshot
[`9f341de24bfb00180f1b847274256e9b65a3a32e`](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224/commit/9f341de24bfb00180f1b847274256e9b65a3a32e)
through OpenCLIP 2.23.0 commit
[`f08f25f3f226bdb538de2b4ed48a9213ba6b179e`](https://github.com/mlfoundations/open_clip/commit/f08f25f3f226bdb538de2b4ed48a9213ba6b179e);
both publish MIT terms. This is an immutable identity lead only and does not
resolve the documented pretraining-exposure limitation or authorize a
checkpoint download.

Only `PROBVLM-2ADAPTER` versus `POINT-2ADAPTER-RECON` is the primary
same-selection-information, same-score-family, and same-target-topology
comparison. It compares complete routes, not capacity-matched probabilistic
mechanisms: exact active/trainable parameter counts, training compute, and
inference cost must be reported. `POINT-INFONCE` is a secondary same-records
contrastive challenge; `DET-LR` and `DBF-TASK` are distinct privileged ceilings,
not information-matched competitors. At
inference, no method may
receive intervention identity, construction source, ambiguity/artifact label,
provenance field, or protected outcome. The exact implementation, calibration,
software dependency, parameter-count, and supervision ledger must be approved
before Gate 0 closes.

## Required Ablations

- remove \(C_{vt}\) from the risk model;
- remove \(A_v\), \(A_t\), \(M_v\), or \(M_t\) separately;
- replace `PROBVLM-2ADAPTER` with `POINT-2ADAPTER-RECON` under the frozen
  information, score-family, topology, optimization, and capacity-disclosure
  ledger;
- hold fitted ProbVLM means fixed while replacing input-dependent scale/shape
  with the point comparator's frozen global constants; this diagnoses only the
  direct score path conditional on jointly trained means;
- alternative valid normalization and latent dimension;
- alternative conflict quantity chosen before confirmatory evaluation;
- intervention source: natural, rule-edited, model-generated, clinician-edited;
- no-corruption versus matched-corruption controls;
- image-only, text-only, and nuisance-only probes for conflict-cell recovery;
- unrelated-finding change and semantics-preserving rewrite controls;
- missing assertion versus contradictory assertion;
- label-permutation and template/provenance probes;
- calibration-set size and calibration method;
- seed, backbone, finding type, and declared shift robustness.

## Fairness Rules

- same patient partitions and derived-pair inheritance;
- same access to labels and decision-time information;
- prospectively bounded trainable parameter and tuning budgets, with exact
  active-parameter, gradient-path, compute, and inference-cost differences
  reported rather than described as capacity parity;
- identical pre-link/post-link convention for every matched comparison:
  compatible-reference standardization is not invariant to squaring, sigmoid,
  exponential, or another nonlinear monotone transformation;
- no final-test threshold selection;
- no use of intervention labels as model inputs unless that is the explicitly
  evaluated supervised baseline;
- record runtime, peak memory, hardware, total compute, and failed runs.

## Primary Incremental Comparison

On the separately sampled natural target cohort, the confirmatory comparison
should be a paired held-out contrast for independently labelled image-grounded
task error \(H\) between:

```text
baseline risk model: A_v + A_t + M_v + M_t + ordinary confidence
                     + eligible U_epi/U_out
```

and

```text
augmented risk model: baseline terms + C_vt
```

with a separate matched deterministic failure predictor as the strongest
non-decomposed comparator. Promotion requires more than a favourable AUROC; it
requires the frozen proper-score or decision endpoint and calibration evidence.

Construct promotion additionally requires the magnitude-safe endpoint and
0.10 probabilistic-instrument material advantage over the deterministic comparator in
the
[statistical analysis plan](statistical_analysis_plan.md). Failure to
demonstrate probabilistic-instrument superiority is not evidence of equivalence;
deterministic subsumption must meet the plan's positive absolute,
non-inferiority, and downstream conditions.
