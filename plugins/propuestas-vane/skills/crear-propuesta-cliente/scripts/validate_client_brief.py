#!/usr/bin/env python3
"""Validate the lightweight client brief and public privacy boundary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

STAGES = [
    "intake_complete",
    "audit_delivered",
    "execution_selected",
    "prototype_published",
    "final_proposal_published",
    "priced",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Propuestas Vane client brief.")
    parser.add_argument("brief", type=Path)
    parser.add_argument("--for-publication", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.brief.read_text(encoding="utf-8"))
    errors: list[str] = []

    for key in ("client_name", "client_slug", "workflow_stage"):
        if not data.get(key):
            errors.append(f"missing required field: {key}")

    stage = data.get("workflow_stage")
    if stage not in STAGES:
        errors.append(f"invalid workflow_stage: {stage!r}")

    if not isinstance(data.get("links", []), list):
        errors.append("links must be a list")
    if not isinstance(data.get("assets", []), list):
        errors.append("assets must be a list")
    if not isinstance(data.get("published_urls", []), list):
        errors.append("published_urls must be a list")
    if data.get("public_pricing_requested") not in (True, False):
        errors.append("public_pricing_requested must be boolean")

    if stage in ("execution_selected", "prototype_published", "final_proposal_published", "priced"):
        if not data.get("service"):
            errors.append("service is required after execution is selected")

    if stage == "priced":
        pricing = data.get("pricing", {})
        for key in ("currency", "low", "recommended", "high", "as_of"):
            if pricing.get(key) in (None, ""):
                errors.append(f"pricing.{key} is required at priced stage")
        if not isinstance(pricing.get("sources", []), list) or not pricing.get("sources"):
            errors.append("pricing.sources must contain at least one source at priced stage")

    if args.for_publication and data.get("public_pricing_requested") is not True:
        if data.get("public_price") or data.get("internal_cost"):
            errors.append("private pricing fields cannot be published")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Client brief is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
