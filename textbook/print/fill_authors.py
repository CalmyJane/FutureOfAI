"""Replace "and others" in bibliography author lists with the full list (APA 7 names up to 20 authors).

Authors come from Crossref (by DOI) or the arXiv API (by arXiv ID, or by exact title search when the
entry has no identifier). Entries that cannot be matched are left unchanged and reported.

Run:  python3 textbook/print/fill_authors.py [bib files...]   (default: all chapter bibs)
"""
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

TB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "understanding-ai-bibcheck/1.0"}
CACHE = {}


def get(url):
    if url in CACHE:
        return CACHE[url]
    for t in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read()
            CACHE[url] = data
            return data
        except Exception:
            time.sleep(2 * (t + 1))
    return None


def norm(s):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\\[a-z]+|[{}]", "", s.lower()))


def from_crossref(doi):
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/"))
    if not d:
        return None, None
    m = json.loads(d)["message"]
    names = []
    for a in m.get("author", []):
        if a.get("family"):
            names.append(f"{a['family']}, {a.get('given', '')}".strip(", "))
        elif a.get("name"):
            names.append("{" + a["name"] + "}")
    return names, (m.get("title") or [""])[0]


def from_arxiv(query):
    d = get("https://export.arxiv.org/api/query?" + query)
    if not d:
        return None, None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    e = ET.fromstring(d).find("a:entry", ns)
    if e is None or e.find("a:title", ns) is None:
        return None, None
    names = []
    for a in e.findall("a:author", ns):
        full = a.find("a:name", ns).text.strip()
        parts = full.split()
        names.append(f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else full)
    return names, re.sub(r"\s+", " ", e.find("a:title", ns).text)


def bibtex_names(names):
    out = []
    for n in names:
        n = n.replace("&", "\\&")
        out.append(n)
    return " and ".join(out)


def resolve(fields):
    title = fields.get("title", "")
    doi = fields.get("doi", "")
    arx = re.search(r"(\d{4}\.\d{4,5})", doi if "48550" in doi else fields.get("url", "") + " " + fields.get("eprint", ""))
    if doi and "48550" not in doi:
        names, t = from_crossref(doi)
        if names:
            return names, t
    if arx:
        names, t = from_arxiv("id_list=" + arx.group(1))
        if names:
            return names, t
    if title:
        q = re.sub(r"[{}\\]", "", title)
        names, t = from_arxiv("search_query=" + urllib.parse.quote(f'ti:"{q}"') + "&max_results=1")
        if names and norm(t) == norm(q):
            return names, t
    return None, None


def main(files):
    done, left = 0, []
    for f in files:
        text = open(f, encoding="utf-8").read()
        def fix(m):
            nonlocal done
            key, body = m.group(2), m.group(3)
            am = re.search(r"(\n\s*author\s*=\s*\{)((?:[^{}]|\{[^{}]*\})*)(\})", body)
            if not am or "and others" not in am.group(2):
                return m.group(0)
            fields = {k.lower(): v for k, v in re.findall(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", body)}
            names, t = resolve(fields)
            first_bib = norm(am.group(2).split(" and ")[0].split(",")[0])
            if not names or norm(names[0].split(",")[0]) not in (first_bib, ) and first_bib not in norm(names[0]):
                left.append(f"{os.path.basename(f)}:{key}")
                return m.group(0)
            done += 1
            body = body[: am.start(2)] + bibtex_names(names) + body[am.end(2):]
            return m.group(1) + key + "," + body + m.group(4)
        new = re.sub(r"(@\w+\s*\{\s*)([^,\s]+)\s*,(.*?)(\n\})", fix, text, flags=re.S)
        if new != text:
            open(f, "w", encoding="utf-8").write(new)
    print(f"filled {done}; left unchanged: {len(left)}")
    for k in left:
        print("  ", k)


if __name__ == "__main__":
    main(sys.argv[1:] or sorted(glob.glob(os.path.join(TB, "bib", "ch*.bib"))))
