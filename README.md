<p align="center">
  <img src="assets/hero.jpg" alt="Academic Writing Audit — Clear arguments. Supported claims. Careful edits." width="100%">
</p>

<h1 align="center">Academic Writing Audit</h1>

<p align="center"><strong>18 portable agent skills for scientific manuscripts and reviewer responses.</strong><br>
Reconstruct the argument, check the evidence, and change only what needs changing.</p>

**中文简介｜学术论文写作与审稿回复 Skills**

提供 **18 个可独立使用的 agent skills**，覆盖研究准备、论文写作、逻辑与证据审查、概念与自然表达、审稿回复，以及 LaTeX 和 Word 文献核对。先理解研究，再根据证据组织简洁连贯的论述；保留正常专业术语、必要条件、推理桥梁和已经清楚的表达。理性调研与批判性思考帮助形成判断，正文直接讲清研究，回复信回应审稿问题。

[中文使用说明](README.zh-CN.md) · [完整指南与 skill 目录](docs/README.md) · [安装方法](#install)

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-943D32"></a>
  <a href="https://agentskills.io/specification"><img alt="Format: Agent Skills" src="https://img.shields.io/badge/format-Agent_Skills-444444"></a>
  <a href="README.zh-CN.md"><img alt="中文说明" src="https://img.shields.io/badge/docs-中文-786957"></a>
</p>

<p align="center">
  <a href="#choose-a-skill">Choose a skill</a> ·
  <a href="#install">Install</a> ·
  <a href="docs/README.md">Guides</a> ·
  <a href="evals/index.md">Evaluation records</a> ·
  <a href="assets/README.md">Media kit</a>
</p>

A manuscript can become shorter and still lose its argument. A cautious sentence can be essential. A convincing result can support the full system without identifying which component caused the gain.

This library turns recurring editorial decisions into reusable workflows. It follows the actual research question, study design, evidence, and intended readers. Every skill accepts **keep as written** as a useful outcome.

## Choose a skill

Start with the task you have. Each skill is independently installable; a focused edit does not require loading the whole collection.

| Your task | Start with |
| --- | --- |
| Investigate an idea, draft, or restructure a paper | [Research manuscript writing](skills/research-manuscript-writing/SKILL.md) and the [research preparation guide](docs/research-preparation.md) |
| Diagnose a whole manuscript | [Academic writing audit](skills/academic-writing-audit/SKILL.md) |
| Repair terminology, reasoning, sentences, or repetition | [Academic prose editing](skills/academic-prose-editing/SKILL.md), or a [focused skill](docs/README.md#skill-catalog) |
| Write a rebuttal or response letter | [Reviewer response writing](skills/reviewer-response-writing/SKILL.md) |
| Compare an original and revised draft | [Revision integrity audit](skills/revision-integrity-audit/SKILL.md) |
| Verify references or reconcile citations | [Reference guide](docs/reference-guide.md), with separate authenticity, LaTeX, and Word skills |
| Check the final manuscript and handoff | [Manuscript release check](skills/manuscript-release-check/SKILL.md) |

The [guide index](docs/README.md) contains all 18 skills and practical guides. The [field guide](docs/field-guide.md) provides fictional problem-and-repair examples.

```text
Use $academic-writing-audit to review this manuscript.
First audit its argument, evidence boundaries, comparisons, and definitions.
Do not rewrite the file. Identify sound passages that should stay unchanged.
```

## What a careful edit looks like

**Draft**

> We emphasize that incomplete measurements were not quietly discarded. No one should infer that our system guarantees reliable field operation.

**Supplied evidence** — Incomplete measurements receive an abstention, remain in the denominator, and have no concentration estimate. Field operation was not evaluated.

**Revision**

> Incomplete measurements received an abstention rather than a concentration estimate and remained in the evaluation denominator. The study did not evaluate field operation.

The accusation and reassurance disappear. The operative rule, denominator, and study boundary remain. A clear preceding motivation paragraph stays as written.

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

Each complete skill folder includes local copies of the shared resources it needs and does not depend on another installed skill.

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

[Evaluation records](evals/index.md) preserve fixtures, rubrics, complete outputs, failures, assessments, and follow-up checks. They include small control/guided comparisons, guided development trials, and checks of actual LaTeX and Word artifacts. Some controls already passed the core checks. These records support only the reported observations; they do not establish broad or cross-model effectiveness.

To contribute, report an observed failure, propose the smallest useful repair, and preserve a regression case. See [CONTRIBUTING.md](CONTRIBUTING.md).

| Directory | Contents |
| --- | --- |
| [skills/](skills/) | 18 standalone skills with local references, licenses, and optional client metadata |
| [shared/](shared/) | Canonical prose and reference-ledger resources, with local copies bundled in skills for standalone use |
| [docs/](docs/README.md) | Task guides, the skill catalog, and practical prompts |
| [evals/](evals/index.md) | Development records and their evidence |
| [scripts/](scripts/) | Resource synchronization, validation, and release packaging tools |
| [assets/](assets/README.md) | Promotional artwork, web copies, and generation prompts |

## License and artwork

[MIT](LICENSE). Each skill includes its own license. Public examples are fictional or authorized; private source materials are not part of the library.

The promotional images were made with OpenAI's built-in GPT image-generation tool. They illustrate the editorial workflow and are not research figures. Originals, web copies, and generation prompts are available in the [media kit](assets/README.md).
