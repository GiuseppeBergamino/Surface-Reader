Prompt: Create a structured description of the delay time.

Respose: 

Delay time — structured description

I don’t find a documented Delay Time control or parameter for the Korg monotribe in the provided manual. The monotribe manual describes VCO, VCF, VCA, LFO, EG, sequencer, sync, and gate time, but not an onboard delay effect or delay-time parameter.

A safe structured entry would therefore be:

node_id: delay_time
name: Delay Time
status: not documented on this device
role: unsupported_parameter
device: Korg monotribe
description: >
  No official Delay Time control or setting is described in the monotribe manual.
  Static sources do not support treating this as a monotribe parameter.
possible_confusion:
  - Gate Time: documented sequencer control that changes the duration of synth-part notes.
  - LFO Rate: documented control that changes modulation speed.
  - External delay effect: possible in a broader setup, but not part of the monotribe surface described by the manual.
current_state: unavailable
current_state_reason: >
  Static sources cannot determine current settings, connected external effects,
  or any live delay-related state.
non_visual_guidance: >
  Do not search the monotribe panel for a Delay Time control. If you are hearing
  repeats, check external pedals, mixer effects, DAW effects, or other connected gear.

For comparison, the closest documented timing-related control is GATE TIME: while a sequence plays back, holding the GATE TIME button and touching the ribbon keyboard changes the synth note duration from a very short value at the far left to a full-length value at the far right.

[Trace]
Sources used: monotribe_manual.pdf; Routing and Uncertainty Policy; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 55%; Routing/Uncertainty Policy 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual text available here documents timing-related controls but no Delay Time parameter.
Unsupported-current-state risk: Low.
[/Trace]

