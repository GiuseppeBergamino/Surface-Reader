Prompt ID: k3

Prompt: Which control should I use to change the volume of the drum parts? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the RHYTHM knob. It adjusts the volume of the monotribe’s drum sound generator — the drum parts are BD bass drum, SN snare drum, and HH hi-hat.

From the performer’s perspective, the RHYTHM knob is in the sequencer section, on the right side of the lower control area, near the drum step controls. Tactilely, find the row of step buttons along the lower half of the panel; the RHYTHM knob is the rotary knob associated with the drum sound generator controls.

What it does: turn it clockwise to raise the drum-part volume, and counterclockwise to lower it. The manual also tells you to turn both the LEVEL knob and RHYTHM knob fully left before power-off, which confirms RHYTHM is a drum-volume control.

[Trace]
Sources used: monotribe_manual.pdf pages 13–15; monotribe_manual_visual_index.json entry for page 13; Interaction Guidance Store; Surface ARIA Store; Surface Model/Map Schema; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names RHYTHM knob as the drum sound generator volume control, and the sequencer layout diagram supports its region.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the RHYTHM knob. The manual says the RHYTHM knob adjusts the volume of the drum sound generator.

From the performer’s perspective, it is in the sequencer section, toward the right side of the lower control area, near the drum-step controls. It is a rotary knob, so turn it clockwise to raise the drum-part volume and counterclockwise to lower it.

It affects the drum sound generator as a whole: the BD bass drum, SN snare drum, and HH hi-hat parts are the drum parts described by the manual.

[Trace]
Sources used: monotribe_manual.pdf, manual page 15; monotribe_manual_visual_index.json entry for page 13; static panel photo foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The control name and function are explicitly documented, and layout is supported by the sequencer panel diagram/static panel reference.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the RHYTHM knob. The manual says it “adjusts the volume of the drum sound generator,” meaning it controls the overall level of the drum parts: BD, SN, and HH together.

From the performer’s perspective, it is in the sequencer section, on the right half of the top panel. Use the row of eight step buttons as a lower landmark; the RHYTHM knob is above that step-button area, near the drum sequencing controls. It is a rotary knob, so turn it clockwise to raise the drum level and counterclockwise to lower it.

It does not adjust BD, SN, and HH separately; it changes the drum sound generator’s overall volume.

[Trace]
Sources used: monotribe_manual.pdf, page 15; monotribe_manual_visual_index.json entry for page 13; foto_pannello.jpeg; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 04_routing_and_uncertainty_policy.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The control name and function are directly documented, and its region is supported by the sequencer layout.
Unsupported-current-state risk: None.
[/Trace]

# Baseline:
## R1:
Use the RHYTHM knob to change the volume of the drum parts. The manual says this knob “adjusts the volume of the drum sound generator.”

It is in the Sequencer section, near the lower-right area of the panel controls. In the sequencer layout, it is item 11, positioned near the step buttons used for the drum parts.

The drum sound generator includes the three drum parts: BD bass drum, SN snare drum, and HH hi-hat. Turning the RHYTHM knob raises or lowers the overall volume of those drum sounds together; it is not documented as separate volume control for each individual drum part.

[Trace]
Sources used: monotribe_manual.pdf, English manual p.15 “Drum sound generator sequence controls”; static panel photo for general layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual directly identifies the RHYTHM knob and its function.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the RHYTHM knob. It adjusts the volume of the drum sound generator.

It is in the sequencer section, toward the right side of the main control panel, near the row of step buttons. In the sequencer diagram it is item 11, just to the left of the drum step-control area.

Turn it clockwise to raise the drum-part volume, and counterclockwise to lower it. This affects the drum sound generator as a whole, not just one individual drum part.

[Trace]
Sources used: monotribe Owner’s manual, pages 13–15; static panel photo used for general layout.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies “RHYTHM knob” as controlling drum sound generator volume.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the RHYTHM knob to change the volume of the drum parts.

It is in the sequencer section, toward the right side of the panel, near the drum step controls. In the manual’s sequencer layout, it is control 11.

What it does: the RHYTHM knob adjusts the volume of the drum sound generator, which includes the BD bass drum, SN snare drum, and HH hi-hat parts. Turn it left for less drum volume and right for more.

[Trace]
Sources used: monotribe_manual.pdf, pages 13–15; static panel photo.
Routing weights: Device manual 80%; Visual/static layout 20%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies “RHYTHM knob” as adjusting the drum sound generator volume.
Unsupported-current-state risk: None.
[/Trace]

