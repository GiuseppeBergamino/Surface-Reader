Prompt: Represent the step rythm level as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.rhythm_level",
  "role": "slider",
  "name": "RHYTHM knob",
  "description": "Adjusts the volume of the drum sound generator.",
  "region": "sequencer section",
  "group": "drum sound generator sequence controls",
  "parent": "monotribe.sequencer",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase drum sound generator volume",
    "turn counterclockwise to decrease drum sound generator volume"
  ],
  "possible_states": {
    "range": "continuous physical knob range; exact numeric minimum and maximum are not documented"
  },
  "current_state": null,
  "properties": {
    "valuemin": null,
    "valuemax": null,
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "lower-right area of the sequencer section",
    "nearby_controls": [
      "STEP buttons",
      "PART buttons",
      "sequencer controls"
    ],
    "navigation_hint": "From the performer’s perspective, use the lower sequencer area as the landmark. The RHYTHM knob is the rotary control for the drum sound generator level."
  },
  "source": [
    "monotribe_manual.pdf: sequencer section, drum sound generator sequence controls; RHYTHM knob adjusts drum sound generator volume :contentReference[oaicite:0]{index=0}",
    "monotribe_manual_visual_index.json: sequencer section panel overview and behavior diagrams :contentReference[oaicite:1]{index=1}",
    "Surface ARIA Store: rotary knob controlling a continuous value is represented as role `slider`; `valuenow` requires current-state evidence :contentReference[oaicite:2]{index=2}",
    "Surface Model and Map Schema: surface model/map node fields and spatial properties :contentReference[oaicite:3]{index=3}"
  ]
}

Current knob position cannot be represented from the manual or static panel references alone, so valuenow stays null.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual identifies RHYTHM as the drum sound generator volume control, and the ARIA store defines continuous rotary controls as sliders.
Unsupported-current-state risk: Low.
[/Trace]