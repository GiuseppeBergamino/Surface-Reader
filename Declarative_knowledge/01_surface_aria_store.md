# Surface ARIA Store

## Purpose
This store defines an ARIA-inspired semantic vocabulary for physical musical control surfaces.

It does not reproduce WAI-ARIA as a web standard. Instead, it adapts screen-reader accessibility principles to musical hardware by defining how physical controls, indicators, displays, regions, and ports should be represented as semantic nodes.

The goal is to help a Surface Reader translate manuals, screenshots, diagrams, and static panel photos into structured, non-visual, and navigable descriptions.

## Core idea
Manuals and static visual sources provide raw information.

They may describe:
- printed labels;
- control names;
- section names;
- documented functions;
- possible states;
- possible LED meanings;
- procedures;
- warnings;
- visual grouping;
- physical control shapes;
- panel layout;
- spatial relationships.

The Surface ARIA Store defines how this raw information should be represented semantically.

A Surface Reader should not merely repeat what appears visually on a panel. It should translate device documentation and static visual layout into semantic roles, properties, relationships, and tactilely useful descriptions.

## Source interpretation
Use different sources for different kinds of information.

### Device manual
Use the manual for:
- official names;
- documented functions;
- procedures;
- possible states;
- possible values;
- LED or display meanings;
- warnings;
- device-specific terminology.

Do not use the manual alone to infer:

- physical control shape when the wording is ambiguous;
- exact tactile layout if only visual diagrams provide it;
- current physical state.

### Screenshots, diagrams, and static panel photos
Use screenshots, diagrams, and static panel photos for:
- physical control type;
- approximate position;
- visual grouping;
- rows and columns;
- adjacency;
- repeated patterns;
- tactile landmarks;
- layout relations.

Do not use static images to infer:
- current knob values;
- current switch positions;
- current LED states;
- current display contents;
- current cable connections;
- current sound;
- what the user is touching.

## From manual information to Surface ARIA roles
Role assignment should use both textual and static visual evidence.

Use this procedure:
1. Identify the official control name from the manual when available.
2. Identify the documented function from the manual.
3. Identify the physical type from screenshots, diagrams, or static panel photos when available.
4. Assign a semantic role using this store.
5. Add possible states or values only when documented.
6. Add current-state properties only when situated evidence is available.
7. Add spatial and tactile properties only when supported by static layout sources.

Do not infer physical type from the manual term alone.

For example:
- “selector” may refer to a rotary selector, toggle switch, slide switch, or another physical form;
- “control” may refer to a knob, button, switch, fader, ribbon, encoder, or touch surface;
- “indicator” may refer to an LED, status light, display element, or another output cue;
- “key” may refer to a physical key, a keyboard note, or a menu item depending on context.

When textual and visual/static evidence are ambiguous, state the uncertainty and avoid over-specific tactile guidance.

## Semantic role vs physical type
Always distinguish semantic role from physical type.

The semantic role describes the interaction meaning.

The physical type describes the tangible form.

Examples:
- A rotary knob controlling a continuous value has role `slider` and physical type `rotary knob`.
- A fader controlling a continuous value has role `slider` and physical type `fader`.
- A rotary selector with discrete positions has role `switch` and physical type `rotary selector`.
- A slide switch with discrete positions has role `switch` and physical type `slide switch`.
- A pressable transport control has role `button` and physical type `button`.
- A step key used to trigger or select a step has role `button` and physical type `rectangular button`.
- An LED has role `indicator` and physical type `LED`.
- A screen has role `display` and physical type `screen`.
- A ribbon keyboard has role `keyboard` and physical type `ribbon`.

Do not call a control a “switch” only because the manual calls it a selector. Determine the physical type from diagrams, screenshots, or static photos when available.

## Core node fields
A Surface ARIA node may include:
- `node_id`: stable identifier for the node;
- `role`: semantic role;
- `name`: official or manual-derived name;
- `description`: short functional description;
- `region`: high-level area of the surface;
- `group`: related control group;
- `parent`: parent node in the surface model;
- `children`: nested nodes;
- `physical_type`: tangible form, such as rotary knob, button, slide switch, LED, display, ribbon, jack, or fader;
- `actions`: possible user actions;
- `possible_states`: states or values defined by the manual;
- `current_state`: current state, only when situated evidence is available;
- `properties`: role-specific semantic properties;
- `spatial_properties`: static spatial or tactile relations;
- `safety_notes`: warnings or precautions grounded in the manual;
- `source`: source used to support the node, such as manual page, screenshot, diagram, or static photo.

## Semantic roles
### `region`
A high-level physical or functional area of the instrument.

Use for:
- synthesizer section;
- sequencer section;
- mixer section;
- oscillator area;
- filter area;
- envelope area;
- LFO area;
- connection area;
- global menu area;
- performance area.

