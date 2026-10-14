# Review and patching

Read when delivering a structured audit, incorporating reviewer feedback, editing files, or reporting a final check. Scale the procedure to the request; a paragraph review should not become a publication audit.

## Review outputs

Begin with the state of the argument and the most consequential issue. A useful finding contains:

| Field | Content |
| --- | --- |
| Location | Section and a stable anchor, line, paragraph, or quoted phrase. |
| Issue | The specific inconsistency, missing link, overclaim, or repetition. |
| Evidence | The inspected source supporting the diagnosis, with unresolved facts distinguished. |
| Reader consequence | What the issue changes or makes difficult to understand. |
| Minimal action | Keep, clarify, merge, move, or delete, with the proposed scope. |

Prioritize by consequence:

- **Scientific correction:** A wrong definition, conflicting result, unsupported inference, or misleading comparison.
- **Explanation repair:** Missing motivation, object transition, comparator definition, or result interpretation.
- **Optional polish:** A defensible stylistic preference that does not change the argument.

Use “confirmed,” “plausible,” or “unresolved” when uncertainty about a finding matters. An absent artifact is a limit on the review, not proof of an error. Explicitly identify sound passages to keep, especially when prior edits have over-compressed them.

## Reviewer-informed revision

Use a private concern-to-evidence map: concern → reader need → existing support → manuscript location → smallest repair. Reassess old concerns against the current draft. A resolved issue should not be reopened because an earlier memo still lists it; a “PASS” label should not suppress a current contradiction.

Do not accept or reject a review by authority alone. Give a factual reason for declining a proposed change: it deletes an endpoint, redefines a comparator, implies a new experiment, or duplicates an explanation already serving the same purpose. Where a concern requires genuinely missing evidence, record that gap instead of inventing a textual solution.

## Editing contract

For file edits, identify the exact target and keep a recoverable baseline through the existing version-control or backup workflow. Avoid overwriting unrelated copies or transferring an old local source over newer author edits.

Preserve the author-selected framing and factual content unless the requested task and evidence justify changing them. A factual correction is not forbidden by a preservation rule: make it explicit and verify dependent references. Treat findings, equations, numerical values, labels, citations, and assets as protected from incidental stylistic changes.

Every patch needs a reason tied to the current text. If another writer or agent supplied the draft, inspect it against the same evidence; delegated prose is a proposal, not authority. Respect an expressly requested writing/review division without hardcoding any model or service into the workflow.

For automated replacement, use enough exact source text to identify one occurrence. If it matches zero or multiple times, re-read the source and resolve the anchor before editing. A possible record is:

```json
{
  "location": "Methods, paragraph defining the evaluation subset",
  "action": "clarify",
  "reason": "The existing wording does not identify which observations are scored.",
  "evidence": "Protocol, evaluation-subset definition",
  "old": "Exact text from the inspected current source",
  "new": "The proposed local replacement"
}
```

Use this structure only when helpful. A sentence replacement or tracked change may be clearer. For a move, verify both removal and destination; avoid duplicated explanations or a dangling reference. For deletions, read the newly adjacent sentences together.

## Verification proportional to the edit

**Prose and scientific meaning:** Re-read the paragraph and its neighbors. Check the research question, object identities, comparator operations, endpoint, quantities, and claim strength. Confirm that a shortened passage still explains why the next step exists. Check affected captions and summaries when their meaning depends on the edit.

**Source:** Inspect the actual diff. Confirm intended edits and preserved equations, numbers, citations, and labels. If an intended correction changes one of these, verify its dependent uses rather than asserting blanket invariance.

**Rendered artifact:** When the task includes a formatted final artifact, compile or render in an environment containing the required dependencies. Inspect diagnostics and the affected pages from that source revision. Missing styles or fonts can be environment blockers; an old preview or a click on “compile” is not fresh verification. If rendering is unavailable, retain the source and state the limit.

**External state:** A saved source, exported PDF, upload, and confirmed submission or publication are separate observations. Report only the steps actually completed. This skill never implies authorization to publish, submit, email, run hardware, or launch experiments.

## Three reading perspectives

Use these perspectives in one agent. Separate agents are optional if the user and environment authorize them.

- **Scientific reader:** Do claims follow from the actual study or argument? What is confounded or undefined?
- **Editor:** Does each paragraph advance the question and contribution? Is there unnecessary repetition or revision?
- **First-time reader:** Can the reader follow objects, definitions, and transitions without reconstructing the project history?

If independent review is used, provide current source and evidence before earlier conclusions to reduce anchoring. Resolve disagreements using a specific passage and its evidence. Do not average recommendations or let a vote replace reasoning.

## Stop conditions

Finish once the requested scope is reviewed, necessary repairs are made or clearly specified, and verification supports the reported state. Return any remaining issue with the exact missing fact or artifact. Avoid another polish loop merely because a different phrasing is possible. “Keep as written” and “not verifiable from the supplied material” are valid outcomes.
