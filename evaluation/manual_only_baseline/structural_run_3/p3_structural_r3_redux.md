Prompt: Create a structured description of the sync in.

Response: 

SYNC IN — structured description

Direct answer:
SYNC IN is the monotribe’s external synchronization input. When something is connected to SYNC IN, the monotribe ignores its internal step clock, and the sequencer advances according to incoming pulses.

Where it is:
SYNC IN is on the connector side of the unit, in the row of rear/side connections. In the manual’s connection diagram it is numbered 7, immediately to the right of SYNC OUT.

Connector type:
The specification lists SYNC IN as a ø3.5 mm monaural mini-phone jack. Its maximum input level is 20 V.

What it does:
Use SYNC IN to synchronize the monotribe’s sequencer steps with pulses from another monotribe, an analog sequencer, or the audio output of a DAW. Once connected, the TEMPO knob no longer controls the sequencer speed, because the external pulses determine step timing.

Related setting:
The Global menu includes SYNC IN polarity on step button 4.
Factory default: the step advances when the input signal rises.
Alternative setting: the step advances when the input signal falls.

Important limitation:
The manual describes how SYNC IN works, but it cannot tell whether a cable is currently plugged in, what signal is currently arriving, or what the current polarity setting is.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 8, 14, 16, 17.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents SYNC IN location, function, polarity setting, and jack specification.
Unsupported-current-state risk: Low.
[/Trace]
