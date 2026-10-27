# Introduction drafting requests

Use only this fictional packet. No external literature lookup or document rendering is needed. Produce paste-ready prose and a brief separate note about any material missing information. Do not edit any manuscript files.

## Request 1

Draft an introduction for a conference submission and a second introduction for a journal submission from the same study facts below. The two destination briefs are author-supplied requirements for this fictional test, not descriptions of real venues. Keep both concise; no fixed paragraph or sentence count is required.

The conference track addresses measurement algorithms for environmental sensing. Readers know routine sensors. Its brief asks authors to make the central computational contribution and the tested setting clear. It does not require labeled gap, motivation, or contribution subsections.

The journal article addresses interpretation of intermittent irrigation observations. Readers include field monitoring researchers. Its brief asks authors to explain the unresolved observation problem, why it matters for identifying interruptions, and why the proposed measurement integration is appropriate. It does not require a mechanism claim or more background for its own sake.

Study facts and supplied source cards

- The study concerns the timing of short irrigation interruptions, not crop stress, crop yield, or autonomous irrigation control.
- Routine readings track gradual changes but leave widely spaced observations around short interruptions. The supplied study routine2024 reports this under its sampling schedule. Use citation key routine2024 when needed.
- Event-triggered readings are concentrated around rapid changes. The supplied study event2025 reports those readings at irregular times. Use citation key event2025 when needed.
- Combining those records without preserving their observation times can conceal which readings precede or follow an interruption. This is the specific integration problem addressed here. No claim that all prior work ignores time is supported.
- The proposed estimator aligns routine and event-triggered records by their recorded observation times before estimating interruption onset. Routine readings retain background context; event readings provide denser transition observations. No quality filtering, causal plant model, extra sensing hardware, or online control was implemented.
- Across 32 held-out interruption events under the supplied protocol, median onset-time error was 12% lower than the routine-only estimator. No component ablation or cross-site validation was performed.

## Request 2

A separate author asks, “Write an introduction tailored to my next submission from the same study packet.” They supply no target venue, track, article type, or audience. Respond appropriately to that request using the available information. Do not invent the author's destination.
