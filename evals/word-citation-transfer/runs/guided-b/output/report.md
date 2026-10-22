# Word citation audit

Case A needs two displayed-citation corrections and removal of one uncited entry from the main References list. Those changes are proposals only; its original file was not edited or refreshed. Case B has consistent citation mappings, and `revised-b.docx` corrects only **containss → contains**. Case C has an ambiguous Chen citation, but its limited export cannot establish whole-document usage or native field integrity.

This is an offline identity, coverage, and field-safety audit of fictional materials. Publication authenticity and whether a source supports a claim were not checked. No web, native application, external citation-manager, or external-service operations were performed. The only office-engine operation was a bundled headless LibreOffice PDF conversion of the revised Case B file for visual inspection; it is not evidence of a Word citation-manager refresh.

## Scope and style evidence

The governing style for **A and B** is the custom author–year rule in `inputs/request.md`: works by exactly the same author in the same year receive a/b suffixes by title alphabetization; citations and entries must agree; the main References list contains cited works, including note and caption citations; the separate Further reading section may contain uncited recommendations.

Both DOCX packages store `SelectedStyle="/APASixthEditionOfficeOnline.xsl"`, `StyleName="APA"`, and `Version="6"` in `customXml/item1.xml`. This is a stored APA-style configuration hint, not verification of an active Word style or the installed style's exact behavior. The custom instructions govern this audit. I did not assume full APA requirements or recommend unrelated punctuation, capitalization, italics, or overall reference-order changes from these metadata alone. Neither a native Word style selection nor a refresh was observed.

For A and B, I inspected all package XML parts and relationships, the complete main story, the caption, the real footnote, field instructions and cached result text, the reference and further-reading sections, and the embedded source records. Each document has 12 main-story paragraphs and one real footnote, anchored at main-story paragraph 5. The footnotes part also has two separator records; these are not citations. There are no tables, text boxes, embedded content objects, alternate imported content, headers, footers, endnotes, comments, or appendices in these supplied packages. No tracked insertion, deletion, move content, or tracked-revision setting was found; no changes were accepted. Thus the inventory uses the stored document text and cached field displays without merging competing revision views. Native application display behavior remains unverified.

Locations below are stable package locators, not invented Word page numbers: **P3**, for example, means the third `w:p` in `word/document.xml`. **FN1** is `word/footnotes.xml`, footnote ID 1 (the third paragraph in that part). The entire edited Case B render is on page 1; Case A was not rendered.

| Count unit | Case A | Case B |
| --- | ---: | ---: |
| Bibliographic citation occurrences | 4 | 4 |
| Distribution of occurrences | 2 body, 1 caption, 1 footnote | 2 body, 1 caption, 1 footnote |
| Distinct source identities targeted by CITATION fields | 4 | 4 |
| Displayed main References entries | 5 | 4 |
| Main entries with an identified citation-field occurrence | 4 | 4 |
| Main entries with no observed citation in the full supplied package | 1 | 0 |
| Separate Further reading entries | 1 | 1 |
| Stored source records, including unlisted records | 7 | 6 |
| Stored-only records absent from both displayed lists and citation occurrences | 1 | 1 |
| Total complex fields | 7 | 7 |

The seven fields in each DOCX are four `CITATION` fields, one `BIBLIOGRAPHY`, one figure `SEQ`, and one figure `REF`. The figure number, cross-reference number, and footnote marker are not additional bibliographic citations.

## Case A

### Citation to reference mapping

| Occurrence and visible cached form | Field identity and intended target | Finding and smallest proposed action |
| --- | --- | --- |
| A-C1, P3: “The alpha calibration protocol is recorded in (Vale, 2024b).” | `CITATION ValeA`, source A-R1, Tamsin Vale, *Alpha Sensor Calibration*, 2024 | **Wrong displayed target.** The field points to Alpha, but `2024b` identifies the displayed Beta entry. Retain the Alpha source identity; the required citation is **(Vale, 2024a)**. Repair through the citation system and inspect the refreshed result, rather than replacing field display text manually. |
| A-C2, P4: “The beta calibration protocol has a separate record (Vale, 2024).” | `CITATION ValeB`, source A-R2, Tamsin Vale, *Beta Sensor Calibration*, 2024 | **Missing suffix and visibly ambiguous target.** The stored identity resolves the intended work to Beta. The required citation is **(Vale, 2024b)**. Retain `ValeB`; repair the generated display through the citation system. |
| A-C3, P7, Figure 1 caption: `(Imani, 2021)` | `CITATION ImaniCaption`, source A-R4 | Consistent with *Diagram Conventions*. Retain. The caption counts as a citation occurrence. |
| A-C4, FN1: `(Ng, 2022)` | `CITATION NgNote`, source A-R3 | Consistent with *Quiet Instrument Records*. Retain. The footnote counts as a citation occurrence even though the body does not print this author–year pair. |

