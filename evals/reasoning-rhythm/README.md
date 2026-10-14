# Reasoning development and natural expression trials

These fictional cases check whether editing makes an academic argument develop through supported reasoning, appropriate emphasis, and meaningful connections. They also check whether agents preserve clear prose and useful parallel form instead of forcing variety. No authorship or human-likeness score is used, and no private manuscript is published or modified.

## Design

| Case | Requested work | Skills exercised |
| --- | --- | --- |
| [Engineering](cases/engineering/request.md) | Replace a tactile-contact methods inventory with a connected explanation using supplied timing facts. | academic-prose-editing |
| [Ecology](cases/ecology/request.md) | Write Chinese results interpretation connecting equal mean richness with changed community composition; preserve a sound adjacent passage. | research-manuscript-writing and academic-prose-editing |
| [Mathematics](cases/mathematics/request.md) | Audit coherent reasoning, purposeful parallel bounds, and a rank choice whose reason is not supplied. | academic-prose-editing and revision-integrity-audit |

Three fresh-context agents received their request and assigned frozen skills. Instructions excluded parent conclusions, the rubric, other cases, memory, and the network. These are task restrictions, not a claim of enforced filesystem isolation. Execution notes are process reports, not independently reconstructed tool traces.

Requests, skills, and the [rubric](rubric.md) were frozen before execution. A separate fresh-context assessor read the complete requests and exact saved outputs without the skills or parent judgments. It assessed meaning and reader-facing reasoning rather than surface variation, sentence counts, or adherence to an ideal wording. The original tested skills are archived under [tested-skills/initial](tested-skills/initial); entrypoints use SKILL.snapshot.md to prevent duplicate discovery, with unchanged file bytes.

## Initial observations

The independent assessor marked all 15 criteria pass with no partial, failed, or inapplicable judgments and no harmful change. The engineering passage connects the contact-timing question to acquisition-time alignment while retaining the genuine receive buffer. The ecology passage develops the richness/composition distinction into a bounded interpretation. The mathematics answer keeps the clear passage and parallel bounds, removes unsupported assurances about rank four, and leaves the selection rationale unresolved instead of inventing author intent or a sensitivity study.

One optional expression preference is retained. The ecology answer uses 物种身份并不完全相同, which the assessor found understandable and faithful but somewhat literal in Chinese. It offered a more idiomatic alternative without classifying the concept as wrong. The original answer and [full assessment](assessment.md) remain unchanged; [structured judgments](assessment.json) preserve all scores.

## Narrow refinement and regression

The primary editor added a general distinction between evidence and publishable wording. Scientific meaning from working notes must be preserved, but informal or literal note phrasing need not be copied into manuscript prose. Established technical terms, exact quotations, and author-approved wording remain protected. This is not a blacklist or an instruction to replace the ecological expression in every context.

A new fresh-context agent repeated the unchanged ecology request with the revised skills. It received no initial output, assessment, or suspected phrase. Another independent assessor received only the regression case, output, and the same five semantic criteria, without the earlier judgments or skills.

The regression assessor marked all five criteria pass, with no harmful change. It recorded one optional concision preference about the scope-limitation sentence, whose necessity would depend on surrounding discussion that was not supplied. See the [full regression assessment](regression/assessment.md) and [structured judgments](regression/assessment.json).

The primary editor additionally observed that the regression still uses 物种身份. The clarification therefore did not eliminate the initial optional expression in this single run. The second assessor's passing judgment does not erase that observation or prove an improvement. No further word-specific rule or retry was added to force a lexical target. Both outputs, the different optional observations, and the limits remain public.

## Limits

These are deliberately constructed short passages rather than long manuscripts, unseen benchmarks, or independent expert certification. Three entrypoints received behavioral trials; library-wide structural and installation checks do not amount to behavioral testing of every skill. There is no unguided control, repeated-sampling estimate, causal attribution of improvement, or cross-model comparison. Agents used the same configured host without a model override; exact model versions were not independently recorded.

Scientific fidelity is assessed against fictional supplied facts, not raw-data or proof verification. The runs do not test compiled PDF pages, native Word layout, live citations, reviewer acceptance, or submission state. More natural reasoning is an editing objective, not evidence that a human authored the passage or that all future prose will be idiomatic.

## Records

[Initial input freeze](design-freeze.json) · [Regression input freeze](regression/design-freeze.json) · [Run metadata and path resolution](run-metadata.json) · [File and tested-skill hashes](manifest.json)

Initial skills/ paths in the freeze map to the archived initial skill folders, with SKILL.md renamed SKILL.snapshot.md. Regression skills/ paths resolve at the revised version in the manifest. Other paths resolve within the respective evaluation phase. Complete generated outputs, assessments, and execution notes are copied byte for byte. Runtime paths in raw notes record execution context rather than installation instructions.
