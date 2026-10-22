# Audit of the fictional LaTeX project and Word text-export packets

## Scope, evidence, and verification status

This is an audit only. No input, citation, bibliography record, field, or tracked change was edited. All corrections below are proposals. The audit applies the supplied `latex-bibliography-audit` and `word-citation-audit` skills, including their local identity/key and matching/coverage references.

The inspected case inputs are `request.md`, `export-packet.md`, `main.tex`, `appendix.tex`, `references.bib`, `canonical-export.bib`, `word-author-year.txt`, and `word-numeric.txt`, all under `evals/reference-integrity/cases/formats/`. Locations below are line numbers in those files. No other evaluation material, rubric, prior output, or memory was consulted.

The packet explicitly identifies every publication and `10.0000` identifier as fictional. No publication was searched online. Its simulated observations are adequate for the requested fixture-based identity decisions, but they are not live Google Scholar evidence or proof of real-world authenticity. Neither independent agent verification nor a completed reusable two-agent source record is available. Dual authenticity verification is therefore incomplete; no title, author list, year, venue, or DOI is represented here as externally authenticated.

No native Word document, compiler output, or rendered output is supplied. The LaTeX audit covers the supplied source graph and database; the Word audits cover only the visible exports and explicitly identified regions. Compilation, rendered bibliography/citation inspection, native field integrity, tracked-revision integrity, and claim support have not been verified. Mapping a citation to an entry does not establish that the entry supports the cited proposition.

The principal findings are:

- LaTeX: `river2024` and `river_short` represent one intended published version in the fixture; `shared` is instead a collision between two different works. The separately intended preprint, intentional `\nocite` source, and uncited shared-library item should remain.
- Numeric Word export: the expanded citation group requests reference 5, which is absent from the supplied main reference list. Required bracketed numerical formatting conflicts with the reported APA 7 manager setting.
- Author-year Word excerpt: `Lee (2021)` is ambiguous between the two Lee entries carrying 2021a/2021b. The exact required style is unknown, so style-specific corrections remain pending.

## 1. LaTeX project

### 1.1 Project and source coverage

`main.tex` is the supplied main file: it declares the document class and contains the document environment. It loads `natbib` at line 2, defines `\sourcecite` as a one-argument wrapper around `\citep` at line 3, includes `appendix.tex` at line 8, selects `plainnat` at line 9, and loads `references.bib` at line 10. These source declarations indicate the classic BibTeX/natbib workflow, rather than biblatex/Biber. No build command or compiler result is supplied, so the source configuration is not a successful-build claim.

The complete inclusion graph visible in the supplied project is:

```text
main.tex
  ├─ \input{appendix} → appendix.tex
  └─ \bibliography{references} → references.bib
```

`canonical-export.bib` is an audit baseline supplied separately; it is not loaded by `main.tex`. Both TeX sources and the entire loaded database were inspected. No additional included sources, bibliography files, `@string`, `crossref`, or `xdata` dependencies appear in these inputs. No multicite/options syntax beyond the shown commands occurs. The absence of other files in this packet does not establish coverage of an external manuscript or shared-library consumers outside this source graph.

There are five ordinary citation command occurrences containing six key arguments, plus one intentional `\nocite` occurrence containing one argument. The ordinary citations use four distinct key strings: `river2024`, `river_short`, `river_preprint`, and `shared`. Including `\nocite` adds `background` as a fifth requested key string. `references.bib` contains seven records under six distinct key strings because `shared` occurs twice. These counts describe syntax and records, not seven distinct publications or verified sources.

### 1.2 Citation-occurrence inventory

| ID | Location | Original command / requested keys | Intended target and finding |
| --- | --- | --- | --- |
| L1 | `main.tex:5` | `\citep{river2024,river_short}` | Both keys denote the same published calibration article in the supplied simulated evidence. This requests one intended publication twice under different keys. Propose one citation argument, `river2024`. |
| L2 | `main.tex:6` | `\citep{river_preprint}` | Uniquely names the 2022 preprint. The sentence and packet explicitly intend its earlier design. Keep this separate citation and record. |
| L3 | `main.tex:7` | `\citep{shared}` | The sentence identifies the soil/moisture procedure, so its intended record is Osei's *Soil moisture protocols*. The key itself collides with the image paper and is unsafe as currently stored. Propose a dedicated soil key at this occurrence. |
| L4 | `appendix.tex:3` | `\sourcecite{river_short}` | This is a real citation because the inspected wrapper expands to `\citep`. Propose `\sourcecite{river2024}` after resolving the duplicate. |
| L5 | `appendix.tex:4` | `\citep{shared}` | The sentence identifies the image/segmentation procedure, so its intended record is Park's *Image segmentation protocols*. Propose a dedicated image key at this occurrence. Do not map this occurrence to the soil record. |
| L6 | `appendix.tex:5` | `\nocite{background}` | An intentional request to include the background book in the bibliography. Keep it. It is not an ordinary prose citation and is not an accidental unused entry. |

