# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import public_facts as P  # noqa: E402

EX = P.load(ROOT / "examples" / "synthetic-turbopump-thread.yaml")


class PublicFacts(unittest.TestCase):
    def test_no_assessment_in_public_tier(self):
        f = P.facts(EX)
        self.assertIsNone(f["assessment"])

    def test_gap_is_shown(self):
        f = P.facts(EX)
        gaps = [s for s in f["serials"] if s["missing_evidence"]]
        self.assertTrue(gaps, "the synthetic example has a step with no evidence record")

    def test_unordered_real_style_input(self):
        data = {"objects": [{"type": "SerialItem", "id": "s", "serial": "X"},
                            {"type": "ProcessStep", "id": "p", "step_kind": "cleaning"}],
                "links": [{"type": "underwent", "id": "l", "from": "s", "to": "p"}]}
        s = P.facts(data)["serials"][0]
        self.assertFalse(s["ordered"])
        self.assertEqual(s["missing_evidence"], ["p"])


if __name__ == "__main__":
    unittest.main()
