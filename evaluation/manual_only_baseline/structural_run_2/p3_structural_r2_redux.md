Prompt: Create a structured description of the sync in.

Response: 

The SYNC IN jack is the monotribe’s input for external step-clock pulses. When something is connected to SYNC IN, the monotribe ignores its internal step clock, and the sequencer advances according to incoming pulses.

Where it is
It is on the connection side with the other jacks. In the manual’s connection diagram, SYNC IN is connector 7, immediately after SYNC OUT connector 6.

What it does
Use SYNC IN to synchronize the monotribe’s sequencer steps to pulses from another monotribe, an analog sequencer, or the audio output of a DAW.

Important behavior
When SYNC IN is connected, the TEMPO knob is disabled because the step timing is now controlled by the incoming pulses.

Related Global menu setting
The SYNC IN polarity is set in the Global menu on step button 4:

LED unlit: the step advances when the input signal rises.
LED lit: the step advances when the input signal falls.

Connector specification
The manual specifies SYNC IN as a 3.5 mm monaural mini-phone jack, with a maximum input level of 20V.

[Trace]
Sources used: monotribe_manual.pdf, pages 8, 14, 16, 17; connection diagram and Global menu entries.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual directly documents the jack, behavior, polarity setting, and connector specification.
Unsupported-current-state risk: None.
[/Trace]
