# Annotation and Intervention Protocol

**Status:** Gate-0 freeze candidate; no annotation or clinical editing is
authorized

**Date:** 2026-08-29
**Evidence class:** Protocol

## Purpose

This protocol prevents the labels used to validate conflict from being
defined by the paired report, a candidate model, or the intervention name. It
separates four questions:

1. what an exact image independently supports;
2. what an atomic text independently asserts;
3. whether either input is genuinely underdeterminate;
4. whether two determinate semantic states are compatible.

Pleural-effusion presence/absence and MIMIC-CXR/JPG are planning candidates,
not approved clinical or data decisions.

## Unit and Independent Label Spaces

### Image-only record

The reader sees one exact frontal radiograph, the frozen singleton finding,
and no report, paired text, model output, intervention condition, or source
label. The following fields are recorded separately:

| Field | Values | Construct |
| --- | --- | --- |
| Technical integrity | `intact/fully gradable`, `protocol-defined loss but interpretable`, `task-critical loss/non-gradable` | Image information-loss exposure/severity, `M_v` |
| Prescribed input coverage | `complete prescribed field`, `task-critical field/additional view missing`, `not assessable` | Input completeness, separate from semantic ambiguity |
| Finding state | `present`, `absent`, `undefined` | Image-side semantic state, `Y_v` |
| Evidential ambiguity | `determinate`, `genuinely ambiguous`, `not assessable` | Image ambiguity, `A_v` |
| Probability | Integer 0--100 for presence, or structurally missing | Elicited image-only interpretation distribution |
| Reason code | overlap/subtlety; competing explanation; insufficient field; quality loss; additional view needed; other | Audit; never used to collapse constructs |

`Genuinely ambiguous` means the intact, protocol-complete image evidence
supports materially different task-relevant interpretations. It is not a
synonym for low confidence, poor quality, missing view, reader unfamiliarity,
or disagreement between readers. The fact that additional evidence could
resolve an otherwise complete ambiguous item does not itself make that item
information loss. Conversely, uncertainty attributable to a missing field,
view, or technical degradation is `M_v`, not `A_v`.

The image schema is constrained in this order:

1. If technical integrity is `task-critical loss/non-gradable`, or prescribed
   input coverage is not `complete prescribed field`, record critical `M_v`,
   set `Y_v=undefined`, `A_v=not assessable`, and leave the probability
   structurally missing.
2. `Protocol-defined loss but interpretable` records an `M_v` exposure but may
   retain `Y_v` only when readers still assign a unique determinate state under
   the frozen acceptance rule. Then `A_v=determinate`; if the loss prevents a
   unique state, classify it as task-critical loss and set `A_v=not assessable`.
   A degraded item cannot be promoted to natural `A_v` merely because readers
   disagree.
3. Only an intact/fully gradable item with complete prescribed coverage may be
   labelled `A_v=genuinely ambiguous`; then set `Y_v=undefined` and retain the
   probability distribution. A best guess does not make the semantic state
   determinate.
4. If `A_v=determinate`, `Y_v` must be exactly `present` or `absent`.
   `Y_v=undefined` with `A_v=determinate` is invalid.
5. A determinate `present` rating requires presence probability at least 50;
   a determinate `absent` rating requires probability at most 50. An
   inconsistent categorical/probability record is an instrument error, not a
   disagreement to be repaired after review. An unassessable rating retains a
   structurally missing probability.

Thus `M_v` exposure is not a synonym for semantic indeterminacy: a frozen,
semantics-preserving degradation may retain a determinate state, whereas
task-critical loss cannot.

### Text-only record

The reader sees one atomic assertion and the frozen finding definition, but no
image, original report, model output, intervention name, or paired variant.

| Field | Values | Construct |
| --- | --- | --- |
| Input integrity/completeness | `intact/complete`, `protocol-defined corruption with fully recoverable proposition`, `task-critical truncated/corrupt/missing content`, `no proposition` | Text information-loss exposure/severity, `M_t` |
| Target polarity | `positive`, `negative`, `no target`, `not assessable` | Direction of the proposition, separate from commitment; `no target` requires verified absence of a proposition |
| Commitment strength | `definite`, `possible`, `probable`, `cannot exclude`, `other qualified`, `not assessable` | Epistemic form, not linguistic ambiguity |
| Linguistic ambiguity | `unique reading`, `at least two clinically reasonable polarity readings`, `not assessable` | Text ambiguity, `A_t` |
| Derived semantic state | `present`, `absent`, `undefined` | Text-side semantic state, `Y_t` |
| Probability | Integer 0--100 that the assertion commits to presence, or structurally missing | Elicited text-only interpretation distribution |
| Form audit | fluent; grammatical; template; length; punctuation; hedge; negation; provenance | Artifact controls only |

