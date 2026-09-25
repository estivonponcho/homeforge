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
from urllib.parse import parse_qs, urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = json.loads((ROOT / "data" / "picks.json").read_text(encoding="utf-8"))
SITE_URL = DATA.get("site_url", "https://estivonponcho.github.io/homeforge/").rstrip("/") + "/"

# guides/projects markdown that should NOT become public pages
SKIP = {"README.md", "model-watch-template.md", "custom-apps-and-health-integrations.md"}
AI_SAFETY_ORDER = ["ai-safety-deep-research-departures-risks-mitigations", "ai-agent-compaction-summary-security", "monitor-ai-agents-with-receipts", "ai-safety-frontier-debate-september-2026", "ai-safety-researcher-departures-timeline", "ai-safety-practical-agent-checklist"]

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
    if url.startswith(("../assets/", "assets/")):
        return url  # downloadable source files are not generated article pages
    if url.endswith(".md"):
        return url[:-3] + ".html"
    return url


def track_affiliate_clicks(body: str, canonical: str) -> str:
    """Mark tagged Amazon links as GoatCounter events scoped to this page."""
    page_key = re.sub(r"[^a-z0-9-]+", "-", urlparse(canonical).path.strip("/").lower()).strip("-") or "home"

    def mark(match):
        tag = match.group(0)
        href_match = re.search(r'\bhref="([^"]+)"', tag)
        if not href_match or "data-goatcounter-click=" in tag:
            return tag
        url = urlparse(_html.unescape(href_match.group(1)))
        if url.hostname not in {"amazon.com", "www.amazon.com"} or not parse_qs(url.query).get("tag"):
            return tag
        return tag[:-1] + f' data-goatcounter-click="retailer-amazon-{page_key}">'

    return re.sub(r"<a\b[^>]*>", mark, body)


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
.bar{display:flex;align-items:center;gap:12px;position:relative}
.brand{color:var(--ink);font-family:"Bricolage Grotesque",sans-serif;font-weight:800;text-decoration:none;font-size:1.1rem;margin-right:auto}.brand span{color:var(--accent)}
.nav{display:flex;gap:6px;align-items:center;flex-wrap:nowrap}
.nav a,.navbtn{font:500 .76rem "IBM Plex Mono",monospace;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 10px;background:var(--surface);color:var(--ink);display:inline-flex;align-items:center;gap:6px;line-height:1;cursor:pointer}
.nav a:hover,.navbtn:hover{border-color:var(--accent);color:var(--accent)}
.nav svg,.navbtn svg{width:14px;height:14px;flex:none;stroke:currentColor;stroke-width:1.6;fill:none;stroke-linecap:round;stroke-linejoin:round;display:block}
.bar .navtoggle{display:none}
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
.newsletter-inline{margin:32px 0 0;padding:22px;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.newsletter-inline h2{margin:0 0 8px}.newsletter-inline p{margin:0 0 14px}
.newsletter-inline form{display:flex;gap:10px;flex-wrap:wrap;align-items:end}
.newsletter-inline label{display:block;font-weight:600;font-size:.9rem;margin-bottom:5px}
.newsletter-inline input[type=email]{width:min(100%,340px);padding:11px 12px;border:1px solid var(--line);border-radius:8px;background:var(--ground);color:var(--ink);font:inherit}
.newsletter-inline input[type=email]:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.newsletter-inline button{padding:11px 16px;border:0;border-radius:8px;background:var(--accent);color:#fff;font:600 1rem "IBM Plex Sans",sans-serif;cursor:pointer}
.newsletter-inline button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.newsletter-inline .small{margin:12px 0 0;color:var(--muted);font-size:.82rem}
footer{border-top:1px solid var(--line);padding:26px 0 48px;color:var(--muted);font-size:.85rem}
footer a{color:var(--ink)}footer .fl{display:flex;gap:16px;flex-wrap:wrap;font-family:"IBM Plex Mono",monospace;font-size:.78rem;margin-top:8px}
figure.diagram{margin:22px 0;padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface);overflow-x:auto}
figure.diagram svg{max-width:100%;height:auto;display:block;margin:auto}
figure.diagram img{max-width:100%;height:auto;display:block;margin:auto;border-radius:8px}
figure.diagram text{fill:var(--ink)}figure.diagram .wire{stroke:var(--ink)}figure.diagram .data{stroke:var(--accent)}figure.diagram .box{fill:var(--surface2);stroke:var(--ink)}
figure.diagram figcaption{margin-top:10px;color:var(--muted);font-size:.85rem;text-align:center}
@media(max-width:900px){
.bar .navtoggle{display:inline-flex}
.nav{position:absolute;top:calc(100% + 8px);right:0;left:0;z-index:40;flex-direction:column;align-items:stretch;gap:6px;padding:10px;background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:0 12px 32px -18px rgba(27,23,18,.35);max-height:0;overflow:hidden;opacity:0;pointer-events:none;transform:translateY(-6px);transition:opacity .16s,transform .16s}
.nav.open{max-height:none;overflow:visible;opacity:1;pointer-events:auto;transform:none}
.nav a{width:100%;justify-content:flex-start;font-size:.9rem;padding:11px 13px}.nav svg{width:16px;height:16px}
}
"""

# Cohesive monochrome nav icons (match the hand-authored homepage set)
NAV_ICONS = {
    "home": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.8 7.5 8 3l5.2 4.5"/><path d="M4.4 6.7v6.5h7.2V6.7"/></svg>',
    "reads": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 4C6.5 3 4 3 2.5 3.4v9.2C4 12.2 6.5 12.2 8 13.2 9.5 12.2 12 12.2 13.5 12.6V3.4C12 3 9.5 3 8 4z"/><path d="M8 4v9.2"/></svg>',
    "list": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 4.5h10M3 8h10M3 11.5h10"/></svg>',
    "guides": '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.4"/><path d="M10.6 5.4 9.1 9.1 5.4 10.6 6.9 6.9z"/></svg>',
    "model": '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="4.6" y="4.6" width="6.8" height="6.8" rx="1"/><path d="M6.6 2.4v2.2M9.4 2.4v2.2M6.6 11.4v2.2M9.4 11.4v2.2M2.4 6.6h2.2M2.4 9.4h2.2M11.4 6.6h2.2M11.4 9.4h2.2"/></svg>',
    "safety": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2.2 3 4v3.6c0 3 2.1 4.9 5 6.2 2.9-1.3 5-3.2 5-6.2V4z"/></svg>',
    "watch": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5.6 4 12 8l-6.4 4z" fill="currentColor" stroke="none"/></svg>',
    "starter": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.7 5.4 8 2.6l5.3 2.8v5.2L8 13.4 2.7 10.6z"/><path d="M2.7 5.4 8 8.2l5.3-2.8M8 8.2v5.2"/></svg>',
}
HAMBURGER = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h11"/></svg>'
MENU_JS = ('<script>(function(){var b=document.getElementById("navtoggle"),n=document.getElementById("nav");'
           'if(!b||!n)return;function s(o){n.classList.toggle("open",o);b.setAttribute("aria-expanded",o?"true":"false");}'
           'b.addEventListener("click",function(e){e.stopPropagation();s(!n.classList.contains("open"));});'
           'n.addEventListener("click",function(e){if(e.target.closest("a"))s(false);});'
           'document.addEventListener("click",function(e){if(n.classList.contains("open")&&!n.contains(e.target)&&e.target!==b)s(false);});'
           'document.addEventListener("keydown",function(e){if(e.key==="Escape")s(false);});})();</script>')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Bricolage+Grotesque:wght@500;700;800&family=IBM+Plex+Mono:wght@400;500&'
         'family=IBM+Plex+Sans:wght@400;500;600&display=swap">')

ANALYTICS = ('<script data-goatcounter="https://homeforge.goatcounter.com/count" '
             'async src="//gc.zgo.at/count.js"></script>')


def page(title, description, canonical, body, root="", jsonld="", social_image="",
         social_image_width=1122, social_image_height=1402,
         social_image_alt="HomeForge Home Assistant system diagram"):
    body = track_affiliate_clicks(body, canonical)
    desc = _html.escape(description, quote=True)
    social_meta = ""
    if social_image:
        image = _html.escape(social_image, quote=True)
        social_meta = (f'<meta property="og:image" content="{image}">\n'
                       f'<meta property="og:image:secure_url" content="{image}">\n'
                       '<meta property="og:image:type" content="image/png">\n'
                       f'<meta property="og:image:width" content="{social_image_width}">\n'
                       f'<meta property="og:image:height" content="{social_image_height}">\n'
                       f'<meta property="og:image:alt" content="{_html.escape(social_image_alt, quote=True)}">\n'
                       '<meta name="twitter:card" content="summary_large_image">\n'
                       f'<meta name="twitter:image" content="{image}">')
    if not jsonld:
        ld = {"@context": "https://schema.org", "@type": "WebPage",
              "name": title, "description": description, "url": canonical,
              "isPartOf": {"@type": "WebSite", "name": "HomeForge", "url": SITE_URL}}
        jsonld = '<script type="application/ld+json">' + json.dumps(ld) + "</script>"
    nav = (f'<a href="{root}index.html">{NAV_ICONS["home"]}Home</a>'
           f'<a href="{root}reads.html">{NAV_ICONS["reads"]}Reads</a>'
           f'<a href="{root}picks.html">{NAV_ICONS["list"]}The list</a>'
           f'<a href="{root}learn.html">{NAV_ICONS["guides"]}Guides</a>'
           f'<a href="{root}model-watch.html">{NAV_ICONS["model"]}Model Watch</a>'
           f'<a href="{root}ai-safety.html">{NAV_ICONS["safety"]}AI Safety</a>'
           f'<a href="{root}resources.html">{NAV_ICONS["watch"]}Watch &amp; build</a>'
           f'<a href="{root}starter-kit.html">{NAV_ICONS["starter"]}Starter kit</a>')
    foot = (f'<a href="{root}index.html">Home</a><a href="{root}reads.html">Reads</a><a href="{root}picks.html">The list</a>'
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
<link rel="alternate" type="application/rss+xml" title="HomeForge" href="{SITE_URL}feed.xml">
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
<header><div class="wrap bar"><a class="brand" href="{root}index.html"><span>&#9650;</span> HomeForge</a><nav class="nav" id="nav">{nav}</nav><button class="navbtn navtoggle" id="navtoggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">{HAMBURGER}</button></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">HomeForge is reader-supported; some links are affiliate links (no extra cost to you).<div class="fl">{foot}</div></div></footer>
{MENU_JS}
</body>
</html>
"""


def first_para(md):
    for block in md.split("\n\n"):
        b = block.strip()
        if (b and not b.startswith("#") and not b.startswith(">")
                and not b.startswith("*") and not re.fullmatch(r"[-_]{3,}", b)):
            clean = re.sub(r"[\[\]*_`]", "", re.sub(r"\]\(([^)]+)\)", "", b)).replace("\n", " ")
            clean = re.sub(r"\s+", " ", clean).strip()
            if len(clean) <= 155:
                return clean
            return clean[:152].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return DATA.get("tagline", "HomeForge")


def title_of(md, fallback):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return (re.sub(r"[*_`]", "", m.group(1)).strip() if m else fallback)


def newsletter_signup(source, root="../"):
    return (f'<section class="newsletter-inline" aria-labelledby="newsletter-heading">'
            '<h2 id="newsletter-heading">Get HomeForge Field Notes</h2>'
            '<p>One practical build, buying lesson, or AI workflow each week. '
            'Get the steps and checks you can use, without daily email.</p>'
            '<form action="https://buttondown.com/api/emails/embed-subscribe/homeforge" method="post">'
            '<div><label for="article-email">Email address</label>'
            '<input id="article-email" type="email" name="email" autocomplete="email" '
            'placeholder="you@example.com" required></div>'
            f'<input type="hidden" name="tag" value="{source}">'
            '<input type="hidden" name="embed" value="1">'
            '<button type="submit">Subscribe free</button></form>'
            f'<p class="small">Sent through Buttondown. Unsubscribe anytime. <a href="{root}privacy.html">Privacy</a>.</p>'
            '</section>')


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
        social_image_meta = {}
        if slug == "bambu-stratasys-verdict-what-owners-know-2026":
            social_image_meta = {
                "social_image_width": 1672,
                "social_image_height": 941,
                "social_image_alt": "Illustration of a generic enclosed 3D printer making a turquoise object",
            }
        model_watch = folder == "guides" and is_model_watch(slug)
        hub_label = "Model Watch" if model_watch else kind
        hub_url = "model-watch.html" if model_watch else "learn.html"
        if slug in AI_SAFETY_ORDER:
            hub_label, hub_url = "AI Safety", "ai-safety.html"
        # strip the leading H1 from body (we render it in .article too, keep it once)
        body = (f'<div class="article">'
                f'<p class="crumb"><a href="../index.html">HomeForge</a> / <a href="../{hub_url}">{hub_label}</a></p>'
                f'{md_to_html(md)}'
                f'{newsletter_signup("guide-reader" if folder == "guides" else "project-reader")}'
                f'<p><a href="../starter-kit.html">Read the free Starter Kit &rarr;</a></p>'
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
                 social_image=social_image, **social_image_meta), encoding="utf-8")
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


