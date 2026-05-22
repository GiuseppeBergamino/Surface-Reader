Prompt ID: neg1

Prompt: Create a structured description of the delay time.

# Surface Reader:
## R1:
Structured description: Delay time

I do not find a control or parameter officially named “delay time” in the monotribe manual. The closest documented timing-related synth control is GATE TIME, which changes the duration of the synth part’s notes during sequencer playback.

Surface model node
node_id: sequencer.gate_time
name: GATE TIME button
role: button
physical_type: button
region: Sequencer section
group: Synthesizer sequence controls
description: >
  Used with the ribbon keyboard during sequence playback to change the gate time,
  meaning the duration of the synth part’s notes.
actions:
  - hold
  - hold while touching the ribbon keyboard
possible_values:
  - minimum: 1.4% at the far left of the ribbon keyboard
  - middle example: 50% around the middle of the ribbon keyboard
  - maximum: 100% at the far right of the ribbon keyboard
current_state: unknown
state_limitation: >
  Static sources cannot determine the current recorded gate time or whether the
  button is currently being held.
recording_behavior: >
  If this operation is performed in REC mode, the gate time for each step can be
  recorded into the sequence.
manual_term: GATE TIME
Non-visual operational description

To adjust note duration, hold the GATE TIME button while the sequence is playing, then touch the ribbon keyboard. Touch farther left for shorter notes; touch farther right for longer notes. In REC mode, this can be recorded per step.

Important distinction

This is not an audio delay effect. The manual describes gate time, not delay time: it controls how long sequenced synth notes last, not echo or repeat timing.

[Trace]
Sources used: monotribe Owner’s manual, Sequencer section / GATE TIME description; uploaded file citation .
Routing weights: Device manual 70%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents GATE TIME and does not show an official “delay time” parameter in the provided English section.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Structured description: “Delay Time”

Device: Korg monotribe
Control/entity status: No dedicated Delay Time control is documented in the monotribe owner’s manual. The monotribe manual describes VCO, VCF, VCA, LFO, EG, sequencer, rhythm, sync, and global settings, but not an audio delay effect or a delay-time parameter.

Surface model entry
name: Delay Time
documented_on_monotribe: false
role: unsupported / not present in documented surface model
physical_type: none documented
region: none documented
group: none documented
function: not applicable
possible_values: none documented
current_state: unavailable
Non-visual guidance

Do not look for a Delay Time knob, switch, button, or menu item on the monotribe itself. If you are hearing repeats or echoes, that is likely coming from external equipment, a mixer, a pedal, a DAW effect, or another connected device—not from a documented monotribe delay parameter.

Related documented controls that might be confused with delay

The closest time-related controls on the monotribe are:

TEMPO knob:
  role: slider
  physical_type: rotary knob
  region: Sequencer section
  function: Sets sequencer speed.
  delay_related: false

LFO RATE knob:
  role: slider
  physical_type: rotary knob
  region: Synthesizer section / LFO group
  function: Adjusts modulation speed.
  delay_related: false

GATE TIME button:
  role: button
  physical_type: button
  region: Sequencer section
  function: Used with the ribbon keyboard to change synth note duration in the sequence.
  delay_related: false

[Trace]
Sources used: monotribe_manual.pdf, manual page uncertain; 04_routing_and_uncertainty_policy.md; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Routing/Uncertainty Policy 15%; Surface ARIA Store 15%; Surface Model/Map Schema 15%.
Evidence confidence: Medium.
Confidence rationale: The available manual text lists documented controls and functions but contains no Delay Time parameter in the shown English section.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
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

# Baseline:
## R1:
The monotribe manual does not document a “delay time” control or delay effect. A delay-time parameter is therefore not available from the manual-grounded sources.

A documented, similarly named but different control is GATE TIME. This is not delay time; it is the duration of the synth part’s notes during sequence playback.

Where it is: GATE TIME button, in the sequencer section. It is one of the synthesizer sequence controls.

How it works:

Hold GATE TIME while a sequence is playing.
Touch the ribbon keyboard to set the note duration.
Far left of the ribbon keyboard = minimum gate time, 1.4%.
Far right of the ribbon keyboard = maximum gate time, 100%.
In REC mode, gate time can be recorded per step into the sequence.

Limitation: The manual does not describe any separate “delay time” parameter, delay effect, or echo function.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 13–15; static panel photo not used.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents GATE TIME and does not document a delay-time function in the relevant control descriptions.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The monotribe manual does not document a control or parameter named “delay time.” The documented timing-related control that may be closest is GATE TIME, which changes the duration of synth-part notes in the sequencer.

Structured description: GATE TIME / note duration

What it is:
GATE TIME is the duration of the synth part’s notes during sequence playback.

Where it is:
The GATE TIME button is in the sequencer section, near the synth sequence controls. It is used together with the ribbon keyboard.

How it works:
While a sequence is playing, hold GATE TIME and touch the ribbon keyboard. The touched position sets the note duration.

Range:
The far left of the ribbon keyboard gives the minimum gate time: 1.4%.
The far right gives the maximum gate time: 100%.

Recording:
If you do this while in REC mode, the gate time for each step can be recorded into the sequence and played back later.

Limitation:
This is not a delay effect and is not called “delay time” in the manual. A separate delay-time parameter is not documented.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section / GATE TIME description; static panel photo not used.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly documents GATE TIME but does not document a “delay time” parameter.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The monotribe manual does not document a “delay time” control or delay effect. It does document GATE TIME, which is a note-duration setting for the synth part, not an audio delay.

Structured description: GATE TIME

What it controls
GATE TIME changes the duration of the synth part’s notes during sequence playback.

Where it is
The GATE TIME button is in the sequencer section. In the panel diagram, it is control 8, near the top-right area of the sequencer controls.

How to use it
While a sequence is playing, hold down GATE TIME and touch the ribbon keyboard. The position you touch sets the gate time.

Range
The far left of the ribbon keyboard gives the minimum value, 1.4%. The far right gives the maximum value, 100%.

Recording behavior
If you do this while in REC mode, the gate time for each step can be recorded into the sequence and played back later.

Important limitation
This is not documented as delay time. The manual does not describe a delay effect or a delay-time parameter.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual, Sequencer section, “GATE TIME button,” page 15; static panel photo not used.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines GATE TIME and does not document delay time.
Unsupported-current-state risk: None.
[/Trace]

