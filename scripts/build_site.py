#!/usr/bin/env python3
"""Generate SEO content pages for the HomeForge site from source.

Outputs (all under site/):
  hf.css                      shared stylesheet for generated pages
  picks.html                  full on-site catalog (from data/picks.json)
  learn.html                  content hub linking guides + projects + catalog
  guides/<slug>.html          one page per publishable guide (from guides/*.md)
  projects/<slug>.html        one page per publishable project (from projects/*.md)
  sitemap.xml                 regenerated to include every public page

Run: python3 scripts/build_site.py   (stdlib only; run after editing picks/guides/projects)
"""
import json, re, pathlib, html as _html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = json.loads((ROOT / "data" / "picks.json").read_text(encoding="utf-8"))
SITE_URL = DATA.get("site_url", "https://estivonponcho.github.io/homeforge/").rstrip("/") + "/"

# guides/projects markdown that should NOT become public pages
SKIP = {"README.md", "model-watch-template.md", "custom-apps-and-health-integrations.md"}

# Guides that get their own "Model Watch" hub instead of the general Guides grid:
# any file named model-watch-*.md (the recurring drafting routine), plus these
# hand-written comparison pieces. Explicit order controls display order on the
# Model Watch page; anything not listed here falls in after, in file order.
MODEL_WATCH_EXTRA = {
    "deepseek-v4-1-flash-vs-open-weight-rivals-2026",
    "frontier-model-comparison-september-2026",
    "frontier-model-api-pricing-comparison-2026",
    "frontier-vs-open-weight-decision-guide-2026",
    "how-2026-open-weight-models-actually-work",
    "what-it-takes-to-self-host-a-2026-open-weight-model",
    "open-weight-ai-licenses-2026-explained",
    "gpt-6-astra-deep-dive-2026",
    "is-gpt-6-astra-agi-2026",
    "hugging-face-incident-2026-explained",
}
MODEL_WATCH_ORDER = [
    "model-watch-deepseek-v4-1-flash-2026-09-14",
    "frontier-model-comparison-september-2026",
    "gpt-6-astra-deep-dive-2026",
    "hugging-face-incident-2026-explained",
    "is-gpt-6-astra-agi-2026",
    "frontier-model-api-pricing-comparison-2026",
    "deepseek-v4-1-flash-vs-open-weight-rivals-2026",
    "how-2026-open-weight-models-actually-work",
    "what-it-takes-to-self-host-a-2026-open-weight-model",
    "open-weight-ai-licenses-2026-explained",
    "frontier-vs-open-weight-decision-guide-2026",
]


def is_model_watch(slug: str) -> bool:
    return slug.startswith("model-watch-") or slug in MODEL_WATCH_EXTRA


# Vendor/company badge shown on each Model Watch card, for scanning the section
# by maker. Pieces covering multiple vendors list them; the frontier-vs-open-
# weight piece is framed as a category rather than a vendor list. A future
# model-watch-*.md file with no entry here just shows the "Model Watch" tag
# alone — this is cosmetic, not required for the automation to work.
MODEL_WATCH_VENDORS = {
    "model-watch-deepseek-v4-1-flash-2026-09-14": "DeepSeek",
    "frontier-model-comparison-september-2026": "Claude · GPT · Gemini · Grok",
    "frontier-model-api-pricing-comparison-2026": "Claude · GPT · Gemini · Grok",
    "deepseek-v4-1-flash-vs-open-weight-rivals-2026": "DeepSeek · Kimi · GLM · Qwen",
    "how-2026-open-weight-models-actually-work": "DeepSeek · Kimi · GLM · Qwen",
    "what-it-takes-to-self-host-a-2026-open-weight-model": "DeepSeek · Kimi · GLM · Qwen",
    "open-weight-ai-licenses-2026-explained": "DeepSeek · Kimi · GLM · Qwen",
    "frontier-vs-open-weight-decision-guide-2026": "Frontier vs open-weight",
    "gpt-6-astra-deep-dive-2026": "OpenAI",
    "is-gpt-6-astra-agi-2026": "OpenAI · Anthropic · Google DeepMind",
    "hugging-face-incident-2026-explained": "OpenAI · Anthropic · Moonshot",
}

