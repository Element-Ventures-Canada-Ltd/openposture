Handling: Unclassified — public

# Architecture: public shell, private engine

```
OpenChokepoint registry (YAML)
        |
        v
engine/public_facts.py  -- structural facts only (public)
        |
        +--> engine/interface.py: PostureEngine  <-- a private engine implements this, outside this repo
        |
        v
posture.json  -->  ui/index.html
```

**Public facts** are counts and gaps read straight from the registry: steps per serial item, steps with and without an evidence record, and what a synthetic critical item flags. They are reproducible by anyone from the same file.

**Engine output** (judgments, scores, priorities) comes only from a private engine. In this repository `engine/run.py` uses no engine, and the interface shows "Assessment: not available in the public tier".

Real-world records follow the OpenChokepoint public-tier rule: they show which steps happened, not their order.

## Turbopump module

`data/turbopump/` (public records) -> `engine/turbopump.py` (facts: candidates, ownership, gaps) -> `ui/turbopump.html`. The same engine interface applies: assessment is private. See [TURBOPUMP.md](TURBOPUMP.md).
