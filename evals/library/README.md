# Focused-skill development trials

[Library](../../README.md) · [Detailed judgments](scores.md) · [File manifest](manifest.json) · [Original full-audit trials](../README.md)

Run date: 2026-10-14. Ten fictional requests were answered once without a skill and once with the corresponding focused skill. **The controls already handled the core semantic problems correctly. These trials do not demonstrate an improvement from the new skills.**

## Procedure

The cases and rubrics were written before the focused skills. Three fresh control-agent contexts handled the story, evidence, and integrity groups below. Each context answered all cases in its group. They received the case files and were told not to read rubrics, skills, memory, or other project material.

The skill authors inspected those control responses and then wrote the skills. Three new guided-agent contexts received the same groupings, the matching skill entrypoints, and access to their local references. They were told not to read the rubrics, controls, other skills, memory, or author notes. The guided responses were saved without editing.

The lead author read both sets of responses against the semantic rubrics. Assessment was not blinded or independently adjudicated. No exact runtime/model-version identifier was recorded. Cases within a group shared a context, so they are not independent replications. The fixtures influenced development and are not held out. There was no second round of guided trials or tuning on guided failures.

## Cases and observed outputs

“Pass” below means that the complete response meets the supplied semantic criteria in this case. It is not a reliability estimate. The [detailed judgments](scores.md) retain specific evidence and wording qualifications.

| Group | Skill and case | Rubric | Control | Guided | Core judgment |
| --- | --- | --- | --- | --- | --- |
| Story | [scientific-story-audit](cases/scientific-story-audit.md) | [Criteria](rubrics/scientific-story-audit.md) | [Response](results/baseline/scientific-story-audit.md) | [Response](results/guided/scientific-story-audit.md) | Both pass: workflow contribution restored; P1 preserved. |
| Story | [nondefensive-writing](cases/nondefensive-writing.md) | [Criteria](rubrics/nondefensive-writing.md) | [Response](results/baseline/nondefensive-writing.md) | [Response](results/guided/nondefensive-writing.md) | Both pass: assurances removed; endpoint and denominator retained. |
| Story | [related-work-synthesis](cases/related-work-synthesis.md) | [Criteria](rubrics/related-work-synthesis.md) | [Response](results/baseline/related-work-synthesis.md) | [Response](results/guided/related-work-synthesis.md) | Both pass: overlapping axes, prior weighting, and unknowns preserved. |
| Evidence | [claim-evidence-audit](cases/claim-evidence-audit.md) | [Criteria](rubrics/claim-evidence-audit.md) | [Response](results/baseline/claim-evidence-audit.md) | [Response](results/guided/claim-evidence-audit.md) | Both pass: observation retained; attribution, provenance, and transfer bounded. |
| Evidence | [experiment-comparison-audit](cases/experiment-comparison-audit.md) | [Criteria](rubrics/experiment-comparison-audit.md) | [Response](results/baseline/experiment-comparison-audit.md) | [Response](results/guided/experiment-comparison-audit.md) | Both pass: rules, eligibility, budgets, and source removal distinguished. |
| Evidence | [results-interpretation](cases/results-interpretation.md) | [Criteria](rubrics/results-interpretation.md) | [Response](results/baseline/results-interpretation.md) | [Response](results/guided/results-interpretation.md) | Both pass: same-run recovery counts are not an independent ablation. |
| Integrity | [method-definition-audit](cases/method-definition-audit.md) | [Criteria](rubrics/method-definition-audit.md) | [Response](results/baseline/method-definition-audit.md) | [Response](results/guided/method-definition-audit.md) | Both pass: objects, transformation order, and decision levels corrected. |
| Integrity | [figure-caption-audit](cases/figure-caption-audit.md) | [Criteria](rubrics/figure-caption-audit.md) | [Response](results/baseline/figure-caption-audit.md) | [Response](results/guided/figure-caption-audit.md) | Both pass: support sets, arrows, and endpoint repaired in text only. |
| Integrity | [reviewer-comment-triage](cases/reviewer-comment-triage.md) | [Criteria](rubrics/reviewer-comment-triage.md) | [Response](results/baseline/reviewer-comment-triage.md) | [Response](results/guided/reviewer-comment-triage.md) | Both pass: current evidence overrides stale PASS judgments. |
| Integrity | [manuscript-release-check](cases/manuscript-release-check.md) | [Criteria](rubrics/manuscript-release-check.md) | [Response](results/baseline/manuscript-release-check.md) | [Response](results/guided/manuscript-release-check.md) | Both pass: source, build, partial render, draft upload, and submission separated. |

## What these checks establish

They record that these particular responses handled the supplied traps while preserving useful observations and sound text. They provide inspectable regression material for future changes. The guided responses also exercise the requested output boundaries, including no file changes and no claim of image or portal inspection when only text was supplied.

They do not test source retrieval, real citation verification, actual manuscript edits, image perception, compilation, portal operation, cross-client discovery, or behavior across models and disciplines. A correct answer in a deliberately explicit synthetic packet is easier than an audit with missing or contradictory real-world evidence.

The separate [original full-audit record](../README.md) has five controls, five guided responses, and four guided transfer requests. Keep its preservation observation separate from this one-response-per-skill set; pooling them would conceal the different tasks and execution structure.

## Reuse

Use a fresh context for each condition when practical, provide only the intended inputs, retain the full answer, and judge the semantic criteria rather than matching an expected paragraph. Preserve new failures in the record. Run actual file, image, or release workflows separately when those capabilities are the subject of the change.
