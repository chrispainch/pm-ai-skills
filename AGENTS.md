# Product-management operating contract

This repository contains reusable product-management skills under `.agents/`.
Apply these rules to every product-management task before following a selected
skill's task-specific instructions.

## Lifecycle and handoffs

Use the smallest set of skills that resolves the decision at hand. The normal
flow is:

1. **Set direction** with `product-direction`; use `wardley-strategy` when a
   value-chain or evolution view would change the strategic choice.
2. **Understand the market** with `market-research` when external context or a
   consequential assumption needs evidence.
3. **Choose the bet** with `portfolio-prioritization` when competing
   opportunities require a sequencing decision.
4. **Frame the opportunity** with `problem-framing` before proposing a solution.
5. **Shape the solution** with `solution-shaping`. It requires an active product
   direction and a framed problem.
6. **Make the experience legible** with `breadboarding`; use
   `ascii-ui-exploration` only when interface structure remains uncertain.
7. **Prepare rollout** with `product-launching` once the solution is established.

Do not treat the flow as a checklist. Return to research, direction, or framing
when new evidence invalidates a material assumption. Preserve links to the
upstream artifact(s) that informed a downstream decision.

## Artifact policy

- Produce a persistent artifact only when the task calls for a reusable decision
  record. A conversational answer is sufficient for exploratory or transient
  work.
- Use the selected skill's template when one is provided.
- Separate evidence, interpretation, assumptions, and decisions. Include an
  owner and review trigger for consequential decisions.
- Never overwrite a prior learning or decision record merely to create a new
  version; use a dated or otherwise explicit new record when history matters.
- Do not invent missing IDs. Ask for or derive an `initiative_id`, `research_id`,
  `domain_id`, `year`, `quarter`, or `date` only when its output path needs one.

## Output locations

`.agents/output-locations.yaml` is the canonical registry. Read it once at the
start of a task that will create persistent artifacts; do not make each selected
skill rediscover it. Resolve every route relative to `output_root` (currently
`product`) and substitute path placeholders supplied by the task.

| Skill | Persistent output route(s), below `output_root` |
| --- | --- |
| `product-direction` | `strategy/direction/product-direction.md` |
| `market-research` | `strategy/market-research/{research_id}/brief.md`; `strategy/market-research/{research_id}/evidence-ledger.md` |
| `wardley-strategy` | `strategy/wardley/{domain_id}/map.yaml`; optional `strategy/wardley/{domain_id}/review.md` |
| `portfolio-prioritization` | `strategy/portfolio/{year}-{quarter}.md` |
| `problem-framing` | `initiatives/{initiative_id}/framing.md` |
| `solution-shaping` | `initiatives/{initiative_id}/solution.md` |
| `breadboarding` | `initiatives/{initiative_id}/flow.md` |
| `ascii-ui-exploration` | optional `initiatives/{initiative_id}/ui-exploration.md` |
| `product-launching` | `initiatives/{initiative_id}/launch.md` |

When this registry changes, update this table and any skill wording that names a
route in the same change.
