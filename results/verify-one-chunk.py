"""Verify ONE chunk of the recovered cards, in this process, and record it against its exact inputs.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-one-chunk.py MANIFEST.json INDEX

Started by results/verify-current-chunks.py, which gives each chunk its own process. One chunk per
process is what bounds the memory: the preamble keeps every structure it builds for the life of the
process, so a process that verifies many chunks grows until it is killed, whatever the chunks are.

The record is bound to what was checked, so a later tree can never reuse it:

    tree          the commit and the sha256 of the uncommitted diff (so editing a card changes it)
    checker       sha256 of this file and of the orchestrator
    verifier      sha256 of `src/latticedb/checks/records.py`, whose `problems` makes the verdict
    cards         sha256 of every card file in the chunk
    certificates  sha256 of every certificate shard the chunk reads
    tags          the chunk's tag list

A chunk's result is reused only when every one of those is identical.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(tags: list[str]) -> dict:
    """Everything the verdict depends on, as hashes, so a record cannot outlive its inputs."""
    tree = __import__("subprocess").run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                                        capture_output=True, text=True, check=True).stdout.strip()
    dirty = __import__("subprocess").run(["git", "-C", str(ROOT), "diff", "HEAD"],
                                          capture_output=True, check=True).stdout
    groups = sorted({certificates.group(tag) for tag in tags})
    return {
        "tree": {"commit": tree, "diff": hashlib.sha256(dirty).hexdigest()},
        "checker": {
            "one_chunk": digest(Path(__file__)),
            "orchestrator": digest(ROOT / "results" / "verify-current-chunks.py"),
        },
        "verifier": digest(ROOT / "src" / "latticedb" / "checks" / "records.py"),
        "tags": tags,
        "cards": {tag: digest(ROOT / "lattices" / f"{tag}.md") for tag in tags},
        "certificates": {group: digest(ROOT / "certificates" / f"{group}.yaml") for group in groups},
    }


def verify(tags: list[str]) -> list[str]:
    groups = sorted({certificates.group(tag) for tag in tags})
    root = Path(tempfile.mkdtemp(dir=ROOT / ".scratch"))
    try:
        (root / "lattices").mkdir()
        (root / "certificates").mkdir()
        shutil.copy(ROOT / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
        shutil.copy(ROOT / corpus.RETIRED_FILE, root / corpus.RETIRED_FILE)
        for group in groups:
            shutil.copy(ROOT / "certificates" / f"{group}.yaml", root / "certificates" / f"{group}.yaml")
        for tag in tags:
            shutil.copy(ROOT / "lattices" / f"{tag}.md", root / "lattices" / f"{tag}.md")
        loaded = corpus.load(root)
        held = certificates.load(root)
        return checks.records.problems(loaded, held)
    finally:
        shutil.rmtree(root)


def main(manifest_path: str, index: int) -> int:
    manifest = json.loads(Path(manifest_path).read_text())
    chunk = manifest["chunks"][index]
    tags = chunk["tags"]
    now = binding(tags)
    if chunk["problems"] is not None and chunk["binding"] == now:
        # The record was made from exactly these inputs, so it is this tree's result, not another's.
        print(f"chunk {index + 1}/{len(manifest['chunks'])}: {len(tags)} cards, "
              f"{len(chunk['problems'])} problems (recorded for these inputs)", flush=True)
        return 1 if chunk["problems"] else 0
    problems = verify(tags)
    chunk["binding"] = now
    chunk["problems"] = [problem.replace(str(ROOT), "") for problem in problems]
    Path(manifest_path).write_text(json.dumps(manifest, indent=1, sort_keys=True))
    print(f"chunk {index + 1}/{len(manifest['chunks'])}: {len(tags)} cards, {len(problems)} problems", flush=True)
    for problem in chunk["problems"]:
        print("   ", problem, flush=True)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], int(sys.argv[2])))