An explicit clinical hedge expresses epistemic qualification; it does not by
itself create two linguistic readings and therefore does not establish
`A_t`. Truncation or deletion remains `M_t`. A sentence that merely lacks any
mention contains no proposition and is not a negative assertion.

The text schema is constrained in this order:

1. If text has task-critical truncation/corruption/missing content, set
   critical `M_t`, `Y_t=undefined`, `A_t=not assessable`, and do not infer
   polarity: set target polarity to `not assessable`, commitment and probability
   structurally missing/not assessable. If there is verified no proposition,
   record target polarity `no target`, missingness, `Y_t=undefined`,
   `A_t=not assessable`, and a structurally missing probability.
2. A protocol-defined corruption with a fully recoverable proposition records
   an `M_t` exposure but may retain `Y_t` only when every acceptance reader
   recovers the same complete, unique, definite proposition; then
   `A_t=unique reading`. Otherwise it is task-critical loss. Such corruption
   cannot be relabelled natural linguistic ambiguity.
3. Only intact/complete wording may receive a genuine ambiguity label. At
   least two clinically reasonable polarity readings imply text ambiguity and
   `Y_t=undefined`.
4. For intact/complete wording with a unique reading, record positive/negative target
   polarity separately from commitment strength. Only `definite positive`
   derives `Y_t=present`, and only `definite negative` derives `Y_t=absent`.
   Every uncertainty-qualified commitment derives `Y_t=undefined` while
   remaining linguistically unique, not ambiguous.
5. `Y_t=undefined` is therefore compatible with a unique reading only when the
   recorded reason is explicit epistemic qualification; it never enters a
   determinate compatibility cell.

Thus `M_t` exposure is not a synonym for semantic indeterminacy. Recoverable,
semantics-preserving corruption and task-critical information loss occupy
different schema states.

### Derived compatibility record

Compatibility is derived only after independent labels are locked:

```text
if Y_v and Y_t are both determinate and have the same polarity: compatible
if Y_v and Y_t are both determinate and have opposite polarity: conflict
otherwise: C* undefined
```

An undefined conflict label is never recoded as compatible, non-conflicting,
negative, or incorrect. Cross-modal reviewers can only accept or reject a pair;
they can never alter locked unimodal ratings. If paired review exposes a
possible modality-label error, invalidate the pair and send that modality to a
fresh, same-modality panel blinded to the other modality and prior labels under
a new record.

## Reader Roles and Blinding

- **Clinical protocol owner:** approves the finding definition, eligibility
  rules, edge cases, qualifications, workload, and safety/governance route.
- **Image readers:** strongest candidate plan is five independent qualified
  chest-radiograph readers for the locked reliability and final construct
  sets; a three-reader screen may reduce workload but cannot alone establish
  the status of a putatively ambiguous item. Exact credentials and whether
  thoracic subspecialty is required remain approval items.
- **Text readers:** candidate roster is at least six medically qualified readers
  familiar with radiology language, plus a non-voting clinical-language
  reviewer. Opposite-polarity siblings receive disjoint three-reader panels and
  require unanimity; natural-ambiguity items receive five ratings where
  feasible. A smaller or repeat-reader design requires an amended dependency
  model and workload/reliability calculation.
- **Cross-modal panel:** candidate roster is at least six senior clinical
  readers, assigned as disjoint unanimous three-person panels to opposite-
  polarity siblings. They accept/reject intervention validity only.
- **Adjudicator:** reviews one modality at a time after independent labels are
  locked, is blinded to the paired modality, condition, provenance, prior
  reader identity, and model scores, and retains every raw rating.
- **Data/statistical steward:** generates blinded randomized presentation
  order, maintains source-group keys inside the approved environment, and
  computes reliability without revealing intervention outcomes to readers.

