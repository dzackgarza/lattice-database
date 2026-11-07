"""Geometric objects use their Hodge numbers and the lattice corpus together."""

import re
from pathlib import Path

import frontmatter
import pytest
from pydantic import ValidationError

from latticedb import checks, site
from latticedb.geometric import ProjectiveComplexVariety
from latticedb.graphs import WeightedGraph

ROOT = Path(__file__).parent.parent


def test_k3_hodge_diamond_and_lattice_link_are_published(tmp_path: Path) -> None:
    lattice_directory = tmp_path / "lattices"
    lattice_directory.mkdir()
    for tag in (
        "0001",
        "0002",
        "0013",
        "0016",
        "0151",
        "027E",
        "027Z",
        "0283",
    ):
        (lattice_directory / f"{tag}.md").symlink_to(ROOT / "lattices" / f"{tag}.md")
    for name in ("families.yaml", "retired-tags.yaml", "geometric-bibliography.bib"):
        (tmp_path / name).symlink_to(ROOT / name)
    (tmp_path / "theory").symlink_to(ROOT / "theory", target_is_directory=True)
    geometric = tmp_path / "geometric-objects"
    geometric.mkdir()
    for slug in ("k3-surface", "k3-hilbert-2", "kummer-2"):
        (geometric / f"{slug}.md").symlink_to(ROOT / "geometric-objects" / f"{slug}.md")
    families = tmp_path / "geometric-families"
    families.mkdir()
    for slug in ("k3-hilbert", "generalized-kummer"):
        (families / f"{slug}.md").symlink_to(ROOT / "geometric-families" / f"{slug}.md")
    target = tmp_path / "site"
    site.build(tmp_path, target)
    html = (target / "geometric-objects" / "k3-surface.html").read_text()
    assert 'href="../tag/027E.html"' in html
    assert 'href="../tag/027E.html">U^3 + E8(-1)^2</a>' in html
    assert "H<sup>2</sup>(X; ℤ)/tors" in html
    assert '<div class="hodge-row">' in html
    assert "<span>1</span><span>20</span><span>1</span>" in html
    assert 'href="../geometric-objects/k3-surface.html"' in (target / "tag" / "027E.html").read_text()
    assert "Huybrechts" in html
    stylesheets = re.findall(r'<link rel="stylesheet" href="([^"]+)"', html)
    assert stylesheets == ["../assets/styles.css", "../assets/pages.css"]
    for stylesheet in stylesheets:
        published = (target / "geometric-objects" / stylesheet).resolve()
        assert published.read_bytes() == (ROOT / "src" / "latticedb" / "assets" / published.name).read_bytes()
    assert 'href="./geometric-families/k3-hilbert.html"' in (target / "geometric-objects.html").read_text()
    hilbert = (target / "geometric-objects" / "k3-hilbert-2.html").read_text()
    assert 'href="../tag/027Z.html"' in hilbert
    assert 'href="../geometric-families/k3-hilbert.html"' in hilbert
    assert "<span>1</span><span>21</span><span>232</span><span>21</span><span>1</span>" in hilbert
    kummer = (target / "geometric-objects" / "kummer-2.html").read_text()
    assert 'href="../tag/0283.html"' in kummer
    assert "<span>1</span><span>5</span><span>96</span><span>5</span><span>1</span>" in kummer


