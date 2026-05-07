#!/usr/bin/env python3
"""Produce a filesystem-safe concept folder name.

Usage: python concept_slug.py 1 "Celeb Baby Reveal"
Output: 01_Celeb_Baby_Reveal
"""
import re
import sys


def slug(idx: int, name: str, max_chars: int = 50) -> str:
    safe = re.sub(r"[^\w\s-]", "", name).strip()
    safe = re.sub(r"\s+", "_", safe)[:max_chars]
    return f"{idx:02d}_{safe}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: concept_slug.py <index> <concept name>", file=sys.stderr)
        sys.exit(1)
    print(slug(int(sys.argv[1]), " ".join(sys.argv[2:])))