No unimodal reader labels both modalities of the same source/pair. Variant
siblings are not shown to the same reader: image interventions require
disjoint five-reader panels for original and altered siblings, and text/cross-
modal siblings use the disjoint panels above. This implies a minimum ten-person
image-reader roster whenever two image siblings require five ratings each.
Template, polarity, source, condition, and presentation order are
counterbalanced. A candidate 15% of units are blindly repeated after a frozen
washout to estimate intra-reader stability; the fraction and washout require
budget approval. Any washout-based reuse in place of disjoint panels requires
an amended reader-dependence model and new precision/workload calculation.

## Intervention Taxonomy

| Family | Candidate operation | Identified role | Non-equivalence rule |
| --- | --- | --- | --- |
| Determinate compatibility | Hold one independently clear image fixed; pair matched atomic assertions with same versus opposite polarity | Primary within-source `tau_C` | Both assertion versions must remain determinate, fluent, length/template matched, and independently verified. |
| Semantic-preserving text form | Paraphrase, negation template, punctuation, or length-matched rewrite without polarity change | Surface-artifact control | Any semantic-state change invalidates the control. |
| Explicit text uncertainty | Randomized clinically valid modal/hedged wording whose independent readers classify commitment as uncertainty-qualified | Epistemic-form control, not automatically `A_t` | A hedge does not establish multiple readings; deletion, truncation, or no mention is `M_t`. |
| Image information loss | Pre-specified quality change only when changed information is mechanically specified, the finding state remains determinate, and a separate model-independent reader endpoint demonstrates non-trivial task-evidence attenuation | `M_v` negative control | It must never be named image ambiguity merely because confidence falls; discarded pixels alone do not establish task relevance. |
| Text information loss | Pre-specified truncation or missing critical clause | `M_t` negative control | A well-formed hedge is not truncation. |
| Natural ambiguity | Independently identified gradable images or complete texts with at least two clinically reasonable interpretations | Conservative `gamma_A` falsification audit | Matching/weighting does not make this randomized and cannot establish causal separation. |
| Unrelated finding | Change an out-of-task proposition while preserving the target assertion | Semantic-specificity control | Must not alter target-finding entailment. |
| Missing modality/assertion | Remove or replace the task assertion with an explicit missing token under a matched interface | Missingness control | Missing is not contradictory. |

No valid image- or text-ambiguity intervention is declared by this protocol.
Evidence removal is information loss; adding pathology changes truth;
compositing can introduce artifacts; hedging changes epistemic commitment; and
selecting a naturally subtle/ambiguous case is observational. A future
candidate must pass clinical review and demonstrate that it changes
task-relevant interpretive multiplicity while holding information
completeness, technical gradability, truth, source, and nuisance features within
the frozen tolerances.

## Candidate Qualification and Reliability Gate

The numerical values below are **planning candidates requiring approval**, not
validated universal cutoffs.

1. Create a training/qualification set with frozen examples and edge cases;
   it cannot enter reliability estimation or scientific analysis.
2. Run one pilot of 60 independent source units, deliberately spanning the
   label space. A single rubric clarification and reader requalification is
   allowed before the reliability set is opened.
3. Evaluate the locked rubric on a disjoint 150-unit reliability set, with
   five independent image ratings, five independent ratings for natural text
   items, and disjoint unanimous three-reader panels for opposite-polarity text
   siblings, with patient/source clustering retained. The exact marginal
   allocation, repeat selection, and pre-reader precision simulation are the
   unapproved `G0-READERS A` candidate in the [reader measurement and MV-1
   qualification audit](reader_measurement_and_mv1_qualification_audit.md).
4. For every categorical gating axis, the recommended primary coefficient is
   nominal Krippendorff alpha with the audit's exact patient/source-cluster
   bootstrap interval. Ordinal alpha and Gwet AC1/AC2 are sensitivities.
   Report category prevalence, the audit-defined macro and class-specific
   exact agreement, pairwise confusion, intra-reader agreement, adjudication,
   and missingness. For 0--100 probabilities, additionally report within-unit
   dispersion and calibration against the independently locked determinate
   polarity only as a reader-behaviour diagnostic. This package is not approved
   and cannot be replaced after results.
5. Candidate promotion requires the primary coefficient at least 0.80, lower
   95% bound at least 0.67, observed agreement at least 0.85, and class-specific
   positive agreement at least 0.75 for every gating axis: technical integrity/
   input coverage, determinate-versus-ambiguous, polarity, and text integrity/
   ambiguity.
   These are conservative protocol choices, not a theorem that the construct
   is valid.
