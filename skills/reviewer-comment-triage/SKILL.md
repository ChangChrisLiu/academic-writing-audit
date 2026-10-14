---
name: reviewer-comment-triage
description: Use when translating peer-review comments into prioritized manuscript repairs, checking whether concerns remain in the current source, or separating clarification needs from missing evidence. Useful for revisions and camera-ready checks; does not default to response-letter drafting or new experiments.
license: MIT
---

# Reviewer Comment Triage

Use review comments to improve what the paper teaches its reader. A reviewer's question identifies a concern; it does not by itself determine the diagnosis or require a particular experiment.

## Read independently

Establish the requested scope and mode: triage, proposed repair, source edit, or verification of a revision. Read the current relevant text and supporting evidence before adopting earlier assistant judgments. A prior PASS may help locate a passage but cannot prove that the present concern is resolved. Retain author-approved choices and well-functioning prose unless the current evidence reveals a concrete defect.

Read each comment for its substantive question. Separate the reviewer's interpretation, the source's actual claim, the evidence available, and the action already taken. If the supplied packet is incomplete, limit the conclusion to it rather than inferring a missing experiment or inventing a revision history.

## Choose a proportionate repair

For each consequential concern, identify its primary cause:

| Cause | Reader-facing action |
| --- | --- |
| Correct operation is hard to find or ambiguous | State the defining operation where it is needed; keep detailed settings in their appropriate location. |
| Two parts of the paper disagree | Repair the specific inconsistency using the established source of truth; surface unresolved conflicts. |
| Claim exceeds the available evidence | Narrow the claim or state the material boundary. Keep the supported finding. |
| Evidence exists but does not answer the stated question | Explain what it establishes and what remains open. |
| Concern is already addressed in the current paper | Record the relevant passage and why it answers the concern; do not rewrite merely to demonstrate activity. |

Check comparators and ablations by their actual operations, not their names. Removing examples, masking a field, and removing supervision test different things. A temporal split does not establish transfer to another population, and higher performance alone does not identify a mechanism. If a genuinely missing study is essential to the retained claim, mark that dependency explicitly. New experiments are not the automatic consequence of a reviewer asking a broader question; honor the user's chosen scope.

Convert defensive prose into informative content. “We emphasize that our comparison is fair” usually needs a concrete comparison definition, not a stronger assurance. Keep qualifications that change the claim's truth or scope. Remove reviewer-directed staging from the manuscript when its reader-facing substance can stand directly. Draft a response letter only when requested, and do not describe a proposed repair there as completed.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Resolve the intended concept, scope, and implied properties before changing a term. Separate a wrong concept from awkward expression of a correct one. Check word combinations, grammar, modifiers, and agency in context. Preserve valid specialist terms, defined new concepts, and disciplinary uses even when unfamiliar. For a language-only repair, retain the technical term. Keep a correct passage unchanged and flag uncertain meaning rather than guessing. Verify that replacements preserve units, conditions, distinctions, and evidential force; do not use global word bans or substitutions. Apply the same standard to the audit itself. Do not add an unreported mechanism, mathematical form, or property when paraphrasing the source or explaining a finding. Keep an unspecified operation unspecified. For a named experimental condition or author-defined construct, check its operational definition and surrounding table or paragraph before classifying the label. If the operation is correct but the shorthand may mislead, report a naming clarification and consider a local gloss; do not call it a scientific error merely because the label is abbreviated. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Deliver a useful triage

Provide a concise overall judgment and, where several comments are involved, a compact mapping of **concern → current evidence/location → decision → smallest repair → unresolved dependency**. Prioritize scientific correctness and reader comprehension over stylistic preferences. Include explicit preserve/no-change decisions. Give replacement wording only for the authorized passages, with reasons tied to evidence.

Distinguish proposed wording, changes actually made, source consistency checked, and rendered results inspected. For a repair spanning Methods, captions, tables, or conclusions, verify the connected locations rather than fixing only the quoted sentence. If evidence is unavailable, state exactly what cannot yet be checked.

Stop when every in-scope concern has a supported disposition and the requested repairs are consistent. An unresolved evidence gap can remain honestly documented. Do not expand the task into a full rewrite, unsupported promises, automatic statistical analyses, or a second review of already sound passages.
