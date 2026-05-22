Prompt: Represent the keyboard range control as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.synthesizer.vco.range_select_switch",
  "role": "switch",
  "name": "RANGE select switch",
  "description": "Specifies the ribbon keyboard’s playing mode.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synthesizer.vco",
  "physical_type": "multi-position switch",
  "actions": [
    "set to WIDE",
    "set to NARROW",
    "set to KEY"
  ],
  "possible_states": [
    {
      "value": "WIDE",
      "meaning": "The pitch range is extended to approximately six times that of NARROW; pitch change is continuous; the OCTAVE selector is ignored."
    },
    {
      "value": "NARROW",
      "meaning": "The pitch changes continuously according to the printed ribbon keyboard."
    },
    {
      "value": "KEY",
      "meaning": "The pitch changes in chromatic steps according to the printed ribbon keyboard."
    }
  ],
  "current_state": null,
  "properties": {
    "orientation": "discrete choice",
    "possible_values": ["WIDE", "NARROW", "KEY"],
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "synthesizer section, VCO area",
    "layout_source": "manual panel overview for the Synthesizer section"
  },
  "source": [
    "monotribe Owner's Manual, Synthesizer section, RANGE select switch",
    "monotribe manual visual index, page 10 panel overview"
  ]
}

Use role: "switch" because the control selects one of three discrete modes. Do not expose valuenow or valuetext as a current value unless there is situated evidence of the actual switch position. The manual defines the three possible settings and their meanings, but static sources alone cannot determine which one is currently selected.

[Trace]
Sources used: monotribe Owner’s Manual p.10–11; monotribe_manual_visual_index.json entry for p.10; 01_surface_aria_store.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 25%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: Manual explicitly names the RANGE select switch and defines WIDE, NARROW, and KEY; ARIA mapping for discrete selectors is direct.
Unsupported-current-state risk: Low.
[/Trace]