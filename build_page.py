#!/usr/bin/env python3

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

L = json.load(open("data/layout.json", encoding="utf-8"))

SENTS = L["sentences"]

AR_ORIG = L["size_orig"][1] / L["size_orig"][0]

# ---------------------------------------------------------------- verbatim text
TITLE = "VieText2Sign"
SUBTITLE = ("A 3D Avatar-Based Framework for Vietnamese "
            "Text-to-Sign Language Generation")

AUTHORS = [
    ("Ngoc Son Vu", "sonvn.b22kh104@stu.ptit.edu.vn"),
    ("Van Son Hoang", "sonhoangveneno@gmail.com"),
    ("Ket Dong Vu", "dongvk.b21cn232@stu.ptit.edu.vn"),
    ("Hoai Nam Vu", "namvh@ptit.edu.vn"),
]

AFFIL = ("Young Innovation Research Laboratory on Digital Technology — PTIT<br>"
         "Posts and Telecommunications Institute of Technology, Hanoi, Vietnam")

ABSTRACT = (
    "Sign Language Production (SLP) aims to generate sign language videos from natural language "
    "text, often using gloss sequences as an intermediate representation. This task is hindered by "
    "the scarcity of large-scale 3D sign datasets and the difficulty in modeling smooth "
    "transitions between consecutive signs. To address these challenges, we propose VieText2Sign, "
    "an end-to-end framework for translating Vietnamese text into sign language using a 3D avatar. "
    "The framework integrates a Vietnamese gloss–3D sign dictionary, a Text2Gloss translator, "
    "retrieval-based motion generation, a GCN-based sign connector, and 3D avatar rendering. "
    "However, the retrieved 3D sign motions are inherently discrete, often leading to "
    "discontinuous and unnatural transitions between consecutive signs. To address this "
    "limitation, we introduce an improved GCN-based sign connector that explicitly models "
    "inter-sign dynamics to predict the transition duration between consecutive signs. The "
    "predicted duration is then used to interpolate the SMPL-X parameters between consecutive "
    "signs, producing smoother and more coherent intermediate motion. The final outputs are "
    "rendered via a 3D sign avatar. Experimental results demonstrate that the proposed connector "
    "better captures inter-sign dynamics, contributing to more coherent and continuous sign "
    "sequence generation."
)

INDEX_TERMS = ("Sign Language Production, Text-to-Sign, 3D Avatar, Vietnamese Sign Language, "
               "GCN-based Sign Connector, Motion Generation")

ROW_LABELS = ("Text", "Gloss", "Reference", "VieText2Sign")

# ------------------------------------------------------------------------ style
CSS = """
:root{
  --ink:#14181d; --ink-2:#4a5560; --ink-3:#78838f; --label:#404040;
  --line:#e3e7ec; --line-2:#eef1f4;
  --bg:#ffffff; --bg-2:#f7f9fb; --bg-3:#eff3f7;
  --accent:#1367a7; --accent-2:#0f4f80; --accent-soft:#e8f1f8;
  --conn:#f2f2f2;
  --w:1060px;
}
*{box-sizing:border-box}
body{
  margin:0 auto; padding:0 24px 96px; max-width:var(--w);
  background:var(--bg); color:var(--ink);
  font:400 16.5px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","Helvetica Neue",Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
a{color:var(--accent); text-decoration:none}
a:hover{color:var(--accent-2); text-decoration:underline}
hr{border:0; border-top:1px solid var(--line); margin:40px 0}

/* ---- header ---- */
header{padding:64px 0 4px; text-align:center}
h1.title{margin:0 0 8px; font-size:40px; line-height:1.15; font-weight:600; letter-spacing:-.02em}
.subtitle{margin:0 auto 28px; max-width:680px; font-size:20px; color:var(--ink-2); font-weight:400}
.authors{margin:0; font-size:17.5px}
.authors span{white-space:nowrap}
.authors sup{color:var(--accent); font-size:12px}
.affil{margin:10px 0 0; font-size:15px; color:var(--ink-2)}
.affil sup{color:var(--accent)}
.mails{
  display:flex; flex-wrap:wrap; gap:6px 18px; justify-content:center;
  margin:12px 0 0; font-size:13.5px; color:var(--ink-3);
}
.mails a{color:var(--ink-3)}

/* ---- sections ---- */
h2{
  margin:0 0 16px; font-size:15px; font-weight:700;
  letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3);
}
p{margin:0 0 14px}
.abstract{font-size:17px; line-height:1.72; text-align:justify}
.terms{margin:14px 0 0; font-size:14.5px; color:var(--ink-2)}
.terms b{color:var(--ink)}
.intro{font-size:15.5px; line-height:1.7; color:var(--ink-2)}
.intro b{color:var(--ink)}
.legend{display:flex; flex-wrap:wrap; gap:20px; margin:0 0 34px; font-size:13.5px; color:var(--ink-2)}
.legend div{display:flex; align-items:center; gap:7px}
.swatch{width:26px; height:18px; border-radius:3px; border:1px solid var(--line)}
.swatch.sign{background:var(--accent-soft); border-color:#d5e3ef}
.swatch.conn{background:var(--conn); border-color:#dcdfe3}

/* ---- mục 4: một khối cho mỗi câu ---- */
.item{margin:0 0 40px}
.item h3{
  margin:0 0 10px; font-size:17px; font-weight:700; letter-spacing:-.01em;
}
.tblwrap{overflow-x:auto; padding-bottom:4px; -webkit-overflow-scrolling:touch}
.tbl{
  display:grid; min-width:780px;
  grid-template-columns:128px repeat(var(--n), minmax(0,1fr));
  align-items:stretch; row-gap:0; column-gap:0;
}
.lab{
  display:flex; align-items:center; justify-content:flex-start;
  padding:6px 8px; font-size:12.5px; font-weight:700; color:var(--label); text-align:left;
}
.val{
  display:flex; align-items:center; grid-column:2 / -1;
  padding:7px 10px; font-size:15px; line-height:1.5;
}
.val.gloss{letter-spacing:.01em}
.cell{overflow:hidden; line-height:0}
.cell img{width:100%; display:block}
.cell.void{background:var(--conn); aspect-ratio:var(--ar)}

@media (max-width:820px){
  body{padding:0 16px 64px}
  h1.title{font-size:29px}
  .subtitle{font-size:17px}
  header{padding:34px 0 4px}
}
@media print{
  body{max-width:100%}
  .item{page-break-inside:avoid}
}
"""


