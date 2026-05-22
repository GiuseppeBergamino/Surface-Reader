Prompt: Represent the oscillator waveform control as a Surface ARIA node. 

Response: 

I’ll ground the node in the manual’s official control name and possible waveform positions, then map it to the Surface ARIA switch role because it has discrete positions.

Ragionato per 5s

The oscillator waveform control should be represented as a Surface ARIA switch, not a slider, because it selects one of three discrete VCO waveform positions. The manual’s official name is WAVE select switch, and its documented values are sawtooth, triangle, and square. Surface ARIA defines waveform selectors as switch controls and allows possible_values and position_count, while current_state or valuetext require situated evidence.

{
  "node_id": "monotribe.synth.vco.wave",
  "role": "switch",
  "name": "WAVE select switch",
  "description": "Selects the VCO waveform used as the basis of the synth sound.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synth.vco",
  "children": [],
  "physical_type": "switch",
  "actions": [
    "select sawtooth wave",
    "select triangle wave",
    "select square wave"
  ],
  "possible_states": [
    {
      "name": "sawtooth",
      "label": "Sawtooth wave"
    },
    {
      "name": "triangle",
      "label": "Triangle wave"
    },
    {
      "name": "square",
      "label": "Square wave"
    }
  ],
  "properties": {
    "possible_values": [
      "sawtooth",
      "triangle",
      "square"
    ],
    "position_count": 3
  },
  "current_state": null,
  "spatial_properties": {
    "region": "upper-left synthesizer section",
    "group": "VCO controls",
    "ordering": "control 2 in the manual’s synthesizer section panel diagram",
    "neighbours": {
      "left_or_nearby": "OCTAVE selector",
      "below_or_nearby": "NOISE knob and RANGE select switch"
    }
  },
  "source": [
    "monotribe_manual.pdf, English manual, Panel description and functions, Synthesizer section, VCO",
    "Surface ARIA Store, switch role rules"
  ],
  "notes": [
    "Do not expose valuenow or valuetext unless the current physical switch position is available from situated evidence.",
    "The manual defines the possible waveform positions, but static sources alone do not reveal which waveform is currently selected."
  ]
}

[Trace]
Sources used: monotribe_manual.pdf p.10–11 / manual page uncertain via search result; 01_surface_aria_store.md switch-role rules; 05_surface_model_map_schema.md surface node-field rules.
Routing weights: Device manual 45%; Surface ARIA Store 35%; Surface Model/Map Schema 20%.
Evidence confidence: High.
Confidence rationale: The manual names the control and values, and the Surface ARIA Store directly classifies waveform selectors as switches.
Unsupported-current-state risk: Low.
[/Trace]