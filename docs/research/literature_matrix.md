# Literature Matrix

**Status:** Seed evidence map; every entry requires version/code audit before use

The matrix records what a primary source motivates and what it does not
establish for this project. Inclusion is not endorsement or evidence of
reproducibility.

| Area | Primary source | Relevance | Boundary for this project |
| --- | --- | --- | --- |
| Output semantic uncertainty | [Farquhar et al., Nature 2024](https://www.nature.com/articles/s41586-024-07421-0) | Measures uncertainty at the level of answer meaning | Does not isolate input-level image--text conflict |
| Evaluation incentives | [Kalai et al., Nature 2026](https://www.nature.com/articles/s41586-026-10549-w) | Motivates abstention-aware evaluation and explicit error costs | Does not supply a cross-modal decomposition |
| Text uncertainty benchmark | [LM-Polygraph, TACL 2025](https://aclanthology.org/2025.tacl-1.11/) | Supplies output-UQ estimators and comparison discipline | Text-only evidence is a baseline, not the core result |
| Probabilistic cross-modal embedding | [PCME, CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Chun_Probabilistic_Embeddings_for_Cross-Modal_Retrieval_CVPR_2021_paper.html) | Establishes a distributional image--text representation | Representation spread is not automatically an identified uncertainty source |
| Improved probabilistic embedding | [PCME++, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ad9d6ab10446114cf5482d5e1f971a84-Abstract-Conference.html) | Updated probabilistic retrieval comparison | Retrieval performance does not establish calibration or conflict specificity |
| Frozen-VLM probabilistic adapter | [ProbVLM, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Upadhyay_ProbVLM_Probabilistic_Adapter_for_Frozen_Vison-Language_Models_ICCV_2023_paper.html) | Motivates a tractable adapter route | Must be matched to deterministic and epistemic baselines |
| Cross-modal inconsistency | [van Sprang et al., CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/van_Sprang_Same_Content_Different_Answers_Cross-Modal_Inconsistency_in_MLLMs_CVPR_2026_paper.html) | Shows behavioural inconsistency across modality presentations | Behavioural inconsistency is not ambiguity-versus-conflict decomposition |
| Conflict resolution | [CrossCheck-Bench, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/39788) | Tests contradiction detection and conflict resolution | Benchmark accuracy does not identify uncertainty source or calibration |
| Generic failure prediction | [ViLU, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Lafon_ViLU_Learning_Vision-Language_Uncertainties_for_Failure_Prediction_ICCV_2025_paper.html) | Supplies a strong learned failure-prediction comparator | The proposed component must add value beyond this class |
| Bayesian VLM approximation | [BayesVLM, OpenReview](https://openreview.net/forum?id=XLiUcvHfzS) | Candidate approximate-Bayesian baseline | Bayesian naming does not guarantee calibration or identifiability |
| Distribution-free selection | [Conformal prediction for zero-shot models, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Silva-Rodriguez_Conformal_Prediction_for_Zero-Shot_Models_CVPR_2025_paper.html) | Candidate risk-control layer | Guarantees depend on the calibration population and assumptions |

## Candidate Medical Resources

| Resource | Candidate role | Required decision |
| --- | --- | --- |
| [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/) | Paired chest radiographs and free-text reports | Access, version, cohort, ontology, leakage, and derived-artifact permissions |
| [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) | Standardized image files and structured labels | Whether label uncertainty supports rather than circularly defines ambiguity |
| [ReXErr v1.0.0](https://physionet.org/content/rexerr-v1/1.0.0/) | External report-error stress test | Compatibility with the frozen finding-level unit and split |

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

> Does an explicitly identified measure of conditional image--text conflict add
> calibrated, decision-relevant information beyond image ambiguity, text
> ambiguity, epistemic uncertainty, output semantic uncertainty, ordinary
> confidence, and generic failure prediction under controlled interventions?

The gap admits a useful null result. If a matched deterministic predictor
subsumes conflict, the project must narrow its claim rather than hide the
comparison.

## Bibliographic Audit Fields

Before promoting a source, record title, authors, venue, year, DOI/stable URL,
review status, official code, licence, commit/tag, dataset/checkpoint versions,
compute requirements, claim selected for comparison, and known deviations.
