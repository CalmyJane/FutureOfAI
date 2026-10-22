"""All figures of the book, drawn from the specs in figures/specs/ in one house style.
Each chapter's figures live in figs_chNN.py and register themselves with @fig("fig-NN-MM").

Run:  python3 textbook/print/figures.py [fig-id ...]
"""
import glob
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figstyle import FIGS  # noqa: E402

for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs_ch*.py"))):
    importlib.import_module(os.path.basename(f)[:-3])

if __name__ == "__main__":
    names = sys.argv[1:] or sorted(FIGS)
    for n in names:
        FIGS[n]()
        print("drew", n)
