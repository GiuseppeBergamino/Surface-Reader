Prompt: Create a structured description of the VCO wave selector.

Respose: 

Structured description: VCO WAVE select switch

Official name: WAVE select switch
Surface node ID: monotribe.vco.wave_select
Parent region: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: Three-position slide switch
Control purpose: Selects the VCO waveform. The manual says the VCO waveform can be sawtooth, triangle, or square.

Possible settings
Position / value	Meaning
Sawtooth wave	Selects sawtooth as the oscillator waveform
Triangle wave	Selects triangle as the oscillator waveform
Square wave	Selects square as the oscillator waveform

Current state: Unknown. A manual, diagram, or static panel photo can identify the switch and its possible positions, but cannot confirm which waveform is selected on your physical unit right now.

Non-visual location and tactile map

From the performer’s perspective, the WAVE select switch is in the upper-left synthesizer area, inside the VCO group.

Use this mental anchor:

VCO group = octave selector, waveform switch, noise knob, range switch.

A tactile route:

Start in the upper-left control area of the panel.
Find the VCO controls.
The WAVE select switch is a small three-position switch near the OCTAVE selector and above/near the NOISE knob area.
It is not a continuous knob; it has three discrete stops.
Surface model entry
node_id: monotribe.vco.wave_select
name: WAVE select switch
role: switch
physical_type: three-position slide switch
region: Synthesizer section
group: VCO
parent: monotribe.vco
description: Selects the VCO waveform used as the basis of the synth sound.
possible_states:
  - sawtooth wave
  - triangle wave
  - square wave
current_state: unknown
actions:
  - move switch to one of three waveform positions
state_rule: current selected waveform requires situated evidence
sources:
  - monotribe_manual.pdf, panel description and VCO section
  - monotribe_manual_visual_index.json, page 10 panel overview
  - foto_pannello static panel reference

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for p.10; foto_pannello static panel reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three waveform settings, while the panel diagram/photo support static location and physical grouping.
Unsupported-current-state risk: Medium.
[/Trace]
