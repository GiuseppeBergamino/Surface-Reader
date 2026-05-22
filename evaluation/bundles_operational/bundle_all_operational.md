Prompt ID: All

Prompt: Describe what the Monotribe is and what it does.

# Surface Reader:
## R1:
The Korg monotribe is an analogue ribbon station: a small, self-contained instrument that combines an analog synthesizer, analog drum sounds, and an eight-step sequencer.

It makes sound in two main ways:

The synthesizer part uses analog circuitry: a VCO for pitch and waveform, a VCF filter for tone color, and a VCA for volume. The filter is based on the classic Korg MS-20 filter circuit. You play the synth from the ribbon keyboard, which can act like a continuous pitch strip or play chromatic notes depending on the range setting.

The drum part has three discrete analog drum sounds: BD bass drum, SN snare drum, and HH hi-hat. These are controlled from the sequencer.

The sequencer lets you create repeating patterns. It has eight steps and can sequence both the synth part and the drum parts. Its FLUX mode lets the synth sequence play back more continuously instead of being locked strictly to one note per step, which is useful for more fluid or irregular grooves.

It can also process outside sound. Audio plugged into AUDIO IN is mixed with the oscillator and sent through the filter and amplifier, so the monotribe can act partly like an effects processor for another audio source. It has a built-in speaker, headphone/output connections, sync in/out for timing with other gear, and can run from batteries or an optional AC adapter.

Tactile mental map: think of it as three instruments in one box — a ribbon-played analog synth, a three-sound drum machine, and a step sequencer. The ribbon keyboard is the performance surface; the knobs and switches shape the synth sound; the buttons and step row build patterns.

[Trace]
Sources used: monotribe_manual.pdf, especially Main features, sound generator structure, block diagram, connections, panel description, sequencer section.
Routing weights: Device manual 80%; Interaction Guidance Store 10%; Mode Policy Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The answer summarizes official manual descriptions and avoids unsupported current-state claims.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The Korg monotribe is an analog ribbon station: a small performance instrument that combines an analog synthesizer, analog drum sounds, and an eight-step sequencer.

It makes sound in two main ways:

Synthesizer part
It has an analog VCO, VCF, and VCA: oscillator, filter, and amplifier. In practical terms, you shape pitch, tone, and volume. The filter is based on the classic Korg MS-20 low-pass filter circuit.
Drum part
It has a three-part analog drum sound generator: BD bass drum, SN snare, and HH hi-hat.

You play it with a ribbon keyboard, not normal keys. The ribbon can play continuous pitch changes or chromatic notes, depending on the range setting.

It also has an eight-step sequencer, so you can create repeating loops with the synth part and the drum parts. The FLUX mode lets the synth sequence play back more freely, without being locked strictly to step positions.

From a non-visual orientation standpoint, think of it as three functional areas:

Synth controls: shape the sound with oscillator, filter, amp, envelope, and LFO controls.
Sequencer controls: start, stop, record, choose parts, and turn steps on or off.
Performance/input area: the ribbon keyboard for playing notes and entering synth sequences.

It also has audio input, audio output, headphones, sync in/out, a built-in speaker, and can run on batteries or an optional AC adapter.

[Trace]
Sources used: monotribe_manual.pdf, monotribe_manual_visual_index.json, 03_mode_policy_store.md, 02_interaction_guidance_store.md.
Routing weights: Device manual 80%; Visual/static layout 5%; Interaction Guidance Store 10%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The answer summarizes documented main features and sound-generator structure from the manual.
Unsupported-current-state risk: None.
[/Trace]

## R3:
The Korg monotribe is an analogue ribbon station: a small hardware instrument that combines an analog synthesizer, analog drum sounds, and an eight-step sequencer. The manual describes its main sound engine as analog circuitry: VCO for pitch/waveform, VCF for tone or brightness, and VCA for volume, with a filter circuit based on the classic Korg MS-20.

What it does:

It makes synth sounds from a ribbon keyboard. You touch the ribbon to play notes, either with continuous pitch movement or chromatic stepped pitch, depending on the range mode.

It also has a three-part analog drum sound generator for bass drum, snare, and hi-hat. These can be sequenced along with the synth.

Its eight-step sequencer lets you create repeating patterns and loops in real time. The synth part can use normal step behavior, or FLUX mode, where synth motion is recorded and played back more freely instead of being locked strictly to each step.

