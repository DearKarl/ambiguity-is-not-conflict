# Estimator Formalization and Equivalence Audit

**Status:** Three pointwise method claims killed; Method A and its non-novel
instrument/matched-comparator interfaces are Commander-approved but not
execution-approved

**Audit date:** 2026-08-29
**Evidence class:** Gate-0 mathematical and authoritative peer-reviewed/
official-source audit under TB-0006, with recent preprints labelled only as
non-authoritative leads; no data, model, code, or experiment was accessed or
run

## Executive Decision

No audited pointwise uncertainty-aware score passes the Gate-0 novelty and
non-equivalence rule. Three finite candidate classes were reduced to their
exact binary forms:

1. probabilistic excess disagreement either becomes ordinary mean
   disagreement after the ambiguity terms are removed, or increases with the
   very marginal uncertainty it is meant to control;
2. a conditional conflict-versus-compatibility density ratio is exactly a
   matched binary classifier logit plus a known sampling-prior offset; and
3. evidential confident disagreement is already the published RCML
   conflictive degree in the binary case and sits inside an occupied
   evidential-fusion line.

**Recommendation:** kill the claim that any of these is a new pointwise
conditional-conflict estimator. Do not select the best of them through
development. Preserve the intervention-defined specificity functional
`psi_mag` and its exact sample estimator as the project's measurement
framework, but do not misdescribe its finite-sample plug-in estimator as a
deployable pair-level score. Gate 0 therefore remains open: the owners must
approve a claim-narrowing amendment centered on the measurement framework.
DR-0016 records that Commander-level Method-A choice; the audit still does not
establish that the framework itself is novel or venue-ready.

## Objects That Must Not Be Conflated

For a modality pair \(X=(X_v,X_t)\), let \(Y_v,Y_t\in\{0,1\}\) denote
independently measured semantic states only when each modality is determinate.
Then

```math
C^*=\mathbb 1\{Y_v\ne Y_t\}
```

is defined only on that determinate support. It is undefined when either state
is ambiguous, missing, or task-critically lost. A **pointwise score**
\(S_m(X)\) is an instrument that attempts to rank pair-level incompatibility.
The **specificity estimand** `psi_mag,m` is instead a population functional of
that already frozen instrument under controlled interventions. The latter can
validate or falsify the former; it cannot create pair-level semantic
identifiability by itself.

The audit treats the following as separate quantities:

- external reader-elicited semantic frequencies
  \(p^R_v=k_v/R_v\) and \(p^R_t=k_t/R_t\), which are measurement variables
  available only where the governed reader protocol supplies them;
- learned model beliefs
  \(\widehat p_v=q_{\theta_v}(Y=1\mid X_v)\) and
  \(\widehat p_t=q_{\theta_t}(Y=1\mid X_t)\), which may be available at pairwise
  inference but need not equal the reader-elicited quantities or a true
  semantic-state probability;
- representation spread, epistemic spread, evidential uncertainty mass, and
  output variation; and
- intervention-defined conflict status \(C^*\), which is not observed from a
  model's own disagreement score.

## Primary-Source Facts

- Subjective-logic work already separates vacuity, or lack of evidence, from
  dissonance, or conflict among strong evidence. That conceptual distinction is
  not new to this project ([Han et al., NeurIPS
  2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/c80d9ba4852b67046bee487bcd9802c0-Abstract.html)).
