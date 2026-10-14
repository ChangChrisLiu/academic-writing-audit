---
name: related-work-synthesis
description: Organize or revise Related Work around meaningful comparison axes, check citation support, and bound novelty claims. Use when a passage is a paper list, creates false camps, or repeats the method instead of locating the work.
license: MIT
---

# Related Work Synthesis

Explain how relevant approaches relate to the research question. Preserve real distinctions without inventing mutually exclusive categories, missing capabilities, or priority claims.

## Establish source coverage

Identify the requested passage, the current work's supplied description, and the available sources. Distinguish full papers from abstracts, excerpts, notes, and earlier assistant summaries. Use the material the task permits. A bounded revision can proceed with incomplete coverage; report what remains unestablished rather than inventing missing facts or requiring an unrelated search.

Check each source-dependent proposition against the source actually available. An excerpt that does not discuss a property establishes **unknown**, not **absent**. Source notes can support a provisional synthesis but cannot silently become verified full-paper claims.

## Choose the comparison axes

Select only axes that explain the present research question: for example, information available, source of supervision, interaction timing, learning objective, decision rule, assumptions, or evaluated endpoint. Similar task names and author chronology are usually insufficient organizing principles.

When several papers overlap, use a small working matrix of **approach × relevant property × source support**. This is optional reasoning support, not mandatory manuscript content. Mark unknown cells explicitly. Permit an approach to occupy multiple categories; “uses archived data” and “accepts later corrections” can both be true.

Distinguish an operational difference from evidence of superiority. A different information source, rule, or evaluation setting does not by itself demonstrate better performance or that another method fails.

## Build the synthesis

Group sources around supported commonalities, then state meaningful differences. Connect each paragraph to the question the paper addresses. Avoid a catalogue of one-sentence paper summaries when an axis explains the relationship more directly.

Keep the present method's description to the detail needed for comparison; move its procedural walkthrough to Methods. Give a plain operational distinction before referring readers to formal details. Preserve substantive differences rather than flattening everything into “related approaches.”

Place citations close to the propositions they support. Split a compound sentence if different sources support different clauses. A citation range does not support a universal statement when one cited source contradicts it. Never invent a reference or infer citation entailment from a title alone.

## Bound novelty

Separate “our design uses these inputs” from “no prior work uses these inputs.” A small source set can establish local contrasts, not exhaustive priority. Remove, narrow, or flag “first,” “all,” and “only” when their required coverage is missing. Do not replace an unsupported priority claim with an equally unsupported claim that a particular combination is unique.

## Worked example

**Source cards:** Study A trains from historical observations and requests expert annotations for uncertain cases. Study B weights historical examples by annotator agreement. The present system combines historical and corrected records using source identity and consistency weights.

**Faulty synthesis:** “Historical and interactive methods are separate camps; ours first introduces evidence weighting.”

**Repair:** “Historical supervision can be extended through targeted expert annotation [A], while agreement-based weighting controls individual examples' training contributions [B]. The present system weights historical and corrected records using source identity and consistency.”

This identifies supported relationships without asserting exclusivity or exhaustive novelty. Any unreported weighting details in A remain unknown.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Check word meaning, natural word combinations, grammar, modifier attachment, and clear agency in context. Replace inflated or invented labels with established terminology or concrete wording without changing the concept. Preserve necessary terms of art and defined new concepts; flag uncertain meaning rather than guessing a synonym. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Deliver and stop

Return the requested synthesized passage or prioritized audit, followed by material citation or novelty uncertainties. Preserve correct comparisons and sound prose. Stop when the supplied sources support the revised distinctions; do not expand the task into new experiments, an unsolicited bibliography, or a complete method rewrite.
