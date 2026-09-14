# Facebook value posts (drafts) — post in your own voice

**How to use these (important):**
- These are *value-first* posts, each tied to a real build — not ads. That's what
  group rules allow and what actually earns clicks.
- **Never paste the same text in two groups** (Facebook flags it as spam). Each
  post below is written for one specific group topic.
- **Every post ends by asking the group for feedback / what they'd improve.** This
  is the single best engagement move: people love to critique and help, it invites
  comments (which spread the post), and it genuinely makes the next build better.
- **Check each group's promo rules first.** Some allow a link in the post; some
  want the link in a comment. Follow theirs.
- Post from **your account, in your voice** — tweak wording so it sounds like you.
- Post a **photo** with each one where you can. Photos massively outperform text.
- Space them out (not all in one day), and reply to every comment.

---

## 1) ESP32 / ESP8266 / microcontroller groups — ✅ POSTED
Posted 2026-09-13 to **ESP32/ESP8266 projects** (fb.com/groups/754518470444906). LIVE.
_Follow-up idea: add a comment asking "what would you change — better printer,
level-shifting, deep-sleep?" to pull in improvement replies._

> Built a little Wi-Fi "message board" on a Wemos D1 Mini: it hosts a web page on
> my network, you type a message, and it prints on a thermal receipt printer with a
> timestamp. Fun bug-that's-a-feature: printers feed paper out the top, so I print
> 180°-rotated *and* reverse the line order — so the slip reads right in your hand.
> Full build (wiring diagram + the ESC/POS heat settings that finally gave clean
> black): [link]
> **What would you have done differently? Better printer, level-shifting, deep-sleep
> to run it on battery? I'd love to make v2 better.**

Link: https://estivonponcho.github.io/homeforge/projects/esp-thermal-printer.html

---

## 2) Raspberry Pi / homelab / self-hosting groups
**Angle: a 3-watt always-on node.**

> PSA for anyone whose "server" is a noisy old tower: a lot of useful always-on jobs
> (network-wide ad-blocking, a mesh VPN to reach home from anywhere, uptime
> monitoring) run happily on a tiny ARM box pulling ~3 watts. Mine runs AdGuard +
> Tailscale and I never think about it. Two lessons: use a mesh VPN instead of
> opening ports, and don't hammer the eMMC with writes. Wrote it up (secrets
> scrubbed): [link]
> **What else would you run on a 3W box — and has anyone found a cleaner fix for
> eMMC/SD wear? Keen to improve the setup.**

Link: https://estivonponcho.github.io/homeforge/projects/quadra-homelab-node.html

---

## 3) 3D printing groups (Makers / MakerWorld) — ⏭️ NEXT UP (intro already live in 3D Printing Makers Group)
**Angle: the fix most beginners skip — dry filament.**

> After a lot of "why is this stringy/brittle?", the answer was almost always
> moisture. Since I started drying filament (especially PETG) before big prints, the
> failures basically stopped. If your prints look fuzzy or snap easily, try a dried
> spool before changing anything else. I keep a short, honest list of the bench gear
> that actually earns its place here: [link]
> **What's your go-to drying setup — temp and time by material? Always trying to
> dial mine in, so tell me what I'm getting wrong.**

Link: https://estivonponcho.github.io/homeforge/picks.html#3d-printing

---

## 4) Local AI / Agentic AI groups — ready (intro already live in Agentic AI)
**Angle: the 15-minute path to a private local model.**

> Running an LLM locally (no subscription, nothing leaving your machine) is a shorter
> on-ramp than people think: install Ollama, pull a small open model, chat in the
> terminal — then add Open WebUI for a ChatGPT-style interface. The real gating
> factor is memory (VRAM, or unified memory on Apple Silicon), not the software.
> Wrote up the shortest path + what hardware matters: [link]
> **What model + hardware combo is actually working for you locally? Trying to land
> on a good default recommendation — tell me what beats mine.**

Link: https://estivonponcho.github.io/homeforge/guides/best-way-to-run-a-local-llm.html

---

## 5) Home Assistant groups
**Angle: presence vs motion (the couch problem).**

> The upgrade that fixed my "lights turn off while I'm sitting still" problem:
> swapping motion (PIR) for presence (mmWave), or better, using both — PIR for the
> instant trigger, mmWave to *hold* the room occupied while you're still. Quick
> honest comparison of the ones worth buying (and when a cheap PIR still wins): [link]
> **Which presence sensor has held up best for you long-term? Curious what's been
> reliable vs. flaky before I recommend a default.**

Link: https://estivonponcho.github.io/homeforge/guides/best-zigbee-presence-sensors-home-assistant.html

---

## Queued future build (needs a write-up first)
- **ESP32 + OLED weather display** (`~/Documents/Arduino/Weather/Weather.ino`) —
  great fit for BOTH the ESP32 group and Home Assistant groups. Needs: confirm the
  Home-Assistant room-temp version (the found sketch pulls OpenWeatherMap, not HA),
  scrub hardcoded secrets (Wi-Fi pass + API key + ZIP), then a build page like the
  thermal printer. Then it becomes posts #6/#7.

---

*Coordinate with the Facebook lane in GROUP-RESEARCH.md so we don't double-post.
These are follow-ups to the intros already made — space them out over the weeks.*
