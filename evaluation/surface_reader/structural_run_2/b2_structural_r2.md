Prompt: Create a structured description of the rec button.

Response: 

Structured description: REC button

Control name: REC button
Semantic role: button
Physical type: pressable button
Region: Sequencer section
Group: Synthesizer sequence controls / recording controls
Related indicator: REC LED

Documented function:
The REC button controls recording for the synthesizer sequence. During playback, pressing REC puts the monotribe into record mode; the REC LED lights, and ribbon keyboard performance data is recorded. When stopped, pressing REC puts the unit into record-ready mode; the REC LED blinks. Pressing PLAY from that state starts playback and activates record mode. Press REC again to exit record or record-ready mode, making the REC LED go dark.

Possible states described by the manual:

REC LED lit: record mode during playback.
REC LED blinking: record-ready mode while stopped.
REC LED dark: not in record mode or record-ready mode.

Additional documented use:
When the sequencer is stopped and the monotribe is not producing sound, holding REC until the REC LED stops blinking and goes dark saves the sequence. Do not turn off the power while data is being saved, because this may destroy internal data.

Non-visual location guidance:
From the performer’s perspective, the REC button is in the sequencer section, near the PLAY button and the FLUX and GATE TIME controls. Use the lower/right sequencer control area as the working region, then identify the small transport/recording cluster rather than relying on printed labels. The manual’s sequencer panel diagram identifies REC as item 7 in that section.

Current-state limitation:
I can describe what the REC LED states mean, but I cannot determine whether the REC LED is currently lit, blinking, or dark from the manual or static panel references alone.

[Trace]
Sources used: monotribe_manual.pdf, sequencer section pages 13–16; monotribe_manual_visual_index.json entry for page 13; Surface ARIA Store; Surface Model/Map Schema; Interaction Guidance Store; Mode Policy Store; Routing and Uncertainty Policy.
Routing weights: Device manual 45%; Visual/static layout 20%; Surface ARIA Store 15%; Surface Model/Map Schema 10%; Interaction Guidance Store 5%; Mode Policy Store 3%; Routing/Uncertainty Policy 2%.
Evidence confidence: High.
Confidence rationale: The REC function and LED meanings are explicitly documented, and the sequencer diagram identifies its control grouping.
Unsupported-current-state risk: Low.
[/Trace]