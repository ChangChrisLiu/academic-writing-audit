<p align="center">
  <img src="assets/hero.jpg" alt="Academic Writing Audit：清晰论证，有据结论，克制修改" width="100%">
</p>

# Academic Writing Audit：学术论证与写作审查

**12 个可独立使用的 agent skills，把论文写作、逻辑审查和审稿回复中反复遇到的问题整理成可执行的判断方法。**

[English](README.md) · [问题与修复示例](docs/field-guide.md) · [审稿回复指南](docs/rebuttal-guide.md) · [完整审查入口](skills/academic-writing-audit/SKILL.md) · [专项试用记录](evals/library/README.md) · [宣传素材](assets/README.md)

先理解研究主线，再检查证据与推理，最后决定哪里需要改。审查后判断“这段原样保留”，同样是有价值的结果。

英文核心指令便于不同 agent 使用；中文说明解释选择和调用方法。每个 skill 都是独立目录，不依赖某篇论文、特定模型或多 agent 工作流。

## 从哪里开始

| 你现在的任务 | 使用入口 | 期望输出 |
| --- | --- | --- |
| 第一次完整阅读一篇稿件 | [academic-writing-audit](skills/academic-writing-audit/SKILL.md) | 按重要性排列的问题、依据和保留项。 |
| 已知具体写作问题 | 从下表选一个专项 skill | 有范围、有依据的替换或补丁。 |
| 撰写 rebuttal 或逐点 response letter | [reviewer-response-writing](skills/reviewer-response-writing/SKILL.md) | 有依据的回应、准确的修改状态，以及单独撰写的正文修改。 |
| 提交前检查版本和成品 | [manuscript-release-check](skills/manuscript-release-check/SKILL.md) | 已核实的源码、编译、渲染和发布状态。 |

```text
使用 $academic-writing-audit 独立阅读这篇论文。
先给结构化审查，不改文件。检查研究主线、证据边界、
比较对象、定义承接、冗余和防御性写作。
区分必须修正、值得改善和可以保留，注明位置与依据。
```

## 按问题选择 skill

| 遇到的问题 | Skill | 核心判断 |
| --- | --- | --- |
| 需要完整的科学与写作审查 | [academic-writing-audit](skills/academic-writing-audit/SKILL.md) | 论证、证据、读者功能、修改范围是否一致？ |
| 动机与方法之间缺一座桥；贡献缩成实现细节 | [scientific-story-audit](skills/scientific-story-audit/SKILL.md) | 问题、困难、贡献和证据是否真正连接？ |
| 正文像回复审稿人，反复保证“我们没有……” | [nondefensive-writing](skills/nondefensive-writing/SKILL.md) | 事实、措辞和位置分别是否有用？ |
| Related Work 变成论文清单或人为划分阵营 | [related-work-synthesis](skills/related-work-synthesis/SKILL.md) | 比较轴是否成立？来源能否支持新颖性判断？ |
| 用系统结果解释单个机制；用现有代码证明旧实验 | [claim-evidence-audit](skills/claim-evidence-audit/SKILL.md) | 哪份证据支持哪条主张，允许推断到哪里？ |
| 基线、消融、预算和数据范围说不清 | [experiment-comparison-audit](skills/experiment-comparison-audit/SKILL.md) | 实际改变了什么，而不是实验叫什么？ |
| Results 只报数字，或把解释写成因果证明 | [results-interpretation](skills/results-interpretation/SKILL.md) | 观察回答了什么，哪些机制仍未隔离？ |
| 公式和附录都有，但读者不知道方法做了什么 | [method-definition-audit](skills/method-definition-audit/SKILL.md) | 能否先用一句操作定义讲清，再核对顺序与参数？ |
| 图、箭头、图注和成功定义含义不一致 | [figure-caption-audit](skills/figure-caption-audit/SKILL.md) | 图的每个连接是否有真实语义支持？ |
| 审稿意见导致全文不断加解释、重复修补 | [reviewer-comment-triage](skills/reviewer-comment-triage/SKILL.md) | 当前稿还缺什么，最小修复应该放在哪里？ |
| 回复信绕开问题、证据不足，或把拟修改写成已完成 | [reviewer-response-writing](skills/reviewer-response-writing/SKILL.md) | 是否直接回答问题，证据是否对应，修改是否真实完成？ |
| 源码已改，PDF、线上预览和提交状态却不确定 | [manuscript-release-check](skills/manuscript-release-check/SKILL.md) | 每一个“完成”到底由什么观察证明？ |

不需要每次加载全部 12 个。先选择与当前问题最接近的入口；只有发现跨章节的问题时，再扩大审查范围。

## 审稿回复与正文分开写

新加入的 [reviewer-response-writing](skills/reviewer-response-writing/SKILL.md) 支持会议 **rebuttal / author response** 和期刊逐点 **response letter / 返修信**。方法来自实际回复写作及后续正文审查中反复遇到的问题；公开案例均为虚构，不包含原始审稿通信。

- **回复信**：直接回答问题，给出对应证据，说明实际修改、位置或尚未解决的限制。相同问题可合并回答，但每条具体请求都要有去向。
- **论文正文**：保留科学解释与证据边界，不写“为回应 Reviewer 2”“我们现已澄清”等回复口吻。把必要说明融入读者需要的位置，避免不断追加辩解。
- **修改状态**：拟议文字、作者报告已完成、实际核对完成分别标明；不编造实验、数值、引用或页码行号。

