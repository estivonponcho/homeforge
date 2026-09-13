# HomeForge — Handoff

_Last updated 2026-09-13. Written by Claude (Opus) for the next agent (Codex) to continue._

## What this is
HomeForge is **Mike Cage's affiliate + email monetization project**: a curated, honest directory + landing page + newsletter lead-magnet for the "self-hosted maker" audience — **smart home, homelab, 3D printing, and AI/local LLMs**. It's modeled on viral "awesome-list" affiliate repos but built as the *honest* version: real curated picks (many bench-tested from Mike's own gear), FTC affiliate disclosure, freshness from our own data file (not scraping someone else's catalog).

- **Owner:** Mike Cage. GitHub: `estivonponcho`. `gh` is authed as estivonponcho on this Mac.
- **Repo:** https://github.com/estivonponcho/homeforge (**now PUBLIC**). Local: `~/homeforge` (git, branch `main`).
- **Live site:** https://estivonponcho.github.io/homeforge/ (GitHub Pages, deploy via Actions — deploying as of handoff).
- **Credential (real, featured):** Mike holds MIT Sloan + MIT CSAIL certificate *"Artificial Intelligence: Implications for Business Strategy"* (verified in his GetSmarter account, cohort 2025-03-05). Featured accurately on the site/README as the authority anchor. Do **not** inflate to a degree.

## Architecture (how to work on it)
- **`data/picks.json`** = single source of truth (72 curated picks + author block). Edit picks here.
- **`scripts/build.py`** = regenerates `README.md` from `picks.json`. Run: `python3 scripts/build.py` after any picks change. (Python 3.)
- **`site/index.html`** = the landing page (self-contained; brand "HomeForge", ember/IBM-Plex design, theme-aware). Deployed by `.github/workflows/deploy-pages.yml`.
- **`site/privacy.html`, `site/terms.html`** = legal pages (linked in footer).
- **`guides/`** = AI content (managing Claude/ChatGPT, prompting-patterns incl. AUTOMAT, model-watch-template).
- **`projects/`** = real build write-ups (ESP thermal printer, Quadra node, Flipper+hardware-hacking, custom-apps/health).
- **`PLAYBOOK.md`** = the monetization + growth operator's manual (affiliate signup, email, SEO, realistic economics).
- **`lead-magnet/starter-kit.md`** = the free resource for email capture.
- **`.github/workflows/`** = `deploy-pages.yml` (auto-deploy site on push) + `link-check.yml` (weekly rebuild + link check).

## Automation already running
- **Weekly "model-watch" cloud routine** (Anthropic cloud): `trig_01Lezgi6qximxipFCEHfXfbH` — https://claude.ai/code/routines/trig_01Lezgi6qximxipFCEHfXfbH . Every Mon ~13:00 UTC it web-searches for notable new model releases, drafts write-ups from `guides/model-watch-template.md`, and opens a PR (falls back to printing drafts). **First run Mon 2026-09-14 — verify it can access the private→now-public repo and open a PR; if not, Mike may need to connect GitHub to Claude cloud.**

## HARD CONSTRAINTS (do not violate)
- **Never publish Mike's coursework verbatim** (MIT/community-college) — copyright + program terms. Synthesize into original writing only.
- **Never commit secrets.** (His ESP `~/Arduino/firmware_v1.ino` creds were moved to a git-ignored `secrets.h` — not in this repo. Keep it that way.)
- **No Amazon self-referral** (buying via own affiliate links violates Amazon ToS).
- **No fabricated benchmarks/prices/specs** in guides — cite sources.
- Keep health/personal data private and scrubbed.

## DONE
- Full repo scaffold, 72 curated picks, generated README, legal pages, playbook, lead magnet.
- Real repo/site URLs wired in; placeholders replaced.
- Repo made public; GitHub Pages enabled (Actions build).
- MIT Sloan+CSAIL credential featured accurately.
- Weekly model-watch routine created.

## PENDING — next steps (roughly in order)
**Autonomous (an agent can do these now):**
1. **Confirm the Pages deploy succeeded** and the live site renders (check the `deploy-pages.yml` run + load the URL).
2. **Fill legal placeholders** once Mike gives them: `[your-contact-email]` (privacy.html + terms.html) and `[your-state/country]` (terms.html).
3. **Convert `guides/` + `projects/` into individual SEO pages** on the site (currently only the README holds the full catalog). This is the #1 traffic lever. Suggested: a simple blog/section under `site/` generated from the markdown. Titles that rank, e.g. "Best Zigbee presence sensors for Home Assistant (2026)".
4. **Add a "Verify credential →" button** to the site's About card once Mike supplies the certificate's public share/verify link (see below).
5. **Custom domain wiring** if/when Mike buys one: set `site_url` + add a `CNAME` file in `site/`, update `picks.json`, rebuild.
6. **Draft the health/custom-app guide** — PENDING Mike's decision on what's shareable (he wanted this featured but health data must stay private/scrubbed).

**Only Mike can do (surface these ONE AT A TIME — he asked not to get a laundry list):**
- **Email provider:** sign up (Buttondown/Kit/Beehiiv) and paste the embed into `site/index.html` at the `<!-- EMAIL FORM -->` marker (currently a demo form).
- **Amazon Associates** application (needs live site w/ content; ⚠️ 3 qualifying sales within 180 days or account closes) + **Bambu Lab** + **Prusa** affiliate programs. Then swap tagged links into `picks.json` for every `program: Amazon/Bambu/Prusa` item and rebuild.
- **Certificate verify link:** the GetSmarter certificate email is in **mike.cage@loves.com** (NOT the connected Gmail mikeisestivonf@gmail.com), or he can use GetSmarter's "Add to LinkedIn" and share the public credential URL. Give that link to the agent to wire into the About card.
- **Enable 2FA** on his GetSmarter account (currently disabled) and confirm GitHub 2FA.
- **Distribution** (the real revenue driver): post to r/homelab, r/selfhosted, r/homeassistant, r/BambuLab, Show HN — per `PLAYBOOK.md`, respecting each community's self-promo rules.

## Working style Mike asked for
Work **autonomously** where possible; when you need him, give **one question or one task at a time** — do NOT dump a checklist on him.

## Reference (files, memory)
- Memory notes exist at `~/.claude/projects/-Users-mikecage/memory/` (`homeforge-project.md`, `mike-credentials.md`) with the same constraints.
- Realistic expectation (already told to Mike): the site can be live today, but affiliate revenue only follows real traffic, which builds over months. First dollars are small; the MIT-credential + genuine-builds angle is the differentiator.