def build_ai_safety(pages):
    byslug = {p["slug"]: p for p in pages}
    cards = "".join(
        f'<a class="card" href="{byslug[s]["url"]}"><span class="tag">AI Safety</span>'
        f'<h3>{_html.escape(byslug[s]["title"])}</h3><p>{_html.escape(byslug[s]["desc"])}</p></a>'
        for s in AI_SAFETY_ORDER if s in byslug)
    body = ('<div class="article" style="max-width:none"><p class="crumb"><a href="index.html">HomeForge</a> / AI Safety</p>'
            '<span class="eyebrow">Evidence, accountability &amp; practical safeguards</span><h1>AI Safety</h1>'
            '<p class="lede">What happened, what remains uncertain, and what you can do before giving an AI more access.</p>'
            '<p>Last reviewed: September 14, 2026. This is a dated editorial collection, not a live incident monitor.</p>'
            f'<div class="cards">{cards}</div>'
            '<h2>How we cover this</h2><ul><li><strong>Documented:</strong> an original statement or identified reporting supports the event.</li>'
            '<li><strong>Attributed:</strong> a researcher or company makes a claim. We name the source; attribution is not independent proof.</li>'
            '<li><strong>Unresolved:</strong> implementation, causes, predictions or outcomes have not been established.</li></ul>'
            '<p>We distinguish an evaluation result from a real-world incident, a resignation from proof of misconduct, and a safety promise from a verified safeguard. '
            'Company statements and advocacy publications are identified as such. New evidence can change a conclusion.</p>'
            '<p>These articles contain no product recommendations or affiliate links. HomeForge has affiliate-supported content elsewhere.</p>'
            '<h2>Read the underlying evidence</h2><p><a href="https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026">International AI Safety Report 2026</a> · '
            '<a href="https://genai.owasp.org/llmrisk/llm062025-excessive-agency/">OWASP: excessive agency</a></p>'
            '<p><a href="reads.html">Browse all HomeForge reads</a></p></div>')
    (SITE / "ai-safety.html").write_text(page("AI Safety | HomeForge", "Sourced AI safety news, researcher departures, and practical safeguards for AI agents.",
        f"{SITE_URL}ai-safety.html", body, root=""), encoding="utf-8")


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


