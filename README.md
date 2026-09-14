# 🏠 🖥️ 🧵 🤖 🎒 HomeForge

> Own your home, your servers, and your AI — curated by someone who runs it.

![Stars](https://img.shields.io/github/stars/estivonponcho/homeforge?style=flat-square) ![License](https://img.shields.io/badge/list-CC--BY--4.0-blue?style=flat-square) ![Picks](https://img.shields.io/badge/curated%20picks-110-brightgreen?style=flat-square) ![Updated](https://img.shields.io/badge/updated-2026--09--13-informational?style=flat-square)

A hand-picked kit for the overlapping worlds of the smart home, the homelab, the 3D-printing bench, and running your own AI. No scraped catalogs, no filler — every item here is something worth owning, with an honest one-line take on why.

**Why trust this list?** It's short on purpose. Every pick is something worth owning, with an honest take on *why* and *when*. No auto-scraped listings, no padded counts. If something's here, it earned the slot.

📬 **Get the free [Self-Hosted Home Starter Kit](https://estivonponcho.github.io/homeforge/)** — a one-page buyer's guide + wiring checklist, no fluff. (Link goes to the signup page.)

▶ **[Watch & Build](https://estivonponcho.github.io/homeforge/resources.html)** — a curated video list for each HomeForge pillar, with a concrete project after every three videos.

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
  - [Filament Drying & Storage](#filament-drying-storage)
  - [Tools & Software](#tools-software)
- [🤖 AI & Local LLMs](#ai-local-llms)
  - [Run AI Locally](#run-ai-locally)
  - [Hardware for Local AI](#hardware-for-local-ai)
  - [Manage Claude & ChatGPT](#manage-claude-chatgpt)
  - [Learn AI](#learn-ai)
- [🎒 Tech EDC](#tech-edc)
  - [Gadgets & Tools](#gadgets-tools)
  - [Power & Cables](#power-cables)
  - [Audio](#audio)
  - [Phone Accessories](#phone-accessories)
  - [iPad Accessories](#ipad-accessories)
  - [Apple Watch](#apple-watch)
  - [Notes & Focus](#notes-focus)
- [How this list makes money (and stays honest)](#how-this-list-makes-money-and-stays-honest)
- [Contributing](#contributing)

## 🏠 Smart Home

_Local-first home automation. Bias toward Home Assistant, Zigbee/Thread/Matter, and gear you own rather than rent from a cloud._

### Hubs & Coordinators

- **[Home Assistant Green](https://www.amazon.com/s?k=Home+Assistant+Green&tag=homeforge0a-20)** ⭐ — The no-fuss way to run Home Assistant — plug in, power on, done. The default recommendation for anyone starting out. _( $ )_
- **[Home Assistant Yellow](https://www.home-assistant.io/yellow/)** — PoE, an M.2 slot, and a built-in Zigbee/Thread radio. The upgrade pick when you want one box on the network. _( $$ )_
- **[Raspberry Pi 5](https://www.amazon.com/s?k=Raspberry+Pi+5&tag=homeforge0a-20)** — Still the most flexible base for a DIY HA server. Pair with an NVMe HAT and it flies. _( $ )_

### Radios & Coordinators

- **[Home Assistant Connect ZBT-2](https://www.amazon.com/s?k=Home+Assistant+Connect+ZBT-2&tag=homeforge0a-20)** ⭐ — Home Assistant's current recommendation for a new ZHA network. Add it to Green or another Home Assistant host for a supported Zigbee radio. _( $ )_
- **[Sonoff Zigbee 3.0 USB Dongle Plus (ZBDongle-E)](https://www.amazon.com/s?k=Sonoff+Zigbee+3.0+USB+Dongle+Plus+%28ZBDongle-E%29&tag=homeforge0a-20)** — The budget coordinator everyone recommends. Flash it, stick it on a USB extension, forget about it. _( $ )_

### Sensors & Presence

- **[Aqara Door & Window Sensor](https://www.amazon.com/s?k=Aqara+Door+%26+Window+Sensor&tag=homeforge0a-20)** — Cheap, tiny, reliable Zigbee contact sensors. The gateway drug of home automation. _( $ )_
- **[Aqara Presence Sensor FP2](https://www.amazon.com/s?k=Aqara+Presence+Sensor+FP2&tag=homeforge0a-20)** ⭐ — mMWave presence done well — knows you're in the room even when you're sitting still. Zone mapping is the killer feature. _( $$ )_
- **[Everything Presence Lite](https://shop.everythingsmart.io/)** — Open, ESPHome-based mmWave presence board. The tinkerer's answer to closed-box presence sensors. _( $ )_
- **[SONOFF Zigbee Temp & Humidity Sensor](https://www.amazon.com/s?k=SONOFF+Zigbee+temperature+humidity+sensor&tag=homeforge0a-20)** — Bench-tested: cheap, accurate Zigbee climate sensors with a display. Great for rooms, fridges, and the 3D-printing enclosure. _( $ )_
- **[Govee H5075 Temperature & Humidity Sensor](https://www.amazon.com/s?k=Govee+H5075&tag=homeforge0a-20)** — Used in my setup for simple room climate readings over Bluetooth. Affordable enough to place in several areas. _( $ )_
- **[Govee H5121 Motion Sensor](https://www.amazon.com/s?k=Govee+H5121&tag=homeforge0a-20)** — Used in my setup for motion-triggered routines. Check the current integration path and exact model before buying. _( $ )_
- **[Zigbee Water Leak Sensor](https://www.amazon.com/s?k=Zigbee+water+leak+sensor+Home+Assistant&tag=homeforge0a-20)** ⭐ — A small sensor with an outsized job. Put one near a water heater, washer, sink, or sump area and alert immediately when it reports wet. _( $ )_

### Switches, Plugs & Power

- **[Shelly Plus 1PM](https://www.amazon.com/s?k=Shelly+Plus+1PM&tag=homeforge0a-20)** ⭐ — Relay + power metering that hides behind an existing switch. Local API, ESPHome-flashable, MQTT — the enthusiast favorite. _( $ )_
- **[ThirdReality Zigbee Smart Plug](https://www.amazon.com/s?k=ThirdReality+Zigbee+smart+plug&tag=homeforge0a-20)** — Compact Zigbee plug with power monitoring at a price that lets you buy a ten-pack. Doubles as a Zigbee repeater. _( $ )_
- **[Aqara Smart Plug (Zigbee)](https://www.amazon.com/s?k=Aqara+Smart+Plug+zigbee&tag=homeforge0a-20)** — Zigbee plug with energy monitoring that also acts as a Zigbee router to extend your mesh. Rock-solid in Home Assistant. _( $ )_
- **[Sonoff S60 Zigbee Smart Plug](https://www.amazon.com/s?k=Sonoff+S60+Zigbee+smart+plug&tag=homeforge0a-20)** — Cheap, reliable Zigbee plug with power metering. Pairs instantly with any Zigbee coordinator (ZHA/Z2M). _( $ )_
- **[Eve Energy (Thread + Matter)](https://www.amazon.com/s?k=Eve+Energy+Thread+Matter+smart+plug&tag=homeforge0a-20)** — Thread + Matter plug with energy monitoring and no cloud or Wi-Fi — the closest thing to a set-and-forget local Matter plug. _( $$ )_
- **[Govee H5081 Smart Plug](https://www.amazon.com/s?k=Govee+H5081&tag=homeforge0a-20)** — Used in my setup to automate ordinary plug-in equipment. A practical fit when you already use Govee devices. _( $ )_
- **[Emporia Vue Energy Monitor](https://www.amazon.com/s?k=Emporia+Vue+Energy+Monitor&tag=homeforge0a-20)** — Whole-panel, per-circuit energy monitoring for a fraction of the utility's price. Feeds beautifully into HA dashboards. _( $$ )_

### Lighting

- **[Philips Hue](https://www.amazon.com/s?k=Philips+Hue&tag=homeforge0a-20)** — Still the gold standard for reliable, fast smart lighting. Expensive, but it just works — and now speaks Matter. _( $$ )_
- **[Govee smart lights](https://www.amazon.com/s?k=Govee+smart+lights&tag=homeforge0a-20)** — Bright, affordable smart lighting with a huge range of strips, bulbs, and room kits. A strong value pick when local control is not the only priority. _( $ )_
- **[Govee H6008 Smart Bulb](https://www.amazon.com/s?k=Govee+H6008&tag=homeforge0a-20)** — One of the exact Govee bulb models used in my setup. Good for affordable color lighting in the Govee ecosystem. _( $ )_
- **[Govee H6159 LED Strip](https://www.amazon.com/s?k=Govee+H6159&tag=homeforge0a-20)** — Used in my setup for cabinet and accent lighting. It adds useful task light without changing the room's main fixtures. _( $ )_
- **[Philips Hue Starter Kit](https://www.amazon.com/s?k=Philips+Hue+starter+kit&tag=homeforge0a-20)** ⭐ — A straightforward entry into the Hue ecosystem with a bridge and bulbs. My larger Hue setup has been a dependable lighting layer. _( $$ )_
- **[Tuya smart lights](https://www.amazon.com/s?k=Tuya+smart+lights&tag=homeforge0a-20)** — A broad ecosystem of affordable bulbs, switches, and light strips. Check the exact device integration before buying because Tuya hardware varies by model. _( $ )_
- **[WLED](https://kno.wled.ge/)** — Free firmware that turns an ESP32 + LED strip into gorgeous, HA-controllable lighting. The DIY entry point. _( Free / DIY )_

### Voice & DIY

- **[Home Assistant Voice Preview Edition](https://www.amazon.com/s?k=Home+Assistant+Voice+Preview+Edition&tag=homeforge0a-20)** — Local voice control with no cloud eavesdropping. The privacy-first alternative to Alexa/Google. _( $ )_
- **[ESPHome + ESP32](https://esphome.io/)** — The framework that turns cheap microcontrollers into custom HA sensors and controllers. Where the real fun starts. _( Free / DIY )_

### Bench & DIY Electronics

- **[ESP32 (ESP-WROOM-32) Dev Boards](https://www.amazon.com/s?k=ESP-WROOM-32+ESP32+development+board&tag=homeforge0a-20)** ⭐ — Bench-tested. Dual-core Wi-Fi + Bluetooth for a couple bucks. Buy a 2-pack — you'll always want another. _( $ )_
- **[WeMos D1 Mini (ESP8266)](https://www.amazon.com/s?k=WeMos+D1+Mini+ESP8266&tag=homeforge0a-20)** — Bench-tested. The tiny board behind my Wi-Fi thermal-printer build. Perfect for single-purpose gadgets. _( $ )_
- **[ELEGOO Breadboard Kit](https://www.amazon.com/s?k=ELEGOO+breadboard+kit&tag=homeforge0a-20)** — Bench-tested. Solderless boards in a few sizes. Prototype before you commit anything to solder. _( $ )_
- **[Dupont Jumper Wire Kit](https://www.amazon.com/s?k=dupont+jumper+wires+M+F&tag=homeforge0a-20)** — Bench-tested. M/M, M/F, F/F ribbon cables. You will use every one of these and still want more. _( $ )_
- **[0.96" OLED Display (SSD1306, I2C)](https://www.amazon.com/s?k=0.96+inch+OLED+SSD1306+I2C&tag=homeforge0a-20)** — Bench-tested. Crisp little status screens for any ESP project — two data wires and you're showing readouts. _( $ )_
- **[Logic Level Converter (3.3V ↔ 5V)](https://www.amazon.com/s?k=logic+level+converter+TXS0108E&tag=homeforge0a-20)** — Bench-tested. The part beginners skip and then fry a board. Bridges 3.3V ESP pins to 5V peripherals safely. _( $ )_
- **[Silicone Soldering Mat](https://www.amazon.com/s?k=silicone+soldering+mat+heat+resistant&tag=homeforge0a-20)** — Bench-tested. Heat-resistant surface with magnetic wells for screws. Saves your desk and your sanity. _( $ )_
- **[37-in-1 Sensor Kit](https://www.amazon.com/s?k=37+in+1+sensor+kit+arduino&tag=homeforge0a-20)** — Bench-tested. A grab-bag of sensors and modules to learn with. The fastest way to find your next project. _( $ )_

## 🖥️ Homelab & Self-Hosting

_The boxes, drives, network, and software to run your own services and stop paying rent to someone else's subscription._

### Mini PCs & SBCs

- **[Beelink Mini PC](https://www.amazon.com/s?k=Beelink+Mini+PC&tag=homeforge0a-20)** ⭐ — Tiny, quiet, cheap x86 boxes that run Proxmox or Docker beautifully. The homelab starter that isn't a Pi. _( $$ )_
- **[Minisforum Mini PC](https://www.amazon.com/s?k=Minisforum+Mini+PC&tag=homeforge0a-20)** — Step-up mini PCs with real cores and RAM headroom — for when one node stops being enough. _( $$ )_
- **[Inovato Quadra](https://www.inovato.com/)** — A shockingly cheap ARM box that sips power — perfect for a always-on Tailscale/AdGuard/utility node. _( $ )_

### NAS & Storage

- **[Synology DiskStation](https://www.amazon.com/s?k=Synology+DiskStation&tag=homeforge0a-20)** — The most polished turnkey NAS. Pay the premium if you want storage that your family can use too. _( $$$ )_
- **[UGREEN NASync](https://www.amazon.com/s?k=UGREEN+NASync&tag=homeforge0a-20)** ⭐ — The value NAS challenger — strong hardware, and you can run TrueNAS/Unraid on it if you outgrow the stock OS. _( $$ )_
- **[WD Red Plus NAS Drives](https://www.amazon.com/s?k=WD+Red+Plus+NAS+Drives&tag=homeforge0a-20)** — CMR NAS drives built for 24/7 spinning. Buy from mixed batches, always keep a cold spare. _( $$ )_
- **[Samsung T7 Portable SSD](https://www.amazon.com/s?k=Samsung+T7+Portable+SSD&tag=homeforge0a-20)** — Fast, pocketable USB-C SSD — great for Time Machine, VM backups, or a bootable rescue drive. _( $$ )_

### Networking

- **[UniFi (Ubiquiti)](https://www.amazon.com/s?k=UniFi+%28Ubiquiti%29&tag=homeforge0a-20)** — Prosumer networking with a gorgeous controller. Once you VLAN off your IoT gear you won't go back. _( $$$ )_
- **[GL.iNet Travel Router](https://www.amazon.com/s?k=GL.iNet+Travel+Router&tag=homeforge0a-20)** ⭐ — Pocket router running OpenWrt with WireGuard/Tailscale baked in. The remote-access swiss army knife. _( $ )_
- **[Tailscale](https://tailscale.com/)** — Zero-config mesh VPN that makes your whole lab reachable from anywhere without opening a single port. _( Free tier )_

### Self-Hosted Software

- **[Proxmox VE](https://www.proxmox.com/)** — Free, rock-solid hypervisor. The foundation most serious homelabs are built on. _( Free )_
- **[Immich](https://immich.app/)** ⭐ — Self-hosted Google Photos replacement that's genuinely good now. The reason a lot of people build a homelab. _( Free )_
- **[Jellyfin](https://jellyfin.org/)** — Fully free, no-account media server. Owns your movies and shows without a subscription. _( Free )_
- **[AdGuard Home](https://adguard.com/adguard-home/overview.html)** — Network-wide ad and tracker blocking. Point your DHCP at it and every device gets cleaner. _( Free )_
- **[Frigate NVR](https://frigate.video/)** — Local, AI-powered camera recording with real object detection — no cloud subscription, no monthly fee. _( Free )_

### Power Protection

- **[CyberPower UPS](https://www.amazon.com/s?k=CyberPower+UPS&tag=homeforge0a-20)** — Keeps your NAS and HA box alive through blips and lets them shut down cleanly. Non-negotiable once data matters. _( $$ )_

### Bench & Maintenance

- **[Phomemo D30 Label Maker](https://www.amazon.com/s?k=Phomemo+D30+label+maker&tag=homeforge0a-20)** — Bench-tested. Label your cables, drives, and bins. The cheapest upgrade to a homelab you'll actually maintain. _( $ )_
- **[ARCTIC MX-4 Thermal Paste](https://www.amazon.com/s?k=ARCTIC+MX-4+thermal+paste&tag=homeforge0a-20)** — Bench-tested. The reliable, non-conductive default for repasting a mini PC, NAS, or GPU that's running hot. _( $ )_

## 🧵 3D Printing

_Printers, filament, upgrades and tools that earn their place on the bench — tuned toward the Bambu ecosystem but not married to it._

### Printers

- **[Bambu Lab A1 mini](https://bambulab.com/en/a1-mini)** ⭐ — The best first printer, full stop. Auto-calibration means you print instead of tinker — unless you want to. _( $ )_
- **[Bambu Lab A1](https://bambulab.com/en/a1)** — Full-size bed, same hands-off ease as the mini, optional AMS lite for multicolor. The value sweet spot. _( $$ )_
- **[Bambu Lab P1S](https://bambulab.com/en/p1)** ⭐ — Enclosed CoreXY speed demon for ABS/ASA and engineering filaments. The upgrade most people land on. _( $$ )_
- **[Prusa Core One](https://www.prusa3d.com/)** — The open, repairable, made-to-last alternative. Buy it if you value the ecosystem and want to own your machine. _( $$$ )_

### Filament

- **[Bambu PLA Basic](https://bambulab.com/en/filament)** — Consistent, RFID-tagged filament that the AMS reads automatically. The path of least resistance. _( $ )_
- **[Polymaker PolyTerra PLA](https://www.amazon.com/s?k=Polymaker+PolyTerra+PLA&tag=homeforge0a-20)** — Matte finish, great color range, eco-spool. A favorite for parts you want to look intentional. _( $ )_
- **[Overture PETG](https://www.amazon.com/s?k=Overture+PETG&tag=homeforge0a-20)** ⭐ — Reliable, affordable PETG for functional parts that need to survive heat and stress. The go-to workhorse. _( $ )_
- **[ELEGOO Rapid PETG](https://www.amazon.com/s?k=ELEGOO+Rapid+PETG+filament&tag=homeforge0a-20)** ⭐ — Bench-tested (I go through this by the case): high-speed PETG that prints clean and cheap. My default workhorse spool. _( $ )_
- **[DEEPLEE PLA (2kg / 4kg)](https://www.amazon.com/s?k=DEEPLEE+PLA+filament&tag=homeforge0a-20)** — Bench-tested. Big-spool value PLA that winds neatly and doesn't clog. What I reach for when cost-per-gram matters. _( $ )_

### Upgrades & Accessories

- **[Bambu AMS](https://bambulab.com/en/ams)** — Multi-color and multi-material without babysitting. Also just a great auto-feeding filament pantry. _( $$ )_
- **[Hardened Steel Nozzle](https://www.amazon.com/s?k=Hardened+Steel+Nozzle&tag=homeforge0a-20)** — The five-dollar upgrade that saves your nozzle the first time you print carbon-fiber or glow filament. _( $ )_

### Filament Drying & Storage

- **[SUNLU S4 Filament Dryer](https://www.amazon.com/s?k=SUNLU+S4+filament+dryer&tag=homeforge0a-20)** ⭐ — Bench-tested — the one I use. 4-spool capacity, 3 circulation fans, 350W PTC heater to 70°C, with humidity readout. Wet filament ruins prints; this fixed my stringing and brittle parts. _( $$ )_
- **[Fonday Rechargeable Silica Gel Desiccant Beads](https://www.amazon.com/s?k=Fonday+moisture+indicating+silica+gel+desiccant+beads+rechargeable&tag=homeforge0a-20)** — Bench-tested. Color-indicating beads (orange → green when spent) that I keep in the AMS and every storage bin. Bake them dry and reuse for years. _( $ )_
- **[Shazo Airtight Storage Containers](https://www.amazon.com/dp/B0CZ1MGZGG?tag=homeforge0a-20)** — Bench-tested — the airtight containers I actually store spools in. Add a scoop of desiccant and filament stays dry for months. Cheapest insurance against wasted filament. _( $ )_

### Tools & Software

- **[OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)** — The community slicer with the best calibration tooling. Free, and better than most stock slicers. _( Free )_
- **[Digital Calipers](https://www.amazon.com/s?k=Digital+Calipers&tag=homeforge0a-20)** ⭐ — You cannot design functional parts without measuring. Buy one decent pair, not three cheap ones. _( $ )_
- **[MakerWorld](https://makerworld.com/)** — Huge, mostly-free model library with one-click print profiles for Bambu machines. Start here before modeling anything. _( Free )_

## 🤖 AI & Local LLMs

_Run models on your own hardware, and drive Claude & ChatGPT like a pro. The same 'own it, don't rent it' ethos as the rest of the list._

### Run AI Locally

- **[Ollama](https://ollama.com/)** ⭐ — Run open LLMs locally with one command. The easiest on-ramp to your own private AI. _( Free )_
- **[LM Studio](https://lmstudio.ai/)** — A polished desktop app for downloading and chatting with local models. Great for non-terminal folks. _( Free )_
- **[Open WebUI](https://openwebui.com/)** — Self-hosted ChatGPT-style front end for Ollama and any OpenAI-compatible API. Runs beautifully on the homelab. _( Free )_
- **[Jan](https://jan.ai/)** — Open-source, offline-first AI assistant. Everything stays on your machine. _( Free )_

### Hardware for Local AI

- **[Mac mini (Apple Silicon)](https://www.amazon.com/s?k=Mac+mini+%28Apple+Silicon%29&tag=homeforge0a-20)** ⭐ — Unified memory makes it a shockingly good, quiet local-LLM box. The value pick for running mid-size models. _( $$ )_
- **[NVIDIA GeForce RTX (VRAM is king)](https://www.amazon.com/s?k=NVIDIA+GeForce+RTX+%28VRAM+is+king%29&tag=homeforge0a-20)** — For local AI, buy the most VRAM you can afford. A used 3090's 24GB still punches above its price. _( $$$ )_
- **[NVIDIA Jetson Orin Nano](https://www.amazon.com/s?k=NVIDIA+Jetson+Orin+Nano&tag=homeforge0a-20)** — A tiny always-on edge box for running small models and vision at the edge of your network. _( $$ )_

### Manage Claude & ChatGPT

- **[Claude Code](https://claude.com/claude-code)** ⭐ — Drive Claude from your terminal to build, edit, and automate. The power-user way to work with Claude. _( Free / Sub )_
- **[ChatGPT](https://chatgpt.com/)** — Custom instructions + Projects + memory turn it from a toy into a real assistant. Learn those three and it changes. _( Free / Sub )_
- **[Cursor](https://cursor.com/)** — AI-native code editor. If you write code, this is the fastest on-ramp to model-assisted work. _( Free / Sub )_
- **[LibreChat](https://www.librechat.ai/)** — Self-hosted, multi-model chat UI — bring your own API keys for Claude, GPT, and local models in one place. _( Free )_

### Learn AI

- **[AI Engineering (Chip Huyen)](https://www.amazon.com/s?k=AI+Engineering+Chip+Huyen&tag=homeforge0a-20)** ⭐ — The field guide to building real products on top of foundation models. Start here if you're going pro. _( $$ )_
- **[Hands-On Large Language Models](https://www.amazon.com/s?k=Hands-On+Large+Language+Models&tag=homeforge0a-20)** — The best illustrated, practical intro to how LLMs actually work and how to use them. _( $$ )_
- **[DeepLearning.AI Short Courses](https://www.deeplearning.ai/courses/)** — Free, focused, hour-long courses on prompting, RAG, agents, and more. The fastest way to skill up. _( Free )_
- **[fast.ai](https://www.fast.ai/)** — The legendary free, top-down deep-learning course. Rigorous without being academic-for-its-own-sake. _( Free )_

## 🎒 Tech EDC

_The tech you actually carry — gadgets, power, audio, and the organizers that keep it all from becoming a tangle in your bag._

### Gadgets & Tools

- **[Flipper Zero](https://www.amazon.com/s?k=Flipper+Zero&tag=homeforge0a-20)** ⭐ — Bench-tested — mine runs Momentum firmware. A pocket multi-tool for RF, NFC, IR, and GPIO. The most fun thing in the bag. _( $$ )_
- **[LOCHBY Tool Roll](https://www.lochby.com/)** — Waxed-canvas roll that keeps your bits, cables, and small tools organized and rugged. The grown-up alternative to a ziplock bag. _( $$ )_
- **[iFixit Precision Bit Driver](https://www.amazon.com/s?k=iFixit+precision+bit+driver+set&tag=homeforge0a-20)** — The kit that opens every phone, console, and gadget. If you mod hardware, this lives in the bag. _( $ )_
- **[Gerber Dual-Force Multitool](https://www.amazon.com/s?k=Gerber+Dual-Force+multitool&tag=homeforge0a-20)** — Bench-tested — the multitool I carry. One-thumb sliding pliers with serious clamping force, plus drivers, blade, and more. _( $$ )_
- **[Clip & Carry Kydex Sheath (Dual-Force)](https://www.amazon.com/s?k=Clip+Carry+Kydex+sheath+Gerber+Dual-Force&tag=homeforge0a-20)** — Bench-tested. US-made Kydex holster that carries the Dual-Force on your belt, so the tool is actually on you when you need it. _( $ )_
- **[Nite Ize Clip Pock-Its XL](https://www.amazon.com/s?k=Nite+Ize+Clip+Pock-Its+XL&tag=homeforge0a-20)** — Bench-tested. Clip-on utility holster with pockets for a multitool, pen, and small gear — keeps the loose stuff together. _( $ )_
- **[EDC Ratchet Wrench (multitool bit adapter)](https://www.amazon.com/s?k=711L+EDC+ratchet+wrench+multitool+flat+bit&tag=homeforge0a-20)** — Bench-tested. A tiny ratchet that snaps onto a multitool's flat bit driver — turns it into a real ratcheting screwdriver. _( $ )_

### Power & Cables

- **[Anker GaN USB-C Charger](https://www.amazon.com/s?k=Anker+GaN+USB-C+charger&tag=homeforge0a-20)** — One small brick that fast-charges your phone, tablet, and laptop. GaN means tiny and cool-running. _( $ )_
- **[USB-C Power Meter / Cable Tester](https://www.amazon.com/s?k=USB-C+power+meter+tester&tag=homeforge0a-20)** — Tells you what's actually charging and which cable is lying to you. A tinkerer's truth-teller. _( $ )_
- **[Braided USB-C Cable](https://www.amazon.com/s?k=braided+USB-C+cable+100W&tag=homeforge0a-20)** — A 100W braided cable that won't fray. Carry two; you'll always need one more than you have. _( $ )_

### Audio

- **[Soundcore Wireless Earbuds](https://www.amazon.com/s?k=Soundcore+by+Anker+wireless+earbuds&tag=homeforge0a-20)** — The value-per-dollar pick for calls, podcasts, and focus — most of the good stuff for a fraction of flagship prices. _( $ )_

### Phone Accessories

- **[PopSockets Grip](https://www.amazon.com/s?k=PopSockets+grip&tag=homeforge0a-20)** — The one-handed grip + kickstand that quietly prevents dropped phones. MagSafe versions pop on and off cleanly. _( $ )_
- **[MagSafe Wallet Stand](https://www.amazon.com/s?k=MagSafe+wallet+stand&tag=homeforge0a-20)** — Cards on the back, flips out to a stand for videos. Ditches the bulky case-wallet. _( $ )_
- **[Spigen Tough Armor MagFit Case](https://www.amazon.com/s?k=Spigen+Tough+Armor+MagFit+case&tag=homeforge0a-20)** — Bench-tested — the case I run on my phone. Built-in kickstand, MagSafe, and genuine military-grade protection. _( $ )_
- **[Tango Ultra-Thin MagSafe Grip](https://www.amazon.com/s?k=Tango+ultra+thin+MagSafe+grip&tag=homeforge0a-20)** — Bench-tested. Space-grade steel grip + stand that's half the thickness of a PopSocket and pops off for wireless charging. _( $ )_

### iPad Accessories

- **[MOFT Dynamic Folio (iPad mini)](https://www.amazon.com/s?k=MOFT+Dynamic+Folio+iPad+mini&tag=homeforge0a-20)** ⭐ — Bench-tested. Slim magnetic folio with 20+ viewing angles and auto wake/sleep — turns the mini into a stand anywhere. _( $$ )_
- **[Spigen Rugged Armor Pro (iPad)](https://www.amazon.com/s?k=Spigen+Rugged+Armor+Pro+iPad+case&tag=homeforge0a-20)** — Bench-tested. Tri-fold rugged case with a built-in Pencil holder — protection without turning the iPad into a brick. _( $ )_
- **[iPad Tempered-Glass Screen Protector](https://www.amazon.com/s?k=iPad+tempered+glass+screen+protector+install+tray&tag=homeforge0a-20)** — Bench-tested. 9H glass with an alignment/install tray so you don't trap bubbles or dust. Buy the two-pack. _( $ )_
- **[MOFT Apple Pencil Holder](https://www.amazon.com/s?k=MOFT+Pencil+holder+Apple+Pencil&tag=homeforge0a-20)** — Bench-tested. Stick-on holder so the Apple Pencil stops rolling off the desk or vanishing in the bag. _( $ )_

### Apple Watch

- **[Nylon Sport Loop Bands](https://www.amazon.com/s?k=Apple+Watch+nylon+sport+loop+band&tag=homeforge0a-20)** — Bench-tested. Breathable nylon loops in every color for a few bucks each — the easy, cheap way to change the watch up daily. _( $ )_
- **[Titanium Band (Ultra)](https://www.amazon.com/s?k=Apple+Watch+Ultra+titanium+band&tag=homeforge0a-20)** — Bench-tested. Titanium link band with a steel buckle — the premium metal look for a fraction of Apple's price. _( $$ )_
- **[ESR Armorite Screen Protector](https://www.amazon.com/s?k=ESR+Armorite+Apple+Watch+screen+protector&tag=homeforge0a-20)** — Bench-tested. Tempered glass + alloy frame that actually saves the screen from bench dings and doorframes. _( $ )_
- **[Portable USB-C Magnetic Watch Charger](https://www.amazon.com/s?k=USB-C+Apple+Watch+magnetic+charger+portable&tag=homeforge0a-20)** — Bench-tested. A tiny USB-C magnetic puck so you can top the watch off from any charger or power bank in the bag. _( $ )_

### Notes & Focus

- **[Supernote A6 X2 Nomad](https://supernote.com/)** ⭐ — Bench-tested — my e-ink notebook. Paper-like writing with zero notifications: the antidote to taking notes on a device that pings you every 30 seconds. _( $$$ )_

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
