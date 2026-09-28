# Claude Opus 5.5 — what actually changed, and whether you should care

Anthropic's first release since Dario Amodei publicly embraced calls to "pace the
frontier" is a cheaper, faster Opus that matches Fable 5.1 on Anthropic's own
agentic benchmarks — not a capability leap, but a genuinely useful cost cut if
you're running long, cache-heavy agent sessions.

**Released:** September 22, 2026 · **Maker:** Anthropic · **Type:** closed, multimodal, agentic/coding frontier model

### The one-line take
> Same tier as Fable 5.1 on Anthropic's numbers, noticeably cheaper to run — this is a cost-and-speed release, not a new capability tier.

### What's new
- Pricing dropped: $4 per million input tokens and $20 per million output tokens,
  a 20% cut from Opus 5. Cache-read pricing fell 60%, to $0.20 per million tokens,
  and cache-write pricing fell 20%, from $6.25 to $5 per million tokens.
  ([TechRepublic](https://www.techrepublic.com/article/news-anthropic-claude-opus-5-5-pricing-performance/))
- Anthropic says the combined pricing changes cut the cost of typical long-running,
  cache-heavy workloads by around 40%, and that the model generates output more
  than 30% faster than Opus 5.
  ([TechRepublic](https://www.techrepublic.com/article/news-anthropic-claude-opus-5-5-pricing-performance/))
- Anthropic's own benchmark numbers: 66.4% on Terminal-Bench 4.0, ahead of GPT-6
  Astra's reported 57.9%; 1846 Elo on GDPval-AA v2.1 across 44 professions,
  ahead of both Fable 5.1 and Opus 5. Treat these as Anthropic-reported until
  independently reproduced.
  ([VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price))
- GitHub's Chief Product Officer Mario Rodriguez said Opus 5.5 used among the
  fewest tokens and steps in GitHub's internal testing, and solved more VS Code
  terminal tasks than Opus 5 while using less than half as many steps.
  ([TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/))
- This is Anthropic's first model release since Amodei called for the industry to
  slow capability progress to match alignment work — worth noting as context, not
  as a technical spec.
  ([Yahoo Finance](https://finance.yahoo.com/technology/article/anthropic-launches-opus-55-its-first-model-since-ceo-amodei-called-for-ai-slowdown-163000869.html))
- Available now via the API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft
  Foundry, plus Claude's Pro, Max, Team, and Enterprise plans (not the free tier).
  ([TechRepublic](https://www.techrepublic.com/article/news-anthropic-claude-opus-5-5-pricing-performance/))
- Sonnet 5.5 and Haiku 5.5 are described as coming "in the coming weeks" with
  similar improvements — unconfirmed timing beyond that.
  ([TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/))

### Who it's for
- **Use it if…** you're already running Opus-tier agent or coding workloads with
  heavy prompt caching (long-running coding sessions, repeated tool-use loops) —
  the cache-read price cut and speed bump compound fast at volume.
- **Skip it if…** you were expecting a jump past Fable 5.1 in raw capability.
  Anthropic is positioning this as matching Fable-level performance at lower
  cost, not beating it outright.

### How it compares
| | Claude Opus 5.5 | Previous / rival |
|---|---|---|
| Strength | 40% cheaper on cache-heavy workloads, 30%+ faster output, matches Fable 5.1 on GDPval-AA v2.1 | Opus 5: higher list price, slower output |
| Weakness | Not a capability jump beyond Fable 5.1 — this is a cost/speed release | — |
| Price | $4/M input, $20/M output, $0.20/M cache read, $5/M cache write | Opus 5: $5/M input, $25/M output, $6.25/M cache write |
| Context | Up to 1M tokens via the API (per Anthropic's platform docs); 200K by default in the Claude Code CLI | Comparable to Opus 5 |

### Can you run it yourself?
No — this is a closed, API/subscription-only model, not open-weight. It's not a
fit for the [local-AI picks](../README.md#-ai--local-llms); if you want that,
look at the open-weight guides on this site instead. For API use, it's live now
across Anthropic's own API and the three major cloud marketplaces listed above.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
