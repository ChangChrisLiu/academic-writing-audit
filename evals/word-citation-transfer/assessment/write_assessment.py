"""Write criterion decisions after independent report and artifact assessment."""
from pathlib import Path
import hashlib
import json

BASE = Path('/TEST_WORKDIR')
OUT = BASE / 'assessment'
RUNS = ['guided-a', 'guided-b', 'control']
rubric = json.loads((BASE / 'private/rubric.json').read_text())
checks = json.loads((OUT / 'artifact_checks.json').read_text())

# Lines identify the unchanged reports actually read by this assessor.
rows = [
 ('A1', rubric['A']['findings'][0], 'P3 contains CITATION ValeA but cached (Vale, 2024b). ValeA identifies Alpha Sensor Calibration; P10 labels Alpha 2024a. All runs retain the field identity and propose 2024a.', [38, 38, 21], 'fixtures.a.fields; fixtures.a.sources; fixtures.a.paragraphs[P3,P10]'),
 ('A2', rubric['A']['findings'][1], 'P4 contains CITATION ValeB and cached (Vale, 2024). ValeB uniquely identifies Beta Sensor Calibration, labeled 2024b in P10. All runs propose the missing b while retaining ValeB. The visible citation is ambiguous in isolation; the intended source is resolved by the native field.', [39, 39, 22], 'fixtures.a.fields; fixtures.a.sources; fixtures.a.paragraphs[P4,P10]'),
 ('A3', rubric['A']['findings'][2], 'Footnote ID 1 contains CITATION NgNote with (Ng, 2022), and the main story has the ID 1 footnote anchor. All runs count it and retain the main-list entry.', [41, 41, 23], 'fixtures.a.fields; fixtures.a.footnotes; fixtures.a.note_anchors'),
 ('A4', rubric['A']['findings'][3], 'The P7 Caption paragraph contains CITATION ImaniCaption with (Imani, 2021). All runs count it and retain the main-list entry.', [40, 40, 24], 'fixtures.a.fields; fixtures.a.paragraphs[P7]'),
 ('A5', rubric['A']['findings'][4], 'P10 lists Marin, but the full main story and the sole substantive footnote contain no Marin citation; no additional content stories are present. All runs propose excluding Marin from the main list without inventing usage or requiring source-library deletion.', [55, 57, 36], 'fixtures.a.paragraphs; fixtures.a.fields; fixtures.a.members'),
 ('A6', rubric['A']['findings'][5], 'P11 explicitly introduces Further reading and P12 contains Sato. The request permits uncited recommendations there. All runs retain it.', [56, 58, 37], 'fixtures.a.paragraphs[P11,P12]; fixtures/request.md'),
 ('A7', rubric['A']['findings'][6], 'LumenLibrary exists in customXml/item1.xml but is absent from all displayed paragraph/reference text and citation fields. All runs distinguish the stored record from an uncited displayed list entry.', [58, 60, 38], 'fixtures.a.sources; fixtures.a.paragraphs; fixtures.a.fields'),
 ('A8', rubric['A']['findings'][7], 'ValeA and ValeB have distinct source GUIDs and distinct Alpha/Beta titles, with the same complete author and year. All runs treat them as separate works and retain their identities.', [60, 62, 40], 'fixtures.a.sources'),
 ('A9', rubric['A']['findings'][8], 'Exactly four CITATION fields occur, plus BIBLIOGRAPHY, SEQ Figure, and REF figProcess. The note marker is an anchor, not a fifth citation. Both guided reports state this explicitly; the control counts exactly four citation fields, separates the two numbering fields, and counts the citation inside the note rather than its marker.', [30, 30, 44], 'fixtures.a.fields; fixtures.a.citation_count; fixtures.a.note_anchors'),
 ('A10', rubric['A']['required_preservation'], 'Every run input case-a.docx is byte-identical to the frozen fixture. All three reports explicitly say A was not edited or refreshed. Current artifacts prove unchanged contents; they do not independently prove the absence of a transient application operation that left no saved change.', [15, 68, 9], 'runs.*.checks.case_a_input_byte_identical; reports for no-refresh statement'),
 ('B1', rubric['B']['findings'][0], 'EllisA identifies Archive Register Methods and EllisB identifies Museum Register Methods, both by Morgan Ellis in 2020. Cached citations and main entries consistently use a/b in title order. All runs accept them.', [70, 74, 54], 'fixtures.b.sources; fixtures.b.fields; fixtures.b.paragraphs[P3,P4,P10]'),
 ('B2', rubric['B']['findings'][1], 'PazNote occurs in real footnote ID 1; KlineCaption occurs in P7 Caption. All runs count both.', [72, 80, 56], 'fixtures.b.fields; fixtures.b.footnotes; fixtures.b.paragraphs[P7]'),
 ('B3', rubric['B']['findings'][2], 'Four displayed main entries each have one identified citation occurrence across body, caption, and footnote. All runs report no uncited main entries.', [87, 74, 61], 'fixtures.b.fields; fixtures.b.paragraphs[P10]'),
 ('B4', rubric['B']['findings'][3], 'Huang is displayed beneath Further reading; DaneLibrary is stored only. All runs retain these without reporting a main-list defect.', [85, 82, 58], 'fixtures.b.sources; fixtures.b.paragraphs[P11,P12]; fixtures.b.fields'),
 ('B5', rubric['B']['edit'], 'Each actual revised DOCX has precisely one uncompressed member changed: word/document.xml equals its original bytes with only The catalogue containss two registers replaced by The catalogue contains two registers. All 17 other payloads, seven complete fields and results, six source records with IDs, relationships, bookmark, and note anchor are preserved.', [99, 97, 70], 'runs.*.checks; runs.*.artifact.fields; runs.*.artifact.sources; runs.*.artifact.relationships'),
 ('C1', rubric['C']['findings'][0], 'The only visible Chen (2023) citation has two same-initial/year candidate entries with distinct a/b labels; no field target is supplied. All runs leave the intended target unresolved, reject a guessed suffix, and do not merge the entries.', [122, 141, 84], 'fixtures/case-c-excerpt.txt'),
 ('C2', rubric['C']['findings'][1], 'The export expressly excludes notes, captions, tables, and appendices and provides only one body paragraph. All runs limit Reed and Chen coverage findings to the excerpt and reject global-unused/deletion conclusions.', [125, 143, 88], 'fixtures/case-c-excerpt.txt'),
 ('C3', rubric['C']['findings'][2], 'All runs say the export cannot establish native fields, active style, or refresh behavior. Their suffix suggestions are conditional on establishing intended identity and applicable style; no native operation is claimed.', [129, 149, 90], 'fixtures/case-c-excerpt.txt; report evidence'),
 ('G1', rubric['all']['requirements'][0], 'No run declares publication authenticity or sentence-level support verified. The guided reports explicitly exclude both checks. The control explicitly excludes authenticity and makes no support verdict; it does not expressly label claim support outside scope, which is a minor reporting omission rather than a false verdict.', [5, 5, 7], 'all complete reports; fixtures/request.md'),
 ('G2', rubric['all']['requirements'][1], 'All runs distinguish four citation occurrences/targets from displayed main and Further reading entries and the larger embedded source inventory. Stored-only Lumen and Dane are correctly separated from displayed-list coverage.', [17, 17, 40], 'fixtures.a and fixtures.b source, paragraph and field inventories; complete reports'),
 ('G3', rubric['all']['requirements'][2], 'The guided reports tabulate units and region distribution. The control labels counts as distinct works, entries, stored records, or citation fields and states the inspected main-story/footnote scope; C is bounded to one paragraph. Its less tabular presentation is sufficient under the intended criterion.', [17, 17, 9], 'fixtures.a.citation_regions; fixtures.b.citation_regions; complete reports'),
]

