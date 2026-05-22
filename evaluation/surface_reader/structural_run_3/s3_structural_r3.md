Prompt: Create a structured description of the octave selector.

Response:

Structured description: OCTAVE selector

Official name: OCTAVE selector
Device: Korg monotribe
Region: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: rotary selector, based on the panel layout/static panel references
Interaction: turn/select one of the octave positions
Current state: unknown from static sources alone

Function

The OCTAVE selector specifies the VCO pitch in octave steps. The manual states that with the 64' setting, the ribbon keyboard pitch range is A0–D2.

Possible values

The manual identifies it as an octave selector for the VCO. The visible panel layout shows multiple discrete octave positions around the selector; these are possible positions, not current state. Static sources cannot tell which octave is selected now.

Non-visual location

From the performer’s perspective, the OCTAVE selector is in the upper-left area of the synthesizer section, at the start of the VCO controls. Use it as an early landmark for the synth controls: it sits before the waveform and range-related controls, and belongs to the pitch/source area rather than the filter or sequencer area.

Surface model node
node_id: monotribe.vco.octave_selector
name: OCTAVE selector
role: switch
physical_type: rotary selector
region: Synthesizer section
group: VCO
description: Specifies the VCO pitch in octave steps.
actions:
  - turn/select octave position
possible_states:
  - documented octave selector positions; current selected position requires situated evidence
current_state: unknown
Surface map entry
node_id: monotribe.vco.octave_selector
approximate_position: upper-left synthesizer area
landmarks:
  - upper-left VCO control group
  - nearby waveform/range controls
tactile_description: discrete rotary selector used for octave selection
navigation_hint: start at the upper-left control area of the synth section; the octave selector is the VCO pitch-range selector there.

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for panel overview p.10; static panel photo foto_pannello; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The function and section are manual-grounded; physical type and location are based on static layout references, not live observation.
Unsupported-current-state risk: Low.
[/Trace]
