#!/usr/bin/env python3
"""Inventory SQLite databases and detect WAL/SHM companions.

Databases are opened using SQLite read-only URI mode. Run against working
copies when companion-file behavior or source preservation is a concern.
"""

from __future__ import annotations
import argparse, csv, sqlite3
from pathlib import Path

SQLITE_MAGIC = b"SQLite format 3\x00"

def is_sqlite(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(16) == SQLITE_MAGIC
    except OSError:
        return False

def inspect(path: Path, root: Path) -> dict[str, object]:
    row: dict[str, object] = {
        "relative_path": str(path.relative_to(root)),
        "size_bytes": path.stat().st_size,
        "wal_present": Path(str(path) + "-wal").exists(),
        "shm_present": Path(str(path) + "-shm").exists(),
        "table_count": "",
        "user_version": "",
        "error": "",
    }
    try:
        uri = f"{path.resolve().as_uri()}?mode=ro"
        with sqlite3.connect(uri, uri=True) as db:
            row["table_count"] = db.execute(
                "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
            ).fetchone()[0]
            row["user_version"] = db.execute("PRAGMA user_version").fetchone()[0]
    except sqlite3.Error as exc:
        row["error"] = str(exc)
    return row

def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory SQLite databases.")
    parser.add_argument("source", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("sqlite_inventory.csv"))
    args = parser.parse_args()
    if not args.source.is_dir():
        parser.error("source must be a directory")

    rows = [inspect(p, args.source) for p in sorted(args.source.rglob("*"))
            if p.is_file() and is_sqlite(p)]
    fields = ["relative_path", "size_bytes", "wal_present", "shm_present",
              "table_count", "user_version", "error"]
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
