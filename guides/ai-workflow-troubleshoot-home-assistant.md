# An AI workflow for troubleshooting Home Assistant without exposing your secrets

Home Assistant problems are easier to solve when you give an AI a clean symptom timeline, a small configuration excerpt, and evidence from the right logs. Dumping the entire installation into a chat usually adds noise and can expose information that never needed to leave your network.

This workflow prepares a focused diagnostic packet, ranks likely causes, and tests one change at a time.

## Start with a precise symptom

Replace “my automation is broken” with an observable statement:

- What should happen?
- What actually happens?
- When did it last work?
- What changed immediately before the failure?
- Is the device unavailable, or is only the automation failing?
- Can you reproduce it on demand?

Example: “The hallway light turns on from the dashboard, but the motion automation stopped triggering after I renamed the sensor entity.”

## Collect the smallest useful packet

Gather only what applies:

- The automation trace for one failed run.
- The relevant YAML or visual-editor fields.
- Exact entity IDs used by the trigger, conditions, and actions.
- The device and integration names.
- A short log excerpt around the failure time.
- The before-and-after change, if known.

Redact external URLs, location data, camera images, access tokens, webhook IDs, Wi-Fi details, and any secret stored in configuration files.

## Use a diagnostic prompt

```
Act as a careful Home Assistant troubleshooting partner.

Expected behavior:
[What should happen.]

Observed behavior:
[What happens instead.]

Recent change:
[The last relevant change, or “unknown”.]

Evidence:
<configuration>
[Relevant automation or integration excerpt.]
</configuration>
<trace_or_log>
[Small trace or log excerpt.]
</trace_or_log>

Return:
1. Facts directly supported by the evidence.
2. Up to three hypotheses ranked by likelihood.
3. The single safest next test.
4. The exact result that would confirm or reject that hypothesis.
5. Any missing information needed before suggesting a configuration change.

Do not invent entity IDs, services, integration behavior, or configuration keys.
Do not propose multiple changes at once.
```

The request for one test matters. Five simultaneous changes can make the problem disappear without telling you which change fixed it.

## Test from the bottom up

Use this order:

1. Confirm the physical device has power and network or mesh connectivity.
2. Confirm Home Assistant shows the correct entity state.
3. Trigger the device manually from Home Assistant.
4. Test the automation trigger.
5. Check conditions.
6. Test the action.
7. Run the complete automation.

If manual control fails, rewriting the automation is wasted effort. If the entity state never changes, debug the device or integration first.

## Ask for a minimal patch

Once one cause is supported, request the smallest edit:

```
Propose the minimum change that addresses the confirmed cause.
Show the original lines and replacement lines. Explain why each changed line is
necessary. Include a rollback instruction and a test procedure. Do not modify
unrelated names, formatting, or behavior.
```

Review the change before applying it. Check current Home Assistant documentation when a service, action, integration, or schema may have changed.

## Turn the fix into prevention

After it works, ask the AI to produce a five-line incident note:

- Symptom.
- Root cause.
- Evidence.
- Fix.
- Prevention.

Good prevention might be a clearer entity name, a backup before migration, a comment explaining a non-obvious condition, or an availability alert for the underlying device.

## Never paste these into a model

- Long-lived access tokens.
- `secrets.yaml` contents.
- Publicly reachable webhook URLs.
- Alarm codes, door codes, precise presence history, or camera footage.
- A full diagnostic download without reviewing and redacting it.

The goal is a repeatable troubleshooting method, not permission for the model to operate your home unsupervised.

*Related: [Best Zigbee presence sensors for Home Assistant](best-zigbee-presence-sensors-home-assistant.md) and [smart plugs for local control](best-smart-plugs-home-assistant.md).*
