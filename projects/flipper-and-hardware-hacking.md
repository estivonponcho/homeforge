# Flipper Zero & hardware hacking

*Custom firmware, a curated toolkit, and the microsoldering skills to modify
hardware at the board level. This is the "I actually open the case" end of the
hobby.*

> Ethics first: everything here is about **your own devices** — custom firmware,
> homebrew, backups, and learning how hardware works. Not piracy, not attacking
> anyone else's stuff.

---

## Flipper Zero on custom firmware

The Flipper Zero is a pocket multi-tool for RF, NFC, infrared, GPIO, and more. The
stock firmware is fine; the community firmware is where it opens up.

- **Running [Momentum](https://momentum-fw.dev/) custom firmware** (dev channel) —
  more apps, more settings, and a faster feature pace than stock.
- **Flashing safely:** update from a downloaded firmware file via qFlipper's
  *"Install from file"* rather than the one-click stock updater, so you stay on the
  firmware channel you actually chose. (A bad flash is the main way to brick one —
  do it deliberately.)
- **A curated toolkit** of community resources — the excellent
  [awesome-flipperzero](https://github.com/djsime1/awesome-flipperzero) list, an
  animation manager for custom boot/idle screens, and assorted community app packs.
  (These are community projects I use, not ones I wrote — credit to their authors.)

## Board-level modding: a Switch Lite modchip

Installing a modchip in a Nintendo Switch Lite is a genuinely advanced hardware
project, and the interesting part isn't the console — it's the **skill**:

- **Microsoldering to fine pitch points.** A patched console can't be software-only;
  it needs a small chip wired to specific test points with very fine solder work
  under magnification. This is a real, transferable electronics skill.
- **Working inside a tightly-packed device** — full teardown, ribbon cables,
  reassembly, and getting it all back together working.
- **Custom firmware / homebrew** — the same "run what you want on hardware you own"
  ethos as the Flipper and the ESP boards.

> I'm deliberately keeping the console-specific details out of this write-up. The
> showcase here is the **microsoldering and hardware-modding capability**, which is
> what's worth demonstrating.

## Why this matters for the rest of the site

The same skills show up everywhere on this list: reading a datasheet, wiring to
the right pins, not frying a 3.3V part with 5V, flashing firmware without bricking
a board. If you can modchip a handheld, an ESPHome sensor is a relaxing afternoon.

## Gear used

- Flipper Zero + [Momentum firmware](https://momentum-fw.dev/)
- A fine-tip temperature-controlled soldering iron, flux, and magnification
- [Silicone soldering mat](../README.md#-smart-home) and good tweezers
