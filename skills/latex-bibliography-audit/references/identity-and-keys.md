# Identity and citation keys

| Case | Action |
| --- | --- |
| Two keys, same verified publication/version, different capitalization or abbreviated venue | One publication. Use the intended Scholar export's bibliographic fields and a stable project key; update dependent citations. |
| Same DOI but incompatible title/authors | Investigate the erroneous identifier before merging. |
| Preprint and later journal article | Preserve if separately intended. If the author wants all citations to the published version, verify equivalence for those cited claims before replacing them. |
| Same key assigned to different articles | Resolve each citation's intent, create distinct keys, and update only justified occurrences. |
| Same title, different authors or venues | Treat as separate candidates until identity is established. |
| Two distinct exports for one intended version disagree | Retain both captures and report the discrepancy; do not silently blend fields or invent a third canonical export. |
| Canonical export lacks a DOI | Preserve it as missing. Add only if explicitly requested or needed by the style and independently verified; label the addition's source. |
| A database entry is uncited | It may belong to a shared library. Do not remove it automatically. |
| `\nocite{*}` prints a library | Flag the resulting coverage and author intent; do not silently remove intentional bibliography entries. |

Example of a source-aware mapping for a confirmed duplicate:

```text
retired key: river_short
surviving key: river2024
identity: same verified work and version
canonical data: captured Scholar Cite → BibTeX export
affected citations: main text, included appendix, figure caption
other dependencies: checked crossref/xdata and custom citation wrappers
```

Do not call a render clean merely because all keys resolve. Two different keys can still print the same article twice, and one key can resolve to the wrong paper.
