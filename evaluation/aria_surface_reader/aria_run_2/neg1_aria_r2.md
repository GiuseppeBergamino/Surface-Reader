Prompt: Represent the delay time as a Surface ARIA node. 

Response: 

{
  "node_id": "effect.delay.time",
  "role": "slider",
  "name": "Delay Time",
  "description": "Controls the time interval before the delayed signal is heard.",
  "region": "effects section",
  "group": "delay effect",
  "parent": "effect.delay",
  "physical_type": "rotary knob",
  "actions": [
    "turn clockwise to increase delay time",
    "turn counterclockwise to decrease delay time"
  ],
  "properties": {
    "possible_values": "continuous range, device-specific",
    "valuemin": null,
    "valuemax": null,
    "valuenow": null,
    "valuetext": null
  },
  "spatial_properties": {
    "approximate_position": null,
    "neighbours": [],
    "landmarks": [],
    "navigation_hint": null
  },
  "current_state": null,
  "source": [
    "Surface ARIA Store: continuous rotary controls should use role `slider`; `valuenow` requires situated evidence",
    "Surface Model and Map Schema: node fields for semantic surface model representation"
  ],
  "notes": "This is a generic Surface ARIA representation. The monotribe manual sources available here do not document a dedicated Delay Time control, so this node should not be treated as a confirmed monotribe control."
}

For ARIA semantics, Delay Time is best represented as a slider because it is a continuous or quasi-continuous parameter. If the physical control is known to be a knob, its semantic role remains slider and its physical_type is rotary knob. Current values such as valuenow must stay empty unless there is live/situated evidence of the knob position.

[Trace]
Sources used: 01_surface_aria_store.md; 05_surface_model_map_schema.md; monotribe_manual.pdf.
Routing weights: Surface ARIA Store 55%; Surface Model/Map Schema 30%; Device manual 15%.
Evidence confidence: Medium.
Confidence rationale: The semantic role is well grounded, but Delay Time is not documented as a monotribe control in the provided manual excerpt.
Unsupported-current-state risk: Low.
[/Trace]