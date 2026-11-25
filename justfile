ai_review_ci_schema_version := "1"
ai_review_ci_profile := "sage"
ai_review_ci_ref := "main"
ai_review_ci_release_channel := "main"
ai_review_ci_workflow_template_version := "1"
ai_review_ci_local_delegation := "global-justfile"
ai_review_ci_default_branch := "main"
ai_review_ci_format_scheduled_dirs := "lattices"

[doc("List available recipes")]
default:
    @just --list

[doc("Run lattice-database workflows in the repository's Sage Python with both source trees visible.")]
[private]
[positional-arguments]
_latticedb *ARGS:
    PYTHONPATH="$HOME/research/src:src:/repos/sage-extensions/src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m latticedb "$@"

[doc("Author a lattice card from its Gram tensor: `just new --gram '[[2,1],[1,2]]' --name A2 --latex A_2`")]
new *ARGS:
    just _latticedb new {{ARGS}}

[doc("Author all canonical sums of known untwisted indecomposables up to rank 10 and form content 2")]
populate-standard-sums *ARGS:
    just _latticedb populate-standard-sums {{ARGS}}

[doc("Store a caller-chosen prefix of the preamble's unbounded construction enumeration")]
populate-construction-prefix *ARGS:
    just _latticedb populate-construction-prefix {{ARGS}}

[doc("Author tensor products of known specimens and their proper integral overlattices")]
populate-standard-products *ARGS:
    just _latticedb populate-standard-products {{ARGS}}

[doc("Author proper integral overlattices of selected existing lattice cards")]
populate-overlattices *ARGS:
    just _latticedb populate-overlattices {{ARGS}}

[doc("Author a morphism on source card S: `just morphism 0016 0016 --name exchange --matrix '[[0,1],[1,0]]'`")]
morphism SOURCE TARGET *ARGS:
    just _latticedb morphism {{SOURCE}} {{TARGET}} {{ARGS}}

[doc("Convert stored source rows into permanent lattice cards")]
seed *ARGS:
    just _latticedb seed {{ARGS}}

[doc("Seed the regular and spinor regular ternary forms, their values certified by citation")]
regular-ternaries *ARGS:
    just _latticedb regular-ternaries {{ARGS}}

[doc("Compute and store derived fields on existing cards")]
enrich *ARGS:
    just _latticedb enrich {{ARGS}}

[doc("CI certification: compute uncertified values, replace disagreements, and write certificate hashes")]
certify *ARGS:
    just _latticedb certify {{ARGS}}

[doc("Inspect recorded certification failures and their triage history")]
[positional-arguments]
certification-failures *ARGS:
    just _latticedb certification-failures "$@"

[doc("Release a failed computation: TAG block.field --note 'repair or investigation'")]
[positional-arguments]
retry-computation *ARGS:
    just _latticedb retry-computation "$@"

[doc("Report stored-card inconsistencies, delegating mathematical checks to the preamble")]
verify:
    just _latticedb verify

[doc("Format the cards with the commit gate's Markdown formatter; run nightly by format.yml")]
format-cards:
    git ls-files -z lattices | xargs -0 uvx --from 'git+https://github.com/dzackgarza/flowmark.git' flowmark --inplace --nobackup --semantic --no-respect-gitignore

[doc("Build the site into _site/")]
build:
    just _latticedb build

[doc("Build the site and serve it at http://lattice-database.localhost/")]
deploy:
    just _latticedb deploy

[doc("Print the tag for the next new record")]
tag:
    just _latticedb next-tag

[doc("Focused local model/schema gate.")]
test:
    PYTHONPATH="$HOME/research/src:src:/repos/sage-extensions/src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_model.py tests/test_card_merge.py -q

[doc("CI-only constructor/serialization/publication integration. Mathematical correctness lives in preamble tests.")]
test-validation:
    PYTHONPATH="$HOME/research/src:src:/repos/sage-extensions/src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_catalogue_schemas.py tests/test_corpus.py tests/test_genus.py tests/test_ge_generators.py tests/test_geometric.py tests/test_hashimoto.py tests/test_records.py tests/validation

[doc("Certification scheduling, failure triage and persistence on small specimens")]
[positional-arguments]
test-certification *ARGS:
    PYTHONPATH="$HOME/research/src:src:/repos/sage-extensions/src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_genus.py tests/test_failures.py tests/test_persist.py "$@"

[doc("Exercise archived-source importers and source-to-card collation; provenance only, not mathematical validation")]
test-source-intake:
    PYTHONPATH="$HOME/research/src:src:/repos/sage-extensions/src" "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest tests/test_bulk_sources.py tests/source_intake

[doc("List the tags that share a Gram tensor")]
duplicates:
    just _latticedb duplicates

[doc("Merge each card into the earliest card that states its Gram tensor, retiring its tag")]
deduplicate:
    just _latticedb deduplicate

[doc("MVP publication: inspect staged syntax only; model tests and architectural ownership rules run in CI, not at every commit.")]
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

[doc("Publishing work does not wait for the database's test suite.")]
test-push:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-push

[doc("Run the complete shared gate, including every source and corpus test, in CI.")]
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

[doc("Detect coordinate conventions written in the database source (research CONTRIBUTING.md, OWN-24): coordinate operations belong to research's preamble/tensors/.")]
tensor-boundary:
    #!/usr/bin/env bash
    set -uo pipefail
    files=$(git ls-files 'src/*.py') || exit 1
    total=0
    for pattern in '$X.transpose()' '$X.T' '$X.matrix_action_right($$$A)' '$X.matrix_action_left($$$A)' '$X.einsum($$$A)' 'einsum($$$A)' '$X.matmul($$$A)' 'matmul($$$A)' '$X.dot($$$A)' '$X @ $Y'; do
        matches=$(ast-grep run --lang python --pattern "$pattern" --json $files)
        status=$?
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

[doc("Run the scheduled whole-tree audit (semgrep and debt scans) through the central implementation.")]
ambient:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . ambient
