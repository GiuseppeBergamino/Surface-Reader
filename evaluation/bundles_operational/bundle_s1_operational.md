Prompt ID: s1

Prompt: Which control should I use to change the ribbon keyboard range? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the RANGE select switch. It changes the ribbon keyboard’s playing mode/range. The manual lists three settings: WIDE, NARROW, and KEY. In WIDE, the ribbon pitch range is expanded to about six times the NARROW range and pitch is continuous; in NARROW, pitch changes continuously across the printed ribbon keyboard; in KEY, pitch changes in chromatic steps.

From the performer’s perspective, it is in the upper-left synthesizer/VCO area. Find the ribbon keyboard along the lower part of the panel as a landmark, then move up to the left-side synth controls. The RANGE control is a small three-position switch near the OCTAVE selector, WAVE select switch, and NOISE knob. It belongs to the VCO/ribbon keyboard control group.

It does not tell me the current range setting from the manual or static panel image alone; it only tells the possible settings and what they do.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10 panel overview, manual page 11 RANGE select switch description, monotribe_manual_visual_index.json, foto_pannello static panel photo, 01_surface_aria_store.md, 02_interaction_guidance_store.md, 03_mode_policy_store.md, 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The control name and function are directly documented, and its layout is supported by the panel diagram/static photo.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
Use the RANGE select switch. The manual says it “specifies the ribbon keyboard’s playing mode” and gives three settings: WIDE, NARROW, and KEY.

From the performer’s perspective, it is in the upper-left synthesizer section, in the VCO area. Use the ribbon keyboard as a lower-panel landmark, then move up and left toward the small VCO controls. The RANGE control is a three-position slide switch, near the OCTAVE selector, WAVE select switch, and NOISE knob. The manual’s panel overview identifies it as control 4 in the synthesizer section.

What it does:

WIDE: gives a much wider, continuous pitch sweep; the OCTAVE selector is ignored.
NARROW: gives continuous pitch changes over the printed ribbon keyboard range.
KEY: makes the ribbon play in chromatic steps, more like a regular keyboard.

[Trace]
Sources used: monotribe_manual.pdf, manual page 10/panel overview via monotribe_manual_visual_index.json, Surface ARIA Store, Surface Model/Map Schema, Interaction Guidance Store, Mode Policy Store, Routing/Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 7%; Mode Policy Store 2%; Routing/Uncertainty Policy 1%.
Evidence confidence: High.
Confidence rationale: The control name, function, possible settings, and numbered panel location are directly supported by the manual and visual index.
Unsupported-current-state risk: Low.
[/Trace]

## R3:
Use the RANGE select switch. The manual says it “specifies the ribbon keyboard’s playing mode” with WIDE, NARROW, and KEY settings.

From the performer’s perspective, it is in the left side of the synthesizer section, in the VCO area. Use the ribbon keyboard as a landmark: the RANGE switch is above the left part of the ribbon keyboard, below the upper-left VCO controls, and to the left of the filter knobs.

What it does:

WIDE: extends the ribbon pitch range to about six times the NARROW range; pitch changes continuously, and the OCTAVE selector is ignored.
NARROW: pitch changes continuously across the printed ribbon keyboard range.
KEY: pitch changes in chromatic steps, like a conventional keyboard.

It is a discrete-position control, so treat it as a switch, not a knob. I cannot tell which position yours is currently set to from the manual or static panel photo alone.

[Trace]
Sources used: monotribe_manual.pdf p.10–11; monotribe_manual_visual_index.json entry for p.10; foto_pannello; 01_surface_aria_store.md; 02_interaction_guidance_store.md; 03_mode_policy_store.md; 05_surface_model_map_schema.md.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual names the RANGE select switch and defines its settings; static layout sources support its approximate tactile location.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Use the RANGE select switch to change the ribbon keyboard range.

It is in the Synthesizer section, control number 4 in the manual’s panel diagram. On the top panel, it is near the upper-left synth controls, below/right of the OCTAVE area and next to the VCO controls.

What it does:
WIDE extends the pitch range to about six times the NARROW setting. Pitch changes continuously, and the OCTAVE selector is ignored.

NARROW makes pitch change continuously according to the printed ribbon keyboard.

KEY makes pitch change in chromatic steps according to the printed ribbon keyboard.

[Trace]
Sources used: monotribe_manual.pdf, pages 10–11; static panel photo for general control location.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies “RANGE select switch” and defines WIDE, NARROW, and KEY.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the RANGE select switch to change the ribbon keyboard range.

It is in the Synthesizer section, near the upper-left area of the top panel. In the manual’s control diagram it is control 4, below the WAVE select switch and near the OCTAVE selector.

What it does:

WIDE extends the ribbon keyboard pitch range to about six times the NARROW setting, with continuous pitch change. In WIDE, the OCTAVE selector is ignored.

NARROW gives continuous pitch change according to the printed ribbon keyboard.

KEY makes the pitch change in chromatic steps according to the printed ribbon keyboard.

[Trace]
Sources used: monotribe_manual.pdf, pages 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the RANGE select switch and defines WIDE, NARROW, and KEY.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the RANGE select switch.

It is in the Synthesizer section, near the upper-left area of the top panel. In the manual’s synth panel diagram it is control 4, beside the VCO controls: below the WAVE select switch and to the right of the NOISE knob.

What it does:

WIDE: Extends the ribbon keyboard pitch range to about six times the NARROW range; pitch changes continuously. The OCTAVE selector is ignored.
NARROW: Pitch changes continuously according to the printed ribbon keyboard.
KEY: Pitch changes in chromatic steps according to the printed ribbon keyboard.

[Trace]
Sources used: monotribe_manual.pdf, pp. 10–11; static panel photo used for layout confirmation.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names the RANGE select switch and describes all three settings.
Unsupported-current-state risk: Low.
[/Trace]


