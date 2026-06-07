#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
SECTION_RE = re.compile(r'^## (Reference links|Authority references)\s*$', re.MULTILINE)
ROOTS = {'sysadmin', 'analytics', 'java-qa', 'shared'}
TYPES = {'agent', 'skill', 'rule', 'workflow', 'eval'}
SKIP = {'sysadmin/skills/incident-triage.md'}


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def fm(text: str) -> dict[str, str] | None:
    m = FM_RE.match(text)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def is_artifact(p: Path) -> bool:
    if p.suffix != '.md' or p.name in {'README.md', 'TEMPLATE.md'}:
        return False
    r = rel(p)
    if r in SKIP:
        return False
    parts = p.relative_to(ROOT).parts
    if not parts or parts[0] not in ROOTS:
        return False
    data = fm(p.read_text(encoding='utf-8'))
    return bool(data and data.get('artifact_type') in TYPES)


def is_flat_reference(src: Path, raw: str) -> bool:
    raw = raw.split('#', 1)[0].split('?', 1)[0]
    if not raw or raw.startswith('http') or raw.startswith('mailto:'):
        return False
    dst = (src.parent / raw).resolve()
    try:
        dst.relative_to(ROOT)
    except ValueError:
        return False
    return dst.parent == ROOT / 'references' and dst.suffix == '.md'


def main() -> int:
    errors = []
    for p in sorted(ROOT.rglob('*.md')):
        if not is_artifact(p):
            continue
        text = p.read_text(encoding='utf-8')
        links = LINK_RE.findall(text)
        r = rel(p)
        if not SECTION_RE.search(text):
            errors.append(f'{r}: missing reference section')
        if not any(is_flat_reference(p, link) for link in links):
            errors.append(f'{r}: missing flat references/*.md link')
        for link in links:
            if 'references/sysadmin/' in link or 'references/analytics/' in link:
                errors.append(f'{r}: old reference path: {link}')
    if errors:
        print('Agent artifact reference validation failed:', file=sys.stderr)
        for e in errors:
            print('- ' + e, file=sys.stderr)
        return 1
    print('Agent artifact reference validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
