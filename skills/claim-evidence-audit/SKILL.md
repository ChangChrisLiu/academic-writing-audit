---
name: claim-evidence-audit
description: Audit whether manuscript claims follow from supplied evidence, especially causal attribution, historical provenance, citation entailment, and generalization. Use for substantive claim review, not a grammar-only request.
license: MIT
---

# Claim Evidence Audit

Keep the strongest conclusion the evidence supports. Distinguish an incorrect claim from an unresolved one, and an unsupported interpretation from a valid observation. Work with the user's supplied material and requested scope; this skill does not require a particular model, tool, or empirical research design.

## Establish the question and sources

Identify the passage and whether the user wants findings, suggested wording, or edits. A review request does not itself request rewriting. Preserve an intentional definition, sound assumption, and supported result unless a concrete problem justifies a change.

Determine what each relevant source can establish. The manuscript establishes its current claims; an author clarification establishes intended meaning; current code establishes inspected behavior. A historical execution claim needs records linking the relevant version, configuration, inputs, and outcome. A later diagnostic or passing test cannot supply that link by itself. Do not demand full provenance for an editorial question that does not depend on it.

If sources conflict, identify the conflict rather than silently privileging the newest file or an old review marked “resolved.” Missing evidence does not prove the claim false.

## Test the inferential link

For each consequential claim, recover the precise subject, endpoint, conditions, and supporting evidence. Separate four levels:

- **Observation:** What the experiment, source, or analysis directly reports.
- **Interpretation:** What that observation is consistent with, given alternatives.
- **Attribution:** What the design or argument isolates as responsible.
- **Generalization:** Where the result extends beyond the studied cases or assumptions.

When multiple factors change together, keep the system-level comparison and remove unsupported component attribution. A working configuration that lacks a component does not automatically show the component is unnecessary in all settings. A selected result does not alone establish why selection helped.

Changing “proves” to “suggests” is insufficient if the causal story still has no evidential link. Repair the proposition, not just its confidence word. Conversely, retain a supported numerical difference without weakening it into vague possibility merely because significance was not evaluated.

Adapt the standard to the evidence. Check assumptions and derivation for a theorem. Distinguish participants' accounts from measured prevalence or causal effects in qualitative work. Do not impose an experimental ablation on every discipline.

When an actual cited source is available, check whether it entails the attached proposition at the relevant level: background, association, mechanism, or result. Distinguish bibliographic validity from claim support. If the source is unavailable, mark entailment unverified; do not invent its contents or expand a bounded audit into an unsolicited literature search.

## Return a usable decision

Give prioritized findings with the claim location, evidence, consequence, and smallest justified repair. Use a compact claim-to-source table only when several claims would otherwise be confused. Identify supported passages worth keeping. If editing is requested, retain the endpoint, numbers, conditions, and author terminology while correcting the unsupported inference.

Keep uncertainty close to the affected claim rather than appending a blanket disclaimer. State what was actually inspected. Stop when material claims are supported, proportionally narrowed, or explicitly unresolved within the requested scope; missing evidence need not prevent completing the supported portion. Do not invent measurements, significance, records, or verification status to close a gap.

Read [the worked examples](references/examples.md) when provenance, attribution, or citation support is ambiguous.
