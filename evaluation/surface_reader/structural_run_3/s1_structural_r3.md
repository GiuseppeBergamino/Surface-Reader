Prompt: Create a structured description of the keyboard range selector.

Response: 

Keyboard range selector — structured description

Official name: RANGE select switch

Surface model role: switch

Physical type: three-position slide switch, based on the panel reference and manual layout.

Region: Synthesizer section

Group: VCO / ribbon keyboard control group

Function: It specifies the ribbon keyboard’s playing mode. The manual defines three possible settings:

Position	Meaning
WIDE	Extends the pitch range to about six times the NARROW setting. Pitch change is continuous. The OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.

Tactile location: From the performer’s perspective, the RANGE select switch is in the upper-left synthesizer area, near the ribbon keyboard controls. It belongs with the VCO controls rather than the sequencer. Use the long ribbon keyboard as a lower-panel landmark, then move upward toward the synth controls; the RANGE switch is one of the small discrete-position switches associated with how the ribbon responds.

Actions:
Move the switch to one of three discrete positions: WIDE, NARROW, or KEY.

Current state: Not available from static sources. I can describe the possible settings, but I cannot know which position your physical switch is currently in without live evidence.

Compact semantic node:

{
  "node_id": "synth.vco.range_select",
  "name": "RANGE select switch",
  "role": "switch",
  "physical_type": "three-position slide switch",
  "region": "Synthesizer section",
  "group": "VCO / ribbon keyboard controls",
  "description": "Specifies the ribbon keyboard's playing mode.",
  "possible_states": ["WIDE", "NARROW", "KEY"],
  "current_state": null,
  "actions": ["move to WIDE", "move to NARROW", "move to KEY"],
  "unsupported_current_state_risk": "High"
}

[Trace]
Sources used: monotribe_manual.pdf p.11; monotribe_manual_visual_index.json entry for p.10; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: Medium.
Confidence rationale: Function and possible states are manual-grounded; tactile location is based on static layout rather than live inspection.
Unsupported-current-state risk: High.
[/Trace]