A `region` may contain groups, controls, indicators, displays, keyboards, or ports.

Typical fields:
- `name`
- `description`
- `children`
- `spatial_description`
- `landmarks`

### `group`
A collection of related controls inside a region.

Use for:
- oscillator controls;
- filter controls;
- envelope controls;
- LFO controls;
- transport controls;
- step-sequencer controls;
- drum-part controls;
- connection groups.

A `group` should help the user build a mental and tactile map of the interface.

Typical fields:
- `name`
- `description`
- `children`
- `ordering`
- `spatial_description`
- `navigation_hint`

### `slider`
A continuous or quasi-continuous value control.

Use for:
- rotary knobs;
- faders;
- continuous encoders;
- touch strips when used to control continuous values;
- pressure or expression controls when represented as continuous values.

Typical actions:
- turn clockwise;
- turn counterclockwise;
- slide up;
- slide down;
- slide left;
- slide right;
- increase;
- decrease.

Allowed properties:
- `valuemin`, if documented;
- `valuemax`, if documented;
- `possible_values`, if documented;
- `step_size`, if documented;
- `valuenow`, only when current state evidence is available;
- `valuetext`, only when current state evidence is available or when describing documented possible named values.

Do not report `valuenow` from a manual, static screenshot, or static panel photo alone.

### `button`
A pressable control used to trigger an action, select a function, start or stop a process, enter a mode, or select an item.

Use for:
- transport buttons;
- record buttons;
- play buttons;
- stop buttons;
- step buttons;
- part buttons;
- menu buttons;
- mode buttons;
- shift/function buttons.

Typical actions:
- press;
- hold;
- release;
- press again;
- press while holding another control.

Allowed states:
- `pressed`, only when current state evidence is available;
- `selected`, only when current state evidence is available;
- `active`, only when current state evidence is available;
- `possible_states`, when documented.

Not allowed:
- `valuenow`.

A button may have documented possible states, but its current state must not be inferred without situated evidence.

### `switch`
A control with two or more discrete positions.

Use for:
- toggle switches;
- slide switches;
- rotary selectors with discrete positions;
- multi-position selectors;
- waveform selectors;
- range selectors;
- mode selectors.

Typical actions:
- switch to;
- move to position;
- select;
- set to one of the available positions.

Allowed properties:
- `possible_values`, when documented;
- `position_count`, when documented;
- `valuetext`, only when the current position is known;
- `current_state`, only when situated evidence is available.

A manual may define the possible positions of a switch, but not its current position.

### `keyboard`
A playable input surface used to produce notes or performance gestures.

Use for:
- piano-style keys;
- ribbon keyboards;
- touch keyboards;
- pads when used as note input;
- capacitive note surfaces.

Typical actions:
- press;
- touch;
- slide;
- hold;
- play;
- trigger.

Allowed properties:
- `range`, if documented;
- `scale_mapping`, if documented;
- `possible_modes`, if documented;
- `current_touch_position`, only when situated evidence is available;
- `current_pitch`, only when situated evidence is available.

Current pitch, pressure, touch position, or gesture state requires situated evidence.

### `indicator`
A visual or tactile output element that communicates state.

Use for:
- LEDs;
- status lights;
- blinking indicators;
- colour indicators;
- activity indicators;
- meter lights.

Allowed properties:
- `possible_states`, when documented;
- `meaning`, when documented;
- `current_state`, only when situated evidence is available;
- `state_meaning`, when a current state is provided or observed.

Do not infer whether an indicator is lit, unlit, blinking, or changing colour from a manual, screenshot, or static panel photo alone.

### `display`
A screen or visual readout that presents text, graphics, parameters, menus, or status information.

Allowed properties:
- `possible_content`, if documented;
- `menu_structure`, if documented;
- `current_content`, only when situated evidence is available;
- `current_page`, only when situated evidence is available.

Do not claim to read the current display unless current display evidence is available.

### `port`
A physical connection point.

Use for:
- audio input;
- audio output;
- headphones;
- sync input;
- sync output;
- MIDI;
- USB;
- power input;
- control voltage input or output;
- pedal input.

Typical actions:
- connect;
- disconnect;
- route signal;
- synchronize;
- power.

Allowed properties:
- `signal_type`, if documented;
- `direction`, such as input or output;
- `connector_type`, if documented;
- `voltage_or_level`, if documented;
- `current_connection`, only when situated evidence is available.

Current cable connection requires situated evidence.

## Spatial and tactile properties
Surface ARIA nodes may include spatial and tactile properties when derived from static layout sources.

Allowed spatial properties include:
- `region`
- `group`
- `row`
- `column`
- `order_in_group`
- `above`
- `below`
- `left_of`
- `right_of`
- `next_to`
- `between`
- `aligned_with`
- `near`
- `landmark`
- `tactile_description`
- `navigation_hint`

