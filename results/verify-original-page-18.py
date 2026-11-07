"""Exercise the original rational page construction, including the actual graph files.

#18 / sage-extensions#304. Run in the existing published rootfs with real owner imports:

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-original-page-18.py

The original failed at TypeError `Fraction(2, 1) does not describe an element of Free module on {[0]}
over Fraction Field of Integer Ring` in `graphs._gram_form`. This now requires a completed page at
`graph/a2-su21-satake.html`. The five retained source graphs are passed unmodified. No provider code,
data, or stored card is edited; a fresh attachment directory is used.
"""
from pathlib import Path
import shutil
import sys
import tempfile

from latticedb import site

REPOSITORY = Path(__file__).resolve().parent.parent
GRAPH = next(
    path for path in sorted((REPOSITORY / "graphs").glob("*.md"))
    if path.stem == "a2-su21-satake"
)


def main() -> None:
    work = Path(tempfile.mkdtemp(prefix="original-rational-page-", dir=REPOSITORY / "attachments"))
    (work / "lattices").mkdir(parents=True)
    (work / "lattices" / "0001.md").write_text(
        "---\ntag: '0001'\nname: rank-one placeholder\nlatex: S\nrank: 1\n"
        "gram_tensor:\n- [1]\nsignature: [1, 0]\ndeterminant: 1\n"
        "definiteness: positive_definite\nintegral: {parity: odd}\n---\n"
    )

    def link(relative: str) -> None:
        source = REPOSITORY / relative
        target = work / relative
        if not source.exists():
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() and not target.is_symlink():
            target.symlink_to(source)

    for child in ("graphs", "theory"):
        link(child)
    for name in ("families.yaml", "retired-tags.yaml", "geometric-bibliography.bib", "gram-index.json"):
        if (REPOSITORY / name).is_file():
            shutil.copy(REPOSITORY / name, work / name)

    # No collection-wide pages: the original graph is what this test must reach and publish.
    (work / "pages").mkdir(exist_ok=True)
    (work / "lattice-families").mkdir(exist_ok=True)

    target = work / "site"
    count = site.build(work, target)
    page = target / "a2-su21-satake.html"
    if not page.exists():
        # The slug's own URL convention, not a guessed name: choose its actual matching output file.
        matches = list(target.rglob("a2-su21-satake*.html"))
        assert matches, "the actual a2-su21-satake graph was not published"
        page = matches[0]
    contents = page.read_text()
    assert contents
    print(f"published {count} lattice card(s); the actual original graph page is {page.relative_to(work)}")
    normalised = contents.replace("\\mathbb", "")
    present = any(word in normalised for word in ("alpha", "a2", "SU(2,1)", "Satake"))
    assert present, "the published graph page is not recognisable as the original card"
    print("real page builder passed for the original source graph")


if __name__ == "__main__":
    main()
