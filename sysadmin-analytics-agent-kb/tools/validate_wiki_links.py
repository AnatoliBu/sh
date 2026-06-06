#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI_RE = re.compile(r'\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|[^\]]+)?\]\]')


def rel(path):
    return path.relative_to(ROOT).as_posix()


def main():
    errors = []
    for path in sorted(ROOT.rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        for raw_path, _anchor in WIKI_RE.findall(text):
            target = raw_path if raw_path.endswith('.md') else raw_path + '.md'
            dst = (path.parent / target).resolve()
            try:
                dst.relative_to(ROOT)
            except ValueError:
                errors.append(f'{rel(path)}: wiki link escapes repo root: {raw_path}')
                continue
            if not dst.exists():
                errors.append(f'{rel(path)}: broken wiki link: {raw_path}')
    if errors:
        print('Wiki link validation failed:', file=sys.stderr)
        for error in errors:
            print('- ' + error, file=sys.stderr)
        return 1
    print('Wiki link validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
