---
name: scientific-story-audit
description: Audit or repair the scientific argument of an abstract, introduction, or manuscript when motivation, research gap, contribution, and evidence feel disconnected. Preserve coherent passages; not a default workflow for grammar-only edits.
license: MIT
---

# Scientific Story Audit

Find the missing connection in the research argument before changing its prose. A readable story explains why the question matters, what remains difficult, how the contribution addresses that difficulty, and what the evidence establishes.

## Set the boundary

Use the current manuscript and supplied evidence. Earlier editorial judgments are leads, not verdicts. Identify whether the request is an audit, a revision, or a check after editing. Return findings for an audit; perform the bounded revision when requested. With an excerpt, assess its local argument and state which broader connection cannot be checked.

## Recover the argument

Write a short working account of **problem → unresolved difficulty → contribution → evidence → conclusion**. This is a reasoning aid, not a mandatory outline or replacement introduction. For theoretical or interpretive work, evidence may be a derivation, source analysis, or reasoned argument.

Check each connection:

- Does the difficulty explain why the proposed contribution is useful, or does the text jump from a broad topic to a method announcement?
- Does the contribution name the scientific operation or framework at the right level? A coefficient, filter, or implementation mechanism may serve a broader contribution without representing all of it.
- When components are complementary, does the text explain their distinct roles? Preserve acquisition, coverage, correction, inference, and selection as separate operations when those distinctions matter.
- Does the conclusion answer the original question within the evidence's scope? Describing a component's intended role is different from establishing its independent effect.

At paragraph level, identify the claim each sentence advances and the fact supporting the next step. Check whether a connector expresses contrast, consequence, or chronology accurately. Resolve vague “this” and shifts in subject, population, or unit before polishing the transition. A grammatical connection does not supply a missing premise.

Do not manufacture a literature gap to complete this chain. Mark an unsupported gap as unresolved. Likewise, do not promote every implementation choice into a contribution or weaken a supported contribution merely because it has several parts.

## Repair the smallest broken link

Locate the exact point where the reader loses the argument. Prefer a bridge, a corrected topic sentence, or a reordered sentence over rewriting an entire section. Follow scientific objects across the transition: a collected record, corrected annotation, training example, fitted model, and reported outcome are not interchangeable.

Before shortening, read the sentences on both sides of the proposed deletion. A general sentence may supply the reason for the method. Preserve a coherent passage verbatim when no concrete defect is identified. Necessary repetition can orient readers in a standalone abstract; repeated wording alone does not establish redundant function.

## Worked example

**Supplied facts:** A crop-monitoring workflow combines scheduled observations, follow-up measurements after anomalous readings, and expert corrections. A scoring rule determines their training contributions. Only the complete workflow has been evaluated.

**Weak framing:** “We introduce a scoring equation; other components include follow-up visits and corrections.”

**Repair:** “We introduce a workflow that combines routine observations, targeted follow-ups, and expert corrections for crop monitoring. A scoring rule controls how these complementary records contribute during fitting.”

This restores the contribution's level without claiming that each component independently causes improvement. Keep any preceding motivation that already explains why heterogeneous observations are difficult to combine.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Resolve the intended concept, scope, and implied properties before changing a term. Separate a wrong concept from awkward expression of a correct one. Check word combinations, grammar, modifiers, and agency in context. Preserve valid specialist terms, defined new concepts, and disciplinary uses even when unfamiliar. For a language-only repair, retain the technical term. Keep a correct passage unchanged and flag uncertain meaning rather than guessing. Verify that replacements preserve units, conditions, distinctions, and evidential force; do not use global word bans or substitutions. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Deliver and stop

For an audit, give the main argument defect, its location and consequence, plus explicit keep decisions. For revision, provide only the affected replacement or patch, a brief rationale, and material unresolved facts. Respect requested length and format.

Stop when the requested connections are clear and the claim strength matches the supplied evidence. “No change needed” is a valid outcome. Do not expand a story repair into a new study, exhaustive literature search, or wholesale stylistic rewrite.
