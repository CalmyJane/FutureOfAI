"""Render figures to a PNG contact sheet for checking: python3 preview.py out.png fig-ids..."""
import sys, os, subprocess, tempfile
out, ids = sys.argv[1], sys.argv[2:]
here = os.path.dirname(os.path.abspath(__file__))
html = '<html><head><style>@page{size:148mm 420mm;margin:6mm} img{width:113mm;display:block;margin:0 auto 6mm;border:0.2pt solid #ddd}</style></head><body>'
for i in ids: html += f'<p style="font:8pt sans-serif">{i}</p><img src="file://{os.path.join(os.path.dirname(here), "figures", "svg", i)}.svg">'
html += '</body></html>'
d = tempfile.mkdtemp()
open(os.path.join(d, '_prev.html'), 'w').write(html)
subprocess.run([sys.executable, '-m', 'weasyprint', os.path.join(d, '_prev.html'), os.path.join(d, 'p.pdf')], check=True, capture_output=True)
subprocess.run(['pdftoppm', '-r', '110', '-png', os.path.join(d, 'p.pdf'), os.path.join(d, 'p')], check=True)
pngs = sorted(f for f in os.listdir(d) if f.endswith('.png') and f.startswith('p-'))
subprocess.run(['convert'] + [os.path.join(d, p) for p in pngs] + ['+append', out], check=True)
print(out)
