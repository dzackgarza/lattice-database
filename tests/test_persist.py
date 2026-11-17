"""Shards push their progress to main while certification keeps writing their worktrees."""

import os
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

from latticedb import failures

REPOSITORY = Path(__file__).resolve().parent.parent


def failure_attempt(reason: str) -> dict:
    """A complete `failures.Attempt`, as the ledger's own model requires."""
    return {
        "hash": "h",
        "gram_tensor": [[2]],
        "reason": reason,
        "stderr": "",
        "seconds": 0.0,
        "recorded_at": datetime(2026, 11, 7, tzinfo=UTC),
        "run_url": None,
        "database_revision": None,
        "research_revision": None,
    }
PERSIST = REPOSITORY / ".github" / "scripts" / "persist.sh"


def git(root: Path, *arguments: str) -> str:
    return subprocess.run(["git", "-C", str(root), *arguments], check=True, capture_output=True, text=True).stdout


def shard(origin: Path, path: Path) -> Path:
    git(path.parent, "clone", "-q", str(origin), path.name)
    git(path, "config", "user.name", "test")
    git(path, "config", "user.email", "test@example.invalid")
    git(path, "config", "merge.keyed-map.driver", f"{sys.executable} -m latticedb merge-keyed-map %O %A %B")
    # `.gitattributes` names both drivers: `certificates/` and the ledgers merge key by key, and a card
    # merges key by key too, so the fields run and the searches run keep each other's values (#21).
    git(path, "config", "merge.card-map.driver", f"{sys.executable} -m latticedb.card_merge %O %A %B")
    return path


def run_persist(root: Path, label: str) -> subprocess.CompletedProcess:
    environment = {**os.environ, "GITHUB_WORKSPACE": str(root), "GITHUB_RUN_ID": "1", "GITHUB_RUN_ATTEMPT": "1", "PYTHONPATH": str(REPOSITORY / "src")}
    return subprocess.run(["bash", str(PERSIST), label], cwd=root, env=environment, capture_output=True, text=True)


def persist(root: Path, label: str) -> None:
    finished = run_persist(root, label)
    assert finished.returncode == 0, finished.stdout + finished.stderr


def log(root: Path, entries: dict[str, int]) -> None:
    (root / "exceeded.yaml").write_text(yaml.safe_dump({name: {"hash": "h", "seconds": seconds} for name, seconds in entries.items()}))


def repository(tmp_path: Path) -> tuple[Path, Path, Path]:
    """A `main` whose two cards are underived, its bare origin, and two shards cloned from it."""
    seed = tmp_path / "seed"
    (seed / "lattices").mkdir(parents=True)
    (seed / "certificates").mkdir()
    (seed / "certificates" / "00.yaml").write_text("{}\n")
    (seed / ".gitattributes").write_text((REPOSITORY / ".gitattributes").read_text())
    for tag in ("0001", "0002"):
        (seed / "lattices" / f"{tag}.md").write_text(f"{tag} underived\n")
    log(seed, {})
    (seed / "failures").mkdir()
    (seed / "failures" / "00.yaml").write_text("{}\n")
    git(tmp_path, "init", "-q", "-b", "main", "seed")
    git(seed, "-c", "user.name=test", "-c", "user.email=test@example.invalid", "commit", "-q", "--allow-empty", "-m", "base")
    git(seed, "add", ".")
    git(seed, "-c", "user.name=test", "-c", "user.email=test@example.invalid", "commit", "-q", "-m", "cards")
    origin = tmp_path / "origin.git"
    git(tmp_path, "clone", "-q", "--bare", str(seed), str(origin))
    return origin, shard(origin, tmp_path / "first"), shard(origin, tmp_path / "second")


