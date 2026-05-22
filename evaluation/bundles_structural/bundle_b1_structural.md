Prompt ID: b1

Prompt: Create a structured description of the play button.

# Surface Reader:
## R1:
Structured description: PLAY button
node_id: monotribe.sequencer.play_button
name: PLAY button
role: button
physical_type: pressable button
region: Sequencer section
group: Basic controls / transport controls
official_function: Press to play or stop the sequence.
actions:
  - press: starts sequence playback from the beginning
  - press_again: stops sequence playback
indicator:
  name: PLAY LED
  possible_state:
    - lit during playback
current_state: unknown from static sources
manual_grounding: The manual states that the PLAY button plays or stops the sequence, playback always starts from the beginning, and the PLAY LED is lit during playback. :contentReference[oaicite:0]{index=0}
surface_map:
  approximate_position: sequencer section, among the basic sequencer controls
  tactile_landmark: part of the sequencer control area, separate from the ribbon keyboard and synth knobs
  neighbouring_controls:
    - ACTIVE STEP button
    - TEMPO knob
    - REC button
non_visual_guidance: Find the sequencer section, then locate the small transport/control cluster rather than the long ribbon keyboard or the rotary synth knobs. The PLAY button is a pressable control used as the main start/stop control for the sequence.
state_limitation: Static sources can describe what the PLAY LED means, but cannot tell whether it is currently lit.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section/basic controls; monotribe_manual_visual_index.json, sequencer section layout entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The PLAY button function and LED meaning are explicitly documented in the manual, with layout supported by the sequencer panel diagram index.
Unsupported-current-state risk: Low.
[/Trace]


## R2
Structured description: PLAY button
node_id: monotribe.sequencer.play_button
name: PLAY button
role: button
physical_type: pressable button
region: Sequencer section
group: Basic controls / transport controls
official_function: Press to play or stop the sequence.
actions:
  - press: starts sequence playback
  - press_again: stops sequence playback
documented_behavior:
  - Playback always starts from the beginning of the sequence.
  - The PLAY LED is lit during playback.
possible_indicators:
  - PLAY LED lit: playback is active
current_state: unknown
current_state_note: Static sources cannot tell whether the PLAY LED is currently lit or whether playback is running.
surface_map:
  approximate_position: upper area of the Sequencer section
  nearby_controls:
    - ACTIVE STEP button
    - TEMPO knob
    - REC button
    - FLUX button
    - STEP buttons
  tactile_guidance: >
    From the performer’s perspective, work in the sequencer area rather than the synth-control area.
    The PLAY button belongs to the transport/basic-control cluster, near REC and the tempo control.
    Treat it as the main start/stop button for the eight-step sequencer.

The manual identifies the PLAY button as basic control number 4 in the sequencer section and says: “Press this button to play or stop the sequence. Playback always starts from the beginning of the sequence. The PLAY LED will be lit during playback.” The visual index points to the sequencer-section panel diagram on manual page 13, which is the layout source for this control’s region and neighbors.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section/basic controls; monotribe_manual_visual_index.json, page 13 sequencer panel overview; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 40%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 15%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The PLAY button name, function, LED meaning, and sequencer-region placement are directly supported by the manual and visual index.
Unsupported-current-state risk: Low.
[/Trace]


## R3
Structured description: PLAY button

Official name: PLAY button
Device: Korg monotribe
Region: Sequencer section
Group: Basic controls / transport controls
Semantic role: button
Physical type: Pressable button
Primary action: Press
Documented function: Pressing the PLAY button starts or stops the sequence. Playback always starts from the beginning of the sequence. The PLAY LED is lit during playback.

Surface model entry
node_id: sequencer.play_button
name: PLAY button
role: button
physical_type: button
region: Sequencer section
group: Basic controls / transport
description: Starts or stops sequence playback.
actions:
  - press: start sequence playback if stopped
  - press: stop sequence playback if playing
possible_indicators:
  - PLAY LED lit: playback is running
