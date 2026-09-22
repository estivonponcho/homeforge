# Fix an unreliable Zigbee network before buying more devices

Random dropouts are often blamed on the farthest sensor. Start with the coordinator, interference, and router mesh before replacing battery devices.

*Last checked September 22, 2026 · HomeForge*

## Freeze the evidence

Record which devices fail, when they fail, their power source, route if available, coordinator model and firmware, Zigbee channel, nearby Wi-Fi channel, and recent changes. Do not repair five variables at once.

## 1. Move the coordinator away from interference

Home Assistant's ZHA documentation specifically warns about USB 3.x equipment and unshielded cables interfering with low-power 2.4 GHz radios. Use a shielded USB extension cable, prefer a USB 2.0 connection when available, and move the adapter away from computers, storage devices, power supplies, and dense wiring.

Change placement first, then observe the same failing devices for a defined period.

## 2. Map the mesh

Zigbee networks have one coordinator. Mains-powered devices commonly act as routers; battery devices are usually end devices. Add routers where coverage is weak, starting near the coordinator and extending outward.

Do not assume every powered product routes well or supports every end device. Record the exact model and observe the resulting topology.

## 3. Check channel overlap

Zigbee and 2.4 GHz Wi-Fi share spectrum. Record both channel plans before changing them. A channel migration can require devices to reconnect and should be treated as a controlled maintenance event with a backup and rollback plan.

## 4. Separate pairing from steady-state placement

Pair according to the integration and manufacturer guidance. Then place the device where it will operate and confirm it stays connected through the intended routers. A successful pairing next to the coordinator does not prove the final path is reliable.

## 5. Check firmware cautiously

Update the coordinator with the manufacturer's supported process when outdated firmware is a plausible cause. Device OTA updates can change or break features; Home Assistant warns that some updates may require reconfiguration or can rarely brick a device. Read device-specific reports before updating.

## Change log

| Time | Change | Devices observed | Dropouts | Rollback needed |
|---|---|---:|---:|---|
| Baseline | None |  |  |  |
| Test 1 | Coordinator placement |  |  |  |
| Test 2 | Added router |  |  |  |
| Test 3 | Channel plan |  |  |  |

Stop when the evidence improves. More repeaters and more channel changes are not automatically better.

## Source

- [Home Assistant ZHA troubleshooting and interference guidance](https://www.home-assistant.io/integrations/zha)

