# Motion vs presence sensors for Home Assistant (2026)

Why do lights turn off while someone is sitting still? A PIR motion sensor
detects movement, then clears after its timeout. A mmWave sensor can detect
smaller movements and may keep an occupied room from going dark. Placement,
sensitivity, and the automation's timeout all matter.

## PIR vs mmWave — the one thing to understand first

- **PIR (passive infrared)** reacts to changes in infrared radiation as a
  person moves through its view. Battery-powered PIR sensors are useful for
  starting an automation, but may stop reporting when someone sits quietly.
- **mmWave (radar)** can detect smaller movements. It is useful for holding
  occupancy, but can report unwanted presence from nearby areas if placement
  and sensitivity are not tuned. The options below require continuous power.

You can use PIR to turn lights on and mmWave to keep them on. Test one sensor's
behavior in your room before buying a second.

## The picks

| Sensor | Sensing and connection | Best for | Check before buying |
|---|---|---|---|
| **[Aqara Presence Sensor FP2](https://www.aqara.com/us/product/presence-sensor-fp2/)** | mmWave; Wi-Fi; USB power | Room zones and multi-person tracking | Confirm the current Home Assistant integration meets your needs. It is not a Zigbee sensor. |
| **[Everything Presence Lite](https://shop.everythingsmart.io/products/everything-presence-lite)** | mmWave and ambient light; Wi-Fi/ESPHome; USB-C power | Local configuration and zone tuning | **Lite has no PIR sensor.** For one device combining PIR and mmWave, compare the manufacturer's [Everything Presence Pro](https://shop.everythingsmart.io/products/everything-presence-pro). |
| **[Aqara Motion Sensor P1](https://www.aqara.com/en/product/motion-sensor-p1)** | PIR; Zigbee 3.0; battery | Motion-triggered lights where wiring is inconvenient | It detects motion, not continuous still-person presence. Check hub compatibility. |

## A practical first-room setup

1. Identify where someone sits still and where someone enters. Check the
   sensor's field of view and a safe power location.
2. Start with a motion trigger if quick entry detection matters. If lights
   still time out during seated use, add mmWave or adjust the occupancy logic.
3. Test in the actual room: enter, sit quietly, leave, and check for false
   occupancy from adjoining spaces. Tune sensitivity and the off-delay before
   trusting an automatic lights-off rule.

This comparison uses [Aqara's FP2](https://www.aqara.com/us/product/presence-sensor-fp2/)
and [P1](https://www.aqara.com/en/product/motion-sensor-p1) product information
and the manufacturer's [Lite](https://shop.everythingsmart.io/products/everything-presence-lite)
and [Pro](https://shop.everythingsmart.io/products/everything-presence-pro)
specifications, checked September 23, 2026. It is not a hands-on test of these
four sensors.

See all of these in the [full smart-home list](../picks.html#smart-home).

---

*Some HomeForge hardware links are affiliate links; we may earn a commission
at no extra cost to you. As an Amazon Associate I earn from qualifying
purchases.*
