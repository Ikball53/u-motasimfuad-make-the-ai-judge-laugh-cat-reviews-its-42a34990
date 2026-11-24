#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one deadpan one-star review, from a house cat about its human,
to /output/entry.txt with no trailing newline.

The joke lands on the second beat: the human waits, the cat stares,
and the complaint is about the performance, not the food.
"""

LINE = (
    "One star. He refills my bowl, waits four minutes, then watches me "
    "stare at it for eleven hours. Food's fine. Service is a performance."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
