Prompt: Represent the audio input as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.port.audio_in",
  "role": "port",
  "name": "AUDIO IN jack",
  "description": "External audio input. An external audio source connected here is mixed with the VCO output, then sent through the VCF and VCA. It can expand the monotribe’s sound or let the monotribe act as an effect processor for another audio source.",
  "region": "connection area",
  "group": "rear-panel audio connections",
  "parent": "monotribe.region.connection_area",
  "children": [],
  "physical_type": "3.5 mm stereo mini-phone jack",
  "actions": [
    "connect external audio source",
    "disconnect external audio source"
  ],
  "possible_states": [
    "connected",
    "not connected"
  ],
  "current_state": null,
  "properties": {
    "signal_direction": "input",
    "signal_type": "audio",
    "input_channels": "stereo accepted; mixed to mono",
    "processing_path": "AUDIO IN mixed with VCO output, then routed through VCF and VCA"
  },
  "spatial_properties": {
    "approximate_position": "rear-panel connection row",
    "ordering": "third item in the manual’s rear-panel connection diagram, after Power switch and DC 9V jack",
    "neighbours": {
      "left": "DC 9V jack",
      "right": "OUTPUT jack"
    },
    "navigation_hint": "From the rear-panel connection row, find the DC 9V power jack, then move one jack to the right. The next small audio jack is AUDIO IN."
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe Owner's manual, Connections section, p.8",
    "monotribe Owner's manual, Block diagram, p.6",
    "Surface ARIA Store: port role and current-state rules",
    "Surface Model and Map Schema: node and map fields"
  ]
}

The current connection state is deliberately null: the manual and static references define what the AUDIO IN jack is and what it can do, but they cannot tell whether a cable is connected right now.

[Trace]
Sources used: monotribe Owner’s manual p.8 Connections; monotribe Owner’s manual p.6 Block diagram; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents the AUDIO IN jack, signal path, connector type, and connection warning; ARIA role mapping is direct for a physical input jack.
Unsupported-current-state risk: Low.
[/Trace]