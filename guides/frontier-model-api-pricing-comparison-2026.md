# What a heavy AI workflow actually costs across Claude, GPT, Gemini, and Grok (2026)

Sticker-price-per-million-tokens numbers are easy to find and easy to misread. The
number that actually matters is what a real request costs once you factor in each
vendor's context-window pricing cliffs — and three of the four frontier models have
one. Here's the arithmetic, using each vendor's own published rate card (see the
[frontier model comparison](frontier-model-comparison-september-2026.md) for sources).

### The rate cards
| Model | Input / output per 1M tokens | Long-context penalty |
|---|---|---|
| Claude Fable 5.1 | $10 / $50 (cache reads $0.25/M) | None — flat rate across the full 1M window |
| GPT-6 Astra | $10 / $50 (cache reads $1.00/M, cache writes $12.50/M) | 2x input/cache, 1.5x output above 272K input tokens — applied to the whole request |
| Gemini 3.8 Flash | $0.75 / $3.75 | None published |
| Grok 4.6 | $2 / $6 | 2x on both input and output above 200K input tokens — applied to the whole request |

### Two illustrative requests
These token counts are made up for illustration, not measured from a real run — but
the per-token math is exact from the rate cards above, with no caching applied.

**A single research/analysis request — 200K input, 20K output tokens** (under every
vendor's pricing cliff):

| Model | Cost |
|---|---|
| Claude Fable 5.1 | $2.00 + $1.00 = **$3.00** |
| GPT-6 Astra | $2.00 + $1.00 = **$3.00** |
| Gemini 3.8 Flash | $0.15 + $0.075 = **$0.225** |
| Grok 4.6 | $0.40 + $0.12 = **$0.52** |

**A long agentic session — 400K input, 40K output tokens** (past Grok's 200K cliff
*and* Astra's 272K cliff):

| Model | Cost |
|---|---|
| Claude Fable 5.1 | $4.00 + $2.00 = **$6.00** |
| GPT-6 Astra | $8.00 (2x) + $3.00 (1.5x) = **$11.00** |
| Gemini 3.8 Flash | $0.30 + $0.15 = **$0.45** |
| Grok 4.6 | $1.60 (2x) + $0.48 (2x) = **$2.08** |

The gap between the two scenarios is the whole point: doubling your input tokens
should roughly double your bill. For GPT-6 Astra it more than tripled (a request 2x
the size cost 3.7x as much) because the penalty rate kicked in and applied to the
entire request, not just the tokens past the threshold. Grok 4.6 shows the same
pattern at a smaller scale. Claude and Gemini scaled linearly because neither has a
published cliff.

**Practical takeaway:** if you're running long-context agent loops — a coding agent
re-reading a large repo, a research assistant chewing through a big document set —
know exactly where your typical request sits relative to 200K and 272K tokens before
you pick a model on sticker price alone. A model that looks cheaper per token can get
expensive fast once your prompts cross its cliff.

### Caching changes the calculus — but not evenly
If your workload re-sends the same long context repeatedly (a coding agent re-reading
the same repo on every turn), the cache-read rate matters more than the raw input
price. Claude's cache-read rate ($0.25/M) is the cheapest of the frontier models here
by a wide margin — GPT-6 Astra's cache read is $1.00/M, with a $12.50/M cache-*write*
cost that only pays off if you get many reads per write. Neither Gemini nor Grok
published a separate cache rate in the sources we found for this piece — check the
current API docs before assuming standard pricing applies to cached tokens.

For context: this is also where open-weight models pull dramatically ahead on cost.
DeepSeek V4.1 Flash's off-peak cache-hit input rate is about $0.003/M — roughly two
orders of magnitude below any frontier model's cache rate here — because DeepSeek is
explicitly optimizing that price for exactly this kind of repetitive agentic traffic.
See the [open-weight rivals comparison](deepseek-v4-1-flash-vs-open-weight-rivals-2026.md)
and the [frontier-vs-open-weight decision guide](frontier-vs-open-weight-decision-guide-2026.md)
for when that trade-off is worth taking.

### Bottom line
For short, one-off requests under every vendor's cliff, Gemini 3.8 Flash is the
cheapest frontier option by a wide margin, and Grok 4.6 is the mid-priced value pick.
Once your workload runs long-context agent loops routinely, model your actual token
distribution against each vendor's cliff before committing — GPT-6 Astra in
particular can cost far more than its sticker price suggests if your prompts commonly
land north of 272K tokens.

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*See also: [Managing Claude & ChatGPT](managing-claude-and-chatgpt.md).*
*Part of [HomeForge](../README.md).*
