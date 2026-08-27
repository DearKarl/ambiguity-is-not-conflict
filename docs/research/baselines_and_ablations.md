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
| Probabilistic embedding | PCME/PCME++/ProbVLM-style candidate | Does distributional representation improve source separation? |
| Epistemic approximation | Ensemble, parameter-efficient ensemble, Bayesian last layer, or Laplace approximation | Is the apparent conflict actually model uncertainty? |
| Generic VLM failure prediction | ViLU-style or closest reproducible matched method | Is the component useful beyond a strong published failure predictor? |
| Risk control | Post-hoc calibration and conformal/risk-controlling selection where assumptions fit | Does the final selection policy add value beyond score ranking? |

The exact list should be reduced to the smallest matched set that can falsify
the primary claim. A broad method zoo with mismatched backbones is not a strong
comparison.

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

The confirmatory comparison should be a paired held-out contrast between:

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
