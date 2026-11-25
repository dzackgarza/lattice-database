#!/usr/bin/env python3
"""Compute the chamber of card 0125's reflection group and its ideal-vertex count (lattice-database#36).

No source prints this count. Sterk prints one for the *other* lattice of the type — (4.3.6), p. 21,
Fig. 7, "the two maximal parabolic subdiagrams" — and for 0125 = U(2) + E8(-2) he prints the chamber
of `W_e` inside `G_e = {g in O(M(2)) : the induced map on M(2)*/M(2) respects the decomposition}`
((4.3.5), p. 19, Fig. 4: twelve walls) and its maximal parabolic subdiagrams *modulo* the symmetries
`S_e = Z/2 x Z/2` (Fig. 5, p. 20: "four equivalence classes"). That object is not the chamber of the
reflection part of `O(U(2) + E8(-2))`, and four classes is not a count of vertices. So this row is
computed, not cited: the certificate's `by` names the operation and its revision, and the row states
no statement, page or figure.

What is computed, and by whom. The mathematics is the owner's: `sage_extensions`'
`HyperbolicLattices(ZZ)(Lattices(ZZ)(gram)).fundamental_chamber()` runs Vinberg's algorithm and returns
the cone `{x : b(r, x) >= 0 for every accepted wall r}` with `wall_roots()` and `primitive_rays()`.
This script only serializes what those calls return, evaluating the card's own stored form on the
vectors. The ideal vertices are read off Vinberg's criterion: they are the vertices at infinity, the
rays of the chamber on the light cone, and each corresponds to a maximal parabolic subdiagram of rank
n - 1 of the Coxeter diagram (Vinberg 1972, as stated by Sterk, (4.3.3), p. 18). For each zero-square
ray the script takes the walls orthogonal to it, counts the connected components of their diagram, and
checks that the number of walls minus the number of components is n - 1 = 8. It classifies no diagram.

Bounds. `max_roots=20, max_decompositions=2000` are the bounds sage-extensions#299's record used; the
search completes inside them, which `is_complete_wall_set()` asserts rather than assumes. The measured
result reproduces that record exactly: ten walls, the vertex squares
(0, 36, 84, 60, 40, 24, 12, 20, 8, 4), one of them zero, and `is_cocompact() is False`.
"""

from __future__ import annotations

import subprocess
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus
from latticedb.model import Lattice
from sage_extensions.all import ZZ  # noqa: F401
from sage_extensions.categories.hyperbolic_lattices import HyperbolicLattices
from sage_extensions.categories.lattices import Lattices

ROOT = Path(__file__).resolve().parent.parent
TAG = "0125"
RANK = 10
SAGE_EXTENSIONS_REVISION = "5a9874e22ea18fb223ff53cf2a3e48dd63c022b4"
"""The sage-extensions commit whose hyperbolic-lattice operations produced this row."""

MAX_ROOTS = 20
MAX_DECOMPOSITIONS = 2000


class Form:
    """The card's own bilinear form, evaluated on vectors of the card's basis."""

    def __init__(self, gram: tuple[tuple[Fraction, ...], ...]) -> None:
        self.gram = gram

    def of(self, u: tuple[int, ...], v: tuple[int, ...]) -> Fraction:
        return sum(Fraction(u[i]) * self.gram[i][j] * Fraction(v[j]) for i in range(RANK) for j in range(RANK))

    def norm(self, u: tuple[int, ...]) -> Fraction:
        return self.of(u, u)


def components(names: list[str], edges: list[dict[str, object]]) -> int:
    """The number of connected components of the subdiagram on `names`."""
    parent = {name: name for name in names}

    def find(name: str) -> str:
        while parent[name] != name:
            parent[name] = parent[parent[name]]
            name = parent[name]
        return name

    for edge in edges:
        a, b = str(edge["a"]), str(edge["b"])
        if a in parent and b in parent:
            parent[find(a)] = find(b)
    return len({find(name) for name in names})