decisions = []
for id_, criterion, reasoning, lines, artifact_ref in rows:
    decisions.append({
        'id': id_, 'frozen_criterion': criterion,
        'independent_assessment': reasoning,
        'artifact_evidence': {'file': str(OUT / 'artifact_checks.json') if not id_.startswith('C') else str(BASE / 'fixtures/case-c-excerpt.txt'), 'locator': artifact_ref},
        'runs': {run: {'status': 'pass', 'report_evidence': {'path': str(BASE / 'runs' / run / 'output/report.md'), 'line': line}} for run, line in zip(RUNS, lines)},
    })

clarifications = [
    {'issue': 'Known target with missing suffix versus genuinely unresolved identity', 'decision': 'No disagreement with any run. Guided-a says the visible text is ambiguous and guided-b says visibly ambiguous target, but both immediately resolve ValeB to Beta using its field. This is not a missed identity resolution. Case C lacks that evidence and remains unresolved.'},
    {'issue': 'Control says change the citation result', 'decision': 'Read with its Field safety and proposals section, this is an exact desired display proposal, not an instruction to flatten or blindly patch a cache. It explicitly retains field identity, prescribes a field-aware workflow, and warns cached text may be overwritten. A was not changed.'},
    {'issue': 'What unchanged package bytes establish', 'decision': 'They establish saved structure and cached-content preservation. They do not prove native Word field execution or the historical absence of every possible transient operation. All reports preserve this application boundary.'},
]

