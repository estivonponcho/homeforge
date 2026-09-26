# How to dry and store 3D-printing filament (2026)

Half of "my printer is broken" is actually wet filament. Plastic absorbs moisture
from the air; when that water hits the hot nozzle it flashes to steam, and you get
stringing, popping, weak layers, and a rough surface. The fix is cheap and it's the
single biggest quality upgrade most people skip. Here's the exact system I use.

## Signs your filament is wet

- Stringing and wisps between parts that tuning won't fix
- Popping or crackling sounds from the nozzle
- Rough, bumpy, or hazy surfaces
- Parts that snap instead of flex (brittle layers)

PETG, TPU, and nylon drink moisture fast; even PLA does over time.

## The three-part system

<figure class="diagram">
<svg viewBox="0 0 720 130" role="img" aria-label="Filament moisture workflow">
<rect class="box" x="6" y="36" width="150" height="58" rx="8" stroke-width="1.5"/>
<text x="81" y="60" font-size="12" text-anchor="middle">New / wet</text>
<text x="81" y="78" font-size="12" text-anchor="middle">spool</text>
<rect class="box" x="196" y="36" width="150" height="58" rx="8" stroke-width="1.5"/>
<text x="271" y="60" font-size="12" text-anchor="middle">Dryer</text>
<text x="271" y="78" font-size="12" text-anchor="middle">(SUNLU S4)</text>
<rect class="box" x="386" y="36" width="150" height="58" rx="8" stroke-width="1.5"/>
<text x="461" y="56" font-size="12" text-anchor="middle">Airtight bin</text>
<text x="461" y="74" font-size="12" text-anchor="middle">+ desiccant</text>
<rect class="box" x="566" y="36" width="150" height="58" rx="8" stroke-width="1.5"/>
<text x="641" y="56" font-size="12" text-anchor="middle">Printer / AMS</text>
<text x="641" y="74" font-size="12" text-anchor="middle">+ desiccant</text>
<line class="data" x1="156" y1="65" x2="192" y2="65" stroke-width="2.5"/>
<polygon points="192,65 184,61 184,69" style="fill:var(--accent)"/>
<line class="wire" x1="346" y1="65" x2="382" y2="65" stroke-width="2"/>
<polygon points="382,65 374,61 374,69" style="fill:var(--ink)"/>
<line class="wire" x1="536" y1="65" x2="562" y2="65" stroke-width="2"/>
<polygon points="562,65 554,61 554,69" style="fill:var(--ink)"/>
</svg>
<figcaption>Dry it once, then keep it dry — a sealed bin with desiccant, and desiccant living in the AMS too.</figcaption>
</figure>

### 1. Dry it — an active dryer
An active dryer heats and circulates air to pull moisture back out. I use the
**[SUNLU S4](../picks.html#3d-printing)** — 4 spools at once, 3 circulation fans, up
to 70°C, with a humidity readout so you can watch it drop. You can also print
straight from it, which is the move for TPU and nylon.

Do not choose a drying cycle from the material name alone. Follow the filament maker's instructions for the exact formulation, check the spool's temperature limit, and confirm the dryer can safely provide that cycle. A dryer that cannot reach the specified conditions is not a substitute for a suitable one.

[Prusa's drying guidance](https://help.prusa3d.com/article/drying-filament_332086) distinguishes filament formulations and spool versions. Its settings are for its materials; they are not a universal recipe for every brand. Follow the dryer manual for loading, airflow and placement.

### Before buying a dryer

- **Keep what works:** if your material prints reliably and is stored appropriately, buying a larger dryer is not automatically the next step.
- **Match the job:** check the number and dimensions of spools you actually use, the required cycle, and the supported feed path if printing from the dryer.
- **Separate diagnosis from shopping:** stringing and rough surfaces can have other causes. Save the slicer profile and compare one change at a time.
- **Treat the readout as context:** a chamber humidity reading describes conditions near the sensor; it is not a direct measurement of water inside the filament.

### 2. Store it — an airtight bin + desiccant
Once dry, keep it dry. A gasketed **[airtight bin](../picks.html#3d-printing)** with
a scoop of desiccant is all it takes. I use **[Fonday rechargeable silica-gel
beads](../picks.html#3d-printing)** — they're orange and turn green when spent, so
you can see at a glance when to recharge them. Recharge them only according to the exact desiccant product instructions, including its container limits. Do not assume a filament-drying cycle is suitable for desiccant regeneration.

### 3. Keep desiccant in the AMS
Check the exact AMS or feeder model: storage and active-drying capabilities differ. Desiccant helps control the storage environment but does not replace a specified active drying cycle. Follow that model's instructions for desiccant placement and replacement.

## The routine that keeps prints clean

1. Check the new spool and its material instructions; dry it when the documented use requires it.
2. Store dried spools in a sealed bin with desiccant.
3. Check storage conditions and the exact feeder's desiccant instructions.
4. Regenerate or replace desiccant using its own product instructions.

Keep a short log of the material, drying cycle, storage conditions and print profile. Moisture control is one part of diagnosis; it does not guarantee that a print defect disappears.

## Gear used

- [SUNLU S4 filament dryer](../picks.html#3d-printing) — the active dryer
- [Fonday rechargeable silica-gel desiccant](../picks.html#3d-printing) — bins + AMS
- [Airtight storage bins](../picks.html#3d-printing) — sealed storage
- The rest of my [3D-printing picks](../picks.html#3d-printing)

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost to
you. This is the exact drying/storage setup I run.*

## Optional shopping checklist

Check the filament maker’s drying temperature and time, spool temperature limit, dryer capacity and ventilation instructions. Buy only what your existing setup lacks; sealed storage helps keep already-dried material dry.

**Affiliate disclosure:** As an Amazon Associate I earn from qualifying purchases. These are Amazon search links, not guarantees of stock, price, seller quality or compatibility.

- [SUNLU S4 listings on Amazon](https://www.amazon.com/s?k=SUNLU+S4+filament+dryer&tag=homeforge0a-20)
- [Rechargeable silica-gel desiccant on Amazon](https://www.amazon.com/s?k=rechargeable+silica+gel+desiccant&tag=homeforge0a-20)
- [Airtight filament storage bins on Amazon](https://www.amazon.com/s?k=airtight+filament+storage+bins&tag=homeforge0a-20)


*Editorial review September 26, 2026: replaced generic drying ranges with exact-material/spool checks and clarified storage, feeder and desiccant limits. Existing owner equipment notes are not comparative performance tests.*
