Prompt: Represent the step buttons as a Surface ARIA node. 

Response: 

{
  "node_id": "monotribe.step_buttons",
  "role": "group",
  "name": "STEP buttons",
  "description": "Eight pressable buttons used by the sequencer to turn steps on or off. For the selected drum part, they turn each rhythm step on or off. In the Global menu, step buttons 1–7 also select global settings.",
  "region": "sequencer section",
  "group": "step-sequencer controls",
  "parent": "monotribe.sequencer_section",
  "children": [
    "monotribe.step_button_1",
    "monotribe.step_button_2",
    "monotribe.step_button_3",
    "monotribe.step_button_4",
    "monotribe.step_button_5",
    "monotribe.step_button_6",
    "monotribe.step_button_7",
    "monotribe.step_button_8"
  ],
  "physical_type": "row of eight buttons",
  "actions": [
    "press",
    "hold with another control",
    "press while holding ACTIVE STEP",
    "press while holding a PART button"
  ],
  "possible_states": [
    {
      "name": "on",
      "meaning": "The step will be played and its step LED will light up."
    },
    {
      "name": "off",
      "meaning": "The step will not be played and its step LED will not light up."
    },
    {
      "name": "active-step enabled",
      "meaning": "When used with ACTIVE STEP, the step is enabled and included in playback/recording."
    },
    {
      "name": "active-step disabled",
      "meaning": "When used with ACTIVE STEP, the step is skipped during playback and recording."
    }
  ],
  "current_state": null,
  "properties": {
    "setsize": 8,
    "orientation": "horizontal",
    "valuenow": null,
    "supports_selected": "current-state evidence required",
    "supports_pressed": "current-state evidence required",
    "supports_active": "current-state evidence required"
  },
  "spatial_properties": {
    "approximate_position": "lower area of the sequencer section",
    "ordering": "left to right, step 1 through step 8",
    "landmarks": [
      "sequencer section",
      "row of repeated step buttons",
      "near STEP LEDs"
    ],
    "tactile_description": "A repeated horizontal row of eight pressable controls. Count from the performer’s left for step numbers 1 through 8."
  },
  "source": [
    "monotribe_manual.pdf: sequencer section, STEP buttons and STEP LEDs",
    "monotribe_manual_visual_index.json: page 13 sequencer panel overview; page 14 step/part concept; page 15 sequencer behavior diagrams",
    "Surface ARIA Store: button and group role rules",
    "Surface Model and Map Schema: surface model/map node fields"
  ],
  "notes": [
    "Do not expose `valuenow` for these buttons.",
    "Do not claim which steps are currently on, off, pressed, selected, or active without situated evidence.",
    "The associated STEP LEDs should be represented separately as indicator nodes, not as the buttons’ current state unless observed."
  ]
}

A single child button can be represented like this:

{
  "node_id": "monotribe.step_button_1",
  "role": "button",
  "name": "STEP button 1",
  "description": "Pressable sequencer step button for step 1.",
  "region": "sequencer section",
  "group": "STEP buttons",
  "parent": "monotribe.step_buttons",
  "physical_type": "button",
  "actions": [
    "press",
    "press while holding ACTIVE STEP",
    "press while holding a PART button"
  ],
  "possible_states": [
    "on",
    "off",
    "enabled in active-step mode",
    "disabled in active-step mode"
  ],
  "current_state": null,
  "properties": {
    "posinset": 1,
    "setsize": 8,
    "pressed": null,
    "selected": null,
    "active": null
  },
  "spatial_properties": {
    "ordering": "first of eight from the performer’s left",
    "neighbours": {
      "right": "monotribe.step_button_2"
    }
  }
}

The manual identifies the monotribe sequencer as an eight-step sequencer and describes the STEP buttons as turning each step on or off, with step LEDs indicating on/off and current-step behavior . Semantically, each step button is a button, while the full row is best modeled as a group containing eight ordered button nodes .

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 01_surface_aria_store.md, 05_surface_model_map_schema.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 35%; Visual/static layout 20%; Surface ARIA Store 25%; Surface Model/Map Schema 15%; Interaction Guidance Store 3%; Mode Policy Store 1%; Routing/Uncertainty Policy 1%.
Evidence confidence: High.
Confidence rationale: Manual text defines the STEP button functions, and the ARIA/model stores directly define button/group node structure and current-state limits.
Unsupported-current-state risk: Low.
[/Trace]