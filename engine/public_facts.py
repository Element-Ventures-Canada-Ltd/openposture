# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Structural facts read from an OpenChokepoint registry. Counts and gaps only; no judgments."""
from pathlib import Path

import yaml


def load(path):
    with open(Path(path), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def facts(data: dict) -> dict:
    objects = {o["id"]: o for o in data.get("objects", [])}
    links = data.get("links", [])
    evidenced = {l["from"] for l in links if l.get("type") == "evidenced_by"}
    serials = []
    for sid, o in objects.items():
        if o.get("type") != "SerialItem":
            continue
        steps = [l for l in links if l.get("type") == "underwent" and l.get("from") == sid]
        ordered = all("sequence" in l for l in steps)
        steps = sorted(steps, key=lambda l: l.get("sequence", 0)) if ordered else steps
        design = next((objects[l["to"]] for l in links if l.get("type") == "instance_of" and l.get("from") == sid), {})
        serials.append({
            "id": sid,
            "serial": o.get("serial"),
            "synthetic": o.get("synthetic") is True,
            "design": f"{design.get('part_number', '?')} rev {design.get('revision', '?')}",
            "ordered": ordered,
            "steps": [{"id": l["to"], "kind": objects.get(l["to"], {}).get("step_kind"),
                       "evidence": l["to"] in evidenced} for l in steps],
        })
        s = serials[-1]
        s["with_evidence"] = sum(1 for x in s["steps"] if x["evidence"])
        s["missing_evidence"] = [x["id"] for x in s["steps"] if not x["evidence"]]
    flags = []
    for cid, o in objects.items():
        if o.get("type") == "CriticalItem" and o.get("synthetic") is True:
            flags.append({"id": cid, "name": o.get("name"),
                          "targets": [l["to"] for l in links if l.get("type") == "flags" and l.get("from") == cid],
                          "single_source": o.get("single_source"), "qualified_alternate": o.get("qualified_alternate"),
                          "missing_evidence": o.get("missing_evidence", False)})
    return {"serials": serials, "synthetic_critical_items": flags,
            "assessment": None, "assessment_note": "Assessment: not available in the public tier"}
