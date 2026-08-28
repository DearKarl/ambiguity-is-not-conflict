# Baselines and Ablations

**Status:** Candidate comparison matrix; exact implementations await Gate 0

The scientific comparison asks whether an explicit conflict component adds
information beyond simpler predictors under the same backbone, split,
preprocessing, task output, and calibration budget wherever technically
possible.

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
| Uncertainty-adjusted compatibility | CONFER's modality-specific uncertainty-adjusted compatibility or an exactly documented task-valid reimplementation | Is conditional conflict already captured by confidence-adjusted modality compatibility? |
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

The expanded rows are mandatory threats for the confirmatory comparison plan,
not permission to turn the Month-3 kill test into a method zoo. Method identity,
official implementation, licence, and task-valid porting must be frozen before
outcomes are inspected; see the [novelty audit](novelty_audit.md).

## Required Ablations

- remove \(C_{vt}\) from the risk model;
- remove \(A_v\), \(A_t\), \(M_v\), or \(M_t\) separately;
- replace distributional representations with matched point embeddings;
- hold mean embeddings fixed while ablating learned scale/covariance where the
  architecture permits;
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
- comparable trainable parameter and tuning budgets, with differences reported;
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
