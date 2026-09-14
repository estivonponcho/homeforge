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

Rough temps and times (start conservative; the S4 tops out at 70°C):

| Material | Dryer temp | Time |
|---|---|---|
| PLA | 45–55°C | 4–6 h |
| PETG | 55–65°C | 4–6 h |
| TPU | 45–55°C | 4–8 h |
| ABS / ASA | 65–70°C | 4–6 h |
| Nylon (PA) | 70°C | 8–12 h |

### 2. Store it — an airtight bin + desiccant
Once dry, keep it dry. A gasketed **[airtight bin](../picks.html#3d-printing)** with
a scoop of desiccant is all it takes. I use **[Fonday rechargeable silica-gel
beads](../picks.html#3d-printing)** — they're orange and turn green when spent, so
you can see at a glance when to recharge them. Bake them dry (or run them in the
dryer) and reuse for years.

### 3. Keep desiccant in the AMS
The AMS isn't sealed enough to dry filament, but a pod of the same rechargeable
desiccant inside it keeps loaded spools from creeping back up in humidity between
prints. Swap or recharge when the beads turn green.

## The routine that keeps prints clean

1. New spool → dry it before the first big print.
2. Store dried spools in a sealed bin with desiccant.
3. Keep desiccant in the AMS and check the color monthly.
4. Recharge green beads in the dryer and reuse.

That's it — a one-time dryer purchase plus a few dollars of reusable desiccant, and
"why is this stringy?" mostly disappears.

## Gear used

- [SUNLU S4 filament dryer](../picks.html#3d-printing) — the active dryer
- [Fonday rechargeable silica-gel desiccant](../picks.html#3d-printing) — bins + AMS
- [Airtight storage bins](../picks.html#3d-printing) — sealed storage
- The rest of my [3D-printing picks](../picks.html#3d-printing)

---

*HomeForge is reader-supported; some links are affiliate links, at no extra cost to
you. This is the exact drying/storage setup I run.*
