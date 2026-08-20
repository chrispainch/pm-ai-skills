# AI PM Skills
Where Christian Painchaud develops agentic skills for his own use.

This repository contains skill collections organized around practical workflows rather than generic prompts. Each collection lives in its own project folder and exposes one folder per skill.

The product-management factory combines product direction, standalone market research, Wardley strategy, and software-PM delivery skills. Its shared artifact loop is documented in [references/product-factory-loop.md](references/product-factory-loop.md), and all emitted product artifacts follow the [Product Artifact Contract](references/product-artifact-contract.md).

## Current Projects

### `software-pm-skills`

This collection turns strategy-linked opportunities into validated, delivered, launched, and measured product increments.

- `problem-framing`: turns a strategic play into an evidence-rated, prioritization-ready opportunity brief.
- `portfolio-prioritization`: compares opportunities and decides which bets to pursue, sequence, hold, discover further, or stop.
- `product-discovery`: validates the selected opportunity before solution commitment.
- `breadboarding`: maps current-state or target-state workflows into flowchart-ready tables that show screens, affordances, transitions, and technical constraints.
- `solution-shaping`: defines solution boundaries, components, scope, risks, and success criteria without dropping into implementation detail too early.
- `ascii-ui-exploration`: explores screen structure and interaction hierarchy with ASCII concepts once the solution is already shaped.
- `usability-validation`: tests whether users can complete important shaped tasks before broad release.
- `delivery-specification`: defines acceptance criteria, non-functional requirements, instrumentation, and release conditions.
- `product-launching`: prepares rollout briefs, documentation needs, phased launch plans, and success measurement.
- `product-learning`: turns post-launch evidence into an expand, iterate, pause, retire, or strategy-revision decision.
- `initiative-reviewer`: validates initiative artifacts and flags structural, evidence, decision, and readiness gaps.

At a high level, this project forms a workflow:
`frame -> prioritize -> discover -> shape -> validate -> deliver -> launch -> learn`.

### `market-research-skills`

This collection supplies reusable market intelligence for product and strategy decisions: segments, alternatives, competitors, category trends, constraints, and evidence quality.

- `market-research`: creates a source-backed market brief that can inform Wardley mapping, opportunity framing, solution positioning, launch, and post-launch learning.

### `product-direction-skills`

This collection defines the durable product purpose, desired future, strategic outcomes, boundaries, measures, and assumptions that downstream evidence must be allowed to reaffirm, refine, or challenge.

- `product-direction`: creates and revises the canonical product-direction artifact.

### `wardley-strategy-skills`

This collection is focused on structured strategy work using Wardley Maps. It helps turn vague strategic discussion into explicit user needs, mapped value chains, evolutionary positioning, doctrine gaps, climatic forces, inertia, and context-specific plays.

- `wardley-strategy`: structures strategy analysis around user needs, value chains, evolution, doctrine, climatic patterns, and strategic plays rather than generic planning language.

At a high level, this project forms a workflow:
`user needs -> value chain -> evolution -> patterns and inertia -> strategic plays`.

## Structure

Current top-level folders:

- `software-pm-skills/`
- `wardley-strategy-skills/`
- `market-research-skills/`
- `product-direction-skills/`

Within each collection, each skill folder contains:

```text
<skill-name>/SKILL.md
```

Each collection also includes a high-level `README.md` plus supporting templates and references inside its skill folders.

## Summary

The repository currently contains four active agentic skill projects:

1. A product-direction system that defines durable intent and strategic boundaries.
2. A standalone market-research system that supplies reusable evidence about markets, segments, alternatives, and constraints.
3. A software/PM system centered on product opportunity selection, validation, solution definition, delivery, launch, and learning.
4. A Wardley strategy system centered on user needs, value-chain mapping, evolutionary analysis, and strategic gameplay.
