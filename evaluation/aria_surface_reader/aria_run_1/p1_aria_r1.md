Prompt: Represent the audio input as a Surface ARIA node. 

Response: 

I’ll ground this as a semantic Surface ARIA node: manual for the official AUDIO IN function, then ARIA/schema rules for role and fields.

Ragionato per 11s
{
  "node_id": "monotribe.port.audio_in",
  "role": "port",
  "name": "AUDIO IN jack",
  "description": "Accepts an external audio source; the input is mixed with the VCO output and then sent through the VCF and VCA.",
  "region": "connection area",
  "group": "rear-panel audio connections",
  "parent": "monotribe.region.connections",
  "physical_type": "3.5 mm stereo mini-phone jack",
  "actions": [
    "connect external audio source",
    "disconnect external audio source",
    "route audio into synth signal path"
  ],
  "properties": {
    "direction": "input",
    "signal_type": "external audio",
    "connector_type": "3.5 mm stereo mini-phone jack",
    "processing_path": "mixed with VCO output, then routed through VCF and VCA",
    "stereo_handling": "stereo input is mixed to mono"
  },
  "current_state": {
    "current_connection": "requires situated evidence"
  },
  "spatial_properties": {
    "approximate_position": "rear connection row",
    "order_in_group": 3,
    "near": [
      "DC 9V jack",
      "OUTPUT jack"
    ],
    "tactile_description": "small 3.5 mm jack in the rear-panel connection row",
    "navigation_hint": "From the rear connection row, AUDIO IN is the third item in the numbered connection sequence, after the power switch and DC 9V jack, before OUTPUT."
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf, Connections page: AUDIO IN jack function and warning",
    "monotribe_manual.pdf, Specifications: connector type",
    "Surface ARIA Store: physical connection points use role `port`; current cable connection requires situated evidence"
  ]
}

The role is port because Surface ARIA defines physical connection points such as audio input as ports, with valid properties including signal_type, direction, connector_type, and current_connection only when live evidence is available. The monotribe manual says the AUDIO IN jack takes an external audio source, mixes it with the VCO, sends it through the VCF and VCA, and mixes stereo input to mono. The manual also warns to turn power off before making connections. Static sources cannot tell whether a cable is currently plugged in.

[Trace]
Sources used: monotribe_manual.pdf p.8 Connections; monotribe_manual.pdf Specifications; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 5%.
Evidence confidence: High.
Confidence rationale: The official jack name/function and port-role mapping are directly supported; current connection is correctly left unknown.
Unsupported-current-state risk: Low.
[/Trace]