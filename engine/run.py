# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Usage: python3 engine/run.py <registry.yaml>  -> prints posture JSON (public facts, no assessment)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import public_facts  # noqa: E402

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(json.dumps(public_facts.facts(public_facts.load(sys.argv[1])), indent=2, default=str))
