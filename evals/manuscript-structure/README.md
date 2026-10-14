# Manuscript structure and concise writing trials

These fictional development cases exercise research understanding, section logic, connected literature synthesis, discipline-specific interpretation, and source-format delivery. They do not use or publish private manuscript or reviewer text.

## Design

Three fresh-context agents received their complete request, a frozen standalone skill or the two skills explicitly assigned to separate tasks, and local references. They were instructed not to read the rubric, other cases, prior outputs, parent conclusions, memory, or the network. These are task restrictions, not a claim of a complete filesystem sandbox or independently reconstructed tool trace.

| Case | Requested work | Skills exercised |
| --- | --- | --- |
| [Engineering](cases/engineering/request.md) | A compact seven-section LaTeX draft about greenhouse interruption estimation. | research-manuscript-writing |
| [Qualitative research](cases/qualitative/request.md) | Paste-ready Word prose about archival classification, with a combined Findings and Discussion section and a countercase. | research-manuscript-writing |
| [Mathematics](cases/mathematics/request.md) | A literature review about contraction and perturbation, followed by an independent title-only request for an unsupported abstract. | related-work-synthesis and scientific-story-audit |

The packets, skills, and [rubric](rubric.md) were frozen before execution. Supplied literature cards and measurements are fictional test facts, not independently verified publications or scientific results. The initial tested skill snapshots are preserved under [tested-skills/initial](tested-skills/initial). Entrypoint snapshots use SKILL.snapshot.md so clients do not discover duplicate installed skills; their bytes are unchanged. Complete generated outputs and execution notes are preserved in each case directory without rewriting.

A separate fresh-context assessor read the full requests and delivered artifacts against the rubric, without the skills or parent judgments. It distinguished scientific errors, material structural defects, unresolved sources, and optional editorial preferences. Source-format inspection is separate from any claim about compilation or rendered layout.

## Initial assessment

The independent assessor marked 16 applicable judgments pass, two dimensions not applicable, and none qualified or failed. All three requests were fulfilled without material or harmful findings. The mathematics case does not request Methods or an evidence-supported abstract, so those section dimensions are not scored as if the sections had been drafted.

One optional wording issue remains recorded. The engineering conclusion refers to the supplied laboratory evaluation, which reflects the writing packet rather than manuscript-reader context. Removing that adjective would improve reader-facing phrasing. The original output is preserved unchanged.

[Full independent assessment](assessment.md) and [structured judgments](assessment.json) include exact source and output anchors. The primary editor's stricter narrative preference below is separate from that assessor's passing literature judgment; it is not presented as an independently confirmed scientific error.

## Observed refinement and regression design

The primary editor found that the initial engineering review repeatedly ended paragraphs by explaining what prior studies had not established for the present task. Although it did not say our method is better, this still organized the review around the present paper's gap. The rules now ask writers to explain prior contributions in their own settings and reserve limitations for those needed to interpret the prior finding itself. Source-coverage notes can stay outside the manuscript passage when they do not affect its scientific meaning.

Two new fresh-context agents repeated the engineering and mathematics requests with the revised skills. They received the same request bytes and no initial outputs or findings. The mathematical case checks that the refinement does not erase necessary assumptions or the difference between an error bound and vanishing error. No other skill changes are introduced during these runs.

## Regression assessment

A second independent fresh-context assessor marked 10 applicable dimension judgments pass and two not applicable, with no qualified or failed judgments and no material or harmful issue. The engineering review explains acquisition and integration studies within their own settings. The mathematical review retains the assumptions and distinctions needed to interpret contraction and error bounds, without using those boundaries to advertise a gap for the present paper. The separate title-only request still does not produce a fabricated abstract.

One optional concision preference remains. The engineering Method repeats a shared-records/shared-episodes statement in its closing sentence. The assessor suggested removing that local restatement but did not classify it as a failure. Neither output nor assessment was rewritten to remove this caveat. [Full regression assessment](regression/assessment.md) and [structured judgments](regression/assessment.json) preserve the evidence and limits.

These observations do not establish that the rule refinement caused a change. Three skill entrypoints were exercised behaviorally; structural and installation checks cover all 14 skills. The initial and regression assessors did not inspect each other's findings.

## Limits

These are short fictional drafts and excerpts, not full-length research manuscripts, unseen external benchmarks, or cross-model comparisons. All agents use the same configured host without an explicit model override; exact model versions were not recorded. There are no unguided controls, repeated-sampling estimates, or causal effectiveness estimates.

The format checks concern LaTeX source and paste-ready Word text. No LaTeX compilation, rendered page inspection, native .docx creation, or preservation test on live citation-manager fields was performed. The library describes these document requirements, but this run does not certify them. Missing research facts must remain missing rather than become fabricated prose.

## Records

[Initial input freeze](design-freeze.json) · [Regression input freeze](regression-design-freeze.json) · [Run metadata](run-metadata.json) · [File and skill hashes](manifest.json)

Raw execution notes and occasional raw-output links retain transient run paths. They record execution context rather than portable installation locations.
