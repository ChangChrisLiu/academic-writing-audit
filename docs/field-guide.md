# From a writing problem to a useful repair

[Back to the library](../README.md) · [中文导航](../README.zh-CN.md#按问题选择-skill)

These patterns are generalized editorial lessons. The examples below are fictional. Choose the skill for the problem you actually have; a narrow task does not require loading the entire collection.

## 1. The introduction loses the reason for the method

**Pattern:** An editor removes a broad but coherent difficulty statement, then promotes a weighting formula into the entire contribution. The paragraph becomes shorter but jumps from the application to a technical detail.

**Repair:** Recover the problem–difficulty–contribution connection. Explain the complementary roles of the framework's operations. Retain the difficulty statement if it already supplies that connection. A component's intended role is not its experimentally isolated effect.

**Use [scientific-story-audit](../skills/scientific-story-audit/SKILL.md):**

```text
Check the argument in this abstract and introduction. Identify the exact
missing bridge, if any. Preserve coherent motivation. Do not reduce the
whole framework to its scoring rule or invent a new contribution.
```

## 2. “Remove defensive prose” becomes “delete every limitation”

**Pattern:** “We stress that the evaluation was fair” is empty reassurance. “Uncertain cases remained in the denominator” changes how the result is understood. Both can sound cautious; they do different jobs.

**Repair:** Judge the fact, its wording, and its placement separately. Replace reassurance with the supported operation. Keep eligibility rules, denominators, endpoints, and consequential uncertainty. Remove repetition only when the same reader need is already met.

**Use [nondefensive-writing](../skills/nondefensive-writing/SKILL.md):**

```text
Make this passage more direct. Explain what each proposed deletion loses.
Preserve necessary boundaries and useful interpretation. Mark an unchanged
paragraph explicitly if omitting it could look like deletion.
```

## 3. Related Work invents mutually exclusive camps

**Pattern:** A paragraph contrasts “historical-data methods” with “interactive methods,” although one cited method uses historical records and later expert annotations. Another paper already weights examples, so “we first introduce weighting” is unsupported.

**Repair:** Compare on meaningful, potentially overlapping axes. An excerpt's silence about a feature means unknown, not absent. State the present design's operational difference without inventing exhaustive priority. Keep the detailed procedure in Methods.

**Use [related-work-synthesis](../skills/related-work-synthesis/SKILL.md):**

```text
Synthesize these source excerpts around information, supervision, and
decision rules. Allow overlapping categories. Bound novelty to the source
coverage and identify claims that still need source verification.
```

## 4. The observed gain turns into an untested explanation

**Pattern:** A complete pipeline outperforms a baseline. The manuscript credits one internal filter, even though several operations changed together. A later code inspection is then offered as proof of what historical runs used.

**Repair:** Attach the observation to its actual study and comparison. State the system-level result; describe the mechanism as an interpretation only when the evidence supports that link. Use historical artifacts to establish historical execution. Current code establishes current implementation.

**Use [claim-evidence-audit](../skills/claim-evidence-audit/SKILL.md):**

```text
Map each consequential claim to its supporting evidence and permitted
inference. Separate current implementation from recorded execution.
Repair overclaims without weakening results that are actually supported.
```

## 5. Baseline names hide different operations

**Pattern:** “Fixed” could mean a linear map, a preset exponential map, or a threshold rule. Equal updates per fit are described as equal compute even though one method selects among several fits. A “no feedback” ablation removes corrected records, not just labels.

**Repair:** Define comparisons by inputs, transformations, information, fitting, and selection. Keep eligible support and effective exposure distinct from nominal budgets. Name the operation removed by the ablation and the inference that comparison permits.

**Use [experiment-comparison-audit](../skills/experiment-comparison-audit/SKILL.md):**

```text
Reconstruct the comparison from these protocol notes. Give each baseline
a one-sentence operational definition. Check support sets, per-fit and
total budgets, selection, and what each ablation actually removes.
```

## 6. Results become either bare numbers or a causal story

**Pattern:** An editor removes all explanation to avoid speculation. Another credits a recovery mechanism by comparing first-pass and final success from the same runs as if they were independent conditions.

**Repair:** Organize the paragraph around the question answered. Explain the supported pattern, uncertainty, and scope. Same-run stage counts describe contribution to the observed total; they do not supply a no-recovery counterfactual. Keep benchmark, stress-test, and internal-selection results separate.

**Use [results-interpretation](../skills/results-interpretation/SKILL.md):**

```text
Turn these results into an interpretation of the research question.
Distinguish observation from mechanism, retain uncertainty, and keep
different protocols separate. Do not invent a missing ablation.
```

## 7. The definition exists only as a formula or appendix pointer

**Pattern:** “See Appendix for the weighting scheme” replaces an explanation of what receives weights. The draft also reverses clipping and normalization or confuses rejection of a candidate with deletion of a training record.

**Repair:** State the operation in plain language before the formal detail. Track the object at each stage and preserve operation order. An appendix can supply parameters; it cannot substitute for the definition readers need now.

**Use [method-definition-audit](../skills/method-definition-audit/SKILL.md):**

```text
Explain the operation in one plain sentence, then check the formula,
object identities, transformation order, and exclusion rules against
the supplied specification. Preserve already correct definitions.
```

## 8. A beautiful figure implies an experiment that never happened

**Pattern:** An arrow routes held-out test data into optimization. A caption says treatment completed, while the evaluated endpoint was alignment and approval before treatment. A baseline branch silently receives extra sources.

**Repair:** Check visual semantics before styling: entities, arrows, grouping, timing, support sets, and endpoints. Read the actual image when available. A textual diagram description supports a semantic audit, not a claim that rendered text or layout was inspected.

**Use [figure-caption-audit](../skills/figure-caption-audit/SKILL.md):**

```text
Compare this figure, caption, and method description. Check every arrow
and endpoint against the protocol. Separate semantic corrections from
visual changes and identify any image content you could not inspect.
```

## 9. Old review verdicts drive new edits

**Pattern:** A previous note says “PASS,” but it points to an obsolete table. Reviewer concerns then accumulate as defensive sentences across the introduction, method, and results. A clarification request is treated as a demand for a new study.

**Repair:** Read the current passage independently. Translate the concern into a reader's missing information. Classify it as a definition, evidence, presentation, or genuinely unresolved research issue. Put the smallest useful repair where readers need it and check nearby repetition.

**Use [reviewer-comment-triage](../skills/reviewer-comment-triage/SKILL.md):**

```text
Map these reviewer concerns to the current manuscript. Treat prior PASS
notes as leads, not evidence. Give the current status, reader consequence,
smallest repair, and unresolved evidence. Preserve sound sections.
```

## 10. “Done” mixes source, PDF, and submission states

**Pattern:** The source has new affiliations, the visible PDF is older, the local compiler lacks the venue style, and a portal shows an uploaded draft. None of those observations proves the latest manuscript was compiled and submitted.

**Repair:** Preserve the latest source. Treat missing style files as an environment issue unless source evidence shows otherwise. Verify source identity, build outcome, rendered pages, uploaded artifact, and submission receipt separately. A handoff records the exact next action without inventing completion.

**Use [manuscript-release-check](../skills/manuscript-release-check/SKILL.md):**

```text
Check the final manuscript state from the supplied files and logs.
Distinguish what was inspected from what was merely clicked or reported.
Preserve the latest source and return a recoverable handoff. Perform
external publication only if it is within my authorized task.
```

## 11. A strong rebuttal leaves the paper unclear

**Pattern:** A reply groups major concerns and supplies new results, but overlooks a small threshold request. It describes a planned second study as finished, attributes a combined system's gain to one component, and copies “to address the reviewer's concern” into Methods. The paper's actual definition is still missing.

**Repair:** Maintain comment-level coverage even when writing by theme. Lead with a direct answer and the evidence that actually addresses it. Keep original and additional studies separate, bound causal attribution, and distinguish completed work from proposals. Write the manuscript explanation separately and verify the letter against the intended source version.

**Use [reviewer-response-writing](../skills/reviewer-response-writing/SKILL.md):**

```text
Draft a response to these comments using the supplied evidence and venue
rules. Track every concrete request, including minor ones. Separate
completed changes from proposals. Give any manuscript replacement in a
separate block that explains the science without reviewer-facing framing.
```

Read the [中文回复写作指南](rebuttal-guide.md) for the two formats and paired examples.

## Combining skills

For an unfamiliar manuscript, begin with [academic-writing-audit](../skills/academic-writing-audit/SKILL.md). If the audit reveals one concrete problem, use the focused skill for that repair. Re-read the affected context after editing and stop when the requested issue is resolved.

One agent can take the scientific, editorial, and first-reader perspectives in sequence. Separate agents are optional. An independent perspective is useful only when it reads the right current source rather than inheriting an old verdict.
