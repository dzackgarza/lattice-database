"""Shards push their progress to main while certification keeps writing their worktrees."""

import os
import subprocess
import sys
from pathlib import Path

import yaml

REPOSITORY = Path(__file__).resolve().parent.parent
PERSIST = REPOSITORY / ".github" / "scripts" / "persist.sh"


def git(root: Path, *arguments: str) -> str:
    return subprocess.run(["git", "-C", str(root), *arguments], check=True, capture_output=True, text=True).stdout


def shard(origin: Path, path: Path) -> Path:
    git(path.parent, "clone", "-q", str(origin), path.name)
    git(path, "config", "user.name", "test")
    git(path, "config", "user.email", "test@example.invalid")
    git(path, "config", "merge.keyed-map.driver", f"{sys.executable} -m latticedb merge-keyed-map %O %A %B")
    return path


def persist(root: Path, label: str) -> None:
    environment = {**os.environ, "GITHUB_WORKSPACE": str(root), "GITHUB_RUN_ID": "1", "GITHUB_RUN_ATTEMPT": "1", "PYTHONPATH": str(REPOSITORY / "src")}
    finished = subprocess.run(["bash", str(PERSIST), label], cwd=root, env=environment, capture_output=True, text=True)
    assert finished.returncode == 0, finished.stdout + finished.stderr


def log(root: Path, entries: dict[str, int]) -> None:
    (root / "exceeded.yaml").write_text(yaml.safe_dump({name: {"hash": "h", "seconds": seconds} for name, seconds in entries.items()}))


def test_shards_push_progress_repeatedly_without_touching_their_worktrees(tmp_path: Path) -> None:
    seed = tmp_path / "seed"
    (seed / "lattices").mkdir(parents=True)
    (seed / "certificates").mkdir()
    (seed / "certificates" / "00.yaml").write_text("{}\n")
    (seed / ".gitattributes").write_text((REPOSITORY / ".gitattributes").read_text())
    for tag in ("0001", "0002"):
        (seed / "lattices" / f"{tag}.md").write_text(f"{tag} underived\n")
    log(seed, {})
    (seed / "failures.yaml").write_text("{}\n")
    git(tmp_path, "init", "-q", "-b", "main", "seed")
    git(seed, "-c", "user.name=test", "-c", "user.email=test@example.invalid", "commit", "-q", "--allow-empty", "-m", "base")
    git(seed, "add", ".")
    git(seed, "-c", "user.name=test", "-c", "user.email=test@example.invalid", "commit", "-q", "-m", "cards")
    origin = tmp_path / "origin.git"
    git(tmp_path, "clone", "-q", "--bare", str(seed), str(origin))
    first, second = shard(origin, tmp_path / "first"), shard(origin, tmp_path / "second")

    (first / "lattices" / "0001.md").write_text("0001 derived\n")
    log(first, {"0001 genus": 30})
    (first / "failures.yaml").write_text(yaml.safe_dump({"0001 integral.genus_symbol": {"disposition": "open", "attempts": [{"reason": "memory exhausted"}]}}))
    persist(first, "0/2")
    (second / "lattices" / "0002.md").write_text("0002 derived\n")
    log(second, {"0002 genus": 60})
    (second / "failures.yaml").write_text(yaml.safe_dump({"0002 integral.genus_symbol": {"disposition": "open", "attempts": [{"reason": "exit status 1"}]}}))
    persist(second, "1/2")
    # The first shard keeps computing; its next push carries only what changed since.
    (first / "lattices" / "0001.md").write_text("0001 derived and certified\n")
    log(first, {})
    persist(first, "0/2")

    main = tmp_path / "main"
    git(tmp_path, "clone", "-q", str(origin), "main")
    assert (main / "lattices" / "0001.md").read_text() == "0001 derived and certified\n"
    assert (main / "lattices" / "0002.md").read_text() == "0002 derived\n"
    assert yaml.safe_load((main / "exceeded.yaml").read_text()) == {"0002 genus": {"hash": "h", "seconds": 60}}
    assert set(yaml.safe_load((main / "failures.yaml").read_text())) == {"0001 integral.genus_symbol", "0002 integral.genus_symbol"}
    # Certification's worktree and index stay as it left them.
    assert git(first, "status", "--porcelain", "--untracked-files=no").split() == ["M", "failures.yaml", "M", "lattices/0001.md"]
