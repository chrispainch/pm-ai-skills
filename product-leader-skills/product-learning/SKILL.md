---
name: product-learning
description: Use after a launch, experiment, or meaningful product change to assess outcomes, synthesize feedback, and decide whether to expand, iterate, pause, retire, or revise strategy. Closes the loop to problem framing, prioritization, market research, and Wardley strategy.
metadata:
  short-description: Turn product outcomes into next decisions
---

# Product Learning

Assess whether a released increment changed the intended user and organizational outcomes, then make the next decision explicit. Do not mistake activity metrics for evidence of value.

## Inputs

Use the linked product direction, opportunity brief, shaped solution, delivery specification, launch plan, expected measures, baselines, product data, qualitative feedback, support signals, and relevant market changes.

## Workflow

1. Restate the original outcome hypothesis and attribution assumptions.
2. Compare observed behavior and outcomes with the baseline and expected direction.
3. Separate data, user feedback, operational signals, and interpretation. Name material measurement gaps.
4. Identify learning about the problem, solution, segment, rollout, strategic assumptions, and product-direction assumptions.
5. Decide whether to expand, iterate, pause, retire, research further, re-prioritize, revisit strategy, or `reaffirm`, `refine`, or `challenge` product direction.
6. Route the learning to the artifact that needs updating rather than leaving it in a retrospective.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write each immutable outcome review to `product/initiatives/<initiative-id>/learning/<yyyy-mm-dd>-outcome-review.md` and add it to `manifest.yaml`, using [references/post-launch-review-template.md](references/post-launch-review-template.md). The decision and evidence should be durable enough to prevent rediscovering the same lesson.

## Handoff

Update `problem-framing` and `portfolio-prioritization` for initiative learning. Update `market-research` and `wardley-strategy` when the learning changes a segment assumption, market context, value chain, evolution view, or strategic play. Update `product-direction` when the learning materially reaffirms, refines, or challenges the direction's assumptions or strategic outcomes.
