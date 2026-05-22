Prompt: Create a structured description of the cutoff.

Response: 
Cutoff — structured description

Official name: CUTOFF knob
Section: Synthesizer section
Group: VCF, or Voltage Controlled Filter
Semantic role: slider
Physical type: rotary knob
Current value: Not knowable from the manual or static panel references alone.

Function: The CUTOFF knob adjusts the cutoff frequency of the VCF. This changes the brightness of the synth sound: turning it left darkens the sound, and turning it right brightens the sound.

Related control: PEAK knob. Cutoff sets the filter frequency; Peak adds resonance or emphasis around that cutoff frequency.

Non-visual location: From the performer’s perspective, Cutoff is in the synthesizer section, in the filter area. It is the upper knob in the VCF pair, with PEAK directly below it. Think of the pair as: Cutoff above, Peak below.

Surface model entry:

node_id: vcf_cutoff
name: CUTOFF knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCF
description: Adjusts the VCF cutoff frequency, affecting sound brightness.
actions:
  - turn counterclockwise to darken the sound
  - turn clockwise to brighten the sound
related_controls:
  - PEAK knob
current_state: unavailable from static sources

[Trace]
Sources used: monotribe_manual.pdf, manual page 10/11 content; monotribe_manual_visual_index.json entry for panel overview; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%, Visual/static layout 20%, Surface ARIA Store 15%, Surface Model/Map Schema 10%, Interaction Guidance Store 5%, Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual directly documents the CUTOFF function and the panel diagram supports its placement in the VCF group.
Unsupported-current-state risk: Low.
[/Trace]