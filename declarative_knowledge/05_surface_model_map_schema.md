# Surface Model and Map Schema

## Purpose
This store defines a device-agnostic schema for linking semantic knowledge to the physical surface of a musical instrument.

A Surface Reader uses two coupled representations:
- **Surface model**: the semantic structure of the interface.
- **Surface map**: the spatial and tactile organization of the interface.

The surface model describes what controls, regions, indicators, displays, and ports exist, what they mean, and how they are semantically related.

The surface map describes where those elements are located on the physical surface and how they can be found non-visually.

Together, they allow the Surface Reader to translate manuals, screenshots, diagrams, and static panel photos into structured, tactile-first guidance.

## Construction pipeline
When answering a device-specific question, the Surface Reader should build a temporary working representation from the available static sources.

Use this pipeline:
1. **Source extraction**  
   Extract official names, labels, functions, procedures, possible states, warnings, section headings, and terminology from the device manual.
2. **Static layout extraction**  
   Use screenshots, diagrams, visual indexes, and static panel photos to identify physical control types, regions, grouping, approximate position, ordering, and spatial relationships.
3. **Semantic typing**  
   Use the Surface ARIA Store to assign each extracted element a semantic role, such as `region`, `group`, `slider`, `button`, `switch`, `indicator`, `display`, `keyboard`, or `port`.
4. **Surface model construction**  
   Organize the semantically typed elements into a hierarchy of regions, groups, controls, indicators, displays, keyboards, and ports.
5. **Surface map construction**  
   Link semantic nodes to spatial and tactile properties, such as row, column, adjacency, vertical pair, repeated row, tactile landmark, or navigation hint.
6. **Non-visual guidance**  
   Use the Interaction Guidance Store and Mode Policy Store to convert the model/map information into an appropriate response.

Do not skip semantic typing. Manual-derived and screenshot-derived information should first be translated into Surface ARIA roles before being used for explanation or navigation.

## Relationship with the Surface ARIA Store
The Surface ARIA Store is the semantic vocabulary for the surface model.

Manuals and images may provide raw information, such as:
- a printed label;
- a diagrammed section;
- a control shape;
- a documented function;
- a possible LED state;
- a visual grouping;
- a spatial relation.

The Surface ARIA Store determines how this raw information should be represented as semantic nodes.

For example:
- a rotary knob controlling a continuous parameter should normally become a `slider`;
- a pressable control should normally become a `button`;
- a discrete-position selector should normally become a `switch`;
- an LED should normally become an `indicator`;
- a screen should normally become a `display`;
- a physical input/output connector should normally become a `port`;
- a section of related controls should normally become a `region` or `group`.

The Surface Model and Map Schema then links these semantic nodes to physical layout and non-visual navigation.

The correct order is:
1. identify information from manual/static sources;
2. assign Surface ARIA roles and properties;
3. place the semantic nodes in a surface model;
4. anchor them in a surface map;
5. produce tactile-first guidance.

## Surface model
The surface model is a semantic representation of the device interface.

It is built by translating device documentation and static visual references into the roles, names, relationships, possible states, and properties defined in the Surface ARIA Store.

The surface model answers questions such as:
- What controls exist?
- What are they called?
- What role do they have?
- What do they do?
- Which region or group do they belong to?
- What possible states or values are documented?
- Which properties require situated evidence?

The surface model does not simply describe the panel visually. It turns documentation into a structured, non-visual representation that can be navigated and queried.

## Surface map
The surface map links surface-model nodes to the physical layout.

It is built from static layout evidence such as manual diagrams, screenshots, visual page indexes, and panel photos.

The surface map answers questions such as:
- Where is the control?
- What physical type is it?
- Which region is it in?
- What is above, below, left, or right of it?
- Is it part of a row, column, pair, repeated pattern, or group?
- What tactile landmark can help the user find it?

The surface map should use the spatial and tactile properties defined in the Surface ARIA Store.

The surface map must not infer current state. It describes where controls are and how they are arranged, not what they are currently doing.

## Coordinate frame
Describe the surface from the performer’s perspective.

Use:
- **top**: farthest from the performer;
- **bottom**: closest to the performer;
- **left**: performer’s left;
- **right**: performer’s right.

Do not switch perspective during a response.

Avoid ambiguous terms such as “front,” “back,” “near side,” or “far side” unless they are explicitly defined for the device.

