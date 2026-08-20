# Product Factory Loop

Product direction is the durable, falsifiable intent. Market research and Wardley Strategy test that intent as well as informing it; the product loop turns an aligned strategic play into a measured decision and returns learning to the appropriate layer.

```text
PRODUCT DIRECTION (living strategic intent)
  outputs: product/strategy/direction/product-direction.md
       │                    │                    │
       │                    │                    └──→ problem framing and portfolio prioritization
       │                    └─────────────────────→ Wardley strategy
       └──────────────────────────────────────────→ market research

MARKET RESEARCH (continuous, reusable evidence)
  outputs: product/strategy/market-research/<research-id>/{brief.md,evidence-ledger.md}
       │          │                    │                  │
       │          │                    │                  └──→ product launching
       │          │                    └─────────────────────→ solution shaping
       │          └──────────────────────────────────────────→ problem framing
       └─────────────────────────────────────────────────────→ Wardley strategy

WARDLEY STRATEGY (per product, domain, or landscape)
  input: product direction, market research, and internal context
  outputs: product/strategy/wardley/<domain-id>/map.yaml and optional review.md
       │
       ▼
PROBLEM FRAMING (per candidate opportunity)
  input: product direction, strategic play, outcome intent, and relevant evidence
  output: product/initiatives/<initiative-id>/{manifest.yaml,framing.md}
       │
       ▼
PORTFOLIO PRIORITIZATION (across opportunity briefs)
  input: comparable opportunities, capacity, dependencies, and timing
  output: product/strategy/portfolio/<yyyy>-<quarter>.md
       │
       ▼  selected opportunity
PRODUCT DISCOVERY
  input: selected opportunity and its critical assumptions
  output: product/initiatives/<initiative-id>/discovery.md plus evidence/
       │                         │
       │                         ├──────────────→ problem framing
       │                         └──────────────→ portfolio prioritization
       ▼  validated problem
SOLUTION SHAPING
  input: validated problem, strategic constraints, and priority boundary
  output: product/initiatives/<initiative-id>/solution.md
       │
       ▼  as needed for the work
BREADBOARDING → ASCII UI EXPLORATION → USABILITY VALIDATION
  outputs: flow.md, ui-exploration.md, and usability-validation.md when used
       │                         │
       │                         └──────────────→ breadboarding / UI exploration / solution shaping
       ▼  stable behavior and UX rules
DELIVERY SPECIFICATION
  input: solution shape, flow/UI artifacts, usability findings, launch constraints
  output: product/initiatives/<initiative-id>/delivery-specification.md
       │
       ▼
IMPLEMENTATION
  output: tested product increment and operational documentation
       │
       ▼
PRODUCT LAUNCHING
  input: implemented increment, market context, audience, rollout constraints
  output: product/initiatives/<initiative-id>/launch.md
       │
       ▼
PRODUCT LEARNING
  input: outcome hypothesis, baselines, usage data, feedback, operational and market signals
  output: product/initiatives/<initiative-id>/learning/<yyyy-mm-dd>-outcome-review.md
       │
       ├──────────────────────→ problem framing and portfolio prioritization
       ├──────────────────────→ market research (changed segment or market assumption)
       └──────────────────────→ Wardley strategy (changed value chain, evolution, or play)
       └──────────────────────→ product direction (reaffirm, refine, or challenge)
```

## Cadence And Boundaries

- `market-research` is invoked whenever a decision needs external market context and its output may be reused by several stages.
- `product-direction` and `wardley-strategy` operate at a product, domain, or portfolio cadence, not once per feature.
- `problem-framing` through `product-learning` operate per opportunity or product increment.
- A return arrow means the named artifact or decision must be revised; it does not mean every cycle restarts from scratch.