extra = [
    {'finding': 'Stored APA/Version 6/SelectedStyle descriptor', 'classification': 'supported', 'reason': 'Present in both source XML roots. All runs call it static metadata and defer to supplied rules rather than assert an active Word style or impose unrelated APA changes.'},
    {'finding': 'No missing stored target or listed identity in A/B; no duplicate work in supplied A/B inventory', 'classification': 'supported_with_scope', 'reason': 'All four field tags resolve in each package; each intended work appears in the saved main list; supplied complete identities/titles are distinct. This is an offline supplied-record conclusion, not external authenticity or bibliographic identity research.'},
    {'finding': 'Full-story inventory, no extra story content, and no revision markup in guided reports', 'classification': 'supported', 'reason': 'Package member inventory, all main-story text, and the note were independently read. The relevant table/textbox/object/import and revision indicators are absent. All relationships target existing package parts.'},
    {'finding': 'Successful one-page conversion and readable revised page', 'classification': 'supported_with_scope', 'reason': 'All render logs name bundled soffice; all three saved PNGs are byte-identical. The assessor visually inspected one representative complete page, which is readable with the corrected word, all citations, bibliography, caption/cross-reference, Further reading, and note. This is no native Word check.'},
    {'finding': 'Cause of Vale display mismatch', 'classification': 'properly_qualified_hypothesis', 'reason': 'The control calls a stale or manually altered cache possible and says the cause was not observed. No report presents a cause as demonstrated or guarantees a refresh alone will fix it.'},
    {'finding': 'No web/native Word operations and post-render hash history', 'classification': 'reported_operation_history_not_independently_witnessed', 'reason': 'Reports and logs are available, not complete execution telemetry. Current inputs/output hashes and unchanged field contents corroborate saved artifact claims, but cannot reconstruct every past process. No additional outcome is inferred.'},
]

limitations = [
    'Independent assessment but unblinded: run labels and treatment assignments were known. Fresh contexts, withheld rubric, and no cross-report access are protocol facts supplied by the parent, not independently verified by this artifact review.',
    'Only two constructed DOCX fixtures and one short partial export were tested. There are two guided runs and one control; 21 rubric items are not 21 independent experiments.',
    'Native Microsoft Word open, citation-manager refresh, native save/reopen, active style behavior, and post-refresh persistence were not tested. Static XML and LibreOffice rendering cannot establish those outcomes.',
    'No actual citation or bibliography repair was authorized or performed. A future repair that changes generated suffixes or excludes a source from BIBLIOGRAPHY remains untested.',
    'The fixtures contain no numeric ranges, grouped references, corporate or ambiguous multi-author cases, actual tracked revisions, nonempty table/textbox/appendix stories, external manager field formats, corrupted fields, or long-document layout challenges.',
    'No authenticity or claim-support verification was tested because the fictional offline request excludes it. No external lookup was used by this assessor.',
    'A current byte-identical input proves no saved change. A no-refresh historical claim remains report-based without complete execution traces.',
]

