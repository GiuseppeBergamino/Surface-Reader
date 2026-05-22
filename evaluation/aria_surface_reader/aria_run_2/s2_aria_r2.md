Prompt: Represent the oscillator waveform control as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.vco.wave_select",
  "role": "switch",
  "name": "WAVE select switch",
  "description": "Selects the VCO waveform used as the basis of the synthesizer sound.",
  "region": "Synthesizer section",
  "group": "VCO",
  "parent": "monotribe.synthesizer.vco",
  "children": [],
  "physical_type": "multi-position switch",
  "actions": [
    "select sawtooth wave",
    "select triangle wave",
    "select square wave"
  ],
  "possible_states": [
    {
      "name": "sawtooth wave",
      "manual_symbol": "sawtooth wave"
    },
    {
      "name": "triangle wave",
      "manual_symbol": "triangle wave"
    },
    {
      "name": "square wave",
      "manual_symbol": "square wave"
    }
  ],
  "current_state": null,
  "properties": {
    "orientation": "discrete",
    "valuetext": "available only with situated evidence; do not infer from manual or static photo"
  },
  "spatial_properties": {
    "section": "Synthesizer section",
    "approximate_position": "upper-left area of the synthesizer section",
    "nearby_controls": [
      "OCTAVE selector",
      "NOISE knob",
      "RANGE select switch"
    ],
    "layout_source": "manual panel overview, page 10"
  },
  "source": [
    "monotribe_manual.pdf, English manual pages 10–11",
    "monotribe_manual_visual_index.json entry for page 10",
    "01_surface_aria_store.md"
  ]
}

The correct semantic role is switch, not slider, because the WAVE select switch has three discrete waveform positions rather than a continuous range. The manual identifies it as “WAVE select switch” and says it selects the VCO waveform: sawtooth, triangle, or square. The Surface ARIA Store defines waveform selectors and other multi-position selectors as switch nodes, with current state only allowed when there is situated evidence.

[Trace]
Sources used: monotribe_manual.pdf pages 10–11; monotribe_manual_visual_index.json page 10 entry; 01_surface_aria_store.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 5%.
Evidence confidence: High.
Confidence rationale: The manual names the control and values, while Surface ARIA directly supports the switch role for discrete waveform selectors.
Unsupported-current-state risk: Low.
[/Trace]