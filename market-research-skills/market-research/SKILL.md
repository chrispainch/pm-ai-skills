---
name: market-research
description: Use when product or strategy work needs evidence-backed market context about segments, alternatives, competitors, category trends, pricing, regulation, or technology shifts. Produces reusable market intelligence; use product-discovery for initiative-specific user validation.
metadata:
  short-description: Build reusable market decision context
---

# Market Research

Build market context that improves a decision. Keep external observations, internal signals, and inferences distinguishable so the artifact remains useful after the immediate initiative.

## When To Use

Use this skill before or alongside Wardley mapping, when framing an opportunity, when a solution depends on market positioning or alternatives, or when launch audiences and timing need clarification.

Do not use it as a substitute for direct research into a selected user problem. That belongs to `product-discovery`.

## Workflow

1. Define the decision, the market boundary, and the linked product-direction assumptions the research can support or challenge.
2. Identify relevant segments, buyers, users, operators, and alternatives, including manual workarounds and doing nothing.
3. Gather only evidence material to that decision. Record source, date, evidence type, and confidence for every consequential claim.
4. Separate observations from interpretations. Do not turn a competitor feature inventory into a strategy recommendation without explaining the user or market implication.
5. Identify market, technology, distribution, pricing, regulatory, and ecosystem forces when they materially constrain the decision.
6. Assess the direction explicitly as `reaffirm`, `refine`, or `challenge`. State the disconfirming evidence sought, what would materially change the direction, and any review trigger.
7. State implications for Wardley mapping, problem framing, solution shaping, launch, and any research still required.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write reusable research to `product/strategy/market-research/<research-id>/brief.md` and its evidence ledger to `product/strategy/market-research/<research-id>/evidence-ledger.md`. Use [references/market-research-brief-template.md](references/market-research-brief-template.md) and [references/evidence-ledger-template.md](references/evidence-ledger-template.md).

## Handoff

- To `wardley-strategy`: candidate users and needs, alternatives, relevant value-chain signals, evolution clues, and uncertainties.
- To `problem-framing`: segment context, problem signals, alternatives, and strategic constraints.
- To `solution-shaping` or `product-launching`: positioning, market constraints, and audience implications.
- To `product-discovery`: questions that require direct user validation.
