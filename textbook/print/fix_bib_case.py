"""Protect proper nouns in bibliography titles so that APA sentence case does not lower-case them.

APA (and the CSL style) prints titles in sentence case: every word after the first is lower-cased
unless it is wrapped in braces. A word is protected here when the book's own text treats it as a
proper noun: it appears capitalised in mid-sentence and rarely or never in lower case. Months,
days and a list of place and organisation words are always protected. Idempotent.

Run:  python3 textbook/print/fix_bib_case.py [--dry]
"""
import collections
import glob
import os
import re
import sys

TB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALWAYS = set("""January February March April May June July August September October November December
Monday Tuesday Wednesday Thursday Friday Saturday Sunday English French German Spanish Italian Chinese
Japanese Korean Hindi Swahili Polish Danish Dutch Swedish British European American African Asian Indian
Brazilian Canadian Australian Russian Ukrainian Irish Scottish Welsh Nigerian Ghanaian Kenyan Turkish Israeli Rs""".split()) - {"May"}
FUNCTION = set("Does Not Any Our We You Your How Why What When Who Can Is Are Was Were Will It Its This That These Those Be Been Has Have Had Do Did Should Would Could Must May Might All Some More Most".split())
NEVER = set("Section Chapter Table Figure Part Box Center Centre Labor Labour Strategic Report Act".split())


def corpus_counts():
    text = " ".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(TB, "chapters", "ch*.md")))
    text = re.sub(r"\[@[^\]]*\]|\{[^}]*\}|`[^`]*`", " ", text)
    cap_mid, low = collections.Counter(), collections.Counter()
    for m in re.finditer(r"(?<=[a-z0-9,;)] )([A-Za-z][a-z]+)\b", text):
        w = m.group(1)
        if w[0].isupper():
            cap_mid[w] += 1
        else:
            low[w.capitalize()] += 1
    caps = collections.Counter(m.group(0) for m in re.finditer(r"(?<=[a-z0-9,;)] )[A-Z][a-z]+(?: [A-Z][a-z]+)+\b", text))
    lower_text = text.lower()
    phrases = set()
    for ph, n in caps.items():
        words = ph.split()
        for i in range(len(words) - 1):
            for j in range(i + 2, len(words) + 1):
                sub = " ".join(words[i:j])
                if set(sub.split()) & FUNCTION:
                    continue
                if sum(c for p2, c in caps.items() if sub in p2) >= 2 and not re.search(r"(?<![\w])" + re.escape(sub.lower()) + r"(?![\w])", re.sub(r"(?<![\w])" + re.escape(sub) + r"(?![\w])", "", text).lower()):
                    phrases.add(sub)
    return cap_mid, low, phrases


def protect_title(title, cap_mid, low, phrases=None):
    # leave already-braced spans alone; work on the text outside braces at depth 0
    out, depth, buf, first = [], 0, "", True
    def flush(seg, is_first):
        def rep(m):
            nonlocal is_first
            w = m.group(0)
            if is_first:
                is_first = False
                return w
            if w == "May" and re.match(r"\s*\d", seg[m.end():]):
                return "{May}"
            if re.fullmatch(r"[A-Z][a-z]+", w) and w not in NEVER and w != "May" and (w in ALWAYS or (cap_mid[w] >= 2 and cap_mid[w] > 4 * low[w]) or (cap_mid[w] >= 2 and low[w] == 0)):
                return "{" + w + "}"
            return w
        # filing names such as "Form 10-K" keep their capitals
        seg = re.sub(r"(?<!\{)\b(Form \d+-[A-Z])\b", r"{\1}", seg)
        # multi-word proper names the book itself writes in capitals ("Golden Gate", "South Korea")
        if phrases:
            def rep_phrase(m):
                words = m.group(0).split()
                start = 1 if (is_first and m.start() == len(seg) - len(seg.lstrip())) else 0
                if any(" ".join(words[i:j]) in phrases for i in range(len(words)) for j in range(i + 2, len(words) + 1)):
                    return " ".join(w if k < start else "{" + w + "}" for k, w in enumerate(words))
                return m.group(0)
            seg = re.sub(r"(?<![{\w])[A-Z][a-z]+(?: [A-Z][a-z]+)+(?![}\w])", rep_phrase, seg)
        res = re.sub(r"(?<![{\w])[A-Za-z][A-Za-z'’\-]*(?![}\w])", rep, seg)
        return res, is_first
    for ch in title:
        if ch == "{":
            if depth == 0 and buf:
                seg, first = flush(buf, first)
                out.append(seg)
                buf = ""
            depth += 1
            out.append(ch)
            first = False if depth == 1 and first and False else first
        elif ch == "}":
            depth -= 1
            out.append(ch)
            if depth == 0:
                first = False
        elif depth == 0:
            buf += ch
        else:
            out.append(ch)
    if buf:
        seg, first = flush(buf, first)
        out.append(seg)
    return "".join(out)


def main(dry):
    cap_mid, low, phrases = corpus_counts()
    changed = 0
    for f in sorted(glob.glob(os.path.join(TB, "bib", "*.bib"))):
        text = open(f, encoding="utf-8").read()
        def fix(m):
            nonlocal changed
            new = protect_title(m.group(2), cap_mid, low, phrases)
            if new != m.group(2):
                changed += 1
                if dry:
                    print(f"{os.path.basename(f)}: {m.group(2)[:90]}\n    -> {new[:110]}")
            return m.group(1) + new + m.group(3)
        new_text = re.sub(r"(\n\s*title\s*=\s*\{)((?:[^{}]|\{[^{}]*\})*)(\})", fix, text)
        if not dry and new_text != text:
            open(f, "w", encoding="utf-8").write(new_text)
    print(f"titles changed: {changed}")


if __name__ == "__main__":
    main("--dry" in sys.argv)
