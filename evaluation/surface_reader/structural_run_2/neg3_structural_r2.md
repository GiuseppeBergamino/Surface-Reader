Prompt: Create a structured description of the tap-tempo button.

Response: 

Structured description: tap-tempo button
{
  "node_id": "sequencer_tap_tempo_unconfirmed",
  "official_name": null,
  "requested_name": "tap-tempo button",
  "device": "Korg monotribe",
  "status": "not documented as a dedicated control in the available manual sources",
  "recommended_mapping": {
    "do_not_create_as": "confirmed button",
    "reason": "The monotribe manual documents a TEMPO knob for sequencer speed, not a tap-tempo button."
  },
  "nearest_documented_control": {
    "node_id": "sequencer_tempo",
    "official_name": "TEMPO knob",
    "role": "slider",
    "physical_type": "rotary knob",
    "region": "Sequencer section",
    "function": "Sets the speed of the sequencer.",
    "possible_values": {
      "NARROW_range": "60–180 BPM",
      "WIDE_range": "10–600 BPM"
    },
    "current_state": "requires situated evidence"
  },
  "static_layout": {
    "region": "Sequencer section",
    "manual_panel_callout": "5",
    "layout_confidence": "medium",
    "note": "The visual index identifies manual page 13 as the sequencer-section panel overview, including transport and sequencer controls."
  },
  "non_visual_guidance": {
    "guidance": "Use the sequencer section as the search region. The documented tempo control is a knob, not a press button. Do not rely on a printed 'tap tempo' label because the available monotribe manual does not document one."
  },
  "unsupported_current_state": [
    "current tempo value",
    "current knob position",
    "whether SYNC IN is connected",
    "whether any LED is lit or blinking"
  ]
}

The important correction is that I cannot confirm a “tap-tempo button” for the monotribe from the uploaded manual. The manual identifies TEMPO knob as the control that sets sequencer speed, and notes that it is disabled when SYNC IN is connected. The sequencer-panel diagram is indexed as the visual source for this control area.

[Trace]
Sources used: monotribe_manual.pdf p.14–16 / manual page uncertain citation chunk; monotribe_manual_visual_index.json entry for sequencer section page 13; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 10%.
Evidence confidence: Medium.
Confidence rationale: The manual strongly supports TEMPO knob behavior, but no dedicated tap-tempo button is documented in the retrieved sources.
Unsupported-current-state risk: Low.
[/Trace]
