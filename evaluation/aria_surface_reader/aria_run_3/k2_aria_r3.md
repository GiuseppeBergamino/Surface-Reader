Prompt: Represent the noise level as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vco.noise.level",
  "role": "slider",
  "name": "NOISE knob",
  "description": "Adjusts the level of white noise mixed with the VCO output.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.vco",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase the white-noise level",
    "turn counterclockwise to decrease the white-noise level"
  ],
  "properties": {
    "possible_values": "continuous level range, exact numeric range not documented",
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left area of the synthesizer section",
    "ordering": "control 3 in the manual's synthesizer-section panel diagram",
    "neighbours": [
      "OCTAVE selector",
      "WAVE select switch",
      "RANGE select switch"
    ]
  },
  "current_state": null,
  "source": [
    "monotribe_manual.pdf, synthesizer section: VCO / NOISE knob",
    "monotribe_manual_visual_index.json, page 10 panel overview"
  ],
  "notes": "Do not expose valuenow from static sources alone; the current knob position requires situated evidence."
}

The manual defines the NOISE knob as the control that “adjusts the level of white noise that’s mixed with the VCO output” . In Surface ARIA terms, it is best represented as a slider because it is a continuous value control, with physical type rotary knob .

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual names and defines the NOISE knob, and the ARIA store clearly maps continuous rotary controls to slider.
Unsupported-current-state risk: Low.
[/Trace]