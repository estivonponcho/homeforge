# HomeForge — Handoff

_Last updated 2026-09-13. Started by Claude and updated by Codex for the next agent to continue._

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
- **Weekly Codex newsletter-draft heartbeat:** `homeforge-weekly-newsletter-draft`. Every Wednesday at 9:00 a.m. Chicago time it inspects the repo and prepares one non-duplicate, source-grounded newsletter draft. It may commit/push when the tree is clean, but it must never schedule or send an email.

## HARD CONSTRAINTS (do not violate)
- **Never publish Mike's coursework verbatim** (MIT/community-college) — copyright + program terms. Synthesize into original writing only.
- **Never commit secrets.** (His ESP `~/Arduino/firmware_v1.ino` creds were moved to a git-ignored `secrets.h` — not in this repo. Keep it that way.)
- **No Amazon self-referral** (buying via own affiliate links violates Amazon ToS).
- **No fabricated benchmarks/prices/specs** in guides — cite sources.
- Keep health/personal data private and scrubbed.
- **Do not post HomeForge on Mike's personal Facebook page.** He explicitly declined that channel.
- **Do not launch, boost, or fund paid ads without new explicit approval at the final spend step.** Mike is interested in exploring ads but is not ready to spend tangible money.
- For Facebook distribution, research relevant groups/posts and read each group's promotion rules before drafting. Never paste the same promotion across groups.

## DONE
- Full repo scaffold, 72 curated picks, generated README, legal pages, playbook, lead magnet.
- Real repo/site URLs wired in; placeholders replaced.
- Repo made public; GitHub Pages enabled (Actions build).
- MIT Sloan+CSAIL credential featured accurately.
- Weekly model-watch routine created.
- Amazon Associates tag `homeforge0a-20` applied to all 15 Amazon links; required disclosure is live.
- Amazon Associates tax interviews show **Completed** for the United States and Canada. The account dashboard is active; the last observed report showed 0 clicks and $0 earned, so traffic is now the main revenue constraint.
- Buttondown newsletter `homeforge` is verified, branded, and connected to the homepage signup form.
- Public Starter Kit page is live at `site/starter-kit.html`.
- Four weekly newsletter drafts exist in `newsletters/` and are scheduled in Buttondown for 9:00 a.m. America/Chicago on 2026-09-20, 2026-09-27, 2026-10-04, and 2026-10-11. The Buttondown newsletter timezone is `America/Chicago`.
- Added a privacy-preserving Watch & Build resource layer based on Mike's YouTube research. Raw and unrelated history was not stored or published. The public page is `site/resources.html`; citations and editorial notes are in `resources/youtube-watchlist.md`.
- `CONTENT-STRATEGY.md` defines the watch → build → document → recommend funnel, four content clusters, a twelve-week rhythm, and the first four build concepts.
- A first original 4:5 Facebook creative and compliant launch-copy draft exist under `marketing/facebook/`. The creative is grounded in verified claims (72 picks, four pillars, free Starter Kit). **These are drafts only and must not be posted to Mike's personal profile.**
- Reddit account `u/Equal-Obligation-884` is logged in but has only 1 karma and no posts. r/homeassistant's current rules prohibit AI-generated responses and spam; do not publish AI-written material there. Mike should first participate genuinely in his own words.
- Facebook research update: Mike joined the official Home Assistant group; the Ideas/Projects group's participation request is still pending. Current group observations and newly surfaced Home Server/Homelab leads are recorded in `marketing/facebook/GROUP-RESEARCH.md`. No Facebook post has been made.

## PENDING — next steps (roughly in order)
**Autonomous (an agent can do these now):**
1. **Confirm the Pages deploy succeeded** and the live site renders (check the `deploy-pages.yml` run + load the URL).
2. **Legal placeholders are complete:** public contact is `sewer-afraid4q@icloud.com`; governing law is Illinois.
3. **Convert `guides/` + `projects/` into individual SEO pages** on the site (currently only the README holds the full catalog). This is the #1 traffic lever. Suggested: a simple blog/section under `site/` generated from the markdown. Titles that rank, e.g. "Best Zigbee presence sensors for Home Assistant (2026)".
4. **Add a "Verify credential →" button** to the site's About card once Mike supplies the certificate's public share/verify link (see below).
5. **Custom domain wiring** if/when Mike buys one: set `site_url` + add a `CNAME` file in `site/`, update `picks.json`, rebuild.
6. **Draft the health/custom-app guide** — PENDING Mike's decision on what's shareable (he wanted this featured but health data must stay private/scrubbed).
7. **Research Facebook groups and existing posts** relevant to Home Assistant, homelabs/self-hosting, functional 3D printing, and local AI. Initial read-only findings are recorded in `marketing/facebook/GROUP-RESEARCH.md`; no group was joined and nothing was posted. Continue with rules and the Proxmox/NAS/self-hosted search lane.
8. **Prepare a zero-spend Facebook distribution plan:** organic group participation, UTM-tagged HomeForge links, and a simple click/signup tracking sheet. Paid-ad exploration may include draft audiences, copy, and a hypothetical budget, but no campaign creation or spend.

**Only Mike can do (surface these ONE AT A TIME — he asked not to get a laundry list):**
- **Buttondown paid automation decision:** native welcome-email automations require the $29/month Automations add-on. Do not purchase without Mike's explicit confirmation. The Starter Kit is linked directly on the homepage as the no-cost fallback.
- **Amazon Associates** application (needs live site w/ content; ⚠️ 3 qualifying sales within 180 days or account closes) + **Bambu Lab** + **Prusa** affiliate programs. Then swap tagged links into `picks.json` for every `program: Amazon/Bambu/Prusa` item and rebuild.
- **Certificate verify link:** the GetSmarter certificate email is in **mike.cage@loves.com** (NOT the connected Gmail mikeisestivonf@gmail.com), or he can use GetSmarter's "Add to LinkedIn" and share the public credential URL. Give that link to the agent to wire into the About card.
- **Enable 2FA** on his GetSmarter account (currently disabled) and confirm GitHub 2FA.
- **Distribution** (the real revenue driver): post to r/homelab, r/selfhosted, r/homeassistant, r/BambuLab, Show HN — per `PLAYBOOK.md`, respecting each community's self-promo rules.
- **Facebook access:** Chrome recognizes the saved Mike Cage profile but was still showing the `Continue` sign-in screen. Mike may need to complete sign-in manually. Once available, inspect joined/relevant groups read-only first. Do not use his personal timeline.

## Working style Mike asked for
Work **autonomously** where possible; when you need him, give **one question or one task at a time** — do NOT dump a checklist on him.

## Reference (files, memory)
- Memory notes exist at `~/.claude/projects/-Users-mikecage/memory/` (`homeforge-project.md`, `mike-credentials.md`) with the same constraints.
- Realistic expectation (already told to Mike): the site can be live today, but affiliate revenue only follows real traffic, which builds over months. First dollars are small; the MIT-credential + genuine-builds angle is the differentiator.