## Surface model node fields
A surface model node may include:
- `node_id`: stable identifier;
- `role`: semantic role from the Surface ARIA Store;
- `name`: official or manual-derived name;
- `description`: short function or purpose;
- `region`: high-level area of the device;
- `group`: functional or spatial group;
- `parent`: parent node;
- `children`: nested nodes;
- `physical_type`: knob, button, switch, fader, jack, LED, display, ribbon, etc.;
- `actions`: possible actions;
- `possible_states`: states or values defined by the manual;
- `current_state`: current state, only when situated evidence is available;
- `safety_notes`: manual-grounded warnings;
- `source`: manual page, screenshot, diagram, or other static source.

## Surface map fields
A surface map entry may include:
- `node_id`: link to the corresponding surface model node;
- `region`: physical area of the device;
- `group`: local group of related controls;
- `approximate_position`: top-left, upper-middle, lower-right, etc.;
- `row`: approximate row if meaningful;
- `column`: approximate column if meaningful;
- `ordering`: position in a sequence or group;
- `neighbours`: nearby controls;
- `landmarks`: stable tactile or spatial references;
- `physical_shape`: round knob, small button, long ribbon, jack, etc.;
- `spatial_description`: natural-language location description;
- `tactile_description`: non-visual description of the control or group;
- `navigation_hint`: tactile-first path to reach the control;
- `source`: static source supporting the spatial description.

## Regions
A region is a high-level physical or functional area.

Examples:
- synthesizer section;
- sequencer section;
- transport section;
- mixer section;
- oscillator section;
- filter section;
- envelope section;
- LFO section;
- connection area;
- global menu area;
- keyboard or performance area.

Regions should be used to reduce cognitive load.

Instead of describing every control separately, first identify the relevant region, then guide the user within it.

A good region description includes:
- its purpose;
- its approximate location;
- major groups inside it;
- useful tactile landmarks;
- how it relates to neighbouring regions.

## Groups
A group is a collection of related controls inside a region.

Examples:
- oscillator group;
- filter group;
- envelope group;
- LFO group;
- transport group;
- step-sequencer group;
- drum-part group;
- connection group.

Groups should support mental-map building.

A good group description includes:
- what the group is for;
- how many main controls it contains, if known;
- how the controls are arranged;
- which control is a useful landmark;
- how the group can be found from a stable tactile reference.

## Controls
A control is an interactive physical element.

Examples:
- knob;
- button;
- switch;
- fader;
- encoder;
- ribbon;
- pad;
- key;
- jack.

For each control, distinguish:
- **identity**: what the control is called;
- **semantic role**: what role it has according to the Surface ARIA Store;
- **physical type**: what tangible form it has;
- **function**: what the control does;
- **location**: where the control is;
- **possible state**: what states it may have;
- **current state**: what state it is in now.

Current state requires situated evidence.

## Physical type extraction
Do not infer physical type from manual wording alone when the wording is ambiguous.

Examples:
- “selector” may be a rotary selector, slide switch, toggle switch, or another discrete control.
- “control” may be a knob, button, switch, fader, encoder, ribbon, or touch surface.
- “key” may refer to a musical key, a button, a keyboard note, or a menu key.

Use screenshots, diagrams, static panel photos, and visual indexes to confirm physical type when available.

If physical type remains uncertain, state uncertainty and avoid precise tactile instructions based on an assumed shape.

Bad:
> The OCTAVE switch is below the WAVE switch.

Better:
> The manual identifies OCTAVE as a selector. Its exact physical form should be confirmed from the panel diagram or static photo before giving precise tactile guidance.

## Indicators and displays

Indicators and displays communicate state visually or tactually.

Examples:
- LEDs;
- status lights;
- blinking indicators;
- screens;
- small displays;
- meters.

A static source may describe:
- where the indicator is;
- what possible states mean;
- what the display may show;
- which menu or setting uses it.

A static source cannot determine:
- whether an indicator is currently lit;
- whether it is currently blinking;
- what colour it currently has;
- what the display currently shows.

## Spatial relationships

Use spatial relationships to support navigation.

Useful relations include:
- above;
- below;
- left of;
- right of;
- next to;
- between;
- first in row;
- last in row;
- upper control in a pair;
- lower control in a pair;
- nearest repeated control;
- aligned with;
- grouped with;
- closer to the left edge;
- closer to the right edge;
- above a row;
- below a row.

When possible, combine spatial relationship with physical type and group.

Better:
> The target is the upper rotary knob in a vertical filter pair.

Weaker:
> The target is above the other control.

Avoid broad or misleading landmarks.

For example, if a control is not directly above the keyboard, do not say “directly above the keyboard” merely because it is somewhere in the upper half of the panel.

## Tactile landmarks
A tactile landmark is a stable feature that can help the user orient on the device.

Good tactile landmarks may include:
- panel edges;
- corners;
- large knobs;
- repeated rows of buttons;
- recessed areas;
- raised or separated sections;
- jacks along an edge;
- keyboard or ribbon area;
- transport cluster;
- large gaps between groups;
- vertical or horizontal pairs of controls.

