Prompt: Represent the tap tempo as a Surface ARIA node. 

Response: 

The monotribe manual does not document a Tap Tempo control. It documents a TEMPO knob that sets sequencer speed, with 60–180 BPM in narrow range and 10–600 BPM in wide range, and says the TEMPO knob is disabled when SYNC IN is connected.

So a Surface ARIA node for tap tempo should be marked as unsupported/not present in the documented monotribe surface, unless you are modeling an external or hypothetical control.

{
  "node_id": "sequencer_tap_tempo",
  "role": "button",
  "name": "Tap Tempo",
  "description": "Sets sequencer tempo by repeated presses. Not documented as a monotribe control in the available manual.",
  "region": "Sequencer section",
  "group": "Tempo controls",
  "parent": "sequencer_section",
  "physical_type": "button",
  "actions": [
    "press repeatedly to define tempo"
  ],
  "possible_states": {
    "supported_on_monotribe": false,
    "documented_alternative": "TEMPO knob"
  },
  "current_state": "requires situated evidence; no current state is available from static sources",
  "properties": {
    "pressed": "current-state only; requires situated evidence",
    "valuenow": "not valid for button role",
    "derived_tempo_bpm": "would be device/software-derived, not directly exposed by this button node unless documented"
  },
  "spatial_properties": {
    "documented_location": "not documented",
    "navigation_hint": "Use the documented TEMPO knob in the sequencer section instead."
  },
  "source": [
    "monotribe_manual.pdf, sequencer section: TEMPO knob",
    "Surface ARIA Store: button role rules",
    "Surface Model/Map Schema: node field structure"
  ]
}

For the actual monotribe control, the better grounded node is:

{
  "node_id": "sequencer_tempo_knob",
  "role": "slider",
  "name": "TEMPO knob",
  "description": "Sets the speed of the sequencer.",
  "region": "Sequencer section",
  "group": "Tempo controls",
  "parent": "sequencer_section",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase tempo",
    "turn counterclockwise to decrease tempo"
  ],
  "possible_states": {
    "range_narrow": "60–180 BPM",
    "range_wide": "10–600 BPM",
    "disabled_condition": "disabled if the SYNC IN jack is connected"
  },
  "current_state": "requires situated evidence",
  "properties": {
    "valuemin": "10 BPM if global TEMPO range is wide; 60 BPM if narrow",
    "valuemax": "600 BPM if global TEMPO range is wide; 180 BPM if narrow",
    "valuenow": "requires situated evidence"
  },
  "source": [
    "monotribe_manual.pdf, sequencer section: TEMPO knob",
    "monotribe_manual.pdf, global menu: TEMPO knob range"
  ]
}

[Trace]
Sources used: monotribe_manual.pdf p.14–16/manual page uncertain; Surface ARIA Store; Surface Model/Map Schema.
Routing weights: Device manual 55%; Surface ARIA Store 25%; Surface Model/Map Schema 20%.
Evidence confidence: High.
Confidence rationale: The manual documents TEMPO knob behavior but provides no Tap Tempo control.
Unsupported-current-state risk: Low.
[/Trace]