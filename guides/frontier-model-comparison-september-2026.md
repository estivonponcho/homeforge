# The frontier AI model landscape (September 2026): Claude, GPT, Gemini, and Grok compared

Four labs, four different bets, all reshuffled within about five weeks of each other:
Grok 4.6 (Aug 12), Claude Fable 5.1 (Sept 1), Gemini 3.8 Flash (Sept 2), and GPT-6
Astra (Sept 4). Here's what actually changed, with the numbers each vendor put on the
record — not the launch-day hype.

### One asymmetry worth flagging up front
Google's actual flagship "Pro" tier — Gemini 3.1 Pro — dates back to February 2026 and
hasn't been refreshed. Gemini 3.8 Flash is Google's newest and most capable *currently
shipping* model, but it's positioned as a workhorse/agentic tier, not a like-for-like
flagship against Fable 5.1, GPT-6 Astra, or Grok 4.6. It's the fair comparison point
today because it's what's actually new — just don't read the table below as "Google's
best vs. everyone else's best."

### Head-to-head
| Model | Maker | Released | Context window | Max output | Price (input / output per 1M tokens) |
|---|---|---|---|---|---|
| **Claude Fable 5.1** | Anthropic | Sept 1, 2026 | 1M | 128K | $10 / $50 (cache reads $0.25/M) |
| Claude Mythos 5.1 *(restricted access)* | Anthropic | Sept 1, 2026 | 1M | 128K | same as Fable 5.1 |
| **GPT-6 Astra** | OpenAI | Sept 4, 2026 | 1.05M | 128K | $10 / $50 (2x input/cache, 1.5x output above 272K-token prompts) |
| **Gemini 3.8 Flash** | Google | Sept 2, 2026 | 1M | 64K | $0.75 / $3.75 |
| **Grok 4.6** | xAI | Aug 12, 2026 | 500K | — | $2 / $6 (doubles to $4/$12 above 200K-token prompts) |

*Sources: Claude Fable 5.1 / Mythos 5.1 from [MarkTechPost](https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/)
and [llm-stats.com](https://llm-stats.com/models/claude-fable-5-1); GPT-6 Astra from
[llm-stats.com](https://llm-stats.com/models/gpt-6-astra) and
[OpenRouter](https://openrouter.ai/openai/gpt-6-astra); Gemini 3.8 Flash from
[eesel AI](https://www.eesel.ai/blog/gemini-3-8-flash) and
[llm-stats.com](https://llm-stats.com/models/gemini-3.8-flash); Grok 4.6 from
[kingy.ai](https://kingy.ai/blog/grok-4-6-price-benchmarks-api-cursor-context-window/)
and [OpenRouter](https://openrouter.ai/x-ai/grok-4.6).*

### What the benchmarks say — and don't
Every lab publishes its own suite, so a single "who's smartest" number doesn't really
exist. Here's what's directly comparable and what isn't:

- **GPQA Diamond** is the one benchmark three of the four vendors report: **Grok 4.6 at
  94.9%**, **GPT-6 Astra at 89.5%**. Anthropic didn't publish a GPQA Diamond number for
  Fable 5.1 in its own materials — its headline figure is Terminal-Bench-Science 0.1
  (52.6%, vs. 24.7% for the previous Fable 5 and 29.0% for Opus 5).
- **Agentic/coding evals** aren't comparable across vendors either: GPT-6 Astra reports
  76.2 on its own "Coding" index; Grok 4.6 reports 76.8 on its own "Coding Index";
  Gemini 3.8 Flash reports 73.7% on DeepSWE v1.1. These are three different tests with
  similar-sounding names — don't treat them as the same number.
- **Third-party normalization exists** — [Artificial Analysis](https://artificialanalysis.ai/models)
  runs its own Intelligence Index across vendors on a shared methodology, and as of this
  writing it puts Claude Fable 5.1 at the top of the field with GPT-6 Astra close behind,
  and Grok 4.6 further back but priced far lower. Check their live leaderboard for
  current scores rather than trusting a snapshot here — it's continuously re-run and the
  exact point values move.
- OpenAI's more eye-catching numbers (FrontierMath Tier 4 at 97.6%, ARC-AGI-3 at 99.9%,
  ExploitBench at 100%) are all OpenAI-reported and worth a grain of salt until
  reproduced independently, same as every other vendor's headline claim.

### Who it's for
- **Claude Fable 5.1** — the current pick if you want the model with the best
  independent (Artificial Analysis) intelligence ranking today, and you're already
  paying premium per-token rates for other reasons (long agentic sessions, coding).
  Mythos 5.1 is functionally the same model with looser safety rails, gated to vetted
  cyberdefense/life-sciences orgs — not a general option.
- **GPT-6 Astra** — closely competitive with Fable 5.1 on third-party rankings, with a
  slightly larger context window, but watch the pricing cliff: prompts over 272K
  tokens double in cost. Fine for most single-turn work, expensive for very long
  agentic contexts that creep past that line.
- **Gemini 3.8 Flash** — by far the cheapest of the four at $0.75/$3.75, and Google's
  own numbers show real gains over 3.7 Flash on agentic/coding evals. The honest
  caveat: it's a workhorse-tier model, not Google's best possible model, because
  there hasn't been a Pro/Ultra refresh since February.
- **Grok 4.6** — the value pick among the "genuinely frontier" models: roughly 60%
  cheaper than Claude or GPT at list price, and it actually leads on GPQA Diamond.
  Smallest context window here (500K, doubling in price above 200K) is the real
  trade-off.

### Bottom line
On paper, and pending independent verification of every vendor's own numbers: Claude
Fable 5.1 and GPT-6 Astra are trading blows at the top on third-party rankings, Grok
4.6 is the best value if you don't need the largest context window, and Gemini 3.8
Flash is the one to reach for when cost matters more than being at the absolute
frontier — which, for a lot of real workloads, it does. See the
[pricing breakdown](frontier-model-api-pricing-comparison-2026.md) for what this
actually costs at real usage volumes, and the
[frontier-vs-open-weight guide](frontier-vs-open-weight-decision-guide-2026.md) if
you're also considering a self-hosted or open-weight model instead.

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*See also: [Managing Claude & ChatGPT](managing-claude-and-chatgpt.md) and
[DeepSeek V4.1 Flash vs. the other open-weight giants of 2026](deepseek-v4-1-flash-vs-open-weight-rivals-2026.md).*
*Part of [HomeForge](../README.md).*
