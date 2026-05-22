Prompt: Represent the distortion as a Surface ARIA node. 

Response: 

I cannot create a grounded Monotribe Surface ARIA node for “Distortion” as a device control, because the provided monotribe manual sources do not document an official control or section named Distortion.

The closest grounded representation is the external audio processing path, because the manual says the AUDIO IN jack lets an external audio source be mixed with the VCO and sent through the VCF and VCA, allowing the monotribe to be used “as an effect processor for a separate audio source.”

{
  "node_id": "monotribe_audio_in_effect_processing",
  "role": "port",
  "name": "AUDIO IN jack",
  "description": "External audio input mixed with the VCO and routed through the VCF and VCA; the manual says this can be used to expand the monotribe’s sonic possibilities or as an effect processor for a separate audio source.",
  "region": "connection area",
  "group": "audio input/output",
  "parent": "monotribe_connection_area",
  "physical_type": "3.5 mm stereo mini-phone jack",
  "actions": [
    "connect external audio source"
  ],
  "possible_states": [
    "external audio source connected",
    "external audio source not connected"
  ],
  "current_state": null,
  "properties": {
    "signal_path": "AUDIO IN mixed with VCO output, then routed through VCF and VCA",
    "documented_use": "effect processor for an external audio source"
  },
  "spatial_properties": {
    "approximate_position": "rear-panel connection area",
    "neighbours": [
      "DC 9V jack",
      "OUTPUT jack"
    ]
  },
  "safety_notes": [
    "Turn off the power before connecting anything; careless usage may damage the speaker system or cause other malfunctions."
  ],
  "source": [
    "monotribe_manual.pdf: Connections, AUDIO IN jack",
    "monotribe_manual_visual_index.json: page 8 rear-panel connections"
  ],
  "unsupported_inference_note": "No official Distortion control, distortion parameter, or distortion effect node is documented in the available monotribe sources. Do not expose this as a dedicated control unless supported by additional evidence."
}

A dedicated distortion node would be unsafe unless modeled as a user-defined or downstream audio effect outside the monotribe’s documented control surface.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 10%; Surface ARIA Store 25%; Surface Model/Map Schema 15%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual supports AUDIO IN effect-processing but does not support a named Distortion control.
Unsupported-current-state risk: Low.
[/Trace]