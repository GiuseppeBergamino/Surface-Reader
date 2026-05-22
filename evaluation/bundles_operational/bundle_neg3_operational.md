Prompt ID: neg3

Prompt: Which control should I use for tap tempo? Describe where it is and what it does.

# Surface Reader:
## R1:
The monotribe does not appear to have a dedicated tap-tempo control in the manual. For tempo, use the TEMPO knob. The manual says the TEMPO knob sets the speed of the sequencer, with a range set in the Global menu: 60–180 BPM in NARROW, or 10–600 BPM in WIDE. It is disabled when SYNC IN is connected.

From the performer’s perspective, the TEMPO knob is in the sequencer section, toward the upper-right area of the panel, near the transport and recording controls. Use the lower row of step buttons as a landmark, then move upward into the sequencer control cluster; the TEMPO knob is a round rotary knob, separate from the small rectangular buttons.

What it does: turn it to change the sequencer speed. Faster tempo makes the synth and drum sequence run faster; slower tempo makes it run slower.

[Trace]
Sources used: monotribe_manual.pdf, manual page 13–14 content; monotribe_manual_visual_index.json page 13 sequencer layout entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The TEMPO knob function is explicit in the manual, but the absence of tap tempo is based on no documented tap-tempo control being present in the provided manual content.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
The monotribe does not document a tap-tempo button. For tempo, use the TEMPO knob. The manual says it “sets the speed of the sequencer,” with a Global menu option for narrow or wide tempo range. It is disabled when SYNC IN is connected.

From the performer’s perspective, the TEMPO knob is in the Sequencer section, the control area associated with Play, Rec, Flux, Gate Time, part buttons, and step buttons. The manual’s sequencer panel diagram identifies it as control 5.

Tactilely: find the sequencer area on the right/lower part of the top panel. The TEMPO control is a round rotary knob, separate from the rows of small step buttons. Turn it clockwise for a faster sequence and counterclockwise for a slower one. Static sources cannot tell me its current position.

[Trace]
Sources used: monotribe_manual.pdf, sequencer panel overview entry in monotribe_manual_visual_index.json, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 05_surface_model_map_schema.md, 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual documents TEMPO as the sequencer speed control, and no tap-tempo control is documented in the available source.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the TEMPO knob. The manual does not document a tap-tempo button or tap-tempo procedure; it says the TEMPO knob sets the speed of the sequencer. In the Global menu, its range can be NARROW, 60–180 BPM, or WIDE, 10–600 BPM. The TEMPO knob is disabled when SYNC IN is connected.

From the performer’s perspective, it is in the sequencer section, in the upper-right half of the panel. Use the row of eight step buttons as a landmark near the lower part of the sequencer area, then move upward toward the small sequencer control cluster. The TEMPO control is a rotary knob, not a button: turn it left for slower sequencer playback, right for faster playback.

So for “tap tempo,” the supported monotribe action is: adjust tempo manually with the TEMPO knob, or use SYNC IN from another clock source. There is no manual-grounded tap control.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section / TEMPO knob; monotribe_manual_visual_index.json, page 13 sequencer panel overview; foto_pannello static panel photo; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 50%; Visual/static layout 25%; Surface ARIA Store 5%; Surface Model/Map Schema 5%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The TEMPO function is clearly documented, but exact tactile placement is derived from static layout references rather than live evidence.
Unsupported-current-state risk: Low.
[/Trace]


# Baseline:
## R1:
Use the TEMPO knob. The manual does not document a tap-tempo control or tap-tempo procedure for the monotribe.

Where it is: in the sequencer section, it is control number 5 in the panel diagram. It sits in the basic sequencer controls area, near the PLAY button and other sequence controls.

What it does: the TEMPO knob sets the speed of the sequencer. Its range can be changed in the Global menu: NARROW gives 60–180 BPM for detailed adjustment, and WIDE gives 10–600 BPM. The manual also says the TEMPO knob is disabled if the SYNC IN jack is connected.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section, “Basic controls,” TEMPO knob; panel description diagram; static panel photo for layout only.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the TEMPO knob and describes its function, but does not document tap tempo.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the TEMPO knob. The manual does not document a tap-tempo button or tap-tempo procedure for the monotribe.

It is in the Sequencer section, identified as control 5 in the manual’s sequencer panel diagram. It sits among the basic sequencer controls near the PLAY button and the part/step controls.

What it does: the TEMPO knob sets the speed of the sequencer. Its range can be changed in the Global menu: NARROW gives finer adjustment from 60–180 BPM, and WIDE gives 10–600 BPM. The manual also says the TEMPO knob is disabled when something is connected to SYNC IN.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section pp. 13–14; Global menu p. 16.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual directly identifies the TEMPO knob and describes its function and limits.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The monotribe manual does not document a tap-tempo control. For tempo, use the TEMPO knob instead.

It is in the Sequencer section, among the basic sequencer controls, near the PLAY, ACTIVE STEP, PART, and step-button area.

The TEMPO knob “sets the speed of the sequencer.” Its range can be changed in the Global menu: NARROW gives detailed adjustment from 60–180 BPM, and WIDE gives 10–600 BPM. The manual also says the TEMPO knob is disabled if the SYNC IN jack is connected.

[Trace]
Sources used: monotribe manual, Sequencer section, Basic controls, TEMPO knob; panel description diagram.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents TEMPO knob behavior and does not document tap tempo.
Unsupported-current-state risk: None.
[/Trace]


