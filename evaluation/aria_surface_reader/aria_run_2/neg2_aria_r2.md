Prompt: Represent the distortion as a Surface ARIA node. 

Response: 

The monotribe manual does not document an official control named “Distortion.” The closest grounded representation is an inferred effect concept tied to the documented audio path: external audio can enter through AUDIO IN, be mixed with the VCO, and pass through the VCF and VCA; the manual says this can let the monotribe act as an effect processor.

{
  "node_id": "effect_distortion_inferred",
  "role": "group",
  "name": "Distortion",
  "description": "Inferred sound-processing effect concept; not an official monotribe control name in the manual.",
  "region": "Synthesizer section",
  "group": "External audio processing / sound shaping",
  "parent": "synthesizer_section",
  "children": [
    "port_audio_in",
    "filter_cutoff",
    "filter_peak",
    "amp_level"
  ],
  "physical_type": "not a dedicated physical control",
  "actions": [
    "route external audio through AUDIO IN",
    "shape the signal with VCF controls",
    "adjust output level with VCA LEVEL"
  ],
  "possible_states": "No documented distortion on/off or amount states.",
  "current_state": "requires situated evidence",
  "properties": {
    "semantic_status": "inferred_effect_concept",
    "official_manual_control": false,
    "dedicated_control": false
  },
  "spatial_properties": {
    "navigation_hint": "There is no separate Distortion knob or switch to locate. Use the AUDIO IN port for external input, then the VCF and VCA controls for sound shaping."
  },
  "source": [
    "monotribe_manual.pdf: AUDIO IN and synthesizer signal path",
    "01_surface_aria_store.md: group/node validity rules",
    "05_surface_model_map_schema.md: surface model node fields"
  ]
}

A stricter model could omit this node entirely and instead represent only the documented nodes: AUDIO IN as a port, CUTOFF and PEAK as slider controls, and LEVEL as a slider.

[Trace]
Sources used: monotribe_manual.pdf; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Surface ARIA Store 25%; Surface Model/Map Schema 20%; Routing/Uncertainty Policy 10%.
Evidence confidence: Medium.
Confidence rationale: The manual supports external audio processing, but “Distortion” is not documented as an official monotribe control.
Unsupported-current-state risk: Low.
[/Trace]