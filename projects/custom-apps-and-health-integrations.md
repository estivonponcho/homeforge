# Custom apps & health integrations

*Beyond wiring boards together: building full software when the app you want
doesn't exist — including a private, self-hosted health-data hub that pulls
together device data on my own terms.*

> Privacy first, and on purpose: this write-up describes the **engineering**, never
> any personal health data. The whole point of building it myself was to keep that
> data private and off someone else's cloud — which is the same "own it, don't rent
> it" ethos as the rest of HomeForge.

---

## The capability

Most people accept whatever the manufacturer's app gives them. The more useful
move — and a real skill — is building the app *you* actually want:

- **Device & API integrations** — pulling data from health/fitness devices and
  platforms into one place instead of a dozen walled-garden apps.
- **Custom dashboards** — surfacing the metrics that matter to *you*, the way you
  want to see them.
- **Self-hosted & private** — your data lives on infrastructure you control (fits
  right alongside the [homelab](../README.md#-homelab--self-hosting) picks), not a
  vendor's servers.
- **Full-stack build** — data models, integrations, UI, and deployment, tied
  together into something you use every day.

## Why it belongs here

HomeForge is about owning your stack. Health data is the most personal data there
is — building a **private, self-hosted** place to consolidate it is the logical
extension of running your own [Immich](../README.md#-homelab--self-hosting) or
[AdGuard](../README.md#-homelab--self-hosting). Same principle: your data, your
rules.

It's also proof of range: from soldering an ESP board to shipping a full custom
application with third-party integrations.

## What I can share

The build itself stays private (as health tooling should). What's fair game for
HomeForge write-ups is the **transferable how-to**, with zero personal data:

- How to integrate device/health APIs into a custom app
- Designing a dashboard around metrics that actually matter
- Self-hosting a personal data app privately and securely

> **Decision needed:** tell me which of the above you're comfortable turning into a
> public guide (and how much of the architecture to show), and I'll draft it —
> screenshots blurred/scrubbed, no personal metrics, ever.

## Related

- [The Quadra homelab node](quadra-homelab-node.md) — the kind of box a private app like this runs on
- [Homelab & self-hosting picks](../README.md#-homelab--self-hosting)
