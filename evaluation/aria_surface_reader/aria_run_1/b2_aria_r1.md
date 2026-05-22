Prompt: Represent the rec button as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.synth_sequence.rec_button",
  "role": "button",
  "name": "REC button",
  "description": "Press during playback to enter record mode for the SYNTH part. Press while stopped to enter record-ready mode. Press again to exit record or record-ready mode.",
  "region": "Sequencer section",
  "group": "Synthesizer sequence controls",
  "parent": "monotribe.sequencer.synth_sequence",
  "children": [
    "monotribe.sequencer.synth_sequence.rec_led"
  ],
  "physical_type": "button",
  "actions": [
    "press",
    "press again",
    "hold"
  ],
  "possible_states": [
    {
      "state": "record_mode",
      "indicator": "REC LED lit",
      "meaning": "Performance data from the ribbon keyboard is recorded during playback."
    },
    {
      "state": "record_ready_mode",
      "indicator": "REC LED blinking",
      "meaning": "Pressing PLAY will start playback and activate record mode."
    },
    {
      "state": "inactive",
      "indicator": "REC LED dark",
      "meaning": "Not in record mode or record-ready mode."
    },
    {
      "state": "save_sequence_hold",
      "condition": "Sequencer stopped and monotribe not producing sound",
      "meaning": "Holding REC until the REC LED stops blinking and goes dark saves the sequence."
    }
  ],
  "current_state": null,
  "properties": {
    "has_popup": false,
    "pressed": null,
    "active": null,
    "selected": null
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, upper-right area of the sequencer controls",
    "neighbours": [
      "FLUX button",
      "GATE TIME button",
      "PLAY button",
      "STEP LEDs"
    ],
    "layout_source": "manual sequencer-section panel diagram"
  },
  "safety_notes": [
    "Never turn off the power while data is being saved, because doing so may destroy the internal data."
  ],
  "source": [
    "monotribe Owner's manual: Sequencer section, REC button description",
    "monotribe Owner's manual: Saving a sequence",
    "Surface ARIA Store: button role rules"
  ]
}

A button role is appropriate because the REC control is a pressable control used to enter, exit, and prepare recording modes. The manual says pressing REC during playback puts the monotribe in record mode and lights the REC LED; pressing it while stopped puts the unit in record-ready mode and blinks the REC LED; pressing it again makes the REC LED go dark. It also says holding REC while stopped and silent saves the sequence.

Do not expose pressed, active, or a current LED state unless there is live evidence. From static sources, this node can only list documented possible states, not the current state. The Surface ARIA Store says a button may have documented possible states, but current-state properties require situated evidence.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The REC button function and LED meanings are explicitly documented, and the semantic role follows the Surface ARIA button rules.
Unsupported-current-state risk: Low.
[/Trace]