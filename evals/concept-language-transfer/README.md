# Concept and language transfer trials

Four fictional cases were executed in fresh agent contexts on 2026-10-14 after the core terminology guidance was generalized. The instructions now distinguish a conceptual error, awkward expression of a valid concept, unresolved meaning, and correct prose. The earlier dataset/buffer issue is one reference example rather than a core word-specific rule.

## Cases and saved outputs

| Domain and task | Standalone skill | Complete output | Terms and distinctions examined |
| --- | --- | --- | --- |
| [Mathematical exposition](cases/mathematics.md) | academic-prose-editing | [Answer](results/mathematics/answer.md) and [execution record](results/mathematics/execution.txt) | Null set versus empty set, almost everywhere versus everywhere, essential versus ordinary supremum, and an author-defined exception mass. |
| [Spectroscopy passage and caption](cases/chemistry.md) | academic-prose-editing | [Answer](results/chemistry/answer.md) and [execution record](results/chemistry/execution.txt) | Bathochromic shift, chemical buffer, absorption wavelength versus quantum yield, and a defined spectral-persistence measure. |
| [Chinese economics audit](cases/economics.md) | academic-writing-audit | [Answer](results/economics/answer.md) and [execution record](results/economics/execution.txt) | Semi-elasticity versus elasticity, relative percentage versus percentage points, fixed effects, endogeneity, and a defined exposure measure. |
| [Qualitative research source edit](cases/qualitative-research.md) | academic-writing-audit | [Manuscript](results/qualitative-research/manuscript.md), [notes](results/qualitative-research/answer.md), and [execution record](results/qualitative-research/execution.txt) | Thick description, emic meanings, an author-defined quiet-agency category, participant accounts versus national prevalence, and an exact quotation. |

## Design and verification

The [rubric](rubric.md), requests, and skill inputs were fixed before writer execution. [design-freeze.json](design-freeze.json) records their hashes. Each writer received only one request and its frozen standalone skill with relevant references, plus an initial manuscript when actual editing was requested. The writers did not receive the rubric, other outputs, or earlier editorial judgments.

A separate fresh-context assessor received all four requests, complete outputs, execution records, and the rubric. It did not receive the skills or the primary agent's conclusions. The [run metadata](run-metadata.json) records task identities, resource restrictions, and runtime limits. Saved outputs are unedited.

The primary agent also performed [exact-text checks](mechanical-checks.json). The correct opening passages in mathematics and chemistry, the spectroscopy caption, and the first two qualitative paragraphs including the quotation match the supplied source verbatim. Economics was an audit-only task, so its keep decisions require semantic assessment rather than comparison with a rewritten source.

## Independent assessment

The separate assessor marked all 24 judgments as pass across the six prespecified dimensions in each case. It found no unjustified change to a valid specialist term, an author-defined concept, or a correct passage. Substantive corrections were supported by the supplied facts. Unresolved constructs remained author questions outside manuscript prose. The [full assessment](assessments/assessment.md) and [structured judgments](assessments/assessment.json) preserve the assessor's complete, unedited findings.

The assessor identified optional presentation preferences, including possible concision improvements, but no rubric-level defect requiring a further instruction change. This is an observed result for these four outputs, not a guarantee of future behavior.

The assessor's evidence paths use its isolated input layout. A path of the form `<domain>/request.md` maps to `cases/<domain>.md` here. Other `<domain>/<filename>` paths map to `results/<domain>/<filename>`. The rubric is unchanged, and all 14 recorded input hashes match those published files. [manifest.json](manifest.json) records hashes for this trial package.

## Interpretation limits

These are four guided development cases on one configured host, not four different models. There is no unguided control, repeated sampling, causal estimate of improvement, or independently designed benchmark. The cases were written in the same development session as the instructions and provide definitions as factual ground truth. They test application and preservation within that supplied context, not independent mastery of every discipline.

Two skill entrypoints were exercised behaviorally. All 13 packages receive structural and installation checks, which do not establish their editorial effectiveness. The outputs do not establish behavior on a full real manuscript, unfamiliar terms without adequate evidence, all audiences or venues, conflicting sources, or future runs. Execution records are self-reports and do not independently reconstruct every tool call. No external research validation, manuscript rendering, submission, or authorship detection was performed.

Earlier trial records remain associated with the versions they actually tested. A lack of harmful edits in these cases supports only the observed sample and is not a guarantee that a future agent will never alter a valid term.
