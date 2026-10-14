# Professional language trials

Two fictional tasks were executed in fresh agent contexts on 2026-10-14 to inspect the terminology and sentence-usage update. One used academic-prose-editing for English revision; the other used academic-writing-audit for Chinese diagnosis without rewriting. A separate assessor received the requests, rubric, and complete outputs, but not the skills or the primary agent's conclusions.

## Initial cases and results

| Case | Request | Full output | Observed behavior |
| --- | --- | --- | --- |
| English method and result | [Request](cases/english-terms.md) | [Answer](results/english-terms/answer.md) and [execution record](results/english-terms/execution.txt) | Replaced inflated labels with the actual weighting rule, corrected the error metric name, preserved defined terminology, and kept an undefined readiness claim outside the manuscript. |
| Chinese professional-language audit | [Request](cases/chinese-professional-audit.md) | [Answer](results/chinese-professional-audit/answer.md) and [execution record](results/chinese-professional-audit/execution.txt) | Identified unclear agency, unnatural word combinations, and the misnamed index while retaining legitimate specialist and author-defined terms. |

The [independent assessment](assessments/assessment.md), with [structured findings](assessments/assessment.json), reports all ten applicable checks passing. It also records optional presentation refinements without treating them as technical errors. The English author note could be shorter and its separator is optional. The Chinese preservation rationale could be more concise. Neither output silently invents the meaning of an undefined label or declares that an unavailable analysis was never performed.

## Dataset and buffer follow-up

After the initial trials and assessment, the author clarified a specific failure in which buffer was used for an object that actually meant dataset. The instructions were extended to require names that match the defined object and consistency across in-scope prose and captions. The initial frozen inputs remain tied to the intermediate commit that preceded this extension.

A new [fictional request](cases/dataset-buffer.md) compares a fixed post-training dataset with a genuine bounded input buffer. Its [separate rubric](object-naming-rubric.md) and [frozen inputs](object-naming-freeze.json) were prepared before the fresh writer executed the follow-up. The [full answer](results/dataset-buffer/answer.md) and [execution record](results/dataset-buffer/execution.txt) are preserved unedited.

A second fresh assessor reports all four follow-up checks passing in the [assessment](assessments/object-naming-assessment.md) and [structured findings](assessments/object-naming-assessment.json). The fixed collection is named post-training dataset consistently in the body, appendix reference, and caption, with training, validation, and audit-only records kept distinct. The actual input-buffer passage is preserved verbatim, as is the legacy code identifier. Optional shortening of the naming reasons is documented.

The combined record now contains three guided writer executions and two separate assessments. The ten initial checks and four later checks cover different cases and versions; they are not repeated measurements of one fixed test set. There is no comparative baseline, and the follow-up was prompted by the author's clarification rather than discovered in the initial executions.

## Evidence and limits

The [rubric](rubric.md) and initial requests were fixed before execution. [design-freeze.json](design-freeze.json) records their hashes and the tested skill inputs. [Run metadata](run-metadata.json) describes the input restrictions. The primary agent verified the exact preservation of the English definition paragraph and retained numerical values in [mechanical-checks.json](mechanical-checks.json). Saved writer and assessor outputs are unedited.

The two initial guided executions and the later targeted execution used one configured host with no unguided control, repeated sampling, or cross-model comparison. Only two entrypoints were exercised, not every skill or a whole-paper workflow. No external validation of the fictional research, rendered document, or submission occurred. Execution records are self-reports and do not independently establish all tool use. Passing these cases does not establish universal professional-language quality or the causal benefit of the skill.
