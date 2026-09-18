# Historical Dataset Preparation Note

Migration wrapper dated 2026-09-18: the September 15 explanation below is
preserved as historical public research context. Its application-status
statements are superseded by the [September 18 progress ledger](../docs/research/progress_2026-09-18.md).
It is not scientific authority or permission to access data. NeurIPS 2027
Main Track remains the sole objective under DR-0019. The original local source
was not modified. Source SHA-256:
`7bbf45fecbbcbd87a35021dd646f649d84b72ea3ee3a51c39fa911483b7aa418`.

The text below contains the safe explanatory note, not a meeting transcript,
private correspondence, application record or training report.
Trailing whitespace was normalized in this copy for staged validation; the
source hash identifies the untouched original, not this wrapped copy.

---

# MIMIC data plan for *Ambiguity Is Not Conflict*

**Publication target: NeurIPS 2027 Main Track**
**For supervisor discussion · 15 September 2026**

## 1. One paper, one focused first study

Our sole publication target for this project is a high-quality **NeurIPS 2027 Main Track** paper. The intended contribution is a measurement and inference framework for testing whether a cross-modal score responds specifically to **determinate semantic conflict**, while treating ambiguity and information loss separately. Chest radiography provides the first controlled validation setting. Publication is the objective; the scientific claims must remain falsifiable and supported by the results.

The first study should stay focused on **one finding, provisionally pleural effusion presence/absence, using one exact frontal chest X-ray and one atomic text assertion**. The clinical suitability of that image unit still needs to be established. The primary question is:

> When image evidence and text meaning are independently determinate, does a frozen score respond specifically to their incompatibility, beyond its response to controlled information loss and construction artifacts?

The existing Method-A route compares a probabilistic image–text instrument with a matched deterministic comparator. It requires evidence of conflict specificity and incremental value over that comparator. Natural ambiguity is a separate falsification test: passing it does not, by itself, establish causal separation from ambiguity. Calibration and selective review follow only after the measurement claim is supported.

This first experiment concerns image–text vision–language representations. Any later generative multimodal-LLM evaluation or breadth study must test the same construct under a defined protocol. The immediate data request is therefore a focused radiograph–report resource with independent clinical assessment, rather than an expansion of modalities or disease tasks.

## 2. What MIMIC provides and how image–text pairing works

We propose retaining **MIMIC-CXR v2.1.0 together with MIMIC-CXR-JPG v2.1.0 as one coupled primary preparation source**.

| Resource | Available data | Role in our first study |
| --- | --- | --- |
| [MIMIC-CXR v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/) | De-identified chest radiographs in DICOM format, original free-text radiology reports, and patient/study/image linkage. The documented corpus contains 377,110 images from 227,835 studies at Beth Israel Deaconess Medical Center, Boston. | Supplies the source image–report relationship and original wording; DICOM remains available if clinically necessary for the chosen image representation. |
| [MIMIC-CXR-JPG v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/) | JPG conversions, image metadata, reference train/validation/test splits, and CheXpert/NegBio report-derived labels for 14 observation categories, including pleural effusion. | Provides a convenient image representation and candidate-screening information. It is derived from MIMIC-CXR, so it is not independent external validation. |

The linkage is:

```text
Patient (subject_id)
  → Examination / study (study_id)
      → One radiology report
      → One or more images (dicom_id), potentially with different views
```

