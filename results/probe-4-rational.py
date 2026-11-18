"""#4 probe: the two element classes `_rational` takes, on the smallest inputs that reach it."""
from fractions import Fraction

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

from latticedb import sage_genus

# I_3 = <1,1,1>: the card 0022 of the regression test, rank 3.
lattice = Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
genus = lattice.genus()

print("--- local_density(2, m): a localization element")
for m in (1, 2, 4):
    value = genus.local_density(2, m)
    print(f"m={m} type={type(value).__module__}.{type(value).__name__} str={str(value)!r} "
          f"num={value.numerator()!r} den={value.denominator()!r} rational={sage_genus._rational(value)!r}")
    try:
        Fraction(str(value))
        print("   Fraction(str(value)) ACCEPTED (the old parser would survive this value)")
    except ValueError as error:
        print(f"   Fraction(str(value)) -> ValueError: {error}")

print("--- theta_series coefficients: an owned ring element")
series = genus.theta_series(precision=4)
for exponent in range(4):
    value = series[exponent]
    print(f"q^{exponent} type={type(value).__module__}.{type(value).__name__} str={str(value)!r} "
          f"rational={sage_genus._rational(value)!r}")
print("_coefficients ->", sage_genus._coefficients(series, 3))

print("--- the real _local_densities path")
print(sage_genus._local_densities(lattice, 4))
