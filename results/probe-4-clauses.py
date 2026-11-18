"""#4 body clauses: no fallback in `_rational`; an undecided value stores nothing."""
import shutil, tempfile
from pathlib import Path
import frontmatter
from latticedb import corpus, genus, records, sage_genus

print("--- no guard and no fallback: a non-rational raises, in the serializer it reaches first")
for bad in (1.5, "3/2", None, [1]):
    try:
        sage_genus._rational(bad)
        print(f"  {bad!r}: RETURNED (a fallback exists)")
    except Exception as error:
        print(f"  {bad!r}: {type(error).__name__}: {error}")

print("--- an undecided value stores nothing")
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    (root / "lattices").mkdir()
    shutil.copy(Path("families.yaml"), root / "families.yaml")
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    path = root / "lattices" / "0022.md"
    document = frontmatter.load("lattices/0022.md")
    del document.metadata["integral"]["local_densities"]
    del document.metadata["certifications"]["integral.local_densities"]
    path.write_text(records.record_text(corpus.front_matter(document), document.content))
    genus.store(path, {"local_densities": None, "genus_symbol": None})
    after = frontmatter.load(str(path)).metadata["integral"]
    print("  integral keys after storing two Nones:", sorted(after))
    assert "local_densities" not in after, after
    print("  local_densities still absent: True")
