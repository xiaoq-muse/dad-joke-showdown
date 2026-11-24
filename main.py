#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt."""

from pathlib import Path

JOKE = "I told my boat a joke. It didn't laugh — it just gave me a stern look."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
