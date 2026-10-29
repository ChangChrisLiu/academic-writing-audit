# First-draft progression

This v0.9.1 record covers a focused revision to the existing drafting and audit skills. It adds no skill names. The main drafting reference is [section reasoning](../../skills/research-manuscript-writing/references/section-reasoning.md), and the independent literature entrypoint is [related-work-synthesis](../../skills/related-work-synthesis/SKILL.md).

An ordinary abstract now defaults to at most six sentences, retains the motivation-to-contribution reasoning, and closes in the principal supported result. Six is a ceiling, not six mandatory slots or permission to overload sentences. Required author and venue formats take precedence. The introduction chooses its opening and route to the question before prose, with constraints scoped to the particular approaches they describe. Literature develops that question without a preset number of directions, a method-family catalogue or an invented lineage among papers. The [Chinese guide](../../docs/manuscript-guide.md) describes the same workflow.

## Procedure and retained evidence

Three fresh-context participants answered seven fictional task units across engineering, urban acoustics, qualitative research, theoretical analysis and a retrospective clinical comparison. One additional participant answered the engineering packet without repository-skill guidance. A separate assessor read the fixed rubric and full outputs. Labels were visible, so the assessment was independent of drafting but not blinded. See the [cases](cases/engineering.md), [literature packet](cases/literature.md), [abstract edge cases](cases/abstract-edges.md), [rubric](rubric.md), [initial freeze](design-freeze.json), and [run metadata](run-metadata.json).

The full initial [engineering](runs/engineering.md), [literature](runs/literature.md), [edge-case](runs/edges.md), and [control](runs/control.md) answers remain unchanged. The [initial assessment](assessment-initial.md) identifies no material failure. It records an optional cohesion concern and judgment uncertainty in Literature A rather than declaring the initial passage wrong.

| Abstract task | Observed sentences | Evidence boundary retained |
| --- | --- | --- |
| Engineering | 4 | Retrospective held-out evaluation, matched observation budget and detection-delay comparison |
| Theory | 4 | Supplied scalar, noiseless theorem and its assumptions |
| Qualitative study | 3 | Interview scope and the reported exception |
| Results pending | 2 | Explicitly provisional; missing results described outside the passage |
| Mandatory structured format | 7 | Required headings and count, observational association and confounding |

The [control assessment](assessment-control.md) finds both engineering drafts scientifically supported. The guided answer is shorter and ends directly in the numerical result. The control retains a qualified interpretation after its result, more explanation and secondary evidence, and two explanatory colons. The control packet did not prohibit that punctuation. These differences do not establish a causal skill benefit; added explanation and necessary qualification are not automatically defensive writing.

## Targeted refinement

The initial literature output accurately distinguished the source mechanisms and endpoints, but its move from event timing to amplitude weighting had only a broad topical connection. The coordinator refined two policy locations to treat sources as candidates rather than a coverage checklist. A relevant study may establish, qualify or challenge the needed scientific point. Tangential material can be omitted, while consequential counterevidence must remain. A stronger transition must never be fabricated merely to retain every source.

A new fresh-context participant used the same literature packet and rubric, without prior outputs or assessment. The [regression freeze](regression-freeze.json) identifies the revised skill bytes, and the complete [regression answer](runs/literature-regression.md) retains the sound social-science paragraph verbatim. Its acoustic passage omits the amplitude-only result and explains that scope choice outside the manuscript. The separate [regression assessment](assessment-regression.md) records the judgment and its remaining limits.

The two changed initial policy files are preserved as byte-identical text snapshots under `skill-versions/initial/`; the map in the regression freeze identifies them. All other initially frozen skill bytes remain unchanged in the released folders. This preserves both policy states without duplicating whole standalone bundles. The [manifest](manifest.json) checks those snapshots, released skill files and this record. The initial freeze covers four changed bundles, but participants invoked only the drafting and literature skills. The broad audit and story audit received consistency checks, not new direct behavioral trials.

## Boundaries and maintenance

These are small synthetic development regressions, not held-out research validation, repeated sampling, a general reliability estimate or an authorship detector. Directory restrictions and withheld rubrics were prompt instructions, not enforced filesystem isolation. The coordinator generalized lessons from private editorial history; participants received only fictional packets. No private manuscript text, result, reviewer comment or filesystem path is published here, and the original manuscripts were not edited.

No live reference retrieval, scholarly authenticity check, document compilation, rendered layout inspection, native Word operation or complete research-team workflow was performed. Plain text and LaTeX snippets do not establish those operations. The [structural record](structural-checks.json) records maintenance checks separately from editorial judgments. The 23 existing validator and packaging tests passed; their scripts and shared policy sources are unchanged. Previous evaluation artifacts retain their bytes and expected hashes, with only the v0.9.0 manifest's resolution metadata pinned before editing tested skills. The maintained evaluation index links this new record.
