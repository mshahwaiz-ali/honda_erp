#!/usr/bin/env python3
"""
Legacy Honda ERP screenshot inventory helper.

Creates reproducible metadata for screenshot evidence and, when a manifest
exists, preserves the logical review order defined by that manifest.

This script intentionally does NOT perform OCR or semantic ERP analysis.
Detailed business interpretation is written separately after visual review.

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


def image_metadata(path: Path, sequence: int, image_id: str | None = None) -> dict:
    width, height = png_dimensions(path)
    data = {
        "sequence": sequence,
        "filename": path.name,
        "path": path.as_posix(),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "width": width,
        "height": height,
        "analysis_status": "pending",
    }
    if image_id:
        data["image_id"] = image_id
    return data


def load_manifest(manifest_path: Path) -> dict | None:
    if not manifest_path.is_file():
        return None
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def build_from_manifest(source: Path, manifest: dict) -> dict:
    actual_files = {
        p.name: p
        for p in source.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    }

    manifest_names: list[str] = []
    batches: list[dict] = []
    sequence = 0

    for batch in manifest.get("batches", []):
        out_images = []
        for entry in batch.get("images", []):
            filename = entry["filename"]
            manifest_names.append(filename)

            if filename not in actual_files:
                raise SystemExit(
                    f"Manifest references missing screenshot: {filename}"
                )

            sequence += 1
            out_images.append(
                image_metadata(
                    actual_files[filename],
                    sequence,
                    entry.get("image_id"),
                )
            )

        batches.append({
            "batch_number": len(batches) + 1,
            "batch_id": batch.get("batch_id"),
            "analysis_status": batch.get("status", "pending"),
            "images": out_images,
        })

    duplicate_names = sorted(
        name for name in set(manifest_names)
        if manifest_names.count(name) > 1
    )
    if duplicate_names:
        raise SystemExit(
            "Duplicate screenshot(s) in manifest: " + ", ".join(duplicate_names)
        )

    unlisted = sorted(set(actual_files) - set(manifest_names))
    if unlisted:
        raise SystemExit(
            "Screenshot(s) exist but are not listed in manifest: "
            + ", ".join(unlisted)
        )

    return {
        "source_directory": source.as_posix(),
        "ordering": "logical_manifest",
        "image_count": sequence,
        "batch_size": manifest.get("batch_size", 3),
        "batch_count": len(batches),
        "batches": batches,
    }


def build_alphabetically(source: Path, batch_size: int) -> dict:
    files = sorted(
        p for p in source.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    )

    images = [
        image_metadata(path, i)
        for i, path in enumerate(files, start=1)
    ]

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
        "ordering": "alphabetical_fallback",
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
        "--manifest",
        default="docs/bike_erp_image_analysis/bike_image_manifest.json",
        help="Logical screenshot review manifest.",
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

    manifest_path = Path(args.manifest)
    manifest = load_manifest(manifest_path)

    if manifest is not None:
        data = build_from_manifest(source, manifest)
    else:
        data = build_alphabetically(source, args.batch_size)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    print(f"Images:   {data['image_count']}")
    print(f"Batches:  {data['batch_count']}")
    print(f"Ordering: {data['ordering']}")
    print(f"Output:   {output}")

    if data["batches"]:
        print("First batch:")
        for image in data["batches"][0]["images"]:
            print(f" - {image['filename']}")


if __name__ == "__main__":
    main()
