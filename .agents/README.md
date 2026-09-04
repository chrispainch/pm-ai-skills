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

The skills support a product-management spiral: start broad, make strategic
choices, turn those choices into a portfolio of problems, then repeatedly narrow
the loop as evidence and delivered products make the next practical decision
clearer.

1. **Understand the market** with `market-research`: its participants, needs,
   alternatives, forces, and evidence gaps.
2. **Form a strategic point of view** with `product-direction` and, when useful,
   `wardley-strategy`: which needs to serve, how to create traction, and which
   strategic or business-model choices to make.
3. **Choose and frame problems** with `portfolio-prioritization` and
   `problem-framing`, using that strategic frame to decide which user or business
   problems merit attention.
4. **Shape and communicate solutions** with `solution-shaping`, `breadboarding`,
   and optional `ascii-ui-exploration`; then use `product-launching` to make the
   go-to-market plan and success measures explicit.
5. **Learn and spiral inward** from market results, product signals, and user
   journeys. New loops can address a new product line or feature; later loops
   address smaller, more practical, and eventually optimization-level problems.

The sequence is directional rather than a gate. Product work should revisit
market understanding and strategy whenever outcomes challenge them, while each
successful loop augments the value a product provides across its users' journeys.

## Outputs and operating rules

[`AGENTS.md`](AGENTS.md) is the shared contract for agents working in this
repository. It defines the lifecycle, handoff expectations, artifact rules, and
how to resolve persistent output paths. `.agents/output-locations.yaml` is the
canonical path registry; its `output_root` lets a consuming project relocate all
generated artifacts together.

The skills are source material for an agent-enabled product repository. They do
not include an application, implementation code, or generated product artifacts.
