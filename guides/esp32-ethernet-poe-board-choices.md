# Which ESP32 Ethernet + PoE board should you buy?

If you need an ESP32 that gets both network and power through one Ethernet cable, check the exact board variant before buying. An RJ45 jack alone does not mean the board accepts Power over Ethernet (PoE). For a budget project, the main tradeoff is the board's power isolation, not just its sticker price.

*As an Amazon Associate I earn from qualifying purchases. The Amazon link below is a paid link; buying through it may earn HomeForge a commission at no extra cost to you. These are documentation-based comparisons, not boards we tested.*

## Three practical choices

| Board | When it makes sense | Check before ordering |
|---|---|---|
| [Olimex ESP32-POE](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-EA/open-source-hardware) | A lower-cost ESP32 board with 100 Mb Ethernet and 802.3af PoE | It does **not** isolate the board from Ethernet power. Olimex says to disconnect a PoE-powered cable before programming through USB. |
| [Olimex ESP32-POE-ISO](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO-EA-16MB/open-source-hardware) | You want the Olimex design with galvanic isolation | Confirm the exact memory and antenna variant. ESPHome documents this board for an Ethernet Bluetooth proxy. |
| [Waveshare ESP32-S3-POE-ETH on Amazon](https://www.amazon.com/dp/B0DKJ5VXC9?tag=homeforge0a-20) **(paid link)** | You want an Amazon-listed ESP32-S3 board supplied with its PoE module | Select the listing's **PoE Module** version, not its board-only variant. Waveshare documents the PoE version as SKU 28771. It is a different board from the Olimex example in ESPHome's Bluetooth-proxy guide. |

The two Olimex links go to the manufacturer. At the September 23, 2026 check, we could verify the exact Waveshare board-and-module option on Amazon, but could not verify an Amazon listing for either Olimex board. We therefore do not send you to a generic Amazon search that might show a case or an Ethernet-only board instead.

## Make the decision in this order

1. **Confirm the use case.** A Bluetooth proxy, a sensor node and a camera project can need different antennas, GPIO pins, power budgets and firmware settings.
2. **Check the power path.** Make sure the package actually includes the PoE circuitry or module and that your switch or injector supplies a compatible PoE standard. A passive injector is not interchangeable with every 802.3af device.
3. **Decide whether isolation matters.** The standard Olimex ESP32-POE lacks galvanic isolation; the ISO model adds it. Follow Olimex's USB/PoE programming warning for the non-isolated board.
4. **Check the exact firmware configuration.** ESPHome's published Ethernet Bluetooth-proxy example is for the Olimex ESP32-POE-ISO. Do not paste that board configuration into a Waveshare ESP32-S3 build unchanged.
5. **Verify the listing on the day you buy.** Variant, seller, stock and price can change. The Amazon link above was checked for the Waveshare board **with** a PoE module; review that selected option at checkout.

For an ESPHome Bluetooth proxy, start with [ESPHome's official Ethernet proxy instructions](https://esphome.io/components/bluetooth_proxy/) and the [ESPHome ready-made projects page](https://esphome.io/projects/). For board details, see the [Olimex ESP32-POE specifications](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-EA/open-source-hardware), [Olimex ESP32-POE-ISO specifications](https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO-EA-16MB/open-source-hardware), and [Waveshare's variant table](https://docs.waveshare.com/ESP32-S3-ETH).
