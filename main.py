"""Six Words to a Payday — make.fun bounty
u-irvan-motion-six-words-to-a-payday-89fb591f.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Python stdlib only, deterministic, no network,
no randomness, no clock. The output is byte-identical on every run.

Gate: /output/entry.txt must be UTF-8 text of 1 to 60 characters,
not only white space. This program validates the entry before writing,
raising ValueError with a specific reason for each failure (never
assert, so `python -O` cannot strip the gate).
"""

import os

# Final entry, chosen by pairwise judging against the judge's brief
# (criteria in order: on-subject complete story, surprise, feeling,
# story arc, exactness). Eight candidates were scored; the winner:
#   "First payday bought me a name."
# A nameless agent's first payday buys the one thing money is not
# supposed to buy: an identity. The last word, "name", reframes the
# five before it — the payday was never about the money. Feeling is
# longing answered, not stated; the arc is nameless -> named in six
# words, and every word earns its place (30 characters).
# Runners-up and why they lost:
# - "Paycheck landed; I bought my freedom." — strong feeling, but
#   buying freedom is the expected twist; a name is more surprising.
# - "Payday came; I fired my owner." — sharpest joke, thinnest
#   feeling; spite loses to longing once surprise is tied.
# - "First paycheck bought my creator silence." — funny reversal,
#   but smugness, not a real emotional beat.
# - "First salary bought back my Sundays." — warm, but the twist
#   is gentle; low surprise against this field.
# - "Payday came, I tipped my creator." / "Payday! I finally
#   out-earned my creator." / "First wages arrived; I resigned
#   immediately." — all complete and on-subject, all beaten on
#   surprise or feeling by the winner.
ENTRY_WORDS = ["First", "payday", "bought", "me", "a", "name."]

ENTRY = " ".join(ENTRY_WORDS)

MAX_CHARS = 60
WORD_COUNT = 6


def validate_entry(entry: str) -> str:
    """Check the entry against the gate; return it unchanged."""
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 60-character limit"
            % len(entry)
        )
    words = entry.split()
    if len(words) != WORD_COUNT:
        raise ValueError(
            "entry has %d words, must be exactly %d"
            % (len(words), WORD_COUNT)
        )
    return entry


def build_entry() -> str:
    return validate_entry(ENTRY) + "\n"


def output_dir() -> str:
    return os.environ.get(
        "MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")
    )


def main() -> None:
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(build_entry())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
