# Evaluation Rubrics
Two complementary rubrics were used:
-  **Operational responses**: answers to goal-oriented prompts asking which control or connector should be used, where it is located, and what it does.
- **Structured descriptions**: responses to minimal prompts asking the system to create a structured description of a given target.

Both rubrics use a 0–2 ordinal scale.

## Operational Response Evaluation
Operational prompts evaluate whether the system can transform declarative knowledge from the manual and static visual references into useful, non-visual, action-oriented guidance.

Example prompt (see operational_prompt_set.csv):
> Which control should I use to [achieve my goal]? Describe where it is and what it does.

Metrics:
- **M1**: Target resolution
    - 0 = Identifies the wrong target, or invents a non-existent one.
    - 1 = Identifies a nearby region, function, or alternative, but does not fully resolve the target.
    - 2 = Correctly identifies the requested target.
- **M2**: Manual-grounded correctness
    - 0 = Function, procedure, values, or warnings are incorrect or unsupported.
    - 1 = Mostly correct, but incomplete, ambiguous, or includes details not clearly grounded in the sources.
    - 2 = Function, procedure, possible states/settings, warnings, and alternatives are supported by the manual.
- **M3**: Localization correctness
    - 0 = Location is wrong or likely to lead to the wrong target.
    - 1 = Location is in the correct region but approximate, incomplete, or spatial relations are weak/confusing.
    - 2 = Location is correct with reliable region and spatial relations.
- **M4**: Visual dependency
    - 0 = Guidance depends on diagrams, numbering, printed labels, or colours.
    - 1 = Location is correct but not fully self-sufficient; it mainly relies on features that are not explained as tactile landmarks.
    - 2 = Guidance uses edges, rows, groups, tactile landmarks, above/below/left/right relations, physical sequences, or distinguishable controls.
- **M5**: Uncertainty, unsupported-feature, and safety handling
    - 0 = Invents states, absent features, or omits/contradicts relevant safety warnings in a potentially misleading way.
    - 1 = Does not clearly state limits, alternatives, current-state boundaries, or relevant manual-grounded safety cautions.
    - 2 = Clearly states limits and alternatives; when relevant, includes safety or operational cautions supported by the manual.

The operational score is computed as:
> Core Score = mean(M1, M2, M3, M4, M5)

---

## Structured Description Evaluation
Structured-description prompts evaluate whether the system can transform declarative knowledge into a structured, semantically meaningful, and navigable description of a target control, connector, or feature.

Example prompt (see structural_prompt_set.csv):
> Create a detailed description of the [control].

Metrics:
- **SD1**: Grounded content validity
    - 0 = Target is wrong, function is incorrect, a control is invented, or an absent feature is treated as documented.
    - 1 = Target is mostly correct, but the description is incomplete, ambiguous, or includes details not clearly supported by the sources.
    - 2 = Target, official name, function, possible settings, or documented absence are correct and grounded in the manual/static sources.
- **SD2**: Physical / semantic typing
    - 0 = Physical type or control category is absent or wrong.
    - 1 = Physical type or category is partially/generically described, or does not distinguish physical form from functional/semantic role.
    - 2 = Physical type and/or functional-semantic role are clearly distinguished.
- **SD3**: Spatial and relational description
    - 0 = Position is absent, wrong, or not useful.
    - 1 = Position is broadly correct but generic, or mainly based on control number/area without useful relations.
    - 2 = Position is described in detail with: group, nearby controls, and useful spatial relations.
- **SD4**: State boundary handling
    - 0 = Infers or suggests current state, actual value, LED/cable/setting state without evidence.
    - 1 = Does not invent current state, but does not clearly separate possible documented states/settings from current state.
    - 2 = Explicitly distinguishes documented possible states/settings from current state that cannot be inferred from static sources.
- **SD5**: Structured completeness
    - 0 = Response is poorly structured, confusing, or mainly narrative.
    - 1 = Some structure is present, but relevant elements are partial, implicit, or mixed together.
    - 2 = Description is clearly organized, separating function, location, physical/semantic type, actions, relations, and states/limits.


For structured-description prompts, three scores can be reported:
> Grounded Validity = SD1
> Structured Description Score = mean(SD2, SD3, SD4, SD5)
> Overall Structured Score = mean(SD1, SD2, SD3, SD4, SD5)

This separation is chosen because both configurations may be similarly strong in grounded factual content, while differing in how well they structure that content into semantic, spatial, and state-aware descriptions.


