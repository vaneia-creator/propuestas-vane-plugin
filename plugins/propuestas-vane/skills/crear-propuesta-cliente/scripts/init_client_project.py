#!/usr/bin/env python3
"""Create a lightweight Propuestas Vane client workspace."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", ascii_value))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Propuestas Vane client project.")
    parser.add_argument("client_name")
    parser.add_argument("--niche", default="")
    parser.add_argument("--country", default="")
    parser.add_argument("--city", default="")
    parser.add_argument("--service", default="")
    parser.add_argument("--output", default=".")
    args = parser.parse_args()

    slug = slugify(args.client_name)
    if not slug:
        parser.error("client_name must contain letters or numbers")

    root = Path(args.output).resolve() / slug
    if root.exists():
        parser.error(f"project already exists: {root}")

    (root / "research").mkdir(parents=True)
    (root / "private").mkdir()
    (root / "site" / "assets").mkdir(parents=True)

    skill_root = Path(__file__).resolve().parent.parent
    shutil.copy2(
        skill_root / "assets" / "proposal-template.html",
        root / "site" / "proposal-template.html",
    )

    brief = {
        "schema_version": 2,
        "client_name": args.client_name.strip(),
        "client_slug": slug,
        "niche": args.niche.strip(),
        "country": args.country.strip(),
        "city": args.city.strip(),
        "service": args.service.strip(),
        "links": [],
        "assets": [],
        "facts": [],
        "inferences": [],
        "pending": [],
        "workflow_stage": "intake_complete",
        "published_urls": [],
        "pricing": {
            "currency": "",
            "low": None,
            "recommended": None,
            "high": None,
            "usd_equivalent": None,
            "as_of": None,
            "sources": [],
        },
        "public_pricing_requested": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (root / "client-brief.json").write_text(
        json.dumps(brief, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (root / "research" / "sources.md").write_text(
        "# Fuentes\n\n| Fecha | Fuente | URL | Respalda |\n|---|---|---|---|\n",
        encoding="utf-8",
    )
    (root / "private" / "pricing.md").write_text(
        "# Estimación privada\n\nNo publicar ni enlazar desde el sitio.\n",
        encoding="utf-8",
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
