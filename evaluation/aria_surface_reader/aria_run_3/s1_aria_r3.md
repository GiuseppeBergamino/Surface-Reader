Prompt: Represent the keyboard range control as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.synth.vco.range_select",
  "role": "switch",
  "name": "RANGE select switch",
  "description": "Specifies the ribbon keyboard’s playing mode.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synth.vco",
  "children": [],
  "physical_type": "multi-position switch",
  "actions": [
    "set to WIDE",
    "set to NARROW",
    "set to KEY"
  ],
  "possible_states": [
    {
      "name": "WIDE",
      "description": "The pitch range is extended to approximately six times that of NARROW; pitch change is continuous; the OCTAVE selector is ignored."
    },
    {
      "name": "NARROW",
      "description": "The pitch changes continuously according to the printed ribbon keyboard."
    },
    {
      "name": "KEY",
      "description": "The pitch changes in chromatic steps according to the printed ribbon keyboard."
    }
  ],
  "current_state": null,
  "properties": {
    "orientation": "discrete",
    "valuetext": null,
    "valuenow": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left area of the synthesizer section",
    "nearby_controls": [
      "OCTAVE selector",
      "WAVE select switch",
      "NOISE knob",
      "Ribbon keyboard"
    ],
    "layout_note": "Identified as control 4 in the synthesizer-section panel overview."
  },
  "source": [
    "monotribe_manual.pdf, p.10 panel overview",
    "monotribe_manual.pdf, p.11 RANGE select switch description",
    "monotribe_manual_visual_index.json entry for p.10",
    "Surface ARIA Store switch role rules"
  ]
}

The keyboard range control should be a switch, not a slider, because it has three documented discrete settings: WIDE, NARROW, and KEY. Its current_state, valuenow, and current valuetext must remain null unless there is situated evidence of the actual switch position. The manual defines the control as the “RANGE select switch” and documents the three possible modes for the ribbon keyboard. The visual index identifies page 10 as the synthesizer-section panel overview used for layout mapping. The Surface ARIA Store assigns discrete-position selectors to the switch role and reserves current-state properties for situated evidence only.

[Trace]
Sources used: monotribe_manual.pdf p.10 and p.11; monotribe_manual_visual_index.json p.10 entry; 01_surface_aria_store.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 5%.
Evidence confidence: High.
Confidence rationale: Official function and possible states are documented, and the semantic role follows the Surface ARIA discrete-control rule.
Unsupported-current-state risk: Low.
[/Trace]