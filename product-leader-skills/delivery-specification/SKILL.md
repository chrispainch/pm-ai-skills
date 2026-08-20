---
name: delivery-specification
description: "Use when a shaped and validated product increment needs an implementation-ready behavioral handoff: acceptance criteria, edge cases, non-functional requirements, dependencies, instrumentation, and release conditions. Does not replace engineering design or implementation planning."
metadata:
  short-description: Make shaped work delivery-ready
---

# Delivery Specification

Translate a chosen product shape into verifiable behavior without turning the document into a technical design or task list.

## Inputs

Start from the solution-shaping artifact and incorporate the relevant breadboard, UX decisions, usability findings, and launch constraints. If a core product rule is still unclear, return it to shaping.

## Workflow

1. State the intended user outcome and bounded delivery slice.
2. Describe observable behavior with scenarios and acceptance criteria, including important failure and recovery paths.
3. Record non-functional requirements only when material: accessibility, privacy, security, reliability, performance, localization, or compliance.
4. Identify product-facing dependencies, decisions, and release constraints without prescribing an engineering architecture.
5. Specify events, properties, baseline, and success interpretation needed to measure the intended outcome.
6. Define test and release conditions that must be true before rollout.

## Output

Follow the [Product Artifact Contract](../../references/product-artifact-contract.md). Write the specification to `product/initiatives/<initiative-id>/delivery-specification.md` and register it in `manifest.yaml`. Use [references/delivery-spec-template.md](references/delivery-spec-template.md). It is the product handoff for implementation and QA, not a replacement for technical design documents.

## Handoff

Advance the specification to implementation and `product-launching`. Route behavior ambiguity to `solution-shaping`, UX ambiguity to `ascii-ui-exploration` or `usability-validation`, and instrumentation ambiguity to `product-learning`.
