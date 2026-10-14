# Response-writing development fixtures

Added with v0.3.0 on 2026-10-14 for [reviewer-response-writing](../../skills/reviewer-response-writing/SKILL.md).

- [Three fictional requests and source packets](cases.md): a constrained rebuttal, a revision letter with mixed change status, and a narrow audit.
- [Semantic criteria](rubric.md): coverage, evidence scope, completion status, manuscript independence, and preservation of valid text.
- [Manifest](manifest.json): hashes of the v0.3.0 installable skill, fixtures, and criteria. Paths resolve in its recorded source Git commit, not necessarily in the current checkout.

These three cases were published with v0.3.0 as development fixtures and expected behaviors, not recorded model responses. At that release, the author had reviewed the examples and checked package structure, local links, metadata, and standalone installation, but had not run independent behavioral trials.

Later [cross-domain trials and a targeted clarification](transfer/README.md) use a separate case set, including complete outputs and independent assessment. Do not count the three fixtures on this page as executed trials. Their original hashes are preserved against source commit `a01ae7938c20a3c8a6c53b982d0a9e0977f44f6c`; the manifest now records that revision explicitly so later skill changes do not rewrite history.

To run a future trial, provide one case and its source packet in a fresh context. For a guided run, also provide the skill and access to its local references. Keep the rubric, other responses, and originating private materials out of that context. Save the full output, record which files were read and the model/runtime if available, and inspect it against the semantic criteria. A no-guidance control is useful when assessing added value. Report model or editorial failures alongside successes.

The [original full-audit trials](../README.md) and [v0.2 focused-skill trials](../library/README.md) remain separate historical records. Their hashes and results were not changed by this addition.
