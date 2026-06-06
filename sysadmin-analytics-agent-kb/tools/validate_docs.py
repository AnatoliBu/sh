#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PREFIXES = (
    'agents/',
    'rules/',
    'skills/',
    'sysadmin/skills/',
    'analytics/skills/',
)
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$', re.MULTILINE)
LINE_RE = re.compile(r'^L(\d+)(?:-L(\d+))?$')
FENCE_RE = re.compile(r'```.*?```', re.DOTALL)


def rel(path):
    return path.relative_to(ROOT).as_posix()


def clean(text):
    return FENCE_RE.sub('', text)


def is_artifact(path):
    if path.name == 'TEMPLATE.md':
        return False
    return rel(path).startswith(ARTIFACT_PREFIXES)


def slug(text):
    text = text.replace('`', '').lower().strip()
    text = ''.join(ch for ch in text if ch.isalnum() or ch in ' -_')
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text


def anchors(text):
    result = set()
    counts = {}
    for match in HEADING_RE.finditer(text):
        base = slug(match.group(2))
        if not base:
            continue
        n = counts.get(base, 0)
        result.add(base if n == 0 else f'{base}-{n}')
        counts[base] = n + 1
    return result


def split_target(raw):
    raw = raw.strip().split('?', 1)[0]
    if '#' in raw:
        return raw.split('#', 1)
    return raw, None


def local_target(src, target_path):
    if target_path == '':
        return src
    return (src.parent / target_path).resolve()


def check_anchor(src, dst, fragment, raw, errors):
    text = dst.read_text(encoding='utf-8')
    m = LINE_RE.fullmatch(fragment)
    if m:
        line_count = len(text.splitlines())
        start = int(m.group(1))
        end = int(m.group(2) or start)
        if start < 1 or end < start or end > line_count:
            errors.append(f'{rel(src)}: {raw} points outside {rel(dst)} ({line_count} lines)')
        return
    if fragment not in anchors(text):
        errors.append(f'{rel(src)}: anchor {raw} not found in {rel(dst)}')


def check_links(path, text, errors):
    for raw in LINK_RE.findall(clean(text)):
        raw = raw.strip()
        if raw.startswith('http') or raw.startswith('mailto:'):
            if is_artifact(path):
                errors.append(f'{rel(path)}: direct external link in artifact; link to references instead')
            continue
        target_path, fragment = split_target(raw[1:] if raw.startswith('#') else raw)
        dst = local_target(path, target_path)
        try:
            dst.relative_to(ROOT)
        except ValueError:
            errors.append(f'{rel(path)}: link escapes repo root: {raw}')
            continue
        if not dst.exists():
            errors.append(f'{rel(path)}: broken local link: {raw}')
            continue
        if dst.is_dir():
            dst = dst / 'README.md'
            if not dst.exists():
                errors.append(f'{rel(path)}: directory link has no README.md: {raw}')
                continue
        if fragment and dst.suffix == '.md':
            check_anchor(path, dst, fragment, raw, errors)


def check_reference_requirement(path, text, errors):
    if not is_artifact(path):
        return
    for raw in LINK_RE.findall(clean(text)):
        target_path, _ = split_target(raw)
        if 'references/' not in target_path:
            continue
        dst = local_target(path, target_path)
        if dst.exists() and 'references' in dst.relative_to(ROOT).parts:
            return
    errors.append(f'{rel(path)}: missing local reference link under references/')


def main():
    errors = []
    for path in sorted(ROOT.rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        check_links(path, text, errors)
        check_reference_requirement(path, text, errors)
    if errors:
        print('Documentation validation failed:', file=sys.stderr)
        for error in errors:
            print('- ' + error, file=sys.stderr)
        return 1
    print('Documentation validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
