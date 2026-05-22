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
  "physical_type": "multi-position slide switch",
  "actions": [
    "move to WIDE",
    "move to NARROW",
    "move to KEY"
  ],
  "possible_states": [
    {
      "name": "WIDE",
      "meaning": "The pitch range is extended to approximately six times that of NARROW; pitch change is continuous; the OCTAVE selector is ignored."
    },
    {
      "name": "NARROW",
      "meaning": "The pitch changes continuously according to the printed ribbon keyboard."
    },
    {
      "name": "KEY",
      "meaning": "The pitch changes in chromatic steps according to the printed ribbon keyboard."
    }
  ],
  "current_state": null,
  "properties": {
    "orientation": "discrete-position selector",
    "possible_values": ["WIDE", "NARROW", "KEY"],
    "valuetext": "Only valid when describing possible documented values; current valuetext requires situated evidence."
  },
  "spatial_properties": {
    "approximate_position": "synthesizer section, VCO group, near the upper-left control area",
    "neighbours": [
      "OCTAVE selector",
      "WAVE select switch",
      "NOISE knob",
      "Ribbon keyboard"
    ],
    "tactile_landmark": "part of the VCO control cluster above the ribbon keyboard"
  },
  "source": [
    "monotribe_manual.pdf, Panel description and functions, Synthesizer section, RANGE select switch",
    "monotribe_manual_visual_index.json, page 10 panel overview",
    "01_surface_aria_store.md, switch role definition",
    "05_surface_model_map_schema.md, surface model node fields"
  ]
}

The key semantic choice is role: "switch" because this control has three documented discrete positions: WIDE, NARROW, and KEY. Its current position is intentionally left as null; a manual or static panel image can define possible states, but cannot tell which one is currently selected.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the RANGE select switch and its three documented settings; the ARIA role follows the discrete-selector rule.
Unsupported-current-state risk: Low.
[/Trace]