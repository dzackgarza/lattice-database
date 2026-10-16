"""Typed consumer boundaries accept real objects returned by the owned APIs."""

from fractions import Fraction

from dzack_research.preamble.categories.abstract_categories.mor_categories import CategoricalMor
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphismMethods
from dzack_research.preamble.rings import session_ring_objects

from latticedb import hoehn_mason, sage_genus


def test_source_intake_accepts_native_formed_modules_and_module_maps() -> None:
    formed = hoehn_mason._formed(((Fraction(2),),))
    underlying = formed.unformed_module()
    arrow = hoehn_mason._rows(underlying, ((1,),))
    assert isinstance(formed, FormModules.ParentMethods)
    assert isinstance(arrow, CategoricalMor.ElementMethods)
    assert isinstance(arrow, ModuleMorphismMethods)
    assert arrow.codomain() is underlying
    assert hoehn_mason._matrix(arrow) == ((1,),)
    assert sage_genus._matrix_rows(arrow) == [[1]]


def test_coordinate_embeddings_are_owned_category_methods() -> None:
    category = Lattices(session_ring_objects()["ZZ"])
    assert isinstance(category, Lattices.SubcategoryMethods)


def test_public_form_morphism_query_implements_its_declared_owner() -> None:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormedModuleMor

    formed = hoehn_mason._formed(((Fraction(2),),))
    query = FormModules(formed.base_ring()).Mor(formed, formed)
    assert isinstance(query, FormedModuleMor)
    lattice = Lattices(session_ring_objects()["ZZ"])([[2]])
    assert isinstance(FormModules(lattice.base_ring()).Mor(lattice, lattice), FormedModuleMor)
