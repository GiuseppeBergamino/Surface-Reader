Prompt: Represent the step buttons as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.step_buttons",
  "role": "group",
  "name": "STEP buttons",
  "description": "Eight pressable sequencer controls used to turn steps on or off. For drum parts, they turn each step of the selected drum part on or off.",
  "region": "Sequencer section",
  "group": "Step sequencer controls",
  "parent": "monotribe.sequencer",
  "children": [
    {
      "node_id": "monotribe.sequencer.step_button_1",
      "role": "button",
      "name": "STEP button 1",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null,
      "properties": {
        "valuenow": null,
        "note": "Do not expose valuenow for a button. Current on/off state requires situated evidence."
      }
    },
    {
      "node_id": "monotribe.sequencer.step_button_2",
      "role": "button",
      "name": "STEP button 2",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_3",
      "role": "button",
      "name": "STEP button 3",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_4",
      "role": "button",
      "name": "STEP button 4",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_5",
      "role": "button",
      "name": "STEP button 5",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_6",
      "role": "button",
      "name": "STEP button 6",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_7",
      "role": "button",
      "name": "STEP button 7",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    },
    {
      "node_id": "monotribe.sequencer.step_button_8",
      "role": "button",
      "name": "STEP button 8",
      "physical_type": "step button",
      "actions": ["press", "hold with another control where documented"],
      "possible_states": ["on", "off"],
      "current_state": null
    }
  ],
  "actions": [
    "press a step button to turn that step on or off",
    "hold ACTIVE STEP and press a step button to enable or disable that step for playback",
    "for drum parts, press a step button to turn that step of the selected drum part on or off",
    "hold a part button and press a step button to place the drum sound halfway through the step"
  ],
  "possible_states": {
    "step_button_on": "The step will be played and its step LED will light up.",
    "step_button_off": "The step will not be played and its step LED will not light up.",
    "active_step_enabled": "The enabled step is included during playback and recording.",
    "active_step_disabled": "The disabled step is skipped during playback and recording."
  },
  "current_state": null,
  "spatial_properties": {
    "approximate_position": "sequencer section, lower/right performance area",
    "arrangement": "repeated row of eight step buttons",
    "associated_indicators": "STEP LEDs correspond to the step buttons",
    "navigation_hint": "Use the row of eight repeated step controls as a tactile landmark for the sequencer."
  },
  "source": [
    "monotribe_manual.pdf: Sequencer section, STEP LEDs and STEP buttons",
    "monotribe_manual_visual_index.json: page 13 sequencer section layout; page 14 step/part concept; page 15 sequencer behavior diagrams",
    "Surface ARIA Store: step keys/buttons represented with role button; buttons do not expose valuenow"
  ]
}

The manual defines the STEP buttons as controls that turn each step on or off, with the corresponding STEP LEDs indicating lit/unlit states and blinking for the current step during playback. It also documents their use with ACTIVE STEP and with drum part buttons. The visual index identifies the sequencer-section layout and step-button diagrams as the relevant static layout sources. The Surface ARIA Store supports representing step keys as button nodes, with documented possible states but no valuenow or current state from static sources alone.

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 01_surface_aria_store.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents STEP buttons and their possible states, and the ARIA store explicitly maps step buttons to button.
Unsupported-current-state risk: Low.
[/Trace]