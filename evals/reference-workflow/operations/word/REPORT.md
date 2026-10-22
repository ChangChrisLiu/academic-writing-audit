# Native Word citation field operational probe

**Result: package inspection and layout checks completed; native Word opening and citation refresh remain unconfirmed.** The UI route timed out before the fixture could be selected. This is a constructed operational probe of the citation-audit workflow, not a blinded agent efficacy test or evidence of successful Word refresh.

## Fixture and scope

The fixture contains two explicitly fictional book sources embedded in the native Office bibliography XML, two complex `CITATION` fields, and one complex `BIBLIOGRAPHY` field. The body cites `Orchid2024`; a table cell cites `Vale2025`. Every field has begin, instruction, separator, cached-result, and end elements. Its initial result caches are conspicuous pending-refresh markers. They were never replaced with invented refreshed results.

The test requests APA and stores `SelectedStyle="/APA.XSL"`, `StyleName="APA"`, and `Version="6"` in the source XML. These are fixture configuration values. The running Word style and its actual edition were not confirmed; the XML version value alone is not asserted to prove APA sixth edition.

All Word XML parts in the package were scanned, including nested table paragraphs. The fixture has no tracked insertions or deletions and no footnotes, endnotes, text boxes, or appendices. These regions were deliberately absent, so the probe does not test their coverage.

## Mapping and preservation results

| Region | Field target | Embedded source | Before and final working-file display |
| --- | --- | --- | --- |
| Body paragraph | `Orchid2024` | Ada Orchid. 2024. *The Imaginary Copper Orchard*. Fictional Methods Press. | `[BODY CITATION AWAITING WORD REFRESH]` |
| Table cell | `Vale2025` | Bram Vale. 2025. *The Invented Paper Observatory*. Fictional Methods Press. | `[TABLE CITATION AWAITING WORD REFRESH]` |
| Bibliography | `BIBLIOGRAPHY` | Two source records available | `[BIBLIOGRAPHY AWAITING WORD REFRESH]` |

Both citation tags resolve uniquely to an embedded source, and each source has one observed citation occurrence. There are no missing structural targets, duplicate source identities, or source records without an observed occurrence in this fixture. The bibliography has no generated displayed entries yet. Therefore this is a source-to-field relationship check, not a completed displayed-reference-list audit.

The preserved `before.docx` and `after-attempt.docx` are byte-identical. Their source tags, GUIDs, authors, years, titles, source types, publisher/city metadata, field instructions, closure structure, and cached results match. **`after-attempt.docx` is an unchanged working-file snapshot, not a Word-saved or refreshed output.** The final fixture's inherited title rule was removed and its caption made black during authoring after the blocked UI attempt; no source, field instruction, or initial result cache was changed by that layout refinement.

## Native UI execution

1. Microsoft Word was selected through the normal native UI tool. Its start window was observable.
2. The command to open a document (`Cmd+O`) and inspect the resulting UI timed out at 30 seconds. The fixture path had not been entered.
3. A subsequent attempt to inspect Word timed out at 60 seconds and reset the tool session.
4. One bounded recovery check returned `Computer Use server error -10005: timeoutReached` after approximately 17 seconds.

No fixture opening, refresh, source-manager edit, save, or native screenshot was confirmed. The blocker is an unresponsive UI route; this evidence does not identify its underlying application or accessibility cause. No license was accepted, no account was signed into, no app-wide setting was changed, and the Word process was not terminated. No other document was opened or edited.

## Render check

The packaged `render_docx.py` renderer from runtime bundle `26.1013.11914`, using its bundled headless `soffice`, produced a one-page PDF and PNG. Renderer temporary files were confined to the probe directory through a thin wrapper; rendering logic and bundled binary selection were unchanged. The final page was visually inspected: the title, body, caption, table, and bibliography marker are readable, with no clipping or overlap. All three pending-refresh markers remain visible. The renderer did not mutate the input DOCX.

The PNG/PDF prove that the fixture can be rendered by that other office engine. They do not prove that Word accepted or refreshed the native citation fields. Since the two preserved DOCX files are byte-identical, a second render of the unchanged snapshot was unnecessary.

## Evidence and limits

- `build_fixture.py`, `fixture-spec.json`, and `fixture-sources.xml` describe and generate the fixture.
- `inspect_fixture.py`, both inventory JSON files, `reference-ledger.json`, `compare_probe.py`, and `comparison.json` record the package findings and exact comparison.
- `before.docx` and `after-attempt.docx` preserve the fixture state; `render-before/page-1.png` and `render-before/before.pdf` preserve the inspected render.
- `environment-public.json` records the installed Word version and runtime bundle. `ui-attempts.json` records the bounded UI failures without account or document-history details.

The same agent designed the fixture, knew the expected outcomes, and executed the checks. No independent/blinded scorer, adversarial manuscript, field repair, reorder/renumber operation, year-suffix disambiguation, citation-manager integration, or successful native refresh was tested. Bibliographic authenticity and claim support were outside scope because both sources are deliberately fictional. The appropriate release-test label is **blocked for native refresh, passed for the bounded package and render checks**, with neither label generalized into an effectiveness claim for the skill.
