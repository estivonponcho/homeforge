# ESP32 + OLED weather display: build guide

A tiny always-on desk display: an ESP32 driving a 0.96" OLED that cycles through
current conditions and a 5-day forecast, dims itself at night, and draws its own
crisp weather icons. No app, no cloud dashboard — just a glanceable screen that
pulls live data over Wi-Fi. It's a great second ESP project once you've blinked an
LED, because it ties together Wi-Fi, a JSON API, NTP time, and an I2C display.

## What it shows

- **Current screen (8s):** big clock, date, location, temperature, humidity, wind,
  and a hand-drawn condition icon.
- **5 forecast cards (4s each):** hi/lo, rain chance + inches, wind, and average
  humidity per day.
- **Auto night mode:** dims and inverts between sunset and sunrise (using the
  sunrise/sunset times the weather API returns).
- **Procedural icons:** sun, moon, clouds, rain, snow, thunder, mist — drawn with
  lines and circles so they stay crisp on a 128×64 screen instead of blurry bitmaps.

## Parts

- An **ESP32 dev board** (see [ESP-WROOM-32](../picks.html#smart-home)) — Wi-Fi +
  enough power to parse JSON comfortably.
- A **0.96" SSD1306 OLED**, I2C version (4 pins) — see the
  [bench picks](../picks.html#smart-home).
- Four [jumper wires](../picks.html#smart-home).

## Wiring (I2C — four wires)

<figure class="diagram">
<svg viewBox="0 0 680 250" role="img" aria-label="ESP32 to SSD1306 OLED I2C wiring">
<rect class="box" x="30" y="55" width="180" height="150" rx="8" stroke-width="1.5"/>
<text x="120" y="45" font-size="13" text-anchor="middle">ESP32</text>
<text x="120" y="90" font-size="12" text-anchor="middle">3V3</text>
<text x="120" y="120" font-size="12" text-anchor="middle">GND</text>
<text x="120" y="150" font-size="12" text-anchor="middle">GPIO21 (SDA)</text>
<text x="120" y="180" font-size="12" text-anchor="middle">GPIO22 (SCL)</text>
<rect class="box" x="470" y="55" width="180" height="150" rx="8" stroke-width="1.5"/>
<text x="560" y="45" font-size="13" text-anchor="middle">SSD1306 OLED</text>
<text x="560" y="90" font-size="12" text-anchor="middle">VCC</text>
<text x="560" y="120" font-size="12" text-anchor="middle">GND</text>
<text x="560" y="150" font-size="12" text-anchor="middle">SDA</text>
<text x="560" y="180" font-size="12" text-anchor="middle">SCL</text>
<line class="wire" x1="210" y1="86" x2="470" y2="86" stroke-width="2"/>
<text x="340" y="80" font-size="11" text-anchor="middle">3.3V power</text>
<line class="wire" x1="210" y1="116" x2="470" y2="116" stroke-width="2"/>
<text x="340" y="110" font-size="11" text-anchor="middle">ground</text>
<line class="data" x1="210" y1="146" x2="470" y2="146" stroke-width="2.5"/>
<text x="340" y="140" font-size="11" text-anchor="middle">SDA (data)</text>
<line class="data" x1="210" y1="176" x2="470" y2="176" stroke-width="2.5"/>
<text x="340" y="170" font-size="11" text-anchor="middle">SCL (clock)</text>
<text x="340" y="222" font-size="11" text-anchor="middle">I2C address 0x3C · Wire.begin(21, 22)</text>
</svg>
<figcaption>Four wires: power, ground, and the two I2C lines. The OLED runs at 3.3V on address 0x3C.</figcaption>
</figure>

| ESP32 | OLED | Purpose |
|---|---|---|
| 3V3 | VCC | Power (3.3V) |
| GND | GND | Ground |
| GPIO21 | SDA | I2C data |
| GPIO22 | SCL | I2C clock |

## How it works

**Data:** it calls the OpenWeatherMap API twice — the *current* endpoint (every 10
min) and the *5-day/3-hour forecast* endpoint (every 30 min) — over HTTPS, then
parses the JSON with ArduinoJson. The forecast comes in 3-hour slots, so the code
buckets them into local days (hi/lo, max rain %, total precip, max wind, avg
humidity) and picks the icon nearest noon.

**Time:** it syncs with NTP and sets the timezone (`CST6CDT,...`) so the clock and
day bucketing are correct, including DST.

**Config lives in a git-ignored `secrets.h`** — Wi-Fi and the API key never sit in
the sketch:

```
#include "secrets.h"   // WIFI_SSID / WIFI_PASS / OWM_API_KEY / OWM_ZIP
const char* SSID = WIFI_SSID;
const char* PASS = WIFI_PASS;
```

**Display init** is standard SSD1306 over I2C:

```
Wire.begin(21, 22);                         // SDA=21, SCL=22
display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // most 0.96" OLEDs are 0x3C
```

**Night mode** flips the panel when the current UTC time is past sunset or before
sunrise (both returned by the API), so it isn't a glaring white square at 2am.

## ⚠️ Security note

Wi-Fi credentials, the OpenWeatherMap API key, and the ZIP are all in a
**git-ignored `secrets.h`** — never commit them. An exposed API key can be abused
against your quota, so keep it out of screenshots and public repos too.

## What I'd add next: pull room temps from Home Assistant

The natural upgrade is to add *indoor* readings next to the outdoor forecast. Home
Assistant exposes a REST API, so the ESP32 can `GET /api/states/<sensor>` for a room
temperature sensor (with a long-lived token in `secrets.h`) and show, say, "Living
room 71°F" alongside the weather. Same display code — just another data source. That
turns this from a weather clock into a whole-house glance panel.

## Gear used

- [ESP32 dev board](../picks.html#smart-home)
- 0.96" [SSD1306 OLED](../picks.html#smart-home) (I2C)
- [Jumper wires](../picks.html#smart-home)
