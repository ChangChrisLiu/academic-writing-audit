# Argument and evidence

Read for a scientific logic audit, an ambiguous comparator, or a claim that seems stronger than its support. Adapt the questions to the discipline: a proof, archival interpretation, interview study, simulation, and controlled experiment establish different kinds of knowledge.

## 1. Establish what each source can prove

There is no universal file that overrides every other source. Determine authority for the question being asked.

| Source | Establishes | Does not by itself establish |
| --- | --- | --- |
| Current manuscript | What the paper presently claims | That a claim is true or an experiment occurred |
| Author clarification | Intended meaning, terminology, authorized scope | Missing measurements or independent verification |
| Current implementation | Behavior of the inspected version | What an earlier run executed |
| Run record and retained output | The linked configuration and observed output | A different run, protocol, or undocumented causal explanation |
| Proof or derivation | Consequences justified under its assumptions | Claims outside those assumptions |
| Interview or archival material | The documented accounts and source content | Unmeasured prevalence, causation, or universal interpretation |
| Earlier review or handoff | Prior concerns, decisions, and navigation | Current correctness, even if marked “resolved” |
| Figure or demonstration | What is actually depicted in its context | Unreported performance or a general safety guarantee |

Inspect source conflicts; do not silently favor the newest-looking file. If historical execution matters, look for the linkage between source/configuration, consumed data, procedure, and reported outcome. An editorial task need not reconstruct a complete repository history when no claim depends on it.

## 2. Recover the research argument

Write a short working account, not a new introduction:

- What problem matters, and what specific difficulty remains?
- What is the proposed contribution, and how does it address that difficulty?
- What evidence or reasoning tests the contribution?
- What conclusion follows, under which conditions?

Check the links, not just the presence of these ingredients. “Data exist → our method uses data” may omit why those data are useful or difficult to combine. “A mechanism exists → the system improves” needs an appropriate argument or evaluation. A method's implementation detail should not displace the broader contribution it serves.

Preserve complementary roles. A framework may combine data coverage, recovery behavior, and selection; reducing its contribution to one scalar formula can make technically accurate prose scientifically misleading. Conversely, do not promote an untested capability into an empirical contribution.

## 3. Follow the objects through the method

Track what each stage consumes, produces, and acts on. Typical distinctions include a participant versus an observation, a trajectory versus a training row, a recorded action versus a newly predicted action, and a candidate configuration versus a trained model.

At an unexplained transition, add the smallest bridge that identifies the relationship. For example: “Each trajectory is divided into action windows that serve as training examples.” Do not add a field dictionary when a sentence suffices.

Keep separate operations separate. Filtering training records, scoring predictions, and deciding which model is eligible for selection can share vocabulary while acting on different objects. Compressing them into “quality checks” may remove the method's meaning.

For equations, check the object, domain, normalization, operation order, and relevant exceptional case. A floor followed by an exclusion gate is not interchangeable with an unconditional positive floor. If a manuscript equation and implementation disagree, identify the discrepancy rather than cosmetically aligning the prose.

## 4. Bind each claim to its support

Use a small ledger when several claims or studies could be confused:

| Claim and location | Supporting source | Actual comparison or reasoning | Supported conclusion | Unresolved fact |
| --- | --- | --- | --- | --- |
| A claimed improvement | Study A, specified table and endpoint | Full system versus fixed rule | Observed full-system difference under that protocol | Which component explains it |

For a single sentence, a short note is enough. Do not manufacture paperwork for every line.

Distinguish these levels:

- **Observation:** What was measured, reported, or directly shown.
- **Interpretation:** What the observation is consistent with; alternatives remain when the design does not distinguish them.
- **Attribution:** What the design or argument isolates as responsible.
- **Generalization:** Which populations, tasks, settings, or assumptions the evidence can support.

Do not cure an unsupported mechanism by changing “proves” to “suggests” while keeping the same unsupported causal story. State the supported comparison or identify the missing link. Do not weaken a well-supported result merely to sound cautious.

## 5. Define what a comparison changes

For relevant comparators, identify:

| Axis | Question |
| --- | --- |
| Rule | What transformation or decision procedure changes? |
| Information | Which records, features, labels, or annotations are available? |
| Eligibility | Are the same observations allowed to contribute? |
| Optimization | What loss, initialization, updates, and effective exposure are used? |
| Selection | Is there a preset, a search, tuning, or validation choice? |
| Resources | Is equality per fit, per candidate, or over the whole procedure? |
| Evaluation | Are trials, endpoints, interventions, and uncertainty methods comparable? |

Use only the axes necessary to interpret the claim. State a comparator's operation directly: “The fixed baseline uses a preset linear rule with source multipliers.” An acronym repeated in its own definition is not an explanation. Put appendix pointers on coefficients, thresholds, or detailed procedures.

Read an ablation's actual manipulation rather than inferring it from its label. Removing a data source differs from removing a label attached to remaining data. A removal study at one chosen setting is conditional on that setting; it does not independently isolate every component or the selection strategy.

Equal update counts per fit do not imply equal total search cost, retained observations, or effective training exposure. Disclose consequential differences without automatically declaring a study invalid. Adjust the conclusion to the comparison that was actually made.

## 6. Keep studies and uncertainty identifiable

Keep benchmark, stress test, ablation, sensitivity analysis, selection study, and qualitative demonstration identities explicit. Cross-reference complementary findings, but do not pool their counts or subtract their rates as a causal decomposition without a justified analysis.

Check units, denominators, aggregation level, percentage points versus relative changes, and the unit of independence. Repeated observations from one participant or run are not automatically independent replicates. Preserve supplied uncertainty and its method. Do not invent intervals, significance, or equivalence from absent analysis; a raw numerical difference supports a descriptive comparison.

For observational and qualitative research, distinguish association, participants' explanations, and the researcher's inference. Preserve meaningful negative cases. For theoretical work, check assumptions and derivation rather than demanding an empirical ablation. Missing evidence is an unresolved fact, not proof that a claim is false.

## 7. Check agreement across the paper

The abstract, contribution list, method, tables, captions, limitations, and conclusion should name the same objects, endpoint, and claim strength. A figure caption can overclaim even when the body is restrained. A main-text summary may be shorter than its appendix but cannot contradict it.

Give enough interpretation to answer the research question. Results prose should tell the reader what the comparison means, not merely repeat a table or catalogue controls. Keep causal explanations within the evidence; preserve descriptive conclusions that are supported.