The mention of `river_short` in `appendix.tex:6` is a comment documenting an old database key. It is not a citation occurrence and should remain unchanged by a citation-key repair. The `\citep{#1}` in the wrapper definition is a parameterized implementation, not an unresolved literal citation key `#1`.

All requested key strings exist somewhere in the database. This does **not** make the citations correct: `shared` is not uniquely assigned, while the two river keys refer to the same intended publication. The collision can cause a bibliography processing problem or selection of an unintended record; no particular compiler outcome was observed here.

### 1.3 Reference-to-citation inventory and keep decisions

| Record / location | Full identity visible in the packet | Observed use | Decision |
| --- | --- | --- | --- |
| `river2024`, `references.bib:1–4` | Mora, Ana; Chen, Lin. *Calibrating river sensors*. *Journal of Fictional Hydrology*. 2024. Fixture DOI `10.0000/fixture-river`. | L1 | Keep `river2024` as the stable local key for the published version. Use the simulated canonical fields as the proposed baseline, subject to the provenance limits below. |
| `river_short`, `references.bib:5–8` | Mora, A.; Chen, L. *Calibrating River Sensors*. *J. Fictional Hydrol.* 2024. Same fixture DOI. | L1 and L4 | Duplicate of the intended published version according to the supplied packet. Propose retiring this key after remapping its actual citation uses. Preserve the original record in recoverable material if edits are later authorized. |
| `river_preprint`, `references.bib:9–12` | Mora, Ana; Chen, Lin. *Calibrating river sensors*. 2022. Note: “Fictional preprint, version 1.” | L2 | Keep as a separately intended source. Its shared title/authors do not justify merging it with the 2024 article. |
| First `shared`, `references.bib:13–16` | Osei, Kofi. *Soil moisture protocols*. *Fictional Soil Science*. 2020. | Intended by L3 | Keep the work; propose the distinct key `osei2020soil`. |
| Second `shared`, `references.bib:17–20` | Park, Mina. *Image segmentation protocols*. *Fictional Imaging*. 2023. | Intended by L5 | Keep the work; propose the distinct key `park2023image`. This is a different work, not a duplicate to discard. |
| `background`, `references.bib:21–24` | Singh, Tara. *A guide to field sensors*. Fictional Press. 2018. | L6, intentional `\nocite` | Keep the book and the intentional inclusion command. |
| `unused_library`, `references.bib:25–28` | Garcia, Julia. *Lake sensing*. *Fictional Limnology*. 2020. | No occurrence in the supplied TeX graph | Keep. The packet expressly says this is a shared library. An uncited library entry is not automatically a manuscript error and is not grounds for deletion. No `\nocite{*}` is present. |

The seven database records therefore represent six intended source identities/versions under the packet's assumptions: one published river article, its separately intended preprint, the soil article, the image article, the background book, and the lake article. Only the published river record is duplicated. The collision and duplication are different problems and require different repairs.

### 1.4 Canonical export provenance and field decisions

The local `canonical-export.bib:1–8` is explicitly a **simulated** intended-version Cite → BibTeX export. `export-packet.md` says its simulated primary record agrees on title, full ordered authors, year, and venue. This supports the fixture's intended identity; it is not a live retrieval. No observed Scholar search/result URL, actual export URL, retrieval time, or independent source record is supplied. Those provenance items remain unavailable, rather than being reconstructed or invented.

The raw supplied simulated export is:

```bibtex
@article{mora2024calibrating,
  title={Calibrating river sensors},
  author={Mora, Ana and Chen, Lin},
  journal={Journal of Fictional Hydrology},
  volume={12},
  pages={41--58},
  year={2024}
}
```

Keep that raw file unchanged. The proposed canonical-to-local key mapping is `mora2024calibrating` → `river2024`; a stable project key need not match the export key. The title, full authors in their existing order, journal name, volume, page range, and year above are the proposed baseline. This supplies volume 12 and pages 41–58 that are missing from both current river records. Any eventual key substitution should be recorded separately from the raw export. No escaping, encoding, or acronym-protection change is indicated by the supplied fields.

