"""Missing morphism metadata never supplies a scale to a computation."""

import pytest
from pydantic import ValidationError

from latticedb.model import Lattice, Morphism
from latticedb.records import morphism_problems


def test_an_unstated_morphism_scale_remains_unknown() -> None:
    morphism = Morphism.model_validate({"target": "0002", "name": "map", "matrix": [[1]]})
    assert morphism.scale is None
    assert "scale" not in morphism.model_dump(exclude_unset=True)


def test_verifying_a_morphism_requires_its_stated_scale() -> None:
    source = Lattice.model_validate({"tag": "0001", "name": "source", "latex": "S", "rank": 1, "gram_tensor": [[2]]})
    target = Lattice.model_validate({"tag": "0002", "name": "target", "latex": "T", "rank": 1, "gram_tensor": [[2]]})
    morphism = Morphism.model_validate({"target": "0002", "name": "map", "matrix": [[1]]})
    with pytest.raises(ValueError, match="morphism scale must be stated"):
        morphism_problems(morphism, source, target)


def test_explicit_morphism_scale_is_retained_and_zero_is_rejected() -> None:
    fields = {"target": "0002", "name": "map", "matrix": [[1]], "scale": 1}
    assert Morphism.model_validate(fields).scale == 1
    fields["scale"] = 0
    with pytest.raises(ValidationError):
        Morphism.model_validate(fields)


@pytest.mark.parametrize("scale", [None, 1])
def test_authoring_preserves_whether_scale_was_stated(tmp_path, scale: int | None) -> None:
    import frontmatter

    from latticedb.cli import morphism

    cards = tmp_path / "lattices"
    cards.mkdir()
    path = cards / "0001.md"
    path.write_text("---\ntag: '0001'\nname: source\n---\n")
    morphism("0001", "0002", name="map", matrix="[[1]]", scale=scale, root=tmp_path)
    stored = frontmatter.load(str(path))["morphisms"][0]
    if scale is None:
        assert "scale" not in stored
    else:
        assert stored["scale"] == scale


@pytest.mark.parametrize("scale", [None, 1])
def test_verification_index_requires_stated_scale(tmp_path, scale: int | None) -> None:
    from latticedb.corpus import Corpus, Entry, held

    fields = {"target": "0002", "name": "map", "matrix": [[1]]}
    if scale is not None:
        fields["scale"] = scale
    lattice = Lattice.model_validate({"tag": "0001", "name": "source", "latex": "S", "morphisms": [fields]})
    loaded = Corpus(
        entries=(Entry(lattice, "", tmp_path / "0001.md"),),
        families={},
        retired={},
        geometric=(),
        geometric_families=(),
        graphs=(),
        genera=(),
        polytopes=(),
        toric_varieties=(),
        geometric_maps=(),
        local_systems=(),
        operators=(),
        moduli_problems=(),
        lattice_families=(),
        lie_groups=(),
        arithmetic_groups=(),
    )
    if scale is None:
        with pytest.raises(ValueError, match="morphism scale must be stated"):
            held(loaded)
    else:
        assert held(loaded) == {("0001", "0002"): ((((1,),), 1),)}


def test_owned_group_generator_serialization_does_not_reuse_an_unknown_scale() -> None:
    from latticedb.genus import _generator_morphisms
    from latticedb.model import Yaml

    stored: list[dict[str, Yaml]] = [{"target": "0001", "name": "O(L) generator 1", "matrix": [[1]]}]
    names, written = _generator_morphisms("0001", stored, [[[1]]])
    assert "scale" not in written[0]
    assert names == ["O(L) generator 1 #2"]
    assert written[1] == {"target": "0001", "name": "O(L) generator 1 #2", "matrix": [[1]], "scale": 1}
