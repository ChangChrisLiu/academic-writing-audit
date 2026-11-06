---
name: latex-bibliography-audit
description: Audit, add or repair BibTeX entries using only verbatim Google Scholar Cite to BibTeX exports for the intended publications. Use for inconsistent metadata, the same paper stored under multiple keys, key collisions, or citation-key repair. Preserve distinct publication versions and verify the source and rendered bibliography separately.
license: MIT
---

# LaTeX Bibliography Audit

Every accepted BibTeX entry must be copied verbatim from the actual **Google Scholar Cite → BibTeX** export for the intended work and version. This applies to new entries, existing bibliography audits, imports and pasted answers. Use the exported key, entry type, fields, casing, punctuation and escaping as captured.

## Establish the project and evidence

Identify the actual main file, included files, bibliography databases, BibTeX or biblatex/Biber workflow, style, custom citation commands, and requested audit or edit scope. Preserve original records and recoverable files. A shared library can legitimately contain uncited works; do not delete them merely because this manuscript does not cite them.

Create or reuse the [reference ledger](references/reference-ledger.md), retaining original entries, candidate groups, occurrence locations, and per-field provenance. Candidate grouping does not authorize an early merge.

For authenticity, require two distinct agents independently checking the same original references on Google Scholar first, then corroborating the complete title, ordered authors, publication year, venue, and intended version against primary publication evidence. Each agent must do this even when Scholar metadata appears complete; using the same primary source is permitted but is not independent underlying source evidence. Each supplies its own source record before seeing the other's verdict. Leaf verifiers do not recursively delegate. A completed traceable two-agent record for unchanged identities/versions can be reused; a key rename or citation-style change alone does not invalidate it. Reopen affected fields when identity, version, or conflicting evidence changes. Without it, report the metadata or syntax checks performed while leaving dual authenticity verification incomplete. Agreement does not override a source conflict. A failed search is not proof of nonexistence.

## Obtain and verify every export

Inventory every in-scope entry, including apparently correct existing ones. For each, open the intended Scholar result, select **Cite → BibTeX**, and save the returned entry as received. Keep the observed result link or search locator, target version, capture date, raw artifact and checksum in the ledger. Retain the source privately as needed and redact account or session tokens from public evidence. A traceable prior capture may be reused under the ledger's version rules. Record its original capture date. Follow the [Scholar export instructions](https://scholar.google.com/intl/en/scholar/help.html).

Compare the export's full title, ordered authors, year and venue to the intended publication and the two independent verification records. Publisher, DOI and proceedings records corroborate identity. Record confirmed DOI values and other outside metadata in the ledger only. A missing, ambiguous or conflicting identity field requires resolution before acceptance. Preserve both observations if the Scholar export disagrees with the primary record.

Open an available authorized ordinary browser if the retrieval tool cannot read Scholar. Stop at an access challenge. If Cite or its BibTeX output is missing, record the reason and leave the entry pending. Keep an existing entry recoverable and untouched in that state. For a new reference, return its pending citation location in an editorial note. Never construct, autocomplete, reserialize or substitute a BibTeX entry from an agent's memory, a search snippet, publisher export, DOI lookup or other metadata, even if every field looks correct.

After verifying identity and authorization to edit, copy the **whole captured entry** into the working bibliography and compare the final text with the capture. Preserve the exported key and every character inside the entry. Only leading or trailing whitespace around separate entries is outside this comparison. Back up existing entries first. Any extra field such as a verified DOI belongs in the ledger, outside the canonical `.bib` entry. If a style or build requires a modified record, surface the incompatibility and hold the item. Keep unresolved entries out of any count of Scholar-matched references.

Prepare a dedicated capture directory with one raw `.bib` file per intended work and a UTF-8 `captures.json` array. Each row identifies `file` (capture basename), `sha256` (digest of the entire saved file), `scholar_result` (observed HTTPS Scholar search or result URL), `captured_at` (ISO date and time with timezone) and `version` (intended publication). Populate these from the retrieval evidence. Preserve the actual capture precision. Record the work and primary-source corroboration in the ledger. A digest protects saved bytes after capture and requires the retrieval evidence to establish their origin.

For local comparison of export-only bibliography files, run the read-only [export checker](scripts/check_scholar_exports.py) with `python3 scripts/check_scholar_exports.py --bib working.bib --exports capture-directory` from this skill folder. Supply one independently sourced Scholar capture per file and a directory covering the scoped bibliography. Inspect per-entry differences, missing coverage and collisions. Record complex files outside its supported format for manual review. The checker accepts braced entries separated by whitespace and expects the scope of the index and databases to agree. Exit 0 indicates local equality, 1 reports entry differences, and 2 requires review of inputs or unsupported syntax. A text match checks the working copy only. Establish the actual Scholar retrieval, intended version and independent identity checks from their own evidence.

## Resolve identity before deduplication

Read [identity and key decisions](references/identity-and-keys.md). Match the actual work **and version**, using a verified DOI or other stable identifier together with title, authors, year, and venue. A DOI pasted onto the wrong title is a conflict, not proof of identity.

Distinguish the same paper under different keys, one key assigned to different papers, and distinct publications with similar titles. Preserve a preprint, conference paper, journal extension, translation, correction, or new edition when it is a separately intended source. Do not collapse them because Scholar clusters versions or a title happens to match.

## Apply only authorized changes

For duplicate records of one intended publication, use the unaltered key from the verified export and produce an old-to-Scholar key mapping. Update citation arguments across the actual source graph, including included chapters, captions, appendices, multicites, custom wrappers, and intentional `\nocite` use. Parse the project's citation syntax or inspect custom commands directly. Do not run global string replacement through prose, comments, or unrelated macros. Report inaccessible external inputs rather than claiming complete coverage.

Inventory `@string`, `crossref`, `xdata`, encodings, citation options and manager ownership before applying a mapping. Check dependent records as well as TeX files. Preserve project infrastructure separately. If updating a dependency would alter a captured entry, hold it for resolution. If two distinct verified works export the same key, retain both original captures, report both citation locations and leave the conflicting change pending. Generating an alias would change the exported entry.

Do not alter titles to fit prose preferences. Literal punctuation, hyphens, mathematical notation, author names, and style-required syntax are bibliographic data.

## Verify and report

After an authorized edit, compare the source diff, key mapping, remaining collisions, and unresolved citation arguments. Build using the existing project workflow when available and within scope. Associate the build log with the exact edited inputs, and retain the resulting bibliography output when available. Inspect the resulting bibliography and affected citations to confirm that one intended publication is no longer printed twice and that distinct sources remain distinct. Source checking, successful compilation, and rendered-output inspection are separate claims. An audit-only task does not require rewriting or a new build.

Report the scoped total, counts of exact working matches, differences and missing or blocked captures, and the independently verified identity count. For each exception, give the key, field or entry difference, intended version and next action. Report canonical export provenance, resolved and unresolved identities, changes made or proposed, kept versions, source coverage, dual-verification status, and actual build/render status. A syntax-valid `.bib` file is not evidence that its references are real.
