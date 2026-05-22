Prompt ID: p3

Prompt: Create a structured description of the sync in.

# Surface Reader:
## R1:
Sync In — structured description

Official name: SYNC IN jack.

Surface role: port

Physical type: 3.5 mm monaural mini-phone input jack.

Region: Connection area / rear-panel jack row.

Purpose: Receives external sync pulses so the monotribe sequencer can advance step-by-step from another device.

Documented behavior: When the SYNC IN jack is connected, the monotribe ignores its internal step clock. The sequencer advances through its steps according to pulses received at SYNC IN. This can synchronize the monotribe’s steps with another monotribe, an analog sequencer, or the audio output of a DAW.

Related setting: SYNC IN polarity is set in the Global menu using step button 4.
Possible settings:

LED unlit: the step advances when the input signal rises.
LED lit: the step advances when the input signal falls.
Factory default: rise.

Tactile location: From the performer’s perspective, use the rear connection row as the landmark. SYNC IN is one of the small 3.5 mm sync jacks near SYNC OUT. It is part of the connection group with power, audio, headphones, SYNC OUT, and SYNC IN, shown in the manual’s rear-panel connection diagram.

Important limitation: Static sources can describe what SYNC IN does and where it is located, but they cannot tell whether a cable is currently plugged in, whether pulses are arriving, or what the current polarity setting is.

[Trace]
Sources used: monotribe_manual.pdf, page 8 connections; monotribe_manual.pdf, page 16 Global menu; monotribe_manual_visual_index.json, page 8 Connections entry; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: Function, connector type, and polarity behavior are directly documented in the manual, with layout supported by the visual index.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
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


## R3:
Structured description: SYNC IN jack
Identity
Official name: SYNC IN jack
Surface role: port
Physical type: 3.5 mm monaural mini-phone jack
Region: connection area / rear-panel jack row
Purpose: accepts external sync pulses to drive the monotribe sequencer.
Function

When something is connected to SYNC IN, the monotribe ignores its internal step clock. The sequencer advances through its steps according to incoming pulses at this jack. The manual says this can synchronize the monotribe’s steps with pulses from another monotribe, an analog sequencer, or the audio output of a DAW.

Timing behavior
Incoming pulse = step advance trigger.
The TEMPO knob is disabled while SYNC IN is connected, because the external pulse source becomes the timing reference.
This affects the sequencer step clock, not the audio signal path.
Polarity setting

SYNC IN polarity is set in the Global menu, using step button 4:

LED unlit: the step advances when the input signal rises. This is the factory default.
LED lit: the step advances when the input signal falls.
Electrical / connector specification
Connector: 3.5 mm monaural mini-phone jack
Maximum input level: 20 V
Non-visual location guidance

From the performer’s perspective, treat SYNC IN as part of the rear connection row. The manual’s connection diagram places the rear-panel connectors in a left-to-right row and identifies SYNC IN as item 7, at the right end of that row, immediately after SYNC OUT. The visual index confirms page 8 as the rear-panel jack diagram for audio, headphones, and sync connections.

Tactile anchor: find the row of small rear-panel jacks; SYNC IN is the rightmost sync jack, next to SYNC OUT.

Current-state limitation

I cannot tell from the manual or static panel references whether a cable is currently plugged into SYNC IN, what pulse source is connected, or which polarity setting is currently active. Those require current physical or device-state evidence.

[Trace]
Sources used: monotribe_manual.pdf pages 8, 14/15, 16, 17; monotribe_manual_visual_index.json entry for page 8; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The function, connector type, polarity, and sync behavior are explicitly documented; layout is supported by the manual connection diagram/index.
Unsupported-current-state risk: Medium.
[/Trace]

# Baseline:
## R1:
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

## R2:
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

## R3:
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



