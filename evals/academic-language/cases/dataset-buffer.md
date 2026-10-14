# Fictional object-naming revision

Revise the two supplied passages and the caption for accurate professional language. Use the supplied definitions, retain all important scope distinctions, and keep the code identifier verbatim. Return connected paragraphs under separate A and B headings with a brief reason for naming decisions. Do not fetch external facts. Avoid explanatory colons and sentence-interrupting dashes. The request concerns writing, not changes to software.

## A fixed research collection

The object D is a fixed dataset of compiled environmental observations used for post-training. Its eligible records are partitioned into training and validation subsets before fitting. D also retains rejected records for audit; rejected records are in neither fitting nor validation. The intended term is post-training dataset. The paper's appendix reports the same whole D, not only the records used for fitting. No queue, eviction policy, or experience-replay operation is part of this object. The implementation key `buffer_path` is a legacy identifier and must remain unchanged.

Draft body

We assemble a post-training buffer D from the observations. The buffer is partitioned before fitting, and the learning reservoir retains rejected records for audit. Appendix C reports the composition of the training buffer. The implementation reads `buffer_path`.

Draft caption

Composition of the post-training buffer D, including the training and validation subsets and rejected records retained for audit.

## B an actual input buffer

The acquisition service has a bounded memory queue of 32 incoming measurements waiting for processing. The source calls this the input buffer. New measurements enter the queue; processed measurements are removed. When the queue is full, acquisition pauses until capacity becomes available. This is not the fixed research dataset in A. No prediction or experience replay is involved.

Draft body

The input buffer holds up to 32 incoming measurements until processing. Processed measurements are removed. Acquisition pauses when the buffer is full and resumes when capacity becomes available.
