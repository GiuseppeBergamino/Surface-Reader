Prompt: Create a structured description of the cutoff.

Response: 

Cutoff control — structured description

Official name: CUTOFF knob

Region: Synthesizer section

Group: VCF, or Voltage Controlled Filter

Semantic role: slider

Physical type: rotary knob

Function: The CUTOFF knob adjusts the cutoff frequency of the VCF. In practical sound terms, it changes the brightness of the synth sound. Turning it left makes the sound darker; turning it right makes it brighter.

Related control: PEAK knob. Cutoff sets the filter’s cutoff point; Peak emphasizes the sound around that cutoff frequency.

Non-visual location: From the performer’s perspective, the Cutoff knob is in the upper-middle synth-control area, in the filter group. It is the upper knob of the filter pair, with Peak directly below it.

Possible values: Continuous knob range; the manual describes left as darker and right as brighter, but does not provide numeric values.

Current state: Unknown. A manual or static panel photo cannot tell where the Cutoff knob is currently set.

node_id: synth.vcf.cutoff
name: CUTOFF knob
role: slider
physical_type: rotary knob
region: Synthesizer section
group: VCF
actions:
  - turn counterclockwise to lower cutoff / darken sound
  - turn clockwise to raise cutoff / brighten sound
possible_states:
  - lower cutoff / darker sound
  - higher cutoff / brighter sound
current_state: unavailable from static sources
neighbours:
  below: PEAK knob
semantic_relationships:
  - part of VCF filter group
  - affects timbre / brightness

[Trace]
Sources used: monotribe Owner’s Manual, panel description and functions; manual visual index, panel overview for synthesizer section; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%, Visual/static layout 20%, Surface ARIA Store 15%, Surface Model/Map Schema 10%, Interaction Guidance Store 5%, Mode Policy Store 3%, Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The function and neighbouring filter context are documented in the manual, and the layout is supported by the panel overview/static references.
Unsupported-current-state risk: Low.
[/Trace]