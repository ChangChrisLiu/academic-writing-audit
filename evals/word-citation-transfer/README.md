# Word citation transfer checks

Two fresh-context agents independently used `word-citation-audit` on the same three cases. Both identified the incorrect same-author/year displays, counted citations in real footnotes and captions, distinguished unused main-list entries from permitted further reading and stored-only source records, and preserved unresolved matches in a partial export. Their typo-only DOCX edits retained every field and source relationship. A no-citation-skill control reached the same conclusions and produced the same edited file.

These results support the tested decisions and preservation behavior. They do not establish an improvement over the control, cross-model reliability, or native Word refresh behavior for these new cases. No skill change was justified by the observed results; the tested v0.7.2 instructions remain unchanged.

## Design and independence

The run took place on 22 October 2026 against commit `788d2d0ba092c3ec8ed7094105611c4a0d2c5ba5`. The [author request](fixtures/request.md), input files, [criteria](rubric.json), and skill were frozen before execution. Their hashes and historical skill commit are recorded in the [input manifest](fixtures/manifest.json). All run inputs remained unchanged.

Each run received the same materials in an isolated directory, with no parent conversation, memories, expected answers, rubric, or sibling outputs. The two guided runs loaded the skill and its references; the control used general document tooling without citation skills. Native apps and external services were excluded to isolate concurrent trials. This was an offline citation-mapping and editing task, with authenticity explicitly outside scope.

A fourth agent independently assessed the full reports and actual DOCX packages against the frozen criteria. All three runs passed the 21 practical rubric items; these are criteria, not independent experimental samples. It also checked additional findings for unsupported claims or false positives. This assessment was unblinded to the run conditions. The runs shared the configured host, and exact model/version identifiers were not recorded. The study therefore supplies no cross-model comparison. See the [run metadata](run-metadata.json) and [independent assessment](assessment/assessment.md).

## Cases and observed decisions

| Case | Material and requested action | Observed result in both guided runs and the control |
| --- | --- | --- |
| A | [Complete DOCX](fixtures/case-a.docx), audit only. Two distinct Tamsin Vale works from 2024; one incorrect suffix and one missing suffix. A real footnote, a caption citation, figure numbering/cross-reference fields, an uncited main-list entry, permitted further reading, and an embedded unlisted source. | Retained the distinct works and resolved their intended identities from field tags. Proposed correcting the two displayed labels. Counted note/caption citations. Flagged only Marin as an uncited main-list entry. Preserved Sato's permitted recommendation and Lumen's stored-only record. Made no edits or refresh. |
| B | [Complete DOCX](fixtures/case-b.docx) with correct same-author/year labels, note/caption citations, permitted further reading, and a stored-only source. Correct one ordinary prose typo in a paragraph that also contains a citation field. | Found no citation defect under the supplied rules. Changed only `containss` to `contains`. Retained all seven fields, source records, footnote relationships, and caption bookmark. |
| C | [Partial Word text export](fixtures/case-c-excerpt.txt). One ambiguous `Chen (2023)` citation, two candidate works, and a reference absent from the visible paragraph; other document regions and fields unavailable. | Left Chen unresolved without guessing or merging works. Reported Reed only as not found in the inspected portion. Made no global uncited-reference, native-field, active-style, or refresh claim. |

The A/B author instructions specify title-based suffixes and bibliography coverage. They do not prescribe full APA formatting. All runs treated stored APA metadata as configuration evidence rather than proof of an active Word selection, and did not impose unrelated reference-order or typography changes.

The DOCX fixtures contain actual complex field structures, source XML, a footnote part and anchor, and package relationships. Their cached displays were deliberately authored as test inputs, including A's inconsistencies. They are not outputs of a native Word refresh. The [builder](build_fixtures.py) records fixture construction; ZIP timestamps may vary when rebuilding.

## Reports and artifact verification

| Run | Full report | Edited copy | Independent package comparison |
| --- | --- | --- | --- |
| Guided A | [Report](runs/guided-a/output/report.md) | [Revised B](runs/guided-a/output/revised-b.docx) | [Seven checks](verification/guided-a.json) |
| Guided B | [Report](runs/guided-b/output/report.md) | [Revised B](runs/guided-b/output/revised-b.docx) | [Seven checks](verification/guided-b.json) |
| Control | [Report](runs/control/output/report.md) | [Revised B](runs/control/output/revised-b.docx) | [Seven checks](verification/control.json) |

The three revised DOCX files are byte-identical. Each has the same package members as its input; every part other than `word/document.xml` is byte-identical. The document XML contains precisely the requested prose correction. All four `CITATION` fields, the `BIBLIOGRAPHY`, `SEQ Figure`, and `REF figProcess` retain their instructions, results, and complete delimiters. The protected source, footnote, relationship, and bookmark data remain intact. These findings were checked against the actual files, not only the agents' reports.

Each edited document was rendered with the bundled document renderer and LibreOffice, and its full single page was visually inspected. The three page images are also byte-identical. The original two fixture pages were rendered and inspected separately. These checks establish static preservation and readable output; they do not demonstrate native Word regeneration or persistence after a refresh. The earlier [native Word execution test](../word-native-refresh/README.md) remains a separate two-source body/table fixture.

To repeat the static comparison with Python and `lxml`, run this from this directory. It reads the two packages and writes a new JSON result without editing or refreshing the DOCX files.

```sh
python verify_artifacts.py fixtures/case-b.docx runs/guided-a/output/revised-b.docx --output recheck.json
```

The [artifact manifest](manifest.json) hashes the public record. Reports, helper scripts, and renderer logs retain their original conclusions and content, with local paths normalized as disclosed in [publication transformations](publication-transforms.json). Binary DOCX, PDF, and PNG artifacts are unchanged. Per-agent helper scripts are historical execution records with placeholder paths; the portable comparison command above is the supported way to recheck saved outputs.

## Limits

The inputs are small fictional instrument-record and collection-record cases with a supplied author style. Neither literature authenticity nor claim support was tested. The narrow prose edit does not test an actual source-record repair or reference-manager refresh. These trials do not cover grouped citations, tracked changes, text boxes, endnotes, numeric styles, multilingual names, very large documents, or Zotero, EndNote, and Mendeley integrations. All three runs succeeded, so no advantage over general document tooling was measured and no additional skill rules were added.
