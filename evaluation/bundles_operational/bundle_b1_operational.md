Prompt ID: b1

Prompt: Which control should I use to start playback? Describe where it is and how to use it.

# Surface Reader:
## R1:
Use the PLAY button. The manual says: “Press this button to play or stop the sequence. Playback always starts from the beginning of the sequence. The PLAY LED will be lit during playback.”

From the performer’s perspective, it is in the Sequencer section, the control area for steps and transport. Find the row/cluster of small sequencer buttons rather than the synth knobs. The PLAY button is a pressable button, part of the transport controls, near the REC button.

How to use it:

Press PLAY once to start the sequence.
Press PLAY again to stop it.
Playback starts from step 1 each time.

I cannot tell whether it is currently playing from the manual or static panel references alone; the manual only defines that the PLAY LED is lit during playback.

[Trace]
Sources used: monotribe_manual.pdf, manual sequencer section/page 13–14 content; monotribe_manual_visual_index.json entry for page 13; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%, Visual/static layout 20%, Surface ARIA Store 10%, Surface Model/Map Schema 10%, Interaction Guidance Store 10%, Mode Policy Store 3%, Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Function is directly manual-grounded; tactile location is based on static sequencer layout rather than live panel evidence.
Unsupported-current-state risk: Low.
[/Trace]

## R2
Use the PLAY button.

From the performer’s perspective, it is in the sequencer section, in the lower/right half of the top panel. It is a pressable transport button. The manual says: “Press this button to play or stop the sequence. Playback always starts from the beginning of the sequence. The PLAY LED will be lit during playback.”

To find it non-visually:

Start from the row of eight step buttons near the lower part of the panel. Move upward into the sequencer control cluster. The PLAY button is the main transport button in that cluster, near the REC button and the TEMPO knob. Press it once to start the sequence. Press it again to stop playback.

I cannot tell whether it is currently playing from the manual or static panel references alone; that would require current LED, sound, or device-state evidence.

[Trace]
Sources used: monotribe_manual.pdf p.13–14; monotribe_manual_visual_index.json entry “Panel overview (Sequencer section)”; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies the PLAY button and its play/stop function, and static layout sources support its sequencer-section placement.
Unsupported-current-state risk: Low.
[/Trace]

## R3
Use the PLAY button. It starts or stops the sequence; the manual says playback always starts from the beginning, and the PLAY LED is lit during playback.

From the performer’s perspective, the PLAY button is in the sequencer section, in the lower/control area of the panel rather than the synth knob area. On the sequencer layout, it is the transport button identified as PLAY, near the other sequence controls such as REC, FLUX, GATE TIME, and the step buttons.

To use it:

Find the sequencer control area.
Press PLAY once to start the sequence.
Press PLAY again to stop it.

I cannot confirm whether playback is currently running from the manual or static panel references alone; the manual only defines the possible PLAY LED meaning.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section pages 13–15; monotribe_manual_visual_index.json entry for page 13; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies PLAY as the start/stop control, and the sequencer layout supports its region and grouping.
Unsupported-current-state risk: Low.
[/Trace]


# Baseline:
## R1:
Use the PLAY button to start playback. Press it once to play the sequence; press it again to stop. Playback always starts from the beginning of the sequence, and the PLAY LED is lit during playback.

It is in the sequencer section, in the group of basic controls. In the manual’s sequencer diagram, it is control number 4, near the ACTIVE STEP button and the TEMPO knob.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section / Basic controls, PLAY button; static panel photo for general layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies the PLAY button and says it plays or stops the sequence.
Unsupported-current-state risk: None.
[/Trace]

## R2
Use the PLAY button to start playback. Press it once to play the sequence; press it again to stop. Playback always starts from the beginning of the sequence, and the PLAY LED is lit during playback.

Where it is: in the sequencer section, it is control number 4 in the manual’s sequencer panel diagram. On the panel, it is in the transport/basic controls area, near the other sequencer controls such as ACTIVE STEP, TEMPO, REC, FLUX, and GATE TIME.

How to use it:

Make sure the monotribe is powered on.
Press PLAY to start the sequence.
Press PLAY again to stop it.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section, Basic controls, PLAY button, manual pages 13–14.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual directly states that the PLAY button plays or stops the sequence.
Unsupported-current-state risk: None.
[/Trace]

## R3
Use the PLAY button.

It is in the sequencer section, in the lower half of the top panel. In the manual’s sequencer diagram, it is control number 4, near the other transport and sequence controls. On the physical panel, look in the sequencer control area around the row of small buttons and step controls.

Press PLAY once to start the sequence from the beginning. Press PLAY again to stop it. The manual says the PLAY LED is lit during playback.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section, Basic controls, PLAY button; static panel photo for general layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies the PLAY button and states that it starts/stops sequence playback.
Unsupported-current-state risk: Low.
[/Trace]