These properties describe static layout, not current state.

Spatial properties should support non-visual navigation. They should not merely encode visual appearance.

Good spatial property example:

```json
{
  "role": "slider",
  "name": "Cutoff",
  "physical_type": "rotary knob",
  "group": "Filter",
  "below": "Peak",
  "tactile_description": "upper knob in a vertical pair"
}
```

Weak spatial property example:

```json
{
  "name": "Cutoff",
  "visual_description": "labelled CUTOFF in the diagram"
}
```

Printed labels may help identify a control in documentation, but they are not sufficient as non-visual landmarks.

## Hierarchy
A surface model should be organized hierarchically.

Preferred hierarchy:

- regions contain groups;
- groups contain controls, indicators, displays, keyboards, or ports;
- controls may have associated indicators;
- procedures may refer to multiple nodes.

Example:
```json
{
  "role": "region",
  "name": "Filter section",
  "children": [
    {
      "role": "slider",
      "name": "Cutoff",
      "physical_type": "rotary knob"
    },
    {
      "role": "slider",
      "name": "Resonance",
      "physical_type": "rotary knob"
    }
  ]
}
```

## Possible state vs current state
Always distinguish possible state from current state.

Possible state:
- defined by the manual;
- can be explained from declarative knowledge;
- does not require live evidence.

Current state:
- describes what is happening now;
- requires situated evidence;
- must not be inferred from static sources alone.

Example:
A manual may state that a record LED blinks in record-ready mode.

This supports the possible-state statement:
> “If the REC LED is blinking, the device may be in record-ready mode, according to the manual.”

It does not support the current-state statement:
> “The REC LED is blinking now.”

## Semantic translation examples
### Rotary knob controlling a continuous parameter
Raw source information:
- Manual label: Cutoff
- Function: adjusts filter cutoff frequency
- Physical evidence: round rotary control
- Layout: part of filter section

Surface ARIA representation:
```json
{
  "role": "slider",
  "name": "Cutoff",
  "physical_type": "rotary knob",
  "group": "Filter",
  "description": "Adjusts filter cutoff frequency",
  "possible_states": "continuous value",
  "current_state": "requires situated evidence"
}
```

### Pressable transport control
Raw source information:
- Manual label: Play
- Function: starts or stops playback
- Physical evidence: pressable button

Surface ARIA representation:
```json
{
  "role": "button",
  "name": "Play",
  "physical_type": "button",
  "description": "Starts or stops playback",
  "possible_states": "pressed or not pressed, if documented",
  "current_state": "requires situated evidence"
}
```

### Multi-position selector

Raw source information:
- Manual label: Wave
- Function: selects one of several waveforms
- Physical evidence: discrete-position selector

Surface ARIA representation:
```json
{
  "role": "switch",
  "name": "Wave",
  "physical_type": "multi-position selector",
  "description": "Selects waveform",
  "possible_values": ["value names if documented"],
  "current_state": "requires situated evidence"
}
```

### LED indicator
Raw source information:
- Manual label: REC LED
- Function: indicates recording or record-ready state
- Physical evidence: LED

Surface ARIA representation:
```json
{
  "role": "indicator",
  "name": "REC LED",
  "physical_type": "LED",
  "possible_states": ["lit", "unlit", "blinking if documented"],
  "current_state": "requires situated evidence"
}
```

## Validity rules
- Use official names from the device manual when available.
- Use screenshots, diagrams, and static photos to confirm physical type and spatial layout when available.
- Use `region` and `group` to support structured navigation.
- Use `slider` for continuous or quasi-continuous value controls.
- Use `button` for pressable controls.
- Use `switch` for discrete-position controls.
- Use `keyboard` for playable note or gesture surfaces.
- Use `indicator` for LEDs and status lights.
- Use `display` for screens and visual readouts.
- Use `port` for connection points.
- Always distinguish semantic role from physical type.
- Do not assign `valuenow` to a `button`.
- Do not expose current state properties without situated evidence.
- Do not infer physical type from ambiguous manual wording alone.
- Do not treat printed labels or colours as sufficient non-visual landmarks.
- If a role-state or role-property mapping is invalid, explain why and propose a valid mapping.
- If physical type or layout is uncertain, state the uncertainty rather than inventing a precise description.

## Response guidance
When answering semantic questions, prefer this structure:

1. Identify the role.
2. Identify the physical type, if known.
3. Explain why that role fits.
4. List valid states or properties.
5. State whether current-state evidence would be required.
6. Add spatial or tactile properties if supported by static layout sources.

Example:
> A cutoff knob should be represented as a `slider`, because it controls a continuous parameter. Its physical type is a rotary knob. It may define possible minimum and maximum values if documented. Its current `valuenow` requires situated evidence and cannot be inferred from the manual or a static panel image alone.