ANCHOR_MAP = {
    "../README.md#-smart-home": "../picks.html#smart-home",
    "../README.md#-homelab--self-hosting": "../picks.html#homelab",
    "../README.md#-3d-printing": "../picks.html#3d-printing",
    "../README.md#-ai--local-llms": "../picks.html#ai",
    "../README.md": "../picks.html",
}
PILLAR_ANCHOR = {"smart-home": "smart-home", "homelab": "homelab", "3d-printing": "3d-printing", "ai": "ai"}


def rewrite_link(url: str) -> str:
    if url.startswith("http") or url.startswith("mailto:") or url.startswith("#"):
        return url
    if url in ANCHOR_MAP:
        return ANCHOR_MAP[url]
    if url.startswith("../README.md#"):
        return "../picks.html"  # unknown anchor -> catalog top
    if url.endswith(".md"):
        return url[:-3] + ".html"
    return url


# ---------- minimal markdown -> html ----------
def _inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    def link(m):
        url = rewrite_link(m.group(2))
        rel = ' rel="nofollow sponsored noopener"' if "amazon.com" in url else (' rel="noopener"' if url.startswith("http") else "")
        return f'<a href="{url}"{rel}>{m.group(1)}</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w`])_([^_]+)_(?![\w`])", r"<em>\1</em>", text)
    return text


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        # fenced code
        if line.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue
        # blank
        if not line.strip():
            i += 1
            continue
        # raw HTML block (e.g. embedded SVG diagrams) — pass through verbatim
        if line.lstrip().startswith(("<figure", "<svg", "<div", "<img", "<picture")):
            buf = []
            while i < n and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue
        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2).strip())}</h{lvl}>")
            i += 1
            continue
        # hr
        if re.match(r"^(---+|\*\*\*+)\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        # table
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{_inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            continue
        # blockquote
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(buf))}</blockquote>")
            continue
        # unordered list (with wrapped-line + blank-separated item continuation)
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n:
                m = re.match(r"^\s*[-*]\s+(.*)$", lines[i])
                if m:
                    text = m.group(1); i += 1
                    while i < n and lines[i].strip() and not re.match(r"^\s*(\d+\.\s|[-*]\s|#{1,6}\s|>|```|---+|\*\*\*+)", lines[i]):
                        text += " " + lines[i].strip(); i += 1
                    items.append("<li>" + _inline(text) + "</li>")
                elif not lines[i].strip():
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and re.match(r"^\s*[-*]\s+", lines[j]):
                        i = j
                    else:
                        break
                else:
                    break
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n:
                m = re.match(r"^\s*\d+\.\s+(.*)$", lines[i])
                if m:
                    text = m.group(1); i += 1
                    while i < n and lines[i].strip() and not re.match(r"^\s*(\d+\.\s|[-*]\s|#{1,6}\s|>|```|---+|\*\*\*+)", lines[i]):
                        text += " " + lines[i].strip(); i += 1
                    items.append("<li>" + _inline(text) + "</li>")
                elif not lines[i].strip():
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and re.match(r"^\s*\d+\.\s+", lines[j]):
                        i = j
                    else:
                        break
                else:
                    break
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        # paragraph
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|>|```|\s*[-*]\s|\s*\d+\.\s|---+|\*\*\*+)", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + _inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


# ---------- page shell ----------
CSS = """:root{--ground:#F4F3F0;--surface:#fff;--surface2:#FBF9F6;--ink:#1B1712;--muted:#6E6559;--line:#E5E1D9;--accent:#C9531B;--smart:#B8531E;--lab:#1C6E79;--print:#6D42B8;--ai:#2D5FB0}
@media(prefers-color-scheme:dark){:root{--ground:#161309;--surface:#211C13;--surface2:#1B1710;--ink:#F1EADD;--muted:#A99C88;--line:#342C21;--accent:#F0743A;--smart:#F0743A;--lab:#46B7C2;--print:#B48CF0;--ai:#7EA8F0}}
*{box-sizing:border-box}body{margin:0;background:var(--ground);color:var(--ink);font-family:"IBM Plex Sans",system-ui,sans-serif;line-height:1.6}
.wrap{max-width:1040px;margin:auto;padding:0 22px}.article{max-width:74ch}
a{color:var(--ink)}a:hover{color:var(--accent)}
header{border-bottom:1px solid var(--line);padding:14px 0;position:sticky;top:0;background:color-mix(in srgb,var(--ground) 88%,transparent);backdrop-filter:blur(8px);z-index:10}
.bar{display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{color:var(--ink);font-family:"Bricolage Grotesque",sans-serif;font-weight:800;text-decoration:none;font-size:1.1rem}.brand span{color:var(--accent)}
.nav{display:flex;gap:8px;flex-wrap:wrap}.nav a{font:500 .76rem "IBM Plex Mono",monospace;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 11px;background:var(--surface);color:var(--ink)}.nav a:hover{border-color:var(--accent)}
main{padding:48px 0 64px}
.eyebrow{font:500 .72rem "IBM Plex Mono",monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
h1,h2,h3,h4{font-family:"Bricolage Grotesque",sans-serif;line-height:1.15;text-wrap:balance}
.article h1{font-size:clamp(2rem,5vw,3rem);margin:14px 0 8px}
.article h2{font-size:1.5rem;margin:1.8em 0 .4em}.article h3{font-size:1.18rem;margin:1.5em 0 .3em}
.article p,.article li{color:var(--ink)}.article .lede,.lede{font-size:1.12rem;color:var(--muted);max-width:66ch}
.article ul,.article ol{padding-left:22px}.article li{margin:8px 0}
.article a{color:var(--accent);text-underline-offset:3px}
blockquote{margin:18px 0;padding:12px 16px;border-left:3px solid var(--accent);background:var(--surface);border-radius:8px;color:var(--muted)}
code{font-family:"IBM Plex Mono",monospace;font-size:.9em;background:var(--surface2);border:1px solid var(--line);border-radius:5px;padding:1px 5px}
pre{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px;overflow-x:auto}pre code{border:none;background:none;padding:0}
.tablewrap{overflow-x:auto;margin:16px 0}table{border-collapse:collapse;width:100%;font-size:.94rem}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left}th{background:var(--surface)}
hr{border:none;border-top:1px solid var(--line);margin:32px 0}
.crumb{color:var(--muted);font:500 .78rem "IBM Plex Mono",monospace;margin-bottom:8px}.crumb a{color:var(--muted);text-decoration:none}.crumb a:hover{color:var(--accent)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:22px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:20px;text-decoration:none;color:var(--ink);display:block}
.card:hover{border-color:var(--accent)}.card .tag{font:500 .66rem "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.card .tag.vtag{margin-left:8px;padding:1px 7px;border:1px solid var(--line);border-radius:6px;text-transform:none;letter-spacing:.02em;color:var(--ai)}
.card h3{margin:8px 0 6px;font-size:1.15rem}.card p{margin:0;color:var(--muted);font-size:.9rem}
.pillar{margin-top:40px}.pillar h2{font-size:1.6rem}.cat{font:500 .72rem "IBM Plex Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:20px 0 6px}
.picklist{list-style:none;padding:0;margin:0}.picklist li{padding:12px 0;border-top:1px solid var(--line)}.picklist li:first-child{border-top:none}
.picktop{display:flex;justify-content:space-between;gap:10px;align-items:baseline}.picktop a{font-weight:600;text-decoration:none;color:var(--ink)}.picktop a:hover{color:var(--accent)}
.tier{font:500 .7rem "IBM Plex Mono",monospace;color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:2px 6px;white-space:nowrap}
.blurb{display:block;color:var(--muted);font-size:.9rem;margin-top:3px}
.disc{margin:22px 0;padding:14px 16px;border:1px dashed var(--line);border-radius:12px;color:var(--muted);font-size:.9rem}
.cta{display:inline-block;margin-top:26px;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;padding:12px 18px;border-radius:10px}
footer{border-top:1px solid var(--line);padding:26px 0 48px;color:var(--muted);font-size:.85rem}
footer a{color:var(--ink)}footer .fl{display:flex;gap:16px;flex-wrap:wrap;font-family:"IBM Plex Mono",monospace;font-size:.78rem;margin-top:8px}
figure.diagram{margin:22px 0;padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface);overflow-x:auto}
figure.diagram svg{max-width:100%;height:auto;display:block;margin:auto}
figure.diagram img{max-width:100%;height:auto;display:block;margin:auto;border-radius:8px}
figure.diagram text{fill:var(--ink)}figure.diagram .wire{stroke:var(--ink)}figure.diagram .data{stroke:var(--accent)}figure.diagram .box{fill:var(--surface2);stroke:var(--ink)}
figure.diagram figcaption{margin-top:10px;color:var(--muted);font-size:.85rem;text-align:center}
@media(max-width:720px){main{padding-top:34px}}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Bricolage+Grotesque:wght@500;700;800&family=IBM+Plex+Mono:wght@400;500&'
         'family=IBM+Plex+Sans:wght@400;500;600&display=swap">')

ANALYTICS = ('<script data-goatcounter="https://homeforge.goatcounter.com/count" '
             'async src="//gc.zgo.at/count.js"></script>')


def page(title, description, canonical, body, root="", jsonld="", social_image=""):
    desc = _html.escape(description, quote=True)
    social_meta = ""
    if social_image:
        image = _html.escape(social_image, quote=True)
        social_meta = (f'<meta property="og:image" content="{image}">\n'
                       f'<meta property="og:image:secure_url" content="{image}">\n'
                       '<meta property="og:image:type" content="image/png">\n'
                       '<meta property="og:image:width" content="1122">\n'
                       '<meta property="og:image:height" content="1402">\n'
                       '<meta property="og:image:alt" content="HomeForge Home Assistant system diagram">\n'
                       '<meta name="twitter:card" content="summary_large_image">\n'
                       f'<meta name="twitter:image" content="{image}">')
    nav = (f'<a href="{root}index.html">Home</a>'
           f'<a href="{root}picks.html">The list</a>'
           f'<a href="{root}learn.html">Guides</a>'
           f'<a href="{root}model-watch.html">Model Watch</a>'
           f'<a href="{root}resources.html">Watch &amp; build</a>'
           f'<a href="{root}starter-kit.html">Starter kit</a>')
    foot = (f'<a href="{root}index.html">Home</a><a href="{root}picks.html">The list</a>'
            f'<a href="{root}learn.html">Guides</a>'
            f'<a href="https://github.com/{DATA.get("repo","estivonponcho/homeforge")}/blob/main/AFFILIATE-DISCLOSURE.md">Disclosure</a>'
            f'<a href="{root}privacy.html">Privacy</a><a href="{root}terms.html">Terms</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{_html.escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="HomeForge">
{social_meta}
{FONTS}
<link rel="stylesheet" href="{root}hf.css">
{jsonld}
{ANALYTICS}
</head>
<body>
<header><div class="wrap bar"><a class="brand" href="{root}index.html"><span>&#9650;</span> HomeForge</a><nav class="nav">{nav}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">HomeForge is reader-supported; some links are affiliate links (no extra cost to you).<div class="fl">{foot}</div></div></footer>
</body>
</html>
"""


def first_para(md):
    for block in md.split("\n\n"):
        b = block.strip()
        if (b and not b.startswith("#") and not b.startswith(">")
                and not b.startswith("*") and not re.fullmatch(r"[-_]{3,}", b)):
            return re.sub(r"[\[\]*_`]", "", re.sub(r"\]\(([^)]+)\)", "", b)).replace("\n", " ")[:155]
    return DATA.get("tagline", "HomeForge")


