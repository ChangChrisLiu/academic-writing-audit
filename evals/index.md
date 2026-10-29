# Evaluation records

[Library](../README.md) · [中文说明](../README.zh-CN.md) · [Contributing](../CONTRIBUTING.md)

Use this index to find the evidence relevant to a proposed change. These are separate development records with different inputs, controls, assessors and operational coverage. They are not a pooled benchmark or a general reliability estimate. A recorded pass means the stated criteria were met in that case; package checks do not establish writing quality.

The linked records preserve their original procedures, complete public outputs, qualifications, failures and manifests. The [original evaluation README](README.md) remains the October 2026 full-audit trial record. This index is maintained as new records are added.

## Argument, revision and language

| Record | What to inspect | Evidence boundary |
| --- | --- | --- |
| [Original full audit](README.md) | Five controls, five guided responses and guided transfer requests; preservation of a coherent motivation paragraph. | Development inputs influenced the skill; author-assessed and not blinded. |
| [Focused skills](library/README.md) | Ten cases with control and guided outputs across story, evidence and integrity tasks. | Controls already handled the core problems; no measured skill advantage. |
| [Natural prose and logic](academic-prose-editing/README.md) | English revision, Chinese audit-only work and paired response/manuscript edits. | Guided fictional cases with a separate assessor; no unguided control. |
| [Professional language](academic-language/README.md) | Terminology, sentence roles and the targeted dataset/buffer case. | Small guided cases; each freeze identifies its tested version. |
| [Concept and language transfer](concept-language-transfer/README.md) | Mathematics, chemistry, economics and qualitative research; valid terminology and correct passages. | Fictional cases testing two entrypoints, with a separate assessor. |
| [Private real-manuscript audit](real-manuscript-audit/README.md) | Public method and assessment summaries, initial findings and regression judgments. | The known manuscript and review materials remain private; this index grants no access to them. |
| [Manuscript structure](manuscript-structure/README.md) | Engineering, qualitative and mathematical writing, plus a title-only request with missing research facts. | Source/text checks; no compiled-page or native Word-layout validation. |
| [Roles and revision integrity](roles-revision-integrity/README.md) | Discipline-specific review, intended repairs, useful shortening and information preservation. | Guided fictional cases with a separate assessor; no unguided control. |
| [Reasoning and expression](reasoning-rhythm/README.md) | Methods, interpretation and mathematical keep/repair decisions; retained optional refinements. | Guided checks; no authorship score or causal effectiveness estimate. |
| [Introduction focus](introduction-focus/README.md) | Destination-aware drafting, detours and reasoning lost through shortening. | Author-assessed fictional cases; initial shortcomings remain visible. |

## Research preparation

| Record | What to inspect | Evidence boundary |
| --- | --- | --- |
| [Literature to story](literature-to-story/README.md) | Independent overlapping investigation, reciprocal review and synthesis handoff. | Closed fictional packets; author assessment, no live retrieval or unguided control. |
| [Gap persistence](gap-persistence/README.md) | Earlier attempts, conditional failures, alternative names, changed constraints and useful replication. | Closed packets with independent investigation, reciprocal review and a separate assessor. |
| [Constructive inquiry](constructive-inquiry/README.md) | Early proposals, supported effects, confounded claims and accurate prose that should remain unchanged. | Two guided runs and separate assessment; no full research-team execution or measured improvement. |

## Responses, references and document operations

| Record | What to inspect | Evidence boundary |
| --- | --- | --- |
| [Response-writing fixtures](reviewer-response-writing/README.md) | Initial requests, evidence packets and expected criteria. | Published fixtures, not executed model trials. |
| [Response-writing transfer](reviewer-response-writing/transfer/README.md) | Cross-domain outputs, scope ambiguities, targeted regressions and assessments. | Guided same-host trials; no unguided control. |
| [Reference integrity](reference-integrity/README.md) | Independent public-reference checks and fictional LaTeX/Word audits. | Retains incomplete Scholar access; does not prove exports, compilation or native refresh. |
| [Reference workflow execution](reference-workflow/README.md) | Source captures, Cite → BibTeX export, LaTeX source changes, build/render evidence and the initial blocked Word attempt. | Operational evidence is scoped to the tested records and artifacts. |
| [Native Word follow-up](word-native-refresh/README.md) | Actual style selection, field refresh, save, reopen, structure checks and page evidence. | One constructed fixture; same operator and assessor, no general integration claim. |
| [Word citation transfer](word-citation-transfer/README.md) | Guided and control reports, citation mappings, footnotes, captions and preserved fields. | The control also passed; static/package checks do not establish native refresh for these cases. |

## Add or verify a record

The [repository-consolidation record](repository-consolidation/README.md) covers shorter entrypoints, centralized maintenance with standalone resource copies, documentation routing, three fresh-context regression runs and portable tool tests. It preserves the original evidence and records a reused-fixture logistics mismatch. Structural size reduction is not a writing-quality result.

For a behavior change, freeze the inputs and tested skill version before execution, retain full outputs and disagreements, and add a separate record with its own scope and limitations. Link it here instead of expanding both library READMEs with repeated test summaries. Follow the [contribution workflow](../CONTRIBUTING.md).

Run `python3 scripts/validate.py` from a full Git clone to check repository structure and recorded hashes. A manifest's `source_git_commit` resolves its top-level files at that revision; a `skill_versions` entry uses its own `directory` and optional `git_commit`. Unpinned paths resolve in the current checkout. Missing Git history is a verification gap, not evidence of a hash mismatch. Keep historical expected hashes unchanged when pinning a tested version for later maintenance.

Structural validation does not rerun these trials, establish source authenticity, inspect a rendered document or measure the effect of a writing rule. The [validator tests](../scripts/test_validate.py) exercise maintenance failures in temporary repositories.
