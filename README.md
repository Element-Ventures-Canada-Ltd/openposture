Handling: Unclassified — public

# OpenPosture

The open shell of the PHAROS Alpha prototype: a public user interface and adapter layer that reads an [OpenChokepoint](https://github.com/Element-Ventures-Canada-Ltd/openchokepoint) registry and shows a supply chain's evidence posture.

First use case: the rocket turbopump supply chain, built for customer and partner validation. The turbopump module ([docs/TURBOPUMP.md](docs/TURBOPUMP.md)) maps 41 part categories to public-record supplier candidates, their ownership and the gaps. Its data is real and public, with a source on every record; the serial-traceability example is synthetic.

## What is public, and what is not

| Public (this repository) | Private (not here) |
|---|---|
| User interface (`ui/`) | Determination logic and scoring |
| OpenChokepoint adapter and structural facts (`engine/public_facts.py`) | Weights, rubrics and any layered framework mapping |
| The engine interface a private engine plugs into (`engine/interface.py`) | Real-world assessments of organizations or parts |
| Public-record supply map (`data/turbopump/`) and synthetic examples (`examples/`) | Non-public records of any kind |

The public tier reports **structural facts only**: which steps have an evidence record, which do not, and what a synthetic critical item flags. It makes no judgments. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Run it

Canada Space Supply Chain Map (turbopump module): `python3 tools/build_ui.py`, then open `ui/map.html`.

Serial-traceability example:

```
python3 engine/run.py examples/synthetic-turbopump-thread.yaml > ui/posture.json
python3 -m http.server -d ui 8000
```

Then open http://localhost:8000. Tests: `python3 -m unittest discover -s tests -v`. Requires Python 3.10+ and PyYAML.

## Contributing

Contributions follow the OpenChokepoint programme rules: CLA, contribution scope, handling and the deferred bounty ledger. See [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under Apache-2.0. © 2026 T. Leroy Smith. Exclusively licensed to Element Ventures (Canada) Ltd.
