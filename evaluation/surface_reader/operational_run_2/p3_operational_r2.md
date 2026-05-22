Prompt: Which port should I use to synchronize the instrument from an external device? Describe where it is and what it does.

Response: 

Use the SYNC IN jack to synchronize the monotribe from an external device. The manual says that when SYNC IN is connected, the monotribe ignores its internal step clock and the sequencer advances according to pulses coming into that jack. It can sync to pulses from another monotribe, an analog sequencer, or the audio output of a DAW.

From the performer’s perspective, it is on the rear connection edge, in the row of ports. Move along that rear row from left to right: after HEADPHONES comes SYNC OUT, then SYNC IN. So SYNC IN is immediately to the right of SYNC OUT and just before the grounding screw area. The visual index identifies manual page 8 as the rear-panel connections diagram for audio, headphones, and sync I/O.

Use SYNC OUT only when the monotribe is the clock source for another device. Use SYNC IN when another device is the clock source for the monotribe.

[Trace]
Sources used: monotribe_manual.pdf, page 8; monotribe_manual_visual_index.json, page 8 entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store.
Routing weights: Device manual 45%; Visual/static layout 25%; Surface ARIA Store 10%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 5%.
Evidence confidence: High.
Confidence rationale: The manual directly names SYNC IN/SYNC OUT and documents their sync behavior; the connection diagram supports the rear-panel location.
Unsupported-current-state risk: Low.
[/Trace]