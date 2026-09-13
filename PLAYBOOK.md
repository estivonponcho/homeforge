# HomeForge — Monetization & Growth Playbook

This is the operator's manual: how the thing makes money, how to grow it, and
what to *not* do so you don't get an affiliate account banned or lose reader
trust. Read it once, then work the checklist at the bottom.

The model in one sentence: **publish a genuinely useful curated resource, grow
an audience around it, and earn from (a) affiliate commissions on gear people
were going to buy anyway and (b) an email list you own.** That's it. It compounds
slowly and honestly. Nobody gets rich in month one — people who stick it out for
a year build a real asset.

---

## 1. Set up your affiliate accounts

You earn nothing until these exist. Start with the two that cover most of the list.

### Amazon Associates (covers most gear)
- Sign up: <https://affiliate-program.amazon.com/>
- You get a **tracking tag** like `homeforge-20`. Every Amazon link you publish
  must carry it (`?tag=homeforge-20` or via SiteStripe).
- Easiest way to make links: browse to a product while logged in and use
  **SiteStripe** (the bar Amazon shows at the top) to grab a tagged link.
- ⚠️ **You must make 3 qualifying sales within 180 days** or the account is
  closed (you can reapply). So don't apply until the site is live and getting
  a trickle of traffic.

### Manufacturer programs (higher payouts, fewer products)
- **Bambu Lab** affiliate: search "Bambu Lab affiliate program" — covers all the
  3D-printing picks, and printer commissions dwarf Amazon's.
- **Prusa** affiliate: <https://www.prusa3d.com/> (footer → affiliate).
- **Shelly / Emporia / others**: check each brand's site footer for "affiliate"
  or "partners." Apply as you grow.

### The ones that pay nothing (and why they still matter)
Open-source software (Home Assistant, Proxmox, Immich, Jellyfin, Tailscale,
OrcaSlicer) and direct-only hardware pay $0. **Keep them anyway.** They're what
makes the list trustworthy instead of a thinly veiled Amazon dump — and trust is
what converts the links that *do* pay.

---

## 2. Turn the picks into money links

Right now every `url` in [`data/picks.json`](data/picks.json) points to an
official product page (so nothing is broken today). To monetize:

1. For each pick with `"program": "Amazon"`, replace its `url` with your
   SiteStripe-tagged Amazon link for that product.
2. For Bambu/Prusa picks, replace with your affiliate link from those programs.
3. Leave `"program": "None"` picks pointing at the official/project page.
4. Rebuild:
   ```bash
   python3 scripts/build.py
   ```
   The README and (if you wire it) the site update from the one data file.

> Keep the `program` field accurate — it's your own map of what's earning.

---

## 3. Capture emails (the asset you actually own)

Stars and affiliate clicks are rented traffic. An email list is yours forever.

1. **Pick a provider (free tiers are fine to start):**
   - [Buttondown](https://buttondown.com/) — simplest, dev-friendly, generous free tier.
   - [ConvertKit/Kit](https://kit.com/) — best automation for creators.
   - [Beehiiv](https://www.beehiiv.com/) — newsletter-native, built-in growth tools.
2. **Create the signup form**, then paste its embed into
   [`site/index.html`](site/index.html) where the `<!-- EMAIL FORM -->` comment is.
3. **Deliver the lead magnet** ([`lead-magnet/`](lead-magnet/)) as the welcome
   email or a download link on the confirmation page.
4. **Email a short, useful note every week or two** — a new pick, a teardown, a
   "here's what I'd buy this week." No blasting. Useful > frequent.

> ⚠️ **Amazon rule:** you may **not** put Amazon affiliate links in emails,
> PDFs, or anything offline — only on your website. So the lead magnet and every
> email should link to your **site pages**, which then carry the affiliate links.
> (Non-Amazon affiliate links are usually fine in email — check each program.)

---

## 4. Publish it

- **Repo:** create a public GitHub repo, push this folder. The README *is* the
  product for the GitHub audience. Set `repo` and `site_url` in `picks.json` and
  rebuild so the badges/links point at you.
- **Site:** [`site/index.html`](site/index.html) is a static page. Deploy free via:
  - **GitHub Pages** (Settings → Pages → deploy from `/site`), or
  - **Netlify / Vercel / Cloudflare Pages** (drag the `site/` folder in).
- **Domain:** buy a clean one (~$10/yr). A real domain makes affiliate programs
  and readers take you seriously. Point it at the host above.

---

## 5. Grow it (the honest version of what those posts do)

The Facebook/GitHub posts you saw work because of *distribution*, not magic. Do
the same distribution — just with a resource that's actually good.

**GitHub stars (social proof flywheel):**
- A tasteful "star this repo" line in the README is fine. Farming with a
  `FOLLOW_CREATOR.md` guilt-file is not — it reads as spam and ages badly.
- Ask in your newsletter once. Let quality do the rest.

**Communities (where your buyers already are):**
- Reddit: r/homeassistant, r/selfhosted, r/homelab, r/BambuLab, r/3Dprinting.
- **Read each sub's self-promo rules first** — most require you to be a real
  participant, not a drive-by linker. Contribute for weeks before you post the list.
- Post the *resource*, answer questions, don't lead with affiliate links.
- Also: Hacker News (Show HN), lemmy self-hosted communities, relevant Discords.

**SEO (the compounding channel):**
- Turn each category into its own page/post ("Best Zigbee presence sensors for
  Home Assistant, 2026"). That's what ranks and earns for years.
- The GitHub repo itself ranks well for "awesome X" style searches.

**Social:**
- Short, genuinely useful posts ("the $5 upgrade that fixed my stringing")
  linking back to the site. This is the honest version of the post you saw.

**What NOT to do** (kills trust or gets you banned):
- Inflating counts or faking stars/reviews.
- Hiding affiliate links or omitting disclosure.
- Spamming subreddits or DMs.
- Recommending junk because it pays more.

---

## 6. Realistic economics (so you don't quit in month two)

- Amazon pays **~1–4%** on most of these categories (electronics is low, ~1–3%;
  home goes a bit higher). Manufacturer programs pay far more per sale.
- Rough mental model: it takes **real traffic** — think thousands of visitors a
  month — before affiliate income is more than coffee money. The email list is
  what turns that traffic into something durable.
- Year one is about **content + audience**, not income. The people who win treat
  it like a garden, not a lottery ticket.

---

## 7. Maintenance cadence

- **Weekly:** send one useful email; drop one new pick or note.
- **Monthly:** re-check that your top-earning links still work and prices/products
  haven't changed; bump `updated` in `picks.json`.
- **Quarterly:** prune anything that's been surpassed. A list that's obviously
  maintained out-earns a bigger stale one.

---

## Launch checklist

- [ ] Rename the brand if you want (edit `brand`/`tagline` in `picks.json`, and
      the `<title>`/headings in `site/index.html`).
- [ ] Buy a domain and set `site_url` + `repo` in `picks.json`, then rebuild.
- [ ] Deploy `site/` to a host; confirm it's live.
- [ ] Push the repo to GitHub (public).
- [ ] Stand up an email provider; paste the embed into `site/index.html`.
- [ ] Apply to Amazon Associates (only once the site is live) + Bambu/Prusa.
- [ ] Swap tagged affiliate links into `picks.json`; rebuild.
- [ ] Confirm affiliate disclosure is visible on the site and in the README. ✅ (already is)
- [ ] Write post #1 for one community you're genuinely part of.
- [ ] Set a weekly reminder to send the email.