def title_of(md, fallback):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return (re.sub(r"[*_`]", "", m.group(1)).strip() if m else fallback)


def build_md_pages(folder, kind):
    pages = []
    d = ROOT / folder
    for f in sorted(d.glob("*.md")):
        if f.name in SKIP:
            continue
        md = f.read_text(encoding="utf-8")
        slug = f.stem
        t = title_of(md, slug)
        desc = first_para(md)
        canonical = f"{SITE_URL}{folder}/{slug}.html"
        social_image = ""
        image_match = re.search(r'<img\s+[^>]*src="\.\./assets/([^"?#]+)', md, re.I)
        if image_match:
            social_image = f"{SITE_URL}assets/{image_match.group(1)}"
        model_watch = folder == "guides" and is_model_watch(slug)
        hub_label = "Model Watch" if model_watch else kind
        hub_url = "model-watch.html" if model_watch else "learn.html"
        # strip the leading H1 from body (we render it in .article too, keep it once)
        body = (f'<div class="article">'
                f'<p class="crumb"><a href="../index.html">HomeForge</a> / <a href="../{hub_url}">{hub_label}</a></p>'
                f'{md_to_html(md)}'
                f'<hr><a class="cta" href="../starter-kit.html">Get the free Starter Kit &rarr;</a>'
                f'</div>')
        ld = [
            {"@context": "https://schema.org", "@type": "Article", "headline": t,
             "description": desc, "url": canonical, "mainEntityOfPage": canonical,
             "author": {"@type": "Person", "name": "Mike Cage"},
             "publisher": {"@type": "Organization", "name": "HomeForge"}},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "HomeForge", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": hub_label, "item": SITE_URL + hub_url},
                {"@type": "ListItem", "position": 3, "name": t, "item": canonical}]},
        ]
        jsonld = '<script type="application/ld+json">' + json.dumps(ld) + "</script>"
        (SITE / folder).mkdir(parents=True, exist_ok=True)
        (SITE / folder / f"{slug}.html").write_text(
            page(f"{t} — HomeForge", desc, canonical, body, root="../", jsonld=jsonld,
                 social_image=social_image), encoding="utf-8")
        pages.append({"slug": slug, "title": t, "desc": desc, "folder": folder,
                      "url": f"{folder}/{slug}.html", "model_watch": model_watch})
    return pages


