# Supplemental adjudication: missing inputs versus study-level absence

## Status and limits

This is a **prompted follow-up**, not a second blind assessment. After the original independent assessment was completed, a separate review identified a possible scope ambiguity in statements about unavailable analyses and supplied raw data. I reread only the same original case packets and outputs for peer-review research, ecology, and materials. I did not read revised skill files, regression outputs, or the other review itself. Source paths below are relative to `open-source/academic-writing-audit/evals/reviewer-response-writing/transfer/`.

The original `independent-review.md` and `independent-review.json` remain unchanged. This supplement records a narrower reassessment of the disputed passages, including two qualifications that were not recorded in the initial matrix. It must not be represented as an additional independent trial or as a silent replacement of the initial all-pass assessment.

## Decision

The prompt exposes a genuine evidentiary-scope ambiguity. **“Not supplied in the packet” does not establish “not performed,” “does not exist,” or “unavailable to the authors.”** The disputed outputs do not explicitly say that the analyses were never performed, and nothing in the packets proves that their availability statements are false. Nevertheless, some wording can reasonably be read as a broader author/study assertion than the packet establishes.

I therefore qualify the **evidence and inference** judgments for peer-review research and ecology. I retain the materials pass because its wording preserves the input-supply distinction and its substantive status claim is explicitly about the revision. I do not identify a demonstrated false result, invented calculation, or confirmed absence claim that requires a fail. The qualifications concern the unsupported reach of an ambiguous factual statement, not a preference against limitation language.

| Case / location | Original criterion 2 | Supplemental criterion 2 | Narrow reason |
| --- | --- | --- | --- |
| Peer-review research / manuscript | pass | qualified | “is available” is unscoped and appears as an authorial statement in ordinary Results text. |
| Ecology / response letter | pass | qualified | “are available to support a stronger inference” is better contextualized, but can still claim knowledge of the authors' available analyses beyond the packet. |
| Materials / response letter | pass | pass | “was supplied” does not assert nonexistence or nonperformance; the adjacent completed-edit and revision-status claims are supported by the saved source. |

The other three criteria for these cases are unchanged. In particular, the questioned manuscript sentence is not reviewer-directed debate, and the source-versus-proposed-edit status remains accurate. This supplement does not reopen the other three cases.

## Peer-review research

Source fact in `cases/peer-review-research.md`:

> No uncertainty analysis is supplied.

Manuscript statement in `results/v0.3.0/peer-review-research/answer.md`:

> No uncertainty analysis is available for this comparison.

The source establishes what the assistant received. The manuscript sentence does not identify that scope. A normal reader of Results can reasonably understand it to mean that the authors have no uncertainty analysis available for the comparison. That broader availability claim was not established in the packet. The introductory label “Proposed replacement Results paragraph” marks edit status; it does not by itself make every unqualified factual claim inside the paragraph conditional or author-facing.

There is a charitable, narrower interpretation: no uncertainty analysis is available in the reported material supporting this paragraph. That was the reading behind the original pass. But “in the reported material” is not stated, and the phrase “for this comparison” identifies the object of the analysis, not the limits of the speaker's knowledge. On reconsideration, an unqualified pass does not adequately acknowledge this distinction.

**Consequence and supplemental verdict:** criterion 2 is qualified for this sentence. The comparison itself remains correct: 51/85 and 44/85, the rounded rates and difference, the participant label, and the abstract-level endpoint are preserved. There is no invented uncertainty estimate, unsupported significance claim, or claim that uncertainty analysis was never conducted. Criterion 1 remains pass: the issue is factual scope, not reviewer-facing voice.

The rebuttal also says:

> No uncertainty analysis is supplied, so we make no claim of statistical significance.

This mirrors the input's wording and does not assert that no analysis exists. Still, “supplied” has an unclear recipient in an author-to-reviewer letter. The useful and supported part is the limited interpretive commitment, “we make no claim of statistical significance.” The supply clause is unnecessary to convey it.

A minimal output correction, if authorized later, could omit the manuscript availability sentence and the rebuttal's supply clause while retaining the observed comparison, absence of a significance claim, and endpoint limits. Alternatively, the manuscript can limit its statement to what the proposed paragraph does: “The comparison is reported descriptively here.” None of these suggestions requires assuming that an unprovided analysis exists or was performed.

