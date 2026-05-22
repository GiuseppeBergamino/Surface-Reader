Prompt ID: p1

Prompt: Create a structured description of the audio in.

# Surface Reader:
## R1:
AUDIO IN — structured description

Official name: AUDIO IN jack
Surface role: port
Physical type: 3.5 mm stereo mini-phone input jack
Region: connection area / rear-panel jack row
Function: accepts an external audio source. The incoming audio is mixed with the VCO output, then routed through the VCF and VCA. This means the monotribe can process an external sound source through its filter and amplifier path.

Signal path

External source → AUDIO IN → mixed with VCO → VCF filter → VCA amp → audio output path.

The manual also states that a stereo signal connected to AUDIO IN is mixed down to mono.

Non-visual location

From the performer’s perspective, AUDIO IN is on the rear connection row, among the small jacks and power connections. In the manual’s connection diagram, it is listed as item 3, between the DC 9V jack and the OUTPUT jack. Use the rear edge as the landmark and move along the jack row from left to right: power switch, DC 9V, then AUDIO IN.

Practical use

Plug an audio player, synth, drum machine, or other line-level source into AUDIO IN. The monotribe will treat that sound as part of the synth signal path, so the filter controls can shape the external audio.

Limitations

I can describe the jack’s documented purpose and static location, but I cannot determine whether anything is currently plugged into AUDIO IN or what signal is being received from static sources alone.

[Trace]
Sources used: monotribe_manual.pdf p.5, p.6, p.8; monotribe_manual_visual_index.json entry for p.8 Connections; static panel photo reference for rear/top orientation; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents the AUDIO IN function, connector type, signal routing, and mono mixing behavior.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
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

## R3:
AUDIO IN — structured surface description

Official name: AUDIO IN jack
Device area: connection area / rear-panel jack group
Semantic role: port
Physical type: 3.5 mm stereo mini-phone input jack
Function: accepts an external audio source. The incoming audio is mixed with the VCO output, then routed through the VCF and VCA. This means the monotribe can process an outside sound source through its filter and amplifier path.

Signal behavior:
A stereo input signal is mixed down to mono before processing.

Musical use:
Use AUDIO IN to expand the monotribe’s sound by blending an external source with the synth oscillator, or to use the monotribe as an effect processor for another sound source.

Surface-map placement:
From the performer’s perspective, AUDIO IN is on the rear connection row. In the manual’s connection diagram, it is item 3, positioned between the DC 9V jack and the OUTPUT jack in the rear-panel jack sequence.

Non-visual navigation hint:
Start at the rear edge where the cable jacks are grouped. Find the power switch area at one side, then move along the jack row: after the DC 9V power jack, the next audio mini-jack is AUDIO IN. The larger OUTPUT jack is nearby after it, which can help confirm the area.

Important limitation:
Static sources can identify the jack and its function, but they cannot tell whether a cable is currently plugged in or whether audio is currently arriving.

[Trace]
Sources used: monotribe_manual.pdf p.8 and p.17; monotribe_manual_visual_index.json entry for p.8; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents AUDIO IN function, connector type, and signal behavior, and the visual index identifies the rear-panel connection diagram.
Unsupported-current-state risk: Low.
[/Trace]


# Baseline:
## R1:
The AUDIO IN jack is the monotribe’s external audio input. It lets you feed an outside audio source into the monotribe so that the incoming sound is mixed with the VCO signal, then processed through the VCF and VCA. This means the monotribe can expand its own synth sound, or act as an effect processor for another audio source.

Where it is:
On the rear connection panel, the AUDIO IN jack is the third connector/control from the left in the manual’s connection diagram: after the Power switch and DC 9V jack, and before the OUTPUT jack.

Signal path and behavior:
External audio connected to AUDIO IN is mixed with the VCO output. After that, the combined signal goes through the VCF filter and VCA amplifier. A stereo input signal is mixed down to mono.

Connector type:
The specifications list the AUDIO IN jack as a 3.5 mm stereo mini-phone jack.

Practical use:
Connect an audio player or other external audio source to AUDIO IN. Then use the monotribe’s filter and amplifier-related controls, such as CUTOFF, PEAK, and LEVEL, to shape what comes through.

[Trace]
Sources used: monotribe_manual.pdf, pages 5, 6, 8, 11, 17; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents AUDIO IN function, signal path, connector type, and rear-panel position.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The AUDIO IN jack is the monotribe’s external audio input. It lets you feed another audio source into the monotribe so that the external sound is mixed with the VCO signal, then processed through the VCF and VCA. The manual says this can expand the monotribe’s sonic possibilities, or let you use the monotribe as an effect processor for a separate audio source. A stereo input signal is mixed down to mono.

Where it is

On the connection side, the AUDIO IN jack is connector number 3 in the manual’s connection diagram. It sits between the DC 9V jack and the OUTPUT jack. In left-to-right order across the connector row: power switch, DC 9V, AUDIO IN, OUTPUT, HEADPHONES, SYNC OUT, SYNC IN.

Signal path

External audio enters through AUDIO IN.
It is mixed with the VCO output.
The mixed signal goes through the VCF filter.
It then goes through the VCA amplifier.
The result is sent toward the audio output path.

Technical detail

The specifications list the AUDIO IN jack as a 3.5 mm stereo mini-phone jack.

Limitations

The manual does not document a separate input level knob for AUDIO IN. It also does not state that the monotribe can detect whether a cable is currently connected, so the current connection state cannot be inferred from the manual or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf: Main features “External input jack”; Block diagram; Connections p.8; Specifications p.17; static panel photo for connector-row orientation.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly describes AUDIO IN function, signal routing, jack type, and connector position.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
The AUDIO IN jack is the monotribe’s external audio input. It lets you feed another audio source into the monotribe so that the incoming sound is mixed with the VCO signal, then sent through the VCF and VCA. This can expand the synth sound or let the monotribe act as an effect processor for an external audio source. A stereo input signal is mixed down to mono.

Where it is: On the rear connection row, the AUDIO IN jack is connector 3. In that row, it is to the right of the DC 9V jack and to the left of the OUTPUT jack.

Signal path:
External audio source → AUDIO IN → mixed with VCO → VCF filter → VCA amp → audio output.

Connector specification: The manual lists the AUDIO IN jack as a 3.5 mm stereo mini-phone jack.

Limitation: The manual documents how AUDIO IN is routed and what connector it uses, but it does not specify an input gain control or a dedicated AUDIO IN level knob.

[Trace]
Sources used: monotribe Owner’s manual pages 5, 6, 8, 11, 17; static panel photo for rear-panel position.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly describes the AUDIO IN jack, routing, stereo-to-mono behavior, and connector type.
Unsupported-current-state risk: None.
[/Trace]


