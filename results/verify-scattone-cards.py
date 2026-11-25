"""Run the repository's verification over the two corrected Scattone cards alone (issue #19).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-scattone-cards.py

`checks.report` is what `latticedb verify` reports: it recomputes each cited field's certificate
over the stored Gram and the stored value and compares it with the shard under `certificates/`.
A scratch corpus holding only 6JRX and 6JRY keeps the run to the two cards this item touched,
since the whole corpus has never finished verification in one process.
"""
import shutil
import tempfile
from pathlib import Path

from latticedb import checks, corpus

ROOT = Path(__file__).resolve().parent.parent
TAGS = ("6JRX", "6JRY")
FILES = ("certificates/cf.yaml", "certificates/17.yaml")


def main() -> int:
    with tempfile.TemporaryDirectory(dir=ROOT / ".scratch") as scratch:
        root = Path(scratch)
        (root / "lattices").mkdir()
        shutil.copy(ROOT / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
        shutil.copy(ROOT / corpus.RETIRED_FILE, root / corpus.RETIRED_FILE)
        (root / "certificates").mkdir()
        for name in FILES:
            shutil.copy(ROOT / name, root / name)
        for tag in TAGS:
            shutil.copy(ROOT / "lattices" / f"{tag}.md", root / "lattices" / f"{tag}.md")
        problems = checks.report(root)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problems in the verification of {' '.join(TAGS)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