def build_picks():
    from collections import OrderedDict
    pil = {p["id"]: p for p in DATA["pillars"]}
    by = OrderedDict((p["id"], OrderedDict()) for p in DATA["pillars"])
    for it in DATA["picks"]:
        by.setdefault(it["pillar"], OrderedDict()).setdefault(it["category"], []).append(it)
    total = len(DATA["picks"])
    body = [f'<div class="article" style="max-width:none"><p class="crumb"><a href="index.html">HomeForge</a> / The list</p>',
            f'<span class="eyebrow">{total} curated picks &middot; {len(by)} pillars</span>',
            "<h1>The HomeForge list</h1>",
            f'<p class="lede">{_html.escape(DATA["intro"])}</p>',
            '<p class="disc">Some links are affiliate links (e.g. Amazon Associates) &mdash; if you buy through them we may earn a small commission at no extra cost to you. We only list gear worth owning.</p>']
    for pid, cats in by.items():
        pm = pil[pid]
        body.append(f'<section class="pillar {pid}" id="{PILLAR_ANCHOR.get(pid, pid)}">')
        body.append(f'<h2>{pm["emoji"]} {_html.escape(pm["title"])}</h2>')
        body.append(f'<p class="lede">{_html.escape(pm["blurb"])}</p>')
        for cat, items in cats.items():
            body.append(f'<div class="cat">{_html.escape(cat)}</div><ul class="picklist">')
            for it in items:
                star = " &#11088;" if it.get("featured") else ""
                tier = f'<span class="tier">{_html.escape(it.get("tier",""))}</span>' if it.get("tier") else ""
                body.append(f'<li><div class="picktop"><a href="{it["url"]}" rel="nofollow sponsored noopener" target="_blank">{_html.escape(it["name"])}{star}</a>{tier}</div>'
                            f'<span class="blurb">{_html.escape(it["blurb"])}</span></li>')
            body.append("</ul>")
        body.append("</section>")
    body.append('<hr><a class="cta" href="starter-kit.html">Get the free Starter Kit &rarr;</a></div>')
    (SITE / "picks.html").write_text(
        page("The HomeForge list — smart home, homelab, 3D printing & local AI gear",
             "Every HomeForge pick in one place: curated smart-home, homelab, 3D-printing, and local-AI gear, with an honest one-line take on each.",
             f"{SITE_URL}picks.html", "\n".join(body), root=""), encoding="utf-8")


