---
name: problem-framing
description: Use when a strategic play or product opportunity needs a prioritization-ready framing artifact before discovery or solution shaping. Clarifies the user problem, strategic outcome hypothesis, evidence, boundaries, and expected value without locking into a solution.
metadata:
  short-description: Frame user needs before shaping solutions
---

# Problem Framing

Use this skill when a strategic play needs to become a comparable product opportunity, or when a product problem needs enough context to enter a transparent portfolio decision.

## When To Use

Use this skill when the user asks to:
- explore a user need, pain point, friction, or missed opportunity
- describe a gap between the current state and a better user outcome
- rank or compare problems by urgency, value, or pain
- write a brief that explains the need before solution design
- clarify who is struggling, why, how much it matters, and why the organization should care

Typical prompts include:
- "Let's frame this problem."
- "Write an opportunity brief for this strategic play."
- "I want to understand the user problem before designing the solution."
- "Help me define the gap and why it matters."

Do not use this skill when the user is already asking for:
- solution boundaries, components, or included/excluded scope
- UI layouts, wireframes, or detailed interaction options
- implementation plans, migrations, routes, schemas, or rollout tasks

Those belong to `solution-shaping`, `ascii-ui-exploration`, or implementation work.

## Core Rule

Stay at the problem level.

The framing artifact explains:
- whose need exists
- what gap exists today
- why the gap matters
- how painful or costly the gap is
- how life improves if the need is satisfied
- what positive organizational outcomes would likely follow if the user outcome is achieved

It must not prescribe the solution in detail.

## Workflow

1. Establish strategic context.
- Link the relevant product direction, Wardley map, strategic play, intended strategic outcome, and decision horizon when they exist.
- State why this problem is being considered now and what must become true for the play to succeed.
- State how the opportunity advances, tensions, or challenges the direction's strategic outcomes and boundaries.
- If the work has no strategic context, state that explicitly rather than inventing one.

2. Identify the user and the need.
- Name the primary user clearly.
- State the job they are trying to get done.
- Distinguish the need from any proposed feature.

3. Describe the current gap.
- Explain the current workflow, workaround, failure mode, or friction.
- Make the gap concrete and observable.
- If useful, use `breadboarding` to map the current workflow and where pain appears.
- When using `breadboarding`, prefer the flowchart-ready table artifact so broken screens, affordances, and transitions are explicit.

4. Assess pain and value.
- Capture qualitative pain: confusion, wasted time, missed trust, operational risk, lost revenue, etc.
- Estimate quantitative signals when available: frequency, reach, conversion loss, support load, time cost, churn risk, missed usage.
- Do not invent numbers. If data is unavailable, say so and use directional confidence.

5. Define the better user outcome.
- Describe what becomes easier, safer, faster, clearer, or more valuable for the user if the need is satisfied.
- Keep this outcome user-facing, not implementation-facing.

6. Define the organizational outcome and causal chain.
- Translate the user outcome into likely benefits for the organization.
- Examples: higher activation, better retention, more usage, fewer support contacts, stronger conversion, lower operational cost, clearer product differentiation, improved trust.
- Call out where the relationship is strong, weak, or still hypothetical.
- Make the chain visible: strategic play -> user outcome or behavior change -> organizational outcome.

7. Isolate the problem statements and opportunity boundary.
- Extract a short set of problem statements from the evidence.
- Prefer crisp statements over broad themes.
- State the target segment, triggering context, alternatives or workarounds, and what is explicitly outside this opportunity.

8. Surface uncertainty and evidence quality.
- List open questions, missing evidence, and assumptions.
- Say what would most change the priority or framing if learned.
- Include any uncertainty in outcome attribution.
- Separate direct evidence, internal signals, market inference, and assumptions. Record confidence without inventing precision.

9. End with a portfolio recommendation.
- State whether the opportunity should be prioritized now, sequenced next, held, discovered further, stopped, or returned to strategy.
- Capture strategic leverage, expected impact, urgency, confidence, material risk, and dependency considerations in a form that can be compared with other opportunities.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Create `product/initiatives/<initiative-id>/manifest.yaml` before writing `product/initiatives/<initiative-id>/framing.md`. The framing artifact is the required first file in an initiative folder; use [references/framing-template.md](references/framing-template.md).

## Scoring Guidance

When preparing an opportunity for comparison, use lightweight scoring if it helps:
- Pain severity: `1-5`
- Frequency: `1-5`
- Reach: `1-5`
- Confidence: `1-5`
- Strategic fit: `1-5`

Also capture, qualitatively or on a consistent scale, strategic leverage, urgency or time window, material risks, dependencies, and reversibility. Portfolio ranking belongs to `portfolio-prioritization`; do not make a portfolio decision from one brief alone.

Do not force scoring when the user only wants a narrative brief.

## Organizational Outcome Guidance

Do not stop at "the user would be happier."

Name the organizational value that would likely follow from the user outcome, such as:
- more successful activation
- improved conversion to paid usage
- better retention or repeat engagement
- lower support burden
- reduced manual operations
- improved data quality or operational reliability
- stronger competitive position

Keep attribution honest. If the connection is indirect or uncertain, say so.

## Breadboarding

Use `breadboarding` when the workflow itself is unclear or when the pain emerges across multiple steps.

In framing, breadboards should focus on:
- the user's current path
- where handoffs happen
- where friction, delay, confusion, or failure appears
- what components already exist and how they are broken or fragmented

Prefer the standard table format so the artifact can later translate into a flowchart.

Do not turn breadboards into screen design. That belongs later.

## Handoff

Recommend `portfolio-prioritization` when the framing artifact is clear on:
- the strategic play or decision context
- the linked direction and its relevant strategic outcome or boundary
- the user
- the need
- the gap
- why it matters
- what better user outcome is desired
- what organizational upside makes the problem worth solving
- evidence quality and the assumptions most likely to change the decision

Recommend `product-discovery` after the opportunity is selected and needs direct validation. Recommend `solution-shaping` only after discovery has validated the problem sufficiently for a bounded solution decision.
