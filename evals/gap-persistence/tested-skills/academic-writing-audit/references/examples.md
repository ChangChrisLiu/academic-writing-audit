# Worked examples

All examples are fictional. They illustrate decisions, not text to paste into an unrelated paper. A suggested rewrite is valid only under its stated facts.

## 1. Remove reassurance, preserve the temporal fact

**Source:** “We emphasize that labels were fixed before aggregate outcomes were computed. No labels were changed merely to improve performance.”

**Known fact:** Labels were fixed before aggregation.

**Revision:** “Labels were fixed before aggregate outcomes were computed.”

**Why:** The timing helps interpret the evaluation. The second sentence and rhetorical opening add assurance rather than another operative fact.

## 2. Keep a necessary negative statement

**Source:** “The evaluation measures referral accuracy; downstream treatment was not evaluated.”

**Known fact:** Only referral decisions were observed.

**Decision:** Keep. Removing the second clause could turn a decision endpoint into an implied treatment outcome. Positive wording is optional; semantic preservation is required.

## 3. Define a comparator instead of renaming it

**Source:** “Preset uses the preset map described in Appendix C.”

**Known fact:** It applies a fixed linear score with source multipliers. Appendix C lists coefficients.

**Revision:** “Preset applies a fixed linear score with source multipliers, using the coefficients in Appendix C.”

**Why:** The operation is understandable before the reader follows the appendix link.

## 4. Preserve the difference between per-fit and total cost

**Source:** “All methods use the same training budget.”

**Known facts:** Every fit uses 3,000 updates. One method searches four fits; the baseline has one fit. Effective training-record counts are not known to match.

**Revision:** “Each fit uses 3,000 updates. The selected method uses four candidate fits, while the baseline uses one.”

**Why:** Equality is scoped to the quantity actually shared. This wording does not establish equal data support or total computation.

## 5. Correct the inference, not merely its confidence word

**Source:** “The selected model's 62/80 success rate, versus 54/80 for the fixed baseline, proves that validation selection identifies the causal feature.”

**Known facts:** This is a full-system comparison. No study isolates selection or that feature.

**Revision:** “The selected model achieved 62/80 successful trials, compared with 54/80 for the fixed baseline.”

**Why:** A full-system comparison supports the observed difference. Changing “proves” to “suggests” would still introduce an unsupported account of the feature. A mechanism claim needs its own support. Do not add an unsolicited caveat after every later mention of these results.

## 6. Keep complementary results distinct

**Known facts:** Study A finds that repair-only training performs poorly from routine starting states. In a separate Study B, removing repair records from mixed-data training reduces performance under perturbations.

**Supported interpretation:** “Together, the findings are consistent with repair records complementing routine records: repairs alone do not cover routine starts, while removing them reduces performance in the separate perturbation study.”

**Boundary:** Do not pool trials, subtract cross-study rates, or claim that the studies uniquely identify recovery coverage as the cause.

## 7. Preserve a sound gap sentence

**Source:** “Archived annotations capture both routine decisions and later corrections. Their different roles make it difficult to use them as a coherent training resource. We introduce a framework that combines these records.”

**Decision:** Keep unless evidence or the surrounding text reveals a concrete problem. The middle sentence explains why combining records is a research challenge. Deleting it for brevity removes the bridge to the proposed framework.

## 8. Repair an object transition with one sentence

**Problem:** A method jumps from a collection of participant sessions to a formula over observations without defining their relationship.

**Known fact:** Each recorded answer is one observation; answers from a participant remain in the same split.

**Local addition:** “Each answer forms one observation, and all observations from a participant remain in the same data split.”

**Why:** The sentence explains both the unit and its dependency. A long implementation schema is unnecessary.

## 9. Keep a theoretical limitation

**Source:** “The argument establishes existence under continuity and compactness; it does not establish uniqueness.”

**Decision:** Keep when both properties matter to the claim. This is a precise account of the theorem's scope, not defensive prose. No empirical experiment is required to justify this kind of limitation.

## 10. Do not turn qualitative testimony into a measured effect

**Source:** “Participants said that peer discussion improved their work, proving its effectiveness across institutions.”

**Known fact:** Interviews were collected at one institution; work quality was not measured independently.

**Revision:** “Participants at the studied institution described peer discussion as helpful to their work.”

**Why:** The evidence supports the participants' accounts. It does not establish an independently measured effect or a cross-institution generalization. Retain meaningful dissenting accounts elsewhere in the analysis.