**The native pairing is at study level, not necessarily one report per image.** A report can describe the combined examination. Our single-image task therefore needs eligibility and coverage checks before a report statement can be related to the selected image. Original reports come from MIMIC-CXR; the JPG companion does not replace them. [Source: MIMIC-CXR documentation](https://physionet.org/content/mimic-cxr/2.1.0/).

The JPG label files cover 227,827 studies; eight source studies could not be labelled. Their values distinguish positive (`1`), negative (`0`), uncertain (`-1`) and unmentioned (blank). The manual test annotations also assess reports. These are **text-derived observations**, not independent judgments of what one exact image supports. [Source: JPG label documentation](https://physionet.org/content/mimic-cxr-jpg/2.1.0/).

For our measurement problem, `-1` cannot simply become “image ambiguity”, and blank cannot become “absence”. A statement can express clinical uncertainty in perfectly clear language. We must preserve that distinction when defining text ambiguity.

## 3. How to apply for access

Both resources are credentialed-access datasets. Their pages require an approved PhysioNet credentialing status, the specified research training and the project data-use agreement. Registration alone does not grant access. [MIMIC-CXR access requirements](https://physionet.org/content/mimic-cxr/2.1.0/).

1. **Create an individual PhysioNet account and apply for credentialing.** Use accurate university and research information; prepare a concise description of this retrospective image–text study. Start at the [credentialing page](https://physionet.org/settings/credentialing/) after signing in. Academic email or an institution-linked ORCID helps verification; a nominated reference may be asked to respond. Each person accessing restricted material needs an approved access basis. [Credentialing FAQ](https://physionet.org/about/faqs/).
2. **Complete the required CITI training.** The resource pages specify **Data or Specimens Only Research**. PhysioNet's instructions provide the **Massachusetts Institute of Technology Affiliates** course route for non-MIT researchers; an MIT email address is not required. Complete that course and the listed **Conflicts of Interest** modules. This training affiliation does not replace our actual Bristol affiliation. [Official CITI instructions](https://physionet.org/about/citi-course/).
3. **Submit the full training report to PhysioNet.** Upload the completion report that lists the modules, rather than only the certificate, through [training settings](https://physionet.org/settings/training/), and check its approval status. Existing training should not be assumed sufficient without confirmation against the current requirements. [Submission guidance](https://physionet.org/about/citi-course/).
4. **Read and accept the relevant project DUA personally.** Return to each of the two resource pages and complete its access requirements. Check that both resources are accessible under the approved account; do not assume access to another MIMIC project covers them. The [MIMIC-CXR DUA](https://physionet.org/content/mimic-cxr/view-dua/2.1.0/) requires research use, secure handling, no sharing of access, and contribution of relevant code when results are openly disseminated.
5. **Confirm university arrangements before restricted processing.** Establish the project's ethics determination, permitted clinical review and derived assertions, named access holders, approved storage/compute, and release rules. PhysioNet access and university project authorization are separate requirements.

MIMIC use is free under the stated agreement; annotation, storage and compute still need a budget. Approval dates and our current account status remain unverified. [MIMIC usage notes](https://physionet.org/content/mimic-cxr/2.1.0/).

Our planned processing boundary is an approved local or institutional environment. Restricted records and derivatives stay out of GitHub and general online AI tools. PhysioNet's current guidance requires verified data-handling conditions for any cloud/API use and does not endorse particular providers. [Online-service guidance, September 2025](https://physionet.org/news/post/llm-responsible-use/).

## 4. The minimum data needed first

The first practical milestone is to establish whether MIMIC can support a **patient-separated, clinically assessable single-frontal-image cohort**. It is not necessary to begin by retrieving the entire image archive or linking a full electronic health record.

The proposed initial feasibility screening uses only the already specified restricted tabular fields:

| Information | Fields needed | Feasibility question |
| --- | --- | --- |
| Patient/study/image linkage and reference split | `subject_id`, `study_id`, `dicom_id`, `split` | Can images and studies be joined consistently and patients kept separate? |
| View and image dimensions | `dicom_id`, `ViewPosition`, `Rows`, `Columns` | How many studies satisfy the strict single-frontal candidate rule? |
| Candidate finding screen | `subject_id`, `study_id`, `Pleural Effusion` from each report labeler | What candidate counts and report-label strata are available? |

These fields come from the JPG split, metadata, CheXpert and NegBio files. [File and schema documentation](https://physionet.org/content/mimic-cxr-jpg/2.1.0/). They remain restricted data even though the schema is public. The table describes a future authorized screening step, not a query already performed.

After eligibility, permissions and the remaining study decisions are settled, the research subset would need:

- The exact selected frontal images in one documented representation, with relevant quality and preprocessing information.
- Their linked original reports, retaining findings/impression where available, negation, qualifiers and references to prior studies; report structure must be checked rather than assumed complete.
- Patient/study/image mapping, study-view coverage and partition provenance, with every variant from a source patient kept together.
- Positive and negative candidates, a separately identified natural-indeterminacy audit subset, and a natural-prevalence evaluation sample for later risk calibration.

Actual eligible counts and annotation attrition must inform the power analysis. Total corpus size cannot establish that the required cohort exists.

## 5. What MIMIC does not settle: our additional measurements

MIMIC supplies a credible source population and image–report linkage. To test *ambiguity is not conflict*, we still need an approved independent measurement process:

| Measurement | What must be recorded |
| --- | --- |
| **Image-only assessment** | What the exact image supports: present, absent or indeterminate; assessability, quality limitations and plausible alternative interpretations. The reader must not see the paired text. |
| **Text-only assessment** | The assertion's meaning, polarity, qualifiers, anatomy and temporal reference, without seeing the image. |
| **Reader reliability** | Individual ratings, confidence/abstention and reasons, with repeated assessments where specified. Disagreement must be investigated, not automatically treated as intrinsic ambiguity. |
| **Pair validity** | Whether independently determinate inputs concern the same proposition and are compatible or incompatible. Pair review must not overwrite modality-only measurements. |

If both inputs are determinate and support opposing states of the same proposition, the pair can be labelled conflicting. **If either input is indeterminate, conflict remains undefined.** Information loss is recorded separately and can occur while an input remains determinate.

The dataset does not need to contain natural contradictions or ready-made conflict labels. After approval and clinical validation, matched compatible/conflicting assertions and information-loss controls can be constructed. Construction must control wording, negation, template and provenance cues; randomly mismatching patients is not a sufficient gold standard.

The quantity of interest is the **within-source change in a frozen score under a determinate compatibility intervention, assessed against its response to validated controls**. This supports a population specificity claim under the stated assumptions. It is not automatically a conflict probability for any new pair. Subsequent error-risk calibration requires held-out patients and the intended population distribution; a balanced synthetic sample does not establish clinical prevalence.

## 6. The first decisions to make with the supervisor

The immediate proposal is to **prepare access to the coupled MIMIC-CXR/JPG resource and resolve the clinical measurement requirements for one finding**. Four decisions would make the next step concrete:

1. **Clinical unit:** Is pleural effusion presence/absence defensible on the exact proposed frontal-image unit, and what makes a case indeterminate?
2. **Clinical support:** Can qualified readers support independent image/text assessment and intervention validation, with a feasible workload?
3. **Access and environment:** Who will obtain individual credentials, and what university approvals and secure processing arrangements are required?
4. **Feasibility evidence:** Which permitted aggregate counts and review-capacity estimates are needed before freezing the sample size, protocol and experiment budget?

If an existing local collection is considered, the corresponding request is narrowly defined: **linked chest radiographs and original reports, stable patient/study/image structure, documented view/coverage information, and permission plus clinical capacity for independent assessment**. Additional clinical reference tests may be useful, but they cannot replace the exact-image assessment or resolve image ambiguity by definition.

The next research milestone is an evidenced data-readiness decision. The route to the NeurIPS target then depends on reliable measurement, controlled identification, matched comparisons and reproducible held-out evaluation. This note does not authorize downloads, annotation or experiments before the project's remaining execution gates are satisfied.

*Public dataset and access guidance checked on 15 September 2026. NeurIPS 2027 Main Track is the project target; no submission deadline or acceptance outcome is assumed here.*