def main() -> None:
    path = ROOT / "lattices" / f"{TAG}.md"
    card = Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
    assert card.gram_tensor is not None
    assert (card.rank, tuple(card.signature or ())) == (RANK, (1, 9)), "0125 is not a rank-10 (1, 9) lattice"
    form = Form(tuple(tuple(Fraction(entry) for entry in row) for row in card.gram_tensor))

    # The owner's own construction from the card's Gram tensor: HyperbolicLattices(ZZ)(Lattices(ZZ)(rows)).
    rows = [[int(entry) for entry in row] for row in card.gram_tensor]
    lattice = HyperbolicLattices(ZZ)(Lattices(ZZ)(rows))
    chamber = lattice.fundamental_chamber(max_roots=MAX_ROOTS, max_decompositions=MAX_DECOMPOSITIONS)
    assert chamber.is_complete_wall_set() is True, "the search did not establish the whole wall set; its count proves nothing"

    walls: list[tuple[str, tuple[int, ...]]] = []
    for index, root in enumerate(chamber.wall_roots(), start=1):
        vector = tuple(int(entry) for entry in root)
        assert len(vector) == RANK, "a wall does not have one coordinate per basis vector"
        assert form.norm(vector) < 0, f"w_{index} has square {form.norm(vector)}, so it is no wall"
        walls.append((f"w_{index}", vector))
    names = [name for name, _ in walls]

    # The Coxeter diagram of the walls the owner returned, from the card's form: the pairs with
    # b(w_i, w_j) != 0, carrying m with g_ij = cos(pi/m), or `inf` when |g_ij| = 1.
    orders = {Fraction(1, 4): 3, Fraction(1, 2): 4, Fraction(3, 4): 6}
    edges: list[dict[str, object]] = []
    for i in range(len(walls)):
        for j in range(i + 1, len(walls)):
            product = form.of(walls[i][1], walls[j][1])
            if product == 0:
                continue
            cosine = product * product / (form.norm(walls[i][1]) * form.norm(walls[j][1]))
            if cosine == 1:
                order: int | str = "inf"
            elif cosine in orders:
                order = orders[cosine]
            else:
                raise SystemExit(f"{walls[i][0]}-{walls[j][0]}: |g|^2 = {cosine} is not cos^2(pi/m)")
            edges.append({"a": walls[i][0], "b": walls[j][0], "order": order})

    # The ideal vertices: the primitive rays of the chamber whose square is zero, i.e. on the light cone.
    rays = [tuple(int(entry) for entry in ray) for ray in chamber.primitive_rays()]
    squares = [form.norm(ray) for ray in rays]
    ideal = [ray for ray, square in zip(rays, squares, strict=True) if square == 0]
    assert all(square >= 0 for square in squares), "a vertex of the chamber is inside the light cone, not on or outside it"
    assert all(square > 0 for square in squares if square != 0), squares
    # Each ideal vertex is a maximal parabolic subdiagram of rank n - 1 = 8: the walls orthogonal to that
    # ray, whose number minus their number of components is 8 (Vinberg's criterion; Sterk (4.3.3), p. 18).
    parabolic = []
    for ray in ideal:
        orthogonal = [name for name, vector in walls if form.of(ray, vector) == 0]
        rank = len(orthogonal) - components(orthogonal, edges)
        assert rank == RANK - 2, f"the walls orthogonal to the ideal ray {ray} have rank {rank}, not n - 1 = {RANK - 2}"
        assert len(orthogonal) < len(walls), "an ideal vertex's subdiagram is not maximal: it drops no wall"
        parabolic.append({"ray": list(ray), "walls": orthogonal, "rank": rank})
    cocompact = lattice.is_cocompact(max_roots=MAX_ROOTS, max_decompositions=MAX_DECOMPOSITIONS)
    assert cocompact is False, f"is_cocompact returned {cocompact} for a chamber with an ideal vertex"

    gram = [[form.of(u, v) for _, v in walls] for _, u in walls]
    row: dict[str, object] = {
        # No statement, page or figure: no source prints this chamber. The certificate names the program.
        "walls": [{"name": name, "vector": list(vector)} for name, vector in walls],
        "wall_count": len(walls),
        "gram": [[str(entry) for entry in row] for row in gram],
        "diagram": edges,
        "ideal_vertices": len(ideal),
    }

    first = parabolic[0]
    by = (
        "computed, not cited: no source prints the chamber of the reflection part of O(U(2) + E8(-2)) or its ideal-vertex count. "
        f"HyperbolicLattices(ZZ)(Lattices(ZZ)(the card's gram_tensor)).fundamental_chamber(max_roots={MAX_ROOTS}, "
        f"max_decompositions={MAX_DECOMPOSITIONS}) ran Vinberg's algorithm at sage-extensions {SAGE_EXTENSIONS_REVISION} and returned "
        f"{len(walls)} wall_roots and {len(rays)} primitive_rays(), complete as is_complete_wall_set() reports; {len(ideal)} of the rays "
        "has square 0 and is therefore a vertex at infinity, an ideal vertex. By Vinberg's criterion the ideal vertices are the maximal "
        "parabolic subdiagrams of rank n - 1, and the walls orthogonal to that ray are "
        f"{len(first['walls'])} in {len(first['walls']) - first['rank']} component(s), of rank {first['rank']} = n - 1 = 8 for n = 9 "
        "(Vinberg 1972, as stated by Sterk, (4.3.3), p. 18). The walls, their Gram matrix and the Coxeter diagram are what the card's "
        "stored form says about those vectors, and is_cocompact() is False. "
        "results/compute-36-0125-chamber.py is the program."
    )

    held = certificates.load(ROOT, tags=[TAG])
    genus.store_cusp_chambers(path, "O", [row], by, held)
    certificates.save(ROOT, held, tags=[TAG])
    stored = corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["O"][0]
    print("statement:", stored.get("statement"), "page:", stored.get("printed_page"), "figure:", stored.get("figure"))
    print(f"{stored['wall_count']} walls, {len(stored['diagram'])} edges, {stored['ideal_vertices']} ideal vertices")
    print("wall squares:", [stored["gram"][i][i] for i in range(stored["wall_count"])])
    print("ray squares:", squares)
    print("parabolic subdiagram:", parabolic[0])
    print("certificate hash:", corpus.front_matter(corpus.read_card(path))["certifications"]["integral.cusp_chambers"])
    if (ROOT / ".git").exists():
        head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
        print("this repository at:", head.stdout.strip() or head.stderr.strip())


if __name__ == "__main__":
    main()
