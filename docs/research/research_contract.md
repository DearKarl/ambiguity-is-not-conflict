# Research Contract

**Status:** Gate 0 open; protocol design only

**Authority:** DR-0001 through DR-0006

**Last reviewed:** 2026-08-29

## Primary Outcome

The first paper succeeds scientifically if it establishes—or cleanly
falsifies—the separate identifiability of a conditional cross-modal conflict
component under controlled image--report interventions. Publication at a top
venue is the strategic objective, not the scientific endpoint and not a
guaranteed outcome.

The single intended paper contribution is a formal conditional conflict
estimand plus an estimator or estimation framework. The controlled benchmark,
candidate representation families, calibration analysis, and selective review
are evidence supporting or falsifying that contribution, not independent
research routes.

The initial confirmatory endpoint will be a pre-specified, paired measure of
conflict specificity. Its exact formula and smallest effect of interest remain
open Gate 0 decisions. Calibration and selective-review value are downstream
promotion outcomes, not substitutes for construct validity.

## Authoritative Inputs

Only the following may authorize scientific execution:

1. the latest approved documents in `docs/research/`;
2. signed decision records in `decision_log.md`;
3. verified primary literature and official data/model documentation;
4. an approved dataset/access record and clinician-annotation protocol;
5. a bounded task brief issued after Gate 0 closes.

Private email, conversation transcripts, unpublished personal documents, and
informal summaries are context, not executable specifications. The sanitized
[supervisor alignment](supervisor_alignment.md) records the research-relevant
facts.

## Allowed Actions While Gate 0 Is Open

- verify current primary literature and code availability;
- refine definitions, causal contrasts, annotation rubrics, and power plans;
- compare candidate tasks, datasets, estimands, baselines, and venues;
- prepare governance applications and access checklists without accessing data;
- draft task briefs, decision records, and preregistration-style protocols;
- maintain repository structure and documentation checks.

## Forbidden Actions While Gate 0 Is Open

- download, inspect, preprocess, or redistribute restricted medical data;
- generate clinical contradictions or request clinician annotation;
- download models, train adapters, tune thresholds, or run core experiments;
- choose a primary estimator after observing confirmatory outcomes;
- describe planned work as a result or claim clinical value;
- copy personal correspondence, identifiers, credentials, or protected files.

## Gate 0 Closure Requirements

All items must be frozen in a dated decision record:

- exact task and prediction unit;
- primary dataset, version, access route, exclusions, and patient split;
- atomic finding ontology and intervention taxonomy;
- image ambiguity, text ambiguity, conflict, missingness, and corruption
  operations;
- primary conflict estimand and smallest effect of interest;
- primary outcome, confirmatory metric, uncertainty interval, and multiplicity
  plan;
- matched baselines, ablations, frozen backbone, and calibration method;
- development, calibration, and final-evaluation partitions;
- construct-sample versus target-distribution sampling and any prevalence
  weighting;
- compute ceiling, annotation capacity, and clinical-review plan;
- cross-backbone breadth and the governed choice of a second medical dataset or
  small controlled general-domain benchmark testing the same construct;
- promotion, kill, stopping, and fallback criteria;
- permitted artifacts and data-retention boundary.

## Promotion Criteria

The route advances from measurement to outcome-risk modelling only if a
pre-specified candidate:

1. changes in the expected direction under compatibility interventions;
2. is materially less responsive to matched ambiguity and corruption controls;
3. retains a non-negligible conditional association after accounting for
   image ambiguity, text ambiguity, and modality-specific information loss;
4. is stable across repetitions, normalization choices, and one declared
   shift;
5. is not fully subsumed by a matched deterministic predictor;
6. survives the frozen cross-backbone and approved second-dataset or
   general-domain breadth tests, or explicitly limits its claim to the tested
   backbone and intervention population;
7. has reproducible artifacts and reports null and failure cases.

It advances to selective-decision evaluation only after held-out error risk is
adequately calibrated for the tested population.

## Stopping Criteria

Stop or narrow the route when:

- controlled interventions cannot isolate semantic compatibility;
- the signal primarily detects image quality, text length, prevalence, source,
  embedding norm, or synthetic artifacts;
- a simpler deterministic baseline subsumes it under matched evaluation;
- data access, leakage control, or annotation validity cannot be defended;
- calibration fails materially under the pre-specified shift;
- decision value requires information unavailable at decision time;
- the remaining claim is no longer substantial enough for the primary venue.

A null result must be recorded. It does not authorize endpoint switching or an
unplanned portfolio of alternative projects.

## Irreversible and External Boundaries

Supervisor or governance confirmation is required before fixing the clinical
task, claiming access to restricted data, initiating clinician work, changing
the approved research area, or making clinical/deployment claims. No public
release may include restricted data or derivations prohibited by a data-use
agreement. Licensing and anonymized-submission strategy must be decided before
code or artifacts are released for paper review.

## Required Evidence Package

- frozen protocol, dataset card, and intervention manifest;
- code revision, environment lock, model/data versions, configuration, seeds,
  and execution command;
- patient-separated cohort flow and leakage audit;
- pair-level intervention metadata where governance permits;
- paired effects with uncertainty intervals and smallest-effect comparison;
- calibration, selective-risk, subgroup, and shift results when promoted;
- ablations, negative controls, deterministic comparisons, and failure cases;
- deviations from protocol and an explicit permitted-claim statement.

## Current Planning Assumptions

The Commander reports full-time research availability, a strong expectation of
adequate compute, and expected clinical-expert support through the University
of Bristol. These are planning assumptions until budget, access, named roles,
time allocation, and governance approval are documented. No experiment may
silently convert them into facts.
