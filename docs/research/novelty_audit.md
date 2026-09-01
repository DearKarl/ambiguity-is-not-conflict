# Novelty and Prior-Art Audit

**Status:** Method-A focused literature-audit snapshot; not a novelty claim
**Audit date:** 2026-09-01
**Evidence class:** Peer-reviewed primary papers and official-code leads, with
preprints explicitly labelled as non-authoritative surveillance leads; no
implementation was downloaded or reproduced

## Audit Question and Boundary

This audit asks which parts of the proposed paper identity are already present
in prior work and what, if anything, remains falsifiably distinct. It covers the
closest work found through the seed bibliography and targeted searches of
primary proceedings and author-linked repositories through the audit date. It
is not an exhaustive systematic review, a patent search, or evidence that the
remaining gap is novel. Search, citation, and code-version audits must continue
until submission.

The following layers are evaluated separately:

1. naming or defining multimodal conflict;
2. detecting contradiction or modality disagreement;
3. decomposing uncertainty into lack of evidence and conflicting evidence;
4. estimating conflict after conditioning on within-modality ambiguity and
   information loss;
5. demonstrating incremental proper-score and selective-decision value.

A paper that covers an earlier layer can invalidate a broad claim at that
layer even if it does not answer the complete research question.

## Prior-Art Map with Evidence Tiers

For peer-reviewed sources, the `Fact` column is limited to what the linked
primary source states. Preprint rows are literature leads only and cannot
support a formal novelty kill or mandatory baseline until authoritative status
is established. The `Boundary` column is this project's inference and must be
rechecked against the full method, appendices, and released implementation
before a paper claim is frozen.

