# Natural prose and logic trials

Three fictional tasks were executed in separate fresh agent contexts on 2026-10-14. They exercise the new academic-prose-editing skill, the extended full audit, and the response-writing skill as individually usable entrypoints. A separate assessor inspected the complete outputs without seeing the skills or the primary agent's conclusions.

The author requested natural expression, no explanatory colons or interrupting dashes, clearer reasoning, simpler sentence structure, and less repetition. The library implements the punctuation choice as an author-overridable prose convention. These trials check behavior, not AI authorship or a detection score.

## Design and artifacts

The [case requests](cases/english-revision.md), [Chinese audit](cases/chinese-audit.md), [paired source task](cases/paired-response.md), and [semantic rubric](rubric.md) were written before writer execution. [design-freeze.json](design-freeze.json) records their hashes and those of the skill files. Writers received only their own request, frozen standalone skill, and any initial source. They did not receive the rubric or other outputs. The [run metadata](run-metadata.json) records the context restrictions and task identities.

| Case | Entry skill | Full saved output | Observed result |
| --- | --- | --- | --- |
| English environmental monitoring revision | academic-prose-editing | [Answer](results/english-revision/answer.md) and [execution record](results/english-revision/execution.txt) | Removed empty staging and repeated results, repaired component attribution, simplified nested conditions, and preserved clear motivation and protected notation verbatim. |
| Chinese education audit | academic-writing-audit | [Answer](results/chinese-audit/answer.md) and [execution record](results/chinese-audit/execution.txt) | Stayed audit-only, located unsupported student-outcome and objectivity claims, explained sentence complexity, and retained meaningful abstract/caption restatement. |
| Paired materials response and source edit | reviewer-response-writing | [Manuscript](results/paired-response/manuscript.md), [response](results/paired-response/response.md), [author note](results/paired-response/answer.md), and [execution record](results/paired-response/execution.txt) | Edited only Results, kept eligibility and independent units, removed causal overclaim and repetition, and separated pending author information from manuscript prose. |

The outputs and assessor files are preserved as written. The primary agent additionally checked protected passages and derived descriptive arithmetic. [Mechanical checks](mechanical-checks.json) record these comparisons; punctuation quality was assessed in context rather than by banning matching characters.

## Assessment

The [independent assessment](assessments/assessment.md), with [structured findings](assessments/assessment.json), reports 16 applicable checks passing and two dimensions inapplicable. The inspected generated prose follows the requested punctuation convention. Compound hyphens, technical colons, minus signs, ranges, URLs, and verbatim quotations remain intact. The paired manuscript contains no reviewer-facing revision narrative.

The assessor noted optional refinements without classifying them as semantic failures. The English temporal modifier could be more explicit, and the Chinese audit could be shorter. The paired letter's R1.3 remains pending author confirmation about uncertainty analysis. This honest unresolved status is compatible with passing the task, but the letter is not ready for final submission.

No instruction repair was required by these three trial outcomes. The supplied tests exercise ambiguity and preservation as well as removal, so passing does not mean every long sentence or repeated fact was deleted.

## Scope and limits

These are three guided executions on one configured host, not three models or a controlled study. There is no unguided baseline, repeated sampling, whole-paper consistency test, or measure of improved effectiveness. Only the three named skill entrypoints were behaviorally exercised for this update; all 13 packages received structural and installation checks. Other publication stages and domains remain untested by this trial set.

Execution logs are writer self-reports. The assessor inspected the actual saved outputs and source comparisons but did not reconstruct all underlying tool calls. The records do not establish real research validity, future reviewer acceptance, universal naturalness, or cross-model reliability. No AI-authorship score was computed. Historical trials elsewhere in the repository remain attached to their original tested skill versions.