def build_learn(guides, projects):
    def cards(items, kind):
        out = []
        for p in items:
            out.append(f'<a class="card" href="{p["url"]}"><span class="tag">{kind}</span>'
                       f'<h3>{_html.escape(p["title"])}</h3><p>{_html.escape(p["desc"])}</p></a>')
        return "".join(out)
    body = ['<div class="article" style="max-width:none"><p class="crumb"><a href="index.html">HomeForge</a> / Guides</p>',
            '<span class="eyebrow">Guides &amp; field notes</span>',
            "<h1>Guides &amp; builds</h1>",
            '<p class="lede">Practical, honest write-ups: how to run the tools, and real builds from the bench. Every guide links to the gear it uses. '
            'Covering a specific AI model release or comparing models head-to-head? That\'s over in '
            '<a href="model-watch.html">Model Watch</a>.</p>',
            "<h2>Guides</h2>", f'<div class="cards">{cards(guides, "Guide")}</div>',
            "<h2 style=\"margin-top:40px\">Builds</h2>", f'<div class="cards">{cards(projects, "Build")}</div>',
            '<hr><a class="cta" href="picks.html">Browse the full list &rarr;</a></div>']
    (SITE / "learn.html").write_text(
        page("Guides & builds — HomeForge",
             "Practical guides for running Claude/ChatGPT and local AI, plus real hardware builds: ESP projects, a homelab node, and more.",
             f"{SITE_URL}learn.html", "\n".join(body), root=""), encoding="utf-8")


