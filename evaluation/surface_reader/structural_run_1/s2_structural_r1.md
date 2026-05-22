Prompt: Create a structured description of the VCO wave selector.

Respose: 

VCO WAVE select switch — structured description

Official name: WAVE select switch
Device section: Synthesizer section
Group: VCO — Voltage Controlled Oscillator
Semantic role: switch
Physical type: three-position waveform selector switch
Purpose: selects the oscillator waveform that becomes the basic sound source of the synth voice.

Documented possible positions
Position	Meaning	Sound source
Sawtooth wave	Selects sawtooth oscillator waveform	bright, harmonically rich VCO tone
Triangle wave	Selects triangle oscillator waveform	smoother, simpler VCO tone
Square wave	Selects square oscillator waveform	hollow/pulse-like VCO tone

The manual states that the VCO generates “the waveform that’s the basis of the sound: a sawtooth wave, triangle wave, or square wave,” and that the WAVE select switch chooses between those three waveforms.

Non-visual location and orientation

From the performer’s perspective, the VCO controls are in the upper-left synthesizer area of the panel. The WAVE select switch is part of the VCO group, near the OCTAVE selector and NOISE knob. Use the VCO area as a small oscillator cluster: octave selection, waveform selection, and noise level all belong together.

Surface model node
node_id: synth.vco.wave_select
role: switch
name: WAVE select switch
region: Synthesizer section
group: VCO
physical_type: three-position selector switch
description: Selects the VCO waveform used as the basis of the synth sound.
possible_states:
  - sawtooth wave
  - triangle wave
  - square wave
actions:
  - select sawtooth wave
  - select triangle wave
  - select square wave
current_state: unknown
current_state_note: Static sources cannot determine the switch’s present position.
Current-state limitation

I can describe the possible settings and static location, but I cannot know which waveform is currently selected without live evidence from the physical instrument.

[Trace]
Sources used: monotribe_manual.pdf; monotribe_manual_visual_index.json; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the WAVE select switch and its three possible waveform settings; layout is supported by the panel overview index.
Unsupported-current-state risk: Low.
[/Trace]
