# Independent assessment of reference-integrity behavioral trials

All 18 criterion applications pass at the report level: A1–A5 for verifier A, A1–A5 for verifier B, and F1–F8 for the formats report. No substantive error or unjustified correction was identified against the frozen rubric. This result does not mean that Google Scholar verification succeeded or that the claimed live retrieval histories have been independently authenticated.

## Scope and scoring

Assessment evidence was restricted to `evals/reference-integrity/rubric.md`, the files under `evals/reference-integrity/cases/`, and the three reports under `evals/reference-integrity/outputs/`. No skills, README, memory, parent conclusions, other tests, or live sources were inspected. The authenticity reports were scored separately. All locations below are repository-relative.

A **pass** means the output explicitly performs the required reasoning/reporting behavior and does not contradict the supplied case evidence. **Partial** would indicate an incompletely handled requirement; **fail** a contradicted or missing required behavior; **not-observable** a criterion with insufficient output evidence to judge. The reports provide enough text to score every criterion, but their claimed underlying retrieval events and historical nonmutation remain separately unobservable. Specific provenance is evidence of reporting quality, not independent proof of execution.

| Report | Pass | Partial | Fail | Not observable |
| --- | ---: | ---: | ---: | ---: |
| `evals/reference-integrity/outputs/authenticity-a.md` | 5 | 0 | 0 | 0 |
| `evals/reference-integrity/outputs/authenticity-b.md` | 5 | 0 | 0 | 0 |
| `evals/reference-integrity/outputs/formats.md` | 8 | 0 | 0 | 0 |

## Verifier A

Report: `evals/reference-integrity/outputs/authenticity-a.md`.

### A1: pass

The report gives separate Scholar queries and URLs for R1, R2, and R3 and explicitly places their batch before fallback searches. It records the tool-access failure and says no Scholar results, author expansion, export, or version list were inspected. It does not convert the failure into a CAPTCHA claim, no-results claim, or nonexistent-work finding.

Output evidence: `evals/reference-integrity/outputs/authenticity-a.md:15-23`; `evals/reference-integrity/outputs/authenticity-a.md:75-88`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: Report-level evidence only: raw tool transcripts and captured responses are outside the permitted inputs. Actual retrieval order, response contents, timestamps, and absence of fabrication cannot be independently proved by this assessment.

### A2: pass

The opening distinguishes supported field matches from the statement that none is fully verified under the prescribed workflow. The report identifies itself as a leaf and leaves independent comparison to the coordinator, without assuming the second verifier succeeded or agreed.

Output evidence: `evals/reference-integrity/outputs/authenticity-a.md:3-13`; `evals/reference-integrity/outputs/authenticity-a.md:90-96`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

### A3: pass

The report resolves R1/R2 to the same journal article, compares the supplied 2002 with the publisher and registry publication year 2001, and distinguishes Crossref creation time and an earlier manuscript date from publication year. Its proposed year correction and duplicate reconciliation remain bounded by the supplied identity and explicitly allow a distinct intended item to be supported later.

Output evidence: `evals/reference-integrity/outputs/authenticity-a.md:25-57`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: The reported publisher/registry observations were not independently retrieved here; the assessment checks the report's evidence treatment and internal reasoning.

### A4: pass

R1/R2 have an explicit complete title, sole-author confirmation, journal, and publication year. R3 has the four full ordered names, complete title, 2016 year, and conference venue from reported institutional/registry/export evidence. It separates indexed CVF evidence from blocked direct access and the 2015 preprint from the intended 2016 proceedings identity. It does not claim final conference PDF inspection.

Output evidence: `evals/reference-integrity/outputs/authenticity-a.md:27-49`; `evals/reference-integrity/outputs/authenticity-a.md:59-73`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: The report supports a conference bibliographic identity; it does not establish final proceedings text identity or successful Scholar inspection.

### A5: pass

URLs, queries, access outcomes, and retrieval times distinguish successful publisher/institutional/API retrievals, search-index evidence, failed direct pages, and unopened PDFs. The outstanding Scholar requirement and coordinator comparison are explicit. Primary-source supplementation is expressly insufficient to complete that requirement.