| Source | Layer already covered (fact) | Boundary for this route (inference) | Threat |
| --- | --- | --- | --- |
| [Christoudias et al., UAI 2008](https://proceedings.mlr.press/r6/christoudias08a.html) | Studies multi-view learning when views disagree | Prevents framing view disagreement itself as a new problem | Foundational |
| [Han et al., NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/c80d9ba4852b67046bee487bcd9802c0-Abstract.html) | Formally separates subjective-logic vacuity from dissonance, described as lack of evidence versus conflict of strong evidence | Prevents claiming that “ambiguity/lack of evidence is not conflict” is itself a new uncertainty decomposition; modality-pair identification remains a separate question | Critical conceptual |
| [Han et al., CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Han_Multimodal_Dynamics_Dynamical_Fusion_for_Trustworthy_Multimodal_Classification_CVPR_2022_paper.html) | Uses evidential uncertainty for trustworthy dynamic multimodal fusion | Challenges a generic evidential-fusion contribution | Strong method |
| [Xu et al., AAAI 2024](https://ojs.aaai.org/index.php/AAAI/article/view/29546) | Formulates reliable conflictive multi-view learning and combines view-specific evidential opinions, decisions, and reliabilities | Directly threatens any confident-disagreement or evidential-conflict formulation; its target is model opinion under conflictive views rather than independently annotated semantic incompatibility | Critical estimator |
| [Gao et al., CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Gao_Embracing_Unimodal_Aleatoric_Uncertainty_for_Robust_Multimodal_Fusion_CVPR_2024_paper.html) | Models unimodal aleatoric uncertainty for robust fusion | Makes unimodal ambiguity/aleatoric controls mandatory rather than optional | Strong control |
| [Bezirganyan et al., AISTATS 2025](https://proceedings.mlr.press/v258/bezirganyan25a.html) | Proposes order-invariant evidential fusion with conflict-based discounting and reports uncertainty-based separation of conflicting from non-conflicting samples | Directly threatens any claim based only on an evidential conflict score or conflict-aware fusion; it does not, from the audited claims, establish crossed identification against image and text ambiguity | Critical estimator |
| [Zhang et al., ICML 2025](https://proceedings.mlr.press/v267/zhang25dq.html) | Formally defines input modality conflict, introduces MMMC, and evaluates prompt, supervised-fine-tuning, and reinforcement-learning mitigation of associated hallucination | Directly subsumes “first formulation of modality conflict” and a generic synthetic-conflict benchmark claim; the possible gap is conditional identification and measurement, not conflict naming | Critical construct/benchmark |
| [Deregnaucourt et al., WACV 2025](https://openaccess.thecvf.com/content/WACV2025/html/Deregnaucourt_A_Conflict-Guided_Evidential_Multimodal_Fusion_for_Semantic_Segmentation_WACV_2025_paper.html) | Uses evidential conflict to guide multimodal semantic-segmentation fusion | Requires a task-matched conflict-guided evidential comparator where feasible | Strong method |
| [Mahmood et al., MICCAI 2025](https://papers.miccai.org/miccai-2025/0693-Paper3526.html) | Trains phrase-grounded chest-radiograph fact checking on systematically perturbed finding/location pairs and evaluates across multiple X-ray datasets | Directly threatens an atomic medical image--finding compatibility method or synthetic-perturbation identity; independent ambiguity and conditional specificity are the possible distinctions | Critical medical task |
| [Hardy et al., PMLR 2025](https://proceedings.mlr.press/v281/hardy25a.html) | Produces finding-level hallucination risk scores from VLM hidden-state sequences on MIMIC-CXR | Makes a matched medical failure-prediction comparator necessary; hallucination risk is not the semantic conflict construct | Strong medical comparator |
| [CrossCheck-Bench, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/39788) | Benchmarks multimodal conflict-resolution reasoning under controlled contradictory evidence | Subsumes a broad conflict-resolution benchmark identity; it does not by itself establish an independently measured, ambiguity-conditioned conflict estimand | Critical benchmark |
| [CLASH, CVPR 2026 Findings](https://openaccess.thecvf.com/content/CVPR2026F/papers/Popordanoska_CLASH_A_Benchmark_for_Cross-Modal_Contradiction_Detection_CVPRF_2026_paper.pdf) | Benchmarks cross-modal contradiction detection with human-verified test cases | Makes a second generic contradiction benchmark insufficient; it is a candidate breadth/stress comparator, subject to data and licence audit | Critical benchmark |
| [van Sprang et al., CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/van_Sprang_Same_Content_Different_Answers_Cross-Modal_Inconsistency_in_MLLMs_CVPR_2026_paper.html) | Measures behavioural inconsistency when equivalent content is presented through different modalities | Distinguishes presentation inconsistency from contradictory paired evidence; both must not be conflated | Strong construct boundary |
| [Zou and Wei, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Zou_CoRiM_Conflict-driven_Risk_Minimization_for_Dynamic_Multimodal_Fusion_CVPR_2026_paper.pdf) | Defines a differentiable modality-conflict risk over predictive distributions and optimizes dynamic fusion under conflict and noise | Directly threatens a symmetric-KL/distribution-disagreement estimator plus decision-risk claim; conditional ambiguity controls and image--text atomic semantics are the possible distinctions | Critical estimator/decision |
| [Zhang et al., arXiv 2025](https://arxiv.org/abs/2511.02243) | Independently varies visual and textual reasoning difficulty, measures relative unimodal entropy, and studies modality following under conflict | Subsumes a claim to the first controlled study of conflict after varying unimodal difficulty; model confidence and source following are not independently measured semantic ambiguity or incompatibility | Critical controlled study |
| [Hou et al., CONFER arXiv v1 2026](https://arxiv.org/abs/2608.07867v1) | Reports uncertainty-adjusted modality compatibility and consensus, dissent, and ambiguity regimes for weak-label calibration | Close surveillance lead for a scalar uncertainty-denominator form; preprint status prevents treating it as formal occupancy, and its ambiguity is not independently annotated input semantics | Non-authoritative preprint lead |
| [SIGNPOST-Bench, arXiv 2026](https://arxiv.org/abs/2608.04244) | Uses 5,111 paired Original, Blank, Similar, Random, and Adversarial text-in-image groups to study conflict resolution | Subsumes a first paired conflict-versus-missing/unrelated/adversarial-control benchmark claim; does not measure semantic ambiguity | Strong controlled benchmark |
| [Ghosh et al., arXiv 2026](https://arxiv.org/abs/2608.17205) | Crosses image/text conflict with four legibility levels, counterbalances sources, and adjusts modality reliance for unimodal accuracy loss | Subsumes a first conflict-versus-degradation design; legibility/corruption is not genuine semantic ambiguity and reliance is not a conflict estimand | Strong controlled study |

The probabilistic-representation line—[PCME, CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Chun_Probabilistic_Embeddings_for_Cross-Modal_Retrieval_CVPR_2021_paper.html),
[ProbVLM, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Upadhyay_ProbVLM_Probabilistic_Adapter_for_Frozen_Vison-Language_Models_ICCV_2023_paper.html),
and [PCME++, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ad9d6ab10446114cf5482d5e1f971a84-Abstract-Conference.html)—already establishes distributional image--text representations. Consequently,
a Gaussian embedding, covariance head, Wasserstein distance, or overlap score is
an implementation candidate, not a contribution by itself.

## Highest-Risk Novelty Threats

1. **RCML and Discounted Belief Fusion:** invalidate a broad claim to the first
   evidential conflict estimator adjusted by confidence, reliability, or
   vacuity. CONFER remains a non-authoritative surveillance lead and cannot
   carry this kill.
2. **When Modalities Conflict:** invalidates a claim to the first controlled
   conflict study that independently varies unimodal difficulty and relates it
   to source preference.
3. **MMMC:** invalidates a first-definition, first-dataset, or generic
   modality-conflict/hallucination framing.
4. **SIGNPOST-Bench, Which Source Wins, CrossCheck-Bench, and CLASH:** together
   invalidate a paper identity centered only on paired conflict interventions,
   degradation/missingness controls, or contradiction-detection accuracy.
5. **Subjective-logic vacuity/dissonance and CoRiM:** invalidate a generic
   ambiguity-versus-conflict decomposition or conflict-aware decision-risk
   contribution.
6. **Phrase-grounded chest-radiograph fact checking:** invalidates a medical
   novelty claim based only on atomic finding perturbation and image--text
   verification.

The peer-reviewed entries are kill threats, not ceremonial citations. The
method and experiment must be designed so that those approaches can falsify the
proposed component under matched inputs and evaluation budgets. Preprint-only
entries guide surveillance and sensitivity design but cannot independently
kill novelty.

## Gap That Provisionally Survives

DR-0016 accepts that no new pointwise-estimator gap survived TB-0006. The
paper-faithful `PROBVLM-2ADAPTER` score is therefore an explicitly non-novel
instrument, and `POINT-2ADAPTER-RECON` is a project-native matched ablation—not
a second novelty claim.

**Inference, not fact:** the broad claim “estimate cross-modal conflict after
accounting for modality ambiguity/uncertainty” is occupied. The audited sources
do not yet establish the narrower complete Method-A combination below:

> an intervention-defined, proposition-level semantic incompatibility
> estimand that uses independent semantic measurements, compares approved
> modality-specific information-loss controls under fixed construction rules,
> treats natural image/text ambiguity as a separately specified observational
> veto unless a governed identification route is added, audits surface
> artifacts, and is not reducible to
> output disagreement adjusted by confidence, and adds held-out proper-score
> and equal-budget selective value beyond matched deterministic, evidential,
> probabilistic, and generic failure predictors.

The conjunction is not automatically a contribution. It survives only if the
partial construct is mathematically non-circular, the intervention-relative
population target is identified under defensible assumptions, the complete
combination remains unoccupied after continued audit, and the result is not
subsumed empirically by the closest methods above. Chest radiography is
validation evidence, not the source of domain-generality.

## Mandatory Comparison Consequences

Before implementation, every candidate formula must undergo an analytic
equivalence screen against the families below. The Month-3 kill test then
instantiates the smallest four-family set in the measurement protocol,
including at least one closest published evidential/uncertainty-adjusted score.
Before confirmatory promotion, the comparison plan must cover, subject to task
validity, implementation feasibility, and licence audit:

- a matched deterministic conditional compatibility classifier/density ratio;
- subjective-logic vacuity/dissonance and RCML conflict degree or the closest
  task-valid analogues;
- Discounted Belief Fusion or an exactly documented task-valid
  reimplementation;
- CoRiM's modality-conflict-risk principle or an exactly documented
  task-valid comparator;
- relative unimodal entropy/source-following measures from *When Modalities
  Conflict*, plus SIGNPOST-style paired shifts and legibility-adjusted source
  reallocation where task-valid;
- deterministic similarity/retrieval margin and unimodal ambiguity controls;
- a published task-matched conflict method: MMMC-style conflict/hallucination,
  CrossCheck-style conflict resolution, or CLASH-style contradiction-detection
  supervision if its interface can be matched without privileged labels;
- matched generic failure prediction through
  [ViLU](https://openaccess.thecvf.com/content/ICCV2025/html/Lafon_ViLU_Learning_Vision-Language_Uncertainties_for_Failure_Prediction_ICCV_2025_paper.html)
  and [Adaptive Confidence Regularization](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Adaptive_Confidence_Regularization_for_Multimodal_Failure_Detection_CVPR_2026_paper.pdf)
  where reproducible;
- if probabilistic embeddings remain,
  [ICPE](https://openaccess.thecvf.com/content/WACV2026/html/Lin_Intra-Class_Probabilistic_Embeddings_for_Uncertainty_Estimation_in_Vision-Language_Models_WACV_2026_paper.html)
  and a modality-gap/embedding-scale audit rather than only inter-modal
  distance;
- [phrase-grounded chest-radiograph fact checking](https://papers.miccai.org/miccai-2025/0693-Paper3526.html)
  as a medical task comparator if its inputs and supervision can be matched.

If a method cannot be fairly ported, the exclusion must be justified before
results are seen; a weak substitute must not be described as reproducing it.

## Code and Reproduction Audit State

Author- or paper-linked repositories were located for
[MMMC](https://github.com/zmzhang2000/MMMC),
[Discounted Belief Fusion](https://github.com/bezirganyan/DBF_uncertainty),
[RCML](https://github.com/jiajunsi/RCML),
[CrossCheck-Bench](https://github.com/bytedance/CrossCheck-Bench), and
[CLASH](https://github.com/tpopordanoska/clash), as well as the recent
[SIGNPOST-Bench](https://github.com/inorganicwriter/SIGNPOST-Bench) and
[Which Source Wins](https://github.com/Ro-netizen004/multimodal-arbitration-artifact)
preprints. Their existence is a
literature lead only. No repository was cloned, no dependency or checkpoint
was downloaded, and no result was reproduced. Commit hashes, tags, licences,
data provenance, model access, compute, and compatibility with the frozen task
remain pre-execution audit fields.

## Claim and Kill Rules

- Do not claim the first definition, dataset, detector, decomposition, or
  conflict-aware fusion method.
- Reject before implementation any candidate score that is a monotone
  transformation or minor parameterization of disagreement already
  authoritatively represented by RCML, Discounted Belief Fusion, relative
  entropy, or deterministic matching. Treat a CONFER-like uncertainty
  denominator as unadjudicated for formal novelty pending authoritative
  evidence, while still requiring a separate semantic-identification bridge.
- Do not equate latent distance, predictive divergence, uncertainty mass, or
  contradiction accuracy with identified conditional conflict.
- Kill the estimator claim if a matched deterministic conditional predictor
  reaches the pre-specified equivalence/non-inferiority boundary.
- Kill the identifiability claim if ambiguity, missingness, corruption,
  provenance, or surface artifacts explain the controlled contrast.
- Kill the claimed framework novelty if a primary source establishes the same
  partial-construct support, independent modality-only measurement,
  intervention/control target, joint inference, and matched deterministic
  challenge. Do not compensate by reviving a killed pointwise estimator.
- Narrow the venue claim if the enduring contribution is controlled evaluation
  science rather than a sufficiently substantive general framework; this is a
  same-route venue decision, not authorization for a second project.
- Continue the audit before every promotion gate and again after the official
  NeurIPS 2027 call. Publication is never presumed.