FEATURED_READS = [
    "ai-safety-deep-research-departures-risks-mitigations",
    "hugging-face-incident-2026-explained",
    "gpt-6-astra-deep-dive-2026",
    "frontier-model-comparison-september-2026",
    "esp-thermal-printer",
]

# Reads taxonomy: slug -> (section, topic tag). Unmapped pages fall back by type.
READ_SECTION_ORDER = [
    "AI Safety",
    "AI News & Analysis",
    "Maker News",
    "Model Releases & Comparisons",
    "AI Explainers",
    "Using AI",
    "Buying Guides",
    "How-To Guides",
    "Builds",
]
READ_META = {
    "ai-agent-compaction-summary-security": ("AI Safety", "Agent memory"),
    "monitor-ai-agents-with-receipts": ("AI Safety", "Agent oversight"),
    "bambu-stratasys-verdict-what-owners-know-2026": ("Maker News", "3D printing"),
    "ai-agent-memory-practical-patterns": ("Using AI", "Agent memory"),
    "ai-safety-deep-research-departures-risks-mitigations": ("AI Safety", "Deep research"),
    "ai-safety-frontier-debate-september-2026": ("AI Safety", "Current debate"),
    "ai-safety-researcher-departures-timeline": ("AI Safety", "Timeline"),
    "ai-safety-practical-agent-checklist": ("AI Safety", "Practical safeguards"),
    "hugging-face-incident-2026-explained": ("AI News & Analysis", "Security"),
    "gpt-6-astra-deep-dive-2026": ("AI News & Analysis", "OpenAI"),
    "is-gpt-6-astra-agi-2026": ("AI News & Analysis", "AGI debate"),
    "model-watch-deepseek-v4-1-flash-2026-09-14": ("Model Releases & Comparisons", "DeepSeek"),
    "deepseek-v4-1-flash-vs-open-weight-rivals-2026": ("Model Releases & Comparisons", "Open-weight"),
    "frontier-model-comparison-september-2026": ("Model Releases & Comparisons", "Frontier"),
    "frontier-model-api-pricing-comparison-2026": ("Model Releases & Comparisons", "Pricing"),
    "frontier-vs-open-weight-decision-guide-2026": ("Model Releases & Comparisons", "Decision guide"),
    "how-2026-open-weight-models-actually-work": ("AI Explainers", "Explainer"),
    "what-it-takes-to-self-host-a-2026-open-weight-model": ("AI Explainers", "Self-hosting"),
    "open-weight-ai-licenses-2026-explained": ("AI Explainers", "Licensing"),
    "managing-claude-and-chatgpt": ("Using AI", "Claude & ChatGPT"),
    "prompting-patterns": ("Using AI", "Prompting"),
    "best-way-to-run-a-local-llm": ("Using AI", "Local LLMs"),
    "best-zigbee-presence-sensors-home-assistant": ("Buying Guides", "Smart home"),
    "best-smart-plugs-home-assistant": ("Buying Guides", "Smart home"),
    "best-mini-pc-for-a-homelab": ("Buying Guides", "Homelab"),
    "best-beginner-3d-printer": ("Buying Guides", "3D printing"),
    "dry-and-store-3d-printing-filament": ("How-To Guides", "3D printing"),
    "esphome-appliance-retrofits": ("How-To Guides", "Smart home"),
    "esp-thermal-printer": ("Builds", "ESP"),
    "esp32-oled-weather-display": ("Builds", "ESP"),
    "quadra-homelab-node": ("Builds", "Homelab"),
    "flipper-and-hardware-hacking": ("Builds", "Hardware"),
    "home-assistant-backup-restore-drill": ("How-To Guides", "Smart home"),
    "is-your-smart-home-feature-local-test": ("How-To Guides", "Smart home"),
    "zigbee-thread-matter-home-assistant": ("How-To Guides", "Smart home"),
    "fix-unreliable-zigbee-network": ("How-To Guides", "Smart home"),
    "home-assistant-energy-watts-kwh": ("How-To Guides", "Smart home"),
    "docker-proxmox-bare-metal-home-server": ("How-To Guides", "Homelab"),
    "homelab-backup-restore-drill": ("How-To Guides", "Homelab"),
    "choose-nas-by-recovery-path": ("Buying Guides", "Homelab"),
    "first-functional-3d-printed-part": ("How-To Guides", "3D printing"),
    "one-charger-tech-edc-power-budget": ("Buying Guides", "Tech EDC"),
}