current_state: unknown
state_note: Current playback state and LED state cannot be inferred from the manual or static panel references alone.
Surface map entry
node_id: sequencer.play_button
approximate_position: sequencer section, upper central transport area
landmarks:
  - sequencer controls cluster
  - nearby REC button
  - step button row below
neighbours:
  - REC button nearby in the same sequencer-control area
  - TEMPO knob nearby in the sequencer section
  - step buttons below in the lower sequencer area
navigation_hint: From the lower step-button row, move upward into the sequencer control cluster; the PLAY button is the transport button used to start and stop playback.
Non-visual description

The PLAY button is the monotribe’s main transport control for sequence playback. Treat it as a toggle-style action button: one press starts the sequence, and another press stops it. The manual says playback starts from the beginning of the sequence, and the PLAY LED indicates playback, but I cannot know whether it is currently lit from static sources alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 14; monotribe_manual_visual_index.json, sequencer section entry for page 13; static panel photo reference; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: The PLAY function is manual-grounded; exact tactile placement is based on static layout references, not live observation.
Unsupported-current-state risk: Low.
[/Trace]



# Baseline:
## R1:
Direct answer: The PLAY button starts or stops the monotribe’s sequence. Pressing it begins playback from the start of the sequence; pressing it again stops playback. The PLAY LED is lit while playback is running.

Where it is: It is in the Sequencer section, listed as control 4 in the manual’s sequencer panel diagram. It sits among the transport/basic sequence controls, near the ACTIVE STEP button, TEMPO knob, and sequencer step controls.

What it does and how to use it:

Press PLAY to play the sequence.
Press PLAY again to stop the sequence.
Playback always starts from the beginning of the sequence.
In record-ready mode, pressing PLAY starts playback and activates record mode.

Limitation: The manual and static panel sources cannot tell whether the PLAY button or PLAY LED is currently active on your unit.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 13–15; static panel photo for general layout context.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The PLAY button function is explicitly documented in the sequencer section.
Unsupported-current-state risk: Low.
[/Trace]

## R2
PLAY button — structured description

Direct answer:
The PLAY button starts or stops the monotribe’s sequence. Press it once to play the sequence; press it again to stop. Playback always starts from the beginning of the sequence. The PLAY LED is lit while playback is running.

Where it is:
It is in the Sequencer section, among the basic transport and step controls. In the manual’s sequencer diagram, it is identified as control 4, near the upper part of the sequencer control area, close to the FLUX, REC, and GATE TIME buttons.

What it does:

Starts sequence playback.
Stops sequence playback.
When playback starts, it begins from the first step of the sequence.
Its LED indicates playback status: lit during playback.

Limitations:
The manual describes what the PLAY button does, but it cannot tell whether your physical PLAY button is currently pressed, whether playback is currently running, or whether the LED is currently lit.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 13–14, Sequencer section / Basic controls / PLAY button; static panel photo for general layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The PLAY button function is explicitly documented in the sequencer section.
Unsupported-current-state risk: Low.
[/Trace]

## R3
Play button — structured description

Direct answer:
The PLAY button starts or stops the monotribe’s sequence. Playback always starts from the beginning of the sequence. The PLAY LED is lit while playback is running.

Where it is:
It is in the Sequencer section, among the basic transport controls. In the manual’s sequencer diagram, it is numbered 4, near the other sequence controls such as ACTIVE STEP, TEMPO, FLUX, and REC.

How to use it:
Press PLAY once to start the sequence. Press PLAY again to stop it. If the monotribe is in record-ready mode after pressing REC while stopped, pressing PLAY starts playback and activates record mode.

What it does not tell us:
The manual and static panel photo can identify the button and describe its function, but they cannot tell whether your unit is currently playing, stopped, or whether the PLAY LED is currently lit.

[Trace]
Sources used: monotribe_manual.pdf, Sequencer section, “Basic controls,” PLAY button; static panel photo for general control-layout context.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines the PLAY button function and LED behavior.
Unsupported-current-state risk: Low.
[/Trace]
