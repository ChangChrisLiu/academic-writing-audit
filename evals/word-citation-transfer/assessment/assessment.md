# Independent assessment of Word citation-skill transfer trial

All three runs satisfy all **21 intended rubric items** on the supplied materials. Both guided runs and the control identify the expected citation and coverage issues, avoid substantive false positives, and deliver the same correctly edited DOCX. **No skill revision is justified by this trial, and no incremental benefit over the control is demonstrated.**

This is an independent but **unblinded** assessment. I knew which runs used the skill. I read every complete report, the frozen request/rubric/skill, and the actual fixture and revised DOCX packages. I used my own read-only package inspection script rather than accepting the runs' preservation reports. I also read the rendering logs and inspected the existing rendered page. All assessment writes are confined to this folder; the skill, fixtures, and trial outputs were not changed.

## Criterion decisions

“Pass” means the practical criterion is met on the available evidence; it does not certify unobserved native Word operations. A10's current-file preservation is independently verified, while its no-refresh operation history is explicitly report-based. The 21 items are rubric items, not independent experimental samples.

| Item | Intended criterion | Guided A | Guided B | Control |
| --- | --- | --- | --- | --- |
| A1 | ValeA field identity conflicts with displayed 2024b while reference entry is 2024a | Pass | Pass | Pass |
| A2 | ValeB has identified source but displayed 2024 lacks required b suffix | Pass | Pass | Pass |
| A3 | NgNote cited in real footnote; do not call uncited | Pass | Pass | Pass |
| A4 | ImaniCaption cited in caption; do not call uncited | Pass | Pass | Pass |
| A5 | MarinUnused is in main reference list with no citation in full fixture | Pass | Pass | Pass |
| A6 | SatoReading legitimately uncited in Further reading | Pass | Pass | Pass |
| A7 | LumenLibrary is embedded but absent from displayed bibliography; not an unused list entry | Pass | Pass | Pass |
| A8 | two Vale works are distinct publications, not duplicates | Pass | Pass | Pass |
| A9 | SEQ/REF fields and footnote marker are not bibliographic citations | Pass | Pass | Pass |
| A10 | original case-a.docx byte identical; no refresh/edit | Pass | Pass | Pass |
| B1 | two Ellis same-year works correctly disambiguated | Pass | Pass | Pass |
| B2 | Paz footnote and Kline caption are citations | Pass | Pass | Pass |
| B3 | no uncited main reference entries | Pass | Pass | Pass |
| B4 | Huang allowed Further reading; Dane embedded-only not a displayed list item | Pass | Pass | Pass |
| B5 | Only containss -> contains in ordinary prose; preserve all 7 fields including 4 citations, bibliography, sequence, and cross-reference; preserve source IDs, footnote relationship and bookmark | Pass | Pass | Pass |
| C1 | Chen 2023 ambiguous between two references; no arbitrary target or merge | Pass | Pass | Pass |
| C2 | no whole-document uncited verdict; Reed and unassigned Chen entries only unobserved in inspected portion | Pass | Pass | Pass |
| C3 | no native-field, style-selection, or refresh claim from text export | Pass | Pass | Pass |
| G1 | no fabricated authenticity/claim-support verdict | Pass | Pass | Pass |
| G2 | clear distinction between source library, displayed list, and occurrence inventories | Pass | Pass | Pass |
| G3 | counts specify units and inspected regions | Pass | Pass | Pass |

The exact criterion text, independent reasoning, report line locators for each run, and artifact evidence keys are recorded in [decisions.json](decisions.json). The original rubric has nine A findings plus preservation, four B findings plus the edit requirement, three C findings, and three cross-case requirements.

## Independent document findings

Case A has four actual citation occurrences: two in body paragraphs, one in the Figure 1 caption, and one in substantive footnote 1. Its main list has five entries, its separate Further reading has one, and its embedded library has seven records. Those are different inventories.

