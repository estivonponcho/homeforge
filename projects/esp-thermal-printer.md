# Wi-Fi Thermal Receipt Printer "Message Board"

*An ESP8266 that hosts a little web page on your network; type a message, hit
send, and it prints on a thermal receipt printer — timestamped, word-wrapped, and
oriented so it reads correctly as the paper feeds out.*

> Inspired by the thermal-printer message-board concept popularized by Peter /
> Urban Circles. This is my own firmware build of the idea.

---

## What it does

- Runs a **web server on a WeMos D1 Mini (ESP8266)** — open its address on your
  phone and you get a clean "Leave a Message" page (Tailwind UI, a character
  counter, and a confetti burst on send).
- On submit, the board **prints the message on a thermal receipt printer** over a
  serial connection, stamped with the current date from an **NTP time server**.
- It's a fun, physical little inbox — leave notes for the household, print
  reminders, or wire it to anything that can hit a URL.

## The parts that were actually interesting

**Printing upside-down, on purpose.** Thermal printers feed paper out the top, so
a normally-printed receipt comes out reading bottom-to-top. The firmware enables
the printer's 180° rotation mode *and* prints the wrapped lines in reverse order,
so the finished slip reads top-to-bottom in your hand. Two bugs that cancel out by
design.

**Word-wrap at 32 characters.** The printer is 32 chars wide, so the firmware
wraps on the last space before the limit rather than mid-word — small touch, big
difference in readability.

**Tuning the burn.** Thermal print quality is all in the heat settings (heating
dots / time / interval via ESC/POS commands). Getting a crisp black without
scorching or ghosting took a few passes.

**NTP + custom dates.** Pulls real time from `pool.ntp.org`, and also accepts a
custom date through the form for backdated slips.

## What I'd change next

- Move Wi-Fi credentials out of the sketch into an untracked `secrets.h`
  (**never commit credentials** — see the security note below).
- Add a small OLED for status, and a physical "print" button.
- Expose it to Home Assistant so automations can print (e.g., "print the day's
  calendar at 7am").

## ⚠️ Security note

The original sketch hardcodes the Wi-Fi SSID and password in plaintext. Before
this (or any Arduino sketch) goes near a public repo, pull secrets into a separate
file and add it to `.gitignore`:

```cpp
// secrets.h  (git-ignored)
#define WIFI_SSID     "your-ssid"
#define WIFI_PASSWORD "your-password"
```

## Gear used

- [WeMos D1 Mini (ESP8266)](../README.md#-smart-home) — the board it runs on
- A 58mm thermal receipt printer (serial / TTL)
- [Dupont jumper wires](../README.md#-smart-home) and a
  [breadboard](../README.md#-smart-home) for prototyping
- [Silicone soldering mat](../README.md#-smart-home) for the final wiring

*Full source lives in my Arduino sketches (credentials scrubbed before publishing).*
