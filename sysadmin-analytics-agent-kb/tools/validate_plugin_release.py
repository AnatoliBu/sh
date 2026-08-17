#!/usr/bin/env python3
"""Проверить, что изменённый пакет доедет до установленных копий.

Клиент пропускает обновление, если разрешённая версия совпадает с установленной. Отсюда два
режима, и оба здесь проверяются:

- **без `version` в plugin.json** (режим по умолчанию для этого репозитория) — версией
  становится commit SHA, обновление доезжает само; проверять нечего;
- **с `version`** — пакет запинен, и содержательное изменение без бампа строки означает, что
  у всех, кто уже установил, останется старая копия. Это и есть ошибка релиза.

Сравнение делается с git-ревизией: `--base HEAD^` для пуша, `--base origin/main` для ветки.
Если ревизия недоступна (shallow-клон, первый коммит), проверка сообщает об этом и не падает:
гейт не должен врать про то, чего не смог посмотреть.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLUGINS = ROOT / "plugins"


def git(*args: str) -> tuple[int, str]:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return proc.returncode, proc.stdout.strip()


def manifest_version(rev: str, name: str) -> str | None:
    path = f"plugins/{name}/.claude-plugin/plugin.json"
    code, out = git("show", f"{rev}:{path}")
    if code != 0:
        return None
    try:
        return json.loads(out).get("version")
    except json.JSONDecodeError:
        return None


def current_version(name: str) -> str | None:
    path = PLUGINS / name / ".claude-plugin" / "plugin.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8")).get("version")


def main() -> int:
    ap = argparse.ArgumentParser(description="Гейт релиза пакетов plugins/")
    ap.add_argument("--base", default="HEAD^", help="git-ревизия для сравнения (по умолчанию HEAD^)")
    args = ap.parse_args()

    if not PLUGINS.is_dir():
        print("Release validation passed (нет каталога plugins/)")
        return 0

    code, _ = git("rev-parse", "--verify", args.base)
    if code != 0:
        print(f"Release validation skipped: ревизия {args.base} недоступна")
        return 0

    code, changed = git("diff", "--name-only", args.base, "HEAD", "--", "plugins")
    if code != 0:
        print(f"Release validation skipped: git diff недоступен ({changed})")
        return 0

    touched = {
        part.split("/")[1]
        for part in changed.splitlines()
        if part.startswith("plugins/") and len(part.split("/")) > 1
    }
    if not touched:
        print(f"Release validation passed (пакеты не менялись относительно {args.base})")
        return 0

    errors: list[str] = []
    pinned: list[str] = []
    for name in sorted(touched):
        now = current_version(name)
        if now is None:
            continue  # версия не объявлена -> версия = commit SHA, обновление доедет
        was = manifest_version(args.base, name)
        pinned.append(f"{name}={now}")
        if was is not None and was == now:
            errors.append(
                f"plugins/{name}: содержимое изменилось, а version осталась {now!r} — "
                "установленные копии обновление не получат; поднять версию или убрать поле"
            )

    if errors:
        print("Release validation failed:", file=sys.stderr)
        for e in errors:
            print("- " + e, file=sys.stderr)
        return 1
    detail = f", запинены: {', '.join(pinned)}" if pinned else ", версии не пинятся"
    print(f"Release validation passed (изменены: {', '.join(sorted(touched))}{detail})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