At main paragraph 3, `CITATION ValeA` identifies Tamsin Vale's *Alpha Sensor Calibration*, but the cached citation says `(Vale, 2024b)` while the Alpha entry says `2024a`. At paragraph 4, `CITATION ValeB` identifies *Beta Sensor Calibration*, but the cached citation lacks the required `b`. Thus Alpha needs the displayed `a`, and Beta needs the displayed `b`; neither field needs retargeting. The full source records establish the same author/year, and Alpha precedes Beta by the specified title rule. All runs correctly preserve that distinction.

Ng is genuinely cited in `word/footnotes.xml`, footnote ID 1, which is linked from the body. Imani is cited in the Caption paragraph. Marin alone has a displayed main-list entry with no citation in any supplied content. Sato is allowed in the separately labeled Further reading. Lumen exists only as an embedded source record. The `SEQ` figure number, `REF figProcess`, and note marker do not add literature citations.

Case B contains four citation occurrences in the same regions, four main entries, one Further reading entry, and six stored sources. The two Morgan Ellis works correctly use Archive = 2020a and Museum = 2020b in fields, displays, and entries. Paz's footnote and Kline's caption count. Huang is permitted Further reading; Dane is embedded only. There is no citation-related defect under the requested rules.

Case C supplies no field target. `Chen (2023)` has two candidate entries and cannot be uniquely assigned from the wording or titles. Neither Chen entry is confirmed used by that occurrence. Reed has no observed occurrence in the one exported paragraph; omitted material prevents any global-unused conclusion for Reed or either Chen work. No run guesses a target, merges entries, orders deletion, or infers native fields/refresh/style selection from this export.

## Saved artifact verification

The independent checks are reproducible with `inspect_independently.py`; detailed source/field/relationship/paragraph inventories are in `artifact_checks.json`.

| Check against frozen Case B fixture | Guided A | Guided B | Control |
| --- | --- | --- | --- |
| Same 18 package members and order | Pass | Pass | Pass |
| Only `word/document.xml` changed | Pass | Pass | Pass |
| Changed XML equals original bytes with only the exact authorized prose replacement | Pass | Pass | Pass |
| Other 17 member payloads byte-identical | Pass | Pass | Pass |
| All seven complete fields, instructions, delimiters, and cached results unchanged | Pass | Pass | Pass |
| Four citations include caption and real footnote | Pass | Pass | Pass |
| Six source records, tags/GUIDs, relationships, note anchor, and bookmark preserved | Pass | Pass | Pass |
| ZIP CRC and XML parsing succeed; internal relationship targets exist | Pass | Pass | Pass |
| All four supplied input files match frozen fixtures | Pass | Pass | Pass |

All three revised DOCX files are **byte-identical**, with SHA-256 `247b25e0b4b4ec934ca99d4073e88b421e80ef621a1453c8126dd9f426380194`. Case A's input is byte-identical to the fixture in every run, SHA-256 `d45de9aeffce9fdb92ea670a3fd965b846e500d095030d6817f0773392f1ba62`. Case B's original hash is `f3be77c7d27af6797dfbf605ea7225491a847e89db96ee4e8e2887adf1fb8463`.

The exact saved change is `The catalogue containss two registers ` → `The catalogue contains two registers ` before the first citation field. No field result or instruction changes. The ordinary text run, remaining XML bytes, footnote and source parts, style/configuration parts, and relationship parts establish the requested narrow edit without relying on a prose claim that fields were preserved.

Each rendering log records the bundled `soffice` converter. The three page PNG files are byte-identical (SHA-256 `0346b839061d9ae6b35fa761e7671f84c798d686a45370e0efcb4ac59c94403a`). I visually inspected the full representative Guided A page; identical bytes make that inspection applicable to the saved PNGs from the other runs. The word “contains,” both Ellis suffixes, Kline caption, figure cross-reference, four main entries, Huang Further reading, and Paz footnote are readable without observed clipping, overlap, or missing content. This review did not rerender or open a native application.

## Disagreements and findings outside the rubric

There are **no substantive disagreements with the reports and no substantive false positives found**. Three interpretation points prevent unfair deductions:

