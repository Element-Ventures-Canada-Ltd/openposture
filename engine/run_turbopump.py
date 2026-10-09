# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Usage: python3 engine/run_turbopump.py > ui/turbopump.json  (public facts, no assessment)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import turbopump  # noqa: E402

if __name__ == "__main__":
    print(json.dumps(turbopump.facts(*turbopump.load()), indent=2, ensure_ascii=False))
