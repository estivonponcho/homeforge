# The Quadra: a 3-watt homelab node

*How a sub-$100 ARM box earns its keep as an always-on utility node — doing real
work on a private mesh network while sipping about as much power as a phone
charger.*

> Scrubbed for publication: no IP addresses, keys, ports, or hostnames. If you
> build one, keep yours off the public internet too.

---

## The idea

Not every homelab job needs a power-hungry server. A huge amount of useful
always-on work — DNS, ad-blocking, monitoring, a VPN exit — is happy on a tiny,
cheap, low-power ARM box. The [Inovato Quadra](../README.md#-homelab--self-hosting)
is one of the best value entries into that: an inexpensive ARM mini-PC that idles
at just a few watts, so leaving it on 24/7 costs almost nothing.

## What it runs

- **Network-wide DNS ad-blocking** with [AdGuard Home](../README.md#-homelab--self-hosting) —
  point your network's DNS at it and every device gets cleaner, ad-free browsing
  with zero per-device setup.
- **Secure remote access over a mesh VPN** with [Tailscale](../README.md#-homelab--self-hosting) —
  the box is reachable from anywhere *without* opening a single port to the public
  internet. This is the single most important design choice here.
- Headless day-to-day, with occasional **VNC** for a graphical session when
  something needs a desktop.

## Lessons worth passing on

- **Mesh VPN beats port-forwarding.** Exposing a home box directly to the internet
  is how people get owned. A mesh network gives you remote access with none of that
  attack surface. Non-negotiable.
- **Treat the onboard storage (eMMC) as fragile.** Don't do heavy, churny writes to
  it; put anything write-heavy on external storage and keep the eMMC for the OS.
- **Right-size the hardware to the job.** Running AdGuard + Tailscale on a $100 ARM
  box instead of a full server is the difference between a few watts and a few
  dozen. Over a year that's real money — and real heat you don't have to deal with.

## What's next

- Add [Uptime Kuma](../README.md#-homelab--self-hosting) for at-a-glance monitoring.
- A scheduled config backup off the box.

## Gear used

- [Inovato Quadra](../README.md#-homelab--self-hosting) — the ARM node itself
- [Tailscale](../README.md#-homelab--self-hosting) — secure mesh remote access
- [AdGuard Home](../README.md#-homelab--self-hosting) — network-wide ad-blocking
