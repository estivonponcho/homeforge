# Home Assistant for beginners: what to buy and what to automate first (2026)

Home Assistant can join devices from different brands into one useful home. You do not need to replace everything, learn YAML, or automate every room on day one. Start with one hub, one reliable radio, and one small problem worth solving.

<figure class="diagram"><img src="../assets/home-assistant-system-infographic.png" alt="Diagram showing sensors connecting to Home Assistant through Zigbee, Bluetooth, and Wi-Fi, then controlling lights, plugs, cameras, speakers, and alerts"><figcaption>Sensors report, Home Assistant decides, and devices respond.</figcaption></figure>

## The shortest good shopping list

| Buy | Why | HomeForge pick |
|---|---|---|
| Home Assistant hub | Runs the system locally | [Home Assistant Green](https://www.amazon.com/s?k=Home+Assistant+Green&tag=homeforge0a-20) |
| Zigbee coordinator | Connects low-power sensors without a vendor hub | [Home Assistant Connect ZBT-2](https://www.amazon.com/s?k=Home+Assistant+Connect+ZBT-2&tag=homeforge0a-20) |
| Contact sensor | Tells you when a door, window, or appliance opens | [Aqara Door and Window Sensor](https://www.amazon.com/s?k=Aqara+Door+Window+Sensor&tag=homeforge0a-20) |
| Motion or presence sensor | Gives the home context before it acts | [Aqara Motion Sensor P1](https://www.amazon.com/s?k=Aqara+Motion+Sensor+P1&tag=homeforge0a-20) |
| Leak sensor | Catches a high-cost problem early | [Zigbee water leak sensor](https://www.amazon.com/s?k=Zigbee+water+leak+sensor+Home+Assistant&tag=homeforge0a-20) |
| Smart plug | Makes an ordinary appliance controllable | [ThirdReality Zigbee Smart Plug](https://www.amazon.com/s?k=ThirdReality+Zigbee+smart+plug&tag=homeforge0a-20) |
| Smart light | Gives your first automation an obvious result | [Philips Hue starter kit](https://www.amazon.com/s?k=Philips+Hue+starter+kit&tag=homeforge0a-20) |

Home Assistant's current installation guide calls Green the quickest way to start. It arrives with Home Assistant OS installed and only needs power and Ethernet for setup. If you already own a Raspberry Pi 4 or 5, you can use that instead. Home Assistant recommends Home Assistant OS for most people bringing their own hardware. See the [official installation choices](https://www.home-assistant.io/installation/).

For a new Zigbee network, Home Assistant now recommends the Connect ZBT-2. Green does not include a Zigbee radio. The older ZBT-1 is discontinued but remains supported. See the [official ZHA hardware guidance](https://www.home-assistant.io/integrations/zha/).

## What each part actually does

- **Contact sensors** report open or closed. Put them on entry doors, a refrigerator, a freezer, or a mailbox.
- **PIR motion sensors** notice heat moving through a room. They are fast and battery-friendly, but they cannot reliably see a person sitting still.
- **mmWave presence sensors** detect much smaller movement. They are better at keeping lights on while someone is reading or watching TV, but usually need constant power and tuning.
- **Leak sensors** sit at floor level near a water heater, sink, washer, or sump area. Their best action is an immediate phone alert.
- **Temperature and humidity sensors** reveal comfort problems, damp basements, warm refrigerators, and storage conditions.
- **Smart plugs** switch a load and may measure energy. Mains-powered Zigbee plugs can also strengthen a Zigbee mesh.
- **Buttons** provide a physical override. A smart home should still feel easy when a phone is nowhere nearby.

## Zigbee, Bluetooth, Wi-Fi, and Matter

Use **Zigbee** for most battery sensors. It is a low-power mesh, runs locally, and gives Home Assistant a broad selection of contact, motion, leak, temperature, button, and plug devices. One Zigbee network uses one coordinator, while mains-powered Zigbee devices can route traffic for nearby battery sensors.

Use **Bluetooth** for nearby temperature and humidity sensors when the signal reaches your Home Assistant host or a Bluetooth proxy. It is inexpensive and does not require another hub.

Use **Wi-Fi** where bandwidth or a mature vendor integration matters, such as cameras, speakers, displays, and some lighting. Check whether the device still works locally if its cloud service is unavailable.

Treat **Matter** as another compatibility option, not a requirement. Buy for a tested use case and current Home Assistant support rather than the logo alone.

## Build one useful room first

1. Install the hub and complete Home Assistant onboarding.
2. Add the Zigbee coordinator on a short USB extension so it is farther from USB 3 and Wi-Fi interference.
3. Create clear areas and names before adding many devices.
4. Pair one contact sensor, one motion or presence sensor, one light, and one smart plug.
5. Build a simple automation: when motion is detected after sunset, turn on a light at a comfortable brightness.
6. Add an off condition that waits for the room to be clear.
7. Add a physical button or normal switch as an override.
8. Run it for a week before copying the pattern to another room.

## The first five automations worth building

1. **Leak alert:** leak detected, send an urgent notification and identify the affected area.
2. **Door-aware lighting:** a door opens after dark, turn on the nearby light for a short period.
3. **Presence lighting:** motion starts the light, presence keeps it on, vacancy turns it off.
4. **Appliance finished:** power draw or a dedicated sensor shows that the washer or dryer cycle ended, send a notification.
5. **Bedtime scene:** one button or NFC tag turns off common-area lights, adjusts selected devices, and confirms completion.

## Do these maintenance jobs early

- Create a low-battery notification that checks all battery sensors.
- Keep a small list of unavailable devices and fix repeat offenders before adding more.
- Schedule automatic backups and store at least one copy away from the Home Assistant device. Home Assistant recommends regular backups and keeping a copy on another system, ideally off-site. Follow the [official backup guide](https://www.home-assistant.io/common-tasks/general/#backups).
- Document what a smart plug controls before the name becomes a mystery six months later.
- Never expose entity IDs, camera feeds, precise presence history, access tokens, or home addresses in public screenshots.

## A practical upgrade path

After the first room is dependable, add safety and utility before novelty: leak sensors, freezer or refrigerator alerts, battery monitoring, appliance-finished notices, and exterior lighting. Then layer in comfort features such as sunset dimming, room presence, media controls, and dashboards.

The goal is not a house that performs tricks. It is a house that quietly removes small annoyances and catches expensive problems early.

---

*HomeForge is reader-supported. Some links are Amazon affiliate links, which means I may earn a commission from qualifying purchases at no extra cost to you. Product compatibility can change, so verify the exact model before buying.*
