<p align="center">
  <img src="assets/hero.jpg" alt="Academic Writing Audit：清晰论证，有据结论，克制修改" width="100%">
</p>

# Academic Writing Audit：学术论证与写作审查

**18 个可独立使用的 agent skills，把论文写作、逻辑审查和审稿回复中反复遇到的问题整理成可执行的判断方法。**

[English](README.md) · [完整指南与 skill 目录](docs/README.md) · [安装](#安装) · [验证记录](evals/index.md) · [宣传素材](assets/README.md)

先理解研究主线，再检查证据与推理，最后决定哪里需要改。理性调研和批判性思考帮助形成有依据的判断，写作将它们组织成简洁、连贯的论述。正常专业术语、必要条件和推理桥梁应当保留；审查后判断“这段原样保留”，同样是有价值的结果。

英文核心指令便于不同 agent 使用，中文指南解释选择和调用方法。每个 skill 都是独立目录，不依赖某篇论文或特定模型。支持 LaTeX 和 Word；回复信回答审稿问题，正文直接向读者解释研究。

## 按问题选择 skill

| 你现在的任务 | 使用入口 |
| --- | --- |
| 从研究想法开始，或起草、重组论文 | [research-manuscript-writing](skills/research-manuscript-writing/SKILL.md) 与[研究准备指南](docs/research-preparation.md) |
| 完整阅读并审查一篇稿件 | [academic-writing-audit](skills/academic-writing-audit/SKILL.md) |
| 检查概念、用词、逻辑、句式或重复 | [academic-prose-editing](skills/academic-prose-editing/SKILL.md)，或选择[其他专项 skill](docs/README.md#skill-catalog) |
| 撰写 rebuttal 或逐点 response letter | [reviewer-response-writing](skills/reviewer-response-writing/SKILL.md) |
| 比较压缩或修订前后的版本 | [revision-integrity-audit](skills/revision-integrity-audit/SKILL.md) |
| 核实文献、BibTeX 或 Word 引用 | [文献核验与引用指南](docs/reference-guide.md) |
| 提交前检查版本和成品 | [manuscript-release-check](skills/manuscript-release-check/SKILL.md) |

不需要每次加载全部 18 个。先选择与当前问题最接近的入口，发现跨章节问题时再扩大范围。[指南索引](docs/README.md)列出全部 skills、专题说明与使用路径；[问题与修复示例](docs/field-guide.md)提供虚构案例和任务模板。

```text
使用 $academic-writing-audit 独立阅读这篇论文。
先给结构化审查，不改文件。检查研究主线、证据边界、
比较对象、定义承接、冗余和防御性写作。
区分必须修正、值得改善和可以保留，注明位置与依据。
```

## 一次有依据的修改

虚构草稿写道：

> 我们强调，不完整的测量绝没有被悄悄丢弃。读者不应认为本系统保证现场运行可靠。

若已知事实是不完整测量触发弃权、保留在分母中、不输出浓度估计，且未开展现场评估，则可改成：

> 不完整测量触发弃权，不输出浓度估计，并保留在评估分母中。本研究没有评估现场运行。

语气更直接，但算法规则、分母和证据边界完整保留。前文若已清楚解释研究动机，就不再改写。更多判断方法见[自然表达与逻辑审查](docs/prose-guide.md)和[修改前后对照](docs/revision-guide.md)。

## 安装

可以先[下载便携发布包](https://github.com/ChangChrisLiu/academic-writing-audit/releases/latest)，也可以单独安装需要的 skill。

目录遵循 [Agent Skills 格式](https://agentskills.io/specification)。支持原生 skills 的客户端可以发现入口；其他 agent 也可以直接阅读 Markdown。可移植不意味着已验证所有模型表现相同。

可选用 [Skills CLI](https://github.com/vercel-labs/skills)：

```sh
# 列出可安装的 skill，不执行安装。
npx skills add ChangChrisLiu/academic-writing-audit --list

# 安装一个，按提示选择目标客户端。
npx skills add ChangChrisLiu/academic-writing-audit --skill nondefensive-writing

# 在当前项目中为 Codex 安装全部 18 个。
npx skills add ChangChrisLiu/academic-writing-audit --skill '*' -a codex
```

需要用户级安装时加 `-g`。已有同名 skill 时，先比较版本和目标位置。

也可以手动把 `skills/` 中选定的整个文件夹复制到客户端的 skills 目录，保留其中的参考文件和 `LICENSE`。[英文说明](README.md#manual-installation)包含 Codex 示例。`agents/openai.yaml` 是可选的展示信息。当前会话没有发现新 skill 时，在新会话中使用。不能安装 skill 的 agent 可以直接阅读 `SKILL.md` 及需要的参考文件。

完整 skill 文件夹已附带所需共享资源的本地副本，不依赖其他已安装 skill。

文献真实性核验要求两个独立 agent 从 Google Scholar 开始检查；LaTeX 规范导出需要 Scholar Cite → BibTeX 访问能力。缺少相应能力时继续报告已取得的证据，并明确哪些步骤尚未完成。具体边界见[文献指南](docs/reference-guide.md)。

## 从理解到验证

<p align="center">
  <img src="assets/workflow.jpg" alt="理解研究问题与贡献，核对主张和比较，完成有依据的修改，分别验证源码与最终成品。" width="540">
</p>

1. **理解**当前稿件和作者的论证，再参考历史审查意见。
2. **核对**重要主张所依赖的证据、比较对象与研究条件。
3. **修改**请求范围内的实际问题，保留有效定义、条件和推理。
4. **验证**任务要求的成品，分别记录源码、编译、页面与发布状态。

只审查时给出判断；明确要求修改时完成有依据的局部修复。局部语法任务保持局部范围。

## 验证与维护

[完整验证索引](evals/index.md)汇集场景、语义标准、完整回答、失败、评估与回归记录，也包含实际 LaTeX 和 Word 产物检查。部分无 skill 对照已通过核心检查。这些小规模开发记录只支持已观察到的行为，不代表跨模型、跨学科的普遍有效性认证。

| 目录 | 内容 |
| --- | --- |
| [skills/](skills/) | 18 个独立 skills，附带本地参考文件、许可证和可选客户端信息 |
| [shared/](shared/) | 集中维护的表达约定与文献清单资源，本地副本随 skill 分发，支持独立使用 |
| [docs/](docs/README.md) | 任务指南、skill 目录和使用提示 |
| [evals/](evals/index.md) | 开发验证记录及其证据 |
| [scripts/](scripts/) | 资源同步、验证和发布打包工具 |
| [assets/](assets/README.md) | 宣传素材、网页版本和生成提示词 |

欢迎提交可复现的问题、最小修复和回归案例，见[贡献说明](CONTRIBUTING.md)。各 skill 附带独立的 [MIT 许可证](LICENSE)。

宣传图由 OpenAI 内置 GPT 图像生成工具制作，用于展示工作方式，不作为实验结果图。三张原图、网页版本及生成提示词均保存在[宣传素材目录](assets/README.md)。
