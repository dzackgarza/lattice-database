"""Correct Scattone cards 6JRX/6JRY and renew their citation-certified orbit rows (issue #19).

Run in the published image:

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/correct-scattone-cards.py

The new Gram is the source's own sum: Scattone, Mem. Amer. Math. Soc. 374 (1987), Section 1.1,
equation (1.1.1), p. 3 states $L_k = \\langle -2k \\rangle \\oplus H^2 \\oplus E_8^2$, with the two
unimodular $E_8$ summands introduced on p. 2. The $E_8$ summand here is Sage's
`CartanMatrix(['E', 8])`, negated, since in this card's basis both are negative definite; its
determinant is 1, so the sum has determinant $-2k$ and discriminant group $\\mathbb{Z}/2k$.

The cited rows are kept exactly as they stand, with their citations, and every field certificate
is regenerated over the corrected tensor through `genus.cite_orbit_row`. No old hash is copied
forward and no value is invented: `determinant` and `discriminant_group` are the determinant
invariants of the source's stated decomposition.
"""
from pathlib import Path

import frontmatter
import yaml
from sage.all import CartanMatrix, block_diagonal_matrix, matrix, ZZ
from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects

from latticedb import certificates, genus, records
from latticedb.model import Lattice

ROOT = Path(__file__).resolve().parent.parent
RING = session_ring_objects()["ZZ"]
SCATTONE = {
    "citation": (
        "J. Scattone, \"On the compactification of moduli spaces for algebraic K3 surfaces\", "
        "Mem. Amer. Math. Soc. 374 (1987), Section 1.1, equation (1.1.1), p. 3: "
        "L_k = <-2k> + H^2 + E8^2, the two unimodular E8 summands introduced on p. 2."
    ),
    "url": "https://doi.org/10.1090/memo/0374",
}
LOCATOR = (
    "\n\nScattone states the decomposition on p. 3, equation (1.1.1), of Section 1.1: "
    "$L_k = \\langle -2k \\rangle \\oplus H^2 \\oplus E_8^2$, the two unimodular $E_8$ summands "
    "introduced on p. 2. In this card's basis both $E_8$ summands are negative definite, so each "
    "is $-1$ times the Cartan matrix of $E_8$; that matrix is unimodular, and the determinant of "
    "the whole sum is therefore $-2k$, with discriminant group $\\mathbb{Z}/2k$."
)
WRONG_DETERMINANT = {1: "$-131072$", 2: "$-262144$"}


def expected(k: int):
    """The source's sum $\\langle -2k \\rangle \\oplus H^2 \\oplus E_8(-1)^2$ in an explicit basis."""
    e8 = matrix(ZZ, -CartanMatrix(["E", 8]))
    u = matrix(ZZ, [[0, 1], [1, 0]])
    return block_diagonal_matrix(u, u, e8, e8, matrix(ZZ, [[-2 * k]]))


def main() -> None:
    held = certificates.load(ROOT)
    for tag, k in (("6JRX", 1), ("6JRY", 2)):
        path = ROOT / "lattices" / f"{tag}.md"
        document = frontmatter.load(str(path))
        old = document.metadata
        rows = (old.get("integral") or {}).get("primitive_orbits")
        assert rows, f"{tag}: the cited Scattone rows must be retained"

        source = expected(k)
        gram = [[int(value) for value in row] for row in source.rows()]
        assert gram == [[int(value) for value in row] for row in matrix(ZZ, gram).transpose().rows()], tag
        assert all(gram[i][i] % 2 == 0 for i in range(len(gram))), f"{tag}: the sum is even"

        owned = Lattices(RING)(gram)
        assert int(owned.determinant()) == -2 * k, (tag, int(owned.determinant()))
        assert tuple(int(value) for value in owned.signature_pair()) == (2, 19), tag
        factors = [2] if k == 1 else [4]
        assert int(owned.discriminant_group().cardinality()) == 2 * k, tag
        smith = [int(value) for value in matrix(ZZ, gram).smith_form()[0].diagonal()]
        assert [value for value in smith if value > 1] == factors, (tag, smith)

        prose = document.content
        assert prose.count(WRONG_DETERMINANT[k]) == 1, f"{tag}: the stored prose states the old determinant"
        prose = prose.replace(WRONG_DETERMINANT[k], f"${-2 * k}$") + LOCATOR
        assert "$-131072$" not in prose and "$-262144$" not in prose

        metadata = {
            "tag": tag,
            "name": old["name"],
            "latex": old["latex"],
            "aliases": old["aliases"],
            "rank": 21,
            "gram_tensor": gram,
            "signature": [2, 19],
            "determinant": -2 * k,
            "definiteness": "indefinite",
            "integral": {
                "parity": "even",
                "discriminant_group": factors,
                "primitive_orbits": rows,
            },
            "indefinite": {"isotropic": True},
            "references": [SCATTONE],
        }
        Lattice.model_validate(metadata)
        path.write_text(records.record_text(metadata, prose))

        # Re-certify every cited row against the corrected input, through the citation route.
        for group in ("O", "O+", "Otilde+"):
            series = dict(rows[group])
            reference = dict(series.get("reference") or {})
            assert "Scattone" in reference["citation"], (tag, group)
            genus.cite_orbit_row(path, group, series, reference, held)

        card = Lattice.model_validate(frontmatter.load(str(path)).metadata)
        assert card.determinant == -2 * k
        assert list(card.integral.discriminant_group or ()) == factors
        assert set(card.integral.primitive_orbits) == {"O", "O+", "Otilde+"}
        print(
            tag,
            "rank", card.rank,
            "determinant", card.determinant,
            "discriminant_group", list(card.integral.discriminant_group or ()),
            "certificate", card.certifications["integral.primitive_orbits"],
        )
    certificates.save(ROOT, held, tags={"6JRX", "6JRY"})


if __name__ == "__main__":
    main()
