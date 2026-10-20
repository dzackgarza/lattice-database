"""Build the static site from the corpus.

The site has one page for each lattice (`tag/<TAG>.html`), whose tables and
sections come from the record and whose prose comes from the Markdown body;
a database page that filters and sorts `lattices.json`, the union of all
records; an index of tags; one page for each collection in `pages/`; one page for each
part of the theory in `theory/`, which the other pages link to; and a
reference page for the fields, generated from the schema.
"""

import json
import re
import shutil
import subprocess
from collections.abc import Iterator
from dataclasses import dataclass
from html.parser import HTMLParser
from importlib.resources import files
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import frontmatter
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape
from markdown_it import MarkdownIt
from markupsafe import Markup, escape
from pydantic import BaseModel, Field

from latticedb.catalogues import ArithmeticGroup, LieGroup
from latticedb.collection_query import Cell as Cell
from latticedb.collection_query import Collection as Collection
from latticedb.collection_query import Row as Row
from latticedb.collection_query import matches_collection
from latticedb.corpus import Entry, load, read_card
from latticedb.geometric import HermitianSymmetricSpace, ProjectiveComplexVariety, RiemannianSymmetricSpace
from latticedb.model import (
    DefiniteData,
    FormData,
    HyperbolicData,
    IndefiniteData,
    IntegralData,
    Lattice,
    Morphism,
    PrimitiveOrbitSeries,
    Record,
    Reference,
    Related,
    RootSpan,
    RootSystemComponent,
)
from latticedb.site_formatting import (
    ORBIT_GROUP_KEYS as ORBIT_GROUP_KEYS,
)
from latticedb.site_formatting import (
    block_tex as block_tex,
)
from latticedb.site_formatting import (
    cardinality_tex as cardinality_tex,
)
from latticedb.site_formatting import (
    combination_tex as combination_tex,
)
from latticedb.site_formatting import (
    cone_zeta_tex as cone_zeta_tex,
)
from latticedb.site_formatting import (
    genus_tex as genus_tex,
)
from latticedb.site_formatting import (
    group_tex as group_tex,
)
from latticedb.site_formatting import (
    group_text as group_text,
)
from latticedb.site_formatting import (
    matrix_tex as matrix_tex,
)
from latticedb.site_formatting import (
    matrix_text as matrix_text,
)
from latticedb.site_formatting import (
    nonzero_zeta_tex as nonzero_zeta_tex,
)
from latticedb.site_formatting import (
    orbit_group_tex as orbit_group_tex,
)
from latticedb.site_formatting import (
    orbit_series_tex as orbit_series_tex,
)
from latticedb.site_formatting import (
    rational_tex as rational_tex,
)
from latticedb.site_formatting import (
    root_span_tex as root_span_tex,
)
from latticedb.site_formatting import (
    root_span_text as root_span_text,
)
from latticedb.site_formatting import (
    root_system_tex as root_system_tex,
)
from latticedb.site_formatting import (
    set_tex as set_tex,
)
from latticedb.site_formatting import (
    span_summands as span_summands,
)
from latticedb.site_formatting import (
    subgroup_tex as subgroup_tex,
)
from latticedb.site_formatting import (
    summand_images as summand_images,
)
from latticedb.site_formatting import (
    summand_name as summand_name,
)
from latticedb.site_formatting import (
    theta_tex as theta_tex,
)

DEFINITENESS_LABEL = {
    "positive_definite": "positive definite",
    "negative_definite": "negative definite",
    "indefinite": "indefinite",
    "positive_semidefinite": "positive semidefinite",
    "negative_semidefinite": "negative semidefinite",
    "zero": "zero",
}
PANES = {
    "rank": "rank",
    "definiteness": "definiteness",
    "property": "properties",
    "family": "families",
}
"""Query parameter of the database page -> the row key whose filter pane it selects."""


