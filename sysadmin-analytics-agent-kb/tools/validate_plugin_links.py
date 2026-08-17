#!/usr/bin/env python3
"""Проверить пакеты в `plugins/` как устанавливаемые артефакты.

Плагин уезжает на чужую машину через marketplace, поэтому внутри него не должно быть
ссылок «в репозиторий»: там их некому резолвить. Проверяется:

- каждая относительная markdown-ссылка ведёт в существующий файл внутри плагина;
- ссылка не выходит за корень плагина (`../../sysadmin-analytics-agent-kb/...` — запрещено);
- у каждого скилла есть `SKILL.md` с frontmatter `name` + `description`;
- имя каталога скилла совпадает с `name` во frontmatter;
- каждый каталог `plugins/<name>` объявлен в `.claude-plugin/marketplace.json` и наоборот;
- `plugin.json` существует, парсится, его `name` равен имени каталога, а `version` — semver
  (иначе `claude plugin update`/`tag` не с чем работать; это же ловит `claude plugin
  validate`, но его в CI нет).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLUGINS = ROOT / "plugins"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FM_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_links(plugin_dir: Path, errors: list[str]) -> None:
    for md in sorted(plugin_dir.rglob("*.md")):
        for raw in LINK_RE.findall(md.read_text(encoding="utf-8")):
            target = raw.split("#", 1)[0].split("?", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(plugin_dir.resolve())
            except ValueError:
                errors.append(f"{rel(md)}: ссылка за пределы плагина: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(md)}: битая ссылка: {raw}")


def check_skills(plugin_dir: Path, errors: list[str]) -> None:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        candidates = [skill_dir / "SKILL.md", skill_dir / "skill.md"]
        found = next((p for p in candidates if p.exists()), None)
        if found is None:
            errors.append(f"{rel(skill_dir)}: нет SKILL.md")
            continue
        m = FM_RE.match(found.read_text(encoding="utf-8"))
        if not m:
            errors.append(f"{rel(found)}: нет frontmatter")
            continue
        fm = m.group(1)
        name = re.search(r"^name:\s*(\S+)\s*$", fm, re.MULTILINE)
        if not name:
            errors.append(f"{rel(found)}: нет name во frontmatter")
        elif name.group(1) != skill_dir.name:
            errors.append(
                f"{rel(found)}: name={name.group(1)} не совпадает с каталогом {skill_dir.name}"
            )
        if not re.search(r"^description:", fm, re.MULTILINE):
            errors.append(f"{rel(found)}: нет description во frontmatter")


def main() -> int:
    errors: list[str] = []
    if not PLUGINS.is_dir():
        print("Plugin validation passed (нет каталога plugins/)")
        return 0

    declared: dict[str, str] = {}
    if MARKETPLACE.exists():
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        for entry in data.get("plugins", []):
            declared[entry["name"]] = entry.get("source", "")
    else:
        errors.append(".claude-plugin/marketplace.json отсутствует")

    on_disk = sorted(p.name for p in PLUGINS.iterdir() if p.is_dir())
    for name in on_disk:
        plugin_dir = PLUGINS / name
        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            errors.append(f"plugins/{name}: нет .claude-plugin/plugin.json")
        else:
            try:
                meta = json.loads(manifest.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{rel(manifest)}: невалидный JSON ({exc})")
                meta = {}
            if meta.get("name") != name:
                errors.append(f"{rel(manifest)}: name={meta.get('name')!r} != каталог {name!r}")
            version = str(meta.get("version", ""))
            if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
                errors.append(
                    f"{rel(manifest)}: version={version or 'отсутствует'!r} не semver "
                    "(без версии не работают plugin update/tag)"
                )
        if name not in declared:
            errors.append(f"plugins/{name}: не объявлен в marketplace.json")
        check_links(plugin_dir, errors)
        check_skills(plugin_dir, errors)

    for name, source in declared.items():
        if name not in on_disk:
            errors.append(f"marketplace.json: плагин {name} объявлен, но каталога нет")
        elif source and source not in (f"./plugins/{name}", f"plugins/{name}"):
            errors.append(f"marketplace.json: {name}: source={source!r} не указывает на каталог")

    if errors:
        print("Plugin validation failed:", file=sys.stderr)
        for e in errors:
            print("- " + e, file=sys.stderr)
        return 1
    print(f"Plugin validation passed ({len(on_disk)} package(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
