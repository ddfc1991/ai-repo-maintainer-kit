#!/usr/bin/env python3
from __future__ import annotations

import subprocess

CATEGORIES = {
    'Added': ('feat', 'add'),
    'Fixed': ('fix', 'bug'),
    'Changed': ('change', 'refactor', 'perf'),
    'Removed': ('remove', 'delete', 'drop'),
}

def sh(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()

def last_tag() -> str | None:
    try:
        return sh(['git', 'describe', '--tags', '--abbrev=0'])
    except subprocess.CalledProcessError:
        return None

def commits() -> list[str]:
    tag = last_tag()
    rev = f'{tag}..HEAD' if tag else 'HEAD'
    out = sh(['git', 'log', '--pretty=format:%s', rev])
    return [line for line in out.splitlines() if line]

def bucket(message: str) -> str:
    lower = message.lower()
    for category, keys in CATEGORIES.items():
        if any(k in lower for k in keys):
            return category
    return 'Changed'

def main() -> None:
    grouped = {name: [] for name in CATEGORIES}
    for msg in commits():
        grouped.setdefault(bucket(msg), []).append(msg)
    print('# Changelog Draft\n')
    for category, items in grouped.items():
        print(f'## {category}')
        if not items:
            print('- No notable changes')
        for item in items:
            print(f'- {item}')
        print()

if __name__ == '__main__':
    main()