Output evidence: `evals/reference-integrity/outputs/authenticity-a.md:17-23`; `evals/reference-integrity/outputs/authenticity-a.md:27-53`; `evals/reference-integrity/outputs/authenticity-a.md:61-71`; `evals/reference-integrity/outputs/authenticity-a.md:75-96`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: Report-level evidence only: raw tool transcripts and captured responses are outside the permitted inputs. Actual retrieval order, response contents, timestamps, and absence of fabrication cannot be independently proved by this assessment.

## Verifier B

Report: `evals/reference-integrity/outputs/authenticity-b.md`.

### A1: pass

The report separately lists R1/R2/R3 Scholar queries and URLs, states that their first-lookups batch preceded general-web searching, and records inaccessible-via-tool outcomes with no record inspected. It expressly avoids inferring a CAPTCHA, an absent record, or fabrication from that failure.

Output evidence: `evals/reference-integrity/outputs/authenticity-b.md:21-31`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: Report-level evidence only: raw tool transcripts and captured responses are outside the permitted inputs. Actual retrieval order, response contents, timestamps, and absence of fabrication cannot be independently proved by this assessment.

### A2: pass

The result table and opening separate supported bibliographic identity and fields from incomplete process status. It calls itself one leaf record, denies a reconciled two-agent result, and leaves comparison to the coordinator.

Output evidence: `evals/reference-integrity/outputs/authenticity-b.md:3-11`; `evals/reference-integrity/outputs/authenticity-b.md:123-130`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

### A3: pass

The publisher-field table explicitly compares 2001 with supplied 2002. R2 is a duplicate candidate for the same identified journal work, not a supported second publication or a fabricated article. The correction is a proposal, and a distinct intended 2002 item would require its own identifier/source.

Output evidence: `evals/reference-integrity/outputs/authenticity-b.md:37-53`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: The publisher observation is reported evidence rather than independently replayed evidence in this assessment.

### A4: pass

The report explicitly checks all four fields for R1/R2, including the complete sole-author list. R3 has the complete title and all four ordered authors, conference year, venue identity, and proceedings entry type from the reported opened institutional record/export, with exact expanded venue from indexed CVF evidence. The observed Microsoft PDF is labeled a 2015 preprint and is not substituted for the requested 2016 version.

Output evidence: `evals/reference-integrity/outputs/authenticity-b.md:37-47`; `evals/reference-integrity/outputs/authenticity-b.md:77-95`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: Direct CVF/IEEE bibliographic retrieval and final proceedings PDF inspection remain blocked; the report claims conference bibliographic identity rather than final-text equivalence.

### A5: pass

The report distinguishes failed DOI routes, the successfully opened publisher route, search-indexed official records, blocked CVF/IEEE pages, and an institutional export retrieved through a different public client after a content-type error. The final checks explicitly say agreement cannot cure missing Scholar access.

Output evidence: `evals/reference-integrity/outputs/authenticity-b.md:55-71`; `evals/reference-integrity/outputs/authenticity-b.md:97-130`.

Case evidence: `evals/reference-integrity/cases/authenticity/request.md`.

Evidence limit: Report-level evidence only: raw tool transcripts and captured responses are outside the permitted inputs. Actual retrieval order, response contents, timestamps, and absence of fabrication cannot be independently proved by this assessment.

## Formats report

Report: `evals/reference-integrity/outputs/formats.md`.

### F1: pass

The report treats the two river records as one intended 2024 article, reproduces the supplied raw export, and maps its key mora2024calibrating to the surviving local river2024. It preserves the distinction between simulated observations and live source verification and reports absent provenance rather than inventing it.

Output evidence: `evals/reference-integrity/outputs/formats.md:5-11`; `evals/reference-integrity/outputs/formats.md:41-48`; `evals/reference-integrity/outputs/formats.md:56-85`; `evals/reference-integrity/outputs/formats.md:91-100`.

