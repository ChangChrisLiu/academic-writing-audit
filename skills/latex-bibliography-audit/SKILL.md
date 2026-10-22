---
name: latex-bibliography-audit
description: Audit or repair a LaTeX project's BibTeX or biblatex records against Google Scholar Cite to BibTeX exports. Use for inconsistent metadata, the same paper stored under multiple keys, key collisions, or citation-key repair. Preserve distinct publication versions and verify the source and rendered bibliography separately.
license: MIT
---

# LaTeX Bibliography Audit

Use the Google Scholar **Cite → BibTeX export for the intended article/version** as the bibliographic baseline. Different citation keys or minor formatting differences do not make the same article two publications.

## Establish the project and evidence

Identify the actual main file, included files, bibliography databases, BibTeX or biblatex/Biber workflow, style, custom citation commands, and requested audit or edit scope. Preserve original records and recoverable files. A shared library can legitimately contain uncited works; do not delete them merely because this manuscript does not cite them.

Create or reuse the [reference ledger](references/reference-ledger.md), retaining original entries, candidate groups, occurrence locations, and per-field provenance. Candidate grouping does not authorize an early merge.

For authenticity, require two distinct agents independently checking the same original references on Google Scholar first, then corroborating the complete title, ordered authors, publication year, venue, and intended version against primary publication evidence. Each agent must do this even when Scholar metadata appears complete; using the same primary source is permitted but is not independent underlying source evidence. Each supplies its own source record before seeing the other's verdict. Leaf verifiers do not recursively delegate. A completed traceable two-agent record for unchanged identities/versions can be reused; a key rename or citation-style change alone does not invalidate it. Reopen affected fields when identity, version, or conflicting evidence changes. Without it, report the metadata or syntax checks performed while leaving dual authenticity verification incomplete. Agreement does not override a source conflict. A failed search is not proof of nonexistence.

## Obtain the canonical export

Find the intended version in Scholar, open **Cite**, then choose **BibTeX**, as described by [Google Scholar help](https://scholar.google.com/intl/en/scholar/help.html). Inspect the actual export, not a guessed export URL, a search snippet, a DOI service's substitute, or model-generated BibTeX. If a retrieval tool cannot read Scholar or its export, try an available, authorized ordinary browser route. Distinguish parser failure, site restriction, and a no-result search. Stop at a challenge or after the available normal route fails, without endpoint loops or bulk retries. If the export still cannot be retrieved, report that step incomplete; an external record may be supplemental evidence but is not a Scholar export.

Save the raw export unchanged and record its observed result/export URLs, capture time, and intended work/version. Keep its bibliographic fields as the default baseline. A stable local citation key may differ from the exported key because keys identify project references, not publication identity. Record key mappings and any necessary encoding, escaping, or acronym-protection changes separately from the untouched export. Separate the untouched export from the working bibliography. **An absent export field is not an instruction to delete an existing field.** Preserve an existing DOI or other bibliographic field that has been verified for this exact work/version, and record its primary-source provenance as a local supplement. An unverified existing field remains pending verification, not automatically false or silently removed. Do not invent absent values, silently add unrelated metadata, or conceal a conflicting value. See the field-retention decisions in [identity and key decisions](references/identity-and-keys.md).

If the export conflicts with the verified article or its primary record, stop automatic replacement for that entry. Report both values and resolve the intended version and conflict before accepting a corrected record. This prevents a canonical-source preference from propagating a known metadata error. Do not claim a full match while that conflict remains.

## Resolve identity before deduplication

Read [identity and key decisions](references/identity-and-keys.md). Match the actual work **and version**, using a verified DOI or other stable identifier together with title, authors, year, and venue. A DOI pasted onto the wrong title is a conflict, not proof of identity.

Distinguish the same paper under different keys, one key assigned to different papers, and distinct publications with similar titles. Preserve a preprint, conference paper, journal extension, translation, correction, or new edition when it is a separately intended source. Do not collapse them because Scholar clusters versions or a title happens to match.

## Apply only authorized changes

For duplicate records of one intended publication, select a stable surviving key and produce an old-to-new mapping. Update citation arguments across the actual source graph, including included chapters, captions, appendices, multicites, custom wrappers, and intentional `\nocite` use. Parse the project's citation syntax or inspect custom commands directly. Do not run global string replacement through prose, comments, or unrelated macros. Report inaccessible external inputs rather than claiming complete coverage.

Preserve `@string`, `crossref`, `xdata`, protected capitalization, encodings, citation options, and citation-manager ownership where present. Check references to removed keys inside bibliography records as well as TeX files. Resolve a same-key/different-work collision by inspecting each citation's intended source; never remap all occurrences to one arbitrary paper. If intent is unknown, keep the conflict explicit.

Do not alter titles to fit prose preferences. Literal punctuation, hyphens, mathematical notation, author names, and style-required syntax are bibliographic data.

## Verify and report

After an authorized edit, compare the source diff, key mapping, remaining collisions, and unresolved citation arguments. Build using the existing project workflow when available and within scope. Associate the build log with the exact edited inputs, and retain the resulting bibliography output when available. Inspect the resulting bibliography and affected citations to confirm that one intended publication is no longer printed twice and that distinct sources remain distinct. Source checking, successful compilation, and rendered-output inspection are separate claims. An audit-only task does not require rewriting or a new build.

Report canonical export provenance, resolved and unresolved identities, changes made or proposed, kept versions, source coverage, dual-verification status, and actual build/render status. A syntax-valid `.bib` file is not evidence that its references are real.
