# Turn a hand sketch into a scaled conceptual dock plan with AI

A chat model can help organize requirements and generate drawing code, but it should not guess dimensions or present a conceptual sketch as engineered work. The reliable workflow is to separate **facts**, **geometry**, and **verification**.

## What this workflow is for

Use it to communicate an early idea for a dock, lift, seawall, walkway, or shoreline layout. A conceptual plan can help an owner discuss options and catch missing information before paying for formal design work.

It is **not** a survey, engineering drawing, construction document, environmental review, or permit set. Shoreline work can involve property boundaries, setbacks, utilities, navigation, structural loads, flood conditions, environmental rules, and local approvals. A qualified professional and the relevant authorities must verify those items.

## Start with a measurement sheet

Record every known dimension instead of asking AI to infer scale from a photograph.

| Item | Measurement | Source | Confidence |
|---|---:|---|---|
| Known shoreline segment | ___ ft | survey / field measure | high / medium / low |
| Dock length | ___ ft | proposed | proposed |
| Dock width | ___ ft | proposed | proposed |
| Lift length | ___ ft | manufacturer | high |
| Lift width | ___ ft | manufacturer | high |
| Distance from reference corner | ___ ft | survey / field measure | high / medium |
| Water direction | note | observation | contextual |

Use one authoritative known dimension as the scale reference. A survey dimension is better than measuring pixels from a photo.

## Convert the sketch into structured facts

Give the model a list like this:

```text
Drawing type: conceptual plan view
Units: feet
Known shoreline segment: 100
Dock: 40 long x 6 wide
Dock center: 42 feet from the left shoreline reference
Lift: 12 long x 10 wide
Lift attaches to the right side of the dock, 8 feet from the outer end
North arrow: up
Unknowns: property boundary, water depth, setbacks, utilities, structural loads
Required label: CONCEPT ONLY — NOT ENGINEERED — NOT FOR CONSTRUCTION OR PERMITTING
```

Ask the model to repeat the facts and unknowns before it draws anything. If it changes a number, stop and correct the source data.

## Generate geometry, not a picture

Ask for SVG or another vector format. Vector coordinates can be checked mathematically and imported into many design tools. An image generator may create an attractive illustration, but it cannot be trusted to preserve scale.

The useful rule is:

```text
pixels = real-world feet × pixels per foot
```

If the drawing uses 8 pixels per foot, a 40-foot dock must be 320 pixels long and a 6-foot width must be 48 pixels.

## Run four verification checks

1. **Dimension check:** calculate each drawn length from its coordinates and scale.
2. **Reference check:** verify the known shoreline dimension independently.
3. **Relationship check:** confirm which side each lift, walkway, or structure attaches to.
4. **Unknowns check:** make sure missing survey, engineering, environmental, and permitting facts remain visibly marked as unknown.

Do not accept “looks about right” as scale verification.

## Use the HomeForge starter tool

The [Conceptual Dock Plan Builder](../tools/concept-site-plan.html) creates a simple scaled SVG from explicit dimensions. It is intentionally limited. The output is a conversation aid, not a design recommendation.

Enter a shoreline length, dock dimensions, lift dimensions, and an offset. The tool converts feet to pixels consistently, draws a scale bar, lists the supplied dimensions, and exports the result as SVG.

## A reusable AI prompt

```text
Act as a drafting assistant for a conceptual, non-engineered plan view.

First, return two tables: KNOWN FACTS and UNKNOWNS. Do not infer any missing measurement. Ask for one authoritative reference dimension if none is supplied.

After I approve the tables, produce SVG using one consistent pixels-per-foot scale. Put all dimensions and geometry in a machine-readable JSON block before the SVG. Include a scale bar, north arrow, dimension labels, and this exact notice:

CONCEPT ONLY — NOT ENGINEERED — NOT FOR CONSTRUCTION OR PERMITTING

After generating the SVG, calculate the real-world dimensions back from the SVG coordinates and report any mismatch. Do not provide structural, electrical, geotechnical, environmental, boundary, setback, or permitting conclusions.
```

## Where AI helps and where it stops

AI is useful for turning notes into a consistent input sheet, producing editable SVG, checking arithmetic, creating revision logs, and listing unanswered questions. It should never invent site measurements, certify boundaries, calculate safety-critical loads without professional review, or imply that a conceptual sketch is approved for construction.

The result should make the next professional conversation clearer, not replace it.

---

*This material is educational and is not engineering, surveying, legal, environmental, or permitting advice.*
