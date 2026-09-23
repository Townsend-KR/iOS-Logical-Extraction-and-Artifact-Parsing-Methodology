#!/usr/bin/env python3
"""Create a SHA-256 inventory without modifying source files."""

from __future__ import annotations
import argparse, csv, hashlib
from pathlib import Path

CHUNK_SIZE = 1024 * 1024

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()

def inventory(root: Path):
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        yield {
            "relative_path": str(path.relative_to(root)),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a SHA-256 file inventory.")
    parser.add_argument("source", type=Path, help="Directory to inventory")
    parser.add_argument("-o", "--output", type=Path, default=Path("hash_inventory.csv"))
    args = parser.parse_args()
    if not args.source.is_dir():
        parser.error("source must be a directory")

    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "size_bytes", "sha256"])
        writer.writeheader()
        writer.writerows(inventory(args.source))

if __name__ == "__main__":
    main()
