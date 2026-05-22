Prompt: Which controls should I use to work with sequencer steps? Describe where they are and what they do.

Response: 

Use the Sequencer section: the cluster of buttons and one knob on the right side of the top panel, from the performer’s perspective. The manual says the monotribe has an eight-step sequencer for the synth and drum parts.

Main step controls

STEP buttons
These are the key controls for steps. They form the repeated step-button row in the sequencer area. Press a step button to turn that step on or off for the currently selected part. For drum parts, they turn steps on or off for BD, SN, or HH. For the synth part, they control whether the step plays. The matching STEP LEDs indicate possible step status and blink during playback to show the current step, but I cannot know their current state from static sources alone.

PART buttons: SYNTH, BD, SN, HH
Use these before editing steps. They select which part the step buttons will edit: synth, bass drum, snare drum, or hi-hat. Tactilely, treat them as the “which lane am I editing?” buttons near the sequencer controls. Their PART LEDs can indicate the selected part, but current selection cannot be inferred from the manual or static panel image.

ACTIVE STEP button
Use this to enable or disable steps in the sequence structure itself. Hold ACTIVE STEP, then press the desired STEP button. Disabled steps are skipped during playback and recording. This is different from simply turning a note or drum hit off; it changes whether the sequencer visits that step at all.

PLAY button
Starts or stops the sequence. Playback always starts from the beginning of the sequence. Use this when checking how your step changes sound in time.

REC button
Use this for recording the synth part. During playback, pressing REC enters record mode; playing the ribbon keyboard records your performance. While stopped, pressing REC puts the unit in record-ready mode.

GATE TIME button
For synth steps, hold GATE TIME while using the ribbon keyboard during playback to change note duration. Left side of the ribbon gives very short gate time; right side gives longer gate time. In record mode, gate time changes can be recorded per step.

FLUX button
Changes how the synth sequence is recorded and played back. With FLUX on, synth performance is recorded and played back as continuous data. With FLUX off, one note plays per step.

TEMPO knob
Sets the sequencer speed. It is a rotary knob in the sequencer area. The manual notes that it is disabled if SYNC IN is connected.

RHYTHM knob
Controls the volume of the drum sound generator. It does not choose steps, but it matters when working with BD/SN/HH step patterns.

A useful mental map: PART buttons choose the lane, STEP buttons choose the events, ACTIVE STEP changes the length/skip behavior, PLAY/REC control motion, and FLUX/GATE TIME shape the synth sequence.

[Trace]
Sources used: monotribe_manual.pdf English sequencer section, manual page uncertain; monotribe_manual_visual_index.json entries for pages 13–15; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 8%; Interaction Guidance Store 7%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: Control names and functions are directly documented; layout is supported by the sequencer panel diagram/index, though exact tactile spacing is approximate.
Unsupported-current-state risk: Low.
[/Trace]