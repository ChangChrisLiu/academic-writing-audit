# Guides and skill catalog · 使用指南与 skill 目录

[Home](../README.md) · [中文说明](../README.zh-CN.md) · [Install](../README.md#install) · [Evaluation records](../evals/index.md)

Choose a task guide for explanation and examples, then load the skill that matches your current problem. The installable instructions are written in English. The practical guides are in Chinese except for the English field guide. Every skill includes the local references and license it needs to work independently.

先按当前任务选择指南，再调用相应 skill。指南解释判断方法与使用场景，`skills/` 中的文件提供 agent 可直接执行的指令。局部问题不需要加载整套库；已经清楚、准确的表达可以原样保留。

## Choose a guide · 选择指南

| Task / 任务 | Guide | What it covers / 主要内容 |
| --- | --- | --- |
| Investigate an idea / 从想法开始 | [研究准备](research-preparation.md) · 中文 | 领域调查、gap 的历史与约束、独立核查、证据综合及写作交接 |
| Draft or restructure / 起草或重组 | [论文结构与写作](manuscript-guide.md) · 中文 | 投稿对象、摘要与引言、关联文献、方法、结果和 LaTeX/Word 交付 |
| Improve a passage / 修改段落 | [自然表达与逻辑审查](prose-guide.md) · 中文 | 概念准确、专业用词、推理承接、句式、标点与冗余 |
| Audit or compare drafts / 审查与版本对照 | [专业角色与修改前后对照](revision-guide.md) · 中文 | 学科与研究设计适配、逻辑预期、原问题是否解决、信息是否保留 |
| Respond to reviewers / 审稿回复 | [审稿回复与正文写作](rebuttal-guide.md) · 中文 | 意见覆盖、证据范围、回复格式、修改状态与正文边界 |
| Verify references / 文献核验 | [文献真实性与引用](reference-guide.md) · 中文 | 双 agent 核验、Scholar BibTeX、Word 引用、可复用记录与成品验证 |
| Recognize a specific failure / 查找具体问题 | [Problem → repair field guide](field-guide.md) · English | Fictional examples and focused prompts for recurring editorial problems |

For an unfamiliar manuscript, start with the full audit. For a known problem, select one focused skill below. After a substantive revision, compare the changed meaning and read the surrounding argument. Final source, render, and publication checks are separate tasks.

从想法形成初稿时，依次使用研究准备与章节写作指南。已有完整稿件时，从整体审查开始；收到审稿意见时，结合回复指南和前后版本对照。详细试用方法、结果和局限保存在[验证记录](../evals/index.md)，宣传素材保存在[media kit](../assets/README.md)。

## Skill catalog

The 18 folders below are independently installable. The [installation instructions](../README.md#install) cover the Skills CLI, manual copying, and direct Markdown use.

| When you encounter… | Skill | What it helps you produce |
| --- | --- | --- |
| Generic prose or disconnected manuscript sections | [research-manuscript-writing](../skills/research-manuscript-writing/SKILL.md) | A research-grounded draft with distinct section roles and LaTeX or Word delivery. |
| A paper needing a complete editorial diagnosis | [academic-writing-audit](../skills/academic-writing-audit/SKILL.md) | A structured scientific and editorial audit. |
| Unclear terminology, awkward phrasing, tangled sentences, or repetition | [academic-prose-editing](../skills/academic-prose-editing/SKILL.md) | Natural paragraphs with clear reasoning and preserved scientific meaning. |
| A missing bridge between problem, contribution, and evidence | [scientific-story-audit](../skills/scientific-story-audit/SKILL.md) | A connected argument that preserves the contribution's scope. |
| Rebuttal-like prose, repeated assurances, or piles of caveats | [nondefensive-writing](../skills/nondefensive-writing/SKILL.md) | Direct explanations with necessary boundaries intact. |
| A paper list, false categories, or an unsupported “first” | [related-work-synthesis](../skills/related-work-synthesis/SKILL.md) | A connected literature narrative that develops the research question without preset categories or default self-comparison. |
| A conclusion stronger than its supporting observation | [claim-evidence-audit](../skills/claim-evidence-audit/SKILL.md) | Claims matched to the study and inference that support them. |
| Ambiguous baselines, ablations, budgets, or data eligibility | [experiment-comparison-audit](../skills/experiment-comparison-audit/SKILL.md) | Operational definitions of what was actually compared. |
| Results that merely repeat numbers or over-explain mechanisms | [results-interpretation](../skills/results-interpretation/SKILL.md) | Useful interpretation with attribution and uncertainty in scope. |
| A formula or appendix pointer that never explains the operation | [method-definition-audit](../skills/method-definition-audit/SKILL.md) | Plain definitions consistent with the formal procedure. |
| Arrows, captions, and endpoints that imply different things | [figure-caption-audit](../skills/figure-caption-audit/SKILL.md) | Aligned visual semantics, labels, and captions. |
| Reviewer comments becoming scattered or repetitive edits | [reviewer-comment-triage](../skills/reviewer-comment-triage/SKILL.md) | Current-text diagnosis and a focused reader-facing repair. |
| A rebuttal or response letter needing direct, supported answers | [reviewer-response-writing](../skills/reviewer-response-writing/SKILL.md) | Concise or point-by-point replies, with evidence and verified revision locations. |
| A shorter revision that may have lost scientific meaning | [revision-integrity-audit](../skills/revision-integrity-audit/SKILL.md) | Before-and-after judgments on the intended repair, logical dependencies, and information preservation. |
| Suspected invented references or mismatched title, authors, year, or venue | [reference-authenticity-audit](../skills/reference-authenticity-audit/SKILL.md) | Two independent Google Scholar-first source records and reconciled field-level findings. |
| Duplicate papers, inconsistent BibTeX, or citation-key collisions | [latex-bibliography-audit](../skills/latex-bibliography-audit/SKILL.md) | Scholar Cite → BibTeX provenance, work/version identity, and safe key repairs. |
| Word citations and reference lists that do not match | [word-citation-audit](../skills/word-citation-audit/SKILL.md) | Style identification and citation-to-list plus list-to-citation checks, with field preservation. |
| An old PDF, uncertain compilation, or unclear submission state | [manuscript-release-check](../skills/manuscript-release-check/SKILL.md) | A precise verification record and usable handoff. |
