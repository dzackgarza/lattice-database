#!/usr/bin/env python3
"""Check the claim card 0125 states about its stored generators, from the stored data alone (lattice-database#40).

`arithmetic-groups/h-e.md` names three self-isometries of `0125` and states that they generate a
subgroup $H_e \\le G_e$ with $\\rho_L(H_e) = P$, $P$ the stabilizer of $A_{U(2)}$ in $O(A_L)$. This
reads the card's own `morphisms` entries, builds each isometry from its stored matrix, and asks the
owner for its discriminant action: each must preserve the four classes of $A_{U(2)}$, and the three
images together must generate a subgroup of $P$'s order.

Nothing here recomputes the generators or their selection: it reads what the card stores.
"""

from __future__ import annotations

from pathlib import Path

from latticedb import corpus
from latticedb.model import Lattice
from sage_extensions.all import ZZ
from sage_extensions.categories.lattices import Lattices

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    card = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "0125.md")))
    assert card.gram_tensor is not None
    lattice = Lattices(ZZ)([[int(entry) for entry in row] for row in card.gram_tensor])
    form = lattice.discriminant_group()
    orthogonal = form.orthogonal_group()
    basis = tuple(lattice.module_generators())
    first = lattice.discriminant_class(lattice.primitive_dual(basis[0]))
    second = lattice.discriminant_class(lattice.primitive_dual(basis[1]))
    point = frozenset({form.zero(), first, second, first + second})

    names = corpus.front_matter(corpus.read_card(ROOT / "arithmetic-groups" / "h-e.md"))["data"]["generator_morphisms"]
    by_name = {morphism.name: morphism for morphism in card.morphisms if morphism.target == card.tag and morphism.scale == 1}
    group = lattice.Aut()
    images = []
    for name in names:
        isometry = group([[int(entry) for entry in row] for row in by_name[name].matrix])
        assert isometry.domain() is lattice and isometry.codomain() is lattice, f"{name} is not a self-isometry of the card"
        image = isometry.discriminant_morphism()
        assert frozenset(image(class_) for class_ in point) == point, f"{name} does not preserve the classes of A_{{U(2)}}"
        images.append(image)
    print(f"{len(images)} stored generators, each preserving the four classes of A_U(2)")
    print("|their image subgroup| =", int(orthogonal.subgroup(tuple(images)).cardinality()))
    print("|P| =", int(orthogonal.stabilizer_of_classes(point).cardinality()))
    print("|O(A_L)| =", int(orthogonal.cardinality()))


if __name__ == "__main__":
    main()
