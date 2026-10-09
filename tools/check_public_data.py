# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Guard for real (non-synthetic) records under data/. Exit 1 on any violation.

Enforces DATA-CONTRIBUTIONS.md 'Real-world records (v0.1)' and EXPORT-CONTROL.md for this repo:
no technical or assessment fields, https provenance on every entity, confirmed/reported grades
only, no personal-profile sources, no private names (supplied by CI, not listed here)."""
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN_KEYS = {"material", "process", "lead_time_weeks", "lt_basis", "own_weeks", "market_sources",
                  "substitutability", "qualification", "automation", "auto_adjacency", "score", "band",
                  "weight", "weights", "critical", "critical_path", "rubric", "registry_refs",
                  "sprint_target", "tier", "trl", "disposition", "notes_internal"}
FORBIDDEN_TEXT = [r"linkedin\.com/in/", r"linkedin\.com/posts/"]  # personal-profile sources
# Private programme, registry and engine names are not listed here: naming them would publish them.
# CI supplies them from the repository secret OPENPOSTURE_PRIVATE_TERMS (one term per line).
FORBIDDEN_TEXT += [re.escape(t.strip()) for t in os.environ.get("OPENPOSTURE_PRIVATE_TERMS", "").splitlines() if t.strip()]
GRADES = {"confirmed", "reported"}


def walk_keys(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield k, f"{path}.{k}"
            yield from walk_keys(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_keys(v, f"{path}[{i}]")


def check_dir(d: Path) -> list:
    errors = []
    for f in sorted(d.glob("*.yaml")):
        text = f.read_text(encoding="utf-8")
        if "Handling: Unclassified — public" not in text.splitlines()[0]:
            errors.append(f"{f.name}: first line must carry the public handling marking")
        for pat in FORBIDDEN_TEXT:
            if re.search(pat, text, re.IGNORECASE):
                errors.append(f"{f.name}: forbidden text (pattern {FORBIDDEN_TEXT.index(pat) + 1})")
        data = yaml.safe_load(text)
        if f.name == "provenance.yaml":
            continue
        for k, p in walk_keys(data):
            if k in FORBIDDEN_KEYS:
                errors.append(f"{f.name}: forbidden field {p}")
        if data.get("synthetic") is not False:
            errors.append(f"{f.name}: real-data files must declare synthetic: false")
        for e in data.get("entities", []):
            src = e.get("sources") or []
            if not src or not all(str(s).startswith("https://") for s in src):
                errors.append(f"{f.name}: {e.get('id')} needs https sources")
            if e.get("evidence_grade") not in GRADES:
                errors.append(f"{f.name}: {e.get('id')} grade must be confirmed or reported")
        ids = {e["id"] for e in data.get("entities", [])}
        if ids:
            check_dir.entity_ids = ids
    bom = d / "bom.yaml"
    if bom.exists():
        parts = yaml.safe_load(bom.read_text(encoding="utf-8"))["parts"]
        pid = {p["id"] for p in parts}
        known = getattr(check_dir, "entity_ids", set())
        for p in parts:
            if p["parent"] is not None and p["parent"] not in pid:
                errors.append(f"bom.yaml: {p['id']} has unknown parent {p['parent']}")
            for c in p.get("candidates", []):
                if c not in known:
                    errors.append(f"bom.yaml: {p['id']} candidate {c} not in entities.yaml")
    if not (d / "provenance.yaml").exists():
        errors.append(f"{d.name}: provenance.yaml missing")
    return errors


if __name__ == "__main__":
    errs = []
    for d in sorted((ROOT / "data").iterdir()):
        if d.is_dir():
            errs += check_dir(d)
    for e in errs:
        print("ERROR", e)
    print("OK" if not errs else f"{len(errs)} error(s)")
    sys.exit(1 if errs else 0)
