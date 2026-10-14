---
name: method-definition-audit
description: Use when a manuscript's method definitions, equations, pseudocode, baseline descriptions, or ablation names may disagree about objects, operation order, or decision stages. Appropriate for operational clarity checks and targeted repairs, not algorithm redesign.
license: MIT
---

# Method Definition Audit

Make the method reconstructable from the paper while preserving the actual scientific procedure. A name, symbol, or appendix pointer is not an operational definition.

## Establish the evidence

Identify the requested mode: audit, proposed wording, or bounded source edit. Honor narrower requests. Read the current passage and relevant definitions before consulting an earlier review. Record which artifacts the author identifies as authoritative: manuscript, appendix, protocol, equations, or implementation. Code can expose a mismatch without automatically overriding an approved protocol. If their authority is unresolved, report the conflict instead of inventing a reconciliation.

Use the available evidence only to its stated extent. Reading pseudocode does not establish implementation behavior, runtime results, or historical provenance.

## Reconstruct the operations

1. **Name the objects.** Identify each input, target, prediction, statistic, parameter, and output. Distinguish a recorded action or annotation from a predicted one; a training example from its features; a score from a weight; and a configuration from the fitted model it produces. Track units, indexing, aggregation level, and population when these affect meaning.
2. **Follow the transformations.** Trace input → operation → output in execution order. Check clipping, normalization, aggregation, thresholding, and fallback rules. These operations need not commute. A bound before normalization is not automatically a bound on the final value. Retain supplied constants and formulas unless a correction is supported and within scope.
3. **Separate decisions by what they act on.** Eligibility may remove records; a candidate audit may reject a parameter setting; validation may select a fitted model. For each decision, identify its object, criterion, timing, and consequence. Do not infer record removal from the word “gate,” or treat a missing implementation detail as a scientific filtering operation.
4. **Define comparisons by operations.** For every relevant baseline or ablation, identify what is retained, removed, replaced, fixed, or selected. Similar labels and equal absence of search do not establish identical algorithms. Removing records differs from hiding their labels or masking an input field. Check the definition against captions and tables as well as Methods.
5. **Put the defining action in the main explanation.** State what is computed, from what, and how it is used before pointing to detailed parameter lists. Use ordinary language first when the mathematical notation alone hides the operation. Preserve necessary conditions rather than replacing them with an assurance that the method is rigorous.

For example, “reject settings whose group mean weight is below the threshold” describes a configuration decision. Rewriting it as “discard low-weight records” changes the training population and therefore the method.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Check word meaning, natural word combinations, grammar, modifier attachment, and clear agency in context. Replace inflated or invented labels with established terminology or concrete wording without changing the concept. Preserve necessary terms of art and defined new concepts; flag uncertain meaning rather than guessing a synonym. Name the actual object consistently; a dataset should not become a buffer through stylistic substitution. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Deliver and stop

For an audit, return a concise verdict followed by consequential mismatches, each with its location, supplied evidence, and smallest repair. Include explicit keep decisions for questioned definitions that already work. For a revision, return replacement text or a bounded patch plus the reason for each substantive change. Retain coherent motivation, correct definitions, and the author's terminology where it remains unambiguous.

Re-read the repaired chain and its connected references. Report separately what was checked in prose, equations, code, or execution; claim only observed checks. Mark missing evidence as unresolved rather than filling it with a plausible procedure.

Stop when the requested definitions are mutually consistent and sufficiently explicit. A no-change judgment is valid. Do not expand the pass into new experiments, algorithm tuning, unrelated prose polishing, or repeated reformulation of sound text.
