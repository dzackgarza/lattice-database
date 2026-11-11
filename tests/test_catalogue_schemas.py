"""The additional catalogues retain their mathematical links to existing records."""

from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb import certificates, checks, corpus
from latticedb.catalogues import ArithmeticGroup, LatticeFamily, LieGroup
from latticedb.geometric import GeometricObject

ROOT = Path(__file__).parent.parent


def test_shipped_group_cards_have_first_class_lie_and_arithmetic_owners() -> None:
    lie = [LieGroup.model_validate(frontmatter.load(str(path)).metadata) for path in (ROOT / "lie-groups").glob("*.md")]
    arithmetic = [ArithmeticGroup.model_validate(frontmatter.load(str(path)).metadata) for path in (ROOT / "arithmetic-groups").glob("*.md")]
    by_slug = {group.slug: group for group in lie}
    assert by_slug["o-2-10"].orthogonal_signature == (2, 10)
    assert by_slug["o-2-10"].dimension == 66
    assert by_slug["o-2-10"].real_rank == 2
    assert all(group.ambient_lie_group in by_slug for group in arithmetic)
    enriques = frontmatter.load(str(ROOT / "lattices" / "029J.md")).metadata
    assert enriques["orthogonal_group"] == "o-t-en"
    assert "gamma-en-2" in enriques["arithmetic_groups"]
    assert next(group for group in arithmetic if group.slug == "o-t-en").standard_name == "O"


