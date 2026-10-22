# LaTeX bibliography repair report

The two records were consolidated into one intended 2001 journal article. The repaired project compiled successfully, and the one-page PDF was visually inspected. **Dual independent authenticity verification remains incomplete**: the evidence packet contains a single coordinator retrieval and publisher check, and this task did not perform new web retrieval or delegate verification.

## Exact changes

- `references.bib`: retained the stable key `breiman2001`; removed duplicate entry `breiman_short`; used all eight bibliographic fields from `scholar-export.bib` (including export capitalization and `publisher={Springer}`). Retained the existing `doi={10.1023/A:1010933404324}` as a local supplement supported by the supplied exact-version publisher record. The export omits DOI; that omission did not cause its deletion.
- `main.tex:5`: changed `\cite{breiman2001,breiman_short}` to `\cite{breiman2001}`, avoiding a repeated identical citation argument after mapping.
- `appendix.tex:2`: changed the inspected custom wrapper argument from `breiman_short` to `breiman2001`. Its definition in `main.tex:2` forwards the key to `\cite`.
- Preserved the non-citation comment at `appendix.tex:3`, other manuscript prose, style, and macro definition. The fixture's phrase “two citation keys” still describes its original input arrangement. `changes.patch` contains the complete source diff.

## Evidence and coverage

`source-record.json` reports the coordinator's 2026-10-22 17:22:20 UTC Scholar Cite → BibTeX retrieval and exact-version publisher check. `scholar-export.bib` is the unchanged displayed-text capture; it is not an HTTP byte capture. The packet records the Scholar query URL and observed export endpoint, but omits transient export-query parameters; no full href was invented or reconstructed. The supplied publisher record supports DOI retention. Title and venue capitalization differences are formatting variants in this packet, not unresolved publication-identity conflicts.

All supplied TeX sources, their local include graph, custom citation wrapper, bibliography entries, and citation arguments were inspected. The working library now has one key, two active citation occurrences, no duplicate keys, and no unresolved citation arguments. No distinct publication version was present or removed. No `crossref`, `xdata`, `@string`, `\nocite`, or inaccessible external input occurs in this fixture. Complete original records, occurrence locations, field decisions, and source URLs are in `reference-ledger.json` and `field-provenance.md`.

## Actual verification

- Source: `verification.json` confirms the key mapping, DOI retention, export-field retention, unchanged comment/evidence, and matching hashes between the edited inputs and the build record. The six original input files are preserved byte-for-byte in `original-inputs/`; `input-manifest.json` records hashes. The supplied source files were not edited.
- Build: `tectonic --keep-intermediates --keep-logs main.tex` completed with exit code 0 and ran BibTeX. Retained outputs are `main.pdf`, `main.aux`, `main.bbl`, `main.blg`, `main.log`, and `build-console.log`; `build-record.json` binds the run to the exact edited input hashes. No warning/error or unresolved-citation lines were found in the retained logs.
- Render: `rendered/page-001.png` was generated with workspace-bundled Python and pypdfium2 and visually inspected. Both citations display `[1]`, and exactly one bibliography entry appears, with author, title, venue, volume/issue, pages, and year. The existing `plain` style does not print the retained DOI; preservation is verified in the working source. `render-record.json` and `pdf-text.txt` retain render provenance and extracted text. An initial PyMuPDF import failed because `fitz` was unavailable; the subsequent pypdfium2 render succeeded.

This is a completed local metadata/key repair and build/render check. It is not a completed two-agent authenticity audit or a claim-support assessment.
