---
name: results-interpretation
description: Write or audit Results interpretation while preserving endpoints, uncertainty, study identities, and the distinction between observed differences and isolated effects. Use when prose overclaims, merely repeats tables, or combines incompatible evidence.
license: MIT
---

# Results Interpretation

Explain what the results answer, how strongly, and under which conditions. Keep supported positive and negative findings visible. A useful Results paragraph connects evidence to the research question without turning every observation into a mechanism or replacing interpretation with disclaimers.

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

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Resolve the intended concept, scope, and implied properties before changing a term. Separate a wrong concept from awkward expression of a correct one. Check word combinations, grammar, modifiers, and agency in context. Preserve valid specialist terms, defined new concepts, and disciplinary uses even when unfamiliar. For a language-only repair, retain the technical term. Keep a correct passage unchanged and flag uncertain meaning rather than guessing. Verify that replacements preserve units, conditions, distinctions, and evidential force; do not use global word bans or substitutions. Apply the same standard to the audit itself. Do not add an unreported mechanism, mathematical form, or property when paraphrasing the source or explaining a finding. Keep an unspecified operation unspecified. For a named experimental condition or author-defined construct, check its operational definition and surrounding table or paragraph before classifying the label. If the operation is correct but the shorthand may mislead, report a naming clarification and consider a local gloss; do not call it a scientific error merely because the label is abbreviated. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Return useful prose

Respect whether the request is an audit or a rewrite. For an audit, identify consequential inference problems before proposing changes. For a rewrite, provide a coherent Results paragraph and briefly explain material changes. Preserve sound passages; do not restyle the author's voice without a reason.

Keep necessary qualifications near their claims, preferably once. Distinguish absent evidence from a negative result. Stop when the paragraph states the main finding, its supported meaning, and the material limits without repeating the table or listing hypothetical objections. Report unresolved source conflicts explicitly; complete the supported interpretation rather than fabricating an answer.

Read [the worked example](references/examples.md) for complementary results and retrospective recovery counts.
