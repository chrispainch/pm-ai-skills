---
name: breadboarding
description: Use when a UX workflow needs a flow map showing current screens or states, user affordances, transitions, involved components, and material technical constraints. Produces a flowchart-ready table rather than visual design.
metadata:
  short-description: Map UX flows into flowchart-ready tables
---

# Breadboarding

Map workflow topology, not visual styling. Make states, actions, transitions, handoffs, and constraints legible enough to expose gaps before implementation.

## Workflow

1. Define the user goal and the flow boundary.
2. Decide whether the map represents the current state, target state, or both.
3. List each screen or state, the affordance available there, the next state, interaction type, components, and technical notes.
4. Include empty, loading, error, permission, and recovery states when material.
5. Keep each transition explicit enough to translate into a flowchart.
6. Identify unclear rules, missing handoffs, and risks exposed by the flow.

## Output

Use [references/breadboarding-template.md](references/breadboarding-template.md). For a persistent record, read the [output-locations configuration](../../output-locations.yaml) and use `outputs.breadboarding.primary`.