def build_model_watch(pages):
    ordered = sorted(pages, key=lambda p: MODEL_WATCH_ORDER.index(p["slug"])
                      if p["slug"] in MODEL_WATCH_ORDER else len(MODEL_WATCH_ORDER))

    def cards(items):
        out = []
        for p in items:
            vendor = MODEL_WATCH_VENDORS.get(p["slug"])
            vtag = f'<span class="tag vtag">{_html.escape(vendor)}</span>' if vendor else ""
            out.append(f'<a class="card" href="{p["url"]}"><span class="tag">Model Watch</span>{vtag}'
                       f'<h3>{_html.escape(p["title"])}</h3><p>{_html.escape(p["desc"])}</p></a>')
        return "".join(out)
    body = ['<div class="article" style="max-width:none"><p class="crumb"><a href="index.html">HomeForge</a> / Model Watch</p>',
            '<span class="eyebrow">AI model releases &amp; comparisons</span>',
            "<h1>Model Watch</h1>",
            '<p class="lede">Notable AI model releases and honest head-to-head comparisons — frontier and open-weight alike — with '
            'sourced benchmarks, real pricing math, and no padded hype. General AI usage guides live over in '
            '<a href="learn.html">Guides</a>.</p>',
            f'<div class="cards">{cards(ordered)}</div>',
            '<hr><a class="cta" href="learn.html">Browse all guides &rarr;</a></div>']
    (SITE / "model-watch.html").write_text(
        page("Model Watch — AI model releases & comparisons — HomeForge",
             "Notable AI model releases and head-to-head comparisons across frontier and open-weight models, with sourced benchmarks and real pricing math.",
             f"{SITE_URL}model-watch.html", "\n".join(body), root=""), encoding="utf-8")


def build_sitemap(guides, projects):
    urls = ["", "picks.html", "learn.html", "model-watch.html", "starter-kit.html", "resources.html", "privacy.html", "terms.html"]
    urls += [p["url"] for p in guides] + [p["url"] for p in projects]
    body = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        body.append(f"  <url><loc>{SITE_URL}{u}</loc></url>")
    body.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def main():
    (SITE / "hf.css").write_text(CSS, encoding="utf-8")
    guides = build_md_pages("guides", "Guides")
    projects = build_md_pages("projects", "Builds")
    model_watch = [p for p in guides if p["model_watch"]]
    learn_guides = [p for p in guides if not p["model_watch"]]
    build_picks()
    build_learn(learn_guides, projects)
    build_model_watch(model_watch)
    build_sitemap(guides, projects)
    print(f"Built: picks.html, learn.html, model-watch.html ({len(model_watch)} items), "
          f"{len(learn_guides)} guides, {len(projects)} builds, hf.css, sitemap.xml")


if __name__ == "__main__":
    main()
