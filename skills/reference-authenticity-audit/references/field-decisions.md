# Field and version decisions

Exact matching is bibliographic identity, not a fuzzy title score. Verify all meaningful title words and subtitles, full ordered authors, the publication year for the intended version, and the actual venue.

| Observation | Decision |
| --- | --- |
| Case, TeX escaping, typographic apostrophe, or Unicode normalization differs | Preserve the recorded forms; accept only meaning-preserving typographic equivalence. |
| Initials or a venue abbreviation appear | Resolve through a full source record; do not guess expansion or call a truncated snippet a complete author check. |
| Subtitle, author, author order, year, or journal differs | Record a field mismatch until source evidence resolves it. An abbreviated display alone does not establish absence. |
| Online-first 2023, issue date 2024 | Determine which publication/version and date rule the citation uses. Keep the distinction explicit; do not arbitrarily choose the earlier date. |
| Same title in a preprint and journal | Check version, authors, year, venue, and identifiers independently. Existence of one does not verify the other. |
| Two papers have the same title | Distinguish authors, venue, year, and identifiers. Title equality alone is insufficient. |
| Scholar shows only a citation-only record | Follow accessible primary evidence; the citation-only record alone cannot verify every field. |
| Scholar has no hit, or access is blocked | Record the query/block and unresolved status. Check primary sources if useful without claiming the Scholar requirement was completed. |
| Two agents agree but the publisher contradicts them | Retain the conflict and resolve it from the intended version's evidence. Do not pass by majority. |
| Work is corrected or retracted | Existence may still be supported. Report the relevant publication status if observed; do not erase it or infer that its claims remain valid. |

A compact per-agent record can use reference ID, query, inspected URLs/time, intended version, four observed fields, field decisions, and limitations. The coordinator adds the comparison and resolution after both records are complete. Do not make agents copy one another's source selections before their independent retrieval.
