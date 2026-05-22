Prompt: Create a structured description of the sync in.

Response: 

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
