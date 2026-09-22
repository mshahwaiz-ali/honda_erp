#!/usr/bin/env python3
"""
Export one legacy Bike screenshot-analysis batch as a ZIP for visual review.

The ZIP is a transport artifact only. It is intentionally not committed.
It contains:
- the 3 screenshots for the requested logical batch
- batch_manifest.json with source paths / IDs / metadata

Only Python standard library is required.
"""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


DEFAULT_INVENTORY = Path("docs/bike_erp/01_legacy_evidence/image_analysis/generated_inventory.json")
DEFAULT_OUTPUT_DIR = Path("review_batches/bike")


def load_inventory(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(
            f"Inventory not found: {path}\n"
            "Run: python3 tools/legacy_image_inventory.py"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_batch(data: dict, batch_number: int) -> dict:
    for batch in data.get("batches", []):
        if batch.get("batch_number") == batch_number:
            return batch
    raise SystemExit(f"Batch {batch_number} not found")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_number", type=int, help="1-based Bike batch number")
    parser.add_argument(
        "--inventory",
        default=str(DEFAULT_INVENTORY),
        help="Generated inventory JSON",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Local ZIP output directory",
    )
    args = parser.parse_args()

    inventory_path = Path(args.inventory)
    data = load_inventory(inventory_path)
    batch = resolve_batch(data, args.batch_number)

    batch_id = batch.get("batch_id") or f"BIKE-BATCH-{args.batch_number:02d}"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_zip = output_dir / f"{batch_id}.zip"

    images = batch.get("images", [])
    if not images:
        raise SystemExit(f"{batch_id} has no images")

    manifest = {
        "system": "bike",
        "batch_id": batch_id,
        "batch_number": args.batch_number,
        "image_count": len(images),
        "images": images,
    }

    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            "batch_manifest.json",
            json.dumps(manifest, indent=2) + "\n",
        )

        for image in images:
            source = Path(image["path"])
            if not source.is_file():
                raise SystemExit(f"Missing source image: {source}")
            zf.write(source, arcname=source.name)

    print(f"Batch:  {batch_id}")
    print(f"Images: {len(images)}")
    for image in images:
        print(f" - {image.get('image_id', '')} {image['filename']}")
    print(f"ZIP:    {output_zip}")
    print(f"Bytes:  {output_zip.stat().st_size}")


if __name__ == "__main__":
    main()
