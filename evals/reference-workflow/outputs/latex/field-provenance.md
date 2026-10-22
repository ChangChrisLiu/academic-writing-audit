# Field provenance

All retrieval facts below are reused from the supplied packet. This repair run performed no new web retrieval. The untouched export is `scholar-export.bib`; the original working entries are preserved in `original-inputs/references.bib`.

| Field | Accepted working value | Basis and decision |
| --- | --- | --- |
| title | `Random forests` | `scholar-export.bib:title`; `source-record.json:primary.observed_title`. Use supplied Scholar export capitalization. Publisher capitalization is a formatting variant, not a different work. |
| author | `Breiman, Leo` | `scholar-export.bib:author`; `source-record.json:primary.observed_author_list`. Use complete author name from supplied export, corroborated in the supplied publisher record. |
| journal | `Machine learning` | `scholar-export.bib:journal`; `source-record.json:primary.observed_venue`. Use export venue spelling and capitalization; abbreviation refers to same intended journal in supplied evidence. |
| volume | `45` | `scholar-export.bib:volume`; `source-record.json:primary.observed_volume`. Unchanged value; use supplied export. |
| number | `1` | `scholar-export.bib:number`. Retain issue number from supplied export and original full record; primary packet does not independently document this field. |
| pages | `5--32` | `scholar-export.bib:pages`; `source-record.json:primary.observed_pages`. Unchanged BibTeX page-range syntax; supplied publisher packet records 5–32. |
| year | `2001` | `scholar-export.bib:year`; `source-record.json:primary.observed_publication`. Unchanged publication year; supplied publisher packet records October 2001. |
| publisher | `Springer` | `scholar-export.bib:publisher`. Added from actual supplied export; no separate new verification claimed. |
| doi | `10.1023/A:1010933404324` | Absent from export; `source-record.json:primary.observed_doi`. Retain pre-existing exact-version DOI as a locally supplemented field, based on supplied coordinator publisher check. Its omission from the Scholar export does not justify deletion. |

The exported key `breiman2001random` is retained only in the untouched export. The stable project key is `breiman2001`; `breiman_short` maps to it. No encoding or title-protection changes were needed. The detailed ledger records original field values, occurrences, source URLs, capture limits, and unresolved verification gaps.

Dual authenticity verification is **incomplete**. The supplied packet documents a single coordinator retrieval and exact-version DOI check, not two independent verifier records.
