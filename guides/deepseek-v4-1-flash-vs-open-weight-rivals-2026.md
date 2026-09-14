# DeepSeek V4.1 Flash vs. the other open-weight giants of 2026

DeepSeek V4.1 Flash didn't ship into an empty field. By September 2026, five different
labs had released trillion-parameter-class (or near it) MoE models with open or
open-ish weights, most converging on the same playbook: ~1M-token context, native
multimodal input, and mixture-of-experts sparsity to keep inference cheap despite a
huge parameter count. Here's how V4.1 Flash actually stacks up against that field —
not the marketing bullet points, the numbers.

### The class it's competing in
- **DeepSeek V4.1 Flash** — Sept 10, 2026. New "Causal Encoder-Decoder" architecture,
  DeepSeek's first Flash model with native vision.
- **DeepSeek V4 Pro** — DeepSeek's own larger sibling, released earlier in 2026.
- **Kimi K3** (Moonshot AI) — July 16, 2026, weights on Hugging Face July 27.
- **GLM-5.3-Flash** (Zhipu / Z.ai) — Aug 26, 2026.
- **Qwen3.8-Max** (Alibaba) — API Aug 3, 2026; open weights (as Qwen3.8-2.4T-A95B)
  Aug 12, 2026 — the first time Alibaba has open-sourced a Max-class Qwen model.

### Head-to-head
| Model | Total / active params | Context window | License | Price (input / output per 1M tokens) |
|---|---|---|---|---|
| **DeepSeek V4.1 Flash** | ~552B / ~8B–16B | 1M in, 384K out | MIT (open weights) | ~$0.003–$0.15 in (off-peak, cache hit/miss) · $0.60 out |
| DeepSeek V4 Pro | ~1.6T / ~49B | 1M | MIT (open weights) | ~$0.87–$1.30 in · ~$1.74–$2.60 out (provider-dependent) |
| Kimi K3 | 2.8T / 104B | 1M in/out | Modified-MIT "Kimi K3 License" (revenue-gated carve-out above $20M/yr MaaS revenue) | $3 in ($0.30 cache-hit) · $15 out |
| GLM-5.3-Flash | 320B / 18B | 1.3M in, 131K out | MIT (open weights) | $0.15 in · $0.50 out (list; launch promo $0.075/$0.25 ended Sept 9) |
| Qwen3.8-Max (open weights) | 2.4T / ~95B | 1M | Custom "Qwen3.8-Max License" (modified MIT; revenue-gated carve-outs) — hosted API version priced separately at $2 in / $6 out | — |

*Sources: DeepSeek V4.1 Flash and V4 Pro pricing/specs from
[Dataconomy](https://dataconomy.com/2026/09/11/deepseek-v4-1-flash-ultralow-token-pricing/),
[OpenRouter](https://openrouter.ai/deepseek/deepseek-v4.1-flash), and
[llm-stats.com](https://llm-stats.com/models/deepseek-v4-pro-0813); Kimi K3 from
[llm-stats.com](https://llm-stats.com/models/kimi-k3) and
[OpenRouter](https://openrouter.ai/moonshotai/kimi-k3); GLM-5.3-Flash from
[Artificial Analysis](https://artificialanalysis.ai/models/glm-5-3-flash) and
[models.dev](https://models.dev/models/zhipuai/glm-5.3-flash/); Qwen3.8-Max from
[llm-stats.com's open-weights writeup](https://llm-stats.com/blog/research/qwen3-8-max-open-weights)
and [OpenRouter](https://openrouter.ai/qwen/qwen3.8-max-0902). Some outlets disagree on
whether the Qwen3.8-Max open weights ship under the custom license or plain Apache 2.0 —
check the Hugging Face repo's own license file before you build on it.*

### What the benchmarks actually say
Every lab here reports its own numbers on its own harness, so treat cross-model
comparisons as directional, not exact. The one benchmark enough of them report to be
worth lining up is **GPQA Diamond**: Kimi K3 leads the open-weight field at roughly
93.5%, with DeepSeek V4.1 Flash close behind at 90.9%. DeepSeek's other reported
numbers for V4.1 Flash (DeepSWE v1.1, Terminal-Bench 4.0, CyberGym, Automation-Bench,
Agents' Last Exam) are DeepSeek's own and haven't been independently reproduced yet —
worth a grain of salt until third-party evals catch up.

### Picking one
- **Cheapest to actually run at scale:** GLM-5.3-Flash. Smallest model here (18B
  active), plain MIT license with no revenue carve-outs found, and list pricing well
  under $1/M tokens both ways.
- **Highest raw open-weight capability today:** Kimi K3, if its GPQA lead holds up —
  but read the Kimi K3 License before building a paid product on it; the $20M/year
  MaaS carve-out matters if you're not a hobbyist.
- **Best fit for cached, bursty agentic workloads:** DeepSeek V4.1 Flash. The
  off-peak/cache-hit pricing tiers are clearly built for agent loops that hammer the
  same context repeatedly — it's a bad fit if your traffic is steady and peak-hours-only.
- **Most total horsepower, most total cost:** DeepSeek V4 Pro and Qwen3.8-Max sit at
  the expensive end of this table (1.6T–2.4T total parameters, $2–$6/M-token API
  pricing) — pick these when the task genuinely needs the extra capacity, not by default.

### Can you self-host any of these?
Not on the kind of hardware in the [local-AI picks](../README.md#-ai--local-llms).
Every model in this table is 300B+ total parameters, and MoE sparsity only reduces
*active* compute per token — you still need enough combined VRAM/RAM to hold the full
expert set. Realistically these are rented-cloud or API-provider models (OpenRouter,
the vendor's own API, or a many-GPU box you rent by the hour), not something you pull
with Ollama on a homelab box. If self-hosting a large open-weight model matters to you,
GLM-5.3-Flash's smaller footprint (320B total, 18B active) is the one worth checking
against your budget first.

### Bottom line
None of these five have a meaningful independent track record yet — they all shipped
within about eight weeks of each other. On paper, DeepSeek V4.1 Flash's pitch is price
and architecture novelty rather than raw benchmark supremacy: it undercuts Kimi K3 and
Qwen3.8-Max on cost by an order of magnitude for cached workloads, while trailing Kimi
K3 slightly on the one benchmark that's roughly comparable across vendors. If cost per
token is what you're optimizing, it's worth a trial; if you need the single most capable
open-weight model regardless of price, Kimi K3's numbers currently lead. Re-check this
once independent evals (not vendor-reported ones) are available for all five.

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*See also: [Model Watch: DeepSeek V4.1 Flash](model-watch-deepseek-v4-1-flash-2026-09-14.md),
[how these architectures actually work](how-2026-open-weight-models-actually-work.md),
[what it really takes to self-host one](what-it-takes-to-self-host-a-2026-open-weight-model.md),
[the license fine print](open-weight-ai-licenses-2026-explained.md), and
[Best way to run a local LLM](best-way-to-run-a-local-llm.md).*
*Part of [HomeForge](../README.md).*