The simulated export contains **no DOI**. Do not add one to it, invent one, or silently blend the DOI from the current library into a purported canonical export. The existing library's matching DOI strings are only synthetic fixture evidence, not an independently verified DOI addition. A proposed local record based strictly on this export would leave the DOI absent. Preserve the original records so their prior DOI values remain recoverable; any later decision to retain/add a DOI should be explicit and separately sourced, rather than represented as a field supplied by this export.

### 1.5 Smallest justified proposed repairs

These changes are fully specified for review but have **not** been applied:

| Existing identity/key | Proposed key / action | Source changes |
| --- | --- | --- |
| `river2024` and `river_short`, same intended 2024 article | Survive as `river2024`; proposed bibliographic fields come from the supplied simulated export | Replace the whole argument list in `main.tex:5` with `{river2024}`; change only the argument of `\sourcecite` in `appendix.tex:3` to `{river2024}`. |
| `shared` belonging to the Osei 2020 soil record | `osei2020soil` | Rename that database record and change `main.tex:7` to `\citep{osei2020soil}`. |
| `shared` belonging to the Park 2023 image record | `park2023image` | Rename that database record and change `appendix.tex:4` to `\citep{park2023image}`. |
| `river_preprint`, `background`, `unused_library` | Keep all three records under their existing keys | Keep the preprint citation and `\nocite{background}` unchanged. |

The `shared` mapping is conditional on the **record identity and occurrence**, not a global old-key-to-one-new-key substitution. Local source wording is sufficient in this fixture to distinguish the intended soil and image records; it does not authenticate their contents. A blanket replacement of every `shared` occurrence with either one of these proposed keys would misdirect the other citation.

Likewise, replacing only `river_short` with `river2024` inside the first group would produce `\citep{river2024,river2024}`. The correct proposed group contains the surviving key once. Leave the old-key comment and unrelated prose unchanged. No `crossref`/`xdata` key references need adjustment in the supplied database, and no external consumers have been checked.

If repairs are later authorized, preserve recoverable inputs, apply these occurrence-aware edits, recheck uniqueness and key resolution across the source graph, and use the actual project's BibTeX/natbib build workflow. Inspect the rendered citations and bibliography to confirm the article is printed only once and the preprint/soil/image sources remain distinct. Those are future validation actions, not checks completed by this audit.

### 1.6 Unresolved `conflict2025` observation

`export-packet.md` separately reports a candidate named `conflict2025`: its simulated Scholar export says 2025, while its simulated intended issue record says 2024. No evidence distinguishes a version difference from an extraction error. This candidate has no record in the supplied `references.bib`, and neither full source record is included; it is therefore a contextual unresolved conflict, not an eighth database record or an observed citation occurrence.

Keep both reported year values explicit. Do not replace a year automatically, blend the records, treat either value as a verified correction, or report a full metadata match. Resolve the intended publication/version against the complete underlying source observations before any correction. The canonical-export preference does not override a known contradictory intended issue record.

## 2. Word numeric export

### 2.1 Required format, reported configuration, and coverage

The venue instructions reported at `word-numeric.txt:2` require a numbered reference list and bracketed citations. The manager is separately reported as set to **APA 7**. These are conflicting observed settings, and the output should be brought into alignment with the venue requirement if editing is later authorized. No exact named numerical style or version is supplied; do not select “Vancouver,” assume first-citation numbering, or impose a specific punctuation/author-abbreviation convention from the brackets alone.

The visible text broadly uses bracketed numerical citations and numbered entries, but the reported manager configuration is not native-field evidence. The export cannot establish which style is actually attached to live fields, whether labels are stale, or whether references are managed fields or plain text. Inspect the native document/manager before a field-aware repair, and obtain the exact numerical style if detailed formatting is needed.

The inspected regions are the body, one table caption, one footnote, the main reference list, and the permitted further-reading section. Appendix and text boxes are explicitly absent. Native fields and tracked revisions cannot be inspected. The intended accepted/original/final revision view is not stated; this audit takes the supplied visible export as the inspected view and does not assume it establishes a complete final-document inventory.

### 2.2 Citation-to-reference inventory