def _read_meta(p):
    if p["slug"] in READ_META:
        return READ_META[p["slug"]]
    if p.get("model_watch"):
        return ("Model Releases & Comparisons", MODEL_WATCH_VENDORS.get(p["slug"], "Model Watch"))
    if p["folder"] == "projects":
        return ("Builds", "Build")
    return ("How-To Guides", "Guide")


def _read_kind(p):
    if p.get("model_watch"):
        return "Analysis"
    return "Build" if p["folder"] == "projects" else "Guide"


def build_reads(guides, projects):
    """Top-level editorial hub: featured up top, then everything grouped by category with topic tags."""
    from collections import OrderedDict
    bymap = {p["slug"]: p for p in (guides + projects)}

    def card(p, feat=False):
        _, tag = _read_meta(p)
        kind = _read_kind(p)
        style = ' style="border-color:var(--accent)"' if feat else ""
        kindlabel = ("&#11088; Featured &middot; " + kind) if feat else kind
        vtag = f'<span class="tag vtag">{_html.escape(tag)}</span>' if tag else ""
        return (f'<a class="card" href="{p["url"]}"{style}><span class="tag">{kindlabel}</span>{vtag}'
                f'<h3>{_html.escape(p["title"])}</h3><p>{_html.escape(p["desc"])}</p></a>')

    featured = [bymap[s] for s in FEATURED_READS if s in bymap]
    fslugs = {p["slug"] for p in featured}

    sections = OrderedDict((s, []) for s in READ_SECTION_ORDER)
    for p in (guides + projects):
        if p["slug"] in fslugs:
            continue
        sec, _tag = _read_meta(p)
        sections.setdefault(sec, []).append(p)

    body = ['<div class="article" style="max-width:none"><p class="crumb"><a href="index.html">HomeForge</a> / Reads</p>',
            '<span class="eyebrow">Long-form &amp; analysis</span>',
            "<h1>Reads</h1>",
            '<p class="lede">The deep end of HomeForge: AI news and analysis, honest model breakdowns, buying guides, and real build write-ups — organized so you can find what you came for.</p>']
    if featured:
        body.append('<h2>Featured</h2>')
        body.append('<div class="cards">' + "".join(card(p, True) for p in featured) + "</div>")
    for sec, items in sections.items():
        if not items:
            continue
        body.append(f'<h2 style="margin-top:40px">{_html.escape(sec)}</h2>')
        body.append('<div class="cards">' + "".join(card(p) for p in items) + "</div>")
    body.append('<hr><a class="cta" href="picks.html">Browse the gear list &rarr;</a></div>')
    (SITE / "reads.html").write_text(
        page("Reads — AI analysis, model breakdowns & builds — HomeForge",
             "HomeForge's long-form: AI news and analysis, honest model breakdowns, buying guides, and real hardware build write-ups, organized by category.",
             f"{SITE_URL}reads.html", "\n".join(body), root=""), encoding="utf-8")


