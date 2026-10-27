Conference introduction

Estimating the onset of short irrigation interruptions requires observations that resolve the transition within the surrounding monitoring record. Under the sampling schedule reported in \cite{routine2024}, routine readings track gradual changes but leave widely spaced observations around short interruptions. Event-triggered sampling concentrates readings around rapid changes, although these observations occur at irregular times \cite{event2025}. Combining these records offers background context and denser transition observations, but discarding observation times can obscure which readings precede or follow an interruption.

We introduce an estimator that aligns routine and event-triggered records by their recorded observation times before estimating interruption onset. This alignment preserves the temporal relationship needed to interpret the two records together. Across 32 held-out interruption events under the study protocol, median onset-time error was 12% lower than for the routine-only estimator.

Journal introduction

Identifying short irrigation interruptions from monitoring records requires locating their onset among observations collected at different times. Routine monitoring describes gradual changes, but the sampling schedule examined in \cite{routine2024} leaves widely spaced observations around short interruptions. Event-triggered readings provide denser observations around rapid changes and are collected at irregular times \cite{event2025}.

Combining these observations creates a timing problem when their recorded observation times are not preserved. A reading can then lose its position before or after an interruption, obscuring the transition whose timing is to be estimated. Using the additional event readings to identify onset therefore calls for an integration procedure that retains this temporal relationship. Alignment by recorded observation time provides that connection, retaining the routine readings as background context and the event readings as denser observations of the transition.

We evaluate an estimator that performs this alignment before estimating interruption onset. Across 32 held-out interruption events under the study protocol, median onset-time error was 12% lower than for the routine-only estimator.

Separate evidence note

The packet does not report uncertainty for the 12% difference. The comparison evaluates the combined estimator; without a component ablation, it does not isolate the contribution of alignment. Cross-site performance remains untested.

Response to Request 2

Which venue and track or article type are you targeting, and who are the intended readers? That information will determine the emphasis of the tailored introduction.

The supported argument can already be organized. Routine readings leave widely spaced observations around short interruptions, while irregular event-triggered readings provide denser transition observations. Integrating them without preserving their recorded times can obscure which readings precede or follow an interruption. The proposed estimator addresses this problem by aligning the records before estimating onset. Its reported evidence is a 12% lower median onset-time error than the routine-only estimator across 32 held-out events under the study protocol. The destination brief is the remaining dependency for deciding how to frame this argument for the next submission.
