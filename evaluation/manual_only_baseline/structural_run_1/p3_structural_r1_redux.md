Prompt: Create a structured description of the sync in.

Response: 

SYNC IN — structured description

Direct answer.
SYNC IN is the monotribe’s external step-clock input. When something is connected to this jack, the monotribe ignores its internal step clock and advances the sequencer according to incoming pulses.

Where it is.
It is connection 7 in the rear-panel connection group, near SYNC OUT. In the manual’s connection diagram, SYNC OUT is immediately before it, and SYNC IN is the rightmost numbered jack in that row.

What it does.
Use SYNC IN to synchronize the monotribe’s sequencer steps to pulses from another monotribe, an analog sequencer, or the audio output of a DAW.

Effect on tempo control.
When SYNC IN is connected, the TEMPO knob is disabled, because the sequencer timing is being driven by the incoming sync pulses instead of the internal clock.

Polarity setting.
The detected pulse polarity is set in the Global menu:

Step button 4: SYNC IN polarity
LED unlit: the step advances when the input signal rises.
LED lit: the step advances when the input signal falls.

Connector specification.
The SYNC IN jack is a 3.5 mm monaural mini-phone jack. The manual lists its maximum input level as 20V.

Limitation.
The manual describes how SYNC IN responds to pulses, but it does not document detailed DAW setup steps or exact audio pulse creation settings.

[Trace]
Sources used: monotribe_manual.pdf, connections section p.8; sequencer TEMPO description p.14; Global menu p.16; specifications p.17.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual directly documents SYNC IN behavior, polarity, tempo interaction, and connector specification.
Unsupported-current-state risk: None.
[/Trace]