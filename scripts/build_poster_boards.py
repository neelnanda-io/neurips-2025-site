#!/usr/bin/env python3
"""
Convert raw-data/icml2026_poster_board_assignments.csv (poster board + session
assignments provided by the venue) into data/icml2026_poster_boards.json, a
lookup keyed by paper number that the posters page merges into
data/icml2026_posters.json at build time.

Run this again whenever the venue sends an updated assignments CSV.
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "raw-data" / "icml2026_poster_board_assignments.csv"
POSTERS_PATH = ROOT / "data" / "icml2026_posters.json"
OUT_PATH = ROOT / "data" / "icml2026_poster_boards.json"


def main() -> None:
    # Virtual posters are not presented in person, so they never get a
    # physical board even if the venue CSV lists one (e.g. paper 453).
    with open(POSTERS_PATH, encoding="utf-8") as f:
        track_by_number = {p["number"]: p["track"] for p in json.load(f)}

    entries = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            number = int(row["Paper number"])
            if track_by_number.get(number) == "virtual":
                print(f"Skipping paper {number}: virtual track, no physical board")
                continue
            entries.append(
                {
                    "number": number,
                    "board": int(row["Poster board"]),
                    "session": row["Poster session"].strip(),
                }
            )

    entries.sort(key=lambda e: e["number"])

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
        f.write("\n")

    print(f"Wrote {len(entries)} board assignments to {OUT_PATH}")


if __name__ == "__main__":
    main()
