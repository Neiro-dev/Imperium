# Quickstart: checking the design archive

How to check `docs/design-archive/` against spec.md's success criteria. The checks need a clone of Imperium-old at the
pinned commit; `$OLD` is its path, and the commands run from this repository's root in Bash with Python 3.

```bash
git clone https://github.com/Neiro-dev/Imperium-old.git "$OLD"
git -C "$OLD" checkout b218bdcbaf5a9f6253d747399986bfd30cabc243
```

## 1. Every pointer resolves (SC-001)

Each `` `path` L<a>-<b> `` in the archive names a file at the pinned commit and lines inside it.

```bash
python -I - "$OLD" docs/design-archive/*.md <<'EOF'
import re, sys, pathlib
old, files = pathlib.Path(sys.argv[1]), sys.argv[2:]
bad = 0
for f in files:
    text = open(f, encoding='utf-8').read()
    # a pointer may wrap across a line break between its path and its lines
    for path, a, b in re.findall(r'`([^`\n]+?)`\s+L(\d+)(?:\s*-\s*L?(\d+))?', text):
        p = old / path
        last = int(b or a)
        if not p.is_file() or last > len(p.read_text(encoding='utf-8').split('\n')) or int(a) > last:
            print(f'{f}: {path} L{a}-{b or a}'); bad += 1
print('unresolved pointers:', bad)
EOF
```

Expected: `unresolved pointers: 0`.

## 2. Every file at the pinned commit is in the coverage record (SC-002)

```bash
git -C "$OLD" ls-tree -r --name-only -z HEAD > /tmp/all.txt
python -I - /tmp/all.txt docs/design-archive/coverage.md <<'EOF'
import re, sys, fnmatch
paths = [p for p in open(sys.argv[1], encoding='utf-8').read().split('\0') if p]
rows = re.findall(r'^\| `([^`]+)` \|', open(sys.argv[2], encoding='utf-8').read(), re.M)
missing = [p for p in paths if not any(p == r or fnmatch.fnmatch(p, r) for r in rows)]
print('files:', len(paths), 'missing:', len(missing)); print('\n'.join(missing[:50]))
EOF
```

Expected: `missing: 0`.

## 3. No requirement keywords in the body (SC-003)

```bash
grep -n -E '\b(MUST|SHOULD|SHALL)\b|必须|禁止|不得' docs/design-archive/*.md
```

Expected: no line, or only lines where the word is inside a quotation of a source.

## 4. Every statement has a pointer (FR-003)

```bash
python -I - docs/design-archive/*.md <<'EOF'
import re, sys
for f in sys.argv[1:]:
    if f.endswith(('README.md', 'open-points.md', 'coverage.md')): continue
    text = open(f, encoding='utf-8').read()
    blocks = [b for b in re.split(r'\n\s*\n', text) if b.strip() and not b.lstrip().startswith('#')]
    for b in blocks[1:]:
        for item in re.split(r'\n(?=- |> - )', b):
            if not re.search(r'` L\d+', item):
                print(f, '::', item.strip()[:100])
EOF
```

Expected: no output, other than sentences that link sections.

## 5. Every conflict and unverified point is indexed (SC-004)

```bash
grep -c -E '^\> \*\*(Conflict|Unverified)\*\*' docs/design-archive/*.md
grep -c -E '^- ' docs/design-archive/open-points.md
```

Expected: the sum of the first equals the entries of `open-points.md`.

## 6. Review of statements against their passages (SC-001)

Pick at least 30 statements across all sections, at random, and open each pointer at the pinned commit (research.md
R-6). Each passage says what its statement says, and the statement adds nothing. Record the result in the pull request.

```bash
python -I - docs/design-archive/*.md <<'EOF'
import random, re, sys
items = []
for f in sys.argv[1:]:
    for n, line in enumerate(open(f, encoding='utf-8'), 1):
        if re.search(r'` L\d+', line): items.append(f'{f}:{n}')
random.seed(17)
print('\n'.join(random.sample(items, min(30, len(items)))))
EOF
```

## 7. The roadmap's slices are covered (SC-005)

For each of R1 to R16 in `ROADMAP.md`, the archive has a section whose headings cover the slice's intent, or an
unverified marking for it. Record the slice-to-section list in the pull request.

## 8. No trait of the base game's Empire is added (SC-006)

```bash
grep -n -i -E 'hypertech|techno-?feudal|peerage|title|psylink|psycast|bestower|stellarch|超科技|技术封建|爵位|头衔' docs/design-archive/*.md
```

Expected: every line found cites a passage that states it of Imperium.
