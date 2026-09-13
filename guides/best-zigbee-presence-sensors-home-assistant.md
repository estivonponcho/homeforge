# Best presence sensors for Home Assistant (2026)

Motion sensors turn your lights off while you're still sitting on the couch.
**Presence** sensors don't — they know you're in the room even when you're
perfectly still. If you've ever been left in the dark mid-movie, this is the
upgrade that fixes it. Here's how the real options compare.

## PIR vs mmWave — the one thing to understand first

- **PIR (passive infrared)** detects *motion* (heat moving across the sensor).
  Cheap, battery-powered, instant — but it can't tell that a still person is
  present, so it "times out" on someone sitting quietly.
- **mmWave (radar)** detects *presence* — tiny movements like breathing — so it
  holds the room "occupied" while you're still. Costs more, usually needs USB
  power, and can need a little tuning.

Most good setups use **both**: PIR for instant trigger, mmWave to hold presence.

## The picks

| Sensor | Type | Best for | Notes |
|---|---|---|---|
| **Aqara FP2** | mmWave | Whole-room + zones | Multi-zone mapping is the killer feature — "couch occupied" vs "doorway." Wi-Fi + USB power. |
| **Everything Presence Lite** | mmWave + PIR | Tinkerers who want it local | Open, ESPHome-based, fully local to Home Assistant. The enthusiast pick. |
| **Aqara Motion Sensor P1** | PIR | Cheap, instant, battery | Great trigger sensor; pair with mmWave for holding presence. Zigbee. |

## Which should you buy?

- **Just want it to work, room-wide, with zones:** the **Aqara FP2**.
- **Want it open, local, and hackable:** the **Everything Presence Lite**.
- **On a budget or need battery power:** start with a PIR like the **Aqara P1**,
  add mmWave later.

A solid first build: one PIR + one mmWave in your most-used room, with a Home
Assistant automation that turns the lights on with motion and only off when
mmWave says the room is truly empty.

See all of these in the [full smart-home list](../picks.html#smart-home).

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost
to you. We only recommend gear worth owning.*
