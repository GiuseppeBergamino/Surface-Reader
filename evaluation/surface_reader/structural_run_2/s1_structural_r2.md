Prompt: Create a structured description of the keyboard range selector.

Response: 

Keyboard range selector — structured description

Official name: RANGE select switch
Device area: Synthesizer section → VCO / keyboard control area
Semantic role: switch
Physical type: three-position slide switch
Purpose: Sets how the ribbon keyboard controls pitch. The manual says it “specifies the ribbon keyboard’s playing mode” .

Possible positions

WIDE
Extends the pitch range to approximately six times the NARROW setting. Pitch change is continuous, and the OCTAVE selector is ignored.

NARROW
Pitch changes continuously according to the printed ribbon keyboard range.

KEY
Pitch changes in chromatic steps according to the printed ribbon keyboard, making it behave more like a conventional keyboard.

Surface model node
{
  "node_id": "monotribe.synth.vco.range_select",
  "role": "switch",
  "name": "RANGE select switch",
  "region": "Synthesizer section",
  "group": "VCO / ribbon keyboard pitch control",
  "physical_type": "three-position slide switch",
  "description": "Selects the ribbon keyboard playing mode.",
  "possible_states": ["WIDE", "NARROW", "KEY"],
  "current_state": null,
  "actions": ["move to WIDE", "move to NARROW", "move to KEY"],
  "state_notes": {
    "WIDE": "Continuous pitch; range extended to about six times NARROW; OCTAVE selector ignored.",
    "NARROW": "Continuous pitch according to the printed ribbon keyboard.",
    "KEY": "Chromatic stepped pitch according to the printed ribbon keyboard."
  }
}
Non-visual orientation

From the performer’s perspective, this switch belongs to the synthesizer section, near the ribbon keyboard controls. Treat it as the keyboard-behavior switch: it decides whether the ribbon plays freely across a wide range, freely across a narrower range, or in chromatic note steps.

I cannot determine its current position from the manual, diagram, or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 11; monotribe_manual_visual_index.json entry for page 10; foto_pannello static panel photo; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual directly defines the RANGE select switch and its three documented positions; static layout sources support its physical/surface role.
Unsupported-current-state risk: Low.
[/Trace]
