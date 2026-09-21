#!/usr/bin/env python3
"""
Legacy Honda ERP screenshot inventory helper.

This script DOES NOT attempt semantic ERP analysis or OCR.
It creates reproducible metadata for screenshot evidence so the visual
analysis can be performed accurately in small batches and stored as JSON.

Only Python standard library is required.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

IMAGE_EXTENSIONS = {".png"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int] | tuple[None, None]:
    with path.open("rb") as f:
        signature = f.read(24)
    if len(signature) < 24 or signature[:8] != b"\x89PNG\r\n\x1a\n":
        return None, None
    width, height = struct.unpack(">II", signature[16:24])
    return width, height


def build_inventory(source: Path, batch_size: int) -> dict:
    files = sorted(
        p for p in source.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    )

    images = []
    for i, path in enumerate(files, start=1):
        width, height = png_dimensions(path)
        images.append({
            "sequence": i,
            "filename": path.name,
            "path": path.as_posix(),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "width": width,
            "height": height,
            "analysis_status": "pending",
        })

    batches = []
    for offset in range(0, len(images), batch_size):
        chunk = images[offset:offset + batch_size]
        batches.append({
            "batch_number": len(batches) + 1,
            "analysis_status": "pending",
            "images": chunk,
        })

    return {
        "source_directory": source.as_posix(),
        "image_count": len(images),
        "batch_size": batch_size,
        "batch_count": len(batches),
        "batches": batches,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        default="client_old/software_images_bike",
        help="Screenshot directory relative to repository root.",
    )
    parser.add_argument(
        "--output",
        default="docs/bike_erp_image_analysis/generated_inventory.json",
        help="JSON output path.",
    )
    parser.add_argument("--batch-size", type=int, default=3)
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_dir():
        raise SystemExit(f"Source directory not found: {source}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    data = build_inventory(source, args.batch_size)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    print(f"Images:  {data['image_count']}")
    print(f"Batches: {data['batch_count']}")
    print(f"Output:  {output}")


if __name__ == "__main__":
    main()
