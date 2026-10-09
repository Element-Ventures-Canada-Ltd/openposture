# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Turbopump module: public facts from the public-record BOM and entity files.

Facts only: candidate counts, ownership of candidates, export-list category and gaps.
No scores, priorities, lead times or critical path. Those come from a private engine
through engine/interface.py and never appear in this repository."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "turbopump"
DOMESTIC = "Canadian"


def load(data_dir=DATA):
    with open(Path(data_dir) / "bom.yaml", encoding="utf-8") as fh:
        bom = yaml.safe_load(fh)
    with open(Path(data_dir) / "entities.yaml", encoding="utf-8") as fh:
        ent = yaml.safe_load(fh)
    return bom, ent


def facts(bom: dict, ent: dict) -> dict:
    entities = {e["id"]: e for e in ent["entities"]}
    parts = []
    for p in bom["parts"]:
        cands = [entities[c] for c in p.get("candidates", []) if c in entities]
        domestic = [c for c in cands if c["ownership_class"] == DOMESTIC]
        if not cands:
            gap = "no_candidate"
        elif not domestic:
            gap = "no_canadian_owned_candidate"
        else:
            gap = None
        parts.append({
            "id": p["id"], "level": p["level"], "parent": p["parent"], "name": p["name"],
            "export_list": p.get("export_list", []),
            "candidates": [{"id": c["id"], "name": c["name"], "ownership_class": c["ownership_class"],
                            "country": c["location"].get("country")} for c in cands],
            "candidate_count": len(cands), "canadian_owned_candidates": len(domestic),
            "gap": gap, "note": p.get("note"), "sources": p.get("sources", []),
        })
    by_owner, by_source = {}, {}
    for e in entities.values():
        by_owner[e["ownership_class"]] = by_owner.get(e["ownership_class"], 0) + 1
        by_source[e["source_type"]] = by_source.get(e["source_type"], 0) + 1
    summary = {
        "parts": len(parts),
        "parts_with_candidate": sum(1 for p in parts if p["candidate_count"]),
        "parts_no_candidate": sum(1 for p in parts if p["gap"] == "no_candidate"),
        "parts_no_canadian_owned_candidate": sum(1 for p in parts if p["gap"] is not None),
        "parts_export_listed": sum(1 for p in parts if p["export_list"]),
        "entities": len(entities), "entities_by_ownership": by_owner, "entities_by_source": by_source,
    }
    return {"module": "turbopump", "as_of": str(bom.get("as_of")), "reference": bom.get("reference"),
            "summary": summary, "parts": parts, "entities": list(entities.values()),
            "assessment": None, "assessment_note": "Assessment: not available in the public tier"}
