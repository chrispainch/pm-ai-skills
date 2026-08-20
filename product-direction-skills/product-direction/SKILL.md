---
name: product-direction
description: Use when a product, domain, or portfolio needs a durable strategic intent that guides downstream choices and can be reaffirmed, refined, or challenged by evidence. Defines purpose, desired future, strategic outcomes, boundaries, principles, measures, assumptions, and review triggers; it is not a roadmap.
metadata:
  short-description: Define durable product direction
---

# Product Direction

Create a durable, falsifiable decision frame. Direction states what the product exists to change and the strategic choices it will make; it must remain open to revision when market, landscape, or outcome evidence challenges its assumptions.

## When To Use

Use this skill when establishing a product or domain strategy, when strategic intent is scattered across planning artifacts, or when accumulated evidence requires a direction review.

Do not use it to select a quarterly portfolio, define a feature, or restate a roadmap. Those belong to `portfolio-prioritization` and downstream product skills.

## Workflow

1. Establish scope, time horizon, owner, and the organizational context the product direction serves.
2. State the product purpose and desired future in user and system terms, not feature terms.
3. Define target users, buyers, and explicit non-targets.
4. Define a small set of strategic outcomes, product principles, boundaries, and material tradeoffs.
5. Identify outcome measures and guardrails without forcing a single north-star metric when one would mislead.
6. Record the assumptions that must hold, disconfirming signals, and review triggers that could require direction to be reaffirmed, refined, or challenged.
7. Link the relevant market research, Wardley maps, and portfolio decisions. Do not claim those artifacts validate the direction unless their evidence supports that conclusion.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write the living direction artifact to `product/strategy/direction/product-direction.md`, using [references/product-direction-template.md](references/product-direction-template.md).

## Handoff

- To `market-research`: research questions and direction assumptions to test, including disconfirming evidence.
- To `wardley-strategy`: desired future, strategic outcomes, boundaries, and the assumptions a landscape assessment must challenge.
- To `portfolio-prioritization` and `problem-framing`: decision rules, strategic outcomes, and explicit tensions.
- From `product-learning`: revise the direction only when the evidence warrants `reaffirm`, `refine`, or `challenge` at the strategic level.
