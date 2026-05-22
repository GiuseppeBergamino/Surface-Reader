Prompt: Represent the distortion as a Surface ARIA node. 

Response: 

The monotribe manual does not document a control officially named “distortion.” It documents the VCF PEAK knob, which increases resonance at the cutoff frequency, and the manual says the filter’s character changes significantly depending on its settings . So this node should be modeled conservatively as PEAK, not as an official “Distortion” control.

{
  "node_id": "monotribe.synth.vcf.peak",
  "role": "slider",
  "name": "PEAK",
  "description": "Adjusts the resonance of the VCF, adding emphasis to the cutoff frequency. High settings may be used musically for more aggressive filter character, but the manual does not name this as a distortion control.",
  "region": "Synthesizer section",
  "group": "VCF",
  "parent": "monotribe.synth.vcf",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase resonance/emphasis",
    "turn counterclockwise to decrease resonance/emphasis"
  ],
  "possible_states": {
    "value_range": "continuous knob travel; exact numeric range not documented"
  },
  "current_state": null,
  "properties": {
    "valuemin": null,
    "valuemax": null,
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "synthesizer section, VCF group",
    "relationship": "paired with CUTOFF; PEAK is the lower control in the filter pair",
    "neighbours": [
      "CUTOFF knob"
    ]
  },
  "safety_notes": [
    "Do not infer the current knob value from the manual or static panel references alone."
  ],
  "source": [
    "monotribe_manual.pdf, English manual page 11: VCF CUTOFF and PEAK descriptions",
    "monotribe_manual_p10.png: synthesizer section panel layout",
    "01_surface_aria_store.md: rotary knob controlling continuous value represented as role slider"
  ]
}

[Trace]
Sources used: monotribe_manual.pdf p.11; monotribe_manual_p10.png; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 20%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: Medium.
Confidence rationale: The PEAK control is documented and mappable, but “distortion” is not an official monotribe control name in the manual.
Unsupported-current-state risk: Low.
[/Trace]