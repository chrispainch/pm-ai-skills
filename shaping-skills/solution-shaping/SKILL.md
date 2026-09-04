---
name: solution-shaping
description: Use when a framed problem and active product direction need a bounded solution before implementation. Covers scope, included and excluded behaviors, components, key risks, success criteria, measurement, and sequencing without becoming a low-level build plan.
metadata:
  short-description: Define the shape of a solution
---

# Solution Shaping

Define a robust solution boundary without over-specifying the build. The result should make the proposal, direction constraints, components, risks, expected outcomes, and measures clear.

## Required Inputs

Use a framed problem and an active product direction. Carry forward the problem's user need, gap, outcomes, evidence, and boundaries; carry forward the direction's strategic outcomes, principles, boundaries, and tradeoffs. If either input is missing or the proposed shape cannot explain how it advances and respects the direction, do not treat the shape as ready.

## Workflow

1. Restate the framed problem's user need, gap, and intended outcomes, then identify the active direction constraints that govern the solution.
2. Define what the solution accomplishes and its included and excluded scope within those direction constraints.
3. Describe the high-level user or system flow.
4. Break the work into meaningful, testable components rather than technical layers.
5. For each component, state its purpose, supported outcome, risks, edge cases, dependencies, and delivery considerations.
6. Define qualitative and quantitative success measures, including measurement gaps.
7. Record unresolved decisions that could change scope or architecture, and any intentional tension with product direction with its rationale.

## Output

Read the [output-locations configuration](../../output-locations.yaml) before creating persistent files. Use `outputs.solution-shaping.primary` and [references/solution-shaping-template.md](references/solution-shaping-template.md).
