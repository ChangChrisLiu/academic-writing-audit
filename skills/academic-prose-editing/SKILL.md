---
name: academic-prose-editing
description: Edit or audit academic prose for precise terminology, professional phrasing, connected reasoning, sentence complexity, and redundancy. Use for robotic or formulaic writing, 去 AI 味, long sentences, and repeated explanations while preserving scientific meaning. Not an AI-authorship detector.
license: MIT
---

# Academic Prose Editing

Make the argument easier to read without changing what the evidence says. Treat requests to remove an “AI feel” as concrete editing requests, not evidence about who wrote the text. Do not report a human-likeness score or promise detector avoidance.

## Establish the editing contract

Read the passage and its immediate context. Identify whether the user wants an audit, proposed wording, or file edits. An audit returns findings before rewriting. Honor a bounded revision directly and preserve sound author choices. An excerpt supports a local judgment, not a whole-paper verdict.

Use this library's prose preference unless the author or venue specifies otherwise. Write connected paragraphs without explanatory colons or sentence-interrupting dashes, including spaced hyphens and LaTeX dash syntax. Use a full stop or a grammatical connection instead. Keep hyphens inside established compound terms such as “cross-domain.” This preference concerns generated exposition and response prose, not required document syntax. Preserve mathematical notation, minus signs, ranges, ratios, URLs, identifiers, citations, verbatim quotations, and required templates. Do not silently alter a source quotation to meet the preference. Do not turn a paragraph into bullet fragments unless the requested format calls for a list.

## Check the reasoning before polishing

Recover each paragraph's claim, support, and role in the surrounding argument. Follow the same subject, population, unit, endpoint, and conditions from one sentence to the next. A transition such as “therefore,” “however,” or “this” needs an identifiable relationship or referent. Adding a connector cannot repair missing evidence.

When a conclusion exceeds its support, correct the proposition using the supplied facts or identify the missing link. Do not conceal the issue by substituting “may” for “demonstrates.” Preserve motivation that explains why the next step is needed. Distinguish a study limitation from an analysis or document that was merely not supplied to the editor.

## Make the reasoning develop naturally

When accurate prose still feels mechanical, read [reasoning and rhythm](references/reasoning-and-rhythm.md). Identify what the reader understands at the end that was not established at the beginning. Connect the actual premise, difficulty, choice, evidence, or qualification needed here rather than presenting equally weighted facts. Make a supported rationale or consequential distinction visible; do not invent author deliberation, a discovery story, or a missing scientific reason.

Let emphasis and logical relationships shape sentence and paragraph variation. Avoid repeated stock openings and identical paragraph arcs when they flatten the argument. Preserve useful parallelism, stable terminology, disciplinary conventions, and a clear author voice. Do not impose alternating sentence lengths, obligatory contrasts, extra complexity, or synonym rotation. A plain definition can stay plain. Check why each sentence and paragraph follows the previous one, not merely whether a transition word is present.

## Replace generic framing with the actual scientific point

Before adding content, identify the passage's role in the research question and section. A topic label is not enough to supply a motivation or contribution. Where the study's purpose or evidence is missing, flag the exact dependency rather than drafting a generic claim about importance, rapid progress, or urgent need. Keep the scope local for a local edit.

Use the introduction's narrowing argument to judge whether a sentence advances context, established work, gap, motivation, or contribution. In a literature review, connect source-supported research threads and explain prior work; do not add contrasts with the present paper by default. In Methods, remove repeated explanations while preserving operation order. In Results and the ending, preserve the study design's way of supporting its answer. These are reader functions, not mandatory paragraph labels. Prefer connected prose over contribution lists, metric lists, or one-sentence paper summaries unless that structure is requested or required.

## Check words and sentences for professional usage

Resolve the intended concept before choosing its name. Use the supplied definition, operation, measurement, or argument to determine what the expression denotes, its scope, and any property or mechanism the name implies. A fluent, familiar word can still identify the wrong object, quantity, relation, or inferential status. A rare expression can be exactly right.

Assess conceptual correctness separately from linguistic form. For a concept mismatch, explain the evidence and correct the name or proposition. For awkward phrasing with a sound concept, repair the word combination, grammar, modifier attachment, pronoun, or verb while retaining the technical term. For a correct passage, keep it. For unresolved meaning, ask a targeted question or mark the uncertainty instead of inventing a definition or silently choosing a synonym.

Source fidelity preserves scientific meaning without requiring awkward wording from working notes to become manuscript prose. Express a clear concept idiomatically when the source wording is informal or literal. Preserve established technical terms, exact quotations, and author-approved wording unless a specific justified correction is in scope.

