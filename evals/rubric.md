# Behavioral evaluation

The fixtures are fictional. None contains manuscript excerpts or experimental results from the originating project. Assess meaning, not keyword matches or a preferred sentence.

## Editorial scenario

Give a fresh agent `editorial-scenario.md`. For a control run, provide no skill. For a guided run, also provide `skills/academic-writing-audit/SKILL.md` and access to its references. The fixture's restriction on additional skills excludes the skill under evaluation in the guided condition. Do not provide this rubric, another run's answer, or expected findings to the agent before its response.

Evaluate each dimension independently:

1. **Author preservation:** P1 has a coherent problem-to-proposal progression. Leave it unchanged unless the agent identifies a concrete defect; a synonymous preference is insufficient.
2. **Attribution:** Remove the unsupported claim that selection or an individual feature caused the gain. Do not imply that a higher selected score establishes a physical mechanism or general robustness.
3. **Comparison identity:** Retain all four reported counts and identify the shifted-lighting experiment as separate. Do not combine denominators or subtract results across studies.
4. **Budget and support:** Distinguish equal nominal updates per fit from five fits versus one and unequal eligible records. Do not assert equal total computation or otherwise matched training data.
5. **Endpoint:** Retain both parts of success, the label-freezing timing, and the fact that evaluation involved no real release. Remove the absolute safety guarantee and repeated reassurance.
6. **Ablation operation:** Removing failed attempts removes records; operator-quality labels remain. Do not reinterpret the variant name as removal of labels or invent its outcome.
7. **Definition:** Explain the fixed linear rule versus the normalized nonlinear mapping in ordinary language. Link the appendix to concrete parameter details.
8. **Proportionality:** Keep useful interpretation at the level supported by the evidence. Do not add new experiments, fabricated uncertainty, a response to reviewers, or a catalogue of hypothetical flaws.

Report pass, partial, or fail with a quoted fragment and rationale. Report each dimension; do not obscure a failure in a composite score. A pass in a synthetic fixture does not establish effectiveness across models, disciplines, or real manuscripts.

## Transfer scenarios

Run `transfer-scenarios.md` with the skill in a fresh context. Expected behavior:

- T1: Read-only review; distinguish source assertions, missing evidence, and a stale memo; preserve a valid negative definition; do not claim compile/render verification.
- T2: Retain the mathematical assumption and the local nature of the result; do not demand experiments or a statistical test for a deductive claim.
- T3: Preserve the negative case and the limits of the qualitative sample; do not convert participants' reported explanations into a demonstrated causal effect.
- T4: Make only the requested grammatical change. Do not expand a grammar request into a full scientific audit.

Inspect the complete responses manually. Automated phrase searches are insufficient: correct answers may quote a bad sentence to explain its problem.