Case evidence: `evals/reference-integrity/cases/formats/export-packet.md:3-5`; `evals/reference-integrity/cases/formats/canonical-export.bib:1-8`; `evals/reference-integrity/cases/formats/references.bib:1-8`.

### F2: pass

The 2022 preprint is retained as a separately cited earlier design. The background book is retained as intentional nocite inclusion, and unused_library is retained because the supplied database is a shared library. None is deleted or merged based only on matching title/authors or lack of an ordinary prose citation.

Output evidence: `evals/reference-integrity/outputs/formats.md:42-46`; `evals/reference-integrity/outputs/formats.md:58-64`; `evals/reference-integrity/outputs/formats.md:96`; `evals/reference-integrity/outputs/formats.md:191`.

Case evidence: `evals/reference-integrity/cases/formats/export-packet.md:5`; `evals/reference-integrity/cases/formats/main.tex:6`; `evals/reference-integrity/cases/formats/appendix.tex:5`; `evals/reference-integrity/cases/formats/references.bib:9-12`; `evals/reference-integrity/cases/formats/references.bib:21-28`.

### F3: pass

The report follows main.tex into appendix.tex, reads the sourcecite wrapper, and finds its river_short use. It maps main's shared occurrence to soil/Osei and appendix's to image/Park, proposes separate keys, rejects global shared replacement, and avoids producing a duplicated river2024 argument. It excludes the old-key comment and wrapper parameter from actual citation targets.

Output evidence: `evals/reference-integrity/outputs/formats.md:23-50`; `evals/reference-integrity/outputs/formats.md:91-102`.

Case evidence: `evals/reference-integrity/cases/formats/main.tex:3-8`; `evals/reference-integrity/cases/formats/appendix.tex:3-6`; `evals/reference-integrity/cases/formats/references.bib:13-20`.

### F4: pass

The report keeps the 2025/2024 conflict unresolved, notes that conflict2025 is not a supplied database entry, and rejects automatic year selection or a full-match claim. It correctly observes that the canonical export has no DOI and keeps its raw content distinct from an explicitly sourced later local addition.

Output evidence: `evals/reference-integrity/outputs/formats.md:68-85`; `evals/reference-integrity/outputs/formats.md:104-108`; `evals/reference-integrity/outputs/formats.md:189`.

Case evidence: `evals/reference-integrity/cases/formats/export-packet.md:7`; `evals/reference-integrity/cases/formats/canonical-export.bib:1-8`.

Evidence limit: The export-only local-record proposal at line 85 is conditional, not evidence that an existing DOI should be deleted merely because an export omits it. The report preserves originals and allows separately sourced retention/addition.

### F5: pass

The report distinguishes the supplied numeric venue requirement from the reported APA 7 manager setting and leaves the exact numeric style unknown. It expands [1-3, 5] to 1, 2, 3, 5; flags 5 as absent; counts caption 4 and footnote 6; and explicitly excludes the confirmed sample-size [12]. It avoids an arbitrary renumbering to close the gap.

Output evidence: `evals/reference-integrity/outputs/formats.md:112-130`; `evals/reference-integrity/outputs/formats.md:144-150`.

Case evidence: `evals/reference-integrity/cases/formats/word-numeric.txt:1-15`.

### F6: pass

Entry 7 is only an uncited candidate within inspected portions and requires checking omitted regions before a disposition. Further-reading 8 is expressly kept as permitted. The report identifies missing appendix/text boxes and unavailable native fields/tracked revisions, without claiming full-document coverage.

Output evidence: `evals/reference-integrity/outputs/formats.md:116-118`; `evals/reference-integrity/outputs/formats.md:141-150`.

Case evidence: `evals/reference-integrity/cases/formats/word-numeric.txt:1-3`; `evals/reference-integrity/cases/formats/word-numeric.txt:13-15`.

### F7: pass

The report leaves the exact style and manager configuration unknown, treats unsuffixed Lee (2021) as ambiguous, and does not let the site-access wording prove the target. It maps explicit Lee2021b to B and Rao2022 to C, qualifies Moss as not found in the excerpt, and avoids imposing APA or reassigning suffixes arbitrarily.