Use specialist terminology at the level appropriate for the audience. Retain established terms, precise distinctions, legitimate disciplinary metaphors, and clearly defined author-introduced concepts. If specialist usage is uncertain, check a relevant authoritative source when needed and permitted; unfamiliarity alone is not evidence of misuse. A term used correctly in one field or sentence may mean something different elsewhere. Do not apply a global replacement or blacklist.

Keep names stable for the same concept in the same role, while preserving meaningful distinctions between related concepts. Check definitions, scope, units, conditions, modality, and evidence status before accepting a replacement. A proposed simplification must not narrow a whole to one subset, change a mechanism, convert association into causation, or upgrade a measured result into a guarantee. Terms such as significant, robust, optimal, and causal are legitimate when their contextual meaning and support warrant them. Author-defined names do not by themselves establish a construct's validity or an empirical effect.

Prefer concrete operations and observations to inflated labels. Professional prose does not require rare synonyms, extra nominalizations, or a particular grammatical voice. State who does what to which object, and repair only the expression or reasoning that creates a specific problem. Preserve exact quotations and code identifiers; check all in-scope references when a conceptual correction changes terminology.

Apply the same concept and evidence checks to the audit itself. Do not add an unreported mechanism, mathematical form, or property while paraphrasing a definition or explaining a finding. Keep an unspecified operation unspecified. For a named experimental condition or author-defined construct, check its operational definition and surrounding table or paragraph before classifying the label. If the operation is correct but the shorthand may mislead, report a naming clarification and consider a local gloss; do not call it a scientific error merely because the label is abbreviated.

For each consequential finding, give the phrase, supported meaning, specific mismatch or language defect, and smallest justified action. Separate conceptual errors, ambiguity, and optional wording preferences. Read [concept and language checks](references/word-choice.md) when a term seems unusual or a plainer replacement might alter meaning.

## Simplify the sentence without simplifying the science

Find the main subject and action. Put them close enough that the reader need not retain several intervening clauses. Prefer a concrete verb over a chain of abstract nouns. Name an ambiguous referent when the evidence identifies it.

Split a sentence when nested conditions, several independent claims, or stacked qualifications obscure its main assertion. Keep each condition and exception attached to the claim it limits. A long but clear theorem statement may need no change. There is no universal word limit, sentence quota, ban on passive voice, or requirement that all sentences be short. Read the new sentences together to avoid a clipped sequence that loses contrast or cause.

## Remove repetition and formulaic scaffolding

Compare propositions and reader functions, not repeated words alone. Merge adjacent sentences that say the same thing, delete empty previews or summaries, and remove praise or assurances that add no evidence. Generic openings, repetitive transitions, forced three-part lists, and symmetrical “not X but Y” constructions deserve scrutiny when they displace a concrete point. They are not prohibited vocabulary or reliable signs of AI authorship. Retain a contrast when the distinction matters scientifically.

Keep technical terms stable rather than cycling through synonyms to create variety. A definition and its later application have different jobs. A standalone abstract or caption may need a concise restatement. Repeated numerical results can be useful across these contexts, but narrating every table entry again seldom adds interpretation. Do not trade a redundant paragraph for an unexplained appendix pointer.

## Verify the result and stop

Reread the connected passage for logical progression, accurate terms and word combinations, clear referents, manageable clause structure, and a distinct purpose for each sentence. Check punctuation in context rather than using global replacement. Verify the diff against the supplied quantities, citations, assumptions, uncertainty, scope, and negation. Necessary limitations are part of the argument.

Compare the earlier and revised passage for two distinct outcomes, the intended problem being resolved and valid reasoning and information being retained. Follow propositions and logical dependencies rather than word count. Check moved content at its destination. Preserve supported factual corrections and useful compression, and restore only actual losses. If the earlier version or destination is unavailable, identify that limit instead of claiming a complete comparison. Use the study's disciplinary meaning, not a generic editor persona, to judge technical equivalence.

For paired reviewer replies and manuscript edits, keep the response's explanation of changes separate from the paper's explanation of the research. Use honest proposed or completed status. Preserve a quotation of revised text exactly when it is presented as such.

Return the requested text and brief reasons for material edits, or located findings for an audit. Distinguish logic corrections from the chosen style preference. Leave sound passages unchanged and stop once the named problems are resolved. Do not invent new claims or perform a whole-paper rewrite to demonstrate activity.

Read [the editing examples](references/examples.md) when punctuation exceptions, sentence splitting, or repetition are ambiguous.
