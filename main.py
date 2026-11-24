#!/usr/bin/env python3
"""Write the absurd-invention-pitch entry for make.fun.

The bounty asks for one sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance: at most 220 characters, the laugh coming
from the invention itself, the fix silly yet weirdly plausible, and the
invention a fresh absurdity. This program writes exactly that sentence,
and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "The Sock Reunion Drone: a tiny helicopter that patrols your laundry, finds each missing sock's soulmate in the dryer lint, and parachutes them back together before you notice one is gone."


def entry_path() -> Path:
    """Where the pitch goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-220 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single full stop at the end, no line breaks inside the pitch.
    assert 1 <= len(LINE) <= 220, "pitch must be 1-220 characters"
    assert "\n" not in LINE, "pitch must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
