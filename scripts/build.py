#!/usr/bin/env python3
"""Generate README.md from data/picks.json.

This is the honest version of "auto-updating": the catalog is regenerated from
your own curated data file, so the repo stays consistent and you can add a pick
in one place. It does NOT scrape anyone else's catalog.

Usage:
    python3 scripts/build.py
"""
import json
import pathlib
import sys
from urllib.parse import quote_plus
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "picks.json"
OUT = ROOT / "README.md"


def slug(text: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in text]
    s = "".join(keep)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


def public_url(item: dict) -> str:
    """Use a tagged Amazon discovery link for picks marked Amazon."""
    url = item["url"]
    if "Amazon" in item.get("program", "") and "amazon.com" not in url:
        return f"https://www.amazon.com/s?k={quote_plus(item['name'])}&tag=homeforge0a-20"
    return url


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    brand = data["brand"]
    repo = data.get("repo", "YOUR-GH-USERNAME/homeforge")
    picks = data["picks"]

    # Group picks: pillar -> category -> [items], preserving first-seen order.
    by_pillar = OrderedDict()
    for p in data["pillars"]:
        by_pillar[p["id"]] = OrderedDict()
    for item in picks:
        cats = by_pillar.setdefault(item["pillar"], OrderedDict())
        cats.setdefault(item["category"], []).append(item)

    pillar_meta = {p["id"]: p for p in data["pillars"]}
    total = len(picks)

    L = []
    a = L.append

    # ---- Header --------------------------------------------------------
    a(f"# {' '.join(p['emoji'] for p in data['pillars'])} {brand}")
    a("")
    a(f"> {data['tagline']}")
    a("")
    a(f"![Stars](https://img.shields.io/github/stars/{repo}?style=flat-square) "
      f"![License](https://img.shields.io/badge/list-CC--BY--4.0-blue?style=flat-square) "
      f"![Picks](https://img.shields.io/badge/curated%20picks-{total}-brightgreen?style=flat-square) "
      f"![Updated](https://img.shields.io/badge/updated-{data['updated'].replace('-', '--')}-informational?style=flat-square)")
    a("")
    a(data["intro"])
    a("")
    a("**Why trust this list?** It's short on purpose. Every pick is something "
      "worth owning, with an honest take on *why* and *when*. No auto-scraped "
      "listings, no padded counts. If something's here, it earned the slot.")
    a("")
    a(f"\U0001f4ec **Get the free [Self-Hosted Home Starter Kit]({data.get('site_url','#')})** "
      "— a one-page buyer's guide + wiring checklist, no fluff. (Link goes to the signup page.)")
    a("")
    a(f"▶ **[Watch & Build]({data.get('site_url','#').rstrip('/')}/resources.html)** "
      "— a curated video list for each HomeForge pillar, with a concrete project after every three videos.")
    a("")

    # ---- Table of contents --------------------------------------------
    a("## Contents")
    a("")
    for pid, cats in by_pillar.items():
        pm = pillar_meta[pid]
        a(f"- [{pm['emoji']} {pm['title']}](#{slug(pm['title'])})")
        for cat in cats:
            a(f"  - [{cat}](#{slug(cat)})")
    a("- [How this list makes money (and stays honest)](#how-this-list-makes-money-and-stays-honest)")
    a("- [Contributing](#contributing)")
    a("")

    # ---- Pillars -------------------------------------------------------
    for pid, cats in by_pillar.items():
        pm = pillar_meta[pid]
        a(f"## {pm['emoji']} {pm['title']}")
        a("")
        a(f"_{pm['blurb']}_")
        a("")
        for cat, items in cats.items():
            a(f"### {cat}")
            a("")
            for it in items:
                star = " ⭐" if it.get("featured") else ""
                tier = it.get("tier", "")
                tier_str = f" _( {tier} )_" if tier else ""
                a(f"- **[{it['name']}]({public_url(it)})**{star} — {it['blurb']}{tier_str}")
            a("")

    # ---- Monetization / honesty note ----------------------------------
    a("## How this list makes money (and stays honest)")
    a("")
    a("Some links are affiliate links: if you buy through them, this project "
      "may earn a small commission at no extra cost to you. That's it — that's "
      "the whole business model. See [AFFILIATE-DISCLOSURE.md](AFFILIATE-DISCLOSURE.md).")
    a("")
    a("What this project will **never** do:")
    a("")
    a("- Recommend something bad because it pays better.")
    a("- Pad the list with junk to inflate a count.")
    a("- Hide that a link is an affiliate link.")
    a("")

    # ---- About the curator --------------------------------------------
    author = data.get("author")
    if author:
        a("## Who curates this")
        a("")
        a(author.get("bio", ""))
        if author.get("credential"):
            a("")
            a(f"**Credential:** {author['credential']}")
        a("")

    # ---- Contributing --------------------------------------------------
    a("## Contributing")
    a("")
    a("Got a pick that genuinely belongs here? Open an issue or PR — see "
      "[CONTRIBUTING.md](CONTRIBUTING.md). Picks live in "
      "[`data/picks.json`](data/picks.json); this README is generated from it "
      "by [`scripts/build.py`](scripts/build.py), so edit the data, not the README.")
    a("")
    a("---")
    a("")
    a(f"_Last updated {data['updated']}. Curated by a human who runs this stuff._")
    a("")

    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {OUT} — {total} picks across {len(by_pillar)} pillars.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
