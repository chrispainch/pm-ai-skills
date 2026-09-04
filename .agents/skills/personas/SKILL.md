---
name: personas
description: Use when market research needs to become a detailed, evidence-rated foundation of all material customer and stakeholder personas. Builds on available market-research rather than repeating market discovery or direct user research.
metadata:
  short-description: Build a foundation of market personas
---

# Personas

Turn the participants identified in available market research into a detailed persona foundation for product management. Describe every material customer and stakeholder role, its context, needs, constraints, and relationship with other actors. Do not collapse that actor system into a single recommended persona.

## Inputs and boundaries

Start with the relevant market-research brief and evidence ledger when they exist. Reuse their defined market boundary, segments, participants, alternatives, and evidence. Do not repeat market discovery.

Market research can support a provisional persona; it does not establish an individual's motivations, language, workflow details, or priority. Mark those as hypotheses unless supported by direct customer evidence (such as interviews, observation, product analytics, or sales/support signals). Direct research remains a separate follow-up where material uncertainty remains.

This skill maps people and organizations around a customer. It does not define a product solution, customer journey, or account plan.

## Workflow

1. State the decision the personas will inform and link the source market-research artifacts.
2. Extract the actors already identified and map their relationship to the customer: buyer, economic buyer, champion, end user, administrator/operator, influencer, approver, blocker, beneficiary, and partner. Include only roles material to the decision.
3. Group actors into distinct role-based personas only where their goals, constraints, behavior, or decision power meaningfully differ. Avoid demographic or fictional detail that does not affect the decision.
4. Create one detailed persona for every material, distinct role. Do not rank or recommend a persona unless the requester specifically asks. Do not equate the buyer with the user without evidence.
5. For each persona, capture its context, job, desired outcomes, current approach and alternatives, pains, constraints, decision influence, and evidence rating. Separate observed evidence, reasoned inference, and validation hypotheses.
6. Map the key dependencies and tensions among actors: who initiates, evaluates, approves, pays, uses, administers, blocks, or benefits. Record how each relationship changes the product manager's understanding of the space.
7. Identify unanswered questions that would materially affect the persona foundation and recommend direct research methods proportionate to each gap.

## Output

For persistent files, follow the shared output policy in the repository's `AGENTS.md` and resolve the `personas.primary` route in `.agents/output-locations.yaml`. Use [references/persona-brief-template.md](references/persona-brief-template.md). Keep citations or links to upstream evidence close to each consequential claim, and preserve uncertainty rather than filling gaps with invented detail.