6. If the disjoint reliability gate fails, do not repeatedly revise against
   it. Stop the proposed task or collect a newly authorized qualification and
   reliability sample under an amended decision record.

Rare categories with too few observations make alpha unstable. They must not
be pooled after seeing results. The pre-access feasibility record must define
minimum counts per required category; failure leaves that contrast
unidentified.

Eligibility rules are mutually exclusive and apply in this order:

1. Any item meeting a **task-critical** information-loss or missingness rule is
   ineligible for `A_v/A_t` and binary `C*`; no ambiguity vote can override it.
   A protocol-defined interpretable/recoverable loss may retain a determinate
   state only under its stricter condition-specific acceptance gate.
2. A clear source image requires at least four of five readers to agree on
   `intact/fully gradable`, `complete prescribed field`, `A_v=determinate`,
   and the same present/absent state, with no more than one reader flagging
   ambiguity or task-critical loss.
3. A natural image-ambiguity item requires at least four of five readers to
   agree on `intact/fully gradable`, `complete prescribed field`, and
   `A_v=genuinely ambiguous`; its `Y_v` remains undefined.
4. Clear opposite-polarity text variants require intact/complete wording, unique
   reading, definite commitment, and the intended polarity from every member
   of each disjoint three-reader panel. A natural text-ambiguity item requires
   at least four of five readers to identify intact/complete wording with multiple
   clinically reasonable polarity readings; its `Y_t` remains undefined.
5. If an item satisfies competing consensus rules or none, mark it
   `unresolved`; never choose the more convenient arm. For determinate
   compatible/conflict pairs, three-of-three cross-modal reviewers must agree
   on atomicity, plausibility, fluency, and absence of nonsemantic cues.
   Information-loss arms use the condition-specific gate below.

Raw ratings are retained as the modality-specific interpretation distribution.
A pre-specified hierarchical multinomial/ordinal reader model may estimate
item distributions while accounting for reader severity, discrimination, and
repeat noise. A single-latent-truth aggregation such as unqualified majority
vote or Dawid--Skene alone cannot define genuine ambiguity because reader error
and item underdetermination are different explanations for disagreement.

## Intervention Acceptance and Artifact Gate

Each intended variant uses a condition-specific acceptance gate:

- Compatible, conflicting, and clear reference variants require the intended
  definite polarity, complete/unique/fluent wording, a clear image state, and
  preservation of every non-target semantic field.
- An `M_t` variant must meet its one frozen operation, severity, and reference
  rule and introduce no contrary proposition. A recoverable corruption must
  preserve the same unique, definite `Y_t` and `A_t=unique reading`; a task-
  critical loss has `Y_t=undefined`, `A_t=not assessable`, and need not be
  fluent. The two states cannot be pooled after outcomes are inspected.
- An `M_v` variant must meet its one frozen operation, severity, retained-field,
  and reference rule and add no contrary evidence. An interpretable loss must
  preserve the same determinate `Y_v`; a task-critical loss has
  `Y_v=undefined` and `A_v=not assessable`. Neither state can be relabelled
  natural ambiguity or pooled post hoc.
- A semantic-preserving surface variant must retain complete, definite semantic
  state while satisfying its matched form constraints. A missing variant must
  be classified as no proposition, not negative or ambiguous.
- Cross-modal reviewers verify only the intended manipulation and non-target
  preservation under the applicable gate; they do not impose determinate
  polarity, completeness, or fluency on an information-loss control.
- For every condition, source image, proposition, and siblings remain in one
  patient/source partition; protected or unsupported clinical content is not
  introduced; length, template, punctuation, fluency, negation, rendering,
  source, and provenance are recorded; exact/near duplicates and cross-
  partition templates are audited.
- The frozen modality/nuisance probe family governs condition recoverability.

