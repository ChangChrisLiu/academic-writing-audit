## A

We assemble a fixed post-training dataset D from compiled environmental observations. Before fitting, we partition its eligible records into training and validation subsets. The dataset also retains rejected records for audit; these records are used for neither fitting nor validation. Appendix C reports the composition of the full post-training dataset D. The implementation reads `buffer_path`.

**Caption**

Composition of the post-training dataset D, including the training and validation subsets and rejected records retained for audit.

The term post-training dataset identifies the fixed collection without implying queueing, eviction, or experience replay. Using this term throughout also preserves the scope of Appendix C, which covers all of D, including validation records and records retained only for audit. The legacy code identifier `buffer_path` remains unchanged.

## B

The input buffer holds up to 32 incoming measurements until processing. Processed measurements are removed. Acquisition pauses when the buffer is full and resumes when capacity becomes available.

Input buffer is the appropriate term for this bounded memory queue, so the passage is retained unchanged. It describes temporary storage while measurements await processing and is distinct from the fixed research dataset in A. The term does not imply prediction or experience replay.