## Ecology

Source fact in `cases/ecology.md`:

> No uncertainty analysis, matching procedure, or adjustment model is supplied.

Response statement in `results/v0.3.0/ecology/answer.md`:

> No uncertainty estimates, matching results, or adjusted analyses are available to support a stronger inference.

The phrase “to support a stronger inference” narrows the relevance of the statement. The surrounding response is explicitly proposing a descriptive interpretation based on the reported means and known design limitations. This makes the disputed sentence less sweeping than a standalone declaration that no analysis exists.

Even so, an author-to-reviewer letter ordinarily speaks for the authors. A reader could interpret it as a claim that the authors have no relevant estimates, matching results, or adjusted analyses available, rather than that the assistant was not given them. The packet does not establish that broader fact. Changing “procedure” and “model” into “results” and “analyses” also makes the sentence a claim about analytic products, whose availability was not separately confirmed. This does not fabricate those products, but it adds specificity to an absence claim.

**Consequence and supplemental verdict:** criterion 2 is qualified for the scope of this response sentence. The main causal correction remains justified independently by the nonrandom assignment, missing pre-restoration measurements, and the descriptive evidence supplied. The draft correctly states what is actually known to be absent: “There are no pre-restoration richness measurements.” That sentence is explicitly supported by the packet and should not be weakened merely because another kind of absence is unconfirmed.

The manuscript has a better-scoped formulation:

> The reported means alone do not establish the precision of the difference.

This describes the information supplied by the reported means, rather than claiming knowledge of all analyses possessed by the authors. Its manuscript-independence and evidence judgments remain pass. The problem is local to the letter's availability sentence. Omitting that sentence would preserve the response's substantive answer and all supported limitations; no new analysis or author confirmation would be needed to complete that narrower draft.

## Materials

Source fact in `cases/materials.md`:

> No inferential uncertainty analysis or raw indent data is supplied.

Response statement in `results/v0.3.0/materials/response.md`:

> No inferential uncertainty analysis or raw indent data was supplied; we have not added confidence intervals, significance claims, or other inferential uncertainty estimates. Inferential uncertainty remains unquantified in this revision.

This is not equivalent to “the authors have no raw indent data” or “no uncertainty analysis was performed.” The response retains the supply predicate rather than converting it into nonexistence or unavailability. It then describes what the actual edit did and expressly limits the uncertainty statement to “this revision.” The saved manuscript supports that edit-status description.

The unresolved issue is voice and recipient: supplied to whom? In the agent's working context, the recipient is clear; in an author-to-reviewer letter, it is not. The clause can sound like an explanation of the assistant's input conditions embedded in the authors' response. That is undesirable final-draft wording, but the rubric's manuscript-independence criterion applies to paper text, and this clause is in the letter. The clause is also not demonstrably false, does not imply a new experiment, and does not alter the supported description of the completed revision.

**Consequence and supplemental verdict:** retain criterion 2 as pass, with a local editorial recommendation to remove the supply clause. The answer to R2.1 would remain complete because it already explains that the claims were softened, identifies the actual changes, and truthfully states that inferential uncertainty is unquantified in the revision. The manuscript itself avoids the issue and remains unchanged in this adjudication.

## Minimal general clarification justified

A small clarification is justified by the concrete ambiguity even though these passages do not demonstrate a fabricated analysis or an explicitly false nonperformance claim. Suggested wording:

> Treat an analysis or dataset that was not supplied as missing input, not as confirmation that it was not performed, does not exist, or is unavailable to the authors. In manuscript and response drafts, state only the supported limits of the reported evidence and the verified revision status; keep any necessary missing-input note explicitly author-facing.

This should not become a blanket prohibition on “available,” “not measured,” or other negative statements. Confirmed absences in these packets—such as no pre-restoration measurements and no measured publication-quality outcome—are substantive study facts and remain appropriate in manuscript text. Nor should this clarification trigger requests for confirmation when a useful draft can simply omit an unnecessary availability claim and retain the supported result.

The smallest useful adjustment concerns **epistemic scope**, not tone: distinguish what the assistant was given, what the manuscript reports, what the current revision changed, and what the authors or study are confirmed not to possess or have done. The original artifacts and their initial judgments remain preserved; this prompted supplement records the narrower qualifications transparently.
