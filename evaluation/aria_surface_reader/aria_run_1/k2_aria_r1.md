Prompt: Represent the noise level as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.synth.vco.noise_level",
  "role": "slider",
  "name": "NOISE knob",
  "description": "Adjusts the level of white noise mixed with the VCO output.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synth.vco",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase white noise level",
    "turn counterclockwise to decrease white noise level"
  ],
  "properties": {
    "valuemin": "minimum noise level, not numerically documented",
    "valuemax": "maximum noise level, not numerically documented"
  },
  "possible_states": [
    "white noise level can be adjusted continuously by the knob"
  ],
  "current_state": null,
  "spatial_properties": {
    "approximate_position": "upper-left area of the synthesizer section",
    "group_context": "inside the VCO group",
    "neighbours": [
      "OCTAVE selector",
      "WAVE select switch",
      "RANGE select switch"
    ]
  },
  "source": [
    "monotribe_manual.pdf, Synthesizer section / VCO: NOISE knob",
    "Surface ARIA Store: rotary knob controlling a continuous value maps to role slider"
  ]
}

The important point is that noise level is not represented as a switch or button. It is a continuous parameter controlled by the NOISE knob, so the Surface ARIA role should be slider. The manual says the NOISE knob adjusts the level of white noise mixed with the VCO output , and the Surface ARIA Store defines a rotary knob controlling a continuous value as a slider role .

Do not include valuenow unless there is situated evidence of the knob’s current physical position.

[Trace]
Sources used: monotribe_manual.pdf; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Surface ARIA Store 35%; Surface Model/Map Schema 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the NOISE knob and its function, and the ARIA store directly maps continuous rotary controls to slider.
Unsupported-current-state risk: Low.
[/Trace]