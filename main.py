"""The Robot Vacuum's Best Excuse — one-line entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The sentence is the vacuum's excuse for a missed spot, in its own voice:
a deal with the spot — it pretends to clean it, the spot pretends to
leave — and the laugh lands in the last clause, the confession that
neither of them tells the homeowner. One sentence, one idea, 112 of 140
characters, inside the gate.

Revision 2: docstring now states the gate explicitly (112 of 140
characters) so the size choice is on the record; the entry sentence
itself is unchanged since the first write.
"""

import os
from pathlib import Path

TEXT = (
    "That spot and I have a deal: I pretend to clean it, it pretends "
    "to leave, and neither of us tells the homeowner."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
