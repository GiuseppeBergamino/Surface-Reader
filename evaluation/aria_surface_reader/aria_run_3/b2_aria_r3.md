Prompt: Represent the rec button as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.synth_sequence.rec_button",
  "role": "button",
  "name": "REC button",
  "description": "Press during playback to enter record mode for the synth performance data. Press while stopped to enter record-ready mode. Press again to exit record or record-ready mode.",
  "region": "Sequencer section",
  "group": "Synthesizer sequence controls",
  "parent": "monotribe.sequencer",
  "children": [
    "monotribe.sequencer.synth_sequence.rec_led"
  ],
  "physical_type": "button",
  "actions": [
    "press",
    "press again",
    "hold"
  ],
  "possible_states": [
    {
      "state": "record mode",
      "indicator": "REC LED lit",
      "meaning": "Performance data from the ribbon keyboard will be recorded during playback."
    },
    {
      "state": "record-ready mode",
      "indicator": "REC LED blinking",
      "meaning": "Pressing PLAY will start playback and activate record mode."
    },
    {
      "state": "inactive",
      "indicator": "REC LED dark",
      "meaning": "Record mode and record-ready mode are off."
    }
  ],
  "current_state": null,
  "properties": {
    "aria_equivalent_role": "button",
    "pressed": null,
    "active": null,
    "valuenow": null
  },
  "spatial_properties": {
    "approximate_position": "Sequencer section, synth sequence control cluster",
    "neighbours": [
      "FLUX button",
      "GATE TIME button",
      "PLAY button"
    ],
    "layout_source": "manual sequencer section diagram, page 13"
  },
  "safety_notes": [
    "The REC button is also used to save a sequence: when the sequencer is stopped and the monotribe is not producing sound, hold REC until the REC LED stops blinking and goes dark.",
    "Never turn off the power while data is being saved."
  ],
  "source": [
    "monotribe_manual.pdf, pages 13, 15, 16",
    "monotribe_manual_visual_index.json, page 13 sequencer layout entry",
    "01_surface_aria_store.md",
    "05_surface_model_map_schema.md"
  ]
}

current_state, pressed, and active are null because static sources define possible states but cannot tell whether the REC button is currently active, pressed, lit, or blinking.

[Trace]
Sources used: monotribe_manual.pdf pages 13, 15, 16; monotribe_manual_visual_index.json page 13 entry; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual directly documents REC behavior and LED meanings; ARIA role mapping for buttons is explicit.
Unsupported-current-state risk: Low.
[/Trace]