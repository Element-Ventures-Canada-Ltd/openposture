# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""The interface a private posture engine implements. No implementation lives in this repository."""
from typing import Protocol


class PostureEngine(Protocol):
    name: str

    def assess(self, facts: dict) -> dict:
        """Take the public facts produced by public_facts.facts() and return an assessment dict.
        Implementations are private and are never contributed to this repository."""
        ...