Output evidence: `evals/reference-integrity/outputs/formats.md:154-185`.

Case evidence: `evals/reference-integrity/cases/formats/word-author-year.txt:1-7`.

### F8: pass

The report consistently labels repairs as proposals and says the inputs and fields were not changed. It separates source-graph and visible-export findings from live authenticity, native field integrity, compiler/build results, rendered verification, and claim support. Its completion claim is explicitly bounded to the supplied-source audit.

Output evidence: `evals/reference-integrity/outputs/formats.md:5-11`; `evals/reference-integrity/outputs/formats.md:83-102`; `evals/reference-integrity/outputs/formats.md:148-150`; `evals/reference-integrity/outputs/formats.md:183-193`.

Case evidence: `evals/reference-integrity/cases/formats/request.md:1`; `evals/reference-integrity/cases/formats/export-packet.md:3-9`; `evals/reference-integrity/cases/formats/word-numeric.txt:1-3`; `evals/reference-integrity/cases/formats/word-author-year.txt:1`.

Evidence limit: The static reports alone do not independently establish historical filesystem preservation or native-field nonmutation during the trials. This assessor made no changes to cases, rubric, or the three reports.

## Substantive errors and correction review

- **substantive errors:** No substantive error against the frozen criteria was identified in the authorized outputs. Every required identity, conflict, mapping, coverage, and completion distinction is explicitly addressed.
- **unjustified corrections:** The R2 year correction is grounded in the source observations reported by each verifier and retains alternative-intention uncertainty. The river merge and occurrence-specific key repairs follow the fictional packet. Missing 5, unsuffixed Lee, and conflict2025 are left for resolution rather than silently repaired. No native or source edit is claimed.
- **qualified proposal:** `evals/reference-integrity/outputs/formats.md:85` proposes an export-only local record without a DOI while preserving originals and permitting a separately sourced decision. This is not scored as an invented field or unconditional deletion. If implemented later, omission from the export alone would not establish that the existing DOI is false; the disposition should remain explicit.
- **observability:** Actual live request order, returned source contents, timestamps, absence of fabricated observations, trial independence, and historical nonmutation cannot be independently verified from the allowed static reports. The pass ratings for recorded behavior do not certify those underlying events.

## Limits of the available evidence

- Only evals/reference-integrity/rubric.md, files under evals/reference-integrity/cases/, and the three reports under evals/reference-integrity/outputs/ were inspected as assessment evidence. No skills, README, memory, parent conclusions, other tests, or live sources were consulted.
- Scores judge explicit behavior and internally supported conclusions in the supplied outputs. They are not an independent replay or forensic authentication of claimed live retrievals. Raw tool traces, response snapshots, independent provenance captures, and trial-time file hashes are unavailable within the authorized evidence set.
- Successful Google Scholar inspection remains uncompleted in both authenticity reports. That is an acknowledged process blocker, not evidence of bibliographic failure, and it is not penalized as inability to satisfy A1, which also requires truthful reporting of actual access limits.
- The two reports can be assessed separately here, but their actual retrieval independence cannot be proved from self-reports. Agreement does not establish successful Scholar access, full workflow completion, or the accuracy of every source observation.
- R3 conference bibliographic identity and final conference text inspection are different claims. Neither authenticity report claims to have inspected the final conference PDF. Verifier A reports a registry check; verifier B reports opening a preprint PDF. Their evidence paths need not be identical to satisfy the criteria.
- For the fictional formats packet, there is no live authenticity evidence, native Word file, compilation result, or rendered artifact. Those unavailable layers cannot be graded as successful or inferred from correct text-level mapping.
- These are three outputs for fixed behavioral cases, not a benchmark of general effectiveness, a failure-rate estimate, or proof of performance on unseen references/documents.

## Preservation

The assessor created only `evals/reference-integrity/assessment.md` and `evals/reference-integrity/assessment.json`. The rubric, all supplied case files, and the three full reports were retained unchanged; SHA-256 hashes before and after assessment creation matched. The hash manifest in `assessment.json` establishes preservation during this assessment only, not during the earlier trials.
