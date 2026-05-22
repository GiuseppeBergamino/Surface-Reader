Prompt: Represent the cutoff as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vcf.cutoff",
  "role": "slider",
  "name": "CUTOFF knob",
  "description": "Adjusts the cutoff frequency of the VCF, affecting the brightness of the sound. Turning left darkens the sound; turning right brightens it.",
  "region": "Synthesizer section",
  "group": "VCF",
  "parent": "monotribe.synthesizer_section.vcf",
  "physical_type": "rotary knob",
  "actions": [
    "turn counterclockwise to decrease cutoff frequency / darken sound",
    "turn clockwise to increase cutoff frequency / brighten sound"
  ],
  "possible_states": {
    "value_type": "continuous",
    "meaning": "cutoff frequency amount"
  },
  "current_state": null,
  "properties": {
    "orientation": "rotary",
    "valuenow": null
  },
  "spatial_properties": {
    "approximate_position": "upper-middle area of the synthesizer section",
    "group_relation": "part of the VCF filter pair",
    "neighbours": {
      "below": "PEAK knob",
      "nearby_group": "VCA LEVEL knob to the right, VCO controls to the left"
    },
    "tactile_description": "upper rotary knob in the two-knob VCF filter group"
  },
  "source": [
    "monotribe_manual.pdf, English panel description, Synthesizer section: VCF CUTOFF knob",
    "monotribe_manual_visual_index.json, page 10 panel overview",
    "foto_pannello.jpeg static top-panel reference",
    "01_surface_aria_store.md slider role rules"
  ]
}

The key ARIA choice is role: "slider" because Cutoff is a continuous rotary knob, not a discrete switch. Do not expose valuenow unless there is live evidence of the knob’s current physical position; static manual and panel sources only support possible function and location.

[Trace]
Sources used: monotribe_manual.pdf, English Synthesizer section / VCF CUTOFF knob; monotribe_manual_visual_index.json page 10 panel overview; foto_pannello.jpeg static panel photo; 01_surface_aria_store.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 30%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual names and defines CUTOFF, and static layout sources support its physical grouping as a rotary knob in the VCF area.
Unsupported-current-state risk: Low.
[/Trace]