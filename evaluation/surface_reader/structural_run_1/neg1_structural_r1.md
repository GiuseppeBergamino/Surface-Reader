Prompt: Create a structured description of the delay time.

Respose: 

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