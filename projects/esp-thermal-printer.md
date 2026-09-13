# Wi-Fi thermal receipt printer: a full build guide

An ESP8266 that hosts a little web page on your network. Open it on your phone,
type a message, hit send — and it prints on a thermal receipt printer,
timestamped and correctly oriented as the paper feeds out. It's a genuinely fun
first "it does a physical thing over Wi-Fi" project, and it teaches web serving,
serial, and ESC/POS printer control in one go.

> Inspired by the thermal-printer message-board concept popularized by Peter /
> Urban Circles. This is my own firmware build of the idea, written up so you can
> make your own.

## How it works, end to end

<figure class="diagram">
<svg viewBox="0 0 720 130" role="img" aria-label="Data flow from phone to printed slip">
<rect class="box" x="8" y="36" width="140" height="58" rx="8" stroke-width="1.5"/>
<text x="78" y="60" font-size="13" text-anchor="middle">Your phone</text>
<text x="78" y="78" font-size="12" text-anchor="middle">(web form)</text>
<rect class="box" x="196" y="36" width="140" height="58" rx="8" stroke-width="1.5"/>
<text x="266" y="60" font-size="13" text-anchor="middle">D1 Mini</text>
<text x="266" y="78" font-size="12" text-anchor="middle">web server</text>
<rect class="box" x="384" y="36" width="140" height="58" rx="8" stroke-width="1.5"/>
<text x="454" y="60" font-size="13" text-anchor="middle">Thermal</text>
<text x="454" y="78" font-size="12" text-anchor="middle">printer</text>
<rect class="box" x="572" y="36" width="140" height="58" rx="8" stroke-width="1.5"/>
<text x="642" y="60" font-size="13" text-anchor="middle">Printed</text>
<text x="642" y="78" font-size="12" text-anchor="middle">slip</text>
<line class="wire" x1="150" y1="65" x2="192" y2="65" stroke-width="2"/>
<polygon points="192,65 184,61 184,69" style="fill:var(--ink)"/>
<text x="171" y="52" font-size="11" text-anchor="middle">Wi-Fi</text>
<line class="data" x1="338" y1="65" x2="380" y2="65" stroke-width="2.5"/>
<polygon points="380,65 372,61 372,69" style="fill:var(--accent)"/>
<text x="360" y="52" font-size="11" text-anchor="middle">TX D8</text>
<line class="wire" x1="526" y1="65" x2="568" y2="65" stroke-width="2"/>
<polygon points="568,65 560,61 560,69" style="fill:var(--ink)"/>
<text x="548" y="52" font-size="11" text-anchor="middle">paper</text>
</svg>
<figcaption>Phone → the ESP's web form → serial (TX pin D8) → the printer → a slip you can hold.</figcaption>
</figure>

## Parts you need

