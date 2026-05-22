Prompt: Represent the cutoff as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vcf.cutoff",
  "role": "slider",
  "name": "CUTOFF knob",
  "description": "Adjusts the cutoff frequency of the VCF, affecting the brightness of the sound.",
  "region": "Synthesizer section",
  "group": "VCF",
  "parent": "monotribe.synthesizer.vcf",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to brighten the sound",
    "turn counterclockwise to darken the sound"
  ],
  "possible_states": {
    "range": "continuous knob position; exact numeric range not documented in the manual",
    "musical_effect": {
      "left": "darker sound",
      "right": "brighter sound"
    }
  },
  "current_state": null,
  "properties": {
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-middle area of the top panel",
    "local_arrangement": "upper control in the VCF knob pair",
    "neighbours": {
      "below": "PEAK knob"
    },
    "navigation_hint": "From the performer’s perspective, find the filter pair in the upper-middle area; CUTOFF is the upper rotary knob, with PEAK directly below it."
  },
  "source": [
    "monotribe Owner's manual: VCF / CUTOFF knob description",
    "monotribe manual visual index: page 10 panel overview",
    "Surface ARIA Store: rotary knob controlling a continuous value is represented as role slider"
  ],
  "notes": [
    "Do not expose valuenow or current knob position without situated evidence.",
    "Static sources support the control name, function, physical type, and layout, but not the current cutoff setting."
  ]
}

The cutoff is best represented as a slider role because it is a continuous rotary knob controlling a continuous sound parameter, not a discrete switch. The manual says the CUTOFF knob adjusts the VCF cutoff frequency: left makes the sound darker, right makes it brighter. The Surface ARIA Store defines rotary knobs controlling continuous values as slider nodes and forbids reporting valuenow from static sources alone.

[Trace]
Sources used: monotribe Owner’s manual, manual page 10 visual index entry, Surface ARIA Store, Surface Model/Map Schema.
Routing weights: Device manual 35%, Visual/static layout 20%, Surface ARIA Store 35%, Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual documents the control and function, while Surface ARIA directly defines the appropriate semantic role.
Unsupported-current-state risk: Low.
[/Trace]