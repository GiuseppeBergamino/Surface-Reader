Prompt: Represent the delay time as a Surface ARIA node. 

Response: 

I’ll model it semantically first, then flag what is and is not grounded for the monotribe specifically.

Ragionato per 9s

A Delay Time control should be represented as a slider when it controls a continuous or quasi-continuous time value. Surface ARIA uses slider for rotary knobs, faders, encoders, or touch controls that adjust continuous values, and valuenow is only valid with current situated evidence.

{
  "node_id": "effect_delay_time",
  "role": "slider",
  "name": "Delay Time",
  "description": "Adjusts the time interval between the original sound and the delayed repeat.",
  "region": "Effects section",
  "group": "Delay",
  "parent": "effect_delay_group",
  "physical_type": "unknown control type",
  "actions": [
    "increase delay time",
    "decrease delay time"
  ],
  "properties": {
    "valuemin": "requires documented range",
    "valuemax": "requires documented range",
    "step_size": "requires documented range",
    "valuenow": "requires situated evidence",
    "valuetext": "requires situated evidence or documented named values"
  },
  "possible_states": "continuous or quasi-continuous time value, if documented",
  "current_state": "requires situated evidence",
  "spatial_properties": {
    "region": "unknown",
    "group": "Delay",
    "navigation_hint": "requires static layout evidence"
  },
  "source": [
    "Surface ARIA Store: slider role and valid properties"
  ]
}

For the Korg monotribe specifically, I would not add this as a grounded monotribe node unless another source documents a delay control. The monotribe manual’s documented sound structure describes VCO, VCF, VCA, LFO, EG, drums, sequencer, sync, and audio I/O, but not a delay-time parameter.

[Trace]
Sources used: 01_surface_aria_store.md; 05_surface_model_map_schema.md; monotribe_manual.pdf, manual page uncertain.
Routing weights: Device manual 20%; Surface ARIA Store 50%; Surface Model/Map Schema 20%; Routing/Uncertainty Policy 10%.
Evidence confidence: Medium.
Confidence rationale: The ARIA role mapping is well grounded, but delay time is not grounded as a monotribe control in the available manual evidence.
Unsupported-current-state risk: Low.
[/Trace]