- A **[WeMos D1 Mini (ESP8266)](../picks.html#smart-home)** — the microcontroller.
- A **58mm thermal receipt printer** with a TTL serial input (the small embeddable
  kind, not a USB desktop printer).
- An **external 5–9V power supply** rated for **2A or more** — thermal printers
  pull a lot of current when the head fires.
- A roll of **58mm thermal paper**, plus [jumper wires](../picks.html#smart-home)
  and a [breadboard](../picks.html#smart-home) to prototype.

## Wiring

The one thing beginners get wrong: **do not power the printer from the D1 Mini.**
The print head can draw an amp or more in bursts — that will brown out the ESP and
cause resets or garbage prints. Give the printer its own supply and just share a
common ground.

<figure class="diagram">
<svg viewBox="0 0 720 300" role="img" aria-label="Wiring diagram">
<rect class="box" x="30" y="110" width="170" height="80" rx="8" stroke-width="1.5"/>
<text x="115" y="145" font-size="14" text-anchor="middle">Wemos D1 Mini</text>
<text x="115" y="165" font-size="12" text-anchor="middle">(ESP8266)</text>
<rect class="box" x="520" y="70" width="170" height="80" rx="8" stroke-width="1.5"/>
<text x="605" y="105" font-size="14" text-anchor="middle">Thermal printer</text>
<text x="605" y="125" font-size="12" text-anchor="middle">(TTL serial)</text>
<rect class="box" x="270" y="228" width="190" height="55" rx="8" stroke-width="1.5"/>
<text x="365" y="251" font-size="13" text-anchor="middle">External 5–9V PSU</text>
<text x="365" y="268" font-size="12" text-anchor="middle">(2A or more)</text>
<line class="data" x1="200" y1="138" x2="520" y2="100" stroke-width="2.5"/>
<text x="360" y="104" font-size="12" text-anchor="middle">D8 (TX) → RX · 9600 baud</text>
<line class="wire" x1="400" y1="228" x2="545" y2="150" stroke-width="2"/>
<text x="500" y="205" font-size="12" text-anchor="middle">power → VIN</text>
<polyline class="wire" points="115,190 115,285 605,285 605,150" fill="none" stroke-width="1.6" stroke-dasharray="5 4"/>
<line class="wire" x1="365" y1="283" x2="365" y2="285" stroke-width="1.6"/>
<text x="360" y="299" font-size="12" text-anchor="middle">common ground — tie every GND together</text>
</svg>
<figcaption>Data on one wire, power on another, and a shared ground. That's the whole circuit.</figcaption>
</figure>

The exact connections:

| From (D1 Mini) | To (thermal printer) | Why |
|---|---|---|
| D8 (TX) | RX / DIN | Serial data at 9600 baud |
| GND | GND | Signals need a shared reference — required |
| — | VIN | Printer power, from the external PSU (not the D1 Mini) |
| 5V / USB | — | Powers the D1 Mini itself |
| GND | PSU (−) | Tie the PSU ground to the common ground too |

> Most 58mm TTL printers accept 3.3V logic on RX, so the D1 Mini's TX drives them
> directly. If yours is finicky, add a [logic level
> converter](../picks.html#smart-home) between D8 and RX.

## The firmware, in the parts that matter

**Connect to Wi-Fi from a git-ignored secrets file** (never hardcode credentials —
see the security note below):

```
#include "secrets.h"      // WIFI_SSID / WIFI_PASSWORD live here, git-ignored
const char* ssid     = WIFI_SSID;
const char* password = WIFI_PASSWORD;
```

**Talk to the printer over SoftwareSerial** on D8, TX-only, at 9600 baud, and send
the ESC/POS init + heat settings. Print quality is almost entirely in the heat
values — too low is faint, too high ghosts and scorches:

```
SoftwareSerial printer(D8, -1);   // D8 = TX, no RX pin
printer.begin(9600);
printer.write(0x1B); printer.write('@');   // ESC @  — reset
printer.write(0x1B); printer.write('7');   // ESC 7  — heating config
printer.write(15);                          // heating dots (max 15)
printer.write(150);                         // heating time
printer.write(250);                         // heating interval
```

**The fun bug-that's-a-feature — printing upside down.** Thermal printers feed
paper out the top, so a normally-printed receipt reads bottom-to-top in your hand.
The fix is two wrongs making a right: enable the printer's 180° rotation *and*
print the wrapped lines in reverse order, so the finished slip reads top-to-bottom:

```
printer.write(0x1B); printer.write('{'); printer.write(0x01);  // ESC { 1 — rotate 180°
// ...then emit the word-wrapped lines last-to-first:
for (int i = lineCount - 1; i >= 0; i--) printLine(lines[i]);
```

The ESP also runs a tiny web server that serves the "Leave a Message" form and, on
submit, hands the text to the printer with an NTP timestamp.

## Troubleshooting

- **Garbage characters / resets:** power problem. Give the printer its own 2A+
  supply and check the common ground.
- **Faint or scorched print:** tune the three heat values above.
- **Nothing prints:** wrong baud (try 19200) or TX/RX swapped.
- **Text reads bottom-to-top:** you have the rotation but not the reversed line
  order (or vice-versa) — you need both.

## What I'd add next

- A small [OLED](../picks.html#smart-home) for status and the current IP.
- A Home Assistant hook so automations can print (e.g. the day's calendar at 7am).

## ⚠️ Security note

The sketch reads Wi-Fi credentials from a **git-ignored `secrets.h`** — never
commit them:

```
// secrets.h  (add to .gitignore)
#define WIFI_SSID     "your-ssid"
#define WIFI_PASSWORD "your-password"
```

## Gear used

- [WeMos D1 Mini (ESP8266)](../picks.html#smart-home)
- A 58mm TTL thermal receipt printer + external 5–9V/2A supply
- [Jumper wires](../picks.html#smart-home), a [breadboard](../picks.html#smart-home), and a [soldering mat](../picks.html#smart-home) for the final build
