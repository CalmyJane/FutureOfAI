"""List paragraphs, list items and captions without a citation. Usage: python3 uncited.py chapters/chNN.md"""
import re
import sys

for f in sys.argv[1:]:
    t = open(f, encoding="utf-8").read()
    n = 0
    for block in re.split(r"\n\s*\n", t):
        items = re.split(r"\n(?=- |\d+\. )", block.strip())
        for s in items:
            s = s.strip()
            if not s or s.startswith(("#", "|", "```")) or re.fullmatch(r":::.*", s):
                continue
            s2 = re.sub(r"^:::.*\n", "", s)
            if "@" in s2 or len(s2.split()) < 12:
                continue
            if re.match(r"\*\*[^*]+\*\*\s*$", s2):
                continue
            n += 1
            line = t[: t.find(s)].count("\n") + 1
            print(f"{f}:{line}: {s2[:140]!r}")
    print(f"{f}: {n} uncited blocks", file=sys.stderr)