def test_symmetric_spaces_and_analytic_variety_are_published(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    for tag in ("0001", "0002", "0011", "0013", "0016", "0151"):
        (tmp_path / "lattices" / f"{tag}.md").symlink_to(ROOT / "lattices" / f"{tag}.md")
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    (tmp_path / "geometric-bibliography.bib").symlink_to(ROOT / "geometric-bibliography.bib")
    (tmp_path / "theory").symlink_to(ROOT / "theory", target_is_directory=True)
    (tmp_path / "geometric-objects").mkdir()
    (tmp_path / "graphs").symlink_to(ROOT / "graphs", target_is_directory=True)
    for slug in (
        "complex-projective-plane",
        "complex-projective-plane-analytic",
        "complex-hyperbolic-2-space",
        "three-sphere",
        "real-hyperbolic-3-space",
        "complex-quadric-q-5",
        "bdi-25-compact",
        "bdi-25-noncompact",
        "complex-cayley-plane",
        "eiii-compact",
        "eiii-noncompact",
    ):
        (tmp_path / "geometric-objects" / f"{slug}.md").symlink_to(ROOT / "geometric-objects" / f"{slug}.md")
    target = tmp_path / "site"
    site.build(tmp_path, target)
    algebraic_plane = (target / "geometric-objects" / "complex-projective-plane.html").read_text()
    analytic_plane = (target / "geometric-objects" / "complex-projective-plane-analytic.html").read_text()
    complex_ball = (target / "geometric-objects" / "complex-hyperbolic-2-space.html").read_text()
    real_hyperbolic = (target / "geometric-objects" / "real-hyperbolic-3-space.html").read_text()
    assert 'href="../geometric-objects/complex-projective-plane-analytic.html"' in algebraic_plane
    assert 'href="../geometric-objects/complex-projective-plane.html"' in analytic_plane
    assert 'href="../geometric-objects/complex-projective-plane-analytic.html"' in complex_ball
    assert 'href="../geometric-objects/three-sphere.html"' in real_hyperbolic
    assert 'href="../graphs/restricted-a1.html"' in real_hyperbolic
    assert 'href="../graphs/a2-su21-satake.html"' in complex_ball
    graph = (target / "graphs" / "a2-su21-satake.html").read_text()
    assert "Coxeter, Dynkin, simply laced, Satake" in graph
    assert 'href="../geometric-objects/complex-hyperbolic-2-space.html"' in graph
    vinberg = (target / "graphs" / "hyperbolic-triangle-2-3-infinity.html").read_text()
    assert "hyperbolic Coxeter polytope" in vinberg
    assert '<h2 id="hodge-diamond">' not in complex_ball
    quadric = (target / "geometric-objects" / "complex-quadric-q-5.html").read_text()
    bdi = (target / "geometric-objects" / "bdi-25-compact.html").read_text()
    exceptional = (target / "geometric-objects" / "eiii-noncompact.html").read_text()
    assert 'href="../geometric-objects/bdi-25-compact.html"' in quadric
    assert 'href="../geometric-objects/complex-quadric-q-5.html"' in bdi
    assert 'href="../geometric-objects/eiii-compact.html"' in exceptional


def test_graph_cards_derive_distinct_datum_from_shared_coxeter_order() -> None:
    def card(slug: str) -> WeightedGraph:
        return WeightedGraph.model_validate(frontmatter.load(ROOT / "graphs" / f"{slug}.md").metadata)

    b2 = card("b2-root-diagram")
    c2 = card("c2-root-diagram")
    assert b2.properties() == c2.properties() == ("Coxeter", "Dynkin")
    assert b2.cartan_matrix() != c2.cartan_matrix()
    assert card("a2-su21-satake").properties() == (
        "Coxeter",
        "Dynkin",
        "simply laced",
        "Satake",
    )
    assert card("hyperbolic-triangle-2-3-infinity").properties() == (
        "Coxeter",
        "hyperbolic Coxeter polytope",
    )
    # Four walls of norm 1 whose adjacent pairs have Gram entry -1 and whose opposite
    # pairs have Gram entry -3: the Gram determinant is (a + 1)^3 (a - 3) at a = 3, so
    # zero, and the signature is (2, 1, 1).  One negative eigenvalue, but a radical,
    # so these are not the walls of an acute-angled hyperbolic Coxeter polytope.
    walls = ("w1", "w2", "w3", "w4")
    degenerate = WeightedGraph.model_validate(
        {
            "slug": "degenerate-quadrilateral",
            "name": "Degenerate quadrilateral Gram matrix",
            "vertices": [{"id": wall, "weight": {"norm_squared": 1}} for wall in walls],
            "edges": [
                {
                    "id": f"{source}{target}",
                    "source": source,
                    "target": target,
                    "relation": "bond",
                    "weight": {"gram": gram, "order": "infinity"},
                }
                for source, target, gram in (
                    ("w1", "w2", -1),
                    ("w2", "w3", -1),
                    ("w3", "w4", -1),
                    ("w4", "w1", -1),
                    ("w1", "w3", -3),
                    ("w2", "w4", -3),
                )
            ],
        }
    )
    assert degenerate.properties() == ("Coxeter",)
    # One black node on A2 with the identity involution: X = {alpha1} gives
    # rho_X^vee = h_1 / 2 and alpha2(rho_X^vee) = -1/2, which is not an integer,
    # so the pair is not admissible (Kolb, Quantum symmetric Kac-Moody pairs,
    # Definition 2.3 (3)).
    invalid_satake = card("a2-su21-satake").model_dump()
    invalid_satake["vertices"][0]["weight"]["satake"] = "black"
    invalid_satake["edges"] = invalid_satake["edges"][:1]
    inadmissible = WeightedGraph.model_validate(invalid_satake)
    assert inadmissible.properties() == ("Coxeter", "Dynkin", "simply laced")
    with pytest.raises(ValueError):
        inadmissible.satake_diagram().validate_admissibility()
    arbitrary = WeightedGraph.model_validate(
        {
            "slug": "arbitrary",
            "name": "Weighted directed multigraph",
            "vertices": [
                {"id": "a", "weight": {"colour": ["red", 2]}},
                {"id": "b", "weight": "blue"},
            ],
            "edges": [
                {
                    "id": "loop",
                    "source": "a",
                    "target": "a",
                    "relation": "map",
                    "directed": True,
                    "weight": [1, "x"],
                },
                {
                    "id": "first",
                    "source": "a",
                    "target": "b",
                    "relation": "map",
                    "directed": True,
                },
                {
                    "id": "second",
                    "source": "a",
                    "target": "b",
                    "relation": "map",
                    "directed": True,
                },
            ],
        }
    )
    assert len(arbitrary.edges) == 3
    assert arbitrary.properties() == ()


def test_cohomology_link_must_match_the_stored_betti_number(tmp_path: Path) -> None:
    lattices = tmp_path / "lattices"
    lattices.mkdir()
    (lattices / "0016.md").symlink_to(ROOT / "lattices" / "0016.md")
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["cohomology_lattices"][0]["tag"] = "0016"
    geometric = tmp_path / "geometric-objects"
    geometric.mkdir()
    (geometric / "k3-surface.md").write_text(frontmatter.dumps(source))
    assert any("Betti number 22, but lattice 0016 has rank 2" in problem for problem in checks.report(tmp_path))


def test_k3_card_reads_its_transcribed_topology_and_hodge_numbers() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    record = ProjectiveComplexVariety.model_validate(source.metadata)
    assert record.betti_numbers == (1, 0, 22, 0, 1)
    assert record.euler_characteristic == 24
    assert record.hodge_number(1, 1) == 20
    assert record.hodge_number(1, 0) == 0

    source.metadata["betti_numbers"] = [1, 0, 22, 0]
    with pytest.raises(ValidationError, match="b_0 through b_"):
        ProjectiveComplexVariety.model_validate(source.metadata)


def test_the_hyperbolic_triangle_card_states_its_gram_signature_and_coxeter_data() -> None:
    """The (2,3,infinity) triangle: what its card states, and what the mirrors' Gram says.

    A card whose vertices carry `norm_squared` and whose bonds carry `gram` presents the inward unit
    normals of the walls of a Coxeter polytope (Vinberg, *Hyperbolic reflection groups*, section 2):
    the Gram matrix of those normals has $G_{vw} = -\\cos(\\pi/m_{vw})$ for a dihedral angle
    $\\pi/m_{vw}$, and the walls bound an acute-angled hyperbolic polytope exactly when the norms are
    positive, the off-diagonal entries are nonpositive and the signature is $(n-1, 1, 0)$
    (Vinberg, section 5). Nothing here is transcribed from a table: every number is recomputed from
    the card through the owner, so a decoration that does not present this object cannot pass.

    The card states three walls of norm 1 with Gram entries -1/2 and -1, so the angles are
    $\\pi/3$ and $\\pi/2$ with an ideal vertex: the $(2,3,\\infty)$ triangle group. Its Gram has
    determinant $-1/4$ and signature $(2, 1)$, one dimension short of free, which is what an
    acute-angled hyperbolic *triangle* in the hyperbolic plane looks like: $2 + 1 = 3$ walls.
    """
    from sage_extensions.rings import session_ring_objects

    QQ = session_ring_objects()["QQ"]
    card = WeightedGraph.model_validate(
        frontmatter.load(ROOT / "graphs" / "hyperbolic-triangle-2-3-infinity.md").metadata
    )
    form = card._gram_form()
    assert form is not None, "the card presents mirror normals with their Gram matrix"
    gram = form.gram_tensor()
    rank = gram.tensor_shape()[0]
    assert rank == 3, "three walls"

    # The stated Gram, entry by entry, as exact rationals of the owner's ring. Integer multiples are
    # compared rather than fractions constructed, so the comparison needs no rational conversion.
    assert all(gram[index, index] == QQ(1) for index in range(rank)), "every wall has norm 1"
    position = {vertex.id: index for index, vertex in enumerate(card.vertices)}
    wall1, wall2, wall3 = position["wall1"], position["wall2"], position["wall3"]
    assert gram[wall1, wall2] * 2 == QQ(-1), "the (1,2) entry is -1/2, an angle of pi/3"
    assert gram[wall2, wall3] == QQ(-1), "the (2,3) entry is -1, an ideal vertex"
    assert gram[wall1, wall3] == QQ(0), "the (1,3) entries are 0, an angle of pi/2"
    assert gram.is_symmetric(), "a Gram matrix is symmetric"

    # The determinant and the signature the Gram has, not a number the card claims.
    assert form.determinant() * 4 == QQ(-1), "the determinant is -1/4"
    signature = form.signature_pair()
    assert (signature.first(), signature.second()) == (2, 1), "signature (2, 1): an acute-angled polytope in H^2"
    assert signature.first() + signature.second() == rank, "nonzero determinant, so no radical"

    # The Coxeter data, read off the invariant matrix of the mirror pairs: 4 b^2 / (q q') is
    # 1 for an angle of pi/3 and 3 for pi/2, and the entry is infinite for a negative product.
    invariants = card.vinberg_invariant_matrix()
    assert invariants is not None
    coxeter = invariants.coxeter_matrix()
    # The matrix is the family of its entries in row-major order over the card's vertices, which is how
    # the owner presents it; the diagonal is 1 by convention and the pairs are symmetric.
    # The positions are the Python integers of the enumeration, not the owner's rank element: the
    # family's constructor admits a position, and an owned element is not one.
    entry = lambda left, right: coxeter[len(card.vertices) * left + right]  # noqa: E731
    assert entry(wall1, wall1) == entry(wall2, wall2) == entry(wall3, wall3) == 1
    assert entry(wall1, wall2) == entry(wall2, wall1) == 3, "the angle pi/3 is the Coxeter entry 3"
    assert entry(wall1, wall3) == entry(wall3, wall1) == 2, "the angle pi/2 is the Coxeter entry 2"
    assert str(entry(wall2, wall3)) == str(entry(wall3, wall2)) == "\u2135_0", "an ideal vertex is infinite"
    assert not invariants.is_simply_laced(), "the diagram has a bond that is not 2 or 3"
    assert invariants.is_acute_angled_hyperbolic_polytope_gram()
    assert card.properties() == ("Coxeter", "hyperbolic Coxeter polytope")




