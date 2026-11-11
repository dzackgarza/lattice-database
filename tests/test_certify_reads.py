"""A per-tag certification reads the cards that tag's computation needs, and no others (#30).

Reading the whole corpus to certify one card cost 7.3 GiB of cards and 1.8 GiB of certificates and was
killed on a 15 GiB runner before the first computation. These tests run the command's own load, with
`genus.certify` replaced by a recorder, so what is asserted is what the command reads.
"""

from pathlib import Path

import pytest

from latticedb import certificates, corpus, genus
from latticedb.cli import app

REPOSITORY = Path(__file__).resolve().parent.parent
CARDS = ("0012", "0016", "0026")


@pytest.fixture
def root(tmp_path: Path) -> Path:
    """A corpus of three cards, with the certificate groups they fall in."""
    (tmp_path / "lattices").mkdir()
    (tmp_path / "certificates").mkdir()
    (tmp_path / "lattices" / "_").mkdir(exist_ok=True)
    for tag in CARDS:
        (tmp_path / "lattices" / f"{tag}.md").write_text((REPOSITORY / "lattices" / f"{tag}.md").read_text())
    for group in {certificates.group(tag) for tag in CARDS}:
        source = REPOSITORY / "certificates" / f"{group}.yaml"
        (tmp_path / "certificates" / f"{group}.yaml").write_text(source.read_text() if source.exists() else "{}\n")
    (tmp_path / corpus.FAMILIES_FILE).write_text("{}\n")
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    (tmp_path / "exceeded.yaml").write_text("{}\n")
    return tmp_path


def certify_reads(tmp_path: Path, tags: tuple[str, ...], monkeypatch: pytest.MonkeyPatch) -> tuple[list[str], list[str]]:
    """Run `certify --tag …` with the queue replaced, and report what its load read."""
    seen: dict[str, list[str]] = {}
    reads: list[str] = []
    original = corpus.read_card

    def counted(path: Path):
        reads.append(path.stem)
        return original(path)

    def recorded(root_path: Path, loaded: corpus.Corpus, held: certificates.Certificates, *args, **kwargs) -> None:
        seen["cards"] = [entry.lattice.tag for entry in loaded.entries]
        seen["groups"] = sorted({certificates.group(name.split(" ", 1)[0]) for name in held})

    monkeypatch.setattr(corpus, "read_card", counted)
    monkeypatch.setattr(genus, "certify", recorded)
    arguments = ["certify", "--minutes", "1", "--root", str(tmp_path)]
    for tag in tags:
        arguments += ["--tag", tag]
    app(arguments, result_action="return_value")
    seen["read"] = sorted(set(reads))
    return seen["cards"], seen["groups"]


def test_a_tag_request_reads_only_that_tag_s_card(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The command that certifies one card reads one card."""
    cards, groups = certify_reads(root, ("0012",), monkeypatch)
    assert cards == ["0012"]
    assert groups == [certificates.group("0012")]


def test_a_two_tag_request_reads_the_two_cards(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cards, groups = certify_reads(root, ("0012", "0026"), monkeypatch)
    assert cards == ["0012", "0026"]
    assert groups == sorted({certificates.group("0012"), certificates.group("0026")})


def test_a_whole_corpus_request_still_reads_every_card(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Without `--tag` the run certifies the corpus, and reads it: the repair narrows nothing there."""
    cards, _ = certify_reads(root, (), monkeypatch)
    assert sorted(cards) == sorted(CARDS)
