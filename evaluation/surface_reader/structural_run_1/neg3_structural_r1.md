Prompt: Create a structured description of the tap-tempo button.

Response: 

Tap-tempo button — structured surface description
{
  "node_id": "sequencer_tap_tempo_button",
  "name": "Tap Tempo button",
  "role": "button",
  "physical_type": "pressable button",
  "region": "Sequencer section",
  "group": "Tempo / transport-related controls",
  "function": "Likely used to set or adjust sequencer tempo by repeated pressing, but this exact Tap Tempo function is not documented in the available owner’s-manual text.",
  "related_control": {
    "name": "TEMPO knob",
    "role": "slider",
    "physical_type": "rotary knob",
    "manual_function": "Sets the speed of the sequencer."
  },
  "static_layout": {
    "approximate_position": "sequencer area, near the TEMPO control",
    "tactile_landmark": "Use the sequencer control cluster and the TEMPO knob as the main landmark.",
    "navigation_hint": "From the sequencer section, find the TEMPO knob first; the Tap Tempo button is treated as a nearby small pressable control."
  },
  "actions": [
    "press",
    "press repeatedly"
  ],
  "possible_states": [
    "pressed",
    "not pressed"
  ],
  "current_state": "requires situated evidence; cannot be inferred from the manual, diagram, or static panel photo",
  "uncertainty": "The available manual text documents the TEMPO knob, not an official Tap Tempo button entry. The structured node is therefore based on static panel identification plus semantic modeling, with function marked as uncertain."
}

The owner’s manual clearly documents the TEMPO knob as the control that “sets the speed of the sequencer,” with global settings for narrow or wide tempo range, and notes that the TEMPO knob is disabled when SYNC IN is connected . It does not clearly document a separate Tap Tempo button in the available English panel-function text, so I would not treat the tap-tempo behavior as manual-confirmed.

Non-visually: treat it as a small button near the tempo area, not as a knob. Use the TEMPO knob as your tactile anchor, then search immediately around that local tempo/transport cluster for a pressable control. Do not rely on any LED or printed label to confirm its state.

[Trace]
Sources used: monotribe_manual.pdf pp. 13–14 text via search results; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 35%; Visual/static layout 25%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: Medium.
Confidence rationale: The tempo area is manual-grounded, but the separate Tap Tempo button is not clearly documented in the available manual text.
Unsupported-current-state risk: Low.
[/Trace]