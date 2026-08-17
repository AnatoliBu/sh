#!/usr/bin/env python3
"""Единственный источник списка доменов Agent KB.

Домен — каталог KB с `agent.md`. Та же конвенция, по которой домены находит
`generate_quartz_index.py`; раньше валидаторы держали список руками, и новый домен молча
выпадал из проверок, пока кто-нибудь не заметит.
"""
from __future__ import annotations

from pathlib import Path

KB = Path(__file__).resolve().parents[1]

# каталоги вне доменного деления: общий слой правил и плоский каталог карточек
SHARED_ROOT = "shared"
REFERENCES_ROOT = "references"


def domain_roots(kb: Path | None = None) -> set[str]:
    """Имена доменных каталогов (тех, где есть `agent.md`)."""
    base = kb or KB
    return {p.name for p in base.iterdir() if p.is_dir() and (p / "agent.md").is_file()}


def agent_roots(kb: Path | None = None) -> set[str]:
    """Домены + `shared`: всё, где живут артефакты агентов."""
    return domain_roots(kb) | {SHARED_ROOT}


def strict_roots(kb: Path | None = None) -> set[str]:
    """То, что проверяется строго, включая плоский каталог карточек."""
    return agent_roots(kb) | {REFERENCES_ROOT}
