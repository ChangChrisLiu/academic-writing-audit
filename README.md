<p align="center">
  <img src="assets/hero.jpg" alt="Academic Writing Audit — Clear arguments. Supported claims. Careful edits." width="100%">
</p>

<h1 align="center">Academic Writing Audit</h1>

<p align="center"><strong>18 portable agent skills for scientific manuscripts and reviewer responses.</strong><br>
Reconstruct the argument, check the evidence, and change only what needs changing.</p>

**中文简介｜学术论文写作与审稿回复 Skills**

提供 **18 个可独立使用的 AI agent skills**，覆盖 **学术论文写作、逻辑与证据审查、专业术语和句子检查、去防御性写作，以及审稿意见回复、response letter 和 rebuttal**。先理解研究问题，再组织摘要、倒三角引言、关联文献综述、方法与学科适配的结果和结尾，支持 **LaTeX 与 Word**。新增 **Google Scholar 文献真实性双 agent 交叉验证、Cite → BibTeX 校对与去重、Word 引用格式和正文与文末参考文献双向核对**。

根据研究设计限定 **reviewer 与 editor 的专业角色**，检查预期论证和当前内容的差距。通过 **修改前后对照** 防止过度压缩丢失逻辑和信息，保留有效纠错与正常专业术语。“去 AI 味”落实为论证展开、自然承接、表达节奏、句式简化和冗余检查，生成段落默认不用解释性冒号或句中破折号，保留术语连字符及技术符号。回复信回应审稿人，正文直接解释研究。通用 Markdown 指令可供不同 agent 使用。

初稿新增[领域调研与故事线准备](docs/research-preparation.md)。从研究想法出发，按学科检索和评价文献，结合近期进展、基础研究与反例，由多个 agent 独立调查并交叉核对，再形成一条清晰主线。充分思考留在研究准备中，正文保持简洁、连贯、不防御。

对明显的研究 gap，先查为什么仍未解决，包括既往尝试、失败条件、实际约束和其他名称下已有的解法。说明重新尝试的依据，区分有证据的变化与待验证的假设；不能把检索空白写成无人尝试，也不能把一次失败扩大成普遍不可行。

