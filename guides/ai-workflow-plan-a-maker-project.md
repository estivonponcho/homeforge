# An AI workflow for planning a maker project without buying the wrong parts

This workflow turns a rough build idea into a practical plan, a compatibility-checked parts list, and a definition of done. It works for ESP32 projects, Raspberry Pi builds, Home Assistant devices, and small homelab upgrades.

The important part is not asking AI to invent the whole project. Give it your real constraints, make it expose uncertainty, and verify every hardware claim before money or voltage is involved.

## What you need before prompting

Write down what is already true:

- The outcome you want in one sentence.
- Hardware you already own.
- Your budget and deadline.
- Required protocols, voltages, ports, and software.
- Things you refuse to depend on, such as a cloud account or Wi-Fi.
- How you will know the build works.

A photo, model number, manual, or existing configuration is more useful than a long description from memory.

## Step 1: turn the idea into a build brief

Use this prompt:

```
Act as a cautious maker-project planner.

Goal:
[Describe the finished result in one sentence.]

What I already own:
[List exact models and quantities.]

Constraints:
[Budget, protocols, dimensions, power, local-only requirements, deadline.]

Produce:
1. A short definition of done.
2. The smallest viable version of the project.
3. A block diagram showing the major components and connections.
4. A list of assumptions and unknowns that must be verified.
5. Three likely failure points.

Do not recommend products yet. Do not invent specifications. Mark anything that
requires a datasheet or live source as VERIFY.
```

This separates the design problem from shopping. It also reveals whether the first version can be much smaller than the idea in your head.

## Step 2: build a compatibility matrix

Now provide manuals, product pages, or datasheet excerpts for the components under consideration.

```
Using only the supplied source material, create a compatibility matrix.

For every connection, show:
- Source component and port or pin
- Destination component and port or pin
- Voltage and current requirements
- Protocol or signal type
- Evidence from the supplied source
- Status: compatible, incompatible, or unverified

If the sources do not establish compatibility, say unverified. Do not infer that
matching connector shapes mean matching voltage, polarity, or protocol.
```

Do not buy anything while an essential row is marked unverified.

## Step 3: create the shopping list

Once the matrix is clean, ask for three groups:

1. Required parts.
2. Parts you already own.
3. Optional upgrades that can wait.

Require an explanation for every item. A part that cannot be tied to a step in the plan does not belong in the cart.

For HomeForge examples, browse the [curated parts list](../picks.html) after the design is settled, not before.

## Step 4: make the build testable

Ask the model to convert the plan into checkpoints:

```
Turn this plan into independently testable stages. Each stage must include:
- The smallest assembly or configuration change
- A test with a clear pass condition
- The evidence I should save
- A rollback step
- What not to connect or change yet
```

For an ESP project, the first checkpoint might only prove that the board boots and joins the network. For a homelab change, it might confirm the backup before any upgrade begins.

## Step 5: keep a tiny decision log

After each session, record:

- What changed.
- What passed or failed.
- What you measured.
- What you decided and why.
- The next smallest test.

Feed that log into the next prompt. This prevents the model from rebuilding its understanding from scattered chat messages.

## Human checks that stay mandatory

- Confirm voltage, polarity, current, and pin assignments from authoritative documentation.
- Back up configurations before changing them.
- Remove passwords, API keys, addresses, and device identifiers before sharing logs.
- Stop if the plan touches mains voltage, life-safety equipment, batteries without protection, or anything outside your experience.
- Treat product availability and prices as live information that must be checked again.

The useful outcome is not a clever prompt. It is a smaller first build, fewer incompatible purchases, and a record you can turn into a real project guide later.

*Related: [Prompting patterns that actually work](prompting-patterns.md) and the [ESP thermal-printer build](../projects/esp-thermal-printer.md).*