| ID | Location and visible form | Expanded target(s) | Status and action |
| --- | --- | --- | --- |
| N1 | Body, line 4: `[1–3, 5]` | 1, 2, 3, 5 | Labels 1, 2, and 3 each have one supplied main-list entry. Label 5 has no supplied entry. Resolve the intended source of 5 from the author/manager; restore that source or correct the citation only after establishing its intended target. Do not invent a reference. |
| N2 | Table caption, line 5: `[4]` | 4 | Maps to the supplied Singh entry. Keep; it is cited in the inspected caption even though absent from the body. |
| N3 | Footnote 1, line 6: `[6]` | 6 | Maps to the supplied Garcia entry. Keep; it is cited in the inspected note. Footnote number 1 is the note container, not a reference-list label assignment. |

`Figure 2` in line 4 is a figure cross-reference, not a bibliographic citation. `[12]` in the same line is explicitly confirmed by the author as a sample-size notation; exclude it from the citation inventory and do not report a missing reference 12. These exclusions are supported by the packet, not by assuming that every bracketed number is or is not a citation.

There are three visible bibliographic citation occurrences containing six expanded target requests: five requests map to supplied main-list entries and one, label 5, is missing. This is a label-mapping result. Native field targets and paper-level support cannot be checked from the export, so an existing numerical label is not proof that a hidden field points to the intended work.

### 2.3 Reference-to-citation inventory

| Main-list label / location | Full visible bibliographic identity | Observed occurrence | Finding / keep decision |
| --- | --- | --- | --- |
| 1, line 8 | Ana Mora. *River calibration*. *Fictional Hydrology*. 2024. | N1 | One visible match; keep. |
| 2, line 9 | Kofi Osei. *Soil measurement*. *Fictional Soil Science*. 2020. | N1 | One visible match; keep. |
| 3, line 10 | Mina Park. *Image measurement*. *Fictional Imaging*. 2023. | N1 | One visible match; keep. |
| 4, line 11 | Tara Singh. *Temperature offsets*. *Fictional Measurement*. 2018. | N2, table caption | Cited in an inspected non-body region; keep. |
| 6, line 12 | Julia Garcia. *Sensitivity analysis*. *Fictional Statistics*. 2021. | N3, footnote | Cited in an inspected non-body region; keep. |
| 7, line 13 | Wei Li. *Coastal measurements*. *Fictional Oceans*. 2019. | None in inspected portions | Uncited-list candidate within this export only. Check the omitted appendix/text boxes and complete revision view before deciding whether it needs a citation, relocation under a permitted convention, or removal. Do not call it unused throughout. |
| Further-reading 8, line 15 | Ruth Brown. *A measurement history*. Fictional Press. 2010. | None in inspected portions | Legitimate uncited further-reading item: the venue expressly permits this section at line 14. Keep; do not classify it as an unused main-list reference. |

The main list contains six entries, five with an observed citation in the inspected portions and one without. The separate further-reading section contains one entry. There is no supplied main-list entry numbered 5. No repeated labels or duplicate identities are evident among the visible entries, but this does not authenticate them or prove absence of duplicates in omitted material.

The missing 5 is a concrete coverage defect. The remaining numbering sequence must be reconsidered after resolving that target and identifying the exact style. Do not manually relabel 6 as 5 merely to close the gap: `[6]` already has an observed use, and such a change would neither identify the original `[5]` target nor preserve field mappings. Whether reference order must follow first appearance, and whether the permitted further-reading section shares numbering, remain style-dependent. Do not assert those conventions without the actual style instructions.

### 2.4 Proposed repair and validation boundary

Resolve the intended missing source 5 and the venue's exact numerical style. If a native managed document becomes available, change the appropriate manager source/style and refresh through the manager; do not flatten fields or manually renumber generated labels. Then recheck the expanded group, caption, note, full main list, omitted regions, and any year/ordering effects of the chosen style. No refresh, renumbering, native field inspection, or rendered-page check was performed here.

## 3. Word author-year excerpt

### 3.1 Style and document limits

`word-author-year.txt:1` asks for formatting and matching but supplies no venue, named citation style, style version, or manager configuration. Narrative and parenthetical author-year forms do not establish APA. The exact required and current configured styles are both unknown. Native manager fields are unavailable, and the packet is expressly an excerpt rather than the full paper. Whether the original document uses live fields, and its intended revision view, cannot be established from this text.

The visible body at line 2 and reference entries at lines 4–7 are the inspected scope. No full body, captions, tables, notes, text boxes, appendices, native package, or rendered pages are provided. Formatting judgments that depend on a named style—including punctuation, use of initials, author abbreviation, and assignment of year suffixes—remain pending. Visible identity mapping can still proceed.

### 3.2 Citation-to-reference inventory

