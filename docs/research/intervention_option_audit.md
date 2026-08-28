# Intervention Option Audit

**Status:** Gate-0 decision support; no intervention is approved or executable

**Date:** 2026-08-29
**Evidence class:** Primary-source literature leads plus protocol inference under
TB-0005

## Bottom Line

The finite primary-control recommendation is:

- `M_v`: deterministic antialiased `224 -> 112 -> 224` spatial-resolution
  attenuation, retained as a **candidate** only when disjoint image panels
  preserve the same determinate image-side finding state and a separate,
  model-independent qualification sample demonstrates non-trivial attenuation
  of task evidence;
- `M_t`: redact the sole polarity-bearing slot of the atomic assertion while
  retaining the finding identity, which makes the text-side state undefined
  rather than ambiguous; and
- retain compression, simulated dose/noise, crop/masking, character noise,
  whole-assertion dropout, hedging, and modifier deletion only in their named
  diagnostic or rejected roles below.

This is one control family for the existing route, not a second scientific
route. Clinical and statistical owners must approve both exact controls before
`J_id` is executable. Neither operation is an ambiguity intervention.

## Evidence Classification

### Verified facts from primary sources

| Source | Fact used | Limit for this project |
| --- | --- | --- |
| [Herron et al., *Radiology* 2000](https://pubmed.ncbi.nlm.nih.gov/10751483/) | Six radiologists read 529 chest radiographs under three pixel resolutions and three luminance levels; resolution effects differed by abnormality, with a statistically significant resolution effect reported for pneumothorax. | It did not study pleural-effusion labels, modern encoder inputs, or the proposed `224 -> 112 -> 224` operation. It shows that resolution cannot be assumed semantically harmless. |
| [Beall et al., *Journal of Digital Imaging* 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC3453278/) | Six radiologists read 150 chest radiographs before and after 10:1 lossy JPEG compression; five of six had higher accuracy on uncompressed images, although the reported difference was not statistically significant. | Non-significance is not equivalence, and the task did not include pleural effusion. The paper does not validate compression as this project's primary control. |
| [Veldkamp et al., *Journal of Digital Imaging* 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC3043684/) | A reduced-dose simulation was built and validated for one raw-data digital radiography system using detector- and noise-specific measurements. | The method does not justify generic noise injection into post-processed MIMIC-CXR-JPG images. |
| [CheckList, ACL 2020](https://aclanthology.org/2020.acl-main.442/) | Minimum-functionality, invariance, and directional tests expose model behaviours missed by aggregate accuracy. | It supplies testing discipline, not a clinically valid radiology perturbation. |
| [Contrast Sets, EMNLP Findings 2020](https://aclanthology.org/2020.findings-emnlp.117/) | Small meaningful perturbations can probe local decision boundaries and annotation artifacts. | A label-changing contrast is not automatically an information-loss control or an identified clinical intervention. |
| [CheXpert, AAAI 2019](https://ojs.aaai.org/index.php/AAAI/article/view/3834) and [MIMIC-CXR-JPG documentation](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) | Radiology-report labelling distinguishes positive, negative, uncertain, and absent/no-mention states. | Report-derived states cannot establish image truth, and no mention cannot be recoded as a negative assertion. |
| [RadGraph, NeurIPS Datasets and Benchmarks 2021](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c8ffe9a587b126f152ed3d89a146b445-Abstract-round1.html) | Its schema distinguishes definitely present, uncertain, and definitely absent observations and represents modifiers/relations separately. | A schema distinction does not show that deleting a modifier preserves this project's binary clinical meaning. |
| [Mahmood et al., MICCAI 2025](https://papers.miccai.org/miccai-2025/0693-Paper3526.html) | The accepted paper creates synthetic report errors by changing findings and locations for phrase-grounded fact checking. | Finding/location substitution creates factual alternatives; it is not a text-information-loss control and already occupies a generic synthetic medical compatibility route. |

### Project inference

For a truly atomic determinate binary assertion, target-semantic information
cannot be removed while the same unique `Y_t` remains fully recoverable. Under
the idealized binary model, if transformed text `T'` still determines `Y_t`,
then `H(Y_t | T') = 0` and `I(Y_t; T') = H(Y_t)`; any removed information was
surface or non-target information. This is a protocol inference using
[Shannon's information framework](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x),
not an empirical clinical fact. Therefore the primary `M_t` candidate below is
task-critical target-state loss with `Y_t=undefined`, not a
semantics-preserving corruption.

### Assumptions requiring external verification

- The provisional finding and single-frontal input support a reliable
  determinate image-side state before and after the proposed `M_v` operation.
- The exact positive/negative atomic grammar is clinically acceptable and has
  exactly one polarity-bearing slot.
- Disjoint qualified panels, secure infrastructure, and the stated screening
  floors are available.
- A fixed half-resolution bottleneck creates meaningful but interpretable
  information loss for enough eligible pleural-effusion cases. Literature does
  not establish this transfer.

## Image Information-Loss Options

### `MV-1` — Half-resolution bandwidth attenuation (recommended candidate)

| Required field | Prospective specification |
| --- | --- |
| Changed information | Remove spatial frequencies unavailable after a two-fold reduction on each axis; do not add, delete, crop, or invert anatomical content. |
| Exact operation | After the frozen geometry/rendering step and before channel normalization, deterministically area-average the `224 x 224` reference input to `112 x 112`, then restore it to `224 x 224` with bilinear interpolation. Freeze library, version, coordinate convention, antialias flag, boundary handling, value range, and rounding. No stochastic augmentation, sharpening, denoising, or recompression is allowed. |
| Severity | One fixed `2x` per-axis bottleneck. No severity may be selected after candidate-score inspection. |
| Semantic-state rule | Primary `MV-1` accepts only `protocol-defined loss but interpretable`, complete prescribed field, `A_v=determinate`, and the same `Y_v` as the intact sibling. Task-critical or ambiguous variants are rejected from this contrast, not pooled. |
| Task-relevance qualification | On a prospectively sampled qualification set disjoint from reader training/reliability, development, Month 3, confirmation, calibration, and target evidence, use disjoint five-reader image-only panels for intact and transformed siblings. Counterbalance reader/panel assignment across sibling state and source polarity. For panel-mean presence probabilities on the `0--1` scale, define `q_b = abs(pbar_intact,b - 0.5) - abs(pbar_MV-1,b - 0.5)`, `q_v,y = E[q_b | independently assigned intact Y_v=y]`, and the construct-transport estimand `q_v,bal = 0.5(q_v,present + q_v,absent)`. Require at least 108 evaluable blocks of each independent polarity. The candidate gate is a patient-clustered one-sided 95% lower bound for `q_v,bal` **strictly above `0.10`**. No model score enters this gate. |
| Within-source reference | The exact pre-bottleneck `224 x 224` compatible image--text pair from the same source block. |
| Reader acceptance | Independent five-reader panels for intact and transformed siblings; at least four of five on the transformed panel must accept interpretable protocol-defined loss, full field coverage, a determinate state, and the same finding polarity established independently on the intact sibling. No more than one reader may flag ambiguity or task-critical loss. Cross-modal review must find no contrary evidence introduced. |
| Artifact threat | A resampling signature can become a shortcut for the `M_v` arm. The kernel and output geometry must be constant, the control response remains inside `abs(D_Mv)`, and no claim of artifact absence follows from a weak probe. |
| Kill consequence | Reject `MV-1` if state preservation, task-relevance qualification, reader reliability, polarity-specific eligible yield, or reproducible rendering fails. If the operation preserves polarity but fails `q_v,bal`, it may be reported only as fixed resolution attenuation and cannot complete primary `J_id`. If a valid estimator responds to a qualified control as strongly as conflict, the estimator—not the control result—is killed by `psi_mag`. Replacing the severity requires a new prospective decision. |

The `224` interface is tied to the conditional primary BiomedCLIP candidate.
A different primary input resolution requires a dated amendment specifying the
exact absolute transform; silently converting this into a relative, model-
dependent severity is prohibited.

The `0.10` probability-scale threshold is a prospective design choice, not a
validated clinical constant. Since each stratum's `q_b` has worst-case bounded
SD `0.50`, one-sided `alpha=0.05`, 90% power, and planning truth
`q_v,bal=0.20` give a crude equal-allocation minimum of 108 evaluable independent
patient blocks per image polarity (216 total). A patient-clustered simulation,
attrition allowance, reader-dependence
model, and resource approval must replace this approximation before an
annotation brief is issued. Approving the rule at Gate 0 does not count as
passing it: the operation remains unvalidated until a later authorized,
model-independent qualification exercise passes prospectively.

### Rejected or diagnostic image options

| Option | Role | Decision reason |
| --- | --- | --- |
| Fixed lossy JPEG recompression | Diagnostic only | Codec/block signatures are conspicuous; compression ratio or quality does not map uniformly to task information; the observer paper does not establish equivalence or transfer to pleural effusion. |
| Pseudo-dose or generic noise injection into JPG | Reject as primary | Valid simulation requires acquisition/raw-data and detector-noise assumptions not supplied by a post-processed JPG. Generic Gaussian noise would be an unvalidated corruption. |
| Crop, field removal, or localized mask | Task-critical missingness diagnostic only | It removes anatomy or localization evidence and creates boundaries/provenance cues. It cannot be called ambiguity or a semantics-preserving degradation. |
| Added pathology, compositing, or inpainting | Reject | It can change image truth, introduce synthetic evidence, and requires a separate governed clinical intervention route. |

The [official MIMIC-CXR-JPG methods](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
state that the released files were already mapped to 8-bit, histogram equalized,
and saved as JPEG at quality 95. Additional JPEG compression would therefore
be compound processing, not a clean first compression of raw detector data.

## Text Information-Loss Options

### `MT-1` — Sole-polarity-slot redaction (recommended candidate)

| Required field | Prospective specification |
| --- | --- |
| Changed information | Remove all and only the target finding's definite polarity while retaining the finding identity and fixed carrier template. |
| Exact operation | Use the frozen atomic forms `Pleural effusion status: present.` and `Pleural effusion status: absent.` for determinate siblings. Replace the entire sole status field with the identical literal `[REDACTED]`, yielding `Pleural effusion status: [REDACTED].` No source-specific wording, whitespace, punctuation, metadata, or hidden field may remain. Exact capitalization and tokenizer input are frozen. |
| Severity | Redact one of one polarity-bearing fields: 100% of the target-state carrier and 0% of the target identity. No graded severity exists. |
| Semantic-state rule | `M_t=task-critical`, target polarity `not assessable`, `Y_t=undefined`, `A_t=not assessable`, and `C*=undefined`. It is missing target-state information, not linguistic ambiguity, uncertainty, a negative finding, or a recoverable proposition. |
| Within-source reference | The same source block's compatible intact definite assertion using the identical carrier grammar. |
| Reader acceptance | Three of three blinded text readers must identify the target finding, classify polarity as not assessable, find no contrary proposition, and classify the corruption as task-critical. The disjoint cross-modal panel verifies only the intended loss and absence of contrary evidence. Exact byte/token and source-polarity balance are construction checks. |
| Artifact threat | Redaction is conspicuous and out of distribution. That is recorded as an `M_t` exposure; it cannot enter a conflict-versus-compatible nuisance channel. The estimator must not treat the cue as semantic conflict. |
| Kill consequence | Reject the operation if polarity leaks, readers infer a conventional polarity, the template contains another state carrier, or target identity becomes unclear. Do not replace it after score inspection. |

This structured grammar is a candidate, not an assertion that it is clinically
fluent. Task-critical loss need not be fluent under the current protocol, but
the clinical owner must still approve its safety and interpretability.

### Rejected or diagnostic text options

| Option | Role | Decision reason |
| --- | --- | --- |
| One prospectively fixed character deletion in the finding lexeme | Recoverable-corruption/surface diagnostic | If every reader recovers the same finding and polarity, no target-state information was removed; tokenizer fragmentation is model-specific. Escalation to task-critical loss cannot be pooled with accepted recovery. |
| Whole-assertion dropout or empty input | Full-missingness diagnostic | It removes finding identity, polarity, and commitment, duplicates the missing-assertion arm, and is coarser than `MT-1`. |
| Deleting the sole negation/polarity word | Reject | It can invert the proposition or create an asymmetric fragment rather than pure information loss. |
| Hedge insertion or certainty change | Epistemic-form diagnostic | It changes commitment. A hedge is not linguistic ambiguity and cannot supply `M_t`. |
| Modifier, location, laterality, or severity deletion | Semantic-specificity diagnostic at most | A truly minimal binary assertion has no such slot. If present, the detail may change clinical entailment or compatibility and requires a separate ontology decision. |
| Finding or location substitution | Reject as `M_t` | It creates a different factual assertion and is a compatibility/error perturbation, not information loss. |

## Joint Freeze and Stop Rule

`MV-1` and `MT-1` are the only recommended members of the two-control
`J_id` candidate. Their different semantic-state rules are intentional and
must be reported: `MV-1` is a proposed interpretable-loss operation preserving
`Y_v`, conditional on passing the separate task-relevance gate; `MT-1` is
task-critical loss making `Y_t` undefined. They cannot be pooled, renamed
ambiguity, or treated as interchangeable doses of one construct.

The Commander selects the scientific package; the clinical owner approves the
finding, grammar, readability, and image acceptance; the statistical owner
approves the paired references, eligibility/attrition consequences, and
`psi_mag` family. Any rejection leaves Gate 0 open and requires one new
prospective option audit. No data, image, report, model, or reader may be used
to choose an alternative under this record.

## Permitted Claim

The repository now contains finite, falsifiable candidate information-loss
controls and an explicit task-relevance criterion for `MV-1`. It does not
establish clinical validity, task-evidence attenuation, intervention validity,
artifact absence, ambiguity identification, feasibility, Gate-0 closure, or a
scientific result.