It can also process outside sound: audio plugged into AUDIO IN is mixed with the VCO and sent through the filter and amplifier, so the monotribe can act partly like an effects processor for another audio source.

A useful mental map: think of the monotribe as one analog synth voice plus three analog drum parts, all driven by a simple loop sequencer, with a ribbon keyboard for hands-on performance.

[Trace]
Sources used: monotribe_manual.pdf, pages 5–6 and related parsed manual text; 03_mode_policy_store.md; 02_interaction_guidance_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 80%; Interaction Guidance Store 10%; Mode Policy Store 5%; Routing/Uncertainty Policy 5%.
Evidence confidence: High.
Confidence rationale: The answer summarizes the manual’s stated main features and sound-generator structure.
Unsupported-current-state risk: None.
[/Trace]

# Baseline:
## R1:
The Korg monotribe is an analog ribbon station: a small instrument for making synth sounds, drum patterns, and loops. It combines an analog synthesizer, an analog three-part drum sound generator, and an eight-step sequencer.

It makes sound with classic analog synth building blocks: VCO for pitch, VCF for timbre, and VCA for volume. You can play the synth from the ribbon keyboard, record synth notes into the sequencer, and create rhythm patterns with bass drum, snare, and hi-hat parts.

It also has features for performance and sound shaping: a ribbon keyboard with different pitch ranges, FLUX mode for less step-bound synth recording, an LFO for modulation, an external audio input that can be processed through the synth path, sync jacks for working with other gear, a built-in speaker, and battery or AC adapter power.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 5–6; page 8 for external input and sync overview.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The description is taken directly from the manual’s “Main features” and sound generator overview.
Unsupported-current-state risk: None.
[/Trace]

## R2:
The Korg monotribe is an analogue ribbon station: a small analog synthesizer and rhythm/sequencer instrument built for hands-on sound creation and loop performance.

It combines three main things:

Analog synthesizer
The synth sound generator uses a VCO, VCF, and VCA. These control pitch, timbre, and volume. The manual says the VCO, VCF, and VCA are built with analog circuitry, and the filter uses the classic Korg MS-20 filter circuit.
Ribbon keyboard
Instead of normal piano keys, you play it by touching a ribbon keyboard. It can work in continuous pitch modes or in chromatic steps, depending on the RANGE setting.
Analog drum and step sequencer
It has a three-part analog drum sound generator: BD bass drum, SN snare drum, and HH hi-hat. These, along with the synth part, can be controlled by the built-in eight-step sequencer to make loops.

It can also process an external audio source through its AUDIO IN jack, synchronize with other compatible gear using SYNC IN and SYNC OUT, and play through its built-in speaker or external outputs.

[Trace]
Sources used: monotribe_manual.pdf pages 5–8, 10–17; static panel photo not used.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The description is directly based on the manual’s “Main features,” sound generator structure, connections, and specifications sections.
Unsupported-current-state risk: None.
[/Trace]

## R3
The Korg monotribe is an analogue ribbon station: a small instrument that combines an analog synthesizer, analog drum sounds, and an eight-step sequencer. The manual describes it as having analog VCO, VCF, and VCA circuitry, with a filter based on the classic Korg MS-20 circuit.

It makes sound in two main ways. First, the synthesizer part produces sound from an oscillator, then shapes it with a filter and amplifier. You can play it by touching the ribbon keyboard, or by playing back recorded sequence data. Second, the drum sound generator provides three analog drum parts: BD bass drum, SN snare drum, and HH hi-hat.

It also has an eight-step sequencer, so you can make repeating patterns using both the synth part and the drum parts. The FLUX mode lets the synth sequence be recorded and played back without being restricted strictly to the steps, for more fluid or unusual rhythmic patterns.

It can also process external audio: an audio source connected to AUDIO IN is mixed with the VCO and sent through the filter and amp, so the monotribe can be used to modify an external sound source. It has a built-in speaker and can run from batteries or an optional AC adapter.

[Trace]
Sources used: monotribe_manual.pdf, English owner’s manual pages 5–6; page 8 for AUDIO IN; page 13 for sequencer overview.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The answer is directly based on the manual’s “Main features” and sound-generator description.
Unsupported-current-state risk: None.
[/Trace]