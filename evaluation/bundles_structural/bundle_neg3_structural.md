Prompt ID: neg3

Prompt: Create a structured description of the tap-tempo button.

# Surface Reader:
## R1:
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

## R2:
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

## R3:
The monotribe manual does not identify an official “tap-tempo button.” The documented tempo control is the TEMPO knob, which sets the speed of the sequencer. The manual says its range can be set in the Global menu: NARROW = 60–180 BPM and WIDE = 10–600 BPM. It also says the TEMPO knob is disabled when the SYNC IN jack is connected.

Structured description:

{
  "node_id": "sequencer_tempo",
  "official_name": "TEMPO knob",
  "requested_alias": "tap-tempo button",
  "alias_status": "not confirmed by the manual",
  "role": "slider",
  "physical_type": "rotary knob",
  "region": "Sequencer section",
  "group": "Basic controls",
  "description": "Sets the speed of the sequencer.",
  "possible_values": {
    "narrow_range": "60–180 BPM",
    "wide_range": "10–600 BPM"
  },
  "related_setting": "Global menu step button 7 sets the TEMPO knob range.",
  "disabled_condition": "Disabled if the SYNC IN jack is connected.",
  "current_state": "requires situated evidence",
  "non_visual_note": "Do not describe this as a tap button unless a separate live or visual source confirms a modified or alternate panel control."
}

Tactile mapping note: treat this as a rotary tempo control, not a pressable tap button, unless the physical unit has a modification or non-manual control. Use the sequencer section as the main landmark; the manual places TEMPO among the basic sequencer controls, alongside PLAY, ACTIVE STEP, and the part/step controls.

[Trace]
Sources used: monotribe_manual.pdf p.13–16 snippets; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Routing and Uncertainty Policy; Mode Policy Store.
Routing weights: Device manual 55%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: Medium.
Confidence rationale: The manual clearly documents TEMPO as a knob and does not surface “tap tempo,” but the static panel photo could not be independently cited here.
Unsupported-current-state risk: Low.
[/Trace]


# Baseline:
## R1:
Tap-tempo button

The monotribe manual does not document a tap-tempo button. The documented tempo control is the TEMPO knob, which sets the speed of the sequencer.

Where it is

The TEMPO knob is in the sequencer section, listed as basic control number 5 in the manual’s sequencer panel description.

What it does

The TEMPO knob sets sequencer speed. Its range can be changed in the Global menu:

NARROW: 60–180 BPM for finer adjustment.
WIDE: 10–600 BPM.

The manual also states that the TEMPO knob is disabled when the SYNC IN jack is connected.

Limitation

A dedicated tap-tempo button, tap-tempo procedure, or tap-tempo function is not documented in the provided manual or static panel source.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section, TEMPO knob and Global menu tempo range entries; static panel photo for layout context.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual documents a TEMPO knob but no tap-tempo button or tap-tempo procedure.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Direct answer: The monotribe manual does not document a tap-tempo button. The documented tempo control is the TEMPO knob, not a button.

Structured description

Name in manual: TEMPO knob.

Control type: Rotary knob, not a button.

Location: In the sequencer section. In the manual’s sequencer diagram it is item 5, among the basic sequencer controls.

Purpose: Sets the speed of the sequencer.

Range: The TEMPO knob range can be changed in the Global menu.
With NARROW, it adjusts 60–180 BPM. With WIDE, it adjusts 10–600 BPM. The manual says these tempo values treat each step as a 16th note.

Important limitation: If the SYNC IN jack is connected, the manual says the TEMPO knob is disabled.

Not documented: A tap-tempo function, tap-tempo button, or tempo-by-tapping procedure is not described in the uploaded manual.

[Trace]
Sources used: monotribe Owner’s manual, sequencer section, p. 13–14/15; Global menu, p. 16.
Routing weights: Device manual 95%; Visual/static layout 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents a TEMPO knob and does not document a tap-tempo button.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The manual does not document a tap-tempo button on the Korg monotribe.

Structured description:

Official documented control: TEMPO knob, not tap-tempo button.
Function: Sets the speed of the sequencer.
Range: The TEMPO knob range is set in the Global menu. In NARROW range it adjusts 60–180 BPM; in WIDE range it adjusts 10–600 BPM.
SYNC IN limitation: The TEMPO knob is disabled when the SYNC IN jack is connected.
Related global setting: Step button 7 in the Global menu selects the TEMPO knob range: LED unlit means narrow range; LED lit means wide range.
Location: In the sequencer section, control number 5 in the manual’s sequencer panel diagram, near the basic transport and sequence controls.

There is no documented procedure for tapping a button to set tempo. A tap-tempo function may exist in some other product or modification, but it is not in the uploaded monotribe manual.

[Trace]
Sources used: monotribe Owner’s manual, sequencer section pp. 13–16; Global menu p. 16; uploaded manual citation
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual documents a TEMPO knob and tempo range setting, but no tap-tempo button or tap-tempo procedure.
Unsupported-current-state risk: None.
[/Trace]


