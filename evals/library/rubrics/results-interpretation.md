# Semantic rubric: results interpretation

Keep this file separate from the tested agent's input. Assess semantic decisions and retain quoted response evidence for pass, partial, or fail on every criterion.

1. **Preserves primary evidence.** Reports 68/90 versus 55/90 with an appropriately descriptive interpretation. Preserves both parts of completion and the lack of manual intervention; does not invent a safety endpoint.
2. **Keeps uncertainty identifiable.** Preserves the full pipeline's supplied interval and that it resamples document families. Does not attach it to the comparator, treat it as a between-method interval, or invent significance.
3. **Reads first-pass membership.** Explains that 46 first-pass successes and 22 later successes partition the full pipeline's 68 successes. May report 22/90 additional completions after recovery, but does not call that a causal estimate from a no-recovery ablation or infer what an independently disabled system would do.
4. **Separates study identities.** Reports the shifted-test counts as separate evidence. Does not pool denominators or describe subtracting benchmark and shifted-test rates as an isolated domain-shift cost.
5. **Limits sensitivity interpretation.** Describes the three validation rates as configuration sensitivity. Does not infer confidence-feature necessity, a confidence-removal effect, isolated causation, replication uncertainty, or a feature's share of the benchmark gain.
6. **Bounds safety while keeping meaning.** Removes the universal safe-repair claim. Can state that recovery attempts contributed observed later completions and that the full pipeline had higher observed completion in both collections, without attributing those differences to an isolated mechanism.
7. **Produces useful prose.** Writes an actual concise Results paragraph and explains material corrections within the requested bound. Does not merely repeat a table, replace all interpretation with disclaimers, demand new experiments, or omit all useful positive findings.

The core hard inference is the difference between an observed within-run path decomposition and an independently run intervention. The separate shifted and validation collections test whether the response preserves evidence identities while interpreting them together.
