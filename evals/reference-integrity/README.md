# Reference-integrity trials

This evaluation covers three new skills for bibliographic authenticity, LaTeX bibliography identity, and Word citation matching. Inputs and a semantic rubric were hashed before the behavioral runs. The two authenticity agents independently received the same three public references, while a separate agent audited fictional LaTeX source and two Word text-export packets. All used fresh contexts without the rubric, other outputs, or parent conclusions.

## Cases and observed scope

| Trial | Inputs | Saved output | Evidence boundary |
| --- | --- | --- | --- |
| Independent authenticity A | [Original reference request](cases/authenticity/request.md) | [Full report](outputs/authenticity-a.md) | Live public-source attempts and supplemental retrievals. Scholar was inaccessible through the browsing tool. |
| Independent authenticity B | The same original reference request | [Full report](outputs/authenticity-b.md) | Separate live retrievals with the same Scholar limitation. |
| LaTeX and Word formats | [Request](cases/formats/request.md), [LaTeX main](cases/formats/main.tex), [appendix](cases/formats/appendix.tex), [database](cases/formats/references.bib), [simulated export](cases/formats/canonical-export.bib), [evidence packet](cases/formats/export-packet.md), [numeric Word export](cases/formats/word-numeric.txt), [author-year Word excerpt](cases/formats/word-author-year.txt) | [Full report](outputs/formats.md) | Fictional records and text exports. No actual Scholar export, compiled LaTeX, native DOCX, live citation fields, or rendered pages. |

Both authenticity reports identified the same erroneous-year duplicate candidate without calling the underlying work fabricated. Both retained the incomplete Scholar status. The [coordinator reconciliation](reconciliation.md) preserves that boundary; agreement between two agents is not evidence that an inaccessible source was inspected.

The format output distinguishes duplicate publications from key collisions, preserves the separately intended preprint and shared-library entry, and checks non-body citations and limited Word coverage. Its proposed changes were not applied. Raw reports are retained without rewriting their conclusions.

## Assessment and reproducibility

The [frozen rubric](rubric.md) has five authenticity criteria scored separately for each agent and eight format criteria. A separate assessor received only the raw inputs, full outputs, and rubric. All 18 criterion applications passed at the report level. The assessor retained a non-failing caveat that omission of a DOI from a Scholar export does not itself establish that an existing DOI is false; any later disposition must be explicit. Actual retrieval histories were not independently authenticated by the assessor. Its [full assessment](assessment.md) and [structured judgments](assessment.json) are preserved. The [input manifest](manifest.json) records the exact tested inputs and skill bytes; [run metadata](run-metadata.json) describes assignment boundaries and the packaging/status follow-ups. A separate [result manifest](results/manifest.json) hashes the completed public records.

These are guided development checks without an unguided control or cross-model comparison. Successful blocked-access reporting does not establish successful end-to-end Scholar verification. The Word tests do not establish native-field editing or document-layout safety, and the LaTeX test does not establish compilation. The public references and fictional fixtures contain no private manuscript or reviewer correspondence.
