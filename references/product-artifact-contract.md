# Product Artifact Contract

This contract governs durable artifacts written by these skills into a consuming product repository. It does not change the layout of this skill-source repository.

## Root Layout

```text
product/
├── README.md
├── strategy/
│   ├── direction/product-direction.md
│   ├── market-research/<research-id>/{brief.md,evidence-ledger.md}
│   ├── wardley/<domain-id>/{map.yaml,review.md}
│   └── portfolio/<yyyy>-<quarter>.md
└── initiatives/<initiative-id>/
    ├── manifest.yaml
    ├── framing.md
    ├── discovery.md
    ├── solution.md
    ├── flow.md
    ├── ui-exploration.md
    ├── usability-validation.md
    ├── delivery-specification.md
    ├── launch.md
    ├── evidence/<source-or-study-id>.md
    └── learning/<yyyy-mm-dd>-outcome-review.md
```

Use lowercase kebab-case IDs. `review.md`, `discovery.md`, `flow.md`, `ui-exploration.md`, `usability-validation.md`, `launch.md`, and `learning/` are created only when the related work occurs. Never move an initiative after creating `initiatives/<initiative-id>/`.

## Initiative Manifest

Every initiative must have `manifest.yaml`. Use [initiative-manifest-template.yaml](initiative-manifest-template.yaml). It must link to `product/strategy/direction/product-direction.md`; `framing.md` is always required; every path named under `artifacts` must exist. The manifest is the machine-readable index, while the Markdown artifacts contain the decision record.

## Artifact Metadata

Every durable Markdown artifact begins with this frontmatter:

```yaml
---
artifact_type: <contract artifact type>
initiative_id: <initiative-id or null for strategy artifacts>
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
upstream:
  - <relative path to the decision or evidence that justified this artifact>
---
```

Use relative links and paths only. A short recap is allowed; do not duplicate the upstream artifact. Keep market research reusable under `product/strategy/market-research/`; put initiative-specific source material under that initiative's `evidence/` folder.

## Lifecycle Rules

- Strategy artifacts and the initiative's living artifacts are revised in place.
- `product/strategy/direction/product-direction.md` is the canonical product intent. Market research, Wardley reviews, and outcome reviews may reaffirm, refine, or challenge it.
- Outcome reviews are immutable, dated files under `learning/`; a new review is created for each review period.
- When an initiative is held or stopped, retain its folder, set `status` and `current_decision` in the manifest, and do not create later-stage artifacts.
- The canonical Wardley artifact is `map.yaml`; `review.md` is a derived human-readable rendering.

## Validation

Run `python3 software-pm-skills/initiative-reviewer/scripts/validate_product_artifacts.py <product-root>` from this skill repository, or copy the packaged script into a consuming repository. It checks the required tree, manifest references, standard names, metadata, and local Markdown links.
