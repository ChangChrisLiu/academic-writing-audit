# Independent reference-authenticity report — verifier A

Checked **2 original entries**, intended as journal articles, using independent live Google Scholar retrievals in a new Chrome tab and direct publisher corroboration. **R1 matches all four supplied fields; R2 has a year mismatch (2002 → 2001).** Inputs were preserved. This is one leaf-verifier record, not a completed dual-verification verdict.

| ID | Original entry (unchanged) | Existence | Required fields | Intended version | Action |
|---|---|---|---|---|---|
| R1 | Leo Breiman. Random Forests. Machine Learning. 2001. | Supported | Full title, complete ordered author list, year, venue match | Journal article matched | Keep |
| R2 | Leo Breiman. Random Forests. Machine Learning. 2002. | Underlying work supported | Title, sole author, venue match; year is wrong | Identified journal version is October 2001, not the supplied year | Propose 2002 → 2001; do not edit yet |

The [publisher record](https://link.springer.com/article/10.1023/a:1010933404324) identifies **Random Forests**, **Leo Breiman** (the complete ordered list consists of this one author), **Machine Learning**, volume **45**, pages **5–32**, **October 2001**. Both its “Published” field and “Issue date” show October 2001, and its citation states 2001. DOI: [10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324). The full title has no subtitle on the inspected record. Scholar's sentence-case “Random forests” and “Machine learning” are typographic equivalents of the publisher's capitalization. The title and author information were read in full, not inferred from a truncated result snippet.

## Retrieval record

| Record | Entry | Exact query or inspected source | UTC capture | Retained evidence |
|---|---|---|---|---|
| S1 | R1 | [Scholar](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22), query `"Random Forests" "Leo Breiman"`; opened matching first-result Cite dialog | 2026-10-22T17:22:50.643Z | [Citation table](evidence-scholar-r1-cite.txt) |
| P1 | R1 | [Publisher article](https://link.springer.com/article/10.1023/a:1010933404324), linked by matching Scholar result | 2026-10-22T17:23:19.806Z | [Publisher excerpt](evidence-publisher.txt) |
| S2a | R2 | [Scholar](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22+2002), query `"Random Forests" "Leo Breiman" 2002` | 2026-10-22T17:23:33.731Z | [Initial query/result headings](evidence-scholar-r2-initial-query.txt) |
| S2b | R2 | [Scholar](https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Leo+Breiman%22), broadened query `"Random Forests" "Leo Breiman"`; opened matching first-result Cite dialog | 2026-10-22T17:24:07.673Z | [Citation table](evidence-scholar-r2-cite.txt) |
| P2 | R2 | [Publisher article](https://link.springer.com/article/10.1023/a:1010933404324), reopened after R2 Scholar retrieval | 2026-10-22T17:24:21.523Z | [Publisher excerpt](evidence-publisher-r2.txt) |

For R2, the first page with the literal year 2002 did not identify the matching Leo Breiman journal article. It showed other works with related titles. Removing the year returned the matching 2001 journal article. This limited initial search is not proof that a separate 2002 work cannot exist; the consequential finding is the mismatch against the positively identified intended journal article. The retained initial headings are search-index evidence; the Cite tables are directly inspected Scholar citation displays; the publisher excerpts are directly inspected primary-publication metadata.

## Decisions and bounds

R1 needs no change. The proposed corrected R2 is **Leo Breiman. Random Forests. Machine Learning. 2001.** No correction has been applied, and R2 remains a mismatch in the supplied input. Both original database occurrences remain distinct in [ledger.json](ledger.json); their common identity is recorded without merging or deleting entries.

For each entry, this verifier completed a Scholar-first check and primary-source corroboration. A second independent agent's record has not been read, and no agreement or disagreement with another verifier is asserted. The coordinator must compare completed records field by field before issuing any dual-verification outcome. P1 and P2 are repeat inspections of one publisher record, not two underlying primary sources. If another verifier reaches this same publisher, that is shared primary-source dependence despite independent retrieval.

No CAPTCHA or site access block occurred. One citation-table selector initially matched two elements; scoping it to the Cite dialog fixed the local locator failure. During R2 query broadening, a key action timed out on a stale accessibility element after the field had changed; fresh state and the visible Search button completed submission. Neither issue was treated as a no-result search or source-access restriction. The publisher privacy banner was handled by rejecting optional cookies. No PDF inspection or citation-file export was needed or claimed; the full publisher record supplied the required fields. Claim support and research quality were outside scope.

## Evidence handling

Public artifacts retain only citation tables, selected publication metadata, and the initial R2 query/result headings. Account details, institution/IP footer, advertisement URLs, unrelated snippets, locale/filter/button parameters, and citation-popup timestamp/session fragments were omitted. Sanitized Scholar URLs retain only the reproducible bibliographic query. Publisher URLs and DOI are public identifiers. The source excerpts were captured from the live browser during this check, not supplied snapshots or synthetic fixtures. Capture times appear in every evidence file. No personal filesystem paths appear in these artifacts.

Completed: 2026-10-22T17:25:42.703816+00:00.
