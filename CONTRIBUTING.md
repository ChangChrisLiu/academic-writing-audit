# Contributing

Propose improvements around an observed editorial failure, not a preference for longer instructions.

1. Supply a short fictional or openly shareable passage and its relevant evidence.
2. Describe the user's requested scope and the agent's actual response.
3. Explain the scientific or reader-facing consequence of the behavior.
4. Propose the smallest change to the skill that addresses it.
5. Re-run the relevant fixture and inspect the full response for regressions.

Keep the core skill portable. Avoid mandatory model brands, provider-specific tools, universal section orders, fixed word quotas, and unnecessary mandatory multi-agent workflows. The reference-authenticity workflow is an explicit exception requiring two independent agents and Google Scholar-first checks; preserve that contract and report capability limits honestly. Put conditional depth in the relevant reference and keep its link discoverable from `SKILL.md`.

For behavior changes, include a no-guidance control when practical. Distinguish observed results from an expected outcome. A small number of synthetic trials is useful regression evidence, not proof of general effectiveness. A no-change decision can be a passing result.

Role guidance must name the decision and evidence appropriate to the study design, not merely announce an expert persona. Revision tests should include both harmful losses and changes that ought to be accepted, such as concise equivalent wording or a correction to an unsupported old claim. Freeze inputs before execution, retain full outputs and disagreements, and pin historical skill versions before changing previously tested files.

Distinguish behavioral report assessments from operational tests. Reference-workflow operation claims need reviewable source captures, export files, source diffs, build artifacts, or observed native citation-field refreshes as appropriate. Static reports, cached field text, and package inspection do not alone establish those operations succeeded. Preserve failures and partial coverage.

Keep descriptions and installation guidance consistent with the current format. Check frontmatter, relative links, and standalone packaging. Do not copy proprietary prompts, manuscripts, correspondence, logs, credentials, or personal filesystem paths into an issue or pull request. Use authorized, minimal source excerpts or fictional examples.

Contributions are distributed under this repository's MIT license.
