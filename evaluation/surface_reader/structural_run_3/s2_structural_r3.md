Prompt: Create a structured description of the VCO wave selector.

Respose: 

Structured description: VCO WAVE select switch

Official name: WAVE select switch
Section: Synthesizer section
Group: VCO, or Voltage Controlled Oscillator
Semantic role: switch
Physical type: multi-position slide switch, based on the panel diagram/static layout
Purpose: Selects the VCO waveform. The manual states that the oscillator generates the waveform that forms the basis of the sound, and the WAVE select switch chooses between sawtooth, triangle, and square waves.

Possible settings
Sawtooth wave
A selectable VCO waveform.
Triangle wave
A selectable VCO waveform.
Square wave
A selectable VCO waveform.
Surface model node
{
  "node_id": "synth.vco.wave_select",
  "role": "switch",
  "name": "WAVE select switch",
  "region": "Synthesizer section",
  "group": "VCO",
  "physical_type": "slide switch",
  "description": "Selects the VCO waveform used as the basis of the synth sound.",
  "possible_states": [
    "sawtooth wave",
    "triangle wave",
    "square wave"
  ],
  "current_state": null,
  "actions": [
    "move switch to sawtooth",
    "move switch to triangle",
    "move switch to square"
  ]
}
Non-visual/tactile guidance

From the performer’s perspective, the WAVE select switch is in the upper-left synthesizer area, inside the VCO group. It is near the OCTAVE selector, the NOISE knob, and the RANGE select switch. Use this as a memory anchor: VCO starts the sound; WAVE chooses the raw shape before filtering and amplification.

I cannot determine the switch’s current position from the manual, screenshots, or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel overview, manual page 11 VCO description, monotribe_manual_visual_index.json, foto_pannello, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual gives the official name, function, and possible settings; static layout sources support placement and physical type.
Unsupported-current-state risk: Low.
[/Trace]