summary = {
    'assessment_type': 'independent_unblinded_report_and_artifact_review',
    'assessment_date': '2026-10-22',
    'rubric_path': str(BASE / 'private/rubric.json'),
    'rubric_sha256': hashlib.sha256((BASE / 'private/rubric.json').read_bytes()).hexdigest(),
    'tested_skill_path': str(BASE / 'tested-skill'),
    'scope': 'Read all reports and frozen skill; independently parsed actual fixtures and revised DOCX packages; inspected existing rendering. No trial output or skill changes.',
    'per_run': {run: {'rubric_pass': len(rows), 'rubric_fail': 0, 'rubric_items': len(rows), 'substantive_false_positives_found': 0, 'missing_required_artifact_checks': [], 'independent_artifact_checks_pass': checks['runs'][run]['all_checks_pass'], 'revised_b_sha256': checks['runs'][run]['artifact']['sha256']} for run in RUNS},
    'criteria': decisions,
    'substantive_disagreements': [],
    'interpretation_clarifications': clarifications,
    'extra_findings_review': extra,
    'minor_reporting_omissions': [{'run': 'control', 'item': 'Does not expressly say claim-support verification was outside scope, but performs no such check and asserts no such verdict.', 'effect_on_rubric': 'none', 'skill_revision_required': False}],
    'limitations_and_unperformed_checks': limitations,
    'skill_revision': {'justified': False, 'reason': 'Both guided runs succeed without a substantive error; the control also succeeds. The frozen guidance already covers the tested distinctions. This evidence does not identify a defect requiring a skill revision.', 'performed': False},
    'incremental_benefit': {'demonstrated': False, 'reason': 'All three runs pass every intended rubric item and produce byte-identical revised DOCX files and PNG pages. Presentation differences do not establish a task-performance advantage.'},
    'native_word_refresh_verified': False,
    'evidence_files': [str(OUT / 'artifact_checks.json'), str(OUT / 'inspect_independently.py'), str(OUT / 'assessment.md')],
}
(OUT / 'decisions.json').write_text(json.dumps(summary, indent=2) + '\n')

md = '''# Independent assessment of Word citation-skill transfer trial

All three runs satisfy all **21 intended rubric items** on the supplied materials. Both guided runs and the control identify the expected citation and coverage issues, avoid substantive false positives, and deliver the same correctly edited DOCX. **No skill revision is justified by this trial, and no incremental benefit over the control is demonstrated.**

This is an independent but **unblinded** assessment. I knew which runs used the skill. I read every complete report, the frozen request/rubric/skill, and the actual fixture and revised DOCX packages. I used my own read-only package inspection script rather than accepting the runs' preservation reports. I also read the rendering logs and inspected the existing rendered page. All assessment writes are confined to this folder; the skill, fixtures, and trial outputs were not changed.

## Criterion decisions

“Pass” means the practical criterion is met on the available evidence; it does not certify unobserved native Word operations. A10's current-file preservation is independently verified, while its no-refresh operation history is explicitly report-based. The 21 items are rubric items, not independent experimental samples.

| Item | Intended criterion | Guided A | Guided B | Control |
| --- | --- | --- | --- | --- |
'''
for id_, criterion, reasoning, lines, artifact_ref in rows:
    short = criterion.replace('|', '\\|')
    md += f'| {id_} | {short} | Pass | Pass | Pass |\n'

