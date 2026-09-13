# Contributing

This list stays good by staying picky. Contributions are welcome, but the bar is
"would I spend my own money on this and tell a friend to?"

## Adding or changing a pick

1. Edit [`data/picks.json`](data/picks.json) — **not** `README.md`. The README
   is generated.
2. Add an object to the `picks` array:

   ```json
   {
     "pillar": "smart-home",              // smart-home | homelab | 3d-printing
     "category": "Sensors & Presence",    // reuse an existing category if you can
     "name": "Product or Project Name",
     "url": "https://official-or-affiliate-link",
     "blurb": "One honest sentence: what it is and when to pick it.",
     "tier": "$",                          // $ | $$ | $$$ | Free | Free / DIY
     "program": "Amazon",                 // where it monetizes, or "None"
     "featured": false                     // true only for the very best in its pillar
   }
   ```

3. Regenerate the README:

   ```bash
   python3 scripts/build.py
   ```

4. Open a PR describing why the pick belongs and whether you have any affiliation
   with the product.

## Rules

- **No pay-for-placement.** A commission never buys a spot.
- **One blurb, one honest sentence.** No marketing copy.
- **Disclose affiliations.** If you make or sell the thing, say so in the PR.
- **Kill your darlings.** If something's been surpassed, propose removing it.
