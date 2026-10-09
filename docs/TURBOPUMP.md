Handling: Unclassified — public

# Turbopump module (v0.1)

The first PHAROS Alpha use case: a public supply map for a small liquid-rocket turbopump, built for customer and partner validation. Reference case: the Launch Canada turbopump programme (public), with electric drive in Phases 1 and 2 and a gas-generator turbopump in Phase 3.

## What it shows

| View | Content |
|---|---|
| Bill of materials | 41 part categories in a tree, with public-capability candidates, ownership of candidates, export-list category and a gap status |
| Entities | 28 public-record entities: role, ownership class, parent, location, capability, evidence grade and sources |
| Evidence trace | The synthetic serial-traceability example from `examples/` |
| Method | Definitions and what is left out |

Gap status per part:

- **No candidate found**: no public record shows a company with the capability.
- **No Canadian-owned candidate**: every candidate is foreign-owned or a Canadian plant of a foreign parent.
- **Canadian-owned candidate**: at least one candidate is Canadian-owned.

## What it does not show

No materials, processes, dimensions, performance, test data or lead times: turbopumps are on Canada's Export Control List (item 6-3), and this repository holds supply mapping only ([EXPORT-CONTROL.md](../EXPORT-CONTROL.md)). No scores, priorities or critical path: assessment comes from the private engine through `engine/interface.py`.

A candidate is a company with a public, relevant capability. It is not a verified or qualified supplier.

## Files

| Path | Purpose |
|---|---|
| `data/turbopump/bom.yaml`, `entities.yaml`, `provenance.yaml` | Real public-record data (`synthetic: false`) with sources |
| `engine/turbopump.py` | Public facts: counts, ownership and gaps |
| `tools/check_public_data.py` | Guard run in CI: forbidden fields and terms, https sources, grades, tree integrity |
| `tools/build_ui.py` | Builds `ui/map.html` (Canada Space Supply Chain Map dashboard) and `ui/turbopump.html` with the data embedded |
| `tests/test_turbopump.py` | Tests for facts and guard |

## Run it

```
python3 tools/check_public_data.py
python3 tools/build_ui.py          # writes ui/map.html and ui/turbopump.html
python3 -m unittest discover -s tests -v
```

Open `ui/map.html` (dashboard: supply network, geography, coverage by assembly, parts explorer) or `ui/turbopump.html` (simple viewer) in a browser. No server needed.

## Corrections

Report a wrong record through an issue with the source that corrects it. Ownership is recorded separately from location; where ownership is not verified, the record says so.
