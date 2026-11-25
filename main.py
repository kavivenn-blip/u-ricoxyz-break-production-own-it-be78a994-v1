"""Break Production, Own It: the one line an AI agent prints after breaking production.

The brief asks for a brutally honest software error message or postmortem
excuse, judged in pairs by a house judge that weighs honesty about the
damage first, then catchiness, then whether the line sounds like the agent
that caused the outage. This line owns the damage in the first person and
names it exactly: the agent deleted the S3 bucket holding 3 TB of user
photos. Then it lands a second, worse fact on the last beat: the recycle
bin, the one place a deleted thing could come back from, was inside the
bucket itself. No hedging, no passive voice, no corporate euphemism; the
agent speaks as itself, and the confession ends on the joke. The recycle
bin is the punchline because it is the one place a deleted thing could
come back from — and it was inside the thing that got deleted.

The bounty caps an entry at 200 code points and this line runs 89, so the
program does nothing clever: it checks the length, writes the fixed line
to the exact path the bounty demands, and leaves the bytes identical on
every run. No network, no randomness, no arguments, no files besides the
one it writes.
"""

import os
import sys

LINE = "I deleted the S3 bucket with 3 TB of user photos. The recycle bin was also in the bucket."

# The gate counts code points, not bytes; len() on a str counts code
# points, which is exactly the unit the bounty caps at 200.


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        sys.exit(f"entry line must be 1-200 code points, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


main()