Only the proposed Month-3 **cardinality and modality roles** are currently
fixed: one `M_v` contrast and one `M_t` contrast. TB-0005 now supplies one
finite recommended identity for each in the
[intervention option audit](intervention_option_audit.md): `MV-1` is exact
antialiased `224 -> 112 -> 224` resolution attenuation retained only when the
same determinate image polarity survives **and** a model-independent
qualification set disjoint from reader training/reliability and every model or
protected/target population yields a patient-clustered one-sided 95% lower bound
strictly above `0.10` for
`q_v,bal = 0.5(q_v,present+q_v,absent)`, with simultaneous one-sided lower
bounds for both polarity-specific terms strictly above zero. Each term is
`E_R[h_intact-h_MV-1 | S=1,E=1,Y_v]` for the locked finite roster, with
`h_s=a_y(pbar_s-0.5)>=0`, `a_y=+1` for present, and `a_y=-1` for absent;
each polarity has at least 108
evaluable independent blocks. The `G0-MV-Q A` candidate reserves 150
metadata-screened cases per report-screen stratum (300 total), uses a locked
finite ten-reader roster with cyclic disjoint panels, and conditions its claim
on the selected/evaluable population; `MT-1` redacts the sole
text polarity slot and is accepted only as task-critical target-state loss
with `Y_t=undefined`. Their exact operations, estimand, joint max-`t` interval,
polarity guardrails, panel schedule, yield arithmetic, simulation contract, and
approximately 129-hour planning row are specified in the [reader measurement
and MV-1 qualification audit](reader_measurement_and_mv1_qualification_audit.md).
They remain statistical, clinical, reader-dependence, attrition, governance,
and resource approval blockers. Approving the rule does not pass the later
qualification gate. Gate 0 cannot close until a dated owner decision accepts
the protocol, and `J_id` cannot be called executable until the later authorized
`MV-1` qualification passes. Full-
modality missingness and every alternate degradation/corruption remain
diagnostics or rejected options as recorded; outcomes may never choose among
them.

The recommended artifact option first enforces exact image/text/template/
process balance from the construction manifest, then uses the frozen four-
probe modality/nuisance family as a diagnostic veto. Orientation-safe
recoverability is `R=max(BA,1-BA)`: sub-chance balanced accuracy cannot pass by
sign error. A lower bound for any `R` above `0.55` kills the instrument; an
upper bound strictly below `0.55` supports only the exact bounded-probe claim; an
interval crossing it is inconclusive. At the present sample ceilings, no weak
or non-significant result may be called artifact equivalence or artifact
survival. The design invariants, optional powered conjunction, and feasibility
burden are defined in the
[statistical analysis plan](statistical_analysis_plan.md) and remain an open
owner choice in the [decision dossier](gate0_decision_dossier.md).

## Governance and Stop Rules

No reader is contacted and no example is shown until dataset access, ethics,
data handling, compensation, withdrawal, and permitted-output decisions are
approved. Raw images, reports, identifiers, row-level labels, counterfactual
text, and reader comments remain in the approved environment. Only explicitly
permitted aggregate reliability and audit outputs may leave after disclosure
review.

Stop or narrow the route when:

- technical integrity/input coverage cannot be judged reliably, or the
  determinate-source pool cannot support a unique image-only state; intact
  natural-ambiguity items may retain `Y_v=undefined`;
- ambiguity cannot be separated from quality loss under the locked rubric;
- determinate polarity or atomic text commitment fails the reliability gate;
- an intervention changes more than the intended semantic axis;
- surface form or either modality alone reveals the condition;
- an ambiguous or missing case would need to be assigned a fake conflict
  label;
- valid ambiguity identification remains unavailable and the intended claim
  is not narrowed.

## Permitted Claim

This document supplies a blinded annotation and intervention freeze candidate.
It does not demonstrate reader reliability, intervention validity, clinical
truth, causal ambiguity separation, data availability, clinical benefit, or
authorization to annotate.

## Methodological Anchors

- The [GRRAS reporting guideline](https://www.equator-network.org/reporting-guidelines/guidelines-for-reporting-reliability-and-agreement-studies-grras-were-proposed/)
  motivates explicit reporting of sampling, readers, design, and both
  inter- and intra-rater agreement.
- The [VinDr-CXR dataset paper](https://www.nature.com/articles/s41597-022-01498-w)
  supplies precedent for multi-radiologist chest-radiograph annotation, but
  does not validate this project's instrument or thresholds.
- Dawid and Skene's
  [observer-error model](https://doi.org/10.2307/2346806) is a useful reader-
  error reference but does not by itself distinguish genuine item ambiguity
  from disagreement around a single latent truth.
