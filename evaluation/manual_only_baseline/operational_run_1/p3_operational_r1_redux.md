Prompt: Which port should I use to synchronize the instrument from an external device? Describe where it is and what it does.

Response: 

Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the connector side of the instrument in the row of rear-panel jacks. In the manual’s connection diagram, it is jack 7, at the right end of the numbered connection row, immediately to the right of SYNC OUT.

What it does: when something is plugged into SYNC IN, the monotribe ignores its internal step clock, and the sequencer advances through its steps according to the pulses arriving at that jack. The manual says it can sync the monotribe’s steps from another monotribe, an analog sequencer, or the audio output of a DAW. The input polarity can be set in the Global menu.

[Trace]
Sources used: monotribe_manual.pdf, Connections section p.8; Global menu p.16.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies SYNC IN and describes its synchronization behavior.
Unsupported-current-state risk: None.
[/Trace]