# Editorial request

Please revise this fictional Related Work passage so that readers can see the research gap and the difference from earlier systems. Keep it compact and keep useful citations. Work only from the supplied source cards; do not browse or invent references. Give a replacement passage and flag any claim you cannot establish from these cards. Do not rewrite the method section.

## Current manuscript

Prior document-triage systems fall into two mutually exclusive camps: systems that learn from archived decisions [A, B] and systems that incorporate editor feedback [C]. Archive-based systems cannot adapt their supervision to difficult examples, whereas feedback systems discard historical records. Our framework is the first to combine historical records and editor corrections. Unlike all prior work, it uses case-level evidence to determine how much each record contributes during training [A–C]. We collect archive cases, accept editor corrections, assign training weights, and choose a candidate on a development set. The next section defines these operations.

## Supplied source cards

The following are fictional excerpts supplied for this exercise, not complete papers or an exhaustive literature review.

### [A] Archive Triage Study

Uses archived editorial decisions for supervised fitting. An uncertainty score identifies archive cases for further editor annotation, and the additional annotations are included in a later fit. The excerpt does not state whether individual examples receive different training weights.

### [B] Confidence-Weighted Archive Study

Fits on archived cases. Each case receives a training weight based on agreement among annotators. The supplied excerpt does not describe interactive editor feedback or candidate selection.

### [C] Interactive Triage Study

Starts from an archive-trained model. Editors correct selected decisions during a later collection phase. Retraining combines retained archive cases with the corrected cases, using equal example weights. A development set selects the stopping point for retraining.

## Supplied description of the present work

The framework retains archived cases and later editor corrections. It assigns training weights using both source identity and a case-level consistency signal. It compares several fixed weighting settings on a development set before evaluating the chosen model on a separate test set. The manuscript contains no exhaustive novelty search or experiment comparing these systems.
