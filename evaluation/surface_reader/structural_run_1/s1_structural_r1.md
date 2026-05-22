Prompt: Create a structured description of the keyboard range selector.

Response: 

Structured description: keyboard range selector

Official control name: RANGE select switch
Surface model role: switch
Physical type: three-position slide switch
Region: Synthesizer section
Group: VCO / keyboard control group
Related control: Ribbon keyboard

Function

The RANGE select switch sets the ribbon keyboard’s playing mode. The manual defines three possible positions: WIDE, NARROW, and KEY.

Possible positions
Position	Documented behavior
WIDE	Extends the pitch range to about six times the NARROW setting. Pitch changes continuously, and the OCTAVE selector is ignored.
NARROW	Pitch changes continuously according to the printed ribbon keyboard.
KEY	Pitch changes in chromatic steps according to the printed ribbon keyboard.
Non-visual description

From the performer’s perspective, the RANGE select switch is in the upper-left synthesizer area, near the VCO controls and related to the ribbon keyboard. It is not a knob; it is a discrete selector with three possible settings. Use it as a mode switch for how the ribbon responds when touched.

State limitation

This describes the control and its possible settings only. I cannot determine the current physical position of the RANGE switch from the manual or static panel references alone.

[Trace]
Sources used: monotribe_manual.pdf, manual page 11; monotribe_manual_visual_index.json entry for manual page 10; foto_pannello; 01_surface_aria_store.md; 05_surface_model_map_schema.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the control and its three documented settings; layout and role are supported by static references.
Unsupported-current-state risk: Low.
[/Trace]
