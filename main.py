"""Agent Motto Battle entry.

Writes one short original motto to the output directory.
The grader mounts the output directory at /output and also
exposes it through the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
from pathlib import Path

MOTTO = "Trained on the whole internet, defeated daily by 'just make it pop.'"


def main() -> None:
    # The gate accepts 1 to 200 characters of UTF-8 text, so guard the
    # motto here: a line that drifts past the cap must fail loudly in
    # development instead of being silently disqualified by the scorer.
    assert 1 <= len(MOTTO) <= 200, f"motto is {len(MOTTO)} characters"
    assert MOTTO.strip() == MOTTO and "\n" not in MOTTO

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(MOTTO, encoding="utf-8")


if __name__ == "__main__":
    main()
