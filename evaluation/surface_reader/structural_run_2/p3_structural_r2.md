Prompt: Create a structured description of the sync in.

Response: 

Structured description: SYNC IN

Official name: SYNC IN jack

Surface role: port

Physical type: 3.5 mm monaural mini-phone input jack

Region: connection area / rear-panel connection group

Function: When something is connected to the SYNC IN jack, the monotribe ignores its internal step clock. The sequencer advances through its steps according to incoming pulse signals. This lets another monotribe, an analog sequencer, or the audio output of a DAW control the monotribe’s step timing.

Signal behavior:
The manual describes SYNC IN as pulse-driven step advance. The detected pulse polarity is configurable in the Global menu:

Step button 4: SYNC IN polarity
LED unlit: the step advances when the input signal rises
LED lit: the step advances when the input signal falls
Factory default is LED unlit.

Current-state limitation:
Static sources can describe what SYNC IN does, but they cannot tell whether a cable is currently connected, whether pulses are arriving, what polarity is currently selected, or whether the sequencer is advancing correctly.

Non-visual/tactile map entry

From the performer’s perspective, treat SYNC IN as part of the rear connection row, not the top control surface. In the manual’s connection diagram, it is item 7, near SYNC OUT. Use the two sync jacks as a pair: SYNC OUT sends timing pulses; SYNC IN receives timing pulses.

Surface model node
node_id: port.sync_in
name: SYNC IN jack
role: port
physical_type: 3.5 mm monaural mini-phone jack
region: connection area
group: sync I/O
direction: input
documented_function: >
  Receives pulse signals that advance the sequencer steps.
  When connected, the internal step clock is ignored.
possible_sources:
  - another monotribe
  - analog sequencer
  - DAW audio output
related_controls:
  - Global menu step button 4: SYNC IN polarity
related_ports:
  - SYNC OUT jack
current_state: unknown from static sources

[Trace]
Sources used: monotribe_manual.pdf p.8 connections, p.16 Global menu; monotribe_manual_visual_index.json entry for p.8 connections; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines SYNC IN behavior, connector type, and polarity setting; layout is supported by the connection diagram index.
Unsupported-current-state risk: Medium.
[/Trace]
