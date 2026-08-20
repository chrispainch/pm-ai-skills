---
name: portfolio-prioritization
description: Use when several strategy-linked product opportunities need a transparent pursue-now, sequence, hold, or stop decision. Compares prioritization-ready opportunity briefs against strategic leverage, expected impact, confidence, urgency, risk, dependencies, and capacity.
metadata:
  short-description: Select and sequence product opportunities
---

# Portfolio Prioritization

Select the next product bets from comparable opportunity briefs. This skill makes a portfolio decision; it does not invent evidence or prescribe a solution.

## Inputs

Require the linked product direction, a strategic objective or Wardley strategic play, an opportunity brief from `problem-framing`, and any material capacity or dependency constraints. If the opportunity cannot explain its evidence, intended outcome, or direction alignment, return it to framing or discovery.

## Workflow

1. Define the decision horizon, available capacity, and non-negotiable constraints.
2. Compare opportunities using a consistent qualitative or numeric scale only where it improves the decision.
3. Evaluate direction alignment or tension, strategic leverage, expected user and organizational impact, confidence, urgency or window, effort or risk, dependencies, and reversibility.
4. Separate evidence from judgement. Do not imply false precision.
5. Decide whether each opportunity is `now`, `next`, `hold`, `discover`, `stop`, or `return to strategy`.
6. Record tradeoffs, deferred work, decision owner, and review trigger.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write the time-bounded portfolio decision to `product/strategy/portfolio/<yyyy>-<quarter>.md`, using [references/prioritization-template.md](references/prioritization-template.md). The output is an ordered decision record, not a feature backlog.

## Handoff

Advance selected opportunities to `product-discovery`. Send insufficiently supported opportunities to `problem-framing` or `market-research`; send strategy conflicts to `wardley-strategy`.
