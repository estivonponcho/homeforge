# Is that smart-home feature actually local? Run five tests

“Works with Home Assistant” does not tell you whether discovery, control, history, automations, or account recovery depend on a vendor cloud. Test the behavior you care about before buying ten more devices.

*Last checked September 22, 2026 · HomeForge*

Use a non-critical device and a reversible test. Do not disconnect safety equipment, medical devices, locks, alarms, heating, or anything whose failure could harm someone.

## Define the feature

Test a specific outcome, such as “the wall button turns on the lamp and Home Assistant records the new state.” A device can expose basic local control while advanced scenes, firmware, history, or voice features remain cloud-dependent.

Record the integration name, device model, firmware, Home Assistant version, and control path before changing anything.

## Test 1: internet unavailable

Temporarily block only the test device or test network from reaching the internet. Keep local networking available. Trigger the feature from Home Assistant and from its physical control.

Record command success, state feedback, latency, and any missing feature. A phone app working over cellular is not proof of local control.

## Test 2: vendor app signed out

Sign out of the vendor app on a test device or use a separate browser profile. Confirm whether the Home Assistant integration continues operating. Do not remove the vendor account or factory-reset the device during this test.

## Test 3: Home Assistant restart

Restart Home Assistant during a safe maintenance window, then repeat the test. Check whether credentials, entity identifiers, and automations recover without manual repair.

## Test 4: device or hub restart

Power-cycle only the non-critical test device or its local bridge. Confirm reconnection time and whether state is accurate after it returns. Avoid repeated power cycling of devices not designed for it.

## Test 5: automation receipt

Run one harmless automation and save the trace or log. Verify the trigger, action, device response, and final state. A command being sent is different from the result being observed.

## Score the control path

| Capability | Local | Cloud-dependent | Unknown |
|---|---:|---:|---:|
| Physical control |  |  |  |
| Home Assistant command |  |  |  |
| State feedback |  |  |  |
| Automation after restart |  |  |  |
| History and energy data |  |  |  |
| Setup and account recovery |  |  |  |
| Firmware updates |  |  |  |

“Local” is not one badge. Publish the result by feature and tested version. Repeat the test after a major firmware or integration change.

Continue with [Home Assistant for beginners](home-assistant-beginners-guide.html) or the [ESPHome appliance retrofit guide](esphome-appliance-retrofits.html).

## Sources

- [Home Assistant integrations](https://www.home-assistant.io/integrations/)
- [Home Assistant automation traces](https://www.home-assistant.io/docs/automation/troubleshooting/)