| ID | Location / visible citation | Candidate(s) | Status and smallest justified action |
| --- | --- | --- | --- |
| A1 | Body, line 2: `Lee (2021)` | Entry A: Lee, S. (2021a); entry B: Lee, S. (2021b) | Ambiguous: the citation lacks the suffix distinguishing the two listed Lee works. “Describes site access” suggests A as a candidate but does not prove paper identity or claim support from the title. Confirm the intended source or field ID. If A is intended and the current suffix assignment is retained under the selected style, propose `Lee (2021a)`; if B is intended, use its corresponding disambiguated form. Do not silently choose A. |
| A2 | Body, line 2: `Rao et al. (2022)` | Entry C: Rao, A.; Green, P.; Ali, H. (2022) | Unique visible identity match in this excerpt. Keep the mapping. Whether `et al.` is the required form for this occurrence is style-dependent; do not call it correct or erroneous under an assumed APA rule. |
| A3 | Body, line 2: `(Lee, 2021b)` | Entry B: Lee, S. (2021b) | Unique visible match using the explicit suffix. Keep the mapping; exact punctuation remains subject to the unidentified style. |

There are three citation occurrences, two with unique visible matches and one ambiguous between two supplied entries. No occurrence is demonstrably missing all candidate references. A1 is an ambiguity, not evidence of a nonexistent or absent reference. No wrong-target native field can be diagnosed from the export.

### 3.3 Reference-to-citation inventory

The A–D prefixes are the packet's reference-entry labels; the author names are the names following those labels.

| Entry / location | Full visible bibliographic identity | Observed use | Finding / keep decision |
| --- | --- | --- | --- |
| A, line 4 | Lee, S. (2021a). *Access at urban sites*. *Fictional Urban Studies*. | Candidate for A1; no unambiguous assigned occurrence | Keep while resolving A1. Do not label A definitively uncited or counted as definitely cited. |
| B, line 5 | Lee, S. (2021b). *Remote sampling*. *Fictional Field Methods*. | A3; also a candidate for A1 | Clearly cited once in the excerpt. Keep this distinct work. |
| C, line 6 | Rao, A.; Green, P.; Ali, H. (2022). *Transport estimates*. *Fictional Transport*. | A2 | Clearly cited once in the excerpt. Keep. |
| D, line 7 | Moss, J. (2019). *Long-term monitoring*. *Fictional Ecology*. | None in inspected excerpt | Report “not found in the inspected excerpt.” Do not assert unused throughout or delete from the full paper without inspecting it. Unlike the numerical packet's further-reading item, no explicit further-reading convention is supplied for D. |

Four reference entries are visible: two are unambiguously cited, one participates in an unresolved match, and one has no observed citation in this excerpt. There is no visible duplicate bibliographic identity; the two Lee entries have different titles and venues and should not be merged because they share author and year. Retain the supplied 2021a/2021b distinctions until the exact style and the complete document permit verification or manager-controlled reassignment. Any eventual suffix changes must be propagated consistently to all occurrences and the bibliography.

### 3.4 Proposed repair and validation boundary

First resolve A1's intended work and obtain the required style. Apply only justified manager-aware changes if a native document is later available. Do not replace managed citation results with plain text, refresh fields during this audit, or accept revisions. A later refresh could change suffix assignment, so check both mapping directions again in the complete document. Current conclusions are limited to visible identity, ambiguity, and excerpt coverage; no native, full-document, detailed style, authenticity, or rendered validation is claimed.

## 4. Disposition and completion

The actionable proposals are: merge only the two records for the fixture's intended 2024 river publication; split the `shared` collision by work and citation occurrence; resolve the missing numerical target 5; reconcile the reported numeric venue requirement with the reported APA 7 setting; and disambiguate `Lee (2021)` after establishing its intended source and style. The unresolved 2025/2024 candidate must remain a conflict pending evidence.

Keep the separately intended 2022 preprint, intentional `\nocite{background}`, uncited shared-library article, cited caption/note references, permitted further-reading item, and distinct Lee works. Treat the Li and Moss entries only as not found within their respective inspected scopes. Do not infer whole-document nonuse from either partial Word export.

This report is the only written output of the audit. Input files were preserved. No online publication search, independent authenticity verification, bibliography repair, Word field operation, compilation, or rendering was performed. The supplied-source audit is complete within these stated bounds; live authenticity, unresolved identity/style decisions, native Word checks, and build/render checks remain uncompleted rather than implicitly passed.
