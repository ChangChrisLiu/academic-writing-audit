# Contributing

Propose improvements around an observed editorial failure, not a preference for longer instructions.

1. Supply a short fictional or openly shareable passage and its relevant evidence.
2. Describe the user's requested scope and the agent's actual response.
3. Explain the scientific or reader-facing consequence of the behavior.
4. Propose the smallest change to the skill that addresses it.
5. Re-run the relevant fixture and inspect the full response for regressions.

Keep the core skill portable. Avoid mandatory model brands, provider-specific tools, universal section orders, fixed word quotas, and mandatory multi-agent workflows. Put conditional depth in the relevant reference and keep its link discoverable from `SKILL.md`.

For behavior changes, include a no-guidance control when practical. Distinguish observed results from an expected outcome. A small number of synthetic trials is useful regression evidence, not proof of general effectiveness. A no-change decision can be a passing result.

Keep descriptions and installation guidance consistent with the current format. Check frontmatter, relative links, and standalone packaging. Do not copy proprietary prompts, manuscripts, correspondence, logs, credentials, or personal filesystem paths into an issue or pull request. Use authorized, minimal source excerpts or fictional examples.

Contributions are distributed under this repository's MIT license.
