"""Card 0125 states the generators of Sterk's discriminant stabilizer, and their certificate (lattice-database#40).

The card's three self-isometries generate a subgroup $H_e \\le G_e$ with $\\rho_L(H_e) = P$, $P$ the
stabilizer of $A_{U(2)}$ in $O(A_L)$; the arithmetic-group card of $G_e$ names them and claims none of
them as a generator of $G_e$. These assertions read the stored cards and the ledger: no preamble
object is built here, so a broken name, a stale hash or a claim moved to the wrong card fails in the
commit gate instead of in a certification job.
"""

from __future__ import annotations

import re
from fractions import Fraction
from pathlib import Path

import frontmatter

from latticedb import certificates, corpus, genus
from latticedb.catalogues import ArithmeticGroup
from latticedb.model import Lattice

ROOT = Path(__file__).parent.parent
TAG = "0125"
SLUG = "h-e"
PARENT = "g-e"
FIELD = f"arithmetic-group.{SLUG}.generator_morphisms"


def _lattice() -> Lattice:
    return Lattice.model_validate(frontmatter.load(str(ROOT / "lattices" / f"{TAG}.md")).metadata)


def _group(slug: str) -> tuple[ArithmeticGroup, str]:
    document = frontmatter.load(str(ROOT / "arithmetic-groups" / f"{slug}.md"))
    return ArithmeticGroup.model_validate(document.metadata), document.content


def _preserves(matrix: list[list[int]], gram: list[list[int]]) -> bool:
    size = len(gram)
    if len(matrix) != size or any(len(row) != size for row in matrix):
        return False
    product = [[sum(matrix[k][i] * gram[k][l] * matrix[l][j] for k in range(size) for l in range(size)) for j in range(size)] for i in range(size)]
    return product == [[int(entry) for entry in row] for row in gram]


def _determinant(matrix: list[list[int]]) -> int:
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    size = len(rows)
    value = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column] != 0), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        value *= rows[column][column]
        scale = rows[column][column]
        rows[column] = [entry / scale for entry in rows[column]]
        for row in range(column + 1, size):
            if rows[row][column] != 0:
                factor = rows[row][column]
                rows[row] = [a - factor * b for a, b in zip(rows[row], rows[column], strict=True)]
    return int(value)


def _named(card: Lattice, names) -> list:
    """The one scale-1 self-morphism of `card` each name denotes."""
    by_name = [morphism for morphism in card.morphisms if morphism.target == card.tag and morphism.scale == 1]
    chosen = []
    for name in names:
        matches = [morphism for morphism in by_name if morphism.name == name]
        assert len(matches) == 1, f"{name} names {len(matches)} scale-1 self-morphisms of {card.tag}"
        chosen.append(matches[0])
    return chosen


def test_the_card_states_the_generators_on_the_subgroup_that_names_them() -> None:
    """`0125` names `h-e`; the `h-e` card names the generators and states the relation to `G_e`."""
    card = _lattice()
    assert SLUG in card.arithmetic_groups
    subgroup, prose = _group(SLUG)
    assert (subgroup.lattice, subgroup.parent_group) == (TAG, PARENT)
    names = list(subgroup.data.generator_morphisms or ())
    assert names, "the subgroup card states the generators, so they are not claimed for G_e"
    assert len(set(names)) == len(names)
    assert len(_named(card, names)) == len(names)
    assert "rho_L(H_e) = P" in prose, "the row states the relation that makes the generators a generating set of H_e"
    assert subgroup.data.index_in_orthogonal_group is None, "no index is claimed for a subgroup the kernel generators would decide"


def test_the_card_of_g_e_names_them_and_claims_no_generator_of_g_e() -> None:
    """`G_e`'s card names the stored isometries and states no generating set of `G_e` itself."""
    subgroup, prose = _group(PARENT)
    names = list(_group(SLUG)[0].data.generator_morphisms or ())
    assert subgroup.data.generator_morphisms is None, "G_e's generators are absent and the card claims none"
    assert subgroup.data.index_in_orthogonal_group is None
    for name in names:
        assert name in prose, f"the card of G_e does not name {name}"
    assert "not** generators of $G_e$" in prose or "not generators of $G_e$" in prose


def test_the_certificate_commits_to_the_stored_matrices() -> None:
    """The card cites a completed certificate over its Gram tensor and the sorted matrices."""
    card = _lattice()
    subgroup, _prose = _group(SLUG)
    names = list(subgroup.data.generator_morphisms or ())
    computation = genus.name(TAG, FIELD, card.definiteness)
    value = genus.certified_value(FIELD, names, card)
    expected = certificates.certification_hash(computation, card, value)
    assert card.certifications[FIELD] == expected, "the cited hash is not the one the stored matrices give"
    held = certificates.load(ROOT, tags=[TAG])
    assert computation in held and held[computation].hash == expected
    assert held[computation].by.strip(), "the certificate names its provenance"
    assert re.search(r"\b[0-9a-f]{40}\b", held[computation].by), "the provenance names the owner revision the computation ran at"


def test_every_stored_generator_is_an_isometry_of_the_card() -> None:
    """Each name the subgroup card lists denotes an isometry, whatever set of members is stored."""
    card = _lattice()
    names = list(_group(SLUG)[0].data.generator_morphisms or ())
    gram = [[int(entry) for entry in row] for row in card.gram_tensor]
    assert names, "the subgroup card states its generators"
    for morphism in _named(card, names):
        matrix = [[int(entry) for entry in row] for row in morphism.matrix]
        assert _preserves(matrix, gram), f"{morphism.name} does not preserve the form"
        assert abs(_determinant(matrix)) == 1, f"{morphism.name} is not unimodular"


def test_the_stated_cardinality_is_the_certified_one() -> None:
    """The `h-e` card's cardinality is cited on `0125`, and that citation is the certificate's hash.

    The value itself is not asserted here: what the gate can decide without running the computation
    is that the card cites a completed certificate over the value it states, so a value edited away
    from its certificate fails here. `results/check-40-h-e-cardinality.py` recomputes the value from
    the stored matrices and the card's Gram tensor.
    """
    card = _lattice()
    subgroup, _prose = _group(SLUG)
    field = f"arithmetic-group.{SLUG}.cardinality"
    computation = genus.name(TAG, field, card.definiteness)
    value = genus.certified_value(field, subgroup.data.cardinality, card)
    expected = certificates.certification_hash(computation, card, value)
    assert card.certifications.get(field) == expected, "the card does not cite the hash of its stated cardinality"
    held = certificates.load(ROOT, tags=[TAG])
    assert computation in held and held[computation].hash == expected
    assert isinstance(subgroup.data.cardinality, int), "the nine stored reflections generate a finite group"
