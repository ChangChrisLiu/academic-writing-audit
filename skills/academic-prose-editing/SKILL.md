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

## Check words and sentences for professional usage

Choose established field terminology for the intended concept and ordinary precise language for its explanation. Check meaning in the supplied definition, method, glossary, or relevant source before choosing a replacement. Distinguish a real term of art or a clearly defined new concept from a vague invented label. An unfamiliar word is not automatically wrong. If its intended meaning cannot be recovered, flag that ambiguity rather than silently guessing.

Check word combinations, prepositions, verb choice, modifier attachment, and pronoun reference in the whole sentence. Replace awkward literal translations, inflated synonyms, vague labels, and colloquial praise with a concrete description of the actual operation or result. State who does what to which object. Professional prose need not use rare words, impersonal constructions, or extra nominalizations. Retain first person or passive voice when it is accurate and appropriate to the author's style.

Name the object according to its actual definition. If the intended object is a dataset, call it a dataset rather than substituting buffer to sound technical. A conventional term can still be wrong for the object at hand. Use buffer only when the described buffering or replay behavior warrants it, and preserve the distinction between a whole collection and its training subset. Check all in-scope mentions when repairing a misleading name.

Keep one term for one concept and distinct terms for distinct concepts. Check consistency across the in-scope text, captions, and notation. Do not interchange technical quantities or strengthen evidential meaning through a supposedly smoother synonym. Terms such as significant, robust, optimal, validated, and causal need the meaning and support claimed in that context; none is a universal banned word. Define an essential unfamiliar term on first use when needed for the target readership, without re-explaining it at every occurrence.

For a consequential wording finding, identify the phrase, its intended meaning, why the current usage misleads or distracts, and the smallest supported repair. Separate incorrect terminology, ambiguous meaning, and optional editorial preference. Read [word choice and sentence usage](references/word-choice.md) when a plain-language replacement might change a technical concept.

## Simplify the sentence without simplifying the science

Find the main subject and action. Put them close enough that the reader need not retain several intervening clauses. Prefer a concrete verb over a chain of abstract nouns. Name an ambiguous referent when the evidence identifies it.

Split a sentence when nested conditions, several independent claims, or stacked qualifications obscure its main assertion. Keep each condition and exception attached to the claim it limits. A long but clear theorem statement may need no change. There is no universal word limit, sentence quota, ban on passive voice, or requirement that all sentences be short. Read the new sentences together to avoid a clipped sequence that loses contrast or cause.

## Remove repetition and formulaic scaffolding

Compare propositions and reader functions, not repeated words alone. Merge adjacent sentences that say the same thing, delete empty previews or summaries, and remove praise or assurances that add no evidence. Generic openings, repetitive transitions, forced three-part lists, and symmetrical “not X but Y” constructions deserve scrutiny when they displace a concrete point. They are not prohibited vocabulary or reliable signs of AI authorship. Retain a contrast when the distinction matters scientifically.

Keep technical terms stable rather than cycling through synonyms to create variety. A definition and its later application have different jobs. A standalone abstract or caption may need a concise restatement. Repeated numerical results can be useful across these contexts, but narrating every table entry again seldom adds interpretation. Do not trade a redundant paragraph for an unexplained appendix pointer.

## Verify the result and stop

Reread the connected passage for logical progression, accurate terms and word combinations, clear referents, manageable clause structure, and a distinct purpose for each sentence. Check punctuation in context rather than using global replacement. Verify the diff against the supplied quantities, citations, assumptions, uncertainty, scope, and negation. Necessary limitations are part of the argument.

For paired reviewer replies and manuscript edits, keep the response's explanation of changes separate from the paper's explanation of the research. Use honest proposed or completed status. Preserve a quotation of revised text exactly when it is presented as such.

Return the requested text and brief reasons for material edits, or located findings for an audit. Distinguish logic corrections from the chosen style preference. Leave sound passages unchanged and stop once the named problems are resolved. Do not invent new claims or perform a whole-paper rewrite to demonstrate activity.

Read [the editing examples](references/examples.md) when punctuation exceptions, sentence splitting, or repetition are ambiguous.
