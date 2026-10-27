Request 1

Conference introduction

Estimating the onset of short irrigation interruptions brings together observations with different temporal coverage. Routine readings track gradual changes but leave widely spaced observations around short interruptions under the sampling schedule studied in [routine2024]. Event-triggered readings concentrate around rapid changes and occur at irregular times [event2025]. Combining these records without preserving their observation times can conceal which readings precede or follow an interruption, obscuring the temporal information needed to estimate its onset.

We present an estimator that aligns routine and event-triggered records by their recorded observation times before estimating interruption onset. This integration retains the background context of routine readings while incorporating the denser transition observations provided by event readings. Across 32 held-out interruption events under the study protocol, the estimator achieved a median onset-time error 12% lower than that of the routine-only estimator. The study evaluates this combined estimation procedure for short irrigation interruptions within the tested protocol.

Journal introduction

Intermittent irrigation observations describe changes over time, but identifying when a short interruption begins depends on the observations available around that change. Routine readings track gradual changes, yet the sampling schedule examined in [routine2024] leaves widely spaced observations around short interruptions. Event-triggered readings provide observations concentrated around rapid changes, although their observation times are irregular [event2025]. Together, these records offer background context and denser observations of transitions.

Using both records leaves a specific observation problem to resolve. Combining readings without preserving their observation times can conceal which were collected before an interruption and which were collected after it. That ambiguity matters directly for estimating onset because the estimate depends on the temporal relationship between the observations and the interruption. Aligning the records by their recorded observation times addresses this integration problem while retaining the different information each record supplies.

We implement this alignment in an estimator of interruption onset. Routine readings retain background context, and event-triggered readings provide denser transition observations for the aligned record. Across 32 held-out interruption events under the study protocol, median onset-time error was 12% lower than for the routine-only estimator. This result supports the combined procedure in the tested setting; its performance across sites and the separate contribution of each component remain untested.

Separate note

Bracketed identifiers are provisional citations using the supplied keys. No further information is needed for these brief-based drafts. The supplied protocol is not described in detail, so neither introduction specifies sampling intervals, site conditions, or interruption durations. The evidence concerns onset timing and does not establish crop outcomes or control performance. Without a component ablation, the 12% reduction cannot be attributed separately to alignment or to the addition of event-triggered readings.

Request 2

Which venue and track or article type are you targeting, and who are its intended readers? Please include any introduction requirements supplied by that destination so I can tailor the emphasis.

The supported argument is already clear. Routine readings provide background context but are widely spaced around short interruptions under the studied schedule. Event-triggered readings add denser transition observations at irregular times. Integrating the two requires preserving when each observation occurred so that its relation to the interruption remains interpretable. The estimator aligns those recorded times before estimating onset, with a 12% lower median onset-time error than the routine-only estimator across 32 held-out events under the study protocol. The destination is the missing information needed to turn this argument into a tailored introduction.
