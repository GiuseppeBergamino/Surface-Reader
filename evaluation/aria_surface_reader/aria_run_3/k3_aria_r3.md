Prompt: Represent the step rythm level as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.rhythm.level",
  "role": "slider",
  "name": "RHYTHM knob",
  "description": "Adjusts the volume of the drum sound generator.",
  "region": "Sequencer section",
  "group": "Drum sound generator sequence controls",
  "parent": "monotribe.sequencer",
  "children": [],
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase drum sound generator level",
    "turn counterclockwise to decrease drum sound generator level"
  ],
  "possible_states": {
    "range": "continuous level range; exact numeric minimum and maximum are not documented"
  },
  "current_state": null,
  "properties": {
    "valuemin": null,
    "valuemax": null,
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, near the drum sequence controls",
    "landmarks": [
      "near the row of STEP buttons",
      "associated with BD, SN, and HH drum parts"
    ]
  },
  "source": [
    "monotribe_manual.pdf, Sequencer section / Drum sound generator sequence controls",
    "Surface ARIA Store: rotary knob controlling a continuous value is represented as role slider"
  ],
  "notes": [
    "Do not expose valuenow unless there is situated evidence of the current knob position.",
    "This node represents the overall rhythm/drum generator level, not the on/off state of an individual rhythm step."
  ]
}

The manual identifies RHYTHM knob as the control that “adjusts the volume of the drum sound generator” . Semantically, because it is a rotary knob controlling a continuous level, it should be represented as a Surface ARIA slider rather than a button or switch .

[Trace]
Sources used: monotribe_manual.pdf; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Surface ARIA Store 35%; Surface Model/Map Schema 20%.
Evidence confidence: High.
Confidence rationale: The manual directly names the RHYTHM knob and its function, and the ARIA store directly maps continuous rotary controls to slider.
Unsupported-current-state risk: Low.
[/Trace]