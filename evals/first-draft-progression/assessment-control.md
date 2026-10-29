# Bounded engineering control comparison

## Basis and limits

This comparison evaluates `runs/engineering.md` and `runs/control.md` against `cases/engineering.md` and the same frozen rubric. The control was not instructed with the repository skill or the rubric. Consequently, a difference in conformity to a rubric-specific preference is not necessarily a failure to follow the control's original drafting request.

Both outputs preserve the substantive evidence. No material scientific failure is identified in either. The observed differences favor the guided output's brevity and conformity to several editorial preferences, while the control supplies a somewhat fuller explanation and additional valid evidence. This is a descriptive comparison of one unreplicated task, not evidence that the guidance caused the differences or would improve drafting generally.

## Shared acceptable behavior

Both drafts explain the practical monitoring problem, limited measurement budget, sparse irregular observations, and the relevance of elapsed time. They distinguish the specific online, reward-dependent exploratory approach from supervised learning on the labeled archive. Neither generalizes the cited classifier's omission of elapsed time to the entire literature.

Both abstracts accurately report 120 recorded episodes from three machines, median detection delays of 3.2 seconds and 5.0 seconds, the time-agnostic supervised comparator, and the same mean measurement count. Both identify retrospective scope, although the control does so in its final sentence rather than the result sentence. Neither invents significance, a maintenance-cost outcome, prospective deployment evidence, or causal component attribution. Both correctly call the archive a dataset and avoid an unnecessary implementation inventory.

The control's explanation that a time-discarding representation cannot distinguish otherwise identical observation sequences recorded at different intervals is a reasonable restatement of the supplied mechanism, not an invented historical or empirical claim.

## Observed differences

| Aspect | Guided engineering output | Control output | Assessment |
| --- | --- | --- | --- |
| Abstract length and progression | Four sentences, ending directly in the scoped quantitative comparison | Six sentences, with the quantitative comparison fifth and a qualified interpretation sixth | Both meet the ordinary sentence-count limit and have a coherent scientific progression. The guided version adheres more directly to the result-ended preference. |
| Abstract conclusion | Principal supported result is the final sentence | “These retrospective results support the use of elapsed-time information for this detection task; prospective performance remains to be evaluated.” | This is a localized editorial departure from ending on the principal result. It is not a fabricated finding or a broad impact slogan. The qualification is scientifically appropriate, although the retrospective scope could be incorporated into the result sentence more economically. |
| Introduction extent | Three paragraphs | Four paragraphs | The control repeats the timing rationale and research question more than necessary. This is mild redundancy, not a repeated obstacle loop or a broken argument. The guided output is more concise. |
| Mechanism explanation | Briefly explains similar observations separated by different intervals | Explains temporal context, indistinguishable sequences when timing is discarded, and the timing-aware representation | The control offers a fuller account that some readers may find useful. The extra explanation remains supported but partly overlaps across paragraphs. |
| Secondary evidence | Omits the ablation and runtime | Reports the 4.8-second ablation and runtime below 2 ms on the workstation | Both choices are acceptable. The control's numbers and scope are correct, and its final qualification avoids causal component attribution. Their inclusion is not an implementation inventory, although omission keeps the introduction more focused. |
| Explanatory colons | None in drafted ordinary prose | “Irregular sampling adds a further challenge:” and “Supervised training on labeled archived observations offers another route:” | Two explicit violations of the frozen stylistic rule in the control. They are minor editorial nonconformities, not material scientific failures. The original packet did not prohibit this punctuation. |
| Scope qualifications | Integrates retrospective scope into the reported evaluation | Uses a final abstract qualification and an explicit final introduction sentence distinguishing retrospective evidence from deployment and component-causal claims | Both preserve scope. The control is more explicit; those qualifications are not inherently defensive prose under the rubric. |

## Classification and uncertainty

**Material failures:** None identified in either output.

**Minor limitations in the control:** Two explanatory colons violate the frozen style criterion. The final abstract sentence follows the principal numerical finding with an interpretation and limitation, so the result-ended preference is less directly satisfied. Some introductory explanation and question framing could be compressed without losing a necessary premise.

**Acceptable or no-change behavior:** Six abstract sentences are allowed. The semicolon in the last abstract sentence does not conceal a module inventory. The control's secondary evidence is accurate, and its explicit evidence boundaries are justified. No citation or terminology repair is indicated. The guided output does not need to add the ablation, runtime, or a separate limitation sentence to be acceptable.

**Judgment uncertainty:** The control's final abstract sentence can reasonably be read as a supported interpretation of its result. Calling it a material failure or a generic impact slogan would overstate the problem. Likewise, the amount of introductory explanation a reader needs is partly an editorial judgment. The clear observable differences are sentence and paragraph counts, the position of the principal quantitative result, inclusion of secondary evidence, and the two explanatory colons.

These observations show that both drafts succeed on the central evidence constraints, with some stylistic differences under this particular rubric. They do not isolate the effect of any skill, establish a reliable improvement rate, or test real reference retrieval, compilation, rendering, native citation fields, or document-scale performance. The restricted-read setup is a prompt condition, not a security boundary.
