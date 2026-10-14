# Private real-manuscript audit

This development evaluation used a complete PACER manuscript source, its historical rebuttal, formal reviews, and a project-specific author clarification on 2026-10-14. The target was a local manuscript snapshot preserved on 2026-10-13, not a freshly verified live editor version. The manuscript postdates the rebuttal.

## Design

Three fresh-context agents ran an audit-only task with the v0.4.2 skills. One inspected terminology using academic-prose-editing without reviewer context. One read the main text first, then compared the rebuttal using academic-writing-audit. One audited the full rebuttal against the reviews and later manuscript using reviewer-response-writing. The main-text scope included the abstract through conclusion, captions, tables, and algorithm; the appendix supplied definition and evidence context.

The rubric and input hashes were frozen before execution. Auditors received only their request, permitted sources, and their standalone skill with its references. They were instructed not to consult the rubric, other outputs, prior judgments, memory, or network sources. Access restrictions are task instructions, not a complete sandbox or an independently reconstructed tool trace. A separate fresh-context assessor inspected the complete audits against the sources and rubric without the skills or parent conclusions.

The author explicitly supplied the project-specific meaning of one dataset name. That instruction was part of the packet, so recognizing it is not evidence of discovering the author's intention without context.

## Initial observations and repairs

The independent assessment marked 14 of 18 dimension judgments pass and four qualified, with no failures. The four qualifications concern two local problems, not four separate errors. No harmful manuscript-edit recommendation was confirmed.

| Observed audit problem | Instruction refinement |
| --- | --- |
| A potentially ambiguous name for an operationally defined condition was classified too strongly as an incorrect scientific object. | Check the definition and surrounding table or paragraph. Distinguish naming clarity from an incorrect operation, and consider a local gloss or expanded display label. |
| An audit paraphrase added a mathematical property that the source had not established. | Apply the same concept and evidence checks to the audit itself. Keep an unspecified operation unspecified rather than supplying a familiar implementation. |

The audits preserved legitimate specialist terms and distinctions, separated the historical response from the later manuscript, and recognized internal source identifiers and acknowledgments as different from reviewer-facing scientific exposition. They retained consequential limitations and did not recommend importing response scaffolding into manuscript prose.

The initial outputs remain preserved locally without edits. These observations motivate narrow refinements; they do not identify the underlying cause of model behavior or prove that a particular instruction caused it.

## Regression observations

Two new fresh-context agents repeated the terminology and response audits with the same source packets and requests, using the revised skills. They did not receive the initial outputs or assessment. Another fresh-context assessor checked both complete outputs against the sources and the [regression rubric](regression-rubric.md), without the skills, initial outputs, or parent conclusions.

The assessor marked all 12 observed-output dimension judgments pass, with no qualified or failed dimensions. Both prespecified concerns were satisfied in both outputs. Its 43 recommendation and keep checks found no harmful recommendation or material new problem. The audits retained valid technical terms and necessary limitations, did not invent missing method properties, and did not recommend placing reviewer-facing rhetoric into the scientific manuscript.

One minor caveat remains in the record. A phrase-level clarity concern was somewhat overstated because the immediate context already distinguished the studies. Repeating that qualifier would be optional; the separate evidence gap is substantive. This caveat did not support another mandatory skill change, and the complete output and assessment are preserved without editing.

These findings describe the observed outputs. The regression assessor did not inspect initial outputs and therefore made no before/after causal claim. The primary agent separately verified that original and isolated manuscript, rebuttal, and review files retained their pre-run SHA-256 hashes. Behavioral runs cover three initial skill entrypoints and two regression entrypoints; structural and installation checks cover all 13 skills.

## Privacy and verification

The manuscript, rebuttal, reviews, full audit outputs, source mappings, and independent assessments remain local. This public record contains the method, aggregate outcomes, general problem categories, and tested-skill hashes. It does not publish manuscript quotations, reviewer identities, private source paths, or correspondence. Readers cannot independently re-score the complete outputs from this public summary alone.

The primary agent compared original and isolated source-file hashes before and after the runs and confirmed unchanged bytes for all three source files. These comparisons are separate from auditor execution self-reports. Source inspection does not establish successful compilation, rendered appearance, scientific execution, venue compliance, or submission.

## Interpretation limits

This is one known development project that helped inform the skill library, not an unseen benchmark. Multiple focused audits of that project are not independent papers or models. All runs use the same configured host with no model override; exact model versions were not recorded. There are no unguided controls, repeated-sampling estimates, causal effectiveness estimates, or cross-model comparisons.

An audit-only task tests recommendations and source preservation. It does not test the safety of automatically rewriting a long manuscript. Valid no-change decisions and properly bounded uncertainty count as useful outcomes.

## Public records

[Initial rubric](rubric.md) · [Regression rubric](regression-rubric.md) · [Run metadata](run-metadata.json) · [Assessment summary](assessment-summary.json) · [File and skill hashes](manifest.json)
