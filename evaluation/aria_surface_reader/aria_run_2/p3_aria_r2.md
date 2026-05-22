Prompt: Represent the sync input as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.connection.sync_in",
  "role": "port",
  "name": "SYNC IN jack",
  "description": "Input jack for external sync pulses. When connected, the monotribe ignores its internal step clock and advances the sequencer steps according to pulses received at this jack.",
  "region": "connection area",
  "group": "sync I/O",
  "parent": "monotribe.connection_area",
  "physical_type": "3.5 mm monaural mini-phone jack",
  "actions": [
    "connect external sync source",
    "disconnect external sync source"
  ],
  "possible_states": {
    "connection": [
      "connected",
      "not connected"
    ],
    "sync_behavior_when_connected": "internal step clock ignored; sequencer advances according to input pulses",
    "polarity_setting": {
      "global_menu_step_button": 4,
      "LED_unlit": "step advances when input signal rises",
      "LED_lit": "step advances when input signal falls",
      "factory_default": "LED unlit"
    }
  },
  "current_state": null,
  "properties": {
    "input_type": "sync pulse input",
    "max_input_level": "20V"
  },
  "spatial_properties": {
    "surface_region": "rear connection row",
    "approximate_position": "right side of the rear-panel jack group",
    "neighbours": [
      "SYNC OUT jack to its left in the rear-panel connection group"
    ],
    "navigation_hint": "From the rear connection row, find the pair of sync mini-jacks; SYNC IN is the right-hand member of that pair."
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf: Connections, p.8",
    "monotribe_manual.pdf: Global menu, p.16",
    "monotribe_manual.pdf: Specifications, p.17",
    "monotribe_manual_visual_index.json: p.8 rear-panel jack diagram",
    "Surface ARIA Store: port role and current-state rules",
    "Surface Model and Map Schema: node and map fields"
  ]
}

Do not treat connected as current state here. It is only a possible state, because static sources cannot tell whether a cable is currently plugged into SYNC IN.

[Trace]
Sources used: monotribe_manual.pdf p.8, p.16, p.17 ; monotribe_manual_visual_index.json p.8 rear-panel jack diagram entry ; 01_surface_aria_store.md ; 05_surface_model_map_schema.md .
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 20%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: Manual explicitly documents SYNC IN behavior, polarity, and connector specification; static layout supports rear jack grouping.
Unsupported-current-state risk: Low.
[/Trace]