def _record(
    path: Path,
    metadata: dict[str, str | int | bool | list[str] | list[int] | list[list[int]]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter.dumps(frontmatter.Post("", **metadata)))


def test_group_orbit_and_genus_links_use_the_existing_lattice_records(
    tmp_path: Path,
) -> None:
    lattices = tmp_path / "lattices"
    lattices.mkdir()
    for tag in ("0012",):
        (lattices / f"{tag}.md").symlink_to(ROOT / "lattices" / f"{tag}.md")
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    lattice = frontmatter.load(str(ROOT / "lattices" / "02BG.md"))
    generators = [entry["name"] for entry in lattice.metadata["morphisms"] if entry["target"] == "02BG"]
    lattice.metadata["morphisms"] = [entry for entry in lattice.metadata["morphisms"] if entry["target"] == "02BG"]
    lattice.metadata["arithmetic_groups"] = ["leech-q8"]
    (lattices / "02BG.md").write_text(frontmatter.dumps(lattice))
    for tag in ("0012", "02BG"):
        document = frontmatter.load(str(lattices / f"{tag}.md"))
        p, q = sorted(document.metadata["signature"])
        path = tmp_path / "lie-groups" / f"o-{p}-{q}.md"
        path.parent.mkdir(exist_ok=True)
        path.symlink_to(ROOT / "lie-groups" / path.name)
    p, q = sorted(lattice.metadata["signature"])
    group_path = tmp_path / "arithmetic-groups" / "leech-q8.md"
    _record(
        group_path,
        {
            "slug": "leech-q8",
            "name": "Leech Q8",
            "latex": "Q_8",
            "lattice": "02BG",
            "ambient_lie_group": f"o-{p}-{q}",
            "data": {
                "generator_morphisms": generators,
                "cardinality": 8,
                "orbits": [{"square": 4, "representatives": [[1] + [0] * 16]}],
            },
        },
    )
    _record(
        tmp_path / "genera" / "a2.md",
        {
            "slug": "a2",
            "signature": [2, 0],
            "determinant": 3,
            "parity": "even",
            "symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
            "representative_tags": ["0012"],
            "class_number": 1,
            "representatives_complete": True,
            "mass": "1/12",
        },
    )
    loaded = corpus.load(tmp_path)
    assert loaded.arithmetic_groups[0].value.data.cardinality == 8
    assert loaded.genera[0].value.mass == Fraction(1, 12)


def _arithmetic_group(generators: list[str] | None) -> dict[str, object]:
    """An arithmetic-group card for A2 whose generators are named on the A2 card."""
    data: dict[str, object] = {"cardinality": 6}
    if generators is not None:
        data["generator_morphisms"] = generators
    return {
        "slug": "a2-rotations",
        "name": "Rotations of A2",
        "latex": "C_{3}",
        "lattice": "0012",
        "ambient_lie_group": "o-0-2",
        "data": data,
    }


def test_an_arithmetic_group_generator_is_one_scale_one_self_isometry_of_its_lattice(
    tmp_path: Path,
) -> None:
    """Each name in `data.generator_morphisms` is one isometry L -> L on the card it names.

    #34: the fixture holds the certificates its copies cite. Without them `checks` reports every cited
    value of 0012 as contradicting a completed certificate the corpus does not hold — the generator
    morphisms among them — and the filter below would be testing that instead of the generator list.
    0012's own generator row does agree with its certificate, which is what the second assertion keeps.
    """
    (tmp_path / "lattices").mkdir()
    (tmp_path / "lattices" / "0012.md").symlink_to(ROOT / "lattices" / "0012.md")
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    (tmp_path / "lie-groups").mkdir()
    (tmp_path / "lie-groups" / "o-0-2.md").symlink_to(ROOT / "lie-groups" / "o-0-2.md")
    # Only this corpus's own card is certified here, so only its certificates join the fixture.
    held = {name: certificate for name, certificate in certificates.load(ROOT, tags=["0012"]).items() if name.split(" ", 1)[0] == "0012"}
    certificates.save(tmp_path, held, tags=["0012"])
    path = tmp_path / "arithmetic-groups" / "a2-rotations.md"
    _record(path, _arithmetic_group(["O(L) generator 1"]))
    problems = checks.report(tmp_path)
    assert [problem for problem in problems if "contradicts its completed computation certificate" in problem] == []
    assert [problem for problem in problems if "generator" in problem] == []

    _record(path, _arithmetic_group(["not an isometry", "O(L) generator 1", "O(L) generator 1"]))
    problems = checks.report(tmp_path)
    assert any("generator not an isometry is not one scale-1 self-morphism of 0012" in problem for problem in problems)
    assert any("each generator of 0012 occurs once in the generator list" in problem for problem in problems)


def test_an_arithmetic_group_states_its_line_plane_and_flag_counts() -> None:
    """#10: the three stratum counts are nonnegative integers, and a flag count requires both strata."""
    record = _arithmetic_group(None)
    data = dict(record["data"])  # type: ignore[arg-type]
    stated = ArithmeticGroup.model_validate(record | {"data": data | {"line_orbits": 1, "plane_orbits": 4, "flag_orbits": 7}})
    assert (stated.data.line_orbits, stated.data.plane_orbits, stated.data.flag_orbits) == (1, 4, 7)
    assert ArithmeticGroup.model_validate(record | {"data": data | {"plane_orbits": 9}}).data.plane_orbits == 9
    assert ArithmeticGroup.model_validate(record).data.flag_orbits is None
    with pytest.raises(ValidationError, match="a flag count requires"):
        ArithmeticGroup.model_validate(record | {"data": data | {"flag_orbits": 7}})
    with pytest.raises(ValidationError):
        ArithmeticGroup.model_validate(record | {"data": data | {"line_orbits": -1}})


def test_an_arithmetic_group_index_is_a_positive_integer_or_absent() -> None:
    record = _arithmetic_group(None)
    data = dict(record["data"])  # type: ignore[arg-type]
    assert ArithmeticGroup.model_validate(record).data.index_in_orthogonal_group is None
    assert ArithmeticGroup.model_validate(record | {"data": data | {"index_in_orthogonal_group": 67456}}).data.index_in_orthogonal_group == 67456
    with pytest.raises(ValidationError):
        ArithmeticGroup.model_validate(record | {"data": data | {"index_in_orthogonal_group": 0}})


def test_the_coble_card_and_its_group_cards_state_only_their_defining_data() -> None:
    """#7, #34: T_Co states its defining data and whatever `certify` has certified, and nothing else.

    CI certifies the fields of this card one at a time — #34 found `integral.discriminant_form` certified
    on it — so the test does not pin which of them are present. It asserts the rule that holds either
    way: no block of the card gains a field that is not certified, every certificate names a field the
    card states, and the blocks that #7 leaves to `certify` and to sage-extensions#286 are still absent.
    The certified value is not to be deleted to make this pass.
    """
    card = frontmatter.load(str(ROOT / "lattices" / "6JRR.md")).metadata
    assert card["name"] == "T_Co"
    assert (card["rank"], card["signature"], card["determinant"], card["definiteness"]) == (11, [2, 9], -2048, "indefinite")
    assert card["gram_tensor"][0][0] == 2 and card["gram_tensor"][1][2] == 2 and card["gram_tensor"][3][3] == -4
    defining = {"integral.parity", "indefinite.isotropic"}
    stated = {
        f"{block}.{field}"
        for block in ("form", "integral", "automorphisms", "definite", "root_span", "root_sublattice", "indefinite", "hyperbolic")
        for field in (card.get(block) or {})
    }
    certified = set(card.get("certifications") or {}) - {"derive"}
    assert stated - defining == certified, "every field of T_Co beyond its defining data is one it certifies, and every certificate names a stated field"
    assert "definite" not in card and "root_span" not in card and "root_sublattice" not in card
    assert card["morphisms"] == []
    for slug in ("otilde-t-co", "otilde-plus-t-co"):
        group = ArithmeticGroup.model_validate(frontmatter.load(str(ROOT / "arithmetic-groups" / f"{slug}.md")).metadata)
        assert group.lattice == "6JRR"
        assert group.ambient_lie_group == "o-2-9"
        assert group.data.index_in_orthogonal_group is None
        assert group.data.generator_morphisms is None
        assert group.data.reference is None
    assert ArithmeticGroup.model_validate(frontmatter.load(str(ROOT / "arithmetic-groups" / "otilde-plus-t-co.md")).metadata).parent_group == "otilde-t-co"


def test_complete_intersection_configuration_has_the_stated_dimension() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["slug"] = "quartic-k3"
    source.metadata["name"] = "Smooth quartic K3 surface"
    source.metadata["construction"] = {
        "kind": "calabi_yau_complete_intersection",
        "ambient_projective_dimensions": [3],
        "equation_multidegrees": [[4]],
    }
    adapter = TypeAdapter(GeometricObject)
    adapter.validate_python(source.metadata)
    source.metadata["construction"]["equation_multidegrees"] = [[3]]
    changed = adapter.validate_python(source.metadata)
    assert changed.construction is not None
    assert changed.construction.equation_multidegrees == [[3]]


def test_dual_lattice_data_lives_on_the_owning_lattice_card() -> None:
    a2 = frontmatter.load(str(ROOT / "lattices" / "0012.md")).metadata
    assert a2["dual_gram_tensor"] == [["2/3", "1/3"], ["1/3", "2/3"]]
    assert not (ROOT / "lattices" / "0017.md").exists()
    retired = yaml.safe_load((ROOT / "retired-tags.yaml").read_text())
    assert "dual is stored on lattice card 0012" in retired["0017"]


def _family(**overrides: object) -> dict[str, object]:
    """The split OG6 family with overrides applied."""
    record: dict[str, object] = {
        "slug": "og6-polarized-split",
        "name": "Polarized OG6 lattices, split case",
        "parameter": "d",
        "minimum": 1,
        "rank": 7,
        "signature": [2, 5],
        "gram_template": [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, -2, 0, 0],
            [0, 0, 0, 0, 0, -2, 0],
            [0, 0, 0, 0, 0, 0, "-2*d"],
        ],
    }
    record.update(overrides)
    return record