# --------------------------------------------------------------------- helpers
def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def table(s):
    cau = f"cau{s['i']:02d}"
    cols = s["cols"]
    n = len(cols)

    gt = "".join(
        (f'<div class="cell"><img loading="lazy" '
         f'src="resources/figs/top10/{cau}_orig_{k}.jpg" alt=""></div>')
        if c["kind"] == "sign" else
        '<div class="cell void"></div>'
        for k, c in enumerate(cols)
    )
    ours = "".join(
        f'<div class="cell"><img loading="lazy" '
        f'src="resources/figs/top10/{cau}_rend_{k}.jpg" alt=""></div>'
        for k in range(n)
    )

    return f"""<div class="tblwrap"><div class="tbl" style="--n:{n}; --ar:{1 / AR_ORIG:.4f}">
  <div class="lab">{ROW_LABELS[0]}</div><div class="val">{esc(s["text"])}</div>
  <div class="lab">{ROW_LABELS[1]}</div><div class="val gloss">{esc(s["gloss_text"].lower())}</div>
  <div class="lab">{ROW_LABELS[2]}</div>{gt}
  <div class="lab">{ROW_LABELS[3]}</div>{ours}
</div></div>"""


def items():
    return "\n".join(
        f'<div class="item">\n  <h3>Sentence {s["i"]}</h3>\n  {table(s)}\n</div>'
        for s in SENTS
    )


# --------------------------------------------------------------------- assemble
authors_html = ", ".join(f'<span>{esc(n)}</span>' for n, _ in AUTHORS)
mails_html = "".join(f'<a href="mailto:{m}">{m}</a>' for _, m in AUTHORS)

n_sign_cols = sum(1 for s in SENTS for c in s["cols"] if c["kind"] == "sign")
n_conn_cols = sum(1 for s in SENTS for c in s["cols"] if c["kind"] == "conn")

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{TITLE}: {SUBTITLE}">
<style>{CSS}</style>
</head>
<body>

<header>
  <h1 class="title">{TITLE}</h1>
  <p class="subtitle">{SUBTITLE}</p>
  <p class="authors">{authors_html}</p>
  <p class="affil">{AFFIL}</p>
  <div class="mails">{mails_html}</div>
</header>

<hr>

<section id="abstract">
<h2>Abstract</h2>
<p class="abstract">{ABSTRACT}</p>
<p class="terms"><b>Index Terms —</b> {INDEX_TERMS}</p>
</section>

<hr>

<section id="visualization">
<h2>Qualitative End-to-End Results</h2>
<p class="intro">Each example presents the input Vietnamese sentence, the predicted gloss sequence, reference sign frames from QIPEDC, and the corresponding VieText2Sign output. Gray cells indicate inter-sign transitions for which no reference frame is available.</p>

{items()}
</section>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"index.html written — {len(HTML) / 1024:.1f} KB")
print(f"  {len(SENTS)} sentences · {n_sign_cols} sign columns · {n_conn_cols} connector columns")
print(f"  row labels: {' / '.join(ROW_LABELS)}")
