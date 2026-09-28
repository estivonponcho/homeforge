# GPT-6 Sol & Luna — what actually changed, and whether you should care

OpenAI's mid-tier and budget GPT-6 models, not the Astra flagship, but the pair
that most API bills will actually run on — and the pricing cut is the real
story here, not a benchmark leap.

**Released:** September 22, 2026 · **Maker:** OpenAI · **Type:** closed, multimodal (text + image input, text output)

### The one-line take
> Sol and Luna aren't trying to beat Astra — they're trying to make GPT-6-tier reasoning cheap enough to run everywhere, and the price cuts back that up.

### What's new
- Two new tiers below flagship GPT-6 Astra: Sol (mid-tier, for complex coding and
  agentic work) and Luna (low-cost, for focused, high-volume tasks).
  ([OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna/))
- Pricing: Sol is $2 per million input tokens / $10 per million output tokens;
  Luna is $0.10 per million input / $0.50 per million output. Cached input gets a
  90% discount on both ($0.20/M for Sol, $0.01/M for Luna).
  ([VentureBeat](https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more))
- That's roughly a 50% cut from GPT-5.6 promotional pricing overall; Luna's output
  price specifically fell 58%, from $1.20 to $0.50 per million tokens.
  ([VentureBeat](https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more))
- Context window: 1,050,000 tokens on both models, with text and image input and
  text-only output.
  ([llm-stats.com](https://llm-stats.com/models/gpt-6-luna))
- OpenAI's own benchmark claims: on AutomationBench (business-workflow tasks
  across apps), Sol at "xhigh" reasoning effort outperforms Claude Opus 5 at max
  effort while costing about 9% of Opus 5's price per task. On DeepSWE 1.1
  (coding), Sol at max effort scores 68.8% versus 69.9% for Claude Fable 5 at
  xhigh effort, with OpenAI estimating roughly 80% lower cost per task. These are
  OpenAI's own comparisons — worth independent verification before leaning on them.
  ([MarkTechPost](https://www.marktechpost.com/2026/09/22/openai-releases-gpt-6-sol-and-luna-50-cheaper-api-pricing-and-benchmarks/))
- OpenAI says both models show lower rates of misleading claims about their own
  coding work compared to their GPT-5.6 predecessors.
  ([llm-stats.com](https://llm-stats.com/models/gpt-6-luna))

### Who it's for
- **Use it if…** you're running GPT-6-family workloads at volume and the Astra
  flagship price doesn't make sense for the task — Sol for agentic/coding work
  that still needs real reasoning, Luna for high-volume, well-bounded jobs
  (classification, extraction, short-form generation).
- **Skip it if…** you need Astra's top-end capability for a genuinely hard task,
  or you need audio/video input — these two accept text and image only.

### How it compares
| | GPT-6 Sol / Luna | Previous / rival |
|---|---|---|
| Strength | ~50-58% cheaper than GPT-5.6 tier, OpenAI claims cost-per-task wins over Opus 5 and Fable 5 on specific benchmarks | GPT-6 Astra: higher raw capability, much higher price |
| Weakness | Below-flagship models; OpenAI's own comparisons haven't been independently reproduced yet | — |
| Price | Sol: $2/$10 per M in/out; Luna: $0.10/$0.50 per M in/out | GPT-5.6 tier: roughly double on most of these numbers |
| Context | 1.05M tokens | Varies by rival, often smaller |

### Can you run it yourself?
No — closed, API-only models, not open-weight, so they're not a fit for the
[local-AI picks](../README.md#-ai--local-llms). Access is through OpenAI's API
under the Responses and Chat Completions endpoints; check your existing
ChatGPT/API plan for rollout timing.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
