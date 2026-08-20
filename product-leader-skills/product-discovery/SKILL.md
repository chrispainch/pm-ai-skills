---
name: product-discovery
description: Use when a prioritized, strategy-linked opportunity needs direct evidence about the user problem, assumptions, or solution hypotheses before solution shaping. Produces a decision to shape, reframe, re-prioritize, or stop; it is not a general market-research skill.
metadata:
  short-description: Validate selected product opportunities
---

# Product Discovery

Reduce uncertainty about a selected opportunity before committing to a solution. Start with the decision that needs to be made, not a method or a proposed feature.

## Inputs

Use a selected opportunity brief from `problem-framing` and `portfolio-prioritization`. Carry forward its linked product direction, strategic play, target segment, outcome hypothesis, evidence, and assumptions.

## Workflow

1. Define the decision and the assumptions that could most change it.
2. Choose proportionate research: existing data, interviews, observation, prototype tests, or other evidence appropriate to the uncertainty.
3. Keep problem evidence separate from solution evidence.
4. Synthesize findings by segment and context. Preserve counterevidence and exceptions.
5. Identify whether findings materially support, refine, or challenge the linked direction as well as the opportunity itself.
6. Decide whether the problem is validated enough to shape, needs reframing, needs more research, should be re-prioritized, should trigger a direction review, or should stop.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write the synthesis to `product/initiatives/<initiative-id>/discovery.md` and register it in `manifest.yaml`. Use [references/discovery-synthesis-template.md](references/discovery-synthesis-template.md); write initiative-specific source material under `product/initiatives/<initiative-id>/evidence/`.

## Handoff

Advance a validated opportunity to `solution-shaping`. Return changed or disproven opportunities to `problem-framing` and, when necessary, `portfolio-prioritization`. Send broad external-context questions to `market-research`.
