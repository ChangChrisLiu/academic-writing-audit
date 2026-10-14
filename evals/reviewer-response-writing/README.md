# Response-writing development fixtures

Added with v0.3.0 on 2026-10-14 for [reviewer-response-writing](../../skills/reviewer-response-writing/SKILL.md).

- [Three fictional requests and source packets](cases.md): a constrained rebuttal, a revision letter with mixed change status, and a narrow audit.
- [Semantic criteria](rubric.md): coverage, evidence scope, completion status, manuscript independence, and preservation of valid text.
- [Manifest](manifest.json): hashes of the new installable skill, fixtures, and criteria; paths are relative to the repository root.

These are development fixtures and expected behaviors, not recorded model responses. The author reviewed the examples and instruction coverage and checked package structure, local links, metadata, and standalone installation. No independent agent trial or control/guided comparison has been run for this skill. Do not count these cases as passing behavioral tests or infer effectiveness from packaging checks.

To run a future trial, provide one case and its source packet in a fresh context. For a guided run, also provide the skill and access to its local references. Keep the rubric, other responses, and originating private materials out of that context. Save the full output, record which files were read and the model/runtime if available, and inspect it against the semantic criteria. A no-guidance control is useful when assessing added value. Report model or editorial failures alongside successes.

The [original full-audit trials](../README.md) and [v0.2 focused-skill trials](../library/README.md) remain separate historical records. Their hashes and results were not changed by this addition.
