# Academic Writing Audit

An agent skill for reviewing academic arguments, removing unnecessary defensive writing, and making evidence-grounded revisions without losing the author's research story.

[中文说明](README.zh-CN.md) · [Skill](skills/academic-writing-audit/SKILL.md) · [Examples](skills/academic-writing-audit/references/examples.md) · [Evaluation](evals/README.md)

The guiding question is: **What does this sentence help the reader understand, and what evidence supports it?**

## What it helps with

- Scientific logic from motivation and contribution through method, evidence, and conclusion.
- Claim strength, comparator definitions, ablation semantics, and distinct experimental protocols.
- Defensive prose that anticipates objections instead of explaining the research.
- Over-editing that removes a necessary definition, boundary, motivation, or transition.
- Reviewer-informed revisions and final checks that preserve current source identity.

The skill distinguishes the importance of a fact from the quality of its wording and placement. It treats **keep as written** as a useful editorial decision. It supports empirical, theoretical, and qualitative work; the appropriate evidence depends on the discipline.

## How it works

The agent first identifies the requested scope and current source, then reconstructs the argument and checks consequential claims against their support. It evaluates questionable sentences by reader function and chooses among keep, clarify, merge, move, and delete. Changes must repair a specific problem. Verification is proportional to the requested output.

For example, “We stress that no labels were changed to improve the result” may become the direct fact “Labels were fixed before aggregate outcomes were computed.” But “Downstream outcomes were not evaluated” must remain when it defines what the reported result means.

The entrypoint is about 630 words. Detailed guidance is loaded only when needed:

| Resource | Use |
| --- | --- |
| [Argument and evidence](skills/academic-writing-audit/references/argument-and-evidence.md) | Source authority, object transitions, claims, comparisons, and generalization. |
| [Nondefensive writing](skills/academic-writing-audit/references/nondefensive-writing.md) | Sentence function, tone, placement, and necessary limitations. |
| [Review and patching](skills/academic-writing-audit/references/review-and-patching.md) | Audit outputs, bounded edits, independent perspectives, and verification. |
| [Worked examples](skills/academic-writing-audit/references/examples.md) | Concrete decisions, including cases where no edit is needed. |

## Use with an agent

The package follows the [Agent Skills format](https://agentskills.io/specification). The instructions use plain Markdown and relative references, with no mandatory model, API, command-line tool, browser, or agent delegation. Native discovery depends on the client; portability of instructions does not establish identical behavior across clients.

### A client that supports Agent Skills

Copy the entire `skills/academic-writing-audit/` folder into the client's configured skills directory. Keep `references/` and `LICENSE` with it. The optional `agents/openai.yaml` supplies Codex UI metadata; the core instructions do not depend on it.

For a local Codex installation, run these commands from this repository's root:

```sh
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skill_root"
test ! -e "$skill_root/academic-writing-audit" && \
  cp -R skills/academic-writing-audit "$skill_root/academic-writing-audit"
```

The copy runs only when that skill directory does not already exist. Review an existing version before replacing it. If the new skill is not listed in the active session, open a new session and invoke it there.

Example request:

```text
Use $academic-writing-audit to review the attached manuscript.
First give a scientific-logic audit; do not rewrite the source.
Prioritize claim-evidence alignment, comparator definitions, defensive
writing, and missing transitions. Identify passages that should stay.
```

For a revision:

```text
Use $academic-writing-audit to revise the Results section in this file.
Make only justified local changes. Preserve the reported values and
the author's framing. Explain any evidence conflict before resolving it.
Return the patch and a short account of the checks actually completed.
```

### Any agent that can read supplied Markdown

Provide `SKILL.md` and its `references/` files, then ask:

```text
Read skills/academic-writing-audit/SKILL.md and follow its guidance
for the manuscript task below. Read only the supporting references
needed for this task. My requested scope and constraints are: ...
```

If the client cannot open relative files, attach the relevant reference documents as well. A skill cannot assess evidence or rendered pages that have not been supplied or inspected.

## Scope and evaluation

This is a writing and reasoning workflow, not a literature-verification service, statistical analysis package, or guarantee of scientific correctness. A narrow grammar request stays narrow. A writing task does not authorize new experiments, hardware execution, or external publication.

The [evaluation materials](evals/README.md) contain fictional editorial and transfer scenarios, a semantic rubric, and observed trial outputs. They test common failure modes, including over-compression and deletion of necessary boundaries. The report separates controls from guided runs and does not claim validation across all agents or disciplines.

## Repository contents

```text
skills/academic-writing-audit/  Installable skill and supporting references
evals/                        Fictional scenarios, rubric, and trial records
README.zh-CN.md                Chinese usage and methodology guide
CONTRIBUTING.md                How to propose a bounded improvement
LICENSE                       MIT license
```

Only generic guidance and fictional examples belong in this repository. Do not add private manuscripts, reviewer correspondence, raw experimental records, account details, or local project histories.

## License

[MIT](LICENSE). The skill's standalone folder includes a copy of the license for redistribution.
