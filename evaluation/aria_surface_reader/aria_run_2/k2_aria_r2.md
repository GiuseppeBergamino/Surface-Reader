Prompt: Represent the noise level as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vco.noise",
  "role": "slider",
  "name": "NOISE knob",
  "description": "Adjusts the level of white noise that is mixed with the VCO output.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synthesizer.vco",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase noise level",
    "turn counterclockwise to decrease noise level"
  ],
  "properties": {
    "possible_values": "continuous level range; exact numeric minimum and maximum not documented",
    "valuenow": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left synthesizer section",
    "neighbours": [
      "OCTAVE selector",
      "WAVE select switch",
      "RANGE select switch"
    ],
    "source": "panel overview diagram"
  },
  "current_state": null,
  "source": [
    "monotribe_manual.pdf: VCO section, NOISE knob description",
    "monotribe_manual_visual_index.json: page 10 panel overview"
  ]
}

The NOISE knob is best represented as a Surface ARIA slider because it is a rotary knob controlling a continuous sound parameter: the white-noise level mixed with the VCO output. Do not expose valuenow unless there is live evidence of the knob’s current physical position.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual names the control and function, and the ARIA store directly maps rotary continuous controls to slider.
Unsupported-current-state risk: Low.
[/Trace]