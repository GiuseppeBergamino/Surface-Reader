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
    "select octave position",
    "rotate to another discrete octave setting"
  ],
  "possible_states": [
    {
      "name": "64'",
      "description": "With the 64' setting, the ribbon keyboard pitch range is A0–D2."
    },
    {
      "name": "other octave positions",
      "description": "Other documented panel positions specify VCO pitch in octave steps."
    }
  ],
  "current_state": null,
  "properties": {
    "possible_values": [
      "64'",
      "32'",
      "16'",
      "8'",
      "4'",
      "2'"
    ],
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "upper-left area of the synthesizer section",
    "group_position": "first numbered VCO control in the manual's synthesizer-section panel diagram",
    "neighbours": [
      "WAVE select switch to the right",
      "NOISE knob below/right in the VCO group",
      "RANGE select switch lower in the keyboard-related VCO area"
    ],
    "tactile_description": "A discrete selector in the VCO group; use it as the octave-setting control, not as a continuous knob."
  },
  "source": [
    "monotribe_manual.pdf, English section, panel description: Synthesizer section, VCO, OCTAVE selector :contentReference[oaicite:0]{index=0}",
    "monotribe_manual_visual_index.json, page 10 panel overview for synthesizer-section layout :contentReference[oaicite:1]{index=1}",
    "01_surface_aria_store.md: discrete-position selectors map to role switch; current state must not be inferred from static sources :contentReference[oaicite:2]{index=2}",
    "05_surface_model_map_schema.md: node fields and surface-map fields :contentReference[oaicite:3]{index=3}"
  ]
}

I used role: "switch" because the OCTAVE selector has discrete octave positions, rather than a continuous value. I left current_state, valuenow, and valuetext as null because static sources can define possible positions but cannot tell which octave is currently selected.

[Trace]
Sources used: monotribe_manual.pdf English VCO/OCTAVE selector text; monotribe_manual_visual_index.json page 10 synthesizer-section layout entry; 01_surface_aria_store.md role rules; 05_surface_model_map_schema.md node/map fields.
Routing weights: Device manual 35%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 15%.
Evidence confidence: Medium.
Confidence rationale: Function and semantic role are well grounded; exact physical type depends on static visual interpretation of the panel control.
Unsupported-current-state risk: Low.
[/Trace]