class Article(Record):
    """A page of `theory/`: the one place where the site explains a part of the theory, which the other pages link to."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(description="One sentence that says what the page explains. Dollar signs mark TeX.")
    order: int = Field(description="Position of the page in the list of theory pages.")


@dataclass(frozen=True)
class ArticlePage:
    slug: str
    article: Article
    prose: str


@dataclass(frozen=True)
class CollectionPage:
    slug: str
    collection: Collection
    prose: str
    members: tuple[Entry, ...]


def inline_markup(text: str) -> Markup:
    """HTML for one line of copy, in which backticks mark code and dollar signs mark TeX."""
    code = re.sub(r"`([^`]+)`", r"<code>\1</code>", str(escape(text)))
    return Markup(re.sub(r"\$([^$]+)\$", r"\\(\1\\)", code))


PROPERTY_MEANINGS = {
    "integral": ("lattices", "integral", "$L$ is integral."),
    "not integral": ("lattices", "integral", "$L$ is not integral."),
    "even": ("lattices", "integral", "$L$ is integral and even."),
    "odd": ("lattices", "integral", "$L$ is integral and odd."),
    "unimodular": ("discriminant-forms", "unimodular", "$L$ is unimodular."),
    "p-elementary": (
        "discriminant-forms",
        "two-elementary",
        "$A_L \\cong (\\mathbb{Z}/p)^a$ for a prime $p$ and $a \\geq 1$; the label states the prime, as in `2-elementary`.",
    ),
    "root lattice": ("roots", "roots", "$L = \\mathbb{Z}\\Phi(L)$."),
    "not a root lattice": ("roots", "roots", "$L \\neq \\mathbb{Z}\\Phi(L)$."),
    "degenerate": ("lattices", "degenerate", "$L$ is degenerate."),
    "hyperbolic": ("indefinite-lattices", "hyperbolic", "$L$ is hyperbolic."),
    "isotropic": (
        "indefinite-lattices",
        "isotropic",
        "$L$ is indefinite and isotropic.",
    ),
    "anisotropic": (
        "indefinite-lattices",
        "isotropic",
        "$L$ is indefinite and not isotropic.",
    ),
    "reflective": ("indefinite-lattices", "reflective", "$L$ is reflective."),
    "not reflective": (
        "indefinite-lattices",
        "reflective",
        "$L$ is hyperbolic and not reflective.",
    ),
}
"""Property label of the database -> (theory page, anchor of the definition, the condition). `p-elementary` stands for the labels that state a prime."""


def properties(lattice: Lattice) -> list[str]:
    """Property labels explicitly supported by stored card fields."""
    found = []
    if lattice.form is not None and lattice.form.integer_valued is False:
        found.append("not integral")
    if lattice.integral is not None:
        found.extend(f"{prime}-elementary" for prime in lattice.integral.elementary_primes or ())
        found.extend(["integral", lattice.integral.parity])
    if lattice.root_sublattice is not None and lattice.root_sublattice.norms is not None:
        found.append("root lattice")
    if lattice.hyperbolic is not None:
        found.append("hyperbolic")
    if lattice.indefinite is not None and lattice.indefinite.isotropic is not None:
        found.append("isotropic" if lattice.indefinite.isotropic else "anisotropic")
    if lattice.hyperbolic is not None and lattice.hyperbolic.reflective is not None:
        found.append("reflective" if lattice.hyperbolic.reflective else "not reflective")
    return found


def root_span_name(lattice: Lattice, lattices: dict[str, Lattice]) -> tuple[str, str] | None:
    """A lattice isometric to $\\mathbb{Z}\\Phi(L)$, as text and as TeX; `None` when the record does not state one.

    Definite lattice: the orthogonal sum of the root lattices of the components
    of `definite.roots`. Other lattice: the orthogonal sum of the records of
    `root_span.summands`, `0` when the lattice has no roots, and `L` when the
    rows of `root_span.roots` generate `L`.
    """
    if lattice.definite is not None and lattice.definite.roots is not None:
        return root_span_text(lattice.definite.roots), root_span_tex(lattice.definite.roots)
    span = lattice.root_span
    if span is None:
        return None
    if span.summands is not None:
        names = [summand_name(lattices[summand.tag], summand.scale) for summand in span.summands]
        return " + ".join(text for text, _ in names), " \\oplus ".join(tex for _, tex in names)
    if not span.roots:
        return "0", "0"
    return None


def row(lattice: Lattice, lattices: dict[str, Lattice]) -> Row:
    """The row of a lattice in `lattices.json`. `lattices` maps each tag of the corpus to its lattice."""
    integral, definite = lattice.integral, lattice.definite
    group = integral.discriminant_group if integral else None
    order = definite.automorphism_group_order if definite else None
    phi = tuple(component.type for component in definite.roots) if definite and definite.roots is not None else None
    span_name = root_span_name(lattice, lattices)
    return {
        "tag": lattice.tag,
        "url": f"tag/{lattice.tag}.html",
        "name": lattice.name,
        "latex": lattice.latex,
        "aliases": list(lattice.aliases),
        "rank": lattice.rank,
        "n_plus": lattice.signature[0] if lattice.signature else None,
        "n_minus": lattice.signature[1] if lattice.signature else None,
        "signature": f"({lattice.signature[0]}, {lattice.signature[1]})" if lattice.signature else None,
        "determinant": str(lattice.determinant) if lattice.determinant is not None else None,
        "determinant_value": float(lattice.determinant) if lattice.determinant is not None else None,
        "definiteness": DEFINITENESS_LABEL[lattice.definiteness] if lattice.definiteness else None,
        "properties": properties(lattice),
        "discriminant_group": group_text(group) if group is not None else None,
        "discriminant_group_tex": group_tex(group) if group is not None else None,
        "genus_symbol": integral.genus_symbol if integral else None,
        "genus_class_count": integral.genus_class_count if integral else None,
        "hyperbolic_index": integral.hyperbolic_index if integral else None,
        "overlattice_count": integral.overlattice_count if integral else None,
        "delta": integral.delta if integral else None,
        "minimum": str(definite.minimum) if definite and definite.minimum is not None else None,
        "minimum_value": float(definite.minimum) if definite and definite.minimum is not None else None,
        "kissing_number": definite.kissing_number if definite else None,
        "automorphism_group_order": str(order) if order is not None else None,
        "automorphism_group_order_value": float(order) if order is not None else None,
        "root_system": " ".join(definite.root_system) if definite and definite.root_system is not None else None,
        "root_system_tex": root_system_tex(definite.root_system) if definite and definite.root_system else None,
        "phi_type": " ".join(phi) if phi is not None else None,
        "phi_type_tex": (root_system_tex(phi) or "\\varnothing") if phi is not None else None,
        "root_span": span_name[0] if span_name else None,
        "root_span_tex": span_name[1] if span_name else None,
        "families": list(lattice.families),
    }


def collections(directory: Path, entries: tuple[Entry, ...]) -> tuple[CollectionPage, ...]:
    lattices = {entry.lattice.tag: entry.lattice for entry in entries}
    rows = {tag: row(lattice, lattices) for tag, lattice in lattices.items()}
    keys = set(next(iter(rows.values())))
    pages = []
    for path in sorted(directory.glob("*.md")):
        document = read_card(path)
        collection = Collection.model_validate(document.metadata)
        assert set(collection.where) <= keys, f"{path}: unknown row keys {sorted(set(collection.where) - keys)}"
        members = tuple(entry for entry in entries if matches_collection(rows[entry.lattice.tag], collection))
        assert members, f"{path}: no lattice satisfies the conditions"
        pages.append(CollectionPage(path.stem, collection, document.content, members))
    return tuple(pages)


def articles(directory: Path) -> tuple[ArticlePage, ...]:
    pages = []
    for path in directory.glob("*.md"):
        document = read_card(path)
        pages.append(ArticlePage(path.stem, Article.model_validate(document.metadata), document.content))
    orders = [page.article.order for page in pages]
    assert len(set(orders)) == len(orders), f"{directory}: two theory pages have one order"
    return tuple(sorted(pages, key=lambda page: page.article.order))


class _Anchors(HTMLParser):
    """The internal links (`href` and `src` without a scheme) and the element ids of one HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            match name, value:
                case "id", str():
                    self.ids.add(value)
                case "href" | "src", str() if not urlsplit(value).scheme:
                    self.links.append(value)


