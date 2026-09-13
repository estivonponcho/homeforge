# Facebook value posts (drafts) — post in your own voice

**How to use these (important):**
- These are *value-first* posts, each tied to a real build — not ads. That's what
  group rules allow and what actually earns clicks.
- **Never paste the same text in two groups** (Facebook flags it as spam and it
  reads as spam to people). Each post below is written for one specific group topic.
- **Check each group's promo rules first.** Some allow a link in the post; some
  require you comment the link, or only allow links on certain days. Follow theirs.
- Post from **your account, in your voice** — tweak wording so it sounds like you.
- Post a **photo** with each one where you can (your printer, the receipt slip, the
  mini PC). Photos massively outperform text-only in groups.
- Space them out (not all in one day), and reply to comments — engagement is what
  spreads a post.

---

## 1) ESP32 / ESP8266 / microcontroller groups
**Angle: the Wi-Fi thermal-printer message board.**

> Built a little Wi-Fi "message board" on a Wemos D1 Mini this week: it hosts a web
> page on my network, you type a message, and it prints on a thermal receipt
> printer with a timestamp. The fun bug-that's-a-feature: thermal printers feed
> paper out the top, so I print the text 180°-rotated *and* reverse the line order
> — so the slip reads correctly in your hand. Happy to share the ESC/POS heat
> settings that finally gave clean black. Full write-up here if useful: [link]

Link: https://estivonponcho.github.io/homeforge/projects/esp-thermal-printer.html

---

## 2) Raspberry Pi / homelab / self-hosting groups
**Angle: a 3-watt always-on node.**

> PSA for anyone whose "server" is a noisy old tower: a lot of the useful always-on
> jobs (network-wide ad-blocking, a mesh VPN so you can reach home from anywhere,
> uptime monitoring) run happily on a tiny ARM box pulling ~3 watts. Mine runs
> AdGuard + Tailscale and I basically never think about it. Two rules I'd pass on:
> use a mesh VPN instead of opening ports, and don't do heavy writes to the eMMC.
> Wrote up the setup (secrets scrubbed): [link]

Link: https://estivonponcho.github.io/homeforge/projects/quadra-homelab-node.html

---

## 3) 3D printing groups (Makers / MakerWorld)
**Angle: the fix most beginners skip — dry filament.**

> After a lot of "why is this print stringy/brittle?" the answer was almost always
> moisture. Since I started drying filament (especially PETG) before big prints,
> the failures basically stopped. If your prints look fuzzy or snap easily, try a
> dried spool before you change anything else. I keep a short honest list of the
> gear that actually earns its place on my bench here if it helps anyone starting
> out: [link]

Link: https://estivonponcho.github.io/homeforge/picks.html#3d-printing

---

## 4) Local AI / Agentic AI groups
**Angle: the 15-minute path to a private local model.**

> If you want to run an LLM locally (no subscription, nothing leaving your machine)
> the on-ramp is way shorter than people think: install Ollama, pull a small open
> model, chat in the terminal — then add Open WebUI if you want a ChatGPT-style
> interface. The real gating factor is memory (VRAM, or unified memory on Apple
> Silicon), not the software. Wrote up the shortest path + what hardware actually
> matters: [link]

Link: https://estivonponcho.github.io/homeforge/guides/best-way-to-run-a-local-llm.html

---

## 5) Home Assistant groups
**Angle: presence vs motion (the couch problem).**

> The upgrade that fixed my "lights turn off while I'm sitting still" problem:
> swapping motion (PIR) for presence (mmWave), or better, using both — PIR for the
> instant trigger, mmWave to *hold* the room occupied while you're still. Zone
> mapping is the bonus. Quick honest comparison of the ones worth buying (and when
> a cheap PIR is still the right call): [link]

Link: https://estivonponcho.github.io/homeforge/guides/best-zigbee-presence-sensors-home-assistant.html

---

*Note: coordinate with the Facebook lane already in progress (see GROUP-RESEARCH.md)
so we don't double-post. These value posts are the follow-up to the intros already
made — space them out over the coming weeks.*
