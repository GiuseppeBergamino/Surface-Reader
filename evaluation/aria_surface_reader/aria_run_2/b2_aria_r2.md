Prompt: Represent the rec button as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.synth_sequence.rec",
  "role": "button",
  "name": "REC button",
  "description": "Puts the monotribe into record mode during playback, or record-ready mode while stopped. Press again to exit record or record-ready mode.",
  "region": "sequencer section",
  "group": "synthesizer sequence controls",
  "parent": "monotribe.sequencer.synth_sequence",
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
      "condition": "REC button is pressed during playback",
      "indicator": "REC LED lights up"
    },
    {
      "state": "record-ready mode",
      "condition": "REC button is pressed while stopped",
      "indicator": "REC LED blinks"
    },
    {
      "state": "inactive",
      "condition": "REC button is pressed again from record or record-ready mode",
      "indicator": "REC LED goes dark"
    },
    {
      "state": "save sequence action",
      "condition": "When the sequencer is stopped and the monotribe is not producing sound, hold REC until the REC LED stops blinking and goes dark"
    }
  ],
  "current_state": null,
  "properties": {
    "supports_pressed": true,
    "supports_active": true,
    "supports_valuenow": false,
    "state_requires_situated_evidence": true
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, upper area of the sequencer controls",
    "neighbours": [
      "FLUX button",
      "GATE TIME button",
      "PLAY button"
    ],
    "spatial_description": "In the sequencer section’s synthesizer sequence controls, the REC button is grouped with FLUX and GATE TIME, near the PLAY transport control.",
    "tactile_description": "Small pressable button in the sequencer control cluster."
  },
  "source": {
    "device_manual": "monotribe_manual.pdf, English manual, sequencer section, REC button description",
    "visual_static_layout": [
      "monotribe_manual_visual_index.json entry for PDF page 13: sequencer section panel overview",
      "monotribe_manual_p13.png",
      "foto_pannello.jpeg"
    ],
    "semantic_rules": [
      "01_surface_aria_store.md: button role rules",
      "05_surface_model_map_schema.md: surface model node fields"
    ]
  }
}

The REC LED should be a separate child indicator node, not folded into the button’s current state. Static sources can define what its lit, blinking, or dark states mean, but they cannot tell whether it is currently lit or blinking.

[Trace]
Sources used: monotribe_manual.pdf p.15/p.16 text as surfaced in uploaded-file context ; monotribe_manual_visual_index.json sequencer-section entry ; 01_surface_aria_store.md button role rules ; 05_surface_model_map_schema.md node fields ; foto_pannello.jpeg; monotribe_manual_p13.png.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines the REC button behavior, and the semantic role follows the Surface ARIA button rules.
Unsupported-current-state risk: Low.
[/Trace]