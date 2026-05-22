Prompt: Represent the oscillator octave control as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vco.octave_selector",
  "role": "switch",
  "name": "OCTAVE selector",
  "description": "Specifies the VCO pitch in steps of an octave.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synthesizer_section.vco",
  "physical_type": "discrete selector",
  "actions": [
    "select octave position",
    "move to one of the documented octave settings"
  ],
  "possible_states": [
    {
      "valuetext": "64'",
      "description": "With this setting, the pitch range of the ribbon keyboard is A0–D2."
    }
  ],
  "current_state": null,
  "properties": {
    "possible_values": "Documented octave steps; full set not fully available from the provided text snippet.",
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left area of the Synthesizer section",
    "ordering": "control 1 in the manual’s Synthesizer section diagram",
    "neighbours": [
      "WAVE select switch",
      "NOISE knob",
      "RANGE select switch"
    ],
    "source": "manual panel overview, page 10"
  },
  "source": [
    "monotribe_manual.pdf: VCO description and OCTAVE selector function",
    "monotribe_manual_visual_index.json: page 10 panel overview"
  ],
  "notes": [
    "Represented as role `switch` because it is a discrete-position pitch selector, not a continuous value control.",
    "Do not expose `valuenow` or current `valuetext` without situated evidence of the actual physical selector position."
  ]
}

The manual identifies the official control as OCTAVE selector and says it specifies the VCO pitch in octave steps; it also documents that the 64' setting gives the ribbon keyboard a pitch range of A0–D2.
The visual index identifies page 10 as the Synthesizer section panel overview used for control identity and grouping.
The Surface ARIA Store says discrete-position selectors should be represented as switch, while current-state properties require situated evidence.

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 01_surface_aria_store.md, 05_surface_model_map_schema.md, 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: Medium.
Confidence rationale: Function and grouping are manual-grounded; full octave value set was not fully visible in the provided excerpt.
Unsupported-current-state risk: Low.
[/Trace]