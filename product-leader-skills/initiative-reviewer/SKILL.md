---
name: initiative-reviewer
description: Use when a product initiative needs a lifecycle-aware quality review for missing artifacts, broken traceability, weak evidence, unresolved decisions, or readiness gaps. Runs the product-artifact validator and reports the smallest useful next action without creating missing work by default.
metadata:
  short-description: Review initiative readiness and gaps
---

# Initiative Reviewer

Review an initiative as a quality gate, not an orchestration engine. Verify its artifact structure first, then assess whether its current status is supported by the available decisions and evidence.

## Inputs

Require the consuming repository's `product/` root and an `initiative-id`. Read the canonical product direction, `manifest.yaml`, and the artifacts named there. If the user requests a portfolio-level review, review each selected initiative separately and summarize common gaps.

## Workflow

1. Run `scripts/validate_product_artifacts.py <product-root>`. Report structural failures exactly; do not silently repair them.
2. Read the product direction, initiative manifest, framing, and every extant artifact listed in the manifest.
3. Use [references/review-checkpoints.md](references/review-checkpoints.md) to assess the claim implied by the initiative status. Missing optional artifacts are only gaps when the work requires them or the manifest claims a later dependent status.
4. Separate findings into `structural`, `decision`, `evidence`, `alignment`, and `readiness` gaps. Include the source artifact and the consequence of each material gap.
5. Recommend the smallest next action: update an artifact, run a named skill, re-prioritize, hold, stop, or proceed. Do not fabricate evidence or create artifacts unless the user explicitly asks.

## Output

Return a concise review with:

- Current status and claimed next decision
- Validator result
- Material gaps grouped by type and severity
- Readiness decision: `ready`, `ready with conditions`, `not ready`, `hold`, or `return to strategy`
- The single next action and its owning skill or role

Do not write a persistent review artifact by default. The validator's test suite is for changes to this skill's validator, not ordinary initiative reviews.

## Validator And Tests

Run the packaged validator with:

```text
python3 <initiative-reviewer-skill-root>/scripts/validate_product_artifacts.py <path/to/product>
```

When changing the validator, run its tests from this skill folder:

```text
python3 -m unittest discover -s tests -v
```

The artifact layout itself is defined by the shared [Product Artifact Contract](../../references/product-artifact-contract.md).
