"""Fail if the delivered PDF was built from different sources than the ones in the repository.

Run:  python3 textbook/print/check_build.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import TB, source_hash  # noqa: E402

info = os.path.join(TB, "delivery", "BUILD-INFO.txt")
recorded = re.search(r"sources_sha256: (\w+)", open(info).read()).group(1) if os.path.exists(info) else None
if recorded != source_hash():
    sys.exit("delivery PDF is stale: rebuild with python3 textbook/print/figures.py && python3 textbook/print/build.py")
print("delivery PDF matches the sources")
