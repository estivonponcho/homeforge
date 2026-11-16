# Claude Fable 5.2 — what actually changed, and whether you should care

**Released:** November 9, 2026 · **Maker:** Anthropic · **Type:** chat / reasoning / multimodal

### The one-line take
> A cheaper, faster point release with a real coding bump — not the generational leap "5.2" might suggest, and Anthropic's own numbers show Opus 5.5 still winning some of the same benchmarks.

### What's new
- Anthropic shipped **Claude Fable 5.2** alongside a restricted sibling, **Claude Mythos 5.2** — same underlying model, but Mythos access is limited to organizations vetted through Anthropic's Cyber and Life Sciences Verification Programs.
  ([9to5Mac](https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here/), [SD Times](https://sdtimes.com/?p=61724))
- API pricing dropped about 20% versus Fable 5.1: multiple outlets put it at **$8 per million input tokens and $40 per million output tokens**, down from $10/$50. A new "Fast mode" is priced at roughly double the standard rate in exchange for Anthropic's claimed up-to-2.5x faster token generation.
  ([TechEnclave](https://techenclave.com/news/items/anthropic-releases-claude-fable-5-2-at-lower-api-prices), [VKTR](https://www.vktr.com/ai-platforms/claude-fable-52-and-mythos-52-arrive-faster-and-cheaper/))
- Context window: **1M tokens**, with up to 128K tokens of output. Available on Anthropic's own API plus AWS, Google Cloud, and Microsoft Azure.
  ([llm-stats.com launch coverage](https://llm-stats.com/blog/research/claude-fable-5-2-launch))
- Anthropic says standard (non-Fast) output is up to 30% faster than Fable 5.1, with gains claimed in coding, reasoning, and vision tasks. The company also claims more than 90% of code changes merged into its own internal codebase are now written by Claude with human guidance — a claim about Anthropic's internal dogfooding, not an independent measurement.
  ([TheNewStack](https://thenewstack.io/anthropic-fable-coding-upgrade/))
- Benchmarks are mixed, not a clean sweep: one tracker lists Fable 5.2 (Max config) at 65 on the Artificial Analysis Intelligence Index v5.0.1 and separately notes Opus 5.5 outperforms it on two of Anthropic's own internal ratings. Other reported figures — 74.2% on Humanity's Last Exam (with tools), 69.9% on FrontierSWE V2, 49.1% on FrontierCode 2.0 — come from lab/launch material and third-party aggregators rather than independently reproduced evals, so treat them as **unconfirmed** until someone outside Anthropic checks them.
  ([llm-stats.com](https://llm-stats.com/blog/research/claude-fable-5-2-launch))

### Who it's for
- **Use it if…** you're already on the Fable line and want the same quality at a 20% lower sticker price, or you specifically need the 1M-token context window with the new Fast mode for latency-sensitive agent work.
- **Skip it if…** you're chasing the absolute top benchmark score — several sources note Opus 5.5 still leads Fable 5.2 on some of Anthropic's own internal comparisons, so this reads as a cost/speed-focused refresh more than a capability leap.

### How it compares
| | Claude Fable 5.2 | Previous / rival |
|---|---|---|
| Strength | ~20% cheaper than Fable 5.1, Fast mode for latency, 1M-token context | Opus 5.5: ahead on some of Anthropic's own internal benchmarks |
| Weakness | Not a clean benchmark sweep; some scores are vendor/aggregator-reported only | — |
| Price | $8/M input, $40/M output (Fast mode ~2x that) | Fable 5.1: $10/M input, $50/M output |
| Context | 1M tokens in / 128K tokens out | Varies by model |

### Can you run it yourself?
No — this is a closed, hosted model. It's available through Anthropic's API and the major cloud marketplaces (AWS, Google Cloud, Azure); there are no downloadable weights. If you're looking for something to self-host, see the [local-AI picks](../README.md#-ai--local-llms) instead.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