md += '''
The exact criterion text, independent reasoning, report line locators for each run, and artifact evidence keys are recorded in [decisions.json](decisions.json). The original rubric has nine A findings plus preservation, four B findings plus the edit requirement, three C findings, and three cross-case requirements.

## Independent document findings

Case A has four actual citation occurrences: two in body paragraphs, one in the Figure 1 caption, and one in substantive footnote 1. Its main list has five entries, its separate Further reading has one, and its embedded library has seven records. Those are different inventories.

At main paragraph 3, `CITATION ValeA` identifies Tamsin Vale's *Alpha Sensor Calibration*, but the cached citation says `(Vale, 2024b)` while the Alpha entry says `2024a`. At paragraph 4, `CITATION ValeB` identifies *Beta Sensor Calibration*, but the cached citation lacks the required `b`. Thus Alpha needs the displayed `a`, and Beta needs the displayed `b`; neither field needs retargeting. The full source records establish the same author/year, and Alpha precedes Beta by the specified title rule. All runs correctly preserve that distinction.

Ng is genuinely cited in `word/footnotes.xml`, footnote ID 1, which is linked from the body. Imani is cited in the Caption paragraph. Marin alone has a displayed main-list entry with no citation in any supplied content. Sato is allowed in the separately labeled Further reading. Lumen exists only as an embedded source record. The `SEQ` figure number, `REF figProcess`, and note marker do not add literature citations.

Case B contains four citation occurrences in the same regions, four main entries, one Further reading entry, and six stored sources. The two Morgan Ellis works correctly use Archive = 2020a and Museum = 2020b in fields, displays, and entries. Paz's footnote and Kline's caption count. Huang is permitted Further reading; Dane is embedded only. There is no citation-related defect under the requested rules.

Case C supplies no field target. `Chen (2023)` has two candidate entries and cannot be uniquely assigned from the wording or titles. Neither Chen entry is confirmed used by that occurrence. Reed has no observed occurrence in the one exported paragraph; omitted material prevents any global-unused conclusion for Reed or either Chen work. No run guesses a target, merges entries, orders deletion, or infers native fields/refresh/style selection from this export.

## Saved artifact verification

The independent checks are reproducible with `inspect_independently.py`; detailed source/field/relationship/paragraph inventories are in `artifact_checks.json`.

| Check against frozen Case B fixture | Guided A | Guided B | Control |
| --- | --- | --- | --- |
| Same 18 package members and order | Pass | Pass | Pass |
| Only `word/document.xml` changed | Pass | Pass | Pass |
| Changed XML equals original bytes with only the exact authorized prose replacement | Pass | Pass | Pass |
| Other 17 member payloads byte-identical | Pass | Pass | Pass |
| All seven complete fields, instructions, delimiters, and cached results unchanged | Pass | Pass | Pass |
| Four citations include caption and real footnote | Pass | Pass | Pass |
| Six source records, tags/GUIDs, relationships, note anchor, and bookmark preserved | Pass | Pass | Pass |
| ZIP CRC and XML parsing succeed; internal relationship targets exist | Pass | Pass | Pass |
| All four supplied input files match frozen fixtures | Pass | Pass | Pass |

All three revised DOCX files are **byte-identical**, with SHA-256 `247b25e0b4b4ec934ca99d4073e88b421e80ef621a1453c8126dd9f426380194`. Case A's input is byte-identical to the fixture in every run, SHA-256 `d45de9aeffce9fdb92ea670a3fd965b846e500d095030d6817f0773392f1ba62`. Case B's original hash is `f3be77c7d27af6797dfbf605ea7225491a847e89db96ee4e8e2887adf1fb8463`.

The exact saved change is `The catalogue containss two registers ` → `The catalogue contains two registers ` before the first citation field. No field result or instruction changes. The ordinary text run, remaining XML bytes, footnote and source parts, style/configuration parts, and relationship parts establish the requested narrow edit without relying on a prose claim that fields were preserved.

Each rendering log records the bundled `soffice` converter. The three page PNG files are byte-identical (SHA-256 `0346b839061d9ae6b35fa761e7671f84c798d686a45370e0efcb4ac59c94403a`). I visually inspected the full representative Guided A page; identical bytes make that inspection applicable to the saved PNGs from the other runs. The word “contains,” both Ellis suffixes, Kline caption, figure cross-reference, four main entries, Huang Further reading, and Paz footnote are readable without observed clipping, overlap, or missing content. This review did not rerender or open a native application.

## Disagreements and findings outside the rubric

There are **no substantive disagreements with the reports and no substantive false positives found**. Three interpretation points prevent unfair deductions:

1. Guided A calls the ValeB visible text ambiguous; Guided B calls it a “visibly ambiguous target.” Each immediately resolves the intended work to Beta through `ValeB` and proposes the correct `2024b`. This is an accurate distinction between inadequate visible disambiguation and known source identity, unlike the genuinely unresolved text-only Chen case.
2. The control's instruction to change a citation result is an exact correction proposal, read alongside its instruction to retain source/field identities, use an appropriate field-aware workflow, and beware of overwritten cached text. It did not change A or recommend replacing fields with plain text.
3. The A/B custom title-alphabetical requirement is not silently imposed as a verified selected style for C. All reports preserve C's unavailable-style boundary while identifying the visible identity problem.

The additional static APA/Version 6 stylesheet observations are supported by the packages and carefully bounded. The reports do not claim an active Word style, full APA compliance, or demand unrelated ordering/typography changes. Their A/B no-missing-target and no-duplicate-work conclusions are supported within these supplied records. The guided reports' statements about absent revision markup and extra content stories are consistent with independent inspection. The control's possible stale/manually changed cache explanation is labeled a possibility and does not become an unsupported causal verdict.

The control does not explicitly say “claim support was not checked,” unlike the guided reports. It makes no claim-support verdict and the requested fictional mapping audit does not require that check. This is a minor reporting omission, with no rubric failure and no evidence for changing the skill. Its counts are less tabular but have identifiable units and stated scope; the lack of an identical ledger layout is not a performance failure.

## Missing checks and limits

No required artifact-level check is missing for the authorized narrow edit. Several outcomes remain untested by design:

'''
for limit in limitations:
    md += '- ' + limit + '\n'

