Prompt: Represent the tap tempo as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.tempo",
  "role": "slider",
  "name": "TEMPO knob",
  "description": "Sets the speed of the sequencer.",
  "region": "Sequencer section",
  "group": "Basic controls",
  "parent": "monotribe.sequencer",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase sequencer speed",
    "turn counterclockwise to decrease sequencer speed"
  ],
  "possible_states": {
    "tempo_range": [
      {
        "name": "NARROW",
        "value_range": "60–180 BPM",
        "condition": "Global menu Step button 7 LED unlit"
      },
      {
        "name": "WIDE",
        "value_range": "10–600 BPM",
        "condition": "Global menu Step button 7 LED lit",
        "factory_default": true
      }
    ],
    "disabled_condition": "The TEMPO knob is disabled if the SYNC IN jack is connected."
  },
  "current_state": null,
  "properties": {
    "possible_values": "10–600 BPM in WIDE range, or 60–180 BPM in NARROW range",
    "valuemin": null,
    "valuemax": null,
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, basic controls area",
    "source_note": "Static layout should be taken from the sequencer-section panel diagram or panel photo before giving precise tactile navigation."
  },
  "source": [
    "monotribe_manual.pdf: Sequencer section, Basic controls, TEMPO knob",
    "monotribe_manual.pdf: Global menu, Step button 7 TEMPO knob range",
    "monotribe_manual_visual_index.json: page 13 sequencer section panel overview; page 16 global menu"
  ],
  "notes": [
    "The monotribe manual names this control TEMPO knob, not Tap Tempo.",
    "Because it is a continuous rotary knob controlling a numeric range, Surface ARIA represents it as role `slider`, physical type `rotary knob`.",
    "Do not expose `valuenow` unless current situated evidence confirms the knob position or actual tempo."
  ]
}

A stricter Surface ARIA version would keep “tap tempo” out of the node name unless you have a separate, documented tap-tempo control. In the provided monotribe manual evidence, tempo is set by the TEMPO knob; the manual states that it sets sequencer speed, can use a NARROW range of 60–180 BPM or WIDE range of 10–600 BPM, and is disabled when SYNC IN is connected.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 10%; Surface ARIA Store 25%; Surface Model/Map Schema 15%; Routing/Uncertainty Policy 5%.
Evidence confidence: Medium.
Confidence rationale: The manual supports TEMPO knob semantics, but “tap tempo” itself is not documented in the provided evidence.
Unsupported-current-state risk: Low.
[/Trace]
