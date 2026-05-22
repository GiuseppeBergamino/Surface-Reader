Prompt: Represent the oscillator waveform control as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vco.wave_select",
  "role": "switch",
  "name": "WAVE select switch",
  "description": "Selects the VCO waveform used as the basis of the synthesizer sound.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synthesizer.vco",
  "physical_type": "three-position switch",
  "actions": [
    "select sawtooth wave",
    "select triangle wave",
    "select square wave"
  ],
  "possible_states": [
    {
      "name": "sawtooth",
      "label": "Sawtooth wave"
    },
    {
      "name": "triangle",
      "label": "Triangle wave"
    },
    {
      "name": "square",
      "label": "Square wave"
    }
  ],
  "current_state": null,
  "properties": {
    "orientation": "discrete multi-position selector",
    "valuetext": null
  },
  "spatial_properties": {
    "surface_region": "upper-left synthesizer area",
    "local_group": "VCO controls",
    "nearby_controls": [
      "OCTAVE selector",
      "NOISE knob",
      "RANGE select switch"
    ],
    "layout_source": "manual synthesizer panel overview, page 10"
  },
  "source": [
    "monotribe_manual.pdf, pages 10-11",
    "monotribe_manual_visual_index.json, page 10 entry",
    "01_surface_aria_store.md"
  ],
  "notes": "Do not expose `current_state`, `valuenow`, or active waveform from static sources alone. The manual documents the possible waveform choices, but the present switch position requires situated evidence."
}

Semantically, this should be a switch, not a slider, because it selects one of three discrete waveform states. The manual names it “WAVE select switch” and defines the choices as sawtooth, triangle, and square wave. The Surface ARIA Store maps discrete-position waveform selectors to the switch role.

[Trace]
Sources used: monotribe_manual.pdf pages 10–11; monotribe_manual_visual_index.json page 10 entry; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 20%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the control and its three waveform choices, and the semantic role follows the store’s switch mapping.
Unsupported-current-state risk: Low.
[/Trace]