[中文使用说明](README.zh-CN.md) · [文献真实性与引用核对](docs/reference-guide.md) · [专业角色与前后对照](docs/revision-guide.md) · [论文结构与写作](docs/manuscript-guide.md) · [自然表达与逻辑审查](docs/prose-guide.md) · [审稿回复与正文写作指南](docs/rebuttal-guide.md) · [安装方法](#install)

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-943D32"></a>
  <a href="https://agentskills.io/specification"><img alt="Format: Agent Skills" src="https://img.shields.io/badge/format-Agent_Skills-444444"></a>
  <a href="README.zh-CN.md"><img alt="中文说明" src="https://img.shields.io/badge/docs-中文-786957"></a>
</p>

<p align="center">
  <a href="#choose-a-skill">Choose a skill</a> ·
  <a href="#install">Install</a> ·
  <a href="docs/field-guide.md">Problem → repair</a> ·
  <a href="evals/library/README.md">Trial records</a> ·
  <a href="assets/README.md">Media kit</a>
</p>

---

A manuscript can become shorter and still lose its argument. A cautious sentence can be essential. A convincing result can support the full system without identifying which component caused the gain.

This library turns those recurring editorial decisions into small, reusable workflows. Use the full audit for an unfamiliar manuscript, or load one focused skill when the problem is already clear. Every skill accepts **keep as written** as a useful outcome.

## Start here

| Your task | Start with | Ask for |
| --- | --- | --- |
| Draft or restructure a paper from study materials | [Research manuscript writing](skills/research-manuscript-writing/SKILL.md) | A concise argument grounded in the actual question, evidence, discipline, and document format. |
| Understand what needs attention in a whole paper | [Academic writing audit](skills/academic-writing-audit/SKILL.md) | Prioritized findings, evidence, and passages to preserve. |
| Repair a specific writing problem | [Choose a focused skill below](#choose-a-skill) | A bounded replacement or patch with a reason for each change. |
| Write a rebuttal or revision response letter | [Reviewer response writing](skills/reviewer-response-writing/SKILL.md) | Evidence-grounded replies, accurate change status, and separately written manuscript edits. |
| Compare a shortened or revised draft with its source | [Revision integrity audit](skills/revision-integrity-audit/SKILL.md) | Concern resolution and preserved reasoning, with justified keep and repair decisions. |
| Verify references or reconcile a bibliography | [Reference authenticity](skills/reference-authenticity-audit/SKILL.md), [LaTeX bibliography](skills/latex-bibliography-audit/SKILL.md), or [Word citations](skills/word-citation-audit/SKILL.md) | Two independent Scholar-first checks, intended-version BibTeX, or bidirectional citation matching. |
| Check the final manuscript and handoff | [Manuscript release check](skills/manuscript-release-check/SKILL.md) | The verified source, build, render, and publication state. |

```text
Use $academic-writing-audit to review this manuscript.
First audit its argument, evidence boundaries, comparisons, and definitions.
Do not rewrite the file. Identify sound passages that should stay unchanged.
```

## Choose a skill

Each folder is independently installable. You do not need to load the whole collection.

| When you encounter… | Skill | What it helps you produce |
| --- | --- | --- |
| Generic prose or disconnected manuscript sections | [research-manuscript-writing](skills/research-manuscript-writing/SKILL.md) | A research-grounded draft with distinct section roles and LaTeX or Word delivery. |
| A paper needing a complete editorial diagnosis | [academic-writing-audit](skills/academic-writing-audit/SKILL.md) | A structured scientific and editorial audit. |
| Unclear terminology, awkward phrasing, tangled sentences, or repetition | [academic-prose-editing](skills/academic-prose-editing/SKILL.md) | Natural paragraphs with clear reasoning and preserved scientific meaning. |
| A missing bridge between problem, contribution, and evidence | [scientific-story-audit](skills/scientific-story-audit/SKILL.md) | A connected argument that preserves the contribution's scope. |
| Rebuttal-like prose, repeated assurances, or piles of caveats | [nondefensive-writing](skills/nondefensive-writing/SKILL.md) | Direct explanations with necessary boundaries intact. |
| A paper list, false categories, or an unsupported “first” | [related-work-synthesis](skills/related-work-synthesis/SKILL.md) | Connected literature threads that explain prior studies without default self-comparison. |
| A conclusion stronger than its supporting observation | [claim-evidence-audit](skills/claim-evidence-audit/SKILL.md) | Claims matched to the study and inference that support them. |
| Ambiguous baselines, ablations, budgets, or data eligibility | [experiment-comparison-audit](skills/experiment-comparison-audit/SKILL.md) | Operational definitions of what was actually compared. |
| Results that merely repeat numbers or over-explain mechanisms | [results-interpretation](skills/results-interpretation/SKILL.md) | Useful interpretation with attribution and uncertainty in scope. |
| A formula or appendix pointer that never explains the operation | [method-definition-audit](skills/method-definition-audit/SKILL.md) | Plain definitions consistent with the formal procedure. |
| Arrows, captions, and endpoints that imply different things | [figure-caption-audit](skills/figure-caption-audit/SKILL.md) | Aligned visual semantics, labels, and captions. |
| Reviewer comments becoming scattered or repetitive edits | [reviewer-comment-triage](skills/reviewer-comment-triage/SKILL.md) | Current-text diagnosis and a focused reader-facing repair. |
| A rebuttal or response letter needing direct, supported answers | [reviewer-response-writing](skills/reviewer-response-writing/SKILL.md) | Concise or point-by-point replies, with evidence and verified revision locations. |
| A shorter revision that may have lost scientific meaning | [revision-integrity-audit](skills/revision-integrity-audit/SKILL.md) | Before-and-after judgments on the intended repair, logical dependencies, and information preservation. |
| Suspected invented references or mismatched title, authors, year, or venue | [reference-authenticity-audit](skills/reference-authenticity-audit/SKILL.md) | Two independent Google Scholar-first source records and reconciled field-level findings. |
| Duplicate papers, inconsistent BibTeX, or citation-key collisions | [latex-bibliography-audit](skills/latex-bibliography-audit/SKILL.md) | Scholar Cite → BibTeX provenance, work/version identity, and safe key repairs. |
| Word citations and reference lists that do not match | [word-citation-audit](skills/word-citation-audit/SKILL.md) | Style identification and citation-to-list plus list-to-citation checks, with field preservation. |
| An old PDF, uncertain compilation, or unclear submission state | [manuscript-release-check](skills/manuscript-release-check/SKILL.md) | A precise verification record and usable handoff. |

For concrete failure patterns and sample requests, see the [field guide](docs/field-guide.md).

## What a careful edit looks like

**Draft**

> We emphasize that incomplete measurements were not quietly discarded. No one should infer that our system guarantees reliable field operation.

**Supplied evidence** — Incomplete measurements receive an abstention, remain in the denominator, and have no concentration estimate. Field operation was not evaluated.

**Revision**

> Incomplete measurements received an abstention rather than a concentration estimate and remained in the evaluation denominator. The study did not evaluate field operation.

The accusation and reassurance disappear. The operative rule, denominator, and study boundary remain. A clear preceding motivation paragraph stays as written.

## Understand the study before drafting

Use [research-manuscript-writing](skills/research-manuscript-writing/SKILL.md) when drafting or restructuring sections from research materials. It first establishes the concrete question, motivation, contribution, and evidence. Missing research facts remain dependencies instead of becoming generic background or invented results.

An idea-led first draft begins with [literature investigation and story development](skills/research-manuscript-writing/references/literature-to-story.md). Two or more agents independently examine overlapping questions, then cross-review evidence before synthesis. Learn problem framing from introductions and related work, inspect pivotal methods and findings, and let closest prior solutions or contrary evidence change the initial story. Recent work matters alongside foundational and less visible scholarship. Source records distinguish what was read, bibliographic identity, methodological support and unresolved questions. Local edits reuse the relevant evidence without restarting field research.

For an apparently obvious gap, investigate earlier attempts and why the question may remain open. Prior failure is a search priority, not an assumed fact. Check successful solutions under other names, preserve the conditions of negative findings, and distinguish a demonstrated enabling change from a proposed one. A useful replication can justify revisiting a question without inventing novelty. Keep unknown causes and research-planning decisions in the preparation record.

The abstract follows a motivated problem-to-result progression. Before drafting an introduction, establish the target conference or journal, audience, and supported submission priorities. Build one narrowing argument from relevant progress through gap and motivation to contribution. Conference framing may integrate the gap and motivation compactly; journal framing makes the unresolved issue, its consequence, and the rationale explicit, subject to the actual venue requirements. Audits remove detours and explanation without a distinct reasoning function while preserving necessary bridges. The literature review develops two or three connected threads from that argument and explains prior studies, without default taxonomies or repeated comparisons with the present paper. Methods follow operational or analytic dependencies, while findings and endings fit the study design and supplied disciplinary conventions.

The default is concise connected prose, not contribution lists, module catalogues, or table narration. Required structured abstracts, formal algorithms, and author-selected formats remain supported. [The writing guide](docs/manuscript-guide.md) explains the section logic and LaTeX/Word boundaries.

## Match the review to the research, then compare revisions

The full audit assigns reviewer and editor responsibilities by subfield, study design, audience, evidence access, and the decision required. It compares what the argument needs to establish with what the current text actually establishes, distinguishing actual reviewer requests from inferred reader needs. A proof, an experimental comparison, and an interpretive account require different judgments. For general editorial review, separate agents are optional; disagreements are resolved through source evidence rather than voting. The dedicated reference-authenticity and idea-led preparation workflows use independent agents for their specified checks.

Use [revision-integrity-audit](skills/revision-integrity-audit/SKILL.md) after shortening or restructuring. It checks both whether the intended concern was resolved and whether valid reasoning and information survived. Keep supported corrections, useful compression, and verified relocation. Restore missing meaning without restoring an entire old paragraph. See the [Chinese role and revision guide](docs/revision-guide.md).

```text
Use $revision-integrity-audit to compare these manuscript versions.
Check the intended repair and any loss of motivation, definitions, conditions,
evidence links, or interpretation. Preserve valid corrections and useful shortening.
Audit only. Give consequential differences and the smallest justified action.
```

## Natural prose and clear reasoning

Use [academic-prose-editing](skills/academic-prose-editing/SKILL.md) to check precise terminology, professional word choice, natural word combinations, sentence complexity, local inference, and repeated meaning. Preserve stable terminology, necessary conditions, and useful motivation. Shorter sentences are helpful when they reduce the reader's burden, not when they erase the argument.

When individually correct sentences still feel mechanical, check how the argument develops. The prose skill traces what the reader learns, why a scientific choice follows, and how evidence qualifies an interpretation. Sentence and paragraph variation follow emphasis and explanatory need, while useful parallelism and author voice remain intact. It does not fabricate an author's deliberations or prescribe alternating sentence lengths. See [reasoning and rhythm](skills/academic-prose-editing/references/reasoning-and-rhythm.md).

The concept and language pass first resolves what an expression denotes, its scope, and any property or mechanism its name implies. It distinguishes a conceptual error, awkward expression of a valid concept, unresolved meaning, and an already correct passage. Repairs preserve units, conditions, disciplinary distinctions, and evidential force. Valid specialist terms, disciplinary metaphors, and defined new concepts remain intact. An unfamiliar word is not automatically an error, and a fluent synonym is not automatically equivalent.

Defined study labels are checked against their operations and context. An ambiguous shorthand may need a gloss without indicating a scientific error. The audit itself must also stay source-grounded and must not introduce an unreported mechanism or mathematical property while explaining a finding.

Generated prose defaults to connected paragraphs without explanatory colons or sentence-interrupting dashes. Compound-word hyphens, scientific notation, ratios, ranges, URLs, exact quotations, and required templates remain intact. This is a configurable editorial preference. It is not an authorship test, and author or venue instructions take precedence. Each focused skill carries the core convention so it can work independently.

```text
Use $academic-prose-editing on this passage.
Check precise terms, natural word combinations, logic, sentence structure, and repetition.
Use connected paragraphs without explanatory colons or sentence-interrupting dashes.
Keep compound hyphens, notation, exact quotations, and scientific conditions.
Preserve sound passages and explain material changes briefly.
```

See the [Chinese prose guide](docs/prose-guide.md) for examples and the distinction between redundant repetition and useful restatement.

## Reviewer responses and manuscript prose

Use the same evidence for two different purposes:

| Deliverable | Its job | Fictional example, after the edit has been checked |
| --- | --- | --- |
| Rebuttal / response letter | Answer the concern and identify the action or remaining gap. | “We have added the comparator's operational definition to Methods, under ‘Comparators.’” |
| Manuscript | Explain the research to a reader who has never seen the review. | “The comparator uses a predetermined linear score with fixed group multipliers and fits one model.” |

The new skill draws on practical author-response work and subsequent manuscript audits: group shared questions without losing individual requests, define the actual comparison, separate studies, bound attribution, and verify promised revisions. Public examples are fictional. A clear reply does not substitute for a clear revised paper.

```text
Use $reviewer-response-writing to draft this rebuttal within the supplied
venue rules. Map every comment to an answer and supporting evidence.
Distinguish completed changes from proposals. Put any proposed manuscript
text in a separate block, written for readers without reviewer references.
```

See the [中文回复写作指南](docs/rebuttal-guide.md) and [paired examples](skills/reviewer-response-writing/references/manuscript-boundary.md).

## Verify references and citation identity

Use [reference-authenticity-audit](skills/reference-authenticity-audit/SKILL.md) to have two agents independently check the same references, each beginning with Google Scholar and verifying the complete title, author list, publication year, venue, and intended version. Each also checks primary publication evidence even when Scholar looks complete. Reconcile their evidence after both finish. A missing search result is unresolved evidence, and a real paper with the wrong year is a metadata error. Neither implies a fabricated work.

Use [latex-bibliography-audit](skills/latex-bibliography-audit/SKILL.md) to retrieve the intended record's Cite → BibTeX export and reconcile duplicate publications and citation keys across the project. Retain raw export provenance and separately intended versions. Keep verified existing fields such as a DOI in the working bibliography even when the export omits them; record their supplemental sources. Use [word-citation-audit](skills/word-citation-audit/SKILL.md) to establish the required style, then match every citation to its reference and every reference to its citations, including the inspected captions, tables, notes, and appendices. Preserve live citation-manager fields.

A reusable reference ledger carries original entries, occurrence locations, version identity, field provenance, and check status across the three workflows. Unchanged identities do not need new searches merely because a citation key or style changes. If a search tool cannot read Scholar, try an available authorized ordinary browser route and record the actual access outcome.

Authenticity, formatting, reference identity, and support for the cited claim are separate judgments. Inaccessible Scholar records, uncertain styles, and incomplete document coverage remain explicit. See the [中文文献核验与引用指南](docs/reference-guide.md).

## Install

[Download a portable release bundle](https://github.com/ChangChrisLiu/academic-writing-audit/releases/latest), or install selected skills below.

The library uses the [Agent Skills format](https://agentskills.io/specification): a Markdown entrypoint, optional local references, and a license in each skill folder. The skills require no particular model or agent provider. The reference-authenticity workflow specifically requires Google Scholar access and two independent agents; LaTeX canonical exports require Scholar Cite → BibTeX access. Clients without these capabilities can report partial findings but cannot claim those steps complete. Client discovery and model behavior can differ.

### With the Skills CLI

The optional [Skills CLI](https://github.com/vercel-labs/skills) supports installation into multiple agent clients. From your project directory:

```sh
# Browse the available skills without installing.
npx skills add ChangChrisLiu/academic-writing-audit --list

# Install one focused skill; choose the target agent when prompted.
npx skills add ChangChrisLiu/academic-writing-audit --skill nondefensive-writing

# Install the collection for Codex in this project.
npx skills add ChangChrisLiu/academic-writing-audit --skill '*' -a codex
```

Add `-g` for a user-wide installation. Review the selected destination before replacing an existing skill.

### Manual installation

Copy the desired folder from `skills/` into your client's configured skills directory. Keep its references and `LICENSE` together. `agents/openai.yaml` is optional Codex display metadata.

For user-wide Codex installation, run from a local clone:

```sh
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skill_root"
test ! -e "$skill_root/academic-writing-audit" && \
  cp -R skills/academic-writing-audit "$skill_root/academic-writing-audit"
```

This copy preserves any existing installation. Substitute another folder name to install a focused skill. Open a new agent session if the installation is not discovered in the current one.

### Any agent that can read Markdown

Supply the skill's `SKILL.md` and any referenced files, then ask:

```text
Read the attached nondefensive-writing/SKILL.md and apply it to the passage.
Revise only this passage. Preserve the study endpoint, denominator,
algorithmic conditions, and any coherent motivation. Explain the changes.
```

## A small, deliberate workflow

<p align="center">
  <img src="assets/workflow.jpg" alt="Understand the question and contribution; check claims and comparisons; revise only justified changes; verify the source and final render." width="540">
</p>

1. **Understand** the current source and the author's argument before consulting old judgments.
2. **Check** consequential claims against the right evidence and experimental setting.
3. **Revise** only within the requested scope, preserving definitions and valid reasoning.
4. **Verify** what the task requires, distinguishing source inspection from compilation, render review, and external publication.

An audit returns findings. An authorized revision proceeds with bounded edits. A grammar-only request stays narrow.

## Evidence and maintenance

The repository includes fictional cases, semantic rubrics, and complete control/guided responses. The [original full-audit trials](evals/README.md) observed better preservation of a coherent paragraph in this small development sample. The [focused-skill trials](evals/library/README.md) also record cases where the controls already handled the core issues correctly. Neither establishes broad or cross-model effectiveness.

The response-writing skill has [ten guided executions across seven fictional domains](evals/reviewer-response-writing/transfer/README.md), including separate assessment agents. No reviewer-facing manuscript voice was found in these outputs. Two initial evidence-scope ambiguities prompted a targeted clarification and fresh regression runs. Full outputs, the original assessment, and its prompted reassessment are preserved. These same-host trials have no unguided controls and do not establish universal or cross-model effectiveness.

The prose update has [three independent-context guided trials](evals/academic-prose-editing/README.md) covering English revision, Chinese audit-only work, and paired response/manuscript edits. A separate assessor found all 16 applicable checks satisfied, including technical punctuation preservation and the response/manuscript boundary. These cases are limited behavioral checks without an unguided control.

The professional-language update has [three additional guided trials](evals/academic-language/README.md), including a targeted dataset/buffer naming check. The saved outputs retain legitimate specialist terms, correct misleading names and sentence roles, and preserve unresolved meanings as author questions. These small fictional cases do not establish general effectiveness.

The generalized concept checks have [four further independent-context trials](evals/concept-language-transfer/README.md) in mathematics, chemistry, economics, and qualitative research. A separate assessor passed all 24 judgments and found no unjustified alteration of valid terms, defined concepts, or correct passages. These fictional same-host cases test two skill entrypoints and do not establish universal reliability.

A [private real-manuscript audit](evals/real-manuscript-audit/README.md) also examines terminology and the manuscript/response boundary on a complete known project. Its initial assessment found two local classification or paraphrase problems, motivating narrow rule refinements. Two fresh regression audits received 12 passing dimension judgments, with one minor presentation caveat retained in the record. The public record reports the method and bounded findings; raw manuscript and review materials remain private.

The [manuscript-structure trials](evals/manuscript-structure/README.md) cover engineering, qualitative research, mathematical literature, and a title-only request with missing research facts. Independent assessments passed 16 applicable initial judgments and 10 regression judgments, with two optional editorial preferences preserved. The format checks concern LaTeX source and paste-ready Word text, not compiled pages or native Word layout.

The [role and revision-integrity trials](evals/roles-revision-integrity/README.md) cover robotics inspection, numerical analysis, and organizational ethnography. A separate assessor passed all 21 criteria, with two optional wording issues retained. The outputs distinguish actual concern resolution from preservation, accept valid corrections and shortening, and retain legitimate specialist terminology. These fictional guided checks have no unguided control and do not establish universal transfer.

The [reasoning and expression trials](evals/reasoning-rhythm/README.md) cover engineering methods, Chinese ecological interpretation, and mathematical keep/repair decisions. Independent assessments passed 15 initial and five regression criteria. Optional expression and concision preferences remain public; one initially noted phrase persists after a narrow clarification, so the record does not claim that the refinement eliminated it. These guided checks have no unguided control or authorship score.

The [reference-integrity trials](evals/reference-integrity/README.md) include two independent live checks of the same public references and one fictional LaTeX/Word format audit. Both live checks retained the incomplete Scholar-access status; format checks distinguish duplicates, version differences, key collisions, and partial document coverage. These records do not establish successful Scholar exports, compiled LaTeX, or native Word validation.

The [reference-workflow execution checks](evals/reference-workflow/README.md) add two completed independent Scholar-first and primary-source checks, an actual Cite → BibTeX export, and a compiled/rendered LaTeX duplicate repair that retains a verified DOI omitted from the export. That record retains the initial blocked Word attempt. The [native Word follow-up](evals/word-native-refresh/README.md) completed refresh, save, and reopen verification with APA Sixth Edition selected. Both body/table citations match their two bibliography entries, and all three native fields and both source identities remain intact. This constructed fixture does not validate other citation-manager integrations or establish general reliability.

The [Word citation transfer checks](evals/word-citation-transfer/README.md) add two independent guided audits and a no-citation-skill control covering same-author/year labels, real footnotes, captions, uncited entries, and partial exports. A separate agent assessed their reports and actual files. All three preserved the seven fields during a narrow prose edit and reached the expected mapping decisions. The control also passed, so these small trials establish no measured skill advantage. The skill instructions were retained unchanged.

The [introduction focus checks](evals/introduction-focus/README.md) cover destination-aware conference/journal drafting, a missing destination, an archival-research detour, and a lost reasoning bridge after shortening. Three fresh-context executions include a targeted drafting regression after the initial journal draft repeated an established explanation. The author assessment retains that initial shortcoming and an optional wording refinement. These fictional checks have no unguided control or independent assessor.

The [literature-to-story checks](evals/literature-to-story/README.md) exercise independent overlapping investigation, reciprocal review and writing handoff on fictional robotics and social-history packets. Cross-review corrects a citation-to-intellectual-dependence overclaim. A fresh synthesis regression follows a narrow repair after the first writer placed a project-readiness question in manuscript prose. The complete records retain both shortcomings. These author-assessed, closed-packet checks do not test live retrieval and have no unguided control.

The [gap-persistence checks](evals/gap-persistence/README.md) use five fictional research cases and a grammar-only control. Two independent investigations, reciprocal reviews and a separate assessor examine conditional failures, alternative terminology, changed conditions, unknown history and useful replication, including the boundary between preparation notes and manuscript prose. The records are closed-packet development evidence, with no live retrieval or unguided control.

The skills support reasoning and editing; the quality of a conclusion still depends on the sources and evidence available to the agent. Read [CONTRIBUTING.md](CONTRIBUTING.md) to propose an observed failure, a small repair, and a regression case.

```text
skills/       18 standalone skills, optional examples, and client metadata
docs/         Problem patterns and practical task prompts
evals/        Synthetic cases, rubrics, observed responses, and manifests
assets/       Generated promotional artwork, web copies, and exact prompts
```

## License and artwork

[MIT](LICENSE). Each skill includes its own license copy. Only generic guidance and fictional or authorized examples belong here.

The three promotional images were made with OpenAI's built-in GPT image-generation tool. They illustrate the editorial workflow; they are not research figures. Download the originals and web copies from the [media kit](assets/README.md), with the [generation prompts](assets/prompts.md).