def test_the_shipped_lattice_families_validate() -> None:
    for slug in (
        "og6-polarized-split",
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
    ):
        document = frontmatter.load(str(ROOT / "lattice-families" / f"{slug}.md"))
        family = LatticeFamily.model_validate(document.metadata)
        assert (family.rank, tuple(family.signature)) == (7, (2, 5))


def test_a_lattice_family_rejects_a_malformed_template() -> None:
    base = _family()
    # Not square.
    with pytest.raises(ValidationError, match="rank rows"):
        LatticeFamily.model_validate(base | {"gram_template": base["gram_template"][:6]})
    # Not symmetric.
    rows = [list(row) for row in base["gram_template"]]
    rows[0][1] = 0
    with pytest.raises(ValidationError, match="symmetric"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # An unknown name.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "-2*e"
    with pytest.raises(ValidationError, match="nothing else"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # Not arithmetic.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "2**d"
    with pytest.raises(ValidationError, match="integer arithmetic"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # The parameter never occurs.
    plain = [[0 if value == "-2*d" else value for value in row] for row in base["gram_template"]]
    with pytest.raises(ValidationError, match="occurs in gram_template"):
        LatticeFamily.model_validate(base | {"gram_template": plain})
    # Mathematical claims are accepted by the schema and checked through the preamble in CI.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "0*d"
    LatticeFamily.model_validate(base | {"gram_template": rows})
    LatticeFamily.model_validate(base | {"signature": [3, 4]})
    # The parameter is not an identifier.
    with pytest.raises(ValidationError, match="identifier"):
        LatticeFamily.model_validate(base | {"parameter": "2d"})


def test_the_corpus_loads_lattice_families_and_checks_their_slugs(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / "lattices" / "0012.md").symlink_to(ROOT / "lattices" / "0012.md")
    (tmp_path / corpus.FAMILIES_FILE).symlink_to(ROOT / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).symlink_to(ROOT / corpus.RETIRED_FILE)
    families = tmp_path / "lattice-families"
    families.mkdir()
    for slug in (
        "og6-polarized-split",
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
    ):
        (families / f"{slug}.md").symlink_to(ROOT / "lattice-families" / f"{slug}.md")
    loaded = corpus.load(tmp_path)
    assert [entry.value.slug for entry in loaded.lattice_families] == [
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
        "og6-polarized-split",
    ]
    assert [problem for problem in checks.report(tmp_path) if "lattice-families" in problem] == []


@pytest.mark.parametrize("literal", ["True", "False", "1.5", "'2'", "None"])
def test_family_expression_parser_refuses_noninteger_literals(literal: str) -> None:
    with pytest.raises(ValidationError, match="integer arithmetic"):
        LatticeFamily.model_validate(_family(rank=1, signature=[1, 0], gram_template=[[f"d + {literal}"]]))


def test_family_expression_parser_accepts_integer_literals() -> None:
    family = LatticeFamily.model_validate(_family(rank=1, signature=[1, 0], gram_template=[["d + 2"]]))
    assert family.gram_template == (("d + 2",),)
