Prompt: Represent the headphones output as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.port.headphones",
  "role": "port",
  "name": "HEADPHONES jack",
  "description": "Stereo headphone output connection for monitoring the monotribe with headphones.",
  "region": "connection area",
  "group": "rear-panel audio connections",
  "parent": "monotribe.region.connections",
  "children": [],
  "physical_type": "3.5 mm stereo mini-phone jack",
  "actions": [
    "connect headphones with a stereo mini-plug",
    "disconnect headphones"
  ],
  "possible_states": [
    "connected",
    "not connected"
  ],
  "current_state": null,
  "properties": {
    "signal_direction": "output",
    "connector_type": "ø3.5 mm stereo mini-phone jack",
    "accepts": "headphones, stereo mini-plug"
  },
  "spatial_properties": {
    "approximate_position": "rear connection area",
    "ordering": "fifth labeled connection in the manual’s rear-panel connection diagram",
    "neighbours": {
      "left": "OUTPUT jack",
      "right": "SYNC OUT jack"
    },
    "navigation_hint": "On the rear connection row, find the audio output jacks; the HEADPHONES jack is the small stereo mini-jack after the larger OUTPUT jack and before the SYNC OUT jack."
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf, Connections section, p.8",
    "monotribe_manual_visual_index.json, p.8 rear-panel jack diagram",
    "Surface ARIA Store: physical input/output connectors should be represented as role `port`"
  ]
}

The manual identifies this as “HEADPHONES jack” and says: “Connect your headphones (stereo mini-plug) here.” The visual index identifies page 8 as the rear-panel connection diagram covering audio in/out, headphones, and sync jacks. The Surface ARIA Store classifies physical input/output connectors as port nodes.

Current connection state is not included, because static sources cannot determine whether headphones are plugged in right now.

[Trace]
Sources used: monotribe_manual.pdf p.8; monotribe_manual_visual_index.json p.8 entry; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 20%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the jack, function, and connector type; the visual index supports rear-panel placement.
Unsupported-current-state risk: Low.
[/Trace]