def broken_links(target: Path) -> list[str]:
    """Each internal link of the site under `target` whose file, or whose anchor in that file, does not exist."""
    pages = {}
    for path in target.rglob("*.html"):
        parser = _Anchors()
        parser.feed(path.read_text())
        pages[path.resolve()] = parser
    broken = []
    for path, parser in pages.items():
        for link in parser.links:
            parts = urlsplit(link)
            destination = (path.parent / parts.path).resolve() if parts.path else path
            if not destination.exists() or (parts.fragment and parts.fragment not in pages[destination].ids):
                broken.append(f"{path.relative_to(target.resolve())}: {link}")
    return broken


def database_query(collection: Collection) -> str | None:
    """The query string that selects the members of a collection on the database page, when its conditions are filter panes."""
    parameters = {}
    for parameter, key in PANES.items():
        match collection.where.get(key):
            case None:
                continue
            case list() as wanted:
                parameters[parameter] = ",".join(wanted)
            case value:
                parameters[parameter] = str(value)
    return urlencode(parameters) if len(parameters) == len(collection.where) else None


def markdown_to_html(texts: list[str], bibliography: Path | None = None) -> list[Markup]:
    """HTML for each Markdown text. TeX stays as `\\(...\\)` for MathJax."""
    local_markdown = MarkdownIt("commonmark")

    def convert(text: str) -> Markup:
        if bibliography is None and text.startswith(("Source entry `", "Catalogue of Lattices archive entry `")):
            return Markup(local_markdown.render(text))
        command = ["pandoc", "--from=markdown", "--to=html", "--mathjax"]
        if bibliography is not None:
            command += [
                "--citeproc",
                "--fail-if-warnings",
                f"--bibliography={bibliography}",
            ]
        done = subprocess.run(command, input=text, capture_output=True, text=True, check=True)
        return Markup(done.stdout)

    return [convert(text) for text in texts]


