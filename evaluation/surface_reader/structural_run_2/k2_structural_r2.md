Prompt: Create a structured description of the noise level.

Response:

Noise level — structured description

Official control name: NOISE knob
Surface role: slider
Physical type: rotary knob
Region: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator group
Parameter controlled: level of white noise mixed with the VCO output
Manual function: The NOISE knob “adjusts the level of white noise that’s mixed with the VCO output.”
Signal-flow context: The manual’s block diagram shows the noise generator feeding the synthesizer signal path before the VCF and VCA, alongside the VCO and external audio input.
Musical meaning: Increasing the noise level adds more white noise to the oscillator sound. This can make the sound rougher, breathier, noisier, or more percussive before it is shaped by the filter and amplifier.
Current state: I cannot determine the current NOISE knob value from the manual, diagram, or static panel photo alone.

Non-visual surface-map entry
node_id: synth_vco_noise
name: NOISE knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCO
action: turn counterclockwise to reduce noise level; turn clockwise to increase noise level
possible_value_type: continuous level
current_state: unknown from static sources
function: adjusts the level of white noise mixed with the VCO output

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 01_surface_aria_store.md, 05_surface_model_map_schema.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The NOISE knob function is explicitly documented, and current-state limits are defined by the routing policy.
Unsupported-current-state risk: Low.
[/Trace]