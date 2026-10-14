# Nondefensive writing

Read when a paper feels like a response letter, repeats precautions, or is being shortened. The target is a clear research argument with accurate boundaries.

## Judge function, formulation, and placement separately

For a disputed sentence, ask three questions:

1. **Function:** What would the reader misunderstand or lose if this fact disappeared?
2. **Formulation:** Does this wording convey the fact directly, or stage an anticipated objection?
3. **Placement:** Is this the point at which the reader needs it, and is the same job already done nearby?

An important fact may need a shorter sentence or a different location. A sentence containing “not,” “fixed,” “excluded,” “limited,” or “untested” may be indispensable. Neither vocabulary nor a general preference for positive wording decides the edit.

## A practical decision table

| Passage function | Typical action |
| --- | --- |
| Defines the measured endpoint, assumptions, or study population | Keep it where the result is interpreted. |
| Defines an algorithmic exclusion, fallback, or scope condition | Keep its operative meaning; place full implementation detail where needed. |
| Reveals unequal resources, data support, or tuning | Retain the difference when it changes what the comparison means. |
| Interprets a result within the available evidence | Keep or clarify; do not reduce Results to numbers alone. |
| Repeats that the procedure is fair, correct, safe, or carefully fixed | Replace with a concrete fact or delete the repeated assurance. |
| Answers an unnamed critic instead of explaining the work | Translate the underlying reader need into a definition, method, or result. |
| Lists unrelated studies that were not performed | Remove the list unless a missing study materially limits the stated conclusion. |
| Repeats technical detail already fully defined elsewhere | Retain a short operational explanation and point to the specific detail. |

## Preserve the argument while shortening

A broad motivation sentence can perform a necessary bridging job. Before cutting it, read the preceding and following sentences together. If the deletion changes “problem → challenge → contribution” into “problem → announcement,” the cut may remove the reason for the method.

Do not rewrite a sound passage to demonstrate editorial activity. For each change, identify the defect and its effect on understanding. Synonymous phrasing, a shorter word count, or matching the editor's preferred voice is not enough.

A local addition may be the smallest repair. Restore an experiment's endpoint, introduce a new object, or explain a comparison before removing surrounding prose. The goal is sufficient explanation with little repetition, not the shortest possible text.

## Turn objections into reader-facing content

| Underlying concern | Useful manuscript response |
| --- | --- |
| “What exactly is this method?” | Its input, operation, output, and role in the research question. |
| “What does the baseline do?” | A plain operational definition and the dimensions that differ. |
| “Were the comparisons equal?” | The relevant shared conditions and actual differences. |
| “Does this show mechanism X?” | The observed result and the inference the design supports. |
| “Where can I reproduce this?” | Parameters and procedural detail in an appropriate, specific location. |

The manuscript need not mention the objection or the reviewer. A response letter, when separately requested, can explain how a concern was addressed; its conversational framing should not leak into the paper.

## Do not mistake limitations for defensiveness

Keep limitations that change interpretation: measurement resolution, selection effects, unisolated mechanisms, population or platform scope, and dependencies required for the method. State them precisely, near the relevant inference or in a coherent limitations passage.

Do not distribute identical caveats after every result. Do not hide a serious limitation in an appendix solely to improve tone. A well-bounded sentence can often carry the necessary scope without an additional disclaimer: “Under the evaluated lighting shifts, the full model achieved higher observed success.”

Necessary negation can be the clearest wording. “The proof does not establish uniqueness” has a different scientific function from “We stress that our proof should not be misunderstood.” Keep the former when relevant; remove the latter.

## Assign information to a useful location

| Location | Reader's need |
| --- | --- |
| Abstract | Problem, contribution, principal evidence, bounded takeaway. |
| Introduction | Why the problem remains and why this contribution addresses it. |
| Related work | Connected prior-work threads derived from the introduction, explaining studies and their relationships. |
| Methods or analysis | Objects, operations or reasoning, and assumptions needed to understand the contribution. |
| Experimental setup | The question tested, actual comparators, endpoint, and design needed to read the results. |
| Results | Main findings and supported interpretation. |
| Ablations or additional analyses | Which manipulation or alternative explanation each analysis addresses. |
| Limitations | Consequential constraints on interpretation and applicability. |
| Appendix | Detailed definitions, derivations, protocols, and supporting analyses. |
| Internal review record | Patch history, review negotiations, hashes, and operational logs. |

Adapt these functions to the manuscript's discipline and structure. They are not mandatory section headings. A central ablation can belong in the main text; an appendix is not a default dumping ground. A concise definition may legitimately recur in a caption that must be understood independently. Repeated terms alone do not prove redundant function.

## Common failure patterns

- **Delete every negative sentence:** Recheck what assumption, endpoint, or boundary the sentence carries.
- **Replace a defense with an abstract assurance:** Write the actual operation or observation instead of “ensures rigorous validity.”
- **Preserve every sentence because its fact matters:** Improve form and placement while retaining the fact.
- **Make the article an audit log:** Keep reproducibility details that serve scientific understanding; keep review bookkeeping elsewhere.
- **Make every reviewer concern a new experiment:** First determine whether a definition, qualified claim, or existing evidence resolves it. Identify a real evidence gap when one remains.
- **Treat every mention of the same concept as repetition:** Check whether one defines it and another interprets its result.