例如，核对 Methods 确已修改后，回复信可以写“我们已在 Methods 的 Comparators 小节补充基线的操作定义”。正文则直接写“该基线采用预设线性评分与固定组别系数，并拟合一个模型”。回复信说清修改，正文说清研究。

完整方法、反例和中文提示词见 [审稿回复与正文写作指南](docs/rebuttal-guide.md)。

## 怎样理解“去防御性写作”

一句话包含否定、限制或不确定性，并不意味着应该删除。我们分别判断：

1. **事实的作用**：删掉后，读者会误解什么或失去哪条逻辑连接？
2. **表达的方式**：它是在说明操作和观察，还是在预先反驳、保证正确？
3. **出现的位置**：读者此时是否需要它，附近是否已完成相同的解释任务？

例如，虚构草稿写道：

> 我们强调，不完整的测量绝没有被悄悄丢弃。读者不应认为本系统保证现场运行可靠。

若已知事实是不完整测量触发弃权、保留在分母中、不输出浓度估计，且未开展现场评估，则可改成：

> 不完整测量触发弃权，不输出浓度估计，并保留在评估分母中。本研究没有评估现场运行。

语气更直接，但算法规则、分母和证据边界完整保留。前文若已清楚解释研究动机，就不再改写。

## 安装

可以先[下载便携发布包](https://github.com/ChangChrisLiu/academic-writing-audit/releases/latest)，也可以按下面的方法单独安装。

目录遵循 [Agent Skills 格式](https://agentskills.io/specification)。支持原生 skills 的客户端可以发现入口；其他 agent 也可以直接阅读 Markdown。可移植不意味着已验证所有模型表现相同。

可选用 [Skills CLI](https://github.com/vercel-labs/skills)：

```sh
# 列出可安装的 skill，不执行安装。
npx skills add ChangChrisLiu/academic-writing-audit --list

# 安装一个，按提示选择目标客户端。
npx skills add ChangChrisLiu/academic-writing-audit --skill nondefensive-writing

# 在当前项目中为 Codex 安装全部 12 个。
npx skills add ChangChrisLiu/academic-writing-audit --skill '*' -a codex
```

需要用户级安装时加 `-g`。已有同名 skill 时，先比较版本和目标位置。

也可以手动把 `skills/` 中选定的整个文件夹复制到客户端的 skills 目录，保留其中的参考文件和 `LICENSE`。[英文说明](README.md#manual-installation)包含 Codex 示例。`agents/openai.yaml` 只是可选的展示信息。当前会话没有发现新 skill 时，在新会话中使用。

对于不能安装 skill 的 agent，提供 `SKILL.md` 及需要的参考文件，然后直接要求按文件中的方法完成任务。

## 可以直接复制的请求

**Rebuttal / response letter 与正文修改**

```text
使用 $reviewer-response-writing，根据这些真实审稿意见、当前稿件和
实验记录起草回复。遵守我提供的篇幅与投稿规则，先回答实质问题，
再给证据、解释边界和修改位置；不要把计划写成已完成。
单独列出建议的正文替换，正文不得出现回应 reviewer 的口吻。
保留尚未解决的问题，不编造实验、阈值、引用或页码行号。
```

**有明确范围的修改**

```text
使用 $experiment-comparison-audit 修改这份稿件的实验设置段。
按真实操作核对基线、数据范围、训练与选择预算、消融含义。
直接完成有依据的局部修复，保留数值和已成立的作者表述。
如果材料冲突，指出冲突；不要编造一个统一解释。
```

**保留解释力度的结果段**

```text
使用 $results-interpretation 检查这一节。
区分观察、解释和因果归因，保留对研究问题有用的分析。
不要把所有解释都删成报数，也不要把同一批运行中的阶段结果
当作独立消融。给出需要改的句子和应该保留的句子。
```

**图注与图意核对**

```text
使用 $figure-caption-audit 对照这张图、图注和方法段。
检查箭头、数据流、对照组范围和实际评估终点。
说明哪些判断来自可见图像，哪些只能由提供的描述支持。
```

更完整的虚构案例与任务模板见 [field guide](docs/field-guide.md)。

## 验证记录

[最初的完整审查试用](evals/README.md)包含 5 次无 skill 对照、5 次带 skill 试用及 4 个迁移场景；在这个小样本中，带 skill 的回答更稳定地保留了一段已经连贯的研究动机。

[10 个专项 skill 的试用记录](evals/library/README.md)公开场景、语义标准和完整回答。这组对照本身已解决核心问题，因此不能据此声称专项 skill 提高了准确率。测试用于检查具体行为、保留失败和支持后续回归检查，不代表跨模型或跨学科有效性认证。

新增回复写作 skill 提供[开发场景与语义检查标准](evals/reviewer-response-writing/README.md)，尚无独立 agent 行为试用结果。格式、链接和打包检查不能替代有效性验证。

## 素材与贡献

宣传图采用纸张、墨色和批注的学术编辑风格，由 OpenAI 内置 GPT 图像生成工具制作。三张原图、网页版本及实际生成提示词都在 [media kit](assets/README.md) 中。它们用于展示工作方式，不作为实验结果图。

项目采用 [MIT 许可证](LICENSE)，每个独立 skill 都附带许可证。欢迎按 [贡献指南](CONTRIBUTING.md)提供可复现的问题、最小修改和测试案例。公开内容使用通用方法与虚构或已授权材料，不包含私人稿件和内部评审通信。
