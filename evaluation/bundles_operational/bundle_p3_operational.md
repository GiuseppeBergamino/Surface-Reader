Prompt ID: p3

Prompt: Which port should I use to synchronize the instrument from an external device? Describe where it is and what it does.

# Surface Reader:
## R1:
Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the rear connection panel, in the row of ports along the top/back edge of the instrument. From the performer’s perspective, feel along that rear row: the SYNC OUT and SYNC IN mini-jacks are near the right side of the connection group, with SYNC IN to the right of SYNC OUT.

What it does: when a cable is connected to SYNC IN, the monotribe ignores its internal step clock. Its sequencer advances step-by-step according to incoming pulses from another monotribe, an analog sequencer, or a DAW audio output. The manual also says the SYNC IN pulse polarity can be set in the Global menu.

[Trace]
Sources used: monotribe_manual.pdf page 8; monotribe_manual_visual_index.json page 8 entry; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 55%; Visual/static layout 20%; Surface ARIA Store 5%; Surface Model/Map Schema 5%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names SYNC IN, describes its function, and the connection diagram supports its rear-panel location.
Unsupported-current-state risk: Low.
[/Trace]

## R2:
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

## R3:
Use the SYNC IN jack to synchronize the monotribe from an external device. The manual says that when SYNC IN is connected, the internal step clock is ignored, and the sequencer advances through its steps according to incoming pulses from another monotribe, an analog sequencer, or a DAW audio output.

From the performer’s perspective, it is on the far/top edge connection panel, near the right end. In the row of rear connections, find the two small sync mini-jacks close together: SYNC OUT is first, and SYNC IN is immediately to its right. Use SYNC IN for receiving clock; use SYNC OUT only when the monotribe is sending clock to another device.

Before connecting, the manual warns to turn off the power to avoid damaging speakers or causing malfunctions.

[Trace]
Sources used: monotribe_manual.pdf page 8; monotribe_manual_visual_index.json entry for page 8; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing/Uncertainty Policy.
Routing weights: Device manual 55%; Visual/static layout 20%; Surface ARIA Store 5%; Surface Model/Map Schema 5%; Interaction Guidance Store 10%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The manual directly identifies SYNC IN and its synchronization behavior, and the page 8 connection diagram supports the rear-panel location.
Unsupported-current-state risk: Low.
[/Trace]

# Baseline:
## R1:
Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the connector side of the instrument in the row of rear-panel jacks. In the manual’s connection diagram, it is jack 7, at the right end of the numbered connection row, immediately to the right of SYNC OUT.

What it does: when something is plugged into SYNC IN, the monotribe ignores its internal step clock, and the sequencer advances through its steps according to the pulses arriving at that jack. The manual says it can sync the monotribe’s steps from another monotribe, an analog sequencer, or the audio output of a DAW. The input polarity can be set in the Global menu.

[Trace]
Sources used: monotribe_manual.pdf, Connections section p.8; Global menu p.16.
Routing weights: Device manual 100%; Visual/static layout 0%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies SYNC IN and describes its synchronization behavior.
Unsupported-current-state risk: None.
[/Trace]

## R2:
Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the connector side/rear edge of the instrument, in the row of ports. In the manual’s connection diagram it is port 7, immediately to the right of SYNC OUT, which is port 6.

What it does: when SYNC IN is connected, the monotribe ignores its internal step clock. The sequencer advances through its steps according to pulses received at this jack. The manual says it can sync to pulses from another monotribe, an analog sequencer, or the audio output of a DAW. The detected pulse polarity can be set in the Global menu.

[Trace]
Sources used: monotribe Owner’s Manual, Connections p.8; Global menu p.16.
Routing weights: Device manual 90%; Visual/static layout 10%.
Evidence confidence: High.
Confidence rationale: The manual explicitly identifies SYNC IN and describes its synchronization function.
Unsupported-current-state risk: None.
[/Trace]

## R3:
Use the SYNC IN jack to synchronize the monotribe from an external device.

It is on the rear connection row, near the right end. In the manual’s connection diagram it is connector 7, immediately to the right of SYNC OUT and just before the grounding screw area.

What it does: when something is connected to SYNC IN, the monotribe ignores its internal step clock, and the sequencer advances through its steps according to incoming pulses. The manual says it can sync to pulses from another monotribe, an analog sequencer, or the audio output of a DAW. The SYNC IN polarity can be set in the Global menu.

[Trace]
Sources used: monotribe_manual.pdf, Connections section p.8; Global menu p.16; static panel photo for rear-panel layout.
Routing weights: Device manual 85%; Visual/static layout 15%.
Evidence confidence: High.
Confidence rationale: The manual explicitly names SYNC IN and describes external pulse synchronization.
Unsupported-current-state risk: None.
[/Trace]



