# Product Management Agent Skills

A local collection of product-management skills for turning strategic intent into
well-scoped, launch-ready product work. Each skill lives in `.agents/<skill-name>`
and contains its instructions, optional OpenAI agent metadata, and supporting
references.

## Skills by category

### Strategy

| Skill | Use it to |
| --- | --- |
| `product-direction` | Establish durable, falsifiable product intent, strategic choices, measures, and review triggers. |
| `wardley-strategy` | Map a strategic landscape, its value chain, evolution, risks, and context-specific plays. |
| `portfolio-prioritization` | Decide which opportunities to pursue now, sequence, hold, discover, or stop. |

### Research

| Skill | Use it to |
| --- | --- |
| `market-research` | Build evidence-backed context on segments, alternatives, competitors, and market forces. |

### Problem and solution shaping

| Skill | Use it to |
| --- | --- |
| `problem-framing` | Define a user need, outcomes, evidence, uncertainty, boundaries, and decision recommendation. |
| `solution-shaping` | Bound a solution's scope, components, risks, measures, and sequencing before implementation. |
| `breadboarding` | Map the workflow states, transitions, exceptions, and technical handoffs. |
| `ascii-ui-exploration` | Compare interface structures and information/action hierarchy before visual design or implementation. |

### Launch

| Skill | Use it to |
| --- | --- |
| `product-launching` | Plan rollout, enablement, documentation, readiness, and success measurement. |

## How the skills work together

The default lifecycle is:

`product-direction` → optional `market-research` / `wardley-strategy` →
`portfolio-prioritization` → `problem-framing` → `solution-shaping` →
`breadboarding` / optional `ascii-ui-exploration` → `product-launching`.

This is a decision flow, not a mandatory linear process. Research and mapping can
run whenever material uncertainty appears; portfolio work needs comparable
opportunities; and launch work builds on an established solution rather than
redefining it.

## Outputs and operating rules

[`AGENTS.md`](AGENTS.md) is the shared contract for agents working in this
repository. It defines the lifecycle, handoff expectations, artifact rules, and
how to resolve persistent output paths. `.agents/output-locations.yaml` is the
canonical path registry; its `output_root` lets a consuming project relocate all
generated artifacts together.

The skills are source material for an agent-enabled product repository. They do
not include an application, implementation code, or generated product artifacts.
