"""One Letter for Your Day — writes exactly one character to /output/entry.txt.

Final letter: F for "frazzled".

Revision pass: the first draft was Z for "zombie", but Z is literally
the example in the competition rules — the obvious pick, penalised by
the final criterion. F wins instead: "frazzled" paints one specific
picture (hair up, coffee down the shirt, three tabs of life open at
once), it is funny because it is slightly undignified, it is true to
a day almost everyone has every week, and the letter fits the word
with a frayed, fizzy alliteration no other candidate matched.
"""
import os

LETTER = "F"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
