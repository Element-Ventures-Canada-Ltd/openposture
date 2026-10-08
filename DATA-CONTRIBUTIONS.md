Handling: Unclassified — public

# Data and Model Contributions

Requirements for any contribution of data, datasets, model weights, fine-tunes,
or evaluation sets to the open tier. These sit alongside CLA.md and HANDLING.md.

## Rules

1. **Synthetic or public only.** Data must be synthetic, or public and licensed
   for redistribution and model training. No real entity-level data from
   non-public sources.
2. **No personal information** unless fully de-identified and permitted by the
   source licence.
3. **No export-controlled technical data**, and nothing marked above
   "Unclassified — public".
4. **Right to train.** You must have the right to let EV use the data to train,
   evaluate, and distribute models, including commercially.
5. **Provenance manifest required.** Every data or model contribution includes
   a `provenance.yaml` in the same folder, completed as below.

## provenance.yaml template

```yaml
handling: "Unclassified — public"
contribution: ""          # short name
type: ""                  # dataset | weights | fine-tune | eval-set
sources:
  - description: ""
    url: ""
    licence: ""           # SPDX id or licence name
    retrieved: ""         # YYYY-MM-DD
synthetic: false          # true if generated
personal_information: none   # none | de-identified (explain in notes)
export_controlled: false
training_rights_confirmed: false
base_model: ""            # for weights / fine-tunes
notes: ""
```

Contributions without a complete manifest will not be merged.

## Real-world records (v0.1)

Real (non-synthetic) records are accepted under `data/` when every rule below holds. Anything else is synthetic and lives under `examples/`.

1. **Public and citable.** Every record cites a publicly released source by https URL and section. Company filings, government registries, procurement and grant disclosures, and published technical reports qualify. Paywalled, leaked, internal or "shared in confidence" material does not.
2. **Licensed for redistribution.** The source's terms permit redistribution of the facts recorded. Facts are recorded in your own words; source text is not copied.
3. **Graded, not inferred.** Real records are graded `confirmed` or `reported`. Gaps are shown as gaps.
4. **Mapping, not technical data.** Who supplies what, where, and with what dependency. No design, process, test or performance data ([CONTRIBUTION-SCOPE.md](CONTRIBUTION-SCOPE.md)).
5. **No judgments on real records.** Critical-item flags and assessments appear on synthetic records only.
6. **Public tier hides process order.** Real step records show which steps happened, not their order (validator rule DT-003).
7. **People.** No named individuals below officer or public-spokesperson level; no personal contact details.
8. **Screened.** The contribution passes the export-control screen ([EXPORT-CONTROL.md](EXPORT-CONTROL.md)).
