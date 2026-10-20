# lattice-database — a catalogue of lattices, one Markdown record per lattice, and the site built from it.
#
# Each recipe runs one lattice database workflow.

ai_review_ci_schema_version := "1"
ai_review_ci_profile := "sage"
ai_review_ci_ref := "main"
ai_review_ci_release_channel := "main"
ai_review_ci_workflow_template_version := "1"
ai_review_ci_local_delegation := "global-justfile"
ai_review_ci_default_branch := "main"
# The cards are formatted nightly by .github/workflows/format.yml, not by the commit gate.
ai_review_ci_format_scheduled_dirs := "lattices"

# List available recipes
default:
    @just --list

# Run lattice-database workflows in the repository's Sage Python with both source
# trees visible.  The preamble is the normal mathematical computation boundary.
[private]
_latticedb *ARGS:
    PYTHONPATH="$HOME/research/src:src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m latticedb {{ARGS}}

# Author a lattice card from its Gram tensor: `just new --gram '[[2,1],[1,2]]' --name A2 --latex A_2`
new *ARGS:
    just _latticedb new {{ARGS}}

# Author a morphism on source card S: `just morphism 0016 0016 --name exchange --matrix '[[0,1],[1,0]]'`
morphism SOURCE TARGET *ARGS:
    just _latticedb morphism {{SOURCE}} {{TARGET}} {{ARGS}}

# Convert stored source rows into permanent lattice cards
seed *ARGS:
    just _latticedb seed {{ARGS}}

# Seed the regular and spinor regular ternary forms, their values certified by citation
regular-ternaries *ARGS:
    just _latticedb regular-ternaries {{ARGS}}

# Compute and store derived fields on existing cards
enrich *ARGS:
    just _latticedb enrich {{ARGS}}

# CI certification: compute uncertified values, replace disagreements, and write certificate hashes
certify *ARGS:
    just _latticedb certify {{ARGS}}

# Report stored-card inconsistencies, delegating mathematical checks to the preamble
verify:
    just _latticedb verify

# Format the cards with the commit gate's Markdown formatter; run nightly by format.yml
format-cards:
    git ls-files -z lattices | xargs -0 uvx --from 'git+https://github.com/dzackgarza/flowmark.git' flowmark --inplace --nobackup --semantic --no-respect-gitignore

# Build the site into _site/
build:
    just _latticedb build

# Build the site and serve it at http://lattice-database.localhost/
deploy:
    just _latticedb deploy

# Print the tag for the next new record
tag:
    just _latticedb next-tag

# Focused local model/schema gate. The preamble may be imported; lattice-db owns
# database mechanics, not a preamble-free shadow mathematics layer.
test:
    PYTHONPATH="$HOME/research/src:src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_model.py -q

# CI-only constructor/serialization/publication integration. Mathematical correctness lives in preamble tests.
test-validation:
    PYTHONPATH="$HOME/research/src:src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_catalogue_schemas.py tests/test_corpus.py tests/test_genus.py tests/test_geometric.py tests/test_hashimoto.py tests/test_records.py tests/validation

# Exercise archived-source importers and source-to-card collation; provenance only, not mathematical validation
test-source-intake:
    PYTHONPATH="$HOME/research/src:src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_bulk_sources.py tests/source_intake

# List the tags that share a Gram tensor
duplicates:
    just _latticedb duplicates

# Merge each card into the earliest card that states its Gram tensor, retiring its tag
deduplicate:
    just _latticedb deduplicate

test-commit: tensor-boundary
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

# Keep local pushes bounded: shared commit checks and the small schema specimen.
# The shared Sage push gate discovers the full corpus suite, so it belongs in CI.
test-push: test-commit test

# Run the complete shared gate, including every source and corpus test, in CI.
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

# Detect coordinate conventions written in the database source (research
# CONTRIBUTING.md, OWN-24): coordinate operations belong to research's
# preamble/tensors/. The scan is necessary but not sufficient: semantic
# ownership needs review.
tensor-boundary:
    #!/usr/bin/env bash
    set -uo pipefail
    files=$(git ls-files 'src/*.py') || exit 1
    total=0
    for pattern in '$X.transpose()' '$X.T' '$X.matrix_action_right($$$A)' '$X.matrix_action_left($$$A)' '$X.einsum($$$A)' 'einsum($$$A)' '$X.matmul($$$A)' 'matmul($$$A)' '$X.dot($$$A)' '$X @ $Y'; do
        matches=$(ast-grep run --lang python --pattern "$pattern" --json $files)
        status=$?
        # ast-grep returns 1 for a valid query with zero matches.
        if [ "$status" -gt 1 ]; then
            echo "tensor-boundary scanner failed (status $status) for $pattern" >&2
            exit "$status"
        fi
        if ! findings=$(printf '%s\n' "$matches" | python3 -c '
    import json, sys
    for hit in json.load(sys.stdin):
        print("{}:{}: {}".format(hit["file"], hit["range"]["start"]["line"] + 1, hit["lines"].strip()))
    '); then
            echo "tensor-boundary could not read the matches for $pattern" >&2
            exit 1
        fi
        n=$(printf '%s\n' "$findings" | grep -c . || true)
        total=$((total + n))
        printf '%4d  %s\n' "$n" "$pattern"
        if [ "$n" -gt 0 ]; then
            printf '%s\n' "$findings" | head -40
        fi
    done
    if [ "$total" -gt 0 ]; then
        echo "$total suspected coordinate operations in src/: state the owned pullback, contraction, composition, inverse or application in research's preamble instead."
        exit 1
    fi
    echo "No prohibited syntax detected; categorical ownership still requires source review."

# Run the scheduled whole-tree audit (semgrep and debt scans) through the central implementation.
ambient:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . ambient
