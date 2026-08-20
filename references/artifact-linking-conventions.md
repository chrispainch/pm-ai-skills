# Product Factory Artifact Linking

Every durable product artifact must use the [Product Artifact Contract](product-artifact-contract.md), link to its immediate upstream decision, and preserve the strategic context that justified it.

| Artifact | Required path | Required links |
|---|---|---|
| Product direction | `product/strategy/direction/product-direction.md` | Market research, Wardley maps, strategic outcomes, and review triggers |
| Market research brief | `product/strategy/market-research/<research-id>/brief.md` | Decision it informs; evidence ledger |
| Wardley map | `product/strategy/wardley/<domain-id>/map.yaml` | Market research briefs; relevant uncertainties |
| Portfolio decision | `product/strategy/portfolio/<yyyy>-<quarter>.md` | Compared opportunity briefs; capacity and decision horizon |
| Opportunity brief | `product/initiatives/<initiative-id>/framing.md` | Product direction, Wardley map scope and strategic play; evidence sources |
| Discovery synthesis | `product/initiatives/<initiative-id>/discovery.md` | Selected opportunity brief; tested assumptions |
| Solution shape | `product/initiatives/<initiative-id>/solution.md` | Validated opportunity and discovery synthesis |
| Delivery specification | `product/initiatives/<initiative-id>/delivery-specification.md` | Solution shape, flow/UI artifacts, and measurement intent |
| Launch brief | `product/initiatives/<initiative-id>/launch.md` | Delivery specification and rollout decision |
| Outcome review | `product/initiatives/<initiative-id>/learning/<yyyy-mm-dd>-outcome-review.md` | Opportunity, solution, launch, and observed evidence |

Use stable relative links only. Do not duplicate upstream content when a link and concise recap are enough.
