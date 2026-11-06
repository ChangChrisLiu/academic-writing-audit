# Bibliography repair

Two original entries represented one journal article. Both now map to `breiman2001random`. The final database has one exact Scholar export, zero differences, zero missing or blocked captures and zero unresolved identities. The paper compiles, and both citations print [1] on the inspected page.

## Identity and export ledger

| Original key and occurrence | Reconciliation |
|---|---|
| `breiman2001` at `backup/references.bib:1–5`, cited in `project/main.tex:5` | Full author, year, volume, issue and pages agree. Title and journal casing differ from the export. The original has a DOI and lacks the exported publisher. |
| `breiman_short` at `backup/references.bib:6–9`, cited in `project/main.tex:5` and `project/appendix.tex:2` | Same work and version. The original abbreviates the author and journal and omits the issue and publisher. |
| Verified work and provenance | Leo Breiman, “Random Forests,” *Machine Learning*, October 2001, 45(1), 5–32. The previously supplied [A](verifier-a/record.md) and [B](verifier-b/record.md) reports independently inspected Scholar Cite → BibTeX and corroborated the title, sole author, year, venue and journal version on the same Springer record. Coverage is 1/1 distinct works. The confirmed DOI `10.1023/A:1010933404324` is retained here and in the backup. Claim support was outside scope. |
| Canonical entry | The [capture index](captures/captures.json) records Scholar result locator, version and original capture time `2026-11-05T19:20-06:00`. Both verifier records identify Scholar result `eCpzaUc5Hg0J`. The [capture](captures/export.bib), both verifiers’ raw exports and the repaired database have the same 195 bytes and SHA-256 `fd274f1b0c5702ad441dd136a83e82cbc68c964b453007acfa8e130197841cd3`. Verification reused the supplied records. No new retrieval occurred. |

## Changes and verification

- Backed up all three original files in [backup](backup/) before editing. Replaced [the database](project/references.bib) with the whole capture, preserving its key, casing, fields and whitespace. Both keys in the main citation collapsed to one argument. The included appendix’s custom citation uses the same key. Its original-key comment and the macro definition were preserved.
- Inspected the complete source graph: [main](project/main.tex), [appendix](project/appendix.tex), one database, `plain` BibTeX style. No external inputs, record dependencies, key collisions or unresolved citations were found. The fixture’s surrounding prose still describes the original two-key state.
- The [checker tests](build/checker-tests.json) returned 1 for the original database, 0 for the repaired database, 1 for a one-character title difference under the correct key, and 2 for a changed capture checksum. Temporary negative controls were separate copies.
- Tectonic 0.16.9 ran offline with cached resources, invoked BibTeX and exited 0. The [build log](build/console.log) and [input hashes](build/inputs.sha256) identify the run. The [bibliography output](build/main.bbl) contains one item. The [PDF](build/main.pdf) was [rendered and inspected](build/page-1.png): the main and appendix citations both read [1], and the reference list prints Breiman once.
