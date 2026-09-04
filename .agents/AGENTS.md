# Product-management operating contract

This repository contains reusable product-management skills under `.agents/`.
Apply these rules to every product-management task before following a selected
skill's task-specific instructions.

## Lifecycle and handoffs

Use the smallest set of skills that resolves the decision at hand. Product work
follows a **strategic spiral**, not a one-way delivery pipeline: begin with the
largest material market and business questions, make a coherent strategic choice,
then repeat the loop at increasingly concrete levels as products are deployed
and their effects become observable.

1. **Understand the market.** Use `market-research` to establish evidence about
   participants, needs, alternatives, market forces, and unknowns.
2. **Form a strategic point of view.** Use `product-direction` to state the
   chosen users, outcomes, principles, boundaries, and measures. Use
   `wardley-strategy` when a value-chain, evolution, doctrine, or inertia view
   would materially affect the strategy. Evaluate the strategic and business
   model choices that can create traction; do not treat either as a feature list.
3. **Create a problem portfolio.** Use `problem-framing` to make each selected
   problem's user need, job context,outcomes, boundaries, evidence, and uncertainty decision-ready. Then use `portfolio-prioritization` to select and sequence the problems worth addressing within the strategic frame.
4. **Shape the response.** Use `solution-shaping` only when the problem and its
   governing product direction are established. Use `breadboarding` to clarify
   workflow and journey changes. Use `ascii-ui-exploration` when information or
   action hierarchy remains a material decision.
5. **Bring it to market and measure it.** Use `product-launching` to define
   rollout, enablement, operational readiness, user communication, success
   measures, and pause/progress criteria.
6. **Learn and spiral inward.** Treat deployed solutions, user-journey outcomes,
   and tracking signals as evidence for the next loop. Early loops resolve broad
   product-line or high-level needs; subsequent loops solve narrower, more
   practical problems, and eventually optimization opportunities. Start a new
   broad loop when pursuing a new product line or feature changes the strategic
   set.

Do not treat this as a checklist or a terminal delivery process. Return to market
research, strategy, portfolio choice, or problem framing when evidence changes a
material assumption. Preserve links to the upstream artifacts and decisions that
inform each downstream artifact.

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
