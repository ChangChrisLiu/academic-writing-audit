# Literature-to-story preparation checks

Run date: 2026-10-29. This record tests a bounded preparation workflow on fictional robotics and social-history cases. Two investigators separately analyze the same source packet, then cross-review each other's records. A fresh writer synthesizes their findings. A second fresh writer repeats synthesis after one narrow instruction repair.

## What was exercised

The [packet](cases/request.md) contains older direct precedents, recent relevant methods, prominent but incompletely available sources, a version-linked preprint and journal article, an unsupported zero-hit novelty inference, and two initial author pitches contradicted by prior work. Both new studies lack results. A separate grammar-only request checks that routine editing does not trigger a new investigation.

The investigators distinguish research progress from unknown capabilities and reject both priority pitches. Cross-review identifies a small attribution overclaim in one initial record: citing a prior study does not by itself establish that the later study builds on it. The first writer adopts the narrower attribution, but retains a project-readiness question in one manuscript opening. A targeted clarification keeps such decisions in the research handoff, and a fresh synthesis run keeps the scientific aims in the openings and the project-readiness choices in the handoff.

## Complete records

| Stage | Preserved output |
| --- | --- |
| Investigator A, independent | [Initial record](runs/a/initial.md) |
| Investigator B, independent | [Initial record](runs/b/initial.md) |
| A checks B | [Reciprocal review](runs/a/cross-review.md) |
| B checks A | [Reciprocal review](runs/b/cross-review.md) |
| First writing handoff | [Provisional openings and handoff](runs/synthesis/answer.md) |
| Revised writing handoff | [Fresh synthesis regression](runs/regression/answer.md) |

See the [frozen semantic rubric](rubric.md), [full author assessment](assessment.md), and [run metadata](run-metadata.json). The initial and integrated writing instructions are retained as [initial](tested-skills/initial/research-manuscript-writing/SKILL.snapshot.md) and [integrated](tested-skills/integrated/research-manuscript-writing/SKILL.snapshot.md) snapshots. The released skill contains the final handoff-boundary clarification.

Inputs were frozen before each phase. The original [initial](design-freeze.json), [cross-review](cross-review-freeze.json), [synthesis](synthesis-freeze.json) and [regression](regression-freeze.json) freeze files retain their original relative workspace keys and hashes. [Publication transformations](publication-transforms.json) map those keys to public files and disclose the temporary-path substitutions in one generated report. No scientific wording in generated reports was edited. The [manifest](manifest.json) covers the public record and released skill bytes.

## Boundaries

This is a closed-packet exercise, not a live literature search, verified bibliography, systematic review, real manuscript edit or rendered-document test. The source packet provides descriptions and locations, not actual full publications. Independent interpretation of shared packet evidence is not independent retrieval or independent underlying evidence.

The skill author assessed all outputs without blinding or independent adjudication. There is no unguided control, and the regression repeats the same development cases. The runs therefore do not establish general effectiveness or isolate the instruction change's effect from generation variability. Fresh context and peer-output restrictions were requested in the prompts; they were not filesystem-enforced isolation. Only the writing and scientific-story entrypoints were used behaviorally; the related-work and umbrella audit changes received consistency and package checks.

The user-specified [Academic Research Skills comparison](../../docs/research-preparation.md) informed the final preparation guidance. The added workflow remains an original part of this MIT library; the CC BY-NC reference project's prompts, code and templates are not distributed here.