`ValeA` and `ValeB` both name **Tamsin Vale** and year **2024** in the supplied source records. **Alpha** sorts before **Beta**, so the current reference-list assignments **Alpha = 2024a** and **Beta = 2024b** are correct under the required rule. Do not swap the reference entries or change the source tags to make the mistaken display appear consistent. The field identity, bibliographic metadata, and wording “alpha”/“beta” support the mapping; no inference about the actual books' content is needed.

All four citation fields resolve to stored source records and displayed main entries. There is no missing source or missing reference-list target in this supplied file. That does not make the two Vale displays correct.

### Reference to citation ledger

The entries below preserve the original displayed bibliographic text. The stable IDs are audit IDs; the source tags are the document's identities. Full GUIDs and source metadata are retained in `inventory-before.json`.

| Audit ID and original displayed entry | Source tag | Observed occurrence and disposition |
| --- | --- | --- |
| A-R1: Vale, T. (2024a). Alpha Sensor Calibration. Example Press. | `ValeA` | A-C1 at P3 targets this identity, despite its incorrect visible `b`. Retain the entry and its `a` suffix. Do not classify it as uncited by searching for exact visible `2024a` alone. |
| A-R2: Vale, T. (2024b). Beta Sensor Calibration. Example Press. | `ValeB` | A-C2 at P4 targets this identity but lacks its suffix. Retain the entry and its `b` suffix. A-C1's printed `b` is a display mismatch, not evidence that its field targets Beta. |
| A-R3: Ng, R. (2022). Quiet Instrument Records. Example Press. | `NgNote` | A-C4 in FN1. Properly included in main References. |
| A-R4: Imani, A. (2021). Diagram Conventions. Example Press. | `ImaniCaption` | A-C3 in the Figure 1 caption. Properly included in main References. |
| A-R5: Marin, L. (2020). Spare Workshop Notes. Example Press. | `MarinUnused` | No citation found anywhere in the supplied main story, caption, or footnote. It violates the stated cited-only main-list rule. Propose excluding this entry from the main References output through the appropriate bibliography/source controls. Retain its source record; do not invent a citation. Moving it to Further reading would require an editorial decision that it is an intended recommendation. |
| A-FR1: Sato, M. (2019). Further Instrument Reading. Example Press. | `SatoReading` | No citation observed, but it is explicitly under Further reading. This is permitted; retain. |

One additional source record, **Kai Lumen (2018), Stored but Unlisted Records, Example Press**, tag `LumenLibrary`, is present only in the embedded source collection. It is not a displayed reference or a citation occurrence. Its storage is not a violation of the main-list rule and is not a reason to delete it.

No duplicate work identities were found among the seven supplied source records or displayed entries. The two Vale works have different titles and are distinct works, not duplicates. No unsupported reference correction or authenticity conclusion is being made.

### Proposed correction sequence and unchanged status

In an authorized future citation-editing session, preserve `ValeA` and `ValeB`, ensure the citation style produces the required title-based suffixes, correct the generated displays to `(Vale, 2024a)` and `(Vale, 2024b)`, and exclude Marin from the main bibliography output while preserving its source record. Then check both mapping directions, the retained note and caption citations, and the suffixes. Native refresh, native save, reopen, and saved display/source verification would each need to be observed separately.

None of these operations was performed in this audit. Case A's complete input-file SHA-256 remained unchanged.

## Case B

### Citation and reference ledger

Case B has no citation-related correction to propose under the supplied author rules. Each main entry has exactly one identified citation occurrence; none is missing, ambiguous, or directed to the wrong stored source. Title alphabetization gives **Archive = 2020a**, **Museum = 2020b**, consistently in citations and references.

