Prompt: Represent the tap tempo as a Surface ARIA node. 

Response: 

I’ll ground this as a semantic node, not a live state: the monotribe sources can define what Tap Tempo is, but not whether it is currently active or being pressed.

Ragionato per 20s

For a Tap Tempo control, the Surface ARIA role should be button, because it is a pressable control that triggers an action rather than a continuous value. A button should not expose valuenow; current pressed/active state would require situated evidence.

For the monotribe specifically, the available manual text documents a TEMPO knob that sets sequencer speed, not a clearly documented “Tap Tempo” button. The TEMPO knob range is 60–180 BPM in NARROW mode or 10–600 BPM in WIDE mode, and it is disabled when SYNC IN is connected. So this node is safe only as a provisional Tap Tempo affordance, not as an officially confirmed monotribe control.

{
  "node_id": "sequencer_tap_tempo",
  "role": "button",
  "name": "Tap Tempo",
  "description": "Pressable tempo-entry control for setting the sequencer tempo by tapping, if this control is confirmed on the device.",
  "region": "sequencer section",
  "group": "tempo controls",
  "parent": "sequencer_section",
  "physical_type": "button",
  "actions": [
    "press",
    "repeat press to enter tempo"
  ],
  "possible_states": [
    "available",
    "disabled when external sync overrides internal tempo, if documented for this control"
  ],
  "current_state": null,
  "properties": {
    "valuenow": null,
    "pressed": "requires situated evidence",
    "active": "requires situated evidence"
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, near tempo controls",
    "confidence": "low",
    "note": "The manual text confirms TEMPO knob behavior, but does not confirm a Tap Tempo button in the extracted text."
  },
  "source": [
    "Surface ARIA Store: button role and current-state rules",
    "monotribe manual: sequencer TEMPO knob behavior"
  ]
}

A stricter monotribe-only model would instead represent the documented tempo control like this:

{
  "node_id": "sequencer_tempo_knob",
  "role": "slider",
  "name": "TEMPO knob",
  "description": "Sets the speed of the sequencer.",
  "region": "sequencer section",
  "group": "tempo controls",
  "physical_type": "rotary knob",
  "possible_values": {
    "narrow_range": "60–180 BPM",
    "wide_range": "10–600 BPM"
  },
  "current_state": null,
  "properties": {
    "valuenow": "requires situated evidence"
  }
}

[Trace]
Sources used: monotribe_manual.pdf, 01_surface_aria_store.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Surface ARIA Store 40%; Surface Model/Map Schema 15%.
Evidence confidence: Medium.
Confidence rationale: Button semantics are well grounded, but “Tap Tempo” is not confirmed as an official monotribe control in the available manual text.
Unsupported-current-state risk: Low.
[/Trace]