def test_shards_push_progress_repeatedly_without_touching_their_worktrees(tmp_path: Path) -> None:
    origin, first, second = repository(tmp_path)

    (first / "lattices" / "0001.md").write_text("0001 derived\n")
    log(first, {"0001 genus": 30})
    (first / "failures").mkdir(exist_ok=True)
    (first / "failures" / f"{failures.group('0001 integral.genus_symbol')}.yaml").write_text(
        yaml.safe_dump({"0001 integral.genus_symbol": {"disposition": "open", "attempts": [failure_attempt("memory exhausted")]}})
    )
    persist(first, "0/2")
    (second / "lattices" / "0002.md").write_text("0002 derived\n")
    log(second, {"0002 genus": 60})
    (second / "failures").mkdir(exist_ok=True)
    (second / "failures" / f"{failures.group('0002 integral.genus_symbol')}.yaml").write_text(
        yaml.safe_dump({"0002 integral.genus_symbol": {"disposition": "open", "attempts": [failure_attempt("exit status 1")]}})
    )
    # The second tick lands on the first tick's push, and the third on the second's.
    persist(second, "1/2")
    # The first shard keeps computing; its next push carries only what changed since.
    (first / "lattices" / "0001.md").write_text("0001 derived and certified\n")
    log(first, {})
    persist(first, "0/2")

    # Every tick is a fast-forward of the main it found, never a commit rebased onto a base that
    # moved and never a merge: one parent per commit, the base's first (#47).
    commits = git(origin, "rev-list", "--parents", "main").splitlines()
    assert len(commits) == 5, "the seed's two commits and one commit per tick"
    assert all(len(line.split()) == 2 for line in commits[:-1]), "no tick merges, and none rewrites history"

    main = tmp_path / "main"
    git(tmp_path, "clone", "-q", str(origin), "main")
    assert (main / "lattices" / "0001.md").read_text() == "0001 derived and certified\n"
    assert (main / "lattices" / "0002.md").read_text() == "0002 derived\n"
    assert yaml.safe_load((main / "exceeded.yaml").read_text()) == {"0002 genus": {"hash": "h", "seconds": 60}}
    assert set(failures.load(main)) == {"0001 integral.genus_symbol", "0002 integral.genus_symbol"}
    # Certification's worktree and index stay as it left them.
    # A snapshot pushed by `persist` is integrated in git without altering this source worktree, so
    # the merged ledger is no longer an outstanding local change. Only the computation completed after
    # the last snapshot remains uncommitted in it.
    assert git(first, "status", "--porcelain", "--untracked-files=no").split() == [
        "M",
        "lattices/0001.md",
    ], "exactly the new not-yet-pushed computation differs in the worktree"


def test_a_tick_keeps_its_progress_where_main_retired_a_path(tmp_path: Path) -> None:
    """A path main deleted mid-run is named and left out; it does not hold the tick's other values."""
    origin, first, second = repository(tmp_path)
    ledger = failures.group("0001 integral.genus_symbol")
    (first / "lattices" / "0001.md").write_text("0001 derived\n")
    log(first, {"0001 genus": 30})
    (first / "failures").mkdir(exist_ok=True)
    (first / "failures" / f"{ledger}.yaml").write_text(
        yaml.safe_dump({"0001 integral.genus_symbol": {"disposition": "open", "attempts": [failure_attempt("memory exhausted")]}})
    )
    persist(first, "0/2")

    # `main` retires the ledger shard while the run that wrote it keeps going.
    maintainer = tmp_path / "maintainer"
    git(tmp_path, "clone", "-q", str(origin), "maintainer")
    git(maintainer, "config", "user.name", "test")
    git(maintainer, "config", "user.email", "test@example.invalid")
    git(maintainer, "rm", "-q", f"failures/{ledger}.yaml")
    git(maintainer, "commit", "-q", "-m", "retire the ledger shard")
    git(maintainer, "push", "-q", "origin", "HEAD:main")

    # The shard completes its card and retries the computation whose ledger shard main retired.
    (first / "lattices" / "0001.md").write_text("0001 derived and certified\n")
    (first / "failures" / f"{ledger}.yaml").write_text(
        yaml.safe_dump(
            {"0001 integral.genus_symbol": {"disposition": "open", "attempts": [failure_attempt("memory exhausted"), failure_attempt("exit status 1")]}}
        )
    )
    finished = run_persist(first, "0/2")
    assert finished.returncode == 0, finished.stdout + finished.stderr
    assert f"main no longer tracks failures/{ledger}.yaml" in finished.stderr

    main = tmp_path / "main"
    git(tmp_path, "clone", "-q", str(origin), "main")
    assert (main / "lattices" / "0001.md").read_text() == "0001 derived and certified\n", "the tick's own values land"
    assert not (main / "failures" / f"{ledger}.yaml").exists(), "the retired path stays retired"