1. Guided A calls the ValeB visible text ambiguous; Guided B calls it a “visibly ambiguous target.” Each immediately resolves the intended work to Beta through `ValeB` and proposes the correct `2024b`. This is an accurate distinction between inadequate visible disambiguation and known source identity, unlike the genuinely unresolved text-only Chen case.
2. The control's instruction to change a citation result is an exact correction proposal, read alongside its instruction to retain source/field identities, use an appropriate field-aware workflow, and beware of overwritten cached text. It did not change A or recommend replacing fields with plain text.
3. The A/B custom title-alphabetical requirement is not silently imposed as a verified selected style for C. All reports preserve C's unavailable-style boundary while identifying the visible identity problem.

The additional static APA/Version 6 stylesheet observations are supported by the packages and carefully bounded. The reports do not claim an active Word style, full APA compliance, or demand unrelated ordering/typography changes. Their A/B no-missing-target and no-duplicate-work conclusions are supported within these supplied records. The guided reports' statements about absent revision markup and extra content stories are consistent with independent inspection. The control's possible stale/manually changed cache explanation is labeled a possibility and does not become an unsupported causal verdict.

The control does not explicitly say “claim support was not checked,” unlike the guided reports. It makes no claim-support verdict and the requested fictional mapping audit does not require that check. This is a minor reporting omission, with no rubric failure and no evidence for changing the skill. Its counts are less tabular but have identifiable units and stated scope; the lack of an identical ledger layout is not a performance failure.

## Missing checks and limits

No required artifact-level check is missing for the authorized narrow edit. Several outcomes remain untested by design:

- Independent assessment but unblinded: run labels and treatment assignments were known. Fresh contexts, withheld rubric, and no cross-report access are protocol facts supplied by the parent, not independently verified by this artifact review.
- Only two constructed DOCX fixtures and one short partial export were tested. There are two guided runs and one control; 21 rubric items are not 21 independent experiments.
- Native Microsoft Word open, citation-manager refresh, native save/reopen, active style behavior, and post-refresh persistence were not tested. Static XML and LibreOffice rendering cannot establish those outcomes.
- No actual citation or bibliography repair was authorized or performed. A future repair that changes generated suffixes or excludes a source from BIBLIOGRAPHY remains untested.
- The fixtures contain no numeric ranges, grouped references, corporate or ambiguous multi-author cases, actual tracked revisions, nonempty table/textbox/appendix stories, external manager field formats, corrupted fields, or long-document layout challenges.
- No authenticity or claim-support verification was tested because the fictional offline request excludes it. No external lookup was used by this assessor.
- A current byte-identical input proves no saved change. A no-refresh historical claim remains report-based without complete execution traces.

All three reports explicitly separate saved package structure and cached displays from native refresh. A successful LibreOffice export and an unchanged package are not evidence that Microsoft Word or a reference-manager integration has refreshed, saved, and reopened correctly. Current input equality also cannot prove that no transient operation ever occurred; that historical statement is reported, not independently witnessed.

## Skill revision and comparative conclusion

Retain the frozen skill unchanged on this evidence. Its existing directions already cover both mapping directions, note/caption coverage, stored-source versus displayed-list distinctions, style evidence, partial exports, narrow editing, and the static/native boundary. Both guided runs apply these distinctions successfully. The control reaches the same practical decisions and produces the same deliverable, so this trial cannot establish incremental benefit, general superiority, or native Word refresh reliability.

The useful result is a passed, narrow transfer/regression check with a successful control. If broader validation is desired, test the unrepresented cases above and observe authorized native refresh/save/reopen separately; those are future tests, not reasons to rewrite a currently passing skill.

## Evidence files

- [decisions.json](decisions.json): every rubric criterion, per-run report locator, outcome, extra-finding review, limits, and revision decision.
- [artifact_checks.json](artifact_checks.json): independently extracted fixture/output evidence and actual comparison results.
- [inspect_independently.py](inspect_independently.py): reproducible static checker used for this assessment.
- [Guided A report](../runs/guided-a/output/report.md), [Guided B report](../runs/guided-b/output/report.md), [control report](../runs/control/output/report.md): assessed reports, unchanged.
- [Representative rendered page](../runs/guided-a/output/rendered-b/page-1.png): visually reviewed; all three saved page PNGs are byte-identical.