def fields() -> Iterator[tuple[str, str | None, type[BaseModel]]]:
    """The models of the schema: heading, block key, model."""
    yield "Every lattice", None, Lattice
    yield "Bilinear form", "form", FormData
    yield "Integral lattice", "integral", IntegralData
    yield (
        "Series of orbits of primitive vectors",
        "integral.primitive_orbits.<group>",
        PrimitiveOrbitSeries,
    )
    yield (
        "Series of orbits on the discriminant group",
        "integral.discriminant_orbits.<group>",
        PrimitiveOrbitSeries,
    )
    yield "Definite lattice", "definite", DefiniteData
    yield (
        "Component of the root system of a definite lattice",
        "definite.roots[]",
        RootSystemComponent,
    )
    yield "Indefinite lattice", "indefinite", IndefiniteData
    yield "Hyperbolic lattice", "hyperbolic", HyperbolicData
    yield "Roots of a lattice that is not definite", "root_span", RootSpan
    yield "Related lattice", "related[]", Related
    yield "Reference", "references[]", Reference
    yield "Morphism", "morphisms[]", Morphism
    yield "Lie group card", "lie-groups/<slug>.md", LieGroup
    yield "Arithmetic group card", "arithmetic-groups/<slug>.md", ArithmeticGroup


def orthogonal_groups(
    target: Path,
    environment: Environment,
    lattices: dict[str, Lattice],
    groups: dict[str, LieGroup],
    arithmetic_groups: dict[str, ArithmeticGroup],
) -> None:
    """Write the Lie-group index from explicit lattice -> arithmetic -> Lie-group links."""
    counts: dict[tuple[int, int], int] = {}
    for lattice in lattices.values():
        if lattice.orthogonal_group is None:
            continue
        arithmetic = arithmetic_groups.get(lattice.orthogonal_group)
        if arithmetic is None:
            continue
        ambient = groups.get(arithmetic.ambient_lie_group)
        if ambient is None or ambient.orthogonal_signature is None:
            continue
        key = (ambient.orthogonal_signature[0], ambient.orthogonal_signature[1])
        counts[key] = counts.get(key, 0) + 1
    orthogonal = {tuple(group.orthogonal_signature): group for group in groups.values() if group.orthogonal_signature is not None}
    limit = max((q for _, q in orthogonal), default=0)
    columns = list(range(limit + 1))
    rows = [
        (
            p,
            [(q, orthogonal.get((p, q)), counts.get((p, q), 0)) if q >= p else (q, None, None) for q in columns],
        )
        for p in columns
    ]
    rendered = environment.get_template("orthogonal-groups.html.j2").render(
        root="./",
        columns=columns,
        rows=rows,
        groups=tuple(sorted(groups.values(), key=lambda group: group.slug)),
    )
    (target / "orthogonal-groups.html").write_text(rendered)
    (target / "lie-groups.html").write_text(rendered)


