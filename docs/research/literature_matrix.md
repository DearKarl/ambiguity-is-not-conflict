# Literature Matrix

**Status:** Peer-reviewed primary-source audit plus explicitly labelled
preprint leads through 2026-08-29; implementation, version, and reproduction
audits remain open

The matrix records what a primary source motivates and what it does not
establish for this project. Inclusion is not endorsement or evidence of
reproducibility.

| Area | Primary source | Relevance | Boundary for this project |
| --- | --- | --- | --- |
| Output semantic uncertainty | [Farquhar et al., Nature 2024](https://www.nature.com/articles/s41586-024-07421-0) | Measures uncertainty at the level of answer meaning | Does not isolate input-level image--text conflict |
| Evaluation incentives | [Kalai et al., Nature 2026](https://www.nature.com/articles/s41586-026-10549-w) | Motivates abstention-aware evaluation and explicit error costs | Does not supply a cross-modal decomposition |
| Text uncertainty benchmark | [LM-Polygraph, TACL 2025](https://aclanthology.org/2025.tacl-1.11/) | Supplies output-UQ estimators and comparison discipline | Text-only evidence is a baseline, not the core result |
| View disagreement | [Christoudias et al., UAI 2008](https://proceedings.mlr.press/r6/christoudias08a.html) | Establishes multi-view learning under view disagreement as an old problem | “Modality disagreement” alone cannot be a novelty claim |
| Vacuity versus dissonance | [Han et al., NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/c80d9ba4852b67046bee487bcd9802c0-Abstract.html) | Formally separates lack of evidence from conflict of strong evidence in subjective logic | Prevents claiming the ambiguity/conflict distinction itself as new; requires a matched evidential baseline |
| Reliable conflictive multi-view learning | [RCML, AAAI 2024](https://ojs.aaai.org/index.php/AAAI/article/view/29546) | Combines view-specific evidential decisions and reliabilities for conflictive instances | Confident/evidential disagreement is not new; semantic input ambiguity still requires independent definition |
| Probabilistic cross-modal embedding | [PCME, CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Chun_Probabilistic_Embeddings_for_Cross-Modal_Retrieval_CVPR_2021_paper.html) | Establishes a distributional image--text representation | Representation spread is not automatically an identified uncertainty source |
| Improved probabilistic embedding | [PCME++, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ad9d6ab10446114cf5482d5e1f971a84-Abstract-Conference.html) | Updated probabilistic retrieval comparison | Retrieval performance does not establish calibration or conflict specificity |
| Frozen-VLM probabilistic adapter | [ProbVLM, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Upadhyay_ProbVLM_Probabilistic_Adapter_for_Frozen_Vison-Language_Models_ICCV_2023_paper.html) | Motivates a tractable adapter route | Must be matched to deterministic and epistemic baselines |
| Cross-modal inconsistency | [van Sprang et al., CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/van_Sprang_Same_Content_Different_Answers_Cross-Modal_Inconsistency_in_MLLMs_CVPR_2026_paper.html) | Shows behavioural inconsistency across modality presentations | Behavioural inconsistency is not ambiguity-versus-conflict decomposition |
| Input modality conflict | [MMMC, ICML 2025](https://proceedings.mlr.press/v267/zhang25dq.html) | Formally defines input modality conflict, constructs a benchmark, and evaluates mitigation of associated hallucination | Subsumes first-definition/first-conflict-benchmark claims; the surviving question is conditional identification and incremental value |
| Conflict-aware uncertainty fusion | [Discounted Belief Fusion, AISTATS 2025](https://proceedings.mlr.press/v258/bezirganyan25a.html) | Proposes order-invariant evidential fusion with conflict-based discounting and uncertainty-based conflict detection | Direct estimator threat; crossed ambiguity and artifact controls must distinguish the proposed target |
| Medical phrase fact checking | [Mahmood et al., MICCAI 2025](https://papers.miccai.org/miccai-2025/0693-Paper3526.html) | Detects perturbed chest-radiograph finding/location errors at phrase level | Subsumes a generic atomic medical compatibility or synthetic-perturbation identity; requires a matched medical comparator |
| Medical hallucination risk | [ReXTrust, PMLR 2025](https://proceedings.mlr.press/v281/hardy25a.html) | Predicts finding-level hallucination risk from VLM hidden states on MIMIC-CXR | Failure prediction is not semantic conflict, but the frozen instrument score must add beyond it |
| Conflict-driven risk | [CoRiM, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Zou_CoRiM_Conflict-driven_Risk_Minimization_for_Dynamic_Multimodal_Fusion_CVPR_2026_paper.pdf) | Defines predictive-distribution modality-conflict risk for dynamic fusion | Symmetric divergence or conflict-aware risk weighting is not sufficient novelty |
| Non-authoritative ambiguity/dissent lead | [CONFER, arXiv v1 2026](https://arxiv.org/abs/2608.07867v1) | Reports modality-specific uncertainty-adjusted compatibility and separates consensus, dissent, and ambiguity regimes for weak-label calibration | Preprint-only surveillance lead; excluded from formal novelty-kill evidence and mandatory baselines unless authoritative status changes |
| Conflict versus unimodal difficulty | [When Modalities Conflict, arXiv 2025](https://arxiv.org/abs/2511.02243) | Independently varies image/text reasoning difficulty and relates relative entropy to modality following | Subsumes a first controlled difficulty-adjusted conflict study; model confidence is not independently annotated semantic ambiguity |
| Paired missing/adversarial controls | [SIGNPOST-Bench, arXiv 2026](https://arxiv.org/abs/2608.04244) | Uses Original, Blank, Similar, Random, and Adversarial paired groups | Subsumes a first paired conflict-versus-missing/unrelated benchmark claim; lacks semantic ambiguity measurement |
| Conflict versus legibility | [Which Source Wins, arXiv 2026](https://arxiv.org/abs/2608.17205) | Crosses source conflict with graded image/text legibility and measures reliance shifts | Subsumes a first degradation-controlled conflict design; corruption/legibility is not genuine ambiguity |
| Conflict resolution | [CrossCheck-Bench, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/39788) | Benchmarks multimodal conflict-resolution reasoning under controlled contradictory evidence | Conflict-resolution accuracy does not identify an uncertainty source or establish calibration |
| Cross-modal contradiction benchmark | [CLASH, CVPR 2026 Findings](https://openaccess.thecvf.com/content/CVPR2026F/papers/Popordanoska_CLASH_A_Benchmark_for_Cross-Modal_Contradiction_Detection_CVPRF_2026_paper.pdf) | Supplies human-verified cross-modal contradiction detection cases | Subsumes a generic controlled-contradiction benchmark identity |
| Generic failure prediction | [ViLU, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Lafon_ViLU_Learning_Vision-Language_Uncertainties_for_Failure_Prediction_ICCV_2025_paper.html) | Supplies a strong learned failure-prediction comparator | The proposed component must add value beyond this class |
| Bayesian VLM approximation | [BayesVLM, OpenReview](https://openreview.net/forum?id=XLiUcvHfzS) | Candidate approximate-Bayesian baseline | Bayesian naming does not guarantee calibration or identifiability |
| Distribution-free selection | [Conformal prediction for zero-shot models, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Silva-Rodriguez_Conformal_Prediction_for_Zero-Shot_Models_CVPR_2025_paper.html) | Candidate risk-control layer | Guarantees depend on the calibration population and assumptions |

## Formal Equivalence Consequences

The [estimator formalization audit](estimator_formalization_audit.md) records
three pre-data method-claim kills:

1. binary self-corrected learned-belief disagreement is exactly
   \((\widehat p_v-\widehat p_t)^2\); its independent-Gaussian analogue cancels
   both covariance traces after the same self-spread correction and leaves
   deterministic mean distance;
2. a conditional conflict-versus-compatibility likelihood ratio is exactly a
   classifier logit minus the known conditional sampling-prior log-odds; and
3. binary evidential projected-distance times conjunctive certainty is exactly
   \(|\widehat p_v-\widehat p_t|(1-u_v)(1-u_t)\), the occupied RCML
   confident-disagreement structure.

PCME++ explicitly places Gaussian mean distance and marginal variances in its
closed-form sampled distance. Together with the three derivations, the
peer-reviewed evidence prevents a new-estimator claim based only on a cosmetic
link, covariance head, or evidential certainty gate. CONFER reports a close
scalar squared-disagreement-over-summed-uncertainty form, but its arXiv-v1
status makes that formula a surveillance lead rather than formal occupancy
evidence here. A denominator-based candidate remains unadjudicated for novelty
and still requires a separate semantic-identification argument. None of these
facts proves empirical deterministic subsumption or establishes that the
retained intervention-specificity framework is itself novel.

## Measurement and Statistical Anchors

| Topic | Primary source | Use | Boundary |
| --- | --- | --- | --- |
| Proper scores | [Gneiting and Raftery, JASA 2007](https://doi.org/10.1198/016214506000001437) | Supports Brier/NLL as proper predictive-score families | Does not choose this project's SESOI or target population |
| Reliability reporting | [GRRAS](https://www.equator-network.org/reporting-guidelines/guidelines-for-reporting-reliability-and-agreement-studies-grras-were-proposed/) | Requires explicit samples, readers, design, inter/intra-reader analysis, and reporting | A reporting guideline does not validate the proposed construct or cutoff |
| Multi-reader CXR precedent | [VinDr-CXR, Scientific Data 2022](https://www.nature.com/articles/s41597-022-01498-w) | Demonstrates independent multi-radiologist chest-radiograph annotation at scale | Its reader counts and labels do not transfer automatically to this instrument |
| Observer-error aggregation | [Dawid and Skene, JRSS C 1979](https://doi.org/10.2307/2346806) | Motivates explicit reader-error modelling | A single latent-truth model can collapse genuine item ambiguity into reader error |
| Equivalence | [Schuirmann, J Pharmacokinet Biopharm 1987](https://pubmed.ncbi.nlm.nih.gov/3450848/) | Supports two one-sided equivalence logic | Failure to show superiority is not equivalence or deterministic subsumption |
| Simultaneous inference | [Romano and Wolf, JASA 2005](https://doi.org/10.1198/016214504000000539) | Motivates resampling-based familywise simultaneous bounds | Exact patient-cluster implementation and covariance remain to be frozen |
| CXR spatial resolution | [Herron et al., Radiology 2000](https://pubmed.ncbi.nlm.nih.gov/10751483/) | Shows observer effects of resolution can be abnormality-specific | Does not validate pleural-effusion transfer or the proposed `224 -> 112 -> 224` control; clinical acceptance remains mandatory |
| CXR lossy compression | [Beall et al., Journal of Digital Imaging 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC3453278/) | Supplies an observer-study warning that non-significant compression differences are not uniform semantic preservation | Does not establish equivalence, modern-input transfer, or a primary compression severity |
| Simulated dose reduction | [Veldkamp et al., Journal of Digital Imaging 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC3043684/) | Shows a dose-like simulation used detector/raw-data and noise-system calibration | Generic noise applied to post-processed MIMIC JPG cannot be called dose simulation |
| Behavioural perturbation tests | [CheckList, ACL 2020](https://aclanthology.org/2020.acl-main.442/) and [Contrast Sets, EMNLP Findings 2020](https://aclanthology.org/2020.findings-emnlp.117/) | Motivate prospective invariance/directional tests and local counterfactual evaluation | Neither source supplies a clinically valid `M_t` or makes a label-changing perturbation information loss |
| Radiology semantic states | [CheXpert, AAAI 2019](https://ojs.aaai.org/index.php/AAAI/article/view/3834) and [RadGraph, NeurIPS Datasets and Benchmarks 2021](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/c8ffe9a587b126f152ed3d89a146b445-Abstract-round1.html) | Distinguish positive/negative/uncertain/no-mention or modifier/relation states | Report-side schemas do not establish image truth; deleting the atomic polarity carrier makes state unavailable, not negative or ambiguous |
| Classifier two-sample/probe tests | [Lopez-Paz and Oquab, ICLR 2017](https://arxiv.org/abs/1610.06545) and [Ojala and Garriga, JMLR 2010](https://www.jmlr.org/beta/papers/v11/ojala10a.html) | Motivate held-out condition recovery and label-permutation calibration | A fitted classifier is a lower-bound detector, not proof of distributional equality or absence of artifacts |
| Conjunctive equivalence | [Eaton and Muirhead, JSPI 2007](https://doi.org/10.1016/j.jspi.2007.03.021) | Supports intersection--union logic when every co-primary component must pass | Global Type-I control does not remove the need for joint-power planning, orientation safety, or pipeline simulation |

## Official Model Candidates

| Model | Official fact used for planning | Eligibility boundary |
| --- | --- | --- |
| [BiomedCLIP](https://huggingface.co/microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224) | Biomedical dual encoder trained on PMC-15M; MIT licence | Conditional candidate only; no patient-level MIMIC exclusion manifest |
| [SigLIP2 base 224](https://huggingface.co/google/siglip2-base-patch16-224) | General-domain image-text encoder trained with WebLI-family data; Apache-2.0 | Unknown-exposure matched breadth/sensitivity only pending overlap audit |
| [BioViL-T](https://huggingface.co/microsoft/BiomedVLP-BioViL-T) | Official card states PubMed plus MIMIC/MIMIC-CXR training; MIT licence | Known-exposure diagnostic, not primary/confirmatory MIMIC evidence |
| [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) | Generative vision-language interface; Apache-2.0 | Unknown exposure and unmatched interface; stress/breadth only |
| [TorchVision ResNet-50](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet50.html) plus [original BERT](https://aclanthology.org/N19-1423/) | Official documentation names ImageNet-1K vision weights and BooksCorpus/Wikipedia text pretraining | Source/type/time-auditable strict non-VLM control lead only; exact checkpoint lineage, dates, licences, and source exclusion still require audit before access |

## Candidate Medical Resources

| Resource | Candidate role | Required decision |
| --- | --- | --- |
| [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/) | Paired chest radiographs and free-text reports | Access, version, cohort, ontology, leakage, and derived-artifact permissions |
| [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) | Standardized image files and structured labels | Whether label uncertainty supports rather than circularly defines ambiguity |
| [ReXErr v1.0.0](https://physionet.org/content/rexerr-v1/1.0.0/) | MIMIC-derived synthetic report-error stress set | Compatibility with the frozen finding-level unit; inheritance of the MIMIC patient/source split; never independent breadth |
| [VisMin, NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/hash/c3070c3388552a08a3326f0d28dc2af9-Abstract-Conference.html) | Candidate controlled general-domain compatibility stress test | Snapshot, inherited asset terms, contamination, and added ambiguity/information-loss controls |
| [PadChest-GR](https://bimcv.cipf.es/bimcv-projects/padchest-gr/) | Candidate independent medical atomic-finding resource | Formal access, derivative-intervention permission, ambiguity labels, and target-population mismatch |
| [CheXpert Plus](https://aimi.stanford.edu/datasets/chexpert-plus) | Candidate larger independent medical image--report cohort | Redivis terms, image-grounded truth, split, derivation, and contamination audit |

## Reproducibility Patterns

The project will adopt patterns visible in strong research repositories:

- explicit install, data, train, evaluate, and result-reproduction commands;
- one versioned configuration per declared experiment cell;
- separate data schema, controlled generation, quality filtering, estimation,
  and evaluation;
- stable interfaces for matched modality controls;
- tests, CI, citation metadata, governance, and documented result locations;
- exact dataset/model revisions, seeds, hardware, runtime, and table/figure
  provenance.

These are engineering patterns, not evidence that the associated papers answer
this project's research question.

Repository-design references inspected at initialization include
[BendVLM](https://github.com/waltergerych/bend_vlm) for a lean paper-oriented
workflow, [VisMin](https://github.com/rabiulcste/vismin) for controlled
minimal-change construction and filtering,
[MMStar](https://github.com/MMStar-Benchmark/MMStar) for matched modality
evaluation, [UniBench](https://github.com/facebookresearch/unibench) for tested
benchmark adapters and CI,
[Uncertainty Baselines](https://github.com/google/uncertainty-baselines) for
separating stable baselines from experiments, and
[einspace](https://github.com/linusericsson/einspace) for versioned
configuration-driven runs. Their licences and design choices are independent;
no code or assets were copied into this repository.

## Defensible Gap

**Inference, not fact:** the broad conflict-after-uncertainty-adjustment claim is
already occupied. The narrower current unresolved question is:

> Can a prospectively frozen score show an intervention-relative population
> response specific to assigned determinate incompatibility against approved
> modality-specific information-loss controls, survive separate observational
> veto audits for natural ambiguity and artifacts, and add held-out proper-score and equal-
> budget selective value beyond confidence-adjusted output disagreement and
> matched deterministic, evidential, probabilistic, and generic failure
> predictors?

The gap admits a useful null result. If the matched deterministic predictor
subsumes the probabilistic instrument, the current Main Track route is killed
and the comparison must be reported rather than hidden or repackaged.

At the current Gate-0 state, natural ambiguity can only falsify this narrow
claim. A broader ambiguity-separation claim requires a separately approved
valid intervention or observational identification route.

The detailed kill-threat analysis and claim boundary are maintained in the
[novelty audit](novelty_audit.md). Dataset facts and unresolved access rights
are maintained in the [dataset feasibility audit](dataset_feasibility_audit.md).

## Bibliographic Audit Fields

Before promoting a source, record title, authors, venue, year, DOI/stable URL,
review status, official code, licence, commit/tag, dataset/checkpoint versions,
compute requirements, claim selected for comparison, and known deviations.
