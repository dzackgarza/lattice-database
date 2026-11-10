#!/usr/bin/env bash
# What persist.sh's integration does to one card, before the card has a merge driver.
#
# Two runs hold different fields of one card. Each rewrites the card from its own checkout and pushes
# its snapshot by cherry-picking it onto main. This does exactly that in a scratch repository that
# declares the repository's own `.gitattributes`, and reports which citations the push drops.
set -euo pipefail

repository="$(cd "$(dirname "$0")/.." && pwd)"
scratch="$(mktemp -d)"
trap 'rm -rf "$scratch"' EXIT

cat >"$scratch/card.py" <<'PY'
"""Write the card one run holds: `python card.py <fields|searches> <base|extra>`."""
import sys, yaml

fields = ["derive", "integral.genus_symbol", "integral.genus_class_count"]
searches = ["hyperbolic.reflective", "root_span.norms", "root_span.roots"]
which, extra = sys.argv[1], sys.argv[2] == "extra"
citations = {field: "1" for field in fields}
if which == "searches":
    citations |= {field: "2" for field in searches}
if extra:
    citations["integral.local_densities"] = "3"
metadata = {
    "tag": "0268",
    "name": "<-1>^2 + <3>",
    "latex": "L",
    "aliases": [],
    "certifications": citations,
    "rank": 3,
    "gram_tensor": [[-1, 0, 0], [0, -1, 0], [0, 0, 3]],
    "integral": {"genus_symbol": "I_{1,2}", **({"local_densities": []} if extra else {})},
    "families": [], "related": [], "references": [],
}
print("---\n" + yaml.dump(metadata, sort_keys=False) + "---\n")
PY

cat >"$scratch/citations.py" <<'PY'
"""Report the citation keys of a card, one per line."""
import sys, yaml

metadata = yaml.safe_load(open(sys.argv[1]).read().split("---")[1])
print("\n".join(sorted(metadata.get("certifications") or {})))
PY

cd "$scratch"
cp "$repository/.gitattributes" .
mkdir lattices
git init -q -b main
git config user.name evidence
git config user.email evidence@example.invalid
python3 card.py fields base >lattices/0268.md
git add .
git commit -q -m "the card both runs read"

# The searches run certifies the three semi-decision fields and pushes them.
git checkout -q -b searches
python3 card.py searches base >lattices/0268.md
git commit -q -am searches

# The fields run, from the card as it was before that push, certifies a field of its own.
git checkout -q main
git checkout -q -b fields
python3 card.py fields extra >lattices/0268.md
git commit -q -am fields

git checkout -q searches
python3 citations.py lattices/0268.md | sort >before
echo "citations on main after the searches run's push ($(wc -l <before)):"
sed 's/^/  /' before

echo
echo "1. persist.sh's cherry-pick, without -X:"
if git cherry-pick fields >/dev/null 2>&1; then
  echo "   merged, citations: $(python3 citations.py lattices/0268.md | wc -l)"
else
  echo "   conflict: the card is not mergeable, so the shard's values never land (persist.sh aborts)"
  git cherry-pick --abort
fi

echo
echo "2. persist.sh's cherry-pick as shipped, with -X theirs:"
git cherry-pick -X theirs fields >/dev/null
python3 citations.py lattices/0268.md | sort >after
echo "   citations after the push: $(wc -l <after)"
echo "   dropped by a push that reported success:"
comm -23 before after | sed 's/^/     -/'
