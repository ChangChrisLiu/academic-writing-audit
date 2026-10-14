---
name: manuscript-release-check
description: Use when checking manuscript finalization, source-to-PDF identity, editor synchronization, submission evidence, or preparing a recoverable handoff for another agent. Especially useful after late source edits, stale previews, missing build dependencies, or conflicting completion reports.
license: MIT
---

# Manuscript Release Check

Tie every completion claim to an identifiable artifact and observed evidence. Source correctness, successful compilation, visual inspection, transfer, and submission are distinct states.

## Establish the target

Identify the intended manuscript source, author-approved changes, destination, and requested operation. Resolve “final” or “latest” using actual file locations, revisions, or manifests. Preserve existing sources, assets, and recoverable prior versions. This skill grants no authorization to upload, submit, publish, delete, or replace material; perform external actions only within the user's existing instructions. A readiness review remains a review.

Read current artifacts independently of earlier completion summaries. Separate observations from logs, human reports, assumptions, and your own newly performed checks. If only an evidence packet is available, assess that packet without claiming direct access to its underlying files or services.

## Follow the artifact chain

1. **Source:** Identify the entry file and needed bibliography, styles, figures, and other dependencies. Check that the intended edits are in the source being built. If a file changes after verification, earlier evidence remains attached to the earlier version.
2. **Build:** Associate a successful compiler result with its exact input and output. A missing style file establishes a dependency blocker, not that the latest edit is wrong or that the remaining source is valid. Use the legitimate dependency or intended build environment when authorized; do not silently substitute a style or revert approved text to obtain a PDF. A Recompile click is only an action record.
3. **Render:** Inspect the intended PDF and record pages or regions checked. A successful build does not establish unclipped figures, correct affiliations, usable cross-references, or final pagination. Partial inspection supports a partial verdict. A preview showing old text cannot verify the new version.
4. **Transfer:** Distinguish a recorded paste or upload from independently verified persisted contents. Confirm the destination identity and intended source or artifact when accessible. A source transfer, successful remote build, and matching exported PDF require separate evidence; none follows merely from an editor action log.
5. **Submission:** Inspect the actual state or receipt when this is within scope. An attachment listed in a draft confirms neither final submission nor public availability. Link any observed receipt to the intended artifact and action. Do not infer completion from a button click or present a future step as already performed.

## Leave a recoverable handoff

Use these fields when another agent must continue; omit only genuinely irrelevant fields:

- **Current source:** location, entry file, revision or observed identifier, and approved changes to preserve.
- **Prior recoverable state:** preserved source/artifact locations and the relationship to the current version.
- **Build state:** input identity, environment/dependencies, command or build entry point when known, log/result, and output identity.
- **Render coverage:** exact output inspected, pages/regions, material findings, and unchecked areas.
- **Destination state:** project/file or portal identity, recorded transfer activity, verification evidence, attachment identity, and submission/receipt status.
- **Resume actions:** smallest remaining checks, unresolved blockers, and action boundaries from the user's instructions.

Use real identifiers already available or hashes actually calculated; do not invent hashes to make the handoff appear precise. A timestamp helps locate evidence but alone does not prove two artifacts match. Keep private paths and identifiers within the authorized handoff context.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Resolve the intended concept, scope, and implied properties before changing a term. Separate a wrong concept from awkward expression of a correct one. Check word combinations, grammar, modifiers, and agency in context. Preserve valid specialist terms, defined new concepts, and disciplinary uses even when unfamiliar. For a language-only repair, retain the technical term. Keep a correct passage unchanged and flag uncertain meaning rather than guessing. Verify that replacements preserve units, conditions, distinctions, and evidential force; do not use global word bans or substitutions. Apply the same standard to the audit itself. Do not add an unreported mechanism, mathematical form, or property when paraphrasing the source or explaining a finding. Keep an unspecified operation unspecified. For a named experimental condition or author-defined construct, check its operational definition and surrounding table or paragraph before classifying the label. If the operation is correct but the shorthand may mislead, report a naming clarification and consider a local gloss; do not call it a scientific error merely because the label is abbreviated. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Report and stop

Lead with the supported readiness judgment, followed by confirmed, failed/blocked, and unverified steps. Name what changed and what still needs checking. A missing receipt means completion is unconfirmed, not proof that a remote action never occurred.

Stop when the requested chain has been verified or every remaining gap has a specific recoverable next step. Preserve the author's valid changes while resolving environmental failures. Do not repeatedly rebuild unchanged inputs, erase prior artifacts, widen a bounded review into publication, or claim that source inspection proves deployment or submission.
