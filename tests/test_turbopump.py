# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
sys.path.insert(0, str(ROOT / "tools"))
import check_public_data as G  # noqa: E402
import turbopump as T  # noqa: E402

BOM, ENT = T.load()
F = T.facts(BOM, ENT)


class TurbopumpFacts(unittest.TestCase):
    def test_no_assessment_in_public_tier(self):
        self.assertIsNone(F["assessment"])
        for p in F["parts"]:
            for k in ("score", "critical", "lead_time_weeks", "priority"):
                self.assertNotIn(k, p)

    def test_counts_are_consistent(self):
        s = F["summary"]
        self.assertEqual(s["parts"], len(BOM["parts"]))
        self.assertEqual(s["parts_with_candidate"] + s["parts_no_candidate"], s["parts"])
        self.assertGreaterEqual(s["parts_no_canadian_owned_candidate"], s["parts_no_candidate"])

    def test_gaps_shown_not_filled(self):
        p = next(x for x in F["parts"] if x["id"] == "TP-430")
        self.assertEqual(p["gap"], "no_candidate")
        self.assertEqual(p["candidates"], [])

    def test_foreign_owned_plant_in_canada_is_not_domestic(self):
        subs = [e for e in ENT["entities"] if e["ownership_class"] == "Canadian subsidiary of foreign parent"
                and e["location"].get("country") == "CA"]
        self.assertTrue(subs)
        for p in F["parts"]:
            ids = {c["id"] for c in p["candidates"]}
            if ids and ids <= {e["id"] for e in subs}:
                self.assertEqual(p["gap"], "no_canadian_owned_candidate")

    def test_tree_is_rooted(self):
        roots = [p for p in BOM["parts"] if p["parent"] is None]
        self.assertEqual([r["id"] for r in roots], ["TP-000"])


class PublicDataGuard(unittest.TestCase):
    def test_repo_data_passes(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "check_public_data.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_guard_catches_forbidden_field_and_text(self):
        import tempfile, shutil
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "turbopump"
            shutil.copytree(ROOT / "data" / "turbopump", d)
            t = (d / "bom.yaml").read_text(encoding="utf-8")
            t = t.replace("  name: Turbine blisk\n", "  name: Turbine blisk\n  material: secret\n", 1)
            (d / "bom.yaml").write_text(t + "# Example Private Programme\n", encoding="utf-8")
            G.FORBIDDEN_TEXT.append("Example Private Programme")
            try:
                errs = G.check_dir(d)
            finally:
                G.FORBIDDEN_TEXT.pop()
            self.assertTrue(any("forbidden field" in e for e in errs))
            self.assertTrue(any("forbidden text" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
