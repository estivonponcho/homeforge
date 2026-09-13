# Best mini PC for a homelab (2026)

You don't need a rack and a power bill to run a homelab. A quiet little mini PC
handles Home Assistant, Proxmox, a dozen Docker containers, or a Jellyfin server
without breaking a sweat — and sips power doing it. Here's how to choose.

## What actually matters

- **x86 vs ARM.** x86 mini PCs (Intel/AMD) run everything, including apps that
  don't ship ARM builds. ARM boards (Raspberry Pi, etc.) are cheaper and lower
  power but occasionally hit "no ARM image" walls.
- **RAM over cores.** Containers and VMs eat RAM first. 16GB is a comfortable
  starting point; get a model with an accessible RAM slot so you can upgrade.
- **Power draw.** This box runs 24/7. A few watts difference is real money over a
  year — and less heat and noise.
- **Storage.** An NVMe slot beats running your OS off an SD card, which dies.

## The picks

| Box | Type | Best for |
|---|---|---|
| **Beelink Mini PC** | x86 | The default first homelab box — quiet, cheap, runs Proxmox/Docker beautifully. |
| **Minisforum Mini PC** | x86 | Step-up cores + RAM headroom when one node isn't enough. |
| **Raspberry Pi 5** | ARM | Cheapest always-on node; great with an NVMe HAT. |
| **Inovato Quadra** | ARM | Ultra-low-power utility node (DNS, VPN, monitoring) for the price of lunch. |

## Which should you buy?

- **Your first real homelab box:** a **Beelink** (x86, 16GB, NVMe). It just runs
  everything.
- **One tiny always-on job** (ad-blocking, a VPN exit, uptime monitoring): an
  **Inovato Quadra** or **Raspberry Pi 5** — a few watts, near-silent. (I run a
  Quadra for exactly this — see the [build](../projects/quadra-homelab-node.html).)
- **Outgrowing one node:** a **Minisforum** with more cores/RAM.

Browse the [full homelab list](../picks.html#homelab) for storage, networking,
and the self-hosted apps to put on it.

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost
to you. We only recommend gear worth owning.*
