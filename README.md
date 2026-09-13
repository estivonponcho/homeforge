# 🏠 🖥️ 🧵 🤖 HomeForge

> Own your home, your servers, and your AI — curated by someone who runs it.

![Stars](https://img.shields.io/github/stars/YOUR-GH-USERNAME/homeforge?style=flat-square) ![License](https://img.shields.io/badge/list-CC--BY--4.0-blue?style=flat-square) ![Picks](https://img.shields.io/badge/curated%20picks-72-brightgreen?style=flat-square) ![Updated](https://img.shields.io/badge/updated-2026--09--13-informational?style=flat-square)

A hand-picked kit for the overlapping worlds of the smart home, the homelab, the 3D-printing bench, and running your own AI. No scraped catalogs, no filler — every item here is something worth owning, with an honest one-line take on why.

**Why trust this list?** It's short on purpose. Every pick is something worth owning, with an honest take on *why* and *when*. No auto-scraped listings, no padded counts. If something's here, it earned the slot.

📬 **Get the free [Self-Hosted Home Starter Kit](https://YOUR-DOMAIN.example)** — a one-page buyer's guide + wiring checklist, no fluff. (Link goes to the signup page.)

## Contents

- [🏠 Smart Home](#smart-home)
  - [Hubs & Coordinators](#hubs-coordinators)
  - [Radios & Coordinators](#radios-coordinators)
  - [Sensors & Presence](#sensors-presence)
  - [Switches, Plugs & Power](#switches-plugs-power)
  - [Lighting](#lighting)
  - [Voice & DIY](#voice-diy)
  - [Bench & DIY Electronics](#bench-diy-electronics)
- [🖥️ Homelab & Self-Hosting](#homelab-self-hosting)
  - [Mini PCs & SBCs](#mini-pcs-sbcs)
  - [NAS & Storage](#nas-storage)
  - [Networking](#networking)
  - [Self-Hosted Software](#self-hosted-software)
  - [Power Protection](#power-protection)
  - [Bench & Maintenance](#bench-maintenance)
- [🧵 3D Printing](#3d-printing)
  - [Printers](#printers)
  - [Filament](#filament)
  - [Upgrades & Accessories](#upgrades-accessories)
  - [Tools & Software](#tools-software)
- [🤖 AI & Local LLMs](#ai-local-llms)
  - [Run AI Locally](#run-ai-locally)
  - [Hardware for Local AI](#hardware-for-local-ai)
  - [Manage Claude & ChatGPT](#manage-claude-chatgpt)
  - [Learn AI](#learn-ai)
- [How this list makes money (and stays honest)](#how-this-list-makes-money-and-stays-honest)
- [Contributing](#contributing)

## 🏠 Smart Home

_Local-first home automation. Bias toward Home Assistant, Zigbee/Thread/Matter, and gear you own rather than rent from a cloud._

### Hubs & Coordinators

- **[Home Assistant Green](https://www.home-assistant.io/green/)** ⭐ — The no-fuss way to run Home Assistant — plug in, power on, done. The default recommendation for anyone starting out. _( $ )_
- **[Home Assistant Yellow](https://www.home-assistant.io/yellow/)** — PoE, an M.2 slot, and a built-in Zigbee/Thread radio. The upgrade pick when you want one box on the network. _( $$ )_
- **[Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)** — Still the most flexible base for a DIY HA server. Pair with an NVMe HAT and it flies. _( $ )_

### Radios & Coordinators

- **[Home Assistant Connect ZBT-1](https://www.home-assistant.io/connectzbt1/)** ⭐ — The SkyConnect successor — a USB Zigbee + Thread stick that keeps your radio off the main board and easy to relocate. _( $ )_
- **[Sonoff Zigbee 3.0 USB Dongle Plus (ZBDongle-E)](https://sonoff.tech/)** — The budget coordinator everyone recommends. Flash it, stick it on a USB extension, forget about it. _( $ )_

### Sensors & Presence

- **[Aqara Door & Window Sensor](https://www.aqara.com/)** — Cheap, tiny, reliable Zigbee contact sensors. The gateway drug of home automation. _( $ )_
- **[Aqara Presence Sensor FP2](https://www.aqara.com/en/product/presence-sensor-fp2/)** ⭐ — mMWave presence done well — knows you're in the room even when you're sitting still. Zone mapping is the killer feature. _( $$ )_
- **[Everything Presence Lite](https://shop.everythingsmart.io/)** — Open, ESPHome-based mmWave presence board. The tinkerer's answer to closed-box presence sensors. _( $ )_
- **[SONOFF Zigbee Temp & Humidity Sensor](https://www.amazon.com/s?k=SONOFF+Zigbee+temperature+humidity+sensor)** — Bench-tested: cheap, accurate Zigbee climate sensors with a display. Great for rooms, fridges, and the 3D-printing enclosure. _( $ )_

### Switches, Plugs & Power

- **[Shelly Plus 1PM](https://www.shelly.com/)** ⭐ — Relay + power metering that hides behind an existing switch. Local API, ESPHome-flashable, MQTT — the enthusiast favorite. _( $ )_
- **[ThirdReality Zigbee Smart Plug](https://www.3reality.com/)** — Compact Zigbee plugs with power monitoring at a price that lets you buy a ten-pack. _( $ )_
- **[Emporia Vue Energy Monitor](https://www.emporiaenergy.com/)** — Whole-panel, per-circuit energy monitoring for a fraction of the utility's price. Feeds beautifully into HA dashboards. _( $$ )_

### Lighting

- **[Philips Hue](https://www.philips-hue.com/)** — Still the gold standard for reliable, fast smart lighting. Expensive, but it just works — and now speaks Matter. _( $$ )_
- **[WLED](https://kno.wled.ge/)** — Free firmware that turns an ESP32 + LED strip into gorgeous, HA-controllable lighting. The DIY entry point. _( Free / DIY )_

### Voice & DIY

- **[Home Assistant Voice Preview Edition](https://www.home-assistant.io/voice-pe/)** — Local voice control with no cloud eavesdropping. The privacy-first alternative to Alexa/Google. _( $ )_
- **[ESPHome + ESP32](https://esphome.io/)** — The framework that turns cheap microcontrollers into custom HA sensors and controllers. Where the real fun starts. _( Free / DIY )_

### Bench & DIY Electronics

- **[ESP32 (ESP-WROOM-32) Dev Boards](https://www.amazon.com/s?k=ESP-WROOM-32+ESP32+development+board)** ⭐ — Bench-tested. Dual-core Wi-Fi + Bluetooth for a couple bucks. Buy a 2-pack — you'll always want another. _( $ )_
- **[WeMos D1 Mini (ESP8266)](https://www.amazon.com/s?k=WeMos+D1+Mini+ESP8266)** — Bench-tested. The tiny board behind my Wi-Fi thermal-printer build. Perfect for single-purpose gadgets. _( $ )_
- **[ELEGOO Breadboard Kit](https://www.amazon.com/s?k=ELEGOO+breadboard+kit)** — Bench-tested. Solderless boards in a few sizes. Prototype before you commit anything to solder. _( $ )_
- **[Dupont Jumper Wire Kit](https://www.amazon.com/s?k=dupont+jumper+wires+M+F)** — Bench-tested. M/M, M/F, F/F ribbon cables. You will use every one of these and still want more. _( $ )_
- **[0.96" OLED Display (SSD1306, I2C)](https://www.amazon.com/s?k=0.96+inch+OLED+SSD1306+I2C)** — Bench-tested. Crisp little status screens for any ESP project — two data wires and you're showing readouts. _( $ )_
- **[Logic Level Converter (3.3V ↔ 5V)](https://www.amazon.com/s?k=logic+level+converter+TXS0108E)** — Bench-tested. The part beginners skip and then fry a board. Bridges 3.3V ESP pins to 5V peripherals safely. _( $ )_
- **[Silicone Soldering Mat](https://www.amazon.com/s?k=silicone+soldering+mat+heat+resistant)** — Bench-tested. Heat-resistant surface with magnetic wells for screws. Saves your desk and your sanity. _( $ )_
- **[37-in-1 Sensor Kit](https://www.amazon.com/s?k=37+in+1+sensor+kit+arduino)** — Bench-tested. A grab-bag of sensors and modules to learn with. The fastest way to find your next project. _( $ )_

## 🖥️ Homelab & Self-Hosting

_The boxes, drives, network, and software to run your own services and stop paying rent to someone else's subscription._

### Mini PCs & SBCs

- **[Beelink Mini PC](https://www.bee-link.com/)** ⭐ — Tiny, quiet, cheap x86 boxes that run Proxmox or Docker beautifully. The homelab starter that isn't a Pi. _( $$ )_
- **[Minisforum Mini PC](https://www.minisforum.com/)** — Step-up mini PCs with real cores and RAM headroom — for when one node stops being enough. _( $$ )_
- **[Inovato Quadra](https://www.inovato.com/)** — A shockingly cheap ARM box that sips power — perfect for a always-on Tailscale/AdGuard/utility node. _( $ )_

### NAS & Storage

- **[Synology DiskStation](https://www.synology.com/)** — The most polished turnkey NAS. Pay the premium if you want storage that your family can use too. _( $$$ )_
- **[UGREEN NASync](https://nas.ugreen.com/)** ⭐ — The value NAS challenger — strong hardware, and you can run TrueNAS/Unraid on it if you outgrow the stock OS. _( $$ )_
- **[WD Red Plus NAS Drives](https://www.westerndigital.com/)** — CMR NAS drives built for 24/7 spinning. Buy from mixed batches, always keep a cold spare. _( $$ )_
- **[Samsung T7 Portable SSD](https://www.samsung.com/)** — Fast, pocketable USB-C SSD — great for Time Machine, VM backups, or a bootable rescue drive. _( $$ )_

### Networking

- **[UniFi (Ubiquiti)](https://ui.com/)** — Prosumer networking with a gorgeous controller. Once you VLAN off your IoT gear you won't go back. _( $$$ )_
- **[GL.iNet Travel Router](https://www.gl-inet.com/)** ⭐ — Pocket router running OpenWrt with WireGuard/Tailscale baked in. The remote-access swiss army knife. _( $ )_
- **[Tailscale](https://tailscale.com/)** — Zero-config mesh VPN that makes your whole lab reachable from anywhere without opening a single port. _( Free tier )_

### Self-Hosted Software

- **[Proxmox VE](https://www.proxmox.com/)** — Free, rock-solid hypervisor. The foundation most serious homelabs are built on. _( Free )_
- **[Immich](https://immich.app/)** ⭐ — Self-hosted Google Photos replacement that's genuinely good now. The reason a lot of people build a homelab. _( Free )_
- **[Jellyfin](https://jellyfin.org/)** — Fully free, no-account media server. Owns your movies and shows without a subscription. _( Free )_
- **[AdGuard Home](https://adguard.com/adguard-home/overview.html)** — Network-wide ad and tracker blocking. Point your DHCP at it and every device gets cleaner. _( Free )_
- **[Frigate NVR](https://frigate.video/)** — Local, AI-powered camera recording with real object detection — no cloud subscription, no monthly fee. _( Free )_

### Power Protection

- **[CyberPower UPS](https://www.cyberpowersystems.com/)** — Keeps your NAS and HA box alive through blips and lets them shut down cleanly. Non-negotiable once data matters. _( $$ )_

### Bench & Maintenance

- **[Phomemo D30 Label Maker](https://www.amazon.com/s?k=Phomemo+D30+label+maker)** — Bench-tested. Label your cables, drives, and bins. The cheapest upgrade to a homelab you'll actually maintain. _( $ )_
- **[ARCTIC MX-4 Thermal Paste](https://www.amazon.com/s?k=ARCTIC+MX-4+thermal+paste)** — Bench-tested. The reliable, non-conductive default for repasting a mini PC, NAS, or GPU that's running hot. _( $ )_

## 🧵 3D Printing

_Printers, filament, upgrades and tools that earn their place on the bench — tuned toward the Bambu ecosystem but not married to it._

### Printers

- **[Bambu Lab A1 mini](https://bambulab.com/en/a1-mini)** ⭐ — The best first printer, full stop. Auto-calibration means you print instead of tinker — unless you want to. _( $ )_
- **[Bambu Lab A1](https://bambulab.com/en/a1)** — Full-size bed, same hands-off ease as the mini, optional AMS lite for multicolor. The value sweet spot. _( $$ )_
- **[Bambu Lab P1S](https://bambulab.com/en/p1)** ⭐ — Enclosed CoreXY speed demon for ABS/ASA and engineering filaments. The upgrade most people land on. _( $$ )_
- **[Prusa Core One](https://www.prusa3d.com/)** — The open, repairable, made-to-last alternative. Buy it if you value the ecosystem and want to own your machine. _( $$$ )_

### Filament

- **[Bambu PLA Basic](https://bambulab.com/en/filament)** — Consistent, RFID-tagged filament that the AMS reads automatically. The path of least resistance. _( $ )_
- **[Polymaker PolyTerra PLA](https://polymaker.com/)** — Matte finish, great color range, eco-spool. A favorite for parts you want to look intentional. _( $ )_
- **[Overture PETG](https://overture3d.com/)** ⭐ — Reliable, affordable PETG for functional parts that need to survive heat and stress. The go-to workhorse. _( $ )_
- **[ELEGOO Rapid PETG](https://www.amazon.com/s?k=ELEGOO+Rapid+PETG+filament)** ⭐ — Bench-tested (I go through this by the case): high-speed PETG that prints clean and cheap. My default workhorse spool. _( $ )_
- **[DEEPLEE PLA (2kg / 4kg)](https://www.amazon.com/s?k=DEEPLEE+PLA+filament)** — Bench-tested. Big-spool value PLA that winds neatly and doesn't clog. What I reach for when cost-per-gram matters. _( $ )_

### Upgrades & Accessories

- **[Bambu AMS](https://bambulab.com/en/ams)** — Multi-color and multi-material without babysitting. Also just a great auto-feeding filament pantry. _( $$ )_
- **[Hardened Steel Nozzle](https://bambulab.com/)** — The five-dollar upgrade that saves your nozzle the first time you print carbon-fiber or glow filament. _( $ )_
- **[Filament Dryer (Sunlu S4 / Eibos)](https://www.sunlu.com/)** — Wet filament ruins prints. A dryer fixes stringing and brittle parts — the upgrade people skip and regret. _( $ )_

### Tools & Software

- **[OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)** — The community slicer with the best calibration tooling. Free, and better than most stock slicers. _( Free )_
- **[Digital Calipers](https://www.mitutoyo.com/)** ⭐ — You cannot design functional parts without measuring. Buy one decent pair, not three cheap ones. _( $ )_
- **[MakerWorld](https://makerworld.com/)** — Huge, mostly-free model library with one-click print profiles for Bambu machines. Start here before modeling anything. _( Free )_

## 🤖 AI & Local LLMs

_Run models on your own hardware, and drive Claude & ChatGPT like a pro. The same 'own it, don't rent it' ethos as the rest of the list._

### Run AI Locally

- **[Ollama](https://ollama.com/)** ⭐ — Run open LLMs locally with one command. The easiest on-ramp to your own private AI. _( Free )_
- **[LM Studio](https://lmstudio.ai/)** — A polished desktop app for downloading and chatting with local models. Great for non-terminal folks. _( Free )_
- **[Open WebUI](https://openwebui.com/)** — Self-hosted ChatGPT-style front end for Ollama and any OpenAI-compatible API. Runs beautifully on the homelab. _( Free )_
- **[Jan](https://jan.ai/)** — Open-source, offline-first AI assistant. Everything stays on your machine. _( Free )_

### Hardware for Local AI

- **[Mac mini (Apple Silicon)](https://www.apple.com/mac-mini/)** ⭐ — Unified memory makes it a shockingly good, quiet local-LLM box. The value pick for running mid-size models. _( $$ )_
- **[NVIDIA GeForce RTX (VRAM is king)](https://www.nvidia.com/en-us/geforce/graphics-cards/)** — For local AI, buy the most VRAM you can afford. A used 3090's 24GB still punches above its price. _( $$$ )_
- **[NVIDIA Jetson Orin Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)** — A tiny always-on edge box for running small models and vision at the edge of your network. _( $$ )_

### Manage Claude & ChatGPT

- **[Claude Code](https://claude.com/claude-code)** ⭐ — Drive Claude from your terminal to build, edit, and automate. The power-user way to work with Claude. _( Free / Sub )_
- **[ChatGPT](https://chatgpt.com/)** — Custom instructions + Projects + memory turn it from a toy into a real assistant. Learn those three and it changes. _( Free / Sub )_
- **[Cursor](https://cursor.com/)** — AI-native code editor. If you write code, this is the fastest on-ramp to model-assisted work. _( Free / Sub )_
- **[LibreChat](https://www.librechat.ai/)** — Self-hosted, multi-model chat UI — bring your own API keys for Claude, GPT, and local models in one place. _( Free )_

### Learn AI

- **[AI Engineering (Chip Huyen)](https://www.amazon.com/s?k=AI+Engineering+Chip+Huyen)** ⭐ — The field guide to building real products on top of foundation models. Start here if you're going pro. _( $$ )_
- **[Hands-On Large Language Models](https://www.amazon.com/s?k=Hands-On+Large+Language+Models)** — The best illustrated, practical intro to how LLMs actually work and how to use them. _( $$ )_
- **[DeepLearning.AI Short Courses](https://www.deeplearning.ai/courses/)** — Free, focused, hour-long courses on prompting, RAG, agents, and more. The fastest way to skill up. _( Free )_
- **[fast.ai](https://www.fast.ai/)** — The legendary free, top-down deep-learning course. Rigorous without being academic-for-its-own-sake. _( Free )_

## How this list makes money (and stays honest)

Some links are affiliate links: if you buy through them, this project may earn a small commission at no extra cost to you. That's it — that's the whole business model. See [AFFILIATE-DISCLOSURE.md](AFFILIATE-DISCLOSURE.md).

What this project will **never** do:

- Recommend something bad because it pays better.
- Pad the list with junk to inflate a count.
- Hide that a link is an affiliate link.

## Who curates this

I hold the MIT Sloan + CSAIL certificate in Artificial Intelligence: Implications for Business Strategy — and I actually build this stuff: ESP firmware, a self-hosted homelab, 3D printing, board-level hardware mods, and custom apps. Everything here is gear and knowledge I use, not a scraped catalog.

**Credential:** Certificate — Artificial Intelligence: Implications for Business Strategy · MIT Sloan School of Management + CSAIL

## Contributing

Got a pick that genuinely belongs here? Open an issue or PR — see [CONTRIBUTING.md](CONTRIBUTING.md). Picks live in [`data/picks.json`](data/picks.json); this README is generated from it by [`scripts/build.py`](scripts/build.py), so edit the data, not the README.

---

_Last updated 2026-09-13. Curated by a human who runs this stuff._
