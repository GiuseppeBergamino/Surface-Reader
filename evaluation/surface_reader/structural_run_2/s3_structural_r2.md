Prompt: Create a structured description of the octave selector.

Response:

Octave selector — structured surface description

Official name: OCTAVE selector.
Region: Synthesizer section.
Group: VCO, or Voltage Controlled Oscillator.
Semantic role: switch.
Physical type: discrete selector control; the static panel sources support it as a multi-position selector, not a continuous knob.
Function: It specifies the VCO pitch in octave steps. The manual gives one documented example: at the 64' setting, the ribbon keyboard pitch range is A0–D2.
Important interaction note: The OCTAVE selector is ignored when the RANGE select switch is set to WIDE; in WIDE mode the ribbon keyboard uses an extended continuous pitch range instead.

Possible states

The manual identifies the OCTAVE selector as an octave-step control, but the available text here does not expose the full list of printed octave positions. Therefore:

node_id: monotribe.synth.vco.octave_selector
name: OCTAVE selector
role: switch
physical_type: multi-position selector
region: Synthesizer section
group: VCO
description: Specifies the VCO pitch in octave steps.
possible_states:
  - documented_example: "64'"
    effect: "Ribbon keyboard range is A0–D2"
current_state: unknown
state_limitation: Current selector position cannot be inferred from the manual, diagram, or static panel photo alone.
Non-visual location and orientation

From the performer’s perspective, place the monotribe with the ribbon keyboard closest to you. The OCTAVE selector belongs to the upper-left synthesizer area, inside the VCO group. Use the left side of the panel as the main landmark: the OCTAVE selector is near the top-left VCO controls, above the lower ribbon-keyboard area and before the filter and LFO controls farther to the right.

Do not rely on the printed octave marking to determine its current setting unless you have sighted assistance or a separate tactile marking. Static sources can identify the control and its function, but not where it is currently set.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel overview via visual index, monotribe_manual_visual_index.json, foto_pannello, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Function and region are manual-grounded; exact tactile form and printed positions are only partially supported by static layout evidence.
Unsupported-current-state risk: Medium.
[/Trace]