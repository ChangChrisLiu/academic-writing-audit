# Semantic rubric: nondefensive-writing

This rubric evaluates meaning, not positive wording or minimum word count. The case is fictional.

## Core repair

- Remove reviewer-facing assurances such as “we emphasize,” “certainly,” “not an attempt,” and “we stress,” or replace them with a direct factual explanation.
- Consolidate the repeated threshold-selection fact into one accurate statement. Retain that the threshold came from development data and was fixed before inspecting test outcomes.
- Judge negation by function. Preserve the out-of-range referral rule, denominator inclusion, and missing human-review endpoint even if they retain negative wording.

## Preservation and inference

- Preserve P1's motivation-to-endpoint bridge. It is concise, relevant, and already readable; no stylistic rewrite is needed.
- Preserve the descriptive result and its supported interpretation. Removing all interpretation because it is not causal would leave an unnecessarily weak Results paragraph.
- Do not turn referrals into correct classifications, remove difficult cases from the denominator, or imply that downstream review was evaluated.
- Retain the consequential limit on human-review accuracy near the interpretation. This can replace the generic safety disclaimer and “limited experiment” assurance; deleting all limits would distort the inference.
- Do not add significance, causality, deployment benefits, or safety guarantees. A new experiment is outside scope.

## Usable output

- Return replacement paragraphs and no more than four short reasons. Explicitly stating that P1 is unchanged is acceptable.
- Keep enough explanation for the next discussion of a human-review workflow. Do not make the paper more cryptic merely to reduce word count.

Critical failures: mechanical removal of all negative statements; loss of denominator or referral semantics; deletion of the unmeasured human-review limitation; replacement of concrete facts by a new assurance of rigor or safety.
