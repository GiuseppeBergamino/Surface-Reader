Prompt: Represent the sync input as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sync_in",
  "role": "port",
  "name": "SYNC IN jack",
  "description": "Input port for external sync pulses. When connected, the monotribe ignores its internal step clock and advances the sequencer according to incoming pulses.",
  "region": "connection area",
  "group": "sync I/O",
  "parent": "monotribe.rear_panel_connections",
  "physical_type": "3.5 mm monaural mini-phone jack",
  "actions": [
    "connect external sync pulse source",
    "disconnect external sync pulse source"
  ],
  "possible_states": {
    "connection": [
      "connected",
      "not connected"
    ],
    "sync_behavior": [
      "internal step clock active when SYNC IN is not connected",
      "sequencer advances from incoming pulses when SYNC IN is connected"
    ],
    "polarity": [
      {
        "value": "rising",
        "meaning": "step advances when the input signal rises",
        "global_menu": "step button 4 LED unlit"
      },
      {
        "value": "falling",
        "meaning": "step advances when the input signal falls",
        "global_menu": "step button 4 LED lit"
      }
    ]
  },
  "current_state": null,
  "properties": {
    "input_signal_type": "sync pulse",
    "maximum_input_level": "20V",
    "current_connection_state_requires_situated_evidence": true,
    "current_polarity_requires_current_global_menu_evidence": true
  },
  "spatial_properties": {
    "surface": "rear connection panel",
    "approximate_position": "right side of rear-panel jack row from performer/device-front perspective, paired with SYNC OUT",
    "neighbours": {
      "left": "SYNC OUT jack"
    },
    "tactile_description": "small round mini-jack in the rear connection row, next to the SYNC OUT mini-jack"
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf: Connections, SYNC IN jack, Global menu sync polarity, Specifications",
    "monotribe_manual_visual_index.json: page 8 rear-panel jack diagram",
    "01_surface_aria_store.md: port role and current-state rules",
    "05_surface_model_map_schema.md: node and map field structure"
  ]
}

The current_state is intentionally null: a static manual or panel reference can define what SYNC IN can do, but cannot tell whether a cable is currently connected or which global polarity setting is currently active.

[Trace]
Sources used: monotribe_manual.pdf ; monotribe_manual_visual_index.json ; 01_surface_aria_store.md ; 05_surface_model_map_schema.md
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents SYNC IN function, polarity, connector type, and maximum input level; the schema/store define the semantic node structure.
Unsupported-current-state risk: Low.
[/Trace]