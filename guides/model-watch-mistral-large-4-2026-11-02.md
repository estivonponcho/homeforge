# Mistral Large 4 ("Le Chonk") — what actually changed, and whether you should care

**Released:** October 29, 2026 (open weights); preview since October 6, 2026 · **Maker:** Mistral AI · **Type:** open-weight, mixture-of-experts

### The one-line take
> Europe's biggest open-weight bet yet — a genuinely trillion-parameter MoE with downloadable weights — but the one fully independent benchmark we could find put it mid-pack, not at the top Mistral claims.

### What's new
- Mistral AI opened a hosted public preview of Large 4 (internally nicknamed "Le Chonk") on
  October 6, 2026 via Mistral Studio and the Mistral API, with open weights promised to follow
  later in the month. Most outlets report the weights actually landed on Hugging Face on
  October 29, 2026, though a couple of sources cite October 27 instead — treat the exact weights
  date as approximate. ([IT Daily](https://itdaily.com/news/innovation/mistral-le-chonk-open-weight/), [aiweekly.co](https://aiweekly.co/alerts/mistrals-1t-parameter-large-4-slated-for-october-31-drop))
- Architecture: a mixture-of-experts model reported at roughly 1 trillion (1.05T) total
  parameters. Sources disagree on active parameters per token — most say 49B, at least one says
  52B — so treat the exact active-parameter figure as **unconfirmed** pending Mistral's own model
  card.
- Context window: Mistral states 1M tokens, but independent measurements differ — Artificial
  Analysis reportedly measured 524,288 tokens on the configuration it tested, and Vals.ai lists
  512K. Mark the full 1M figure as **unconfirmed independently**.
- License: reported as the "Mistral Ecosystem Open-Weight License" — described by one source as
  a modified-MIT-style license permitting commercial use with a carve-out against reselling the
  model as a hosted service. We could not independently confirm the exact license text in this
  pass — check the Hugging Face model card directly before relying on it for a commercial
  deployment.
- Weights are published in FP8 and NVFP4 quantized variants on Hugging Face, and the downloadable
  checkpoint reportedly reflects about three additional weeks of training beyond the October 6
  preview model that shares its name — so the hosted preview and the open weights are not
  necessarily identical.
- Benchmarks are mostly Mistral's own, with the company calling Large 4 the best current
  open-weight model for coding. The clearest independent data point we found: on Cognition's
  FrontierCode 2.0 (a private, human-reviewer-style coding benchmark), Large 4 scored 19.7% —
  the highest of any open-weight model tested there, per Cognition's own reporting. Separately,
  Vals.ai's broader Vals Index ranks it much lower — around #32 of 44 models at 48.05% — which is
  a meaningfully different picture than Mistral's own coding-focused claim. Treat Mistral's
  headline comparisons as vendor-reported until more independent evals land.

### Who it's for
- **Use it if…** you operate or rent multi-GPU, data-center-class infrastructure and want a
  genuinely open-weight, commercially licensed alternative to closed frontier APIs — especially
  if your workload is coding-heavy, where the one independent benchmark we found actually backs
  Mistral's claim.
- **Skip it if…** you want something that runs on a single homelab GPU (it doesn't, at this
  size), or you're choosing a model purely by overall general-capability ranking — the one
  broad independent index we found doesn't put it near the top.

### How it compares
| | Mistral Large 4 | DeepSeek V4.1 Flash ([our prior write-up](model-watch-deepseek-v4-1-flash-2026-09-14.md)) |
|---|---|---|
| Strength | Reportedly strongest open-weight model for coding (Mistral's claim, partially backed by one independent coding benchmark) | Native multimodal in one backbone, aggressive off-peak pricing |
| Weakness | Independent general-capability ranking (Vals Index) much lower than Mistral's own framing | Benchmarks so far are DeepSeek-reported only |
| License | "Mistral Ecosystem Open-Weight License" (terms not fully independently verified) | MIT |
| Context | ~1M claimed; independently measured closer to 512K–524K tokens | 1M tokens in / 384K out |

### Can you run it yourself?
Yes, in the sense that the weights are genuinely downloadable from Hugging Face in FP8 and
NVFP4 variants with no gated approval. But at roughly 1 trillion total parameters, this is not a
homelab GPU job even with MoE sparsity — it needs data-center-class Nvidia hardware, the same
realistic bar as DeepSeek V4.1 Flash. It doesn't fit the single-GPU and Mac mini setups behind
the [local-AI picks](../README.md#-ai--local-llms); this is a rent-cloud-GPU-time model, not a
self-host-tonight one.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
