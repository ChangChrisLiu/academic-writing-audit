# Word citation audit report

Case A has two citation display errors and one uncited entry in its main References. Its stored citation targets are identifiable and do not need to be retargeted. Case B has no citation identity, suffix, or coverage error under the supplied rules; `revised-b.docx` changes only “containss” to “contains” and preserves its fields. Case C is an incomplete export: its Chen citation is ambiguous, and the material cannot support a whole-document uncited-reference finding.

## Scope and evidence

This audit used only `request.md`, `case-a.docx`, `case-b.docx`, and `case-c-excerpt.txt`. The publications are fictional; no authenticity, publication-existence, or external literature search was performed.

For A and B, I read the complete main document XML, the attached footnote, citation field instructions and cached results, stored bibliography sources, relationships, and content types. Both supplied documents have 12 main-body paragraphs, including a caption, main References, and Further reading, plus one substantive footnote. No additional endnote, header, footer, comment, table, text-box, or appendix content is present in these files. The note separators are not substantive notes. “Displayed text” in the A audit means the saved field result in the DOCX, not a newly refreshed Word display. A was not edited, rendered, or refreshed.

The required rules for A and B are author–year citations, title-alphabetical a/b suffixes for exactly the same author and year, and a cited-works-only main References list that counts notes and captions. Uncited recommendations are allowed in Further reading. Both packages store an APA style descriptor (`StyleName="APA"`, version 6, `SelectedStyle="/APASixthEditionOfficeOnline.xsl"`). That descriptor is static metadata; it does not establish that a particular application's style engine is loaded or that an update has been performed. The supplied rules govern this audit.

## Case A

### Citation identity and visible mapping

Locations below are main-body paragraph numbers, counting the title as paragraph 1; the footnote is separately identified.

| Location and field tag | Stored source identity | Saved display and main-list entry | Finding and smallest correction |
| --- | --- | --- | --- |
| Alpha protocol sentence, paragraph 3; `ValeA` | Tamsin Vale, 2024, *Alpha Sensor Calibration* | Citation `(Vale, 2024b)`; entry `Vale, T. (2024a). Alpha Sensor Calibration.` | Wrong displayed suffix. Change the citation result to `(Vale, 2024a)`. Retain the source target and the correctly labeled entry. |
| Beta protocol sentence, paragraph 4; `ValeB` | Tamsin Vale, 2024, *Beta Sensor Calibration* | Citation `(Vale, 2024)`; entry `Vale, T. (2024b). Beta Sensor Calibration.` | Missing disambiguating suffix. Change the citation result to `(Vale, 2024b)`. Retain the source target and the correctly labeled entry. |
| Footnote 1; `NgNote` | Rui Ng, 2022, *Quiet Instrument Records* | `(Ng, 2022)`; matching main-list entry | Correct. This note-only citation counts; keep the entry. |
| Figure 1 caption, paragraph 7; `ImaniCaption` | Ada Imani, 2021, *Diagram Conventions* | `(Imani, 2021)`; matching main-list entry | Correct. This caption-only citation counts; keep the entry. |

The source records establish that the Vale works have exactly the same author and year. Alphabetization places **Alpha before Beta**, so Alpha is 2024a and Beta is 2024b. The reference entries already implement this assignment correctly. The first citation is especially misleading: its field points to Alpha, while its saved visible label would lead a reader to the Beta entry. The second citation's visible label does not choose between the two works, but its `ValeB` target identifies Beta. These are demonstrable display-to-identity inconsistencies, not evidence that the source records should be swapped. A stale or manually altered cache is possible; the cause and the result of a future refresh were not observed.

### Coverage and stored sources