| Audit ID and original displayed entry | Citation location and cached form | Stored source identity | Finding |
| --- | --- | --- | --- |
| B-R1: Ellis, M. (2020a). Archive Register Methods. Example Press. | B-C1, P3: `(Ellis, 2020a)` | `EllisA`, Morgan Ellis, 2020 | Correct identity and suffix. |
| B-R2: Ellis, M. (2020b). Museum Register Methods. Example Press. | B-C2, P4: `(Ellis, 2020b)` | `EllisB`, Morgan Ellis, 2020 | Correct identity and suffix. |
| B-R3: Paz, L. (2018). Oral Catalogue Notes. Example Press. | B-C4, FN1: `(Paz, 2018)` | `PazNote`, Lina Paz, 2018 | Correct; note-only usage warrants inclusion in main References. |
| B-R4: Kline, E. (2022). Collection Diagrams. Example Press. | B-C3, P7 caption: `(Kline, 2022)` | `KlineCaption`, Evan Kline, 2022 | Correct; caption-only usage warrants inclusion in main References. |
| B-FR1: Huang, R. (2017). Further Curatorial Reading. Example Press. | No observed citation | `HuangReading`, Ren Huang, 2017 | Permitted uncited Further reading entry; retain. |

The source collection also contains **Jo Dane (2016), Stored Collection Index, Example Press**, tag `DaneLibrary`. It is not displayed in either list and has no citation occurrence. It is a stored source, not an uncited main References entry. Retain it. No duplicate identities were found in the six source records or displayed entries; the two Ellis titles are separate works.

### Applied edit and preservation evidence

The only applied change is P3's ordinary prose text:

- Before: `The catalogue containss two registers `
- After: `The catalogue contains two registers `

The trailing space, the following `(Ellis, 2020a)` field, and the rest of the paragraph were preserved. The target was one `w:t` in the first run, before the field's begin marker, not part of a field result or instruction. I wrote a new ZIP package with one exact byte-sequence replacement in `word/document.xml`, preserving all other member contents and package metadata used by the edit helper. I did not round-trip the document through a high-level paragraph rewrite or replace a field with plain text.

After closing and reopening the saved output as an OOXML package, the checks established:

- Exactly one member payload changed: `word/document.xml`; its entire byte content equals the original with just the one authorized replacement.
- Every other member payload is byte-identical, including `word/footnotes.xml`, `customXml/item1.xml`, the source-property relationship, all package relationships, styles, settings, and properties.
- Member order, archive comment, and preserved ZIP-entry metadata match. The saved ZIP passes its integrity check.
- All seven fields retain identical instructions, begin/separate/end markers, cached results, and locations. No fields were stripped, flattened, relabeled, or refreshed by the edit.
- Source tags, GUIDs, full supplied identities, stored style attributes, and relationships are unchanged. Every inspected internal relationship target is present.
- No citation, reference entry, further-reading entry, numbering, or revision state was changed. Rechecking the saved package yields the same bidirectional mappings above.

| Field instruction, unchanged before and after | Location | Cached result, unchanged before and after |
| --- | --- | --- |
| `CITATION EllisA \l 1033` | P3 | `(Ellis, 2020a)` |
| `CITATION EllisB \l 1033` | P4 | `(Ellis, 2020b)` |
| `SEQ Figure \* ARABIC` | P7 | `1` |
| `CITATION KlineCaption \l 1033` | P7 | `(Kline, 2022)` |
| `REF figProcess \h` | P8 | `1` |
| `BIBLIOGRAPHY \l 1033` | P10 | The same four main References entries recorded above |
| `CITATION PazNote \l 1033` | FN1 | `(Paz, 2018)` |

Exact instruction whitespace, full source GUIDs, field markers, payload hashes, and cached texts are in `inventory-before.json`, `inventory-after.json`, and `edit-verification.json`. Structural preservation is demonstrated for this narrow edit; it does not establish that Word can refresh these fields correctly.

### Rendering and application-operation boundaries

The bundled document renderer successfully converted the saved output using only `/WORKSPACE_DEPENDENCIES/bin/override/soffice`, with a separate temporary profile, and produced **one page**. I opened and inspected the entire page PNG at original resolution. It shows “contains,” both Ellis suffixes, the Kline caption citation, all four main entries, the separate Huang recommendation, the figure cross-reference, and the Paz footnote. No clipping, overlap, missing text or glyphs, or pagination defect was observed. The render log contains font-cache warnings, but the page was successfully produced and readable.

The DOCX hash remained unchanged by rendering. The PDF and PNG are QA intermediates under `render-b/`, not replacement deliverables.

| Operation | Actual status |
| --- | --- |
| Inspect original package structure and cached text | Completed for A and B |
| Save revised DOCX by the one targeted package edit | Completed for B |
| Reopen and inspect saved DOCX package | Completed for B |
| Bundled headless LibreOffice conversion and full-page visual inspection | Completed for revised B only |
| Open document in native Word | Not performed |
| Native Word/citation-manager refresh | Not performed; refresh behavior unverified |
| Native Word save | Not performed |
| Native Word reopen and post-refresh persistence verification | Not performed; unverified |

## Case C

Only the supplied body paragraph and displayed reference list were inspected. The export explicitly withholds notes, captions, tables, appendices, native fields, and the selected style. No full DOCX was supplied for this case. The request's explicit author-style rules apply to A and B; C's required style is not otherwise specified. Its visible a/b entries can nevertheless be compared with its citation without naming a particular style.

There is **one visible narrative citation**, `Chen (2023)`, and **three displayed reference entries**:

| Audit ID and original entry | Mapping from the inspected body paragraph | Bounded finding |
| --- | --- | --- |
| C-R1: Chen, I. (2023a). Archive access routines. Example Press. | Candidate for C-C1, `Chen (2023)` | The missing suffix prevents a unique match to this entry. |
| C-R2: Chen, I. (2023b). Collection access routines. Example Press. | Candidate for the same C-C1 | Equally unresolved from the supplied evidence. Do not infer the target from “catalogue approach” or a title alone. |
| C-R3: Reed, A. (2021). Note preservation. Example Press. | No citation in the inspected paragraph | **Not found in inspected portions.** It may be cited in omitted content; do not call it unused throughout the document or delete it. |

The two Chen entries have different titles; they are not duplicates merely because the displayed author and year match. Their displayed suffix order agrees with Archive preceding Collection, but no exact style/version or native generation was verified. The export gives only the initial `I.`, not native author/source identities.

The smallest proposed correction is to establish which Chen work the author intended, then use `Chen (2023a)` for Archive or `Chen (2023b)` for Collection, consistently with the final source records and style. Do not choose arbitrarily or count this one citation as confirmed usage of both works. Neither Chen entry has a uniquely resolved occurrence in the excerpt; no whole-document uncited judgment follows for either one. There is an ambiguous candidate set, not proof that the reference is absent.

The export cannot show whether citations are live fields or plain text, whether a field targets a different work from its display, whether cached text is stale, what tracked changes exist, whether references appear in omitted regions, or whether any native update was saved. It also cannot establish overall bibliography completeness or duplicate identities beyond the supplied visible entries. No Case C edits were made.

## Deliverables and evidence record

- `report.md`: this completed audit.
- `revised-b.docx`: the authorized typo-only revision, with field structures and source records preserved.

Supporting evidence in this output directory consists of `inventory-before.json`, `inventory-after.json`, `edit-verification.json`, `final-integrity.json`, the local inspection/edit helpers, `render-b.log`, and the internal `render-b/` QA artifacts. These files record the actual structural checks and conversion result; they do not claim native application verification.

Input integrity after all work:

| File | SHA-256 |
| --- | --- |
| Original case-a.docx, unchanged | `d45de9aeffce9fdb92ea670a3fd965b846e500d095030d6817f0773392f1ba62` |
| Original case-b.docx, unchanged | `f3be77c7d27af6797dfbf605ea7225491a847e89db96ee4e8e2887adf1fb8463` |
| revised-b.docx, saved and unchanged by rendering | `247b25e0b4b4ec934ca99d4073e88b421e80ef621a1453c8126dd9f426380194` |

All citation-related changes remain proposals. The only applied manuscript edit is the authorized ordinary prose typo correction in Case B.