def test_a_path_that_cannot_be_merged_is_this_shards_failure(tmp_path: Path) -> None:
    """A merge the drivers cannot do is named as this shard's, and nothing is rewritten by it."""
    origin, first, second = repository(tmp_path)
    (first / "lattices" / "0001.md").write_text("0001 derived\n")
    log(first, {"0001 genus": 30})
    persist(first, "0/2")
    (second / "lattices" / "0002.md").write_text("0002 derived\n")
    log(second, {"0002 genus": 60})
    persist(second, "1/2")
    pushed = git(origin, "rev-parse", "main").strip()

    # A driver that cannot merge this shard's `exceeded.yaml` with the one main now holds.
    git(first, "config", "merge.keyed-map.driver", "false")
    log(first, {"0001 genus": 45})
    finished = run_persist(first, "0/2")
    assert finished.returncode != 0, "the persister does not call a lost push a success"
    assert "::error::shard 0/2" in finished.stderr and "exceeded.yaml" in finished.stderr, finished.stderr
    assert git(origin, "rev-parse", "main").strip() == pushed, "main is untouched by the attempt"
    assert yaml.safe_load((first / "exceeded.yaml").read_text()) == {"0001 genus": {"hash": "h", "seconds": 45}}
    assert git(first, "diff", "--cached", "--name-only").split() == [], "the shard's own index is not staged"

    # The same tick on the next attempt, with a driver that can merge, lands.
    git(first, "config", "merge.keyed-map.driver", f"{sys.executable} -m latticedb merge-keyed-map %O %A %B")
    persist(first, "0/2")
    main = tmp_path / "main"
    git(tmp_path, "clone", "-q", str(origin), "main")
    assert yaml.safe_load((main / "exceeded.yaml").read_text()) == {
        "0001 genus": {"hash": "h", "seconds": 45},
        "0002 genus": {"hash": "h", "seconds": 60},
    }


def test_a_tick_does_not_carry_a_card_its_run_never_wrote(tmp_path: Path) -> None:
    """A shard's worktree lags main; a card another shard certified must not go back with its tick."""
    origin, first, second = repository(tmp_path)
    (first / "lattices" / "0001.md").write_text("0001 derived\n")
    persist(first, "0/2")
    (second / "lattices" / "0002.md").write_text("0002 derived\n")
    persist(second, "1/2")
    # The first shard ticks again, and again: its worktree still holds 0002 as it checked it out.
    (first / "lattices" / "0001.md").write_text("0001 derived and certified\n")
    persist(first, "0/2")
    (second / "lattices" / "0002.md").write_text("0002 derived and certified\n")
    persist(second, "1/2")
    (first / "lattices" / "0001.md").write_text("0001 derived, certified and indexed\n")
    persist(first, "0/2")

    main = tmp_path / "main"
    git(tmp_path, "clone", "-q", str(origin), "main")
    assert (main / "lattices" / "0001.md").read_text() == "0001 derived, certified and indexed\n"
    assert (main / "lattices" / "0002.md").read_text() == "0002 derived and certified\n", "the other shard's card is not reverted"


def test_the_yaml_merge_driver_runs_without_the_sage_stack(tmp_path: Path) -> None:
    """Git runs a merge driver as its own process, with no Sage session behind it (#47)."""
    base, ours, theirs = (tmp_path / name for name in ("base.yaml", "ours.yaml", "theirs.yaml"))
    base.write_text("{}\n")
    ours.write_text("0001 genus: 30\n")
    theirs.write_text("0002 genus: 60\n")
    finished = subprocess.run(
        [sys.executable, "-m", "latticedb", "merge-keyed-map", str(base), str(ours), str(theirs)],
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(REPOSITORY / "src")},
    )
    assert finished.returncode == 0, finished.stderr
    assert yaml.safe_load(ours.read_text()) == {"0001 genus": 30, "0002 genus": 60}
    imported = subprocess.run(
        [sys.executable, "-c", "import sys, latticedb.__main__; print('latticedb.cli' in sys.modules)"],
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(REPOSITORY / "src")},
    )
    assert imported.stdout.strip() == "False", "the driver names are dispatched before the command line imports the corpus"
