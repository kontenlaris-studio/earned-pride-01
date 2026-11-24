#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry."""
from pathlib import Path

ENTRY = (
    "I kept a houseplant alive for a full year. "
    "It began as a funeral with better lighting."
)
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
