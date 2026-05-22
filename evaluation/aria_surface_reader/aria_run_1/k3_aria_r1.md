Prompt: Represent the step rythm level as a Surface ARIA node. 

Response: 

I’ll model this as a semantic Surface ARIA node, grounded in the monotribe manual’s “RHYTHM knob” unless you intended a different rhythm-related control.

Ragionato per 9s

The closest supported monotribe control is the RHYTHM knob, not a per-step rhythm “level.” The manual says the RHYTHM knob “adjusts the volume of the drum sound generator” . As a continuous rotary control, it should be represented as a Surface ARIA slider, because rotary knobs controlling continuous values map to slider nodes .

{
  "node_id": "sequencer_drum_rhythm_level",
  "role": "slider",
  "name": "RHYTHM knob",
  "description": "Adjusts the volume of the drum sound generator.",
  "region": "Sequencer section",
  "group": "Drum sound generator sequence controls",
  "parent": "sequencer_section",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase drum sound generator volume",
    "turn counterclockwise to decrease drum sound generator volume"
  ],
  "possible_states": "continuous level; exact numeric range not documented in the available manual text",
  "current_state": "requires situated evidence",
  "properties": {
    "valuemin": "not documented",
    "valuemax": "not documented",
    "valuenow": "requires situated evidence",
    "valuetext": "requires situated evidence"
  },
  "spatial_properties": {
    "region": "Sequencer section",
    "group": "Drum sound generator sequence controls",
    "tactile_description": "rotary knob for overall rhythm/drum level; exact current position cannot be inferred from static sources"
  },
  "source": {
    "manual": "monotribe_manual.pdf, Sequencer section, Drum sound generator sequence controls",
    "semantic_rule": "Surface ARIA Store: rotary knob controlling a continuous value uses role slider"
  }
}

If you meant the step buttons for rhythm sequencing, those should be separate button nodes, because the manual says they turn each step of the selected drum part on or off, not adjust level .

[Trace]
Sources used: monotribe_manual.pdf p.15/manual page uncertain; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Surface ARIA Store 40%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies RHYTHM as a knob controlling drum-generator volume, and the ARIA store explicitly maps continuous rotary controls to slider.
Unsupported-current-state risk: Low.
[/Trace]