# Reference workflow execution checks

This v0.7.1 record exercises primary-source corroboration, normal browser access where the earlier retrieval route was incomplete, and preservation of verified working bibliography fields omitted from a Scholar export. It follows the [earlier reference-integrity trials](../reference-integrity/README.md), which did not complete Scholar access or execute document operations.

## Design and evidence

The three updated skills, initial requests, and behavioral rubric were frozen before execution in [manifest.json](manifest.json). The LaTeX fixture and its actual source evidence were frozen in [cases/manifest.json](cases/manifest.json). Each behavioral agent started in a fresh context without the rubric, prior verdicts, or another agent's output. No model overrides were used. The same host and model family were used, so independent contexts do not establish cross-model reliability.

Both behavioral verifiers used Chrome directly. This is not a blinded recovery test from a failed retrieval tool, CAPTCHA, or blocked website.

Two leaf verifiers received the same two original entries for Breiman's journal article *Random Forests*. R1 supplies 2001; R2 deliberately supplies 2002. Each independently searched Scholar in Chrome, inspected the matching record, and corroborated the full title, author, year, venue, and intended version against the Springer publication record. Both found that R1 matches and R2 has a year error. They did not equate that error with a nonexistent paper. Their underlying primary source is shared, not two unrelated authorities. See the unchanged [agent A report](outputs/authenticity-a/report.md), [agent B report](outputs/authenticity-b/report.md), their adjacent evidence and ledgers, and the [coordinator reconciliation](reconciliation.md). R2 remains a mismatch as supplied.

Separately, the coordinator opened the matching Scholar result's Cite menu, selected BibTeX, and captured its actual displayed text. The [raw export](cases/latex/scholar-export.bib) omits DOI. The [source record](cases/latex/source-record.json) supplies the primary publication evidence for the already present DOI. This is a displayed-text capture, not a byte-for-byte HTTP response. Transient export-query parameters and unrelated browser/account information are excluded from the public evidence.

The fresh LaTeX agent received that packet and an isolated duplicate-key fixture, not the completed dual-verifier reports. It applied the repair only to its output copy. The [report](outputs/latex/REPORT.md), source diff, field provenance, ledger, build record, and render record show that it retained the verified DOI, preserved the raw export, repaired main-file and appendix citations, and reduced the working bibliography to one record. Its statement that dual authenticity verification remains incomplete is correct for the evidence it received; the separate live trial does not retroactively become its input.

## Executed document operations

| Operation | Observed result | Limit |
| --- | --- | --- |
| Original LaTeX fixture | Tectonic/BibTeX compiled; one-page PDF has two bibliography entries. | Small constructed fixture, one intended paper. |
| Repaired LaTeX fixture | Tectonic/BibTeX compiled; one-page PDF has one entry and both citation occurrences display `[1]`. | Existing `plain` style does not display DOI; retention is verified in the working `.bib`. |
| Source preservation | Verified DOI retained, raw Scholar export unchanged, original source copies and non-citation comment preserved. | Does not establish every BibTeX/Biber macro or style. |
| Word package | Two fictional embedded source records, two citation fields including a table occurrence, and one bibliography field inspected. | This is structural field-to-source coverage, not a generated reference-list audit. |
| Native Word UI | Start window observed; opening route timed out before file selection. | No fixture opening, refresh, or save confirmed. |
| Word fixture rendering | Bundled office renderer produced an inspected one-page PDF/PNG with all pending markers intact. | Other-engine rendering does not prove native Word refresh. |

The coordinator independently checked the LaTeX source invariants and extracted both PDFs, then visually inspected both page images. [Before artifacts](operations/latex-before/main.pdf), [after artifacts](outputs/latex/main.pdf), and [comparison data](operations/latex-checks.json) retain those results. The method leaves the fixture prose unchanged, including its description of the original two-key arrangement.

The Word operator constructed its own fixture and knew its expected properties. Its [execution report](operations/word/REPORT.md), native documents, inventories, UI attempts, and render are public. The preserved `before.docx` and `after-attempt.docx` are byte-identical. The latter is explicitly an unchanged snapshot, not a Word-saved result. Pending caches were never replaced with fabricated refreshed citations. Native refresh is blocked; it is not a passing end-to-end Word test.

## Review and scope

The [frozen rubric](rubric.md) separates nine behavioral decisions from the constructed Word operational probe. A separate fresh-context assessor reviews cases and retained outputs without the skill text or coordinator verdict. The [assessment report](assessment/report.md) and [machine-readable decisions](assessment/decisions.json) pass all nine criteria within their stated evidence limits. Word package/render checks pass, while native opening, refresh, save, and runtime style remain unconfirmed. A preliminary escaping concern was resolved by actual XML character inspection; no fixture repair was needed. The minor retained “two citation keys” prose issue is disclosed. There is no unguided control, randomized comparison, or broad sample of publication types. The live fixture is one paper with a single author and a deliberately altered year. This record does not test a systematic review, multi-author ordering at scale, all publication-version conflicts, or all citation-manager integrations. Claim support is outside scope.

No private manuscript, review correspondence, or user bibliography was used. Public metadata evidence is limited to the consequential bibliographic fields. [Publication transformations](operations/publication-transforms.json) disclose path normalization; original local outputs were retained. The [run metadata](run-metadata.json) records assignment boundaries.

## Reproducing local checks

Use a separate working copy of the fixtures. With Tectonic available, run `tectonic --keep-logs --keep-intermediates main.tex` inside each copied LaTeX directory and inspect its `.bbl`, log, PDF, and active citation arguments. The recorded after-build input hashes are in `outputs/latex/build-record.json`. PDF text counts supplement visual inspection rather than replacing it.

The Word folder contains `build_fixture.py`, `inspect_fixture.py`, and `compare_probe.py`. The build uses Python with python-docx and lxml. Public script copies resolve their output directory relative to the script; run them only in a disposable copied folder because building replaces fixture files. `render_probe.py` requires `AWA_RENDERER` to point to the client's packaged document renderer and its dependencies. Other clients must supply their own compatible renderer and report which engine ran. A genuine native refresh test must open the disposable document in Word, refresh fields through Word, save a separate result, and inspect native fields and rendered references. Copying the input or editing cached text is not a substitute.
