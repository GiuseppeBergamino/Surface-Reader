Prompt: Create a structured description of the tap-tempo button.

Response: 

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