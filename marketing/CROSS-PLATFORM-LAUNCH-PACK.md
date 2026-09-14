# HomeForge cross-platform launch pack

Every draft is approval-gated. Give the full useful answer before linking. Do not reuse identical wording across communities.

## Reddit discussion seed

**Best fit:** r/homeassistant or r/homeautomation, after checking the current rules.

**Title:** Which Home Assistant automation still feels useful after the novelty wore off?

**Body:**

Mine are the boring ones: leak alerts, low-battery warnings, lights that react differently after bedtime, and appliance-finished notifications. They save time or catch a problem instead of making the house perform a trick.

What automation would you rebuild first if you had to start over?

**Link policy:** no HomeForge link in the opening post. Answer questions completely. Link the beginner guide only if someone asks for the full setup.

## Home Assistant Community project post

**Title:** A practical mixed-brand setup: local sensors, Tuya and Govee lights, and five automations worth keeping

**Opening:**

I documented the Home Assistant setup I actually use and the order I would rebuild it in. The useful pattern has been simple: sensors report, Home Assistant decides, and lights, plugs, or notifications respond. I use a mixed environment rather than replacing every working device at once.

The write-up covers the hardware roles, Zigbee versus Wi-Fi, presence versus motion, maintenance, privacy-safe screenshots, and the first five automations I recommend to beginners.

Guide: https://estivonponcho.github.io/homeforge/projects/my-practical-home-assistant-setup.html?utm_source=ha_community&utm_medium=forum&utm_campaign=practical_setup

Some hardware links on the site are affiliate links, at no extra cost to the reader.

## Pinterest set

| Pin title | Description | Destination |
|---|---|---|
| Your first 5 useful Home Assistant automations | A printable checklist for leak alerts, night lighting, doors, appliances, and bedtime scenes. | `/home-assistant-first-five-automations-checklist.html?utm_source=pinterest&utm_medium=pin&utm_campaign=ha_first_five` |
| Motion sensor vs presence sensor | See what each sensor detects and where it works best in Home Assistant. | `/guides/best-zigbee-presence-sensors-home-assistant.html?utm_source=pinterest&utm_medium=pin&utm_campaign=presence_sensors` |
| Home Assistant beginner shopping list | The hub, coordinator, sensors, plugs, and lights needed for a useful first room. | `/guides/home-assistant-beginners-guide.html?utm_source=pinterest&utm_medium=pin&utm_campaign=ha_beginner` |
| Fix wet 3D printer filament | Drying temperatures, storage habits, and the common symptoms of wet filament. | `/guides/dry-and-store-3d-printing-filament.html?utm_source=pinterest&utm_medium=pin&utm_campaign=filament` |
| Build a tiny ESP thermal printer | A practical ESP8266 project with a real parts list and build notes. | `/projects/esp-thermal-printer.html?utm_source=pinterest&utm_medium=pin&utm_campaign=thermal_printer` |

## YouTube Shorts scripts

### One room first

**Hook:** The fastest way to ruin Home Assistant is buying twenty devices before building one useful room.

**Shots:** hub, coordinator on USB extension, sensor, light, working automation.

**Voiceover:** Start with one hub, one radio, one sensor, and one light. Make motion turn the light on after sunset and vacancy turn it off. Add a physical override. Run it for a week. Then copy what worked.

**CTA:** The full beginner checklist is linked in the description.

### Motion is not presence

**Hook:** This is why your smart light turns off while you are still sitting in the room.

**Voiceover:** A PIR sensor sees warm movement. It is fast and battery-friendly, but you can disappear when you sit still. A presence sensor detects much smaller movement and is better for offices and living rooms. Use motion to turn a light on quickly, presence to keep it on, and vacancy to turn it off.

### The first safety automation

**Hook:** Your first smart-home automation should probably cost less than the damage it prevents.

**Voiceover:** Put a leak sensor by the washer, water heater, sink, or sump. When it detects moisture, send an urgent alert that names the room. Test it with a damp paper towel. It is less flashy than color-changing lights and much more useful.

## GitHub discovery

Publish small, focused resources before creating additional repositories. The first resource is `resources/home-assistant-blueprints/motion-light-with-timeout.yaml`. Link it from answers about beginner lighting automations, and link its README back to the full HomeForge guide.

## Repurposing rule

Each new canonical guide should produce one Reddit discussion, one forum version, three short-video hooks, five pin concepts, and one newsletter angle. The traffic workflow may draft these automatically, but publishing remains approval-gated.
