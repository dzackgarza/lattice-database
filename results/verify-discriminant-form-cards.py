"""Run the repository's verification over the cards #12 added discriminant forms to (#12).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-discriminant-form-cards.py [tag...]

`checks.report` is what `latticedb verify` reports: it recomputes each field's certificate over the
stored Gram tensor and the stored value and compares the result with the shard under `certificates/`.
A scratch corpus holding only these cards keeps the run to them, because a whole-corpus load holds
every card and has never finished in one process on this VM.

The default set is the four cards that now state `integral.discriminant_form`: 6JRX and 6JRY (Trivial
Z/2 and Z/4), 029J (Z/2)^10 and 6JRR (Z/2)^11.
"""
import shutil
import sys
import tempfile
from pathlib import Path

import frontmatter

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ("6JRX", "6JRY", "029J", "6JRR")


def main(tags: tuple[str, ...]) -> int:
    groups = sorted({certificates.group(tag) for tag in tags})
    with tempfile.TemporaryDirectory(dir=ROOT / ".scratch") as scratch:
        root = Path(scratch)
        (root / "lattices").mkdir()
        (root / "certificates").mkdir()
        shutil.copy(ROOT / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
        shutil.copy(ROOT / corpus.RETIRED_FILE, root / corpus.RETIRED_FILE)
        for group in groups:
            shutil.copy(ROOT / "certificates" / f"{group}.yaml", root / "certificates" / f"{group}.yaml")
        for tag in tags:
            shutil.copy(ROOT / "lattices" / f"{tag}.md", root / "lattices" / f"{tag}.md")
        # A card is only valid in a corpus that holds what it names, and the naming is transitive:
        # a morphism targets another card, an arithmetic-group card names its lattice and its parent.
        # The closure of those references is finite and small here (a few cards), so it is followed to
        # the end rather than guessed at.
        pending = list(tags)
        while pending:
            tag = pending.pop()
            path = root / "lattices" / f"{tag}.md"
            if not path.exists() or not (ROOT / "lattices" / f"{tag}.md").exists():
                continue
            metadata = frontmatter.load(str(path)).metadata
            named = [morphism.get("target") for morphism in (metadata.get("morphisms") or ()) if isinstance(morphism, dict)]
            named.extend(relation["tag"] if isinstance(relation, dict) else relation
                         for relation in (metadata.get("related") or ()))
            for collection in ("arithmetic-groups", "lie-groups"):
                source = ROOT / collection
                if not source.is_dir():
                    continue
                if not (root / collection).exists():
                    shutil.copytree(source, root / collection)
                for entry in (root / collection).glob("*.md"):
                    document = frontmatter.load(str(entry)).metadata
                    if document.get("lattice") == tag:
                        named.extend(parent for parent in (document.get("parent_group"),) if parent)
            # Every arithmetic-group card is present, so every lattice one of them names must be too.
            for entry in (root / "arithmetic-groups").glob("*.md") if (root / "arithmetic-groups").is_dir() else ():
                named.append(frontmatter.load(str(entry)).metadata.get("lattice"))
            for name in named:
                if name and not (root / "lattices" / f"{name}.md").exists() and (ROOT / "lattices" / f"{name}.md").exists():
                    shutil.copy(ROOT / "lattices" / f"{name}.md", root / "lattices" / f"{name}.md")
                    # A card's own certificate shard has to come with it, or every field of that card
                    # looks uncertified: `checks` compares the card's citation with the shard.
                    group_file = ROOT / "certificates" / f"{certificates.group(name)}.yaml"
                    if group_file.exists() and not (root / "certificates" / group_file.name).exists():
                        shutil.copy(group_file, root / "certificates" / group_file.name)
                    pending.append(name)
        problems = checks.report(root)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problems in the verification of {' '.join(tags)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:]) or DEFAULT))
