#!/usr/bin/env python3
"""Проверить пакеты в `plugins/` как устанавливаемые артефакты.

Исполняемая часть правила `shared/rules/skill-delivery.md`. Плагин уезжает на чужую машину
через marketplace, поэтому «у меня локально открывается» ничего не значит.

Проверяется:

- каждая относительная markdown-ссылка ведёт в существующий файл ВНУТРИ пакета;
- ссылка не выходит за корень пакета (`../../sysadmin-analytics-agent-kb/...` — мертва после
  установки) и не является абсолютным путём машины автора;
- у каждого скилла есть `SKILL.md` с frontmatter `name` + `description`;
- `name` во frontmatter равен имени каталога скилла;
- `description` триггерный: достаточно длинный и говорит, КОГДА брать скилл;
- `SKILL.md` не раздут: always-on-стоимость платится каждой сессией;
- в `.claude-plugin/` нет ничего кроме `plugin.json`, а компоненты лежат в корне пакета;
- пути в манифесте относительные, начинаются с `./` и не выходят из пакета;
- `plugin.json` парсится, `name` равен каталогу и kebab-case;
- `version` в манифесте по умолчанию отсутствует (иначе пакет запинен и обновления не
  доезжают — см. правило); если объявлена, то обязана быть semver;
- каждый каталог `plugins/<name>` объявлен в `marketplace.json` и наоборот;
- каждый домен KB представлен в `tools/plugin_packages.json` — домен без упаковки
  считается недоставленным.

Пороги можно ослабить флагами, но по умолчанию они те, что записаны в правиле.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / "sysadmin-analytics-agent-kb"
PLUGINS = ROOT / "plugins"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PACKAGES = KB / "tools" / "plugin_packages.json"

# домены, которые не пакуются: общий слой и каталоги не-доменов
NON_PACKAGED_DOMAINS = {"shared", "references", "research", "site", "tools", "ci-reports",
                        "notes", "generated", "public", "agents", "skills", "rules"}

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FM_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
WINDOWS_PATH_RE = re.compile(r"^[A-Za-z]:[\\/]")
# формулировки, по которым видно, что description объясняет момент активации
TRIGGER_HINTS = ("use when", "use this", "когда", "trigger", "используй", "бери")

COMPONENT_DIRS = ("skills", "agents", "commands", "hooks", "workflows", "output-styles",
                  "themes", "monitors", "bin", "scripts")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_links(plugin_dir: Path, errors: list[str]) -> None:
    for md in sorted(plugin_dir.rglob("*.md")):
        for raw in LINK_RE.findall(md.read_text(encoding="utf-8")):
            target = raw.split("#", 1)[0].split("?", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if WINDOWS_PATH_RE.match(target) or target.startswith("/"):
                errors.append(f"{rel(md)}: абсолютный путь в ссылке: {raw}")
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(plugin_dir.resolve())
            except ValueError:
                errors.append(f"{rel(md)}: ссылка за пределы пакета: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(md)}: битая ссылка: {raw}")


def check_skills(plugin_dir: Path, errors: list[str], max_lines: int, min_desc: int) -> None:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        found = next((p for p in (skill_dir / "SKILL.md", skill_dir / "skill.md") if p.exists()), None)
        if found is None:
            errors.append(f"{rel(skill_dir)}: нет SKILL.md")
            continue
        text = found.read_text(encoding="utf-8")
        m = FM_RE.match(text)
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

        desc = re.search(r"^description:\s*(.*?)(?=^\w+:|\Z)", fm, re.MULTILINE | re.DOTALL)
        if not desc:
            errors.append(f"{rel(found)}: нет description во frontmatter")
        else:
            body = " ".join(desc.group(1).split()).lstrip(">|").strip()
            if len(body) < min_desc:
                errors.append(
                    f"{rel(found)}: description {len(body)} симв. — короче {min_desc}; "
                    "скилл не активируется сам без перечисления задач и формулировок"
                )
            elif not any(h in body.lower() for h in TRIGGER_HINTS):
                errors.append(
                    f"{rel(found)}: description не говорит, КОГДА брать скилл "
                    f"(нет ни одного из: {', '.join(TRIGGER_HINTS)})"
                )

        lines = len(text.splitlines())
        if lines > max_lines:
            errors.append(
                f"{rel(found)}: {lines} строк > {max_lines} — always-on платится каждой "
                "сессией, длинное выносить в references/"
            )


def check_layout(plugin_dir: Path, name: str, errors: list[str]) -> None:
    manifest_dir = plugin_dir / ".claude-plugin"
    if manifest_dir.is_dir():
        extra = sorted(p.name for p in manifest_dir.iterdir() if p.name != "plugin.json")
        if extra:
            errors.append(
                f"plugins/{name}/.claude-plugin: лишнее ({', '.join(extra)}) — "
                "внутри только plugin.json, компоненты лежат в корне пакета"
            )
    for comp in COMPONENT_DIRS:
        if (manifest_dir / comp).exists():
            errors.append(f"plugins/{name}/.claude-plugin/{comp}: компонент должен быть в корне")


def check_manifest_paths(meta: dict, manifest: Path, errors: list[str]) -> None:
    path_fields = ("skills", "commands", "agents", "workflows", "hooks", "mcpServers",
                   "outputStyles", "lspServers")
    for field in path_fields:
        value = meta.get(field)
        if value is None:
            continue
        candidates = value if isinstance(value, list) else [value]
        for item in candidates:
            if not isinstance(item, str):
                continue
            if item == ".":
                continue
            if not item.startswith("./"):
                errors.append(f"{rel(manifest)}: {field}={item!r} должен начинаться с './'")
            if ".." in item:
                errors.append(f"{rel(manifest)}: {field}={item!r} выходит за пределы пакета")


def check_domains_are_packaged(errors: list[str]) -> None:
    if not PACKAGES.exists():
        errors.append("tools/plugin_packages.json отсутствует")
        return
    packaged = {
        spec.get("domain")
        for spec in json.loads(PACKAGES.read_text(encoding="utf-8")).values()
    }
    for path in sorted(p for p in KB.iterdir() if p.is_dir()):
        domain = path.name
        if domain in NON_PACKAGED_DOMAINS:
            continue
        if not (path / "agent.md").exists():
            continue  # не доменный пакет
        if domain not in packaged:
            errors.append(
                f"домен {domain} не объявлен в tools/plugin_packages.json — "
                "методология есть, доставки нет"
            )


def main() -> int:
    ap = argparse.ArgumentParser(description="Проверить пакеты plugins/ как устанавливаемые")
    ap.add_argument("--max-skill-lines", type=int, default=140,
                    help="лимит строк SKILL.md (always-on стоимость)")
    ap.add_argument("--min-description", type=int, default=180,
                    help="минимальная длина description во frontmatter скилла")
    args = ap.parse_args()

    errors: list[str] = []
    if not PLUGINS.is_dir():
        print("Plugin validation passed (нет каталога plugins/)")
        return 0

    declared: dict[str, str] = {}
    if MARKETPLACE.exists():
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        for key in ("name", "owner"):
            if key not in data:
                errors.append(f".claude-plugin/marketplace.json: нет обязательного поля {key}")
        for entry in data.get("plugins", []):
            if "name" not in entry or "source" not in entry:
                errors.append(f"marketplace.json: запись без name/source: {entry}")
                continue
            declared[entry["name"]] = entry.get("source", "")
            if "version" in entry:
                errors.append(
                    f"marketplace.json: {entry['name']}: version в записи каталога — "
                    "plugin.json побеждает молча, версию держать в одном месте"
                )
    else:
        errors.append(".claude-plugin/marketplace.json отсутствует")

    on_disk = sorted(p.name for p in PLUGINS.iterdir() if p.is_dir())
    for name in on_disk:
        plugin_dir = PLUGINS / name
        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        if not KEBAB_RE.match(name):
            errors.append(f"plugins/{name}: имя не kebab-case")
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
            if "version" in meta:
                version = str(meta["version"])
                if not SEMVER_RE.match(version):
                    errors.append(f"{rel(manifest)}: version={version!r} не semver")
                else:
                    errors.append(
                        f"{rel(manifest)}: version={version!r} пинит пакет — обновления "
                        "перестают доезжать без ручного бампа; по умолчанию версию "
                        "не объявляем (см. shared/rules/skill-delivery.md). Осознанное "
                        "исключение — снять эту проверку явно"
                    )
            check_manifest_paths(meta, manifest, errors)
        if name not in declared:
            errors.append(f"plugins/{name}: не объявлен в marketplace.json")
        check_layout(plugin_dir, name, errors)
        check_links(plugin_dir, errors)
        check_skills(plugin_dir, errors, args.max_skill_lines, args.min_description)

    for name, source in declared.items():
        if name not in on_disk:
            errors.append(f"marketplace.json: плагин {name} объявлен, но каталога нет")
        elif source and source not in (f"./plugins/{name}", f"plugins/{name}"):
            errors.append(f"marketplace.json: {name}: source={source!r} не указывает на каталог")

    check_domains_are_packaged(errors)

    if errors:
        print("Plugin validation failed:", file=sys.stderr)
        for e in errors:
            print("- " + e, file=sys.stderr)
        return 1
    print(f"Plugin validation passed ({len(on_disk)} package(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