def build(root: Path, target: Path) -> int:
    """Write the site for the corpus under `root` to `target`. Returns the number of lattices."""
    corpus = load(root)
    entries = corpus.entries
    pages = collections(root / "pages", entries)
    theory = articles(root / "theory")
    by_tag = {entry.lattice.tag: entry for entry in entries}
    lattices = {tag: entry.lattice for tag, entry in by_tag.items()}
    environment = Environment(
        loader=PackageLoader("latticedb"),
        autoescape=select_autoescape(["html", "j2"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["inline_markup"] = inline_markup
    environment.globals.update(
        rational_tex=rational_tex,
        group_tex=group_tex,
        genus_tex=genus_tex,
        orbit_group_tex=orbit_group_tex,
        subgroup_tex=subgroup_tex,
        cardinality_tex=cardinality_tex,
        orbit_series_tex=orbit_series_tex,
        cone_zeta_tex=cone_zeta_tex,
        nonzero_zeta_tex=nonzero_zeta_tex,
        theta_tex=theta_tex,
        root_system_tex=root_system_tex,
        set_tex=set_tex,
        combination_tex=combination_tex,
        block_tex=block_tex,
        properties=properties,
        definiteness_label=DEFINITENESS_LABEL,
        collections=pages,
        theory=theory,
        families=corpus.families,
        total=len(entries),
    )

    if target.exists():
        assert (target / "lattices.json").exists(), f"{target} exists and is not a site that this command built"
        shutil.rmtree(target)
    (target / "tag").mkdir(parents=True)
    (target / "collection").mkdir()
    (target / "theory").mkdir()
    (target / "lie-group").mkdir()
    (target / "arithmetic-group").mkdir()
    shutil.copytree(str(files("latticedb") / "assets"), target / "assets")

    ranks: list[int | None] = [*sorted({entry.lattice.rank for entry in entries if entry.lattice.rank is not None})]
    if any(entry.lattice.rank is None for entry in entries):
        ranks.append(None)
    by_rank = {rank: [entry for entry in entries if entry.lattice.rank == rank] for rank in ranks}
    geometric = corpus.geometric
    geometric_families = corpus.geometric_families
    graphs = corpus.graphs
    lie_groups = {entry.value.slug: entry.value for entry in corpus.lie_groups}
    arithmetic_groups = {entry.value.slug: entry.value for entry in corpus.arithmetic_groups}
    prose = markdown_to_html([entry.prose for entry in entries] + [page.prose for page in pages] + [page.prose for page in theory])
    lattice_page = environment.get_template("lattice.html.j2")
    incoming_by_tag: dict[str, list[tuple[Lattice, Morphism]]] = {}
    for source in lattices.values():
        for morphism in source.morphisms:
            incoming_by_tag.setdefault(morphism.target, []).append((source, morphism))
    for index, entry in enumerate(entries):
        lattice = entry.lattice
        components = json.dumps([[int(value) if value.denominator == 1 else str(value) for value in components_row] for components_row in lattice.gram_tensor or ()])
        (target / "tag" / f"{lattice.tag}.html").write_text(
            lattice_page.render(
                root="../",
                lattice=lattice,
                nullity=lattice.nullity,
                prose=prose[index],
                components_text=components.replace('"', ""),
                related=[(by_tag[related.tag].lattice, related.relation) for related in lattice.related],
                span_name=root_span_name(lattice, lattices),
                span_summands=span_summands(lattice, lattices),
                span_images=summand_images(lattice, lattices),
                lattices=lattices,
                incoming_morphisms=incoming_by_tag.get(lattice.tag, ()),
                outgoing_morphisms=[
                    (morphism, lattices[morphism.target], matrix_tex(morphism), matrix_text(morphism)) for morphism in lattice.morphisms if morphism.target in lattices
                ],
                geometric_objects=[
                    entry.geometric
                    for entry in geometric
                    if isinstance(entry.geometric, ProjectiveComplexVariety) and any(link.tag == lattice.tag for link in entry.geometric.cohomology_lattices)
                ],
                ambient_lie_group=(
                    lie_groups.get(arithmetic_groups[lattice.orthogonal_group].ambient_lie_group)
                    if lattice.orthogonal_group is not None and lattice.orthogonal_group in arithmetic_groups
                    else None
                ),
                orthogonal_group=(arithmetic_groups.get(lattice.orthogonal_group) if lattice.orthogonal_group is not None else None),
                arithmetic_groups=[arithmetic_groups[slug] for slug in lattice.arithmetic_groups if slug in arithmetic_groups],
                previous=entries[index - 1].lattice if index > 0 else None,
                following=entries[index + 1].lattice if index + 1 < len(entries) else None,
            )
        )
    collection_page = environment.get_template("collection.html.j2")
    for index, page in enumerate(pages):
        html = collection_page.render(
            root="../",
            page=page,
            prose=prose[len(entries) + index],
            query=database_query(page.collection),
        )
        (target / "collection" / f"{page.slug}.html").write_text(html)
    article_page = environment.get_template("article.html.j2")
    for index, article in enumerate(theory):
        html = article_page.render(
            root="../",
            page=article,
            prose=prose[len(entries) + len(pages) + index],
        )
        (target / "theory" / f"{article.slug}.html").write_text(html)
    (target / "theory.html").write_text(environment.get_template("theory.html.j2").render(root="./"))
    orthogonal_groups(target, environment, lattices, lie_groups, arithmetic_groups)
    lie_group_prose = markdown_to_html([entry.prose for entry in corpus.lie_groups])
    lie_group_page = environment.get_template("lie-group.html.j2")
    for lie_entry, rendered_prose in zip(corpus.lie_groups, lie_group_prose, strict=True):
        group = lie_entry.value
        member_lattices = [
            lattice
            for lattice in lattices.values()
            if lattice.orthogonal_group is not None
            and lattice.orthogonal_group in arithmetic_groups
            and arithmetic_groups[lattice.orthogonal_group].ambient_lie_group == group.slug
        ]
        (target / "lie-group" / f"{group.slug}.html").write_text(
            lie_group_page.render(
                root="../",
                group=group,
                prose=rendered_prose,
                lattices=member_lattices,
                lie_groups=lie_groups,
            )
        )
    arithmetic_prose = markdown_to_html([entry.prose for entry in corpus.arithmetic_groups])
    arithmetic_group_page = environment.get_template("arithmetic-group.html.j2")
    for arithmetic_entry, rendered_prose in zip(corpus.arithmetic_groups, arithmetic_prose, strict=True):
        arithmetic_group = arithmetic_entry.value
        (target / "arithmetic-group" / f"{arithmetic_group.slug}.html").write_text(
            arithmetic_group_page.render(
                root="../",
                group=arithmetic_group,
                prose=rendered_prose,
                lattice=lattices[arithmetic_group.lattice],
                ambient=lie_groups[arithmetic_group.ambient_lie_group],
                parent=arithmetic_groups.get(arithmetic_group.parent_group) if arithmetic_group.parent_group else None,
            )
        )
    (target / "arithmetic-groups.html").write_text(
        environment.get_template("arithmetic-groups.html.j2").render(
            root="./",
            groups=tuple(sorted(arithmetic_groups.values(), key=lambda group: group.slug)),
            by_slug=arithmetic_groups,
            lie_groups=lie_groups,
        )
    )
    (target / "hodge-diamonds.html").write_text(
        environment.get_template("hodge-diamonds.html.j2").render(
            root="./",
            has_k3=any(entry.geometric.slug == "k3-surface" for entry in geometric),
        )
    )
    (target / "geometric-objects").mkdir()
    bibliography = root / "geometric-bibliography.bib"
    geometric_prose = markdown_to_html([entry.prose for entry in geometric], bibliography)
    variety_page = environment.get_template("geometric-object.html.j2")
    space_page = environment.get_template("geometric-space.html.j2")
    for geometric_entry, rendered_prose in zip(geometric, geometric_prose, strict=True):
        record = geometric_entry.geometric
        if isinstance(record, ProjectiveComplexVariety):
            rows = [
                [
                    record.hodge_number(p, degree - p)
                    for p in range(
                        max(0, degree - record.dimension),
                        min(degree, record.dimension) + 1,
                    )
                ]
                for degree in range(2 * record.dimension + 1)
            ]
            html = variety_page.render(
                root="../",
                geometric=record,
                rows=rows,
                lattices=lattices,
                families={entry.family.slug: entry.family for entry in geometric_families},
                prose=rendered_prose,
            )
        else:
            html = space_page.render(root="../", geometric=record, prose=rendered_prose)
        (target / "geometric-objects" / f"{record.slug}.html").write_text(html)
    (target / "geometric-families").mkdir()
    family_prose = markdown_to_html([entry.prose for entry in geometric_families], bibliography)
    family_page = environment.get_template("geometric-family.html.j2")
    for family_entry, rendered_prose in zip(geometric_families, family_prose, strict=True):
        family = family_entry.family
        instances = [entry.geometric for entry in geometric if isinstance(entry.geometric, ProjectiveComplexVariety) and entry.geometric.family == family.slug]
        (target / "geometric-families" / f"{family.slug}.html").write_text(family_page.render(root="../", family=family, instances=instances, prose=rendered_prose))
    (target / "geometric-objects.html").write_text(
        environment.get_template("geometric-objects.html.j2").render(root="./", geometric=geometric, geometric_families=geometric_families)
    )
    (target / "graphs").mkdir()
    graph_prose = markdown_to_html([entry.prose for entry in graphs], bibliography)
    graph_page = environment.get_template("graph.html.j2")
    for graph_entry, rendered_prose in zip(graphs, graph_prose, strict=True):
        graph = graph_entry.graph
        objects = [
            entry.geometric
            for entry in geometric
            if isinstance(entry.geometric, (RiemannianSymmetricSpace, HermitianSymmetricSpace)) and graph.slug in entry.geometric.diagrams
        ]
        (target / "graphs" / f"{graph.slug}.html").write_text(graph_page.render(root="../", graph=graph, objects=objects, prose=rendered_prose))
    (target / "graphs.html").write_text(environment.get_template("graphs.html.j2").render(root="./", graphs=graphs))
    models = [(heading, key, model.__doc__, list(model.model_fields.items())) for heading, key, model in fields()]
    (target / "index.html").write_text(environment.get_template("index.html.j2").render(root="./", by_rank=by_rank))
    (target / "tags.html").write_text(environment.get_template("tags.html.j2").render(root="./", by_rank=by_rank))
    (target / "database.html").write_text(environment.get_template("database.html.j2").render(root="./"))
    family_counts = {family: sum(family in entry.lattice.families for entry in entries) for family in corpus.families}
    fields_page = environment.get_template("fields.html.j2")
    (target / "fields.html").write_text(
        fields_page.render(
            root="./",
            models=models,
            property_meanings=PROPERTY_MEANINGS,
            family_counts=family_counts,
        )
    )
    (target / "lattices.json").write_text(
        json.dumps(
            {"rows": [row(entry.lattice, lattices) for entry in entries]},
            separators=(",", ":"),
        )
    )
    broken = broken_links(target)
    assert not broken, "links to a missing page or anchor:\n" + "\n".join(broken)
    return len(entries)
