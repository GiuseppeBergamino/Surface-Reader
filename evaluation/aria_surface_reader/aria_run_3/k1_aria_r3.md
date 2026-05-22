Prompt: Represent the cutoff as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.synth.vcf.cutoff",
  "role": "slider",
  "name": "CUTOFF knob",
  "description": "Adjusts the cutoff frequency of the VCF, affecting the brightness of the sound.",
  "region": "Synthesizer section",
  "group": "VCF",
  "parent": "monotribe.synth.vcf",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise",
    "turn counterclockwise",
    "increase cutoff frequency",
    "decrease cutoff frequency"
  ],
  "possible_values": {
    "type": "continuous",
    "documented_directional_meaning": {
      "counterclockwise": "darker sound",
      "clockwise": "brighter sound"
    }
  },
  "properties": {
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-middle area of the synthesizer section",
    "group_relation": "upper control in the VCF pair, with PEAK below it",
    "nearby_controls": [
      "PEAK knob below",
      "VCO controls to the left",
      "VCA LEVEL knob to the right"
    ]
  },
  "current_state": null,
  "source": [
    "monotribe_manual.pdf, English panel description, VCF section",
    "monotribe_manual_visual_index.json, page 10 panel overview",
    "01_surface_aria_store.md"
  ]
}

Use role: "slider" because Surface ARIA treats a continuous rotary knob as a slider, with physical_type: "rotary knob". The manual says CUTOFF adjusts the VCF cutoff frequency: left darkens the sound, right brightens it. The current cutoff value must stay null unless there is live evidence of the knob position.

[Trace]
Sources used: monotribe_manual.pdf p.11 / manual page uncertain in uploaded citation view; monotribe_manual_visual_index.json entry for p.10; 01_surface_aria_store.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 5%.
Evidence confidence: High.
Confidence rationale: Official function and naming are in the manual; semantic role follows the Surface ARIA continuous-control rule.
Unsupported-current-state risk: Low.
[/Trace]