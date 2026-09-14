# Best smart plugs for Home Assistant, no Wi-Fi or Z-Wave (2026)

If you're asking for smart plugs that *aren't* Wi-Fi or Z-Wave, you want **Zigbee**
or **Thread/Matter** — local, no cloud account, and they don't clog your Wi-Fi.
Here's the honest shortlist for Home Assistant.

## Why skip Wi-Fi (and Z-Wave)

- **Wi-Fi plugs** each take an IP, often phone home to a vendor cloud, and a dozen
  of them add real congestion. Great until the company sunsets the app.
- **Z-Wave** is fine but pricier, and you're clearly ruling it out.
- **Zigbee / Thread** are low-power mesh radios: plugs join a local coordinator,
  respond instantly, keep working with no internet, and **mains-powered plugs even
  repeat the mesh** to extend range for your battery sensors.

## Zigbee — the widest, cheapest selection

Pair these with a Zigbee coordinator (a [Sonoff or HA Connect ZBT-1
stick](../picks.html#smart-home)) running ZHA or Zigbee2MQTT.

- **[ThirdReality Zigbee Smart Plug](../picks.html#smart-home)** — the value pick.
  Power monitoring, cheap enough to buy a ten-pack, and it repeats the mesh.
- **[Aqara Smart Plug](../picks.html#smart-home)** — energy monitoring + a solid
  Zigbee router. A favorite for reliability in HA.
- **[Sonoff S60 Zigbee](../picks.html#smart-home)** — cheap, reliable, pairs
  instantly. A safe default.

## Thread / Matter — the future, with a caveat

Here's the honest part: **most plugs marketed as "Matter" are Matter-over-Wi-Fi**,
which… still uses Wi-Fi. If you truly want no Wi-Fi, you want **Matter-over-Thread**:

- **[Eve Energy (Thread + Matter)](../picks.html#smart-home)** — genuine Thread,
  energy monitoring, no cloud and no Wi-Fi. Needs a Thread border router (a recent
  Apple TV/HomePod, or an [HA Connect ZBT-1](../picks.html#smart-home) running
  Thread). Pricier, but the cleanest local Matter plug today.

## Quick comparison

| Plug | Radio | Power monitoring | Repeats mesh | Best for |
|---|---|---|---|---|
| ThirdReality | Zigbee | Yes | Yes | Value / buying in bulk |
| Aqara Smart Plug | Zigbee | Yes | Yes | Reliability + range |
| Sonoff S60 | Zigbee | Yes | Yes | Cheapest safe default |
| Eve Energy | Thread/Matter | Yes | Yes (Thread) | Future-proof, no Wi-Fi |

## The verdict

- **Just want it to work, cheap, today:** go **Zigbee** — start with **ThirdReality**
  or **Aqara**.
- **Want to lean into Matter without Wi-Fi:** **Eve Energy** on Thread, if you have
  a border router.

Either way you get local control, instant response, and no vendor cloud — exactly
what Home Assistant is for.

See the full [smart-home list](../picks.html#smart-home) for coordinators, sensors,
and the rest of a local-first setup.

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost to
you. We only recommend gear worth owning.*
