Prompt: Create a structured description of the rythm level.

Response: 

Structured description: RHYTHM level

Official control name: RHYTHM knob
Likely user term: “rhythm level”
Region: Sequencer section
Group: Drum sound generator sequence controls
Semantic role: slider
Physical type: rotary knob
Function: Adjusts the volume of the drum sound generator. The monotribe’s drum sound generator includes BD, SN, and HH parts, played by sequence data.

{
  "node_id": "sequencer_rhythm_level",
  "role": "slider",
  "name": "RHYTHM knob",
  "physical_type": "rotary knob",
  "region": "Sequencer section",
  "group": "Drum sound generator sequence controls",
  "description": "Adjusts the volume of the drum sound generator.",
  "affected_parts": ["BD", "SN", "HH"],
  "actions": ["turn clockwise to raise drum level", "turn counterclockwise to lower drum level"],
  "possible_states": "continuous volume value",
  "current_state": "requires situated evidence",
  "nearby_controls": {
    "related": ["PART buttons", "STEP buttons"],
    "same_functional_area": "drum sequence controls"
  },
  "safety_notes": [
    "Before turning the power on, the manual instructs turning LEVEL and RHYTHM all the way left.",
    "For power-off, the manual also instructs turning LEVEL and RHYTHM all the way left."
  ]
}
Non-visual use

Treat RHYTHM as the drum level knob. It does not set the synth volume; it controls the drum sound generator level. The manual also uses it during startup and shutdown: turn both LEVEL and RHYTHM fully left before powering on or off, then turn RHYTHM clockwise to an appropriate level after power-on.

Current-state limitation

I can describe what RHYTHM does and how it should be represented, but I cannot know its current knob position from the manual or static panel references alone. A continuous rotary knob may be modeled as a slider, but valuenow requires situated evidence.

[Trace]
Sources used: monotribe_manual.pdf pages 5, 9, 15; 01_surface_aria_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 55%; Surface ARIA Store 20%; Surface Model/Map Schema 15%; Interaction Guidance Store 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names RHYTHM knob and states its function; semantic mapping follows the provided surface-model rules.
Unsupported-current-state risk: Low.
[/Trace]

