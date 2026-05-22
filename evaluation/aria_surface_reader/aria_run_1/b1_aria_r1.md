Prompt: Represent the play button as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.transport.play",
  "role": "button",
  "name": "PLAY button",
  "description": "Plays or stops the sequence. Playback always starts from the beginning of the sequence.",
  "region": "sequencer section",
  "group": "basic controls / transport controls",
  "parent": "monotribe.sequencer",
  "physical_type": "button",
  "actions": [
    "press"
  ],
  "possible_states": [
    {
      "name": "playback active",
      "indicator": "PLAY LED lit",
      "meaning": "The sequence is playing"
    },
    {
      "name": "playback stopped",
      "indicator": "PLAY LED not lit",
      "meaning": "The sequence is stopped"
    }
  ],
  "current_state": null,
  "properties": {
    "pressed": null,
    "active": null
  },
  "spatial_properties": {
    "approximate_position": "sequencer section, transport/basic-controls area",
    "source_note": "Static layout comes from the sequencer section panel diagram; current LED state is not inferable from static sources."
  },
  "source": [
    "monotribe_manual.pdf: Sequencer section, Basic controls, PLAY button",
    "monotribe_manual_visual_index.json: page 13 sequencer section panel overview"
  ]
}

The important Surface ARIA choice is role: "button" because the PLAY control is a pressable transport control. The manual states that pressing the PLAY button plays or stops the sequence, that playback starts from the beginning, and that the PLAY LED is lit during playback. The visual index identifies the sequencer-section panel overview as the layout source for transport and related controls.

Do not set pressed, active, or any current LED state unless there is live situated evidence. Static sources only support possible states, not the current state.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; Surface ARIA Store; Surface Model/Map Schema; Routing and Uncertainty Policy.
Routing weights: Device manual 40%; Visual/static layout 15%; Surface ARIA Store 25%; Surface Model/Map Schema 15%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The PLAY button function and LED meaning are explicitly documented, and the ARIA role follows the store’s button rules.
Unsupported-current-state risk: Low.
[/Trace]