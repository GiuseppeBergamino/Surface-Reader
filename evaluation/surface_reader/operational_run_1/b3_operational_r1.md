Prompt: Which controls should I use to work with sequencer steps? Describe where they are and what they do.

Response: 

For sequencer steps on the monotribe, use the Sequencer section, mainly the PART buttons, ACTIVE STEP button, PLAY button, REC button, GATE TIME button, STEP buttons, STEP LEDs, FLUX button, TEMPO knob, and RHYTHM knob. The manual says the monotribe has an eight-step sequencer controlling both the synthesizer and drum sound generator.

From the performer’s perspective, the sequencer section is the lower/right working area of the top panel, near the long ribbon keyboard. The STEP buttons are the main landmark: a row of eight repeated buttons used to turn steps on and off. The STEP LEDs correspond to those steps; during playback, they blink to indicate the current step, but I cannot know their current state from static sources alone.

The important controls are:

STEP buttons
Use these to turn individual steps on or off. For the synth part, an on step plays its recorded synth note; an off step does not play. For drum parts, the same step buttons turn hits on or off for the selected drum part: BD, SN, or HH.

PART buttons: SYNTH, BD, SN, HH
Use these to choose which part you are editing. Press SYNTH for the synth sequence. Press BD, SN, or HH to edit bass drum, snare, or hi-hat steps. Their associated PART LEDs indicate the selected part, but the current selection cannot be inferred here.

ACTIVE STEP button
Hold this while pressing a step button to enable or disable that step in the sequence structure. Disabled steps are skipped during playback and recording. This is different from simply muting a note or drum hit: it changes which steps the sequencer moves through.

PLAY button
Starts or stops the sequence. Playback starts from the beginning of the sequence.

REC button
Use this to record synth performance data from the ribbon keyboard into the sequence. Pressing REC during playback enters record mode; pressing it while stopped enters record-ready mode.

GATE TIME button
Use this with the ribbon keyboard during sequence playback to change the duration of synth notes. Far left on the ribbon gives the shortest gate time; far right gives the longest. In REC mode, gate time can be recorded per step.

FLUX button
Use this for the synth part. With FLUX on, synth sequence data is recorded and played back continuously rather than locked to one note per step. With FLUX off, one note plays back for each step.

TEMPO knob
Sets sequencer speed, unless SYNC IN is connected. Treat it as the main speed knob for step playback.

RHYTHM knob
Controls the volume of the drum sound generator, so it affects how strongly the BD, SN, and HH step patterns are heard.

Tactile memory anchor: the repeated row of eight step buttons is your sequencer grid. First choose the part with SYNTH / BD / SN / HH, then use the eight step buttons to decide what happens on each step. Use PLAY to hear the loop, REC to record synth motion, and ACTIVE STEP when you want the sequence itself to skip steps.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Visual/static layout 15%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly defines the sequencer controls and the visual index identifies the sequencer layout pages.
Unsupported-current-state risk: Low.
[/Trace]