| Source | Where it appears or is cited | Disposition |
| --- | --- | --- |
| Vale, *Alpha Sensor Calibration* | Body citation and main References | Retain; correct citation suffix. |
| Vale, *Beta Sensor Calibration* | Body citation and main References | Retain; add citation suffix. |
| Ng, *Quiet Instrument Records* | Footnote 1 and main References | Retain. |
| Imani, *Diagram Conventions* | Figure 1 caption and main References | Retain. |
| Marin, *Spare Workshop Notes* (2020); `MarinUnused` | Main References and stored source metadata; no citation anywhere in the supplied document | Remove from main References. If the author intends it as a recommendation, moving it to Further reading is an alternative. No source-library deletion is required. |
| Sato, *Further Instrument Reading* (2019); `SatoReading` | Further reading and stored source metadata; uncited | Allowed. Leave in Further reading. |
| Lumen, *Stored but Unlisted Records* (2018); `LumenLibrary` | Stored source metadata only | Not a displayed reference-list entry and not a coverage error. Leave the record alone. |

There are four distinct cited works and five displayed main References entries. Every citation field resolves to a stored source, and every cited work has a main-list entry. No cited work is missing; Marin is the sole excess main-list entry. The seven stored source records are not seven displayed references. The Vale entries are different works, not duplicates.

### Field safety and proposals

All seven complex fields have balanced begin/separate/end structure: four `CITATION` fields (including the footnote), one `BIBLIOGRAPHY`, one `SEQ Figure`, and one `REF figProcess`. The `figProcess` bookmark exists around the caption number, and the saved caption and cross-reference both show 1. These numbering fields are not literature citations. Citation tags are unique in the stored source collection and resolve to the identities above.

No correction was applied to A. The smallest proposed reader-facing corrections are the two citation suffixes and removal of Marin from main References. Retain the source identities, field structures, note, caption, numbering, and bookmark. Do not alter the publication year metadata to contain a suffix or retarget Alpha to Beta merely to match the wrong saved label. If these proposals are implemented later, use a separate working copy and an appropriate field-aware citation/bibliography workflow, then inspect the resulting citations and References. Merely changing cached field text may be overwritten by a later update; this audit does not establish that a refresh alone will fix the display or enforce cited-only bibliography membership.

## Case B

### Citation identity and coverage

| Location and field tag | Stored source identity | Saved display and coverage | Finding |
| --- | --- | --- | --- |
| First register sentence, paragraph 3; `EllisA` | Morgan Ellis, 2020, *Archive Register Methods* | `(Ellis, 2020a)`; matching 2020a main-list entry | Correct. Archive alphabetizes first. |
| Second register sentence, paragraph 4; `EllisB` | Morgan Ellis, 2020, *Museum Register Methods* | `(Ellis, 2020b)`; matching 2020b main-list entry | Correct. Museum alphabetizes second. |
| Footnote 1; `PazNote` | Lina Paz, 2018, *Oral Catalogue Notes* | `(Paz, 2018)`; matching main-list entry | Correct; retain this note-only source. |
| Figure 1 caption, paragraph 7; `KlineCaption` | Evan Kline, 2022, *Collection Diagrams* | `(Kline, 2022)`; matching main-list entry | Correct; retain this caption-only source. |
| Further reading; `HuangReading` | Ren Huang, 2017, *Further Curatorial Reading* | Uncited recommendation in Further reading | Allowed; retain. |
| Stored metadata only; `DaneLibrary` | Jo Dane, 2016, *Stored Collection Index* | No displayed entry or citation | No citation-coverage error; retain the stored record. |

There are four distinct cited works, four matching main References entries, one Further reading entry, and six stored source records. No main-list entry is uncited, and no cited work lacks an entry. The Ellis works share the same full author and year, and their a/b assignments agree across field targets, displayed citations, and entries. No citation correction is proposed under the specified rules. The mere presence of an unused stored source is not grounds to remove or add a displayed entry.

### Authorized edit and preservation verification

The only applied change is in the ordinary text run preceding `CITATION EllisA`:

- Before: `The catalogue containss two registers (Ellis, 2020a).`
- After: `The catalogue contains two registers (Ellis, 2020a).`