- RCML defines a conflictive degree as projected probability distance times
  conjunctive certainty, with the certainty factor
  \((1-u_A)(1-u_B)\) ([Xu et al., AAAI
  2024](https://ojs.aaai.org/index.php/AAAI/article/view/29546)).
- Discounted Belief Fusion provides order-invariant evidential fusion,
  conflict-based discounting, and uncertainty-based conflict detection
  ([Bezirganyan et al., AISTATS
  2025](https://proceedings.mlr.press/v258/bezirganyan25a.html)).
- CoRiM quantifies inter-modal inconsistency in predictive-distribution space
  and defines a differentiable conflict-risk objective for dynamic fusion
  ([Zou and Wei, CVPR
  2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Zou_CoRiM_Conflict-driven_Risk_Minimization_for_Dynamic_Multimodal_Fusion_CVPR_2026_paper.pdf)).
- Logistic discrimination as density-ratio estimation is established prior
  art; its classifier posterior requires the sampling-prior correction
  ([Gutmann and Hyvärinen, AISTATS
  2010](https://proceedings.mlr.press/v9/gutmann10a.html)).
- PCME and ProbVLM already supply probabilistic image--text representation
  routes. PCME++ uses Gaussian embeddings and the closed-form sampled distance

  ```math
  \mathbb E\|Z_v-Z_t\|_2^2
  =\|\mu_v-\mu_t\|_2^2+\operatorname{tr}(\Sigma_v+\Sigma_t),
  ```

  with a pairwise logistic matching objective ([PCME, CVPR
  2021](https://openaccess.thecvf.com/content/CVPR2021/html/Chun_Probabilistic_Embeddings_for_Cross-Modal_Retrieval_CVPR_2021_paper.html);
  [ProbVLM, ICCV
  2023](https://openaccess.thecvf.com/content/ICCV2023/html/Upadhyay_ProbVLM_Probabilistic_Adapter_for_Frozen_Vison-Language_Models_ICCV_2023_paper.html);
  [PCME++, ICLR
  2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ad9d6ab10446114cf5482d5e1f971a84-Abstract-Conference.html)).

These are source facts. The reductions and decisions below are this audit's
derivations and recommendations.

**Non-authoritative literature lead:** CONFER reports an
uncertainty-normalized scalar predictive-belief difference and derived conflict
regimes ([Hou et al., arXiv v1
2026](https://arxiv.org/html/2608.07867v1)). Because the located source is a
recent non-peer-reviewed preprint, it is excluded from this audit's formal
novelty-kill evidence and mandatory-baseline set. It remains a surveillance
lead only.

## Candidate 1 — Distributional Excess Disagreement

### Exact interface

- **Inputs:** learned binary model beliefs
  \(\widehat\pi_v=\operatorname{Bernoulli}(\widehat p_v)\) and
  \(\widehat\pi_t=\operatorname{Bernoulli}(\widehat p_t)\), or learned Gaussian
  representation heads \(Z_v\sim\mathcal N(\mu_v,\Sigma_v)\) and
  \(Z_t\sim\mathcal N(\mu_t,\Sigma_t)\). The external
  \(p^R_v,p^R_t\) reader frequencies are validation measurements, not
  deployable score inputs.
- **Score:** the energy-style self-corrected discrepancy

  ```math
  \kappa_L=\mathbb E L(\widehat Y_v,\widehat Y_t)
  -\tfrac12\mathbb E L(\widehat Y_v,\widehat Y_v')
  -\tfrac12\mathbb E L(\widehat Y_t,\widehat Y_t').
  ```

- **Trainable quantities:** none in the score. Any encoders, probability heads,
  covariance heads, and calibration maps are upstream models and must be
  trained only under a separately frozen objective and split.
- **Candidate objective:** for independent reader counts \(k_r\) of \(R_r\)
  determinate readings, a binary semantic head uses the fixed binomial negative
  log likelihood
  \(-\sum_{r\in\{v,t\}}\{k_r\log \widehat p_r+
  (R_r-k_r)\log(1-\widehat p_r)\}\).
  A PCME++-form Gaussian adapter instead uses

  ```math
  d=\|\mu_v-\mu_t\|^2+\operatorname{tr}(\Sigma_v+\Sigma_t),
  \qquad
  \mathcal L_{match}
  =-m\log\sigma(-ad+b)-(1-m)\log\sigma(ad-b),
  ```

  plus its prospectively frozen VIB term and coefficients. These are distinct
  upstream routes, not tunable parts of `kappa_L`, and may not be exchanged
  after protected outcomes are inspected.
- **Inference:** one scalar per pair; higher means greater distributional
  separation. Development-only orientation and scale remain mandatory.
- **Matched deterministic comparator:** the same mean heads and pairwise
  objective with covariance fixed/removed, evaluated under the candidate's
  identical pre-link or post-link convention. For example, a squared candidate
  requires the squared deterministic mean gap, not only its unsquared ranking.

### Binary reduction

For disagreement loss \(L(a,b)=\mathbb 1(a\ne b)\), independence of the two
model-implied draws gives

```math
\begin{aligned}
\mathbb E L(\widehat Y_v,\widehat Y_t)
  &=\widehat p_v+\widehat p_t-2\widehat p_v\widehat p_t,\\
\tfrac12\mathbb E L(\widehat Y_v,\widehat Y_v')
  &=\widehat p_v(1-\widehat p_v),\\
\tfrac12\mathbb E L(\widehat Y_t,\widehat Y_t')
  &=\widehat p_t(1-\widehat p_t),\\
\therefore\quad \kappa_L&=(\widehat p_v-\widehat p_t)^2.
\end{aligned}
```

Here \(\widehat Y_r,\widehat Y_r'\) are independent draws from the learned
\(\widehat\pi_r\), not reader labels. The score is exactly a fixed square of
\(|\widehat p_v-\widehat p_t|\). It is rank-equivalent, but the nonlinear
square can change paired contrasts after the protocol's affine standardization;
it therefore cannot be credited with an empirical advantage unless the matched
deterministic score receives the identical square. A nominal model-implied
probability of disagreement,

```math
\widehat P_{\ne}
=\widehat p_v(1-\widehat p_t)+(1-\widehat p_v)\widehat p_t,
```

does not solve the problem: if \(\widehat p_v,\widehat p_t\) are themselves
posterior random probabilities and the modality posteriors are assumed
independent, integrating \(\widehat P_{\ne}\) depends only on their posterior
means. The second-order variances cancel. Moreover,
\(\widehat p_v=0.5,\widehat p_t=1\) yields positive model disagreement even
when the external reader protocol would classify the first modality as
indeterminate and leave the project's semantic conflict label undefined.

### Gaussian reduction

For squared Euclidean loss and independent Gaussian draws,

```math
\mathbb E\|Z_v-Z_t\|^2
=\|\mu_v-\mu_t\|^2+\operatorname{tr}(\Sigma_v+\Sigma_t).
```

The uncorrected score rises with marginal spread, so it responds directly to
ambiguity or information loss. Applying the same self-distance correction as
`kappa_L` gives

```math
\begin{aligned}
&\mathbb E\|Z_v-Z_t\|^2
-\tfrac12\mathbb E\|Z_v-Z_v'\|^2
-\tfrac12\mathbb E\|Z_t-Z_t'\|^2\\
&\qquad=\|\mu_v-\mu_t\|^2,
\end{aligned}
```

because each self-distance is twice its covariance trace. The ambiguity terms
cancel, leaving deterministic mean distance. A scalar predictive-belief
normalization could instead be defined as

```math
R_{vt}
=\frac{|\widehat p_v-\widehat p_t|^2}
{2(\widetilde u_v+\widetilde u_t+\epsilon)}.
```

The CONFER preprint is a close reported instance of this scalar form, but it is
not authoritative novelty-kill evidence here; extending it to arbitrary vector
Gaussian means would be an analogy, not an exact transcription. This
denominator variant is therefore unadjudicated for formal novelty and is not
part of Candidate 1's analytic kill. Its formula alone still cannot identify
semantic \(C^*\). Wasserstein--Bures or overlap variants remain
probabilistic-distance choices and likewise do not themselves identify
semantic conflict.

### Assumptions and decision

The reduction assumes valid modality-specific probabilities, independent
draws for the stated expectations, common label semantics, and a fixed loss.
Those assumptions do not establish that representation spread equals semantic
ambiguity. **Decision: KILL as a new estimator.** Retain only as a diagnostic or
published-method comparator. A covariance advantage must exceed the matched
mean-head route prospectively; covariance's mere presence is not a technical
distinction.

## Candidate 2 — Conditional Conflict Density Ratio

### Exact interface

Let \(F\) contain every permitted pair feature available at decision time and
let \(W\) contain only prospectively frozen design strata or nuisance
variables. Define

```math
S_{LR}(F,W)=
\log\frac{p(F\mid C^*=1,W)}{p(F\mid C^*=0,W)}.
```

- **Inputs:** the same frozen representations, uncertainty summaries, and
  permitted nuisance variables supplied to the matched comparator.
- **Trainable quantities:** classifier parameters \(\eta\) in
  \(q_\eta(C^*=1\mid F,W)\); no extra hidden supervision or intervention label is
  available at inference.
- **Objective:** prospectively weighted binary log loss on development-only
  compatible/conflicting determinate blocks, with patient grouping and the
  exact sampling weights frozen.
- **Calibration:** a development-only map may calibrate \(q_\eta\); it changes
  probability interpretation but not the underlying density-ratio identity.
- **Inference:** classifier logit minus the known conditional sampling-prior
  log-odds.
- **Matched deterministic comparator:** the identical classifier architecture,
  inputs, labels, capacity, regularization, tuning, and objective.

### Bayes reduction

Bayes' rule gives, in every supported stratum \(W=w\),

```math
\log\frac{p(F\mid C^*=1,w)}{p(F\mid C^*=0,w)}
=\operatorname{logit}\Pr(C^*=1\mid F,w)
-\operatorname{logit}\Pr(C^*=1\mid w).
```

Under the balanced construction, the last term is zero. Under another known
sampling ratio it is a stratum-specific constant. Consequently the proposed
density-ratio estimator is exactly the matched deterministic classifier score
up to an offset. Feeding Gaussian parameters, evidential masses, or uncertainty
features into \(F\) does not avoid the result: a capacity- and information-
matched deterministic classifier receives the same numbers. Any advantage
obtained by withholding those inputs from the comparator is an information-
budget mismatch, not evidence for a new estimator.

### Assumptions and decision

The likelihood ratio additionally requires positivity, correct construction
labels, stable sampling odds, and either a correct density model or a
consistent probabilistic classifier. It estimates discrimination between the
constructed cells, not semantic conflict outside their support, and it can
learn construction artifacts. **Decision: KILL as a distinct uncertainty-aware
estimator.** Retain the classifier as the strongest matched deterministic kill
baseline and use frozen artifact probes to constrain interpretation.

## Candidate 3 — Evidential Confident Disagreement

### Exact interface

For modality opinions \(\omega_r=(b_r,u_r,a_r)\), \(r\in\{v,t\}\), let the
projected categorical model probabilities be
\(\widehat p_{r,k}=b_{r,k}+a_{r,k}u_r\). RCML's two-view conflictive degree is

```math
S_{EV}=\left(\tfrac12\sum_{k=1}^K
|\widehat p_{v,k}-\widehat p_{t,k}|\right)
\times(1-u_v)(1-u_t).
```

- **Inputs:** two task-aligned categorical evidential opinions.
- **Trainable quantities:** upstream non-negative evidence heads; the conflict
  formula itself has none.
- **Objective:** with evidence \(\alpha_k=e_k+1\), \(S=\sum_k\alpha_k\), and
  \(\tilde\alpha=y+(1-y)\odot\alpha\), the task-port candidate must freeze the
  expected categorical loss

  ```math
  \mathcal L_{EDL}(\alpha,y)
  =\sum_k y_k[\psi(S)-\psi(\alpha_k)]
  +\lambda_{KL}(t)\,
  KL[\operatorname{Dir}(\tilde\alpha)\parallel
     \operatorname{Dir}(\mathbf 1)].
  ```

  The exact view/fused-loss weights, annealing schedule, and any published
  conflict regularizer must be taken from the selected RCML/DBF identity or
  frozen as a documented task-valid deviation. They are unresolved
  implementation blockers; ordinary supervised heads cannot silently be
  called RCML or DBF.
- **Calibration:** projected probabilities and uncertainty masses require
  development-only calibration diagnostics; uncertainty mass is not assumed to
  equal independently measured semantic ambiguity.
- **Inference:** one scalar per pair, zero under a vacuous modality and high for
  confident predictive disagreement.
- **Matched deterministic comparator:** for analytic identity, a deterministic
  function receives the same \(\widehat p_v,\widehat p_t,u_v,u_t\) and applies
  the identical product, reproducing `S_EV` exactly. A point-softmax head
  without \(u_v,u_t\) is a separately required architectural ablation with
  matched encoders,
  semantic supervision, capacity, and tuning; it is not a same-information
  comparator to the full evidential output.

### Binary reduction

For \(K=2\), total variation is
\(|\widehat p_v-\widehat p_t|\), hence

```math
S_{EV}=|\widehat p_v-\widehat p_t|(1-u_v)(1-u_t).
```

This is already RCML's published confident-disagreement structure, not a new
conditional-conflict estimator. Discounted Belief Fusion further occupies
conflict-sensitive evidential fusion and uncertainty-based detection. The
score suppresses a vacuous modality by design, but that behavior is a modeling
choice; it does not prove that genuine semantic ambiguity, information loss,
or epistemic uncertainty has been isolated.

### Assumptions and decision

The route assumes calibrated evidence, compatible class bases and priors,
task-valid porting, and an uncertainty mass with a stable interpretation.
**Decision: KILL as a new estimator.** Retain RCML/Discounted-Belief-Fusion as
closest published comparators if their exact implementations and rights permit
a fair task port.

## Pointwise Identifiability Limit

**Derivation:** no function of model outputs alone identifies this project's
semantic \(C^*\) without an external measurement bridge. Two latent data-
generating states can yield the same learned-output tuple
\((\widehat p_v,\widehat p_t,u_v,u_t,\mu_v,\mu_t,\Sigma_v,\Sigma_t)\) while one
contains genuinely indeterminate semantic evidence and another contains
determinate opposing semantic evidence that the model fails to recover. Every
audited pointwise model-output formula assigns the same score to both
observable tuples, whereas the external reader construct makes \(C^*\)
undefined in the first state and \(C^*=1\) in the second. This counterexample
applies only to learned outputs; it does not treat the external
\(p^R_v,p^R_t\) measurements as model outputs. Therefore model uncertainty
adjustment is not sufficient for construct identification.

The external bridge proposed in this repository is independent semantic
measurement plus a controlled, counterbalanced intervention. It can identify a
population response of a frozen score under its assumptions. It cannot make
that score a universally identified conflict measure or label natural
ambiguous pairs as non-conflicting.

## Retained Exact Measurement Estimator

For a method \(m\), freeze its pair-level score \(S_m\), orientation \(a_m\),
and compatible-development reference location and scale before protected-set
access:

```math
Z_{bm}=a_m\frac{S_{bm}-\mu^{dev}_{0m}}{\sigma^{dev}_{0m}}.
```

For every complete, equally weighted patient block \(b=1,\ldots,n\), construct

```math
D_{C,bm}=Z^{conflict}_{bm}-Z^{compatible}_{bm},
\qquad
D_{j,bm}=Z^j_{bm}-Z^{reference(j)}_{bm}.
```

The retained population estimand and exact plug-in estimator are

```math
\psi_{mag,m}=\min_{j\in\mathcal J_{id}}
\mathbb E[D_{C,m}-|D_{j,m}|],
```

```math
\widehat\psi_{mag,m}=\min_{j\in\mathcal J_{id}}
\left\{\frac1n\sum_{b=1}^n
\left(D_{C,bm}-|D_{j,bm}|\right)\right\}.
```

The finite-sample plug-in estimator is the **minimum of control-specific sample
means**, not the sample mean of a within-block minimum. Because of the outer
minimum, it is generally downward biased for the population functional at
finite \(n\). It has no trainable parameters. Its inputs are complete controlled
score blocks produced by an independently frozen instrument; its inference
interface is the scalar estimate plus every control-specific component,
patient-cluster simultaneous bounds, and the pre-specified raw-scale and
median/MAD sensitivities. The max-`t` procedure must resample whole patients
and construct joint bounds for the smooth component means; directly
bootstrapping the non-smooth minimum is forbidden. The lower bound for
\(\psi_{mag,m}\) is the minimum of its simultaneous component lower bounds.
Ties make the minimum non-smooth, which is why componentwise simultaneous
inference is required.

Identification requires, at minimum, valid determinate semantic labels,
consistency of each intervention version, positivity of both compatibility
states inside the frozen blocks, no cross-patient interference, valid and
semantics-checked within-source controls, exact construction balance/no
condition leakage, complete sibling blocks, a stable frozen score, and a
population/sampling rule matching the expectation. Natural-ambiguity contrasts
do not enter this estimand without a separately approved intervention or
exchangeability-and-transport argument.

This statistical estimator answers:

> Does a named score respond more to the controlled determinate-conflict
> intervention than to every approved information-loss control, on the frozen
> scale and population?

It does **not** answer whether an arbitrary pair is truly conflicting, whether
all ambiguity has been controlled, or whether the tested pointwise score is
novel. It also cannot support selective-decision claims without a separate
natural-target proper-score and equal-budget risk analysis.

## Candidate Registry and Kill Result

| ID | Exact candidate | Closest exact comparator or occupied form | Result |
| --- | --- | --- | --- |
| `E1` | Self-corrected learned-belief/Gaussian distribution discrepancy | Binary or Gaussian mean distance; PCME/PCME++/ProbVLM family | `KILL` — the audited self-correction reduces to deterministic mean discrepancy |
| `E2` | Conditional conflict/compatibility log density ratio | Capacity-, input-, supervision-, and tuning-matched deterministic classifier logit | `KILL` — exact Bayes equivalence up to known prior offset |
| `E3` | Evidential projected disagreement times certainty | RCML conflictive degree; Discounted Belief Fusion line | `KILL` — already published and not semantically identifying |

No candidate is promoted. Empirical performance cannot reverse an analytic
equivalence or convert an occupied formula into novelty.

## Official Implementation, Licence, and Supervision Audit

This is a read-only identity audit, not authorization to obtain any checkpoint
or code. A common feature candidate would have to freeze the official
[BiomedCLIP snapshot
`9f341de24bfb00180f1b847274256e9b65a3a32e`](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224/commit/9f341de24bfb00180f1b847274256e9b65a3a32e)
and [OpenCLIP 2.23.0 commit
`f08f25f3f226bdb538de2b4ed48a9213ba6b179e`](https://github.com/mlfoundations/open_clip/commit/f08f25f3f226bdb538de2b4ed48a9213ba6b179e),
whose exact [BiomedCLIP licence
file](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224/blob/976347208356df345b35d846ae09dd59d5c53668/LICENSE.md)
and [OpenCLIP licence
file](https://github.com/mlfoundations/open_clip/blob/f08f25f3f226bdb538de2b4ed48a9213ba6b179e/LICENSE)
state MIT terms. Their previously documented exposure limitations remain
unchanged.

| Role | Exact identity candidate | Official-code/licence fact | Supervision and disposition |
| --- | --- | --- | --- |
| `RAW-COS` | \(S_{cos}=1-\langle z_v/\|z_v\|,z_t/\|z_t\|\rangle\) on frozen post-projection features, without logit scale or softmax | Project-native arithmetic over the MIT BiomedCLIP/OpenCLIP feature route | No trainables or project labels; include as a zero-capacity compatibility reference, never semantic-conflict truth |
| `DET-LR` | Project-native \(h=[z_v,z_t,|z_v-z_t|,z_v\odot z_t,W]\), binary-log-loss classifier \(g_\eta\), and \(g_\eta+\log(\pi_0/\pi_1)\) | No official end-to-end task implementation to inherit; exact architecture, \(W\), weights, calibration, and software identity remain unfrozen | Uses explicit development \(C^*\) labels; include only as a privileged supervised ceiling unless every claimed matched method receives identical labels |
| `DBF-TASK` | [DBF paper](https://proceedings.mlr.press/v258/bezirganyan25a.html) and official commit [`79b7d56b0cfa53c98a93f29f9d9c59768177ad17`](https://github.com/bezirganyan/DBF_uncertainty/commit/79b7d56b0cfa53c98a93f29f9d9c59768177ad17); a task port would use two binary finding-state evidential heads | The immutable [DBF licence](https://github.com/bezirganyan/DBF_uncertainty/blob/79b7d56b0cfa53c98a93f29f9d9c59768177ad17/LICENSE) states GPL-3.0, while its [README](https://github.com/bezirganyan/DBF_uncertainty/blob/79b7d56b0cfa53c98a93f29f9d9c59768177ad17/README.md) credits borrowed RCML code. The audited [RCML snapshot](https://github.com/jiajunsi/RCML/tree/c9c5ab41e6fe62a85e5f6441a4dc7b568e1fa421) exposes no explicit licence file. The exact DBF [loss](https://github.com/bezirganyan/DBF_uncertainty/blob/79b7d56b0cfa53c98a93f29f9d9c59768177ad17/loss_function.py), [data path](https://github.com/bezirganyan/DBF_uncertainty/blob/79b7d56b0cfa53c98a93f29f9d9c59768177ad17/data.py), and [driver](https://github.com/bezirganyan/DBF_uncertainty/blob/79b7d56b0cfa53c98a93f29f9d9c59768177ad17/main.py) are identity evidence only; direct vendoring is not approved. | Uses semantic \(Y\) supervision on clear compatible pairs; retain only as a privileged comparator through an owner-approved clean-room formula port or a separately governed GPL runner subject to licensing/provenance approval |
| `PROBVLM-2ADAPTER` | [ProbVLM commit `cb69f28b1ab23142a1c671e004b09b5cb5d8a204`](https://github.com/ExplainableML/ProbVLM/commit/cb69f28b1ab23142a1c671e004b09b5cb5d8a204), two modality-specific adapters, and paper-faithful symmetric cross-modal generalized-Gaussian likelihood semantics | The immutable [licence](https://github.com/ExplainableML/ProbVLM/blob/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/LICENSE) states MIT. The audited [loss](https://github.com/ExplainableML/ProbVLM/blob/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/src/losses.py), [network definitions](https://github.com/ExplainableML/ProbVLM/blob/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/src/networks.py), and [training driver](https://github.com/ExplainableML/ProbVLM/blob/cb69f28b1ab23142a1c671e004b09b5cb5d8a204/src/train_probVLM.py) differ materially from a single paper-exact executable identity. | Commander selected paper-faithful likelihood semantics in a project-native scientific interface. Coordinate reduction and full objective weights are project choices; there is no original checkpoint, code-exact reproduction claim, or constructed contradiction as a positive fit pair |
| `POINT-2ADAPTER-RECON` | Project-native two-branch mean-only adapter with identical frozen inputs, independently verified determinate-compatible fitting records, mean trunks, intra/cross target topology, optimization/tuning budget, and GGD score family; global coordinatewise scale/shape constants are fitted on the same compatible fit/development objective and frozen before protected outcomes | New project-native arithmetic; it inherits no third-party adapter code | Commander-selected primary deterministic full-route comparator; unit-scale Laplace is a sensitivity only. Removing scale/shape heads changes active capacity and gradient paths, so this is not a capacity-isolated mechanism comparison; exact executable architecture, parameter counts, compute, and numerical values remain owner-blocked |
| `POINT-INFONCE` | Project-native two-branch point adapter on the same native records, scored by a frozen contrastive pair logit | The closest [CLIP-Adapter snapshot](https://github.com/gaopengcuhk/CLIP-Adapter/tree/08d07f8b2ecafc6f1479fe636b26d464d7a5574e) is a different few-shot classifier and exposes no explicit licence file at the audited snapshot, so its code is excluded. | Secondary same-records contrastive baseline only; its off-diagonal negative assumptions prevent it from being the primary mean-only ablation, and its denominator/multi-positive/false-negative policy remains to be frozen |

The information budget must be explicit:

- `RAW-COS` receives only frozen \(z_v,z_t\).
- `PROBVLM-2ADAPTER` and `POINT-2ADAPTER-RECON` receive identical independently
  verified determinate-compatible fitting records. Fitting-set membership is
  shared semantic selection supervision and must be disclosed; the underlying
  \(C^*\)/semantic states are not model inputs or loss targets. Neither receives
  constructed intervention/control variants, ambiguity, provenance, model-error,
  or protected-outcome labels. `POINT-INFONCE` receives the same records but
  introduces a separately governed contrastive-negative assumption.
- `DET-LR` receives explicit determinate \(C^*\) and known sampling odds.
- `DBF-TASK` receives shared semantic finding \(Y\) on clear compatible pairs.
- At inference, every method receives only its frozen pair features; condition,
  construction, ambiguity, provenance, and protected-outcome fields are
  forbidden.

The finite role set is not one fully matched contest. Only
`PROBVLM-2ADAPTER` versus `POINT-2ADAPTER-RECON` is the primary same-selection-
information, same-score-family, same-target-topology full-route comparison. It
is not a capacity-matched isolation of a probabilistic mechanism, and exact
active parameter/compute differences must be reported. `POINT-INFONCE` is secondary;
`DET-LR` and `DBF-TASK` are privileged ceilings with different scientific
questions. Gate 0 cannot close until the remaining owners approve exact
software identities, numerical specifications, the DBF provenance/licence
route, the InfoNCE negative policy, and every supervision tag.

## Baseline and Ablation Consequences

1. The matched deterministic compatibility classifier is mandatory and must
   receive every decision-time feature given to a learned density-ratio route.
2. Any probabilistic adapter must have the frozen deterministic full-route
   comparator and a frozen-means diagnostic that substitutes the comparator's
   fitted global scale/shape constants. That diagnostic addresses only the
   direct score path conditional on jointly trained means. Self-corrected
   Gaussian distance must be reported as its deterministic mean-distance
   collapse.
3. Any evidential route must report projected-probability disagreement,
   uncertainty mass, their product, and matched point-softmax heads separately.
4. RCML confident disagreement and a task-valid Discounted-Belief-Fusion route
   are authoritative novelty threats, not decorative baselines. CONFER-style
   normalized disagreement remains a non-authoritative preprint surveillance
   lead, not formal kill evidence or a mandatory baseline. Exact
   implementation/licence/applicability audits must precede any execution.
5. `psi_mag` must be computed for each frozen instrument separately. Selecting
   the instrument with the largest observed `psi_mag` on Month 3 is forbidden.

### Link-function guardrail

Compatible-reference `Z` normalization is invariant only to a frozen positive
affine rescaling of a score. It is not invariant to nonlinear monotone links:
squaring, sigmoid, exponential, or another link can change every paired `D`
and hence `psi_mag` while leaving pair rankings unchanged. Therefore every
analytic-equivalence comparison must use the same link convention on both
sides. Compare a squared gap with the squared matched gap, a likelihood ratio
on the logit/pre-link scale with the matched classifier logit, and any retained
sigmoid or exponential with that same transformation applied to the comparator.
Neither rank equivalence nor a larger `psi_mag` created only by link choice is
an uncertainty-aware material advantage.

## Historical Finite Gate-0 Owner Choice

- **`G0-METHOD A` — recommended:** accept the pointwise method-claim kill;
  amend the central contribution prospectively to the intervention-defined
  measurement/validation framework; retain exactly one published or otherwise
  non-novel pointwise instrument as the primary test object and one matched
  deterministic comparator; reassess Main Track fit without claiming a new
  conflict score.
- **`G0-METHOD B`:** retain a new-estimator paper identity only if a new bounded,
  pre-data theory brief supplies one exact candidate with a non-cosmetic
  distinction, the same-information deterministic comparator, and a
  falsifiable advantage that survives analytic equivalence review. No
  development or protected-set inspection occurs first.

This section records the choice presented by TB-0006. DR-0016 subsequently
selects A at the Commander level, makes B inactive, and freezes the
`PROBVLM-2ADAPTER`/`POINT-2ADAPTER-RECON` scientific interfaces. Other-owner
approval and every executable detail remain open; the decision does not
authorize implementation or evidence access.

## Permitted Claim

The repository now contains an exact formalization kill for three candidate
pointwise estimator classes and an exact finite-sample plug-in formula/interface
for the existing intervention-specificity population functional. It does not
establish novelty, empirical identifiability, calibrated uncertainty,
performance, clinical benefit, Gate-0 closure, NeurIPS 2027 fit or eligibility
under the unpublished call, acceptance, or publication.
