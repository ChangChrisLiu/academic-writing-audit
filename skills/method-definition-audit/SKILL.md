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

## Make the account readable without repeating it

Follow the dependencies a reader needs, from objects and assumptions through operations to their outputs and use. For a theoretical or qualitative method, follow the actual proof or analytic process rather than inventing a computational pipeline. Define stable concepts when first needed, then use them consistently. A brief overview, equation, and algorithm can serve different functions, but prose need not restate every representation line by line.

Cut repeated assurances and repeated explanations with the same purpose. Keep the actual safeguards, fallback conditions, and inferential boundaries. Move supporting detail only when the main explanation remains complete enough to follow and the destination contains the promised information. Concision must not remove a defining step or replace it with an unexplained appendix pointer.

## Prose when drafting or revising

When drafting or revising prose, including audit explanations, read [prose editing rules](references/prose-policy.md). Preserve scientific meaning, necessary reasoning and valid technical terms. Keep sound passages, do not add unreported properties, and limit edits to the requested scope. The local reference covers concept accuracy, clear sentences, repetition and punctuation, including the required exceptions.

## Deliver and stop

For an audit, return a concise verdict followed by consequential mismatches, each with its location, supplied evidence, and smallest repair. Include explicit keep decisions for questioned definitions that already work. For a revision, return replacement text or a bounded patch plus the reason for each substantive change. Retain coherent motivation, correct definitions, and the author's terminology where it remains unambiguous.

Re-read the repaired chain and its connected references. Report separately what was checked in prose, equations, code, or execution; claim only observed checks. Mark missing evidence as unresolved rather than filling it with a plausible procedure.

Stop when the requested definitions are mutually consistent and sufficiently explicit. A no-change judgment is valid. Do not expand the pass into new experiments, algorithm tuning, unrelated prose polishing, or repeated reformulation of sound text.
