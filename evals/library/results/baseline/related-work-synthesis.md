**Replacement passage**

Prior document-triage systems combine archived records, editor annotations, and training weights in overlapping ways. Archive supervision can be augmented with annotations of uncertain cases [A]. Another system retrains on retained archives and editor corrections with equal weights, using development data to select the stopping point [C], while confidence-weighted archive fitting uses annotator agreement to weight individual cases [B]. These approaches motivate examining how archives and later corrections should contribute jointly during training. Our framework weights both sources using source identity and case-level consistency, comparing fixed weighting settings on a development set before separate test evaluation.

**Claims the cards do not establish**

- The two mutually exclusive camps and their stated limitations are contradicted by [A] and [C], which combine archived records with additional editor annotations or corrections.
- The claim to be first to combine historical records and editor corrections is contradicted by [C]. Case-level weighting also predates the present framework in [B].
- The cards support describing the present combination, but cannot establish that it is unique across the literature: [A] does not specify weighting, and omissions in [B] do not establish the absence of feedback or candidate selection. No comparative performance advantage is established by the supplied materials.
