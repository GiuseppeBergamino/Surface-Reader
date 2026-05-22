Prompt: Represent the play button as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.transport.play",
  "role": "button",
  "name": "PLAY button",
  "description": "Starts or stops the sequence. Playback always starts from the beginning of the sequence.",
  "region": "Sequencer section",
  "group": "Basic controls / transport controls",
  "parent": "monotribe.sequencer",
  "physical_type": "button",
  "actions": [
    "press"
  ],
  "possible_states": [
    {
      "state": "playback_running",
      "indicator": "PLAY LED lit",
      "meaning": "The sequence is playing back."
    },
    {
      "state": "playback_stopped",
      "meaning": "The sequence is not playing back."
    }
  ],
  "current_state": null,
  "properties": {
    "has_indicator": true,
    "indicator_name": "PLAY LED",
    "valuenow": null
  },
  "spatial_properties": {
    "surface_region": "sequencer section",
    "layout_source": "manual sequencer-section panel overview",
    "approximate_position": "upper area of the sequencer control cluster",
    "neighbours": [
      "ACTIVE STEP button",
      "TEMPO knob",
      "FLUX button",
      "REC button",
      "GATE TIME button"
    ]
  },
  "source": [
    "monotribe_manual.pdf, Sequencer section, Basic controls: PLAY button",
    "monotribe_manual_visual_index.json, page 13 sequencer section panel overview"
  ],
  "notes": [
    "Do not expose `pressed`, `active`, or the current PLAY LED state without situated evidence.",
    "Do not use `valuenow`; Surface ARIA `button` nodes do not support continuous values."
  ]
}

The manual defines the PLAY button as control 4 in the Sequencer section: pressing it plays or stops the sequence, playback starts from the beginning, and the PLAY LED is lit during playback. The visual index identifies manual page 13 as the sequencer-section panel overview for mapping transport and sequencer controls.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names and defines the PLAY button, while the schema sources define the correct semantic role and node fields.
Unsupported-current-state risk: Low.
[/Trace]