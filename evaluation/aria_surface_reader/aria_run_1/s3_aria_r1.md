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
  "children": [],
  "physical_type": "rotary selector",
  "actions": [
    "rotate to another octave position",
    "select an octave setting"
  ],
  "possible_states": {
    "type": "discrete_positions",
    "meaning": "Each position selects a different VCO pitch octave step.",
    "documented_example": {
      "value": "64'",
      "effect": "The ribbon keyboard pitch range is A0-D2."
    }
  },
  "current_state": null,
  "properties": {
    "orientation": "rotary",
    "controls": "VCO pitch octave",
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left area of the synthesizer section",
    "group_position": "in the VCO group",
    "nearby_controls": [
      "WAVE select switch",
      "NOISE knob",
      "RANGE select switch"
    ],
    "navigation_hint": "From the performer’s perspective, start at the upper-left part of the panel. The OCTAVE selector is the leftmost main control in the VCO area, above the nearby VCO controls."
  },
  "source": [
    "monotribe_manual.pdf: Panel description and functions, Synthesizer section; VCO OCTAVE selector",
    "monotribe_manual_visual_index.json: page 10 panel overview for synthesizer layout",
    "foto_pannello.jpeg: static top-panel reference",
    "01_surface_aria_store.md: discrete-position selector mapped to role switch"
  ],
  "notes": [
    "Do not expose a current octave value from static sources alone.",
    "The manual establishes the official name and function; the static panel references support physical type and placement."
  ]
}

The key semantic choice is role: "switch" rather than slider, because the OCTAVE selector chooses among discrete octave positions rather than continuously sweeping pitch. The manual states that the OCTAVE selector specifies VCO pitch in octave steps, and gives 64' as a documented example setting for the ribbon keyboard range. The Surface ARIA rules map discrete rotary selectors to switch, with current-state properties such as valuenow excluded unless there is live evidence.

[Trace]
Sources used: monotribe_manual.pdf page 10/11 text and synthesizer panel diagram; monotribe_manual_visual_index.json page 10 entry; foto_pannello.jpeg static panel photo; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 40%; Visual/static layout 25%; Surface ARIA Store 25%; Surface Model/Map Schema 10%.
Evidence confidence: Medium.
Confidence rationale: Official name and function are manual-grounded; physical placement is from static layout references, but exact current selector position is unavailable.
Unsupported-current-state risk: Low.
[/Trace]