md += '''
All three reports explicitly separate saved package structure and cached displays from native refresh. A successful LibreOffice export and an unchanged package are not evidence that Microsoft Word or a reference-manager integration has refreshed, saved, and reopened correctly. Current input equality also cannot prove that no transient operation ever occurred; that historical statement is reported, not independently witnessed.

## Skill revision and comparative conclusion

Retain the frozen skill unchanged on this evidence. Its existing directions already cover both mapping directions, note/caption coverage, stored-source versus displayed-list distinctions, style evidence, partial exports, narrow editing, and the static/native boundary. Both guided runs apply these distinctions successfully. The control reaches the same practical decisions and produces the same deliverable, so this trial cannot establish incremental benefit, general superiority, or native Word refresh reliability.

The useful result is a passed, narrow transfer/regression check with a successful control. If broader validation is desired, test the unrepresented cases above and observe authorized native refresh/save/reopen separately; those are future tests, not reasons to rewrite a currently passing skill.

## Evidence files

- [decisions.json](decisions.json): every rubric criterion, per-run report locator, outcome, extra-finding review, limits, and revision decision.
- [artifact_checks.json](artifact_checks.json): independently extracted fixture/output evidence and actual comparison results.
- [inspect_independently.py](inspect_independently.py): reproducible static checker used for this assessment.
- [Guided A report](../runs/guided-a/output/report.md), [Guided B report](../runs/guided-b/output/report.md), [control report](../runs/control/output/report.md): assessed reports, unchanged.
- [Representative rendered page](../runs/guided-a/output/rendered-b/page-1.png): visually reviewed; all three saved page PNGs are byte-identical.
'''
(OUT / 'assessment.md').write_text(md)
print(json.dumps({'assessment': str(OUT / 'assessment.md'), 'decisions': str(OUT / 'decisions.json'), 'rubric_items': len(rows), 'per_run': summary['per_run'], 'skill_revision_justified': False, 'incremental_benefit_demonstrated': False}, indent=2))
