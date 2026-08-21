# Product Leader Skills

This collection turns product-direction and strategy-linked opportunities into validated, delivered, launched, and measured product increments.

Durable outputs follow the shared [Product Artifact Contract](../references/product-artifact-contract.md): each opportunity keeps a stable `product/initiatives/<initiative-id>/` folder from framing through learning.

## What This Collection Covers

The product-leadership loop turns durable direction and strategic plays into validated, delivered, launched, and measured product increments:

```text
product direction
  -> problem framing
  -> portfolio prioritization
  -> product discovery
  -> solution shaping
  -> workflow mapping and UI validation
  -> delivery specification
  -> launch planning
  -> product learning
```

They are designed to prevent common failure modes:

- jumping into UI before the problem is clear
- shaping a solution before the user need is well defined
- over-specifying implementation too early
- treating launch as an afterthought once code exists

## Collection Structure

Skills live directly in this collection.

- `product-direction/`
- `problem-framing/`
- `portfolio-prioritization/`
- `product-discovery/`
- `breadboarding/`
- `solution-shaping/`
- `ascii-ui-exploration/`
- `usability-validation/`
- `delivery-specification/`
- `product-launching/`
- `product-learning/`
- `initiative-reviewer/`

Each skill folder contains:

- `SKILL.md`: the machine-facing operating instructions
- `agents/openai.yaml`: skill wiring
- `references/`: templates and supporting docs

## Skill Index

### `product-direction`

Defines durable product purpose, desired future, strategic outcomes, boundaries, measures, assumptions, and review triggers. Market research, Wardley Strategy, and product learning may reaffirm, refine, or challenge it.

### `problem-framing`

Translates a strategic play into an evidence-rated, prioritization-ready product opportunity.

Use it when the user is still asking:

- what problem is worth solving
- who is affected
- why it matters
- how painful it is
- whether the opportunity is worth pursuing

### `breadboarding`

Maps current-state or target-state workflows into a flowchart-ready table.

Use it when the main ambiguity is the shape of the workflow:

- screens or states
- affordances
- transitions
- technical handoffs
- broken or missing steps

### `solution-shaping`

Defines the bounded solution before implementation starts.

Use it to document:

- in-scope and out-of-scope behavior
- major components
- risks and constraints
- success criteria
- measurement approach

### `ascii-ui-exploration`

Explores interface options in text after the solution is already shaped.

Use it when the remaining question is:

- hierarchy
- grouping
- action placement
- layout direction
- interaction emphasis

### `product-launching`

Prepares rollout, documentation, enablement, and success measurement for a shaped solution.

Use it when the feature or product direction is defined and the work now needs:

- launch briefs
- rollout phases
- support readiness
- help-doc updates
- launch metrics

### `portfolio-prioritization`

Compares opportunity briefs and records which bets to pursue, sequence, hold, discover further, or stop.

### `product-discovery`

Tests the critical assumptions behind a selected opportunity before solution commitment.

### `usability-validation`

Tests whether users can complete important shaped tasks before broad release.

### `delivery-specification`

Creates an implementation-ready behavioral handoff with acceptance criteria, non-functional requirements, instrumentation, and release conditions.

### `product-learning`

Assesses post-launch evidence and routes the resulting decision back to framing, prioritization, market research, or strategy.

### `initiative-reviewer`

Runs the artifact validator and reviews whether an initiative has the evidence and decisions required to support its current status.

## Working Conventions

- Stay at the right altitude for the current phase.
- Use problem artifacts to justify solution work.
- Use flow artifacts to clarify transitions and component boundaries.
- Keep UI exploration focused on hierarchy, not strategy reset.
- Tie launch work back to the intended user and organizational outcomes.

## Typical Usage Pattern

1. Define or revise durable product direction.
2. Use market research and Wardley Strategy to test direction and identify strategic plays.
3. Turn an aligned play into an opportunity brief, then select and validate the opportunity.
4. Shape, map, explore, validate, and deliver the experience.
5. Launch deliberately, assess outcomes, and reaffirm, refine, or challenge direction as evidence warrants.
