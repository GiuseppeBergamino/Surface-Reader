Prompt: Create a structured description of the audio in.

Respose: 

AUDIO IN — structured description

Official name: AUDIO IN jack
Surface role: port
Physical type: 3.5 mm stereo mini-phone jack
Region: rear connection area
Function: accepts an external audio source and routes it into the monotribe’s synth signal path. The manual says the external source is mixed with the VCO, then sent through the VCF and VCA. This means the external sound can be filtered and shaped by the monotribe, or the monotribe can be used like an effect processor for another sound source.

Signal behavior:

Stereo input is accepted, but the signal is mixed down to mono.
The input joins the synth voice before the filter and amplifier.
In the block diagram, AUDIO IN feeds into the VCO/noise/synth path before VCF → VCA → AUDIO OUT.

Non-visual location:
From the performer’s perspective, the AUDIO IN jack is on the rear connection strip, along the top edge/far side of the unit. In the manual’s connection diagram it is the third numbered rear-panel item, after the power switch and DC 9V jack, and before OUTPUT, HEADPHONES, SYNC OUT, and SYNC IN.

Structured surface node:

node_id: port_audio_in
name: AUDIO IN jack
role: port
physical_type: 3.5 mm stereo mini-phone jack
region: rear connection area
group: audio connections
actions:
  - insert external audio cable
  - remove external audio cable
input_type: external audio source
signal_path:
  - mixed with VCO output
  - routed through VCF
  - routed through VCA
  - sent toward audio output
possible_values:
  connector: 3.5 mm stereo mini-phone
  stereo_handling: stereo input mixed to mono
current_state: unknown
current_state_note: cable connection and incoming audio cannot be inferred from static sources alone
musical_use:
  - expand monotribe sound sources
  - process an external audio source through the monotribe filter/amplifier path

[Trace]
Sources used: monotribe_manual.pdf: Main features, Block diagram, Connections; monotribe_manual_visual_index.json: page 6 block diagram and page 8 rear-panel connections entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual directly documents the AUDIO IN jack function, connector type, mono mix behavior, and routing.
Unsupported-current-state risk: Low.
[/Trace]
