---
name: usability-validation
description: Use when a shaped flow, wireframe, prototype, or implemented experience needs user-task evidence before broad release. Plans and synthesizes usability validation; use ascii-ui-exploration for interface options and product-discovery for broader opportunity uncertainty.
metadata:
  short-description: Validate flows and interface usability
---

# Usability Validation

Test whether intended users can understand and complete the shaped task. Validate task behavior and comprehension, not aesthetic preference.

## Inputs

Start from the relevant solution-shaping artifact and breadboard or interface direction. State the target user, task, success condition, prototype fidelity, and unresolved UX decision.

## Workflow

1. Turn the shaped user outcome into representative tasks and observable success criteria.
2. Choose a proportionate validation approach and participants who match the intended context.
3. Capture behavior, comprehension, failure, recovery, and notable exceptions.
4. Separate evidence from design recommendations.
5. Classify findings by severity and whether they require UI refinement, flow changes, solution reshaping, or delivery requirements.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write the validation record to `product/initiatives/<initiative-id>/usability-validation.md`, register it in `manifest.yaml`, and store initiative-specific raw evidence under `evidence/`. Use [references/usability-validation-template.md](references/usability-validation-template.md). Do not treat a small test as population-level proof; record confidence and limitations.

## Handoff

Send interface-level changes to `ascii-ui-exploration`, flow issues to `breadboarding`, and scope-changing findings to `solution-shaping`. Confirmed interaction rules feed `delivery-specification`.