def build_sitemap(guides, projects):
    urls = ["", "reads.html", "picks.html", "learn.html", "model-watch.html", "ai-safety.html", "starter-kit.html", "home-assistant-first-five-automations-checklist.html", "resources.html", "privacy.html", "terms.html"]
    urls += [p["url"] for p in guides] + [p["url"] for p in projects]
    body = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        body.append(f"  <url><loc>{SITE_URL}{u}</loc></url>")
    body.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def build_feed(guides, projects):
    items = []
    for p in reversed(guides + projects):
        title = _html.escape(p["title"])
        desc = _html.escape(p["desc"])
        url = f'{SITE_URL}{p["url"]}'
        items.append(
            "    <item>\n"
            f"      <title>{title}</title>\n"
            f"      <link>{url}</link>\n"
            f"      <guid isPermaLink=\"true\">{url}</guid>\n"
            f"      <description>{desc}</description>\n"
            "    </item>"
        )
    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        "    <title>HomeForge</title>",
        f"    <link>{SITE_URL}</link>",
        "    <description>Practical smart-home, homelab, maker, and local-AI guides.</description>",
        f'    <atom:link href="{SITE_URL}feed.xml" rel="self" type="application/rss+xml" />',
        *items,
        "  </channel>",
        "</rss>",
    ]
    (SITE / "feed.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def main():
    (SITE / "hf.css").write_text(CSS, encoding="utf-8")
    guides = build_md_pages("guides", "Guides")
    projects = build_md_pages("projects", "Builds")
    model_watch = [p for p in guides if p["model_watch"]]
    learn_guides = [p for p in guides if not p["model_watch"]]
    build_picks()
    build_learn(learn_guides, projects)
    build_model_watch(model_watch)
    build_ai_safety(guides)
    build_reads(guides, projects)
    build_sitemap(guides, projects)
    build_feed(guides, projects)
    print(f"Built: reads.html, picks.html, learn.html, model-watch.html ({len(model_watch)} items), "
          f"{len(learn_guides)} guides, {len(projects)} builds, hf.css, sitemap.xml, feed.xml")


if __name__ == "__main__":
    main()
