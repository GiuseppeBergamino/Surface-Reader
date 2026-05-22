Prompt: Which port should I use to synchronize the instrument from an external device? Describe where it is and what it does.

Response: 

Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the connector side/rear edge of the instrument, in the row of ports. In the manual’s connection diagram it is port 7, immediately to the right of SYNC OUT, which is port 6.

What it does: when SYNC IN is connected, the monotribe ignores its internal step clock. The sequencer advances through its steps according to pulses received at this jack. The manual says it can sync to pulses from another monotribe, an analog sequencer, or the audio output of a DAW. The detected pulse polarity can be set in the Global menu.

[Trace]
Sources used: monotribe Owner’s Manual, Connections p.8; Global menu p.16.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies SYNC IN and describes its synchronization function.
Unsupported-current-state risk: None.
[/Trace]