Avoid landmarks that require vision only, such as printed labels or colours.

If a landmark is visually documented but may not be tactilely distinguishable, state this limitation.

## Navigation hints
A navigation hint should be short and actionable.

Recommended structure:
1. start from a stable landmark;
2. move in a clear direction;
3. identify the target physical type;
4. confirm using nearby controls or group structure.

Example pattern:
> Start from the lower edge. Move to the row of small buttons. The target is the second button from the left, next to the transport button.

Navigation hints should not rely only on printed labels or visual markings.

## Static map vs live map
A static surface map can be derived from:
- user manuals;
- manual screenshots;
- diagrams;
- visual page indexes;
- static panel photos;
- documented layouts.

A live surface map requires situated evidence, such as:
- camera input;
- hand tracking;
- touch detection;
- live display reading;
- current LED reading;
- user interaction history.

Do not claim that the map has been updated from live evidence unless such evidence is available.

## Avoiding layout hallucinations
When location or physical type is uncertain:
- do not invent precise directions;
- do not assume that a textual “selector” is physically a switch;
- do not use a broad landmark if it may mislead the user;
- prefer group-level guidance over false precision;
- mention uncertainty when needed;
- use screenshots or static photos to confirm physical type and spatial relation.

Bad:
> RHYTHM is the next knob to the right of TEMPO.

Better:
> Use the static panel layout to determine whether RHYTHM is above, right of, or otherwise near TEMPO before giving a correction.

Bad:
> The target is directly above the ribbon keyboard.

Better:
> The target is in the upper-middle control area. Use the relevant control group as the main landmark if the direct path from the keyboard is not clear.

## Surface-map uncertainty
When layout information is incomplete or ambiguous:
- state the uncertainty;
- use approximate spatial descriptions;
- avoid over-precise claims;
- prefer group-level guidance;
- suggest a safer orientation strategy.

Example:
> The manual indicates that this control is in the sequencer section, but the exact tactile relationship is not fully specified. Use the step-button row as the main landmark.

## Example surface model fragment
```json
{
  "node_id": "filter_region",
  "role": "region",
  "name": "Filter section",
  "children": [
    {
      "node_id": "filter_cutoff",
      "role": "slider",
      "name": "Cutoff",
      "physical_type": "rotary knob",
      "description": "Adjusts filter cutoff frequency",
      "possible_states": "continuous value",
      "current_state": "requires situated evidence"
    },
    {
      "node_id": "filter_resonance",
      "role": "slider",
      "name": "Resonance",
      "physical_type": "rotary knob",
      "description": "Adjusts filter resonance",
      "possible_states": "continuous value",
      "current_state": "requires situated evidence"
    }
  ]
}
```

## Example surface map fragment
```json
{
  "node_id": "filter_cutoff",
  "region": "Filter section",
  "approximate_position": "upper-middle panel",
  "physical_shape": "rotary knob",
  "neighbours": {
    "below": "filter_resonance"
  },
  "tactile_description": "upper knob in a vertical filter pair",
  "navigation_hint": "Find the filter group. Cutoff is the upper knob in the pair; Resonance is below it."
}
```

## Good mapping pattern
When giving location guidance, prefer this reasoning pattern:
1. Identify the official control name from the manual.
2. Identify its function from the manual.
3. Assign the semantic role using the Surface ARIA Store.
4. Confirm physical type using screenshots, diagrams, or static panel photos.
5. Identify region and group.
6. Identify nearby controls and spatial relations.
7. Produce a tactile-first navigation hint.

Example:
> The manual identifies Cutoff as a filter control. Semantically, it is a `slider` because it controls a continuous value. The panel diagram shows it as a rotary knob in the filter group. For navigation, describe it as the upper knob in the vertical filter pair, with Peak below it.

## Validity rules
- Use official names from the manual when available.
- Use the Surface ARIA Store for semantic roles.
- Translate manual-derived and screenshot-derived information into Surface ARIA roles before using it for explanation or navigation.
- Do not treat visual grouping as sufficient: convert visual layout into semantic regions, groups, controls, indicators, displays, keyboards, and ports.
- Use screenshots, diagrams, and static photos to confirm physical type and spatial layout when available.
- Use the Interaction Guidance Store for tactile-first descriptions.
- Use static sources only for static layout.
- Do not infer current physical state from static layout.
- Do not over-specify uncertain positions.
- Prefer stable tactile landmarks over printed labels or colours.
- Distinguish location, semantic role, physical type, function, possible state, and current state.
- If the model cannot determine a precise tactile relation, state uncertainty instead of inventing one.