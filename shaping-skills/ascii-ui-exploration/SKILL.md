---
name: ascii-ui-exploration
description: Use when a product decision is clear and the remaining ambiguity is interface structure, information hierarchy, action hierarchy, interaction patterns, or layout options. Produces comparable ASCII concepts and a recommendation before implementation.
metadata:
  short-description: Explore UI options with ASCII concepts
---

# ASCII UI Exploration

Explore interface structure without reopening the product decision. Focus on what users notice first, what action is primary, and the tradeoffs between genuinely distinct layouts.

## Inputs

Use the user goal, the UI decision to explore, and any established constraints. A solution shape or flow can provide useful context when available; it is not a required handoff. If a layout option conflicts with an established product constraint, surface the conflict rather than resolving it through the interface.

## Workflow

1. Restate the user goal, component or page, and constraints that should remain unchanged.
2. Identify the UI decision to make.
3. State the primary, secondary, and peripheral information and actions.
4. Produce structurally distinct ASCII options when there is a meaningful layout choice. When there is one credible direction, show one focused exploration and explain why alternatives would not be useful.
5. Explain each option’s strengths, weaknesses, and behavior it supports.
6. Recommend a direction and refine it after selection.
7. Note mobile collapse or stacking behavior when relevant.

## Output

Use [references/ascii-ui-template.md](references/ascii-ui-template.md) when it helps the discussion. For a persistent record, read the [output-locations configuration](../../output-locations.yaml) and use `outputs.ascii-ui-exploration.primary`; persistence is optional.
