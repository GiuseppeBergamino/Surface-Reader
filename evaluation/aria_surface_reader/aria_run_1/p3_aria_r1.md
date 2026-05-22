Prompt: Represent the sync input as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.port.sync_in",
  "role": "port",
  "name": "SYNC IN jack",
  "description": "Receives sync pulses. When connected, the monotribe ignores its internal step clock and advances the sequencer steps according to incoming pulses.",
  "region": "connection area",
  "group": "sync I/O",
  "parent": "monotribe.region.connections",
  "children": [],
  "physical_type": "3.5 mm monaural mini-phone jack",
  "actions": [
    "connect compatible sync pulse source",
    "disconnect sync cable"
  ],
  "possible_states": {
    "connection": [
      "connected",
      "not connected"
    ],
    "sync_in_polarity": [
      "step advances when input signal rises",
      "step advances when input signal falls"
    ]
  },
  "current_state": null,
  "properties": {
    "direction": "input",
    "signal_type": "sync pulse",
    "maximum_input_level": "20V"
  },
  "spatial_properties": {
    "surface_area": "rear connection panel",
    "approximate_position": "right side of the connection row, near SYNC OUT",
    "neighbours": [
      "SYNC OUT jack"
    ],
    "navigation_hint": "On the rear connection row, find the pair of sync mini-jacks. SYNC IN is the input jack next to SYNC OUT."
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf, Connections section, page 8",
    "monotribe_manual.pdf, Specifications section, page 17",
    "monotribe_manual_visual_index.json, page 8 rear-panel jack diagram",
    "01_surface_aria_store.md",
    "05_surface_model_map_schema.md"
  ]
}

The key semantic choice is role: "port" because this is a physical input connector, not a control. Its current_state is null because a static manual or panel reference cannot determine whether a cable is currently connected.

The manual defines the SYNC IN jack as the connector that makes the sequencer advance from incoming pulses instead of the internal step clock, and it also documents the polarity options in the Global menu.

[Trace]
Sources used: monotribe_manual.pdf page 8 and page 17; monotribe_manual_visual_index.json page 8 entry; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names and defines SYNC IN, while the ARIA/schema stores directly support representing connectors as ports.
Unsupported-current-state risk: Low.
[/Trace]