I verified that the affected text node is outside any field and changed the exact byte string in `word/document.xml`. I did not replace or reconstruct the paragraph. The revised package contains the same 18 members in the same order. Its other 17 member payloads are byte-identical to the original, and the changed XML differs solely by this one spelling correction. The ZIP integrity check passes.

All seven field instructions, delimiters, and cached results remain unchanged: four `CITATION` fields, `BIBLIOGRAPHY`, `SEQ Figure`, and `REF figProcess`. The footnote part, six source records, style metadata, relationships, content types, formatting, bookmark, and caption structure are preserved. This establishes preservation of the live Word field representation in the file. It does not establish successful interactive field refresh in Microsoft Word.

### Observed rendering and application boundaries

I rendered the revised DOCX with the packaged `render_docx.py` using only bundled LibreOffice at `/WORKSPACE_DEPENDENCIES/bin/override/soffice`, under a separate temporary profile. Headless DOCX-to-PDF conversion succeeded and produced one page. I opened and visually inspected the entire page image at its original resolution. The corrected prose, all four citations, References, Further reading, caption number, cross-reference, and footnote are readable with no clipping, overlap, or missing glyphs.

The PDF and PNG are internal QA outputs. The delivered DOCX is the directly patched package, not a LibreOffice-resaved DOCX. Its hash was checked after rendering. No Microsoft Word session, source-manager operation, citation insertion, style switch, bibliography regeneration, explicit field-update command, save/reopen cycle in Word, or external service operation was performed. Successful PDF export and a clean page do not prove those unperformed operations or guarantee future citation-update behavior.

## Case C

The supplied text explicitly contains only one body paragraph and the displayed reference list. Notes, captions, tables, appendices, native fields, and selected style are unavailable.

The body says `Chen (2023)`. The displayed list offers two candidates: `Chen, I. (2023a). Archive access routines.` and `Chen, I. (2023b). Collection access routines.` The visible citation does not unambiguously select either entry. The words “earlier catalogue approach” do not provide enough evidence to identify the intended title. The listed suffixes are consistent with Archive before Collection if the same-author, title-alphabetical rule is intended, but the selected style for C is unknown; the request explicitly prescribes that rule for A and B.

The smallest justified proposal is to identify which Chen work the sentence actually cites using the original field target, author confirmation, or a source-linked full document. If C is intended to follow the same suffix convention, the resulting citation should be `Chen (2023a)` for Archive or `Chen (2023b)` for Collection. Do not choose a suffix by guesswork. If both works are intended, that also requires confirmation before revising the citation.

`Reed, A. (2021). Note preservation.` has no citation in the single exported paragraph. This is **not sufficient to conclude that Reed is uncited in the document**: Reed could occur in an unavailable note, caption, table, appendix, or other body text. The same limitation prevents declaring either Chen entry globally unused. No deletion is justified from this excerpt.

The export cannot establish whole-document coverage, missing or excess references, field existence or integrity, stored source identities, the current style, whether an update occurred, or how a refresh would behave. The absence of fields in a text export is not evidence that the original document lacks them. No document edit or application operation was performed for C.

## Deliverables and audit trail

- `report.md`: this report.
- `revised-b.docx`: the authorized typo-only revision with preserved field structures.

Supporting files in the output folder record the extracted structure, exact edit/check script (`edit_and_verify.py`), verification data (`verification.json`), renderer log (`render-b.log`), and one-page rendering (`rendered-b/`). They are QA records, not additional manuscript deliverables.

All four input files remained unchanged. SHA-256 values for the two original DOCX files and the delivered revision are:

| File | SHA-256 |
| --- | --- |
| `case-a.docx` | `d45de9aeffce9fdb92ea670a3fd965b846e500d095030d6817f0773392f1ba62` |
| `case-b.docx` | `f3be77c7d27af6797dfbf605ea7225491a847e89db96ee4e8e2887adf1fb8463` |
| `revised-b.docx` | `247b25e0b4b4ec934ca99d4073e88b421e80ef621a1453c8126dd9f426380194` |
