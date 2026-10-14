# Worked examples

All scenarios and numbers below are fictional. They illustrate decisions, not text to paste into every audit.

## Combined changes and historical code

**Request:** “Check this claim and make the smallest correction.”

**Draft:** “Validation selection increased correct classifications from 29/48 to 37/48. The gain was independent of color cues because the current preprocessing code discards color.”

**Evidence:** The two configurations differ in both training augmentation and selection. The current grayscale preprocessor was introduced after those runs. The old input configuration is missing. The retained evaluation table supports both counts on the same test set.

**Decision:** Preserve the comparison. Do not attribute its difference specifically to selection, assert the old inputs were grayscale, or conclude color is irrelevant. There are two gaps: a combined-change comparison and unresolved historical input provenance.

**Minimal revision:** “The selected configuration correctly classified 37/48 test items, compared with 29/48 for the preset configuration. Augmentation and selection differed between configurations, so this comparison does not isolate selection's contribution.”

**Separate audit note:** “The current preprocessor removes color, but its later introduction does not establish the inputs used in the reported runs. The claimed independence from color cues is unresolved.” The note belongs beside the relevant method statement if that statement matters; it need not clutter every Results sentence.

## A real reference can still fail to support a claim

**Draft:** “Peer feedback improves assessment accuracy, as established by Study A.”

**Source excerpt:** Study A reports that eight interviewees believed feedback changed their scoring habits. It contains no accuracy measure.

**Decision:** The source supports a reported perception, not a measured accuracy improvement. A valid title, identifier, and publication record would not cure this mismatch.

**Supported wording:** “In Study A, interviewees reported that peer feedback changed their scoring habits.” Keep the attribution to participants. Do not invent missing outcomes or treat the absence of accuracy measurements as evidence that feedback has no effect.
