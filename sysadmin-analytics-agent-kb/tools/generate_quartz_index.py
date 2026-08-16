#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
FRONTMATTER_FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$")
REFERENCE_RE = re.compile(r"(?:\.\./)+references/([^)#\s]+\.md)")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = FRONTMATTER_FIELD_RE.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data


def plain_text(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_~]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def first_section_paragraph(
    text: str,
    headings: tuple[str, ...] = ("Mission", "Purpose"),
) -> str:
    lines = text.splitlines()
    wanted = {f"## {heading}".lower() for heading in headings}
    start = None

    for index, line in enumerate(lines):
        if line.strip().lower() in wanted:
            start = index + 1
            break

    if start is None:
        return ""

    paragraph: list[str] = []
    started = False
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("#"):
            break
        if not stripped:
            if started:
                break
            continue
        started = True
        paragraph.append(stripped)

    return plain_text(" ".join(paragraph))


def count_markdown_files(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    return sum(1 for path in directory.rglob("*.md") if path.is_file())


def referenced_docs(domain: Path) -> set[str]:
    references: set[str] = set()
    for path in domain.rglob("*.md"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        references.update(REFERENCE_RE.findall(text))
    return references


def discover_domains(kb: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in kb.iterdir()
            if path.is_dir() and (path / "agent.md").is_file()
        ),
        key=lambda path: path.name,
    )


def count_label(count: int, singular: str, plural: str | None = None) -> str:
    label = singular if count == 1 else (plural or f"{singular}s")
    return f"{count} {label}"


def render_domain_card(domain: Path) -> tuple[str, dict[str, int], set[str]]:
    agent_text = (domain / "agent.md").read_text(encoding="utf-8")
    heading_match = HEADING_RE.search(agent_text)
    title = heading_match.group(1).strip() if heading_match else domain.name
    title = re.sub(r"^Agent:\s*", "", title, flags=re.IGNORECASE)
    summary = first_section_paragraph(agent_text) or (
        "Agent domain and operational knowledge package."
    )
    frontmatter = parse_frontmatter(agent_text)
    status = frontmatter.get("status", "unspecified")
    references = referenced_docs(domain)
    stats = {
        "skills": count_markdown_files(domain / "skills"),
        "workflows": count_markdown_files(domain / "workflows"),
        "rules": count_markdown_files(domain / "rules"),
        "references": len(references),
    }

    labels = {
        "skills": count_label(stats["skills"], "skill"),
        "workflows": count_label(stats["workflows"], "workflow"),
        "rules": count_label(stats["rules"], "rule"),
        "references": count_label(stats["references"], "reference"),
    }
    stat_html = "".join(
        f'<span class="domain-card__stat">{html.escape(label)}</span>'
        for label in labels.values()
    )
    slug = html.escape(domain.name, quote=True)
    card = (
        f'<a class="domain-card" href="./{slug}/agent" '
        f'aria-label="{html.escape(title, quote=True)}">'
        '<div class="domain-card__topline">'
        f'<span class="domain-card__slug">{slug}</span>'
        f'<span class="domain-card__status">{html.escape(status)}</span>'
        "</div>"
        f"<h2>{html.escape(title)}</h2>"
        f"<p>{html.escape(summary)}</p>"
        f'<div class="domain-card__stats">{stat_html}</div>'
        "</a>"
    )
    return card, stats, references


def render_index(kb: Path) -> tuple[str, list[str]]:
    domains = discover_domains(kb)
    if not domains:
        raise SystemExit("No publishable domains found (expected */agent.md)")

    cards: list[str] = []
    total_skills = 0
    total_workflows = 0
    total_rules = 0
    all_references: set[str] = set()

    for domain in domains:
        card, stats, references = render_domain_card(domain)
        cards.append(card)
        total_skills += stats["skills"]
        total_workflows += stats["workflows"]
        total_rules += stats["rules"]
        all_references.update(references)

    summary = " · ".join(
        [
            count_label(len(domains), "domain"),
            count_label(total_skills, "skill"),
            count_label(total_workflows, "workflow"),
            count_label(total_rules, "rule"),
            count_label(len(all_references), "linked reference"),
        ]
    )

    body = "\n".join(
        [
            "---",
            "title: Agent KB",
            "artifact_type: index",
            "status: foundation",
            "domain: shared",
            "---",
            "",
            "# Agent KB",
            "",
            "Curated source-of-truth references and agent harnesses.",
            "",
            f'<div class="domain-summary">{html.escape(summary)}</div>',
            "",
            '<div class="domain-grid">',
            *cards,
            "</div>",
            "",
            "## Knowledge base",
            "",
            "- [References](references/README.md)",
            "- [Global Rules](shared/rules/global-rules.md)",
            "- [Roadmap](roadmap.md)",
            "",
            "## Graph artifacts",
            "",
            "- [Link Graph JSON](generated/link-graph.json)",
            "- [Link Graph DOT](generated/link-graph.dot)",
            "",
        ]
    )
    return body, [domain.name for domain in domains]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate the Quartz Agent KB landing page."
    )
    parser.add_argument("--kb", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()

    body, domains = render_index(args.kb.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body, encoding="utf-8")
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text("\n".join(domains) + "\n", encoding="utf-8")
    print(
        f"Generated Quartz index for {len(domains)} domain(s): {', '.join(domains)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
