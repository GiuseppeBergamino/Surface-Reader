Prompt: Create a structured description of the octave selector.

Response:

Direct answer: The OCTAVE selector sets the VCO pitch in octave steps. It affects the pitch range used by the ribbon keyboard, except when the RANGE select switch is set to WIDE, because WIDE ignores the OCTAVE selector.

Where it is: It is in the Synthesizer section, at the upper-left area of the main control panel. In the manual’s numbered panel diagram it is control 1, immediately near the WAVE select switch labeled as control 2.

What it does: The manual says: “This specifies the VCO pitch in steps of an octave.” With the 64' setting, the ribbon keyboard pitch range is A0–D2. The VCO pitch is otherwise determined by the touched position on the ribbon keyboard or recorded sequence data.

Interaction with RANGE:

NARROW: OCTAVE selector applies; pitch changes continuously according to the printed ribbon keyboard.
KEY: OCTAVE selector applies; pitch changes in chromatic steps according to the printed ribbon keyboard.
WIDE: OCTAVE selector is ignored; pitch range is extended to about six times NARROW and changes continuously.

Limitation: The manual and static panel photo can identify the selector and describe its function, but they cannot tell what octave position your physical unit is currently set to.

[Trace]
Sources used: monotribe_manual.pdf, English manual pages 10–11; static panel photo.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The OCTAVE selector is explicitly named and described in the manual’s synthesizer section.
Unsupported-current-state risk: Low.
[/Trace]