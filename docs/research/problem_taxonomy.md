# Problem and Outcome Taxonomy

**Status:** Canonical terminology protocol

Each experiment must name the object it manipulates, measures, predicts, or
uses for a decision. The word *uncertainty* is not sufficient by itself.

## Input and Representation Objects

| Term | Operational meaning | Not sufficient evidence of |
| --- | --- | --- |
| Image ambiguity | More than one task-relevant interpretation is plausible from the visual evidence | Cross-modal conflict or epistemic uncertainty |
| Text ambiguity | More than one task-relevant interpretation is plausible from the wording | Cross-modal conflict or model ignorance |
| Information loss | Evidence is missing, occluded, truncated, corrupted, or otherwise unavailable | A contrary semantic proposition |
| Cross-modal conflict | Image and text provide conditionally incompatible evidence about the same task-relevant proposition | Output hallucination by itself |
| Modality gap | A systematic representation or behaviour difference between modalities | Semantic contradiction in an individual pair |
| Epistemic uncertainty | Uncertainty attributable to limited model knowledge or parameter uncertainty | Input ambiguity estimated by a data-dependent variance head |
| Output semantic uncertainty | Variation in meaning across plausible generated outputs | The input source that caused the variation |

## Outcome Objects

| Term | Operational meaning |
| --- | --- |
| Task error | The output is wrong under the frozen task definition |
| Unsupported claim | An output claim is not supported by available evidence |
| Contradictory claim | An output claim conflicts with available evidence |
| Hallucination | A specific unsupported, contradictory, or fabricated output under a stated annotation protocol |
| Calibration failure | Predicted probabilities do not match observed frequencies under the evaluation design |
| Overconfident error | An incorrect output receives confidence above a pre-specified threshold |
| Selective risk | Residual error among cases on which the system chooses to answer |

Cross-modal conflict is an input relationship; hallucination is an output
failure. Either may occur without the other.

## Decision Objects

Candidate actions are:

```text
answer | clarify | verify | abstain | human_review
```

Retrieval or regeneration may later be added only if the frozen task supplies
new decision-time information. An action is justified by expected loss or a
pre-specified risk-control rule, not by a raw score alone. Review budget, delay,
false reassurance, unnecessary escalation, and missed consequential errors
must be represented explicitly.

## Required Labels in Evidence Records

Every result must state:

1. prediction unit and leakage unit;
2. manipulated condition and source provenance;
3. measured signal, units, and normalization;
4. outcome label and annotation source;
5. decision rule and information available at decision time;
6. evidence status and permitted claim.
