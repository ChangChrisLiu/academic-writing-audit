---
name: figure-caption-audit
description: Use when auditing a scientific figure, diagram, chart, or caption for agreement with the current manuscript, especially arrows, data support, stages, comparisons, and evaluation endpoints. Supports text-only diagram specifications without implying that an image was inspected.
license: MIT
---

# Figure and Caption Audit

Check what the figure tells a reader before polishing how it looks. A visually clear diagram can still describe the wrong experiment.

## Set the scope

Identify the requested deliverable: findings, caption repair, diagram instructions, or an actual asset edit. Preserve the author's sound structure and source assets. Use the current manuscript and relevant protocol as evidence; an older figure approval or review memo does not establish agreement with today's source.

Inventory the available representation: textual specification, editable source, exported image, or rendered manuscript page. These support different checks. A text specification supports a semantic review, not conclusions about pixels, legibility, cropping, color, or page layout. A source edit does not establish that an exported or embedded figure changed.

## Audit the scientific meaning

1. **Map the elements.** For each box, curve, panel, symbol, or legend label, identify the real object it represents and its source definition. Distinguish collected records, eligible training examples, diagnostics, predictions, and measured outcomes. Keep names and units consistent across the figure, caption, Methods, and results.
2. **Read every arrow as a claim.** Determine whether it means data flow, temporal order, optimization, selection, evaluation, or a hypothesized relationship. Verify the endpoints and direction. Training, validation, and test feedback are different operations. Changing an unsupported feedback arrow to a dotted line does not establish a supported meaning; remove it or supply an accurate label and connection.
3. **Check populations and comparisons.** Show which examples each method can use. Shared architecture, nominal update budgets, or a common archive do not imply identical training support. Keep diagnostic-only records outside training paths. For charts, check denominators, conditions, uncertainty definitions, and whether panels describe the same experiment before allowing direct comparisons.
4. **Match the measured endpoint.** Trace the final stage to the actual outcome criterion. Preserve all required conditions, including evaluation stopping points. A system that detects a target has not thereby completed the downstream intervention. A schematic output icon should not imply a measured capability absent from the study.
5. **Repair the caption and figure together.** A corrected caption cannot reliably cancel a contradictory arrow or label. Put interpretation-critical conditions where a reader can find them; leave detailed settings to the paper when they are not needed to understand the figure. Distinguish an illustrative workflow from observed experimental results.

For example, a dataset may contain accepted images and excluded images kept for an audit. A single “all images → training” arrow misstates support even if the caption calls the archive comprehensive. Route the audit separately while preserving the useful overall organization.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Resolve the intended concept, scope, and implied properties before changing a term. Separate a wrong concept from awkward expression of a correct one. Check word combinations, grammar, modifiers, and agency in context. Preserve valid specialist terms, defined new concepts, and disciplinary uses even when unfamiliar. For a language-only repair, retain the technical term. Keep a correct passage unchanged and flag uncertain meaning rather than guessing. Verify that replacements preserve units, conditions, distinctions, and evidential force; do not use global word bans or substitutions. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Verify and report

Return a short verdict, then each consequential mismatch as **element/location → implied claim → source evidence → smallest repair**. Provide a replacement caption or edit instructions when requested. State which valid elements should remain. Separate scientific repairs from optional visual preferences.

If image or page evidence is available and visual review is in scope, inspect the actual artifact at a useful size. After authorized edits, check the new export and relevant manuscript placement when accessible. Report the exact representation and coverage inspected; do not reuse a stale preview as verification. When only text is available, label the outcome a specification review and identify the remaining visual check.

Stop when the requested figure and caption accurately communicate the supplied evidence. Do not redesign a sound figure, manufacture results, alter the scientific protocol to fit the artwork, or claim a render was checked without observing it. No justified change is a valid result.
