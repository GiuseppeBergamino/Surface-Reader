Prompt: Represent the step buttons as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.sequencer.step_buttons",
  "role": "group",
  "name": "STEP buttons",
  "description": "Eight pressable step controls used by the sequencer. For the synth part, they turn each step on or off. For the selected drum part, they turn each drum step on or off.",
  "region": "sequencer section",
  "group": "step-sequencer controls",
  "parent": "monotribe.sequencer",
  "children": [
    "monotribe.sequencer.step_button_1",
    "monotribe.sequencer.step_button_2",
    "monotribe.sequencer.step_button_3",
    "monotribe.sequencer.step_button_4",
    "monotribe.sequencer.step_button_5",
    "monotribe.sequencer.step_button_6",
    "monotribe.sequencer.step_button_7",
    "monotribe.sequencer.step_button_8"
  ],
  "physical_type": "row of buttons",
  "actions": [
    "press",
    "hold with another control",
    "press while holding ACTIVE STEP",
    "press while holding a PART button"
  ],
  "possible_states": [
    {
      "state": "on",
      "meaning": "The step will be played and its step LED will light up."
    },
    {
      "state": "off",
      "meaning": "The step will not be played and its step LED will not light up."
    },
    {
      "state": "active-step-enabled",
      "meaning": "When ACTIVE STEP is held, enabled steps have lit LEDs and are included in playback and recording."
    },
    {
      "state": "active-step-disabled",
      "meaning": "When ACTIVE STEP is held, disabled steps are skipped during playback and recording."
    }
  ],
  "current_state": null,
  "properties": {
    "set_size": 8,
    "ordered": true,
    "valuenow": null,
    "current_pressed": null,
    "current_selected": null,
    "current_active": null
  },
  "spatial_properties": {
    "approximate_position": "lower area of the sequencer section",
    "arrangement": "left-to-right row of eight repeated step buttons",
    "ordering": "step 1 at the left, step 8 at the right",
    "associated_indicators": "STEP LEDs correspond to the step buttons",
    "tactile_landmarks": [
      "repeated row of eight buttons",
      "near the ribbon keyboard and sequencer controls"
    ],
    "navigation_hint": "From the performer’s perspective, find the sequencer section on the right side of the top panel, then locate the repeated row of eight small buttons. Count from left to right for steps 1 through 8."
  },
  "source": [
    "monotribe_manual.pdf: Sequencer section, STEP LEDs and STEP buttons",
    "monotribe_manual_visual_index.json: page 13 sequencer panel overview, page 14 basic controls, page 15 sequencer behavior",
    "Surface ARIA Store: button and group role definitions",
    "Surface Model and Map Schema: surface model node fields and surface map fields"
  ],
  "children_template": {
    "role": "button",
    "name_pattern": "STEP button {n}",
    "physical_type": "button",
    "actions": [
      "press",
      "press while holding ACTIVE STEP",
      "press while holding selected PART button"
    ],
    "allowed_current_state_properties": [
      "pressed",
      "selected",
      "active"
    ],
    "current_state_requires_situated_evidence": true,
    "not_allowed": [
      "valuenow"
    ]
  }
}

Compact child example:

{
  "node_id": "monotribe.sequencer.step_button_1",
  "role": "button",
  "name": "STEP button 1",
  "description": "Pressable control for step 1 of the sequence.",
  "parent": "monotribe.sequencer.step_buttons",
  "physical_type": "button",
  "actions": [
    "press",
    "press while holding ACTIVE STEP",
    "press while holding a PART button"
  ],
  "possible_states": [
    "on",
    "off",
    "enabled when used with ACTIVE STEP",
    "disabled when used with ACTIVE STEP"
  ],
  "current_state": null,
  "properties": {
    "posinset": 1,
    "setsize": 8
  },
  "spatial_properties": {
    "ordering": "first button in the left-to-right step-button row"
  }
}

Important constraint: do not expose pressed, selected, active, LED-lit state, or step on/off state as current values unless there is situated evidence. Static manual and panel references only support possible states and layout.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 20%; Surface ARIA Store 30%; Surface Model/Map Schema 15%.
Evidence confidence: High.
Confidence rationale: Manual text defines STEP button functions and possible states; ARIA/schema stores define role and valid properties.
Unsupported-current-state risk: Low.
[/Trace]