# #16: the orbit count is a `Cardinalities` element, serialized through the owner's own API

## The failure, on the owner's own object

`sage-extensions` main `5fc4e0119b`, in the image, for 026E's real card:

    >>> series = Lattices(ZZ)(record.gram_tensor).primitive_orbit_series()
    >>> series["O"]["constant"]
    1                                    class: sage_extensions.categories.sets.cardinals.Cardinalities.parent_class
    >>> json.dumps(series)
    TypeError: Object of type parent_class is not JSON serializable

reproduced by `tests/test_genus.py::test_the_owner_s_orbit_counts_are_cardinalities_that_json_refuses`,
which asks the owner for that series and asserts both the `TypeError` and `is_finite() is True` with
`finite_value() == 1`.

## The owning API

`sage_extensions/categories/sets/cardinals.py`:

    def is_finite(self) -> bool            # decides, on the element's own expression
    def finite_value(self) -> int          # "the ordinary nonnegative integer representing this finite cardinal"
    def is_countably_infinite(self) -> bool
    def is_uncountable(self) -> bool
    def __int__(self) -> int               # raises TypeError for an infinite cardinal

`_orbit_count` now writes what those say, and nothing else:

    if value is None or isinstance(value, int):  return value
    if not isinstance(value, Cardinal):          raise TypeError(...)
    if value.is_finite():                        return value.finite_value()
    if value.is_countably_infinite():            return "aleph0"
    raise ValueError(f"the owner states the count {value} is uncountable; a card states an exact count or aleph0")

`Cardinal` is the owner's own `Cardinalities().ObjectType`, imported from that module. No `int()`
cast, no `getattr` probe, no printed form, no null.

## Red before green

    db18c21a00  test: …           4 passed, 1 failed
                                   test_a_cardinality_beyond_aleph0_is_not_recorded_as_aleph0:
                                   the owner's `continuum` (is_finite False, is_countably_infinite
                                   False, is_uncountable True) was recorded as "aleph0" — a count the
                                   owner never stated.
    <this commit> fix: …          38 passed in 176.74s (tests/test_genus.py, in the image)

Two tests that had used stand-in classes (`Cardinality`, `Infinite`, `Owner`) now run on the owner's
own series for 026E, which is the object the adapter must serialize.

## The certificate and the card value

`latticedb certify --tag 026E --phase fields --shard 0/1 --workers 1` over a root holding 026E (the
full-corpus run of the same command was killed at 15 GiB of RAM before any computation, exit 137):

    026E {'primitive_orbits': {'O': {'constant': 1, 'z': [], 'w': []}, 'SO': …, 'SOtilde+': …}}

lattices/026E.md:

    certifications:
      integral.primitive_orbits: 71acd10a9086e12004375735a77f3c09cfa35d98687b9746995f994599b427c3
    integral:
      primitive_orbits:
        O: {constant: 1, z: [], w: []}      (and the other seven groups, each 1)

certificates/f1.yaml:

    026E integral.primitive_orbits:
      hash: 71acd10a9086e12004375735a77f3c09cfa35d98687b9746995f994599b427c3
      by: research preamble

`results/../.scratch/apply-16.py` moved that value and that entry from the certified one-card root into
this tree, asserting first that the real card recomputes the same hash. `checks.records.problems` then
reports **0 problems** on 026E, alongside the cards of #23 and #24.
