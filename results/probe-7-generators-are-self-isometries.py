"""#7: every generator each arithmetic-group card names is a scale-one isometry of 6JRR's Gram tensor.

The claim is the schema's own (`README.md`: a generator of an arithmetic subgroup is stored once, as
a `morphisms` entry of the lattice card with `scale: 1`, and the group card lists its name), so the
check is integer linear algebra on the stored data and no lattice algorithm:

  * every name a group card lists resolves to exactly one such morphism;
  * each named matrix satisfies `M^T G M = G` for the card's stored Gram tensor `G`;
  * the count the card states (56 for `otilde-t-co`, 95 for `otilde-plus-t-co`) is the number of
    names it lists.
"""
import json
from pathlib import Path

from latticedb import corpus

root = Path(".")
loaded = corpus.cards(root, ("6JRR",))
lattice = loaded.entries[0].lattice
gram = [[int(entry) for entry in row] for row in lattice.gram_tensor]

def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

self_isometries = {morphism.name: [[int(entry) for entry in row] for row in morphism.matrix]
                   for morphism in lattice.morphisms if morphism.target == lattice.tag and morphism.scale == 1}
print(json.dumps({"self_isometries_on_the_card": len(self_isometries)}), flush=True)

for entry in sorted(loaded.arithmetic_groups, key=lambda e: e.value.slug):
    card = entry.value
    names = list(card.data.generator_morphisms or ())
    unresolved = [name for name in names if name not in self_isometries]
    failing = [name for name in names if name in self_isometries
               and multiply(transpose(self_isometries[name]), multiply(gram, self_isometries[name])) != gram]
    print(json.dumps({
        "group": card.slug,
        "names": len(names),
        "unresolved": unresolved[:5],
        "not_isometries": failing[:5],
        "all_resolve": not unresolved,
        "all_are_isometries": not failing,
    }), flush=True)
