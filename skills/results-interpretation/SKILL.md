---
name: results-interpretation
description: Write or audit Results interpretation while preserving endpoints, uncertainty, study identities, and the distinction between observed differences and isolated effects. Use when prose overclaims, merely repeats tables, or combines incompatible evidence.
license: MIT
---

# Results Interpretation

Explain what the results answer, how strongly, and under which conditions. Keep supported positive and negative findings visible. A useful Results paragraph connects evidence to the research question without turning every observation into a mechanism or replacing interpretation with disclaimers.

## Match the study's way of answering its question

Read the research question, study design, discipline, and supplied reporting format before choosing the narrative. The same discipline can contain quantitative, qualitative, theoretical, or mixed-method work. A quantitative study may proceed from a principal estimate to uncertainty and informative secondary findings. An engineering evaluation may connect a benchmark to targeted diagnostics. A qualitative account develops an analytic claim through evidence, interpretation, and variation; it must not turn themes into population frequencies or invent quotations. A theoretical account follows assumptions, propositions, proof dependencies, and consequences without inventing empirical validation. Mixed-method writing explains convergence and disagreement between evidence streams.

Apply the quantitative checks below where relevant, not as compulsory elements in every paper. Respect separate Results and Discussion or a supplied combined format. Keep broader explanation and literature comparison in their appropriate section. Never infer a reporting requirement from a field label alone.

When limitations or a conclusion are requested, tie each material limitation to the inference or applicability it constrains. Return to the study question with the supported answer and bounded significance. Avoid stock caveat lists, section-by-section recaps, new results, and generic future-work promises. These functions may sit within Discussion rather than under separate headings.

## Establish the result's identity

For each material result, recover the study, compared variants, evaluation population or tasks, endpoint, denominator, unit of analysis, and supplied uncertainty. Use only details that affect interpretation. Keep the definition of success intact: a compound endpoint must not become one convenient component or a broader guarantee.

Distinguish primary evaluation, shifted-condition tests, ablations, validation selection, internal sensitivity, and qualitative demonstrations. Similar method names do not make results interchangeable. Explain complementary roles; do not pool counts or subtract rates across different studies as a causal decomposition without a justified design and analysis.

## Move from numbers to meaning

Start with the main supported observation, then state its relevance to the question. A numerical difference can be reported descriptively when no inferential test is supplied. Do not invent significance or weaken a directly observed difference into mere possibility. Preserve null, mixed, and negative findings when they change the interpretation.

Separate the following:

- **Observed difference:** What the reported outcomes show under the tested protocol.
- **Within-run decomposition:** Which paths or stages occurred among the same runs.
- **Isolated effect:** What an appropriate comparison identifies about a changed factor.
- **Broader implication:** What might transfer beyond the evaluated setting, with the evidential limit made explicit.

A retrospective “first pass” subset of successful full-system runs is not a separately executed system with recovery disabled. Additional completions after recovery can be reported as observed later completions; the count does not by itself estimate the causal benefit of enabling recovery. Preserve the useful path information without relabeling it an ablation.

A shifted collection can show performance under those conditions. If samples and other conditions differ, subtracting its rate from a benchmark rate does not isolate the cost of the named shift. A sensitivity study changing several coefficients with every feature retained does not establish the necessity or causal contribution of an individual feature.

## Preserve quantitative meaning

Retain counts and denominators where available. Distinguish percentage points from relative change and individual observations from independent replicates. Keep uncertainty attached to its actual estimate and method: a bootstrap interval for one system is not a between-method interval, and a range across configurations is not replication uncertainty.

Do not invent intervals, equivalence, significance, or pooled estimates. A supplied measurement may be exact as a count while its generalization remains uncertain. A successful endpoint cannot establish unmeasured safety, reliability, or universal deployment performance.

## Prose when drafting or revising

When drafting or revising prose, including audit explanations, read [prose editing rules](references/prose-policy.md). Preserve scientific meaning, necessary reasoning and valid technical terms. Keep sound passages, do not add unreported properties, and limit edits to the requested scope. The local reference covers concept accuracy, clear sentences, repetition and punctuation, including the required exceptions.

## Return useful prose

Respect whether the request is an audit or a rewrite. For an audit, identify consequential inference problems before proposing changes. For a rewrite, provide a coherent Results paragraph and briefly explain material changes. Preserve sound passages; do not restyle the author's voice without a reason.

Keep necessary qualifications near their claims, preferably once. Distinguish absent evidence from a negative result. Stop when the paragraph states the main finding, its supported meaning, and the material limits without repeating the table or listing hypothetical objections. Report unresolved source conflicts explicitly; complete the supported interpretation rather than fabricating an answer.

Read [the worked example](references/examples.md) for complementary results and retrospective recovery counts.
