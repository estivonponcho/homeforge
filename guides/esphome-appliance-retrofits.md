# Make dumb (or cloud-locked) appliances local with ESPHome (2026)

A lot of "smart" appliances are really just cheap hardware chained to a vendor
cloud — they stop working when the company changes the app, and they phone home
the whole time. The fix: swap the brains for an ESP running **ESPHome**, and the
device becomes a fully local Home Assistant citizen. No cloud, no account, instant
control. Here's the approach, from easiest to most hands-on.

## Why retrofit instead of replace

- **Local control** — everything runs on your network; it works with the internet
  down and keeps working when the vendor sunsets the app.
- **No cloud, no telemetry** — the device stops reporting to anyone.
- **It's yours** — add sensors, change behavior, wire it into any automation.
- **Cheaper and greener** than throwing out working hardware.

## Easiest: a drop-in replacement board

For some popular appliances, someone has already made a plug-in ESPHome board — no
reverse-engineering required.

- **[SiloCityLabs Core300-P PCB](../picks.html#smart-home)** — a drop-in **ESP32-C6**
  controller for the **Levoit Core 300-P air purifier**. It replaces the stock board,
  runs ESPHome, and gives you local 4-speed fan control, the LED ring, filter timer,
  and child lock in Home Assistant with **no cloud**. It even exposes spare GPIO so
  you can add an air-quality or VOC sensor and have the purifier react to it.
  - Honest notes: **verify your purifier's Intertek model number first** (the cable
    isn't universal and may need soldering if it's the wrong one), and it sells out —
    check stock.

That's the whole ethos in one part: a $30 cloud gadget becomes a local, sensor-aware
HA device for the cost of a board and ten minutes with a screwdriver.

## The DIY route: ESPHome + an ESP board

For appliances without a ready-made board, you flash an ESP yourself and wire it to
the device's controls (a relay for on/off, PWM for a fan, GPIO to read buttons).

1. Grab an **[ESP32-C6 dev board](../picks.html#smart-home)** — the modern chip that
   also speaks Thread/Zigbee/Matter, so one board can even bridge protocols.
2. Flash **[ESPHome](../picks.html#-ai--local-llms)** (free) — a YAML config, no C
   required for most jobs.
3. Wire to the device's low-voltage control lines (never the mains side unless you
   know exactly what you're doing — see the warning below).
4. Add it to Home Assistant; it appears instantly with entities you define.

Great starter retrofits: a fan or lamp behind a [Shelly](../picks.html#smart-home)
or an ESP relay, a dumb humidifier, or reading a sensor the appliance already has.

## ⚠️ Safety

Mains voltage kills. For anything that plugs into the wall, either keep your
modifications on the **low-voltage control side only**, use a purpose-built module
like a **[Shelly](../picks.html#smart-home)** that's designed for it, or don't do it.
When in doubt, retrofit the control board (like the SiloCityLabs example), not the
power supply.

## Gear used

- [SiloCityLabs Core300-P PCB](../picks.html#smart-home) — the drop-in example
- [ESP32-C6 dev board](../picks.html#smart-home) — for DIY retrofits
- [Home Assistant Green](../picks.html#smart-home) to run it all locally

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost to
you. We only recommend gear worth owning.*
