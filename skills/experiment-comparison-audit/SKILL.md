---
name: experiment-comparison-audit
description: Check experimental baselines, ablations, data eligibility, selection, and resource budgets against their actual implementations or records. Use when interpreting what a comparison isolates or correcting an ambiguous comparator definition.
license: MIT
---

# Experiment Comparison Audit

Make each comparison understandable in terms of what actually changes. Preserve useful experiments while matching their interpretation to their design. A difference between variants is not automatically a flaw; it determines which question the comparison answers.

## Recover the operation

Locate the relevant variant definitions, source/configuration records, and evaluation protocol. Resolve names against these records rather than trusting labels such as “fixed,” “uniform,” “no feedback,” or “without recovery.” If a historical run matters, distinguish its recorded configuration from today's implementation.

Define a comparator in plain operational language before giving its acronym or appendix pointer. For example: “The baseline assigns one of two fixed weights using a confidence threshold.” Put pointers on coefficients and detailed procedures; repeating a rule's name does not define it.

Two fixed baselines can use different rules. A preset parameterization of the proposed formula differs from a separate fixed transformation. Conversely, an identical formula does not establish identical inputs, eligible records, coefficients, or selection procedures.

## Compare only consequential axes

Use the smallest matrix needed to resolve the scientific claim:

| Axis | Establish |
| --- | --- |
| Rule | Transformation, decision procedure, loss, and operation order |
| Information | Available sources, features, labels, and annotations |
| Eligibility | Which observations may actually contribute after gates or filtering |
| Fitting | Initialization, updates, batch size, and relevant exposure differences |
| Selection | Preset parameters, tuning candidates, validation choice, and retuning |
| Resources | Budget per fit versus all candidates, including measured costs if available |
| Evaluation | Units, endpoint, trial set, interventions, and aggregation |

Match distinctions to the claim. Do not turn a narrow definition check into a compulsory exhaustive audit. If an axis is unknown and consequential, mark it unknown rather than assuming equality.

Equal starting pools do not establish equal eligible training data. Equal nominal updates per fit do not establish equal total search cost or effective weighted exposure. Candidate counts establish how many fits were performed, not an exact ratio of wall-clock time or energy unless those quantities were measured. Retain genuine controls, such as a shared architecture, while correcting an overbroad “identical budget” statement.

## Read ablations literally

Specify the intervention and what remains. Removing a source of examples differs from removing a label on retained examples. Disabling a feature differs from changing coefficients while retaining it. A subset labeled retrospectively is not an independently run intervention.

State whether an ablation reuses full-system settings or retunes the reduced system. A removal comparison at one chosen setting answers a conditional question; it need not be discarded, but it does not automatically estimate the best reduced system or isolate selection's contribution. Combined changes do not identify each change's causal share.

## Prose when drafting or revising

Use connected paragraphs with concrete subjects and verbs. Remove empty staging and repeated assurances. Check the inference and referents between adjacent sentences. Simplify nested clauses while keeping conditions attached to their claims. Merge repeated propositions serving the same reader purpose, but retain necessary definitions, limitations, and standalone summaries. Keep technical terms stable. Check word meaning, natural word combinations, grammar, modifier attachment, and clear agency in context. Replace inflated or invented labels with established terminology or concrete wording without changing the concept. Preserve necessary terms of art and defined new concepts; flag uncertain meaning rather than guessing a synonym. Name the actual object consistently; a dataset should not become a buffer through stylistic substitution. Professional wording need not be elaborate. An “AI feel” is an editing concern, not an authorship finding.

This library defaults to no explanatory colons or sentence-interrupting dashes in generated prose, including spaced hyphens and LaTeX dash syntax. Preserve compound-word hyphens, notation, minus signs, ranges, ratios, URLs, citations, exact quotations, and required templates. Author or venue instructions take precedence. Do not replace paragraphs with bullet fragments, mechanically erase punctuation, or impose a sentence-length quota. Apply these checks only within the requested task; a source or submission check does not itself authorize prose edits.

## Deliver the interpretation

Return the actual comparison, consequential mismatches with the draft, and the conclusion the design supports. If wording is requested, give the smallest clear replacement and preserve supported controls and results. Keep source-removal, label-removal, and selection comparisons separately named.

State which relevant records were inspected and what remains unresolved. Do not fabricate missing baseline outcomes or describe every unmatched detail as unfairness. Stop once the variants and claim-relevant differences are clear enough to interpret the reported comparison; propose additional experiments only when the user requests design advice or a specific claim cannot otherwise be assessed.

Read [the worked example](references/examples.md) for a compact comparator and budget audit.
