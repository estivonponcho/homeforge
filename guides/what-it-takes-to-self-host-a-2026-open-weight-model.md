# What it actually takes to self-host a 2026 open-weight model

"Open weight" doesn't mean "runs on your GPU." Every model in this series — DeepSeek V4.1 Flash, DeepSeek V4 Pro, Kimi K3, GLM-5.3-Flash, and Qwen3.8-Max — publishes downloadable weights, and every one of them needs real server-class hardware to actually load, let alone run well. Here's the honest hardware math, quantization ladder by quantization ladder.

### The one fact that changes everything
Active parameters describe compute per token. **Total parameters describe what has to fit in memory** — every expert in a mixture-of-experts model has to be resident in RAM or VRAM whether or not it fires on a given token, because you don't know in advance which experts a given token will route to. (The mechanics of why are in the [architecture deep dive](how-2026-open-weight-models-actually-work.md).) A "552B total / 8B active" model is not an "8B-class" model for hardware-sizing purposes — it's a 552B-class model that happens to be cheap to *run* once it's loaded.

Quantization reduces the bytes needed per parameter (FP16 ≈ 2 bytes/param, INT8/Q8 ≈ 1 byte/param, 4-bit ≈ 0.5 bytes/param, roughly — real GGUF quant levels vary by scheme), but it doesn't change the parameter count, so it scales the floor down without ever changing which tier of hardware you're in.

### The numbers, model by model
| Model | Total params | Smallest usable quant | Practical single-machine reality |
|---|---|---|---|
| **DeepSeek V4.1 Flash** | 552B backbone (~763B incl. Engram memory + DSpark drafter) | Q4_K_M: 444.7 GB · Q8_0: 508 GB · down to Q1_0: 105.9 GB | Q4_K_M fits 1×80GB or 2×48GB GPUs at "close to FP8" quality — the one model here with an actual single-high-end-GPU story |
| **DeepSeek V4 Pro** | 1.6T total, 49B active | ~862 GB in native FP4+FP8 form | Needs 8×H200 (141GB each, ~1.1TB) in one node, or a multi-node H100/H200 cluster over InfiniBand |
| **Kimi K3** | 2.8T total, 104B active | 1-bit UD-IQ1_S: 594 GB (78.9% top-1 accuracy) · 2-bit: 861 GB (90.4%) · TQ1_0: 509 GB | Full weights are 1.56 TB; vLLM wants ~1.68 TB VRAM for the complete model. Native serving runs on 8×B300-class GPUs. A 24GB consumer GPU cannot run this even quantized |
| **GLM-5.3-Flash** | 320B total, 18B active | INT4: ~175 GB · Q4_K_M: ~195–205 GB · 1-bit: fits 100GB RAM · 3-bit: fits 128GB (Mac/DGX Spark) | The smallest model here by far — a single H200 (141GB) fits a "2-bit-lite" quant with room to spare, making it the only one of the five with any real single-GPU story |
| **Qwen3.8-Max (open weights)** | 2.4T total, ~95B active | Q4_K_M: ~1,669 GB (~1,473 GB before overhead) · Q8: ~2,913 GB · FP16: ~5,480 GB | Even Unsloth's smallest 1-bit GGUF is ~397 GB before overhead. Q4_K_M alone needs roughly 21× 80GB datacenter GPUs pooled together. Built for vLLM/SGLang serving clusters, not a workstation |

*Sources: DeepSeek V4.1 Flash — [vramcalculator.com](https://vramcalculator.com/deepseek-v4-1-flash-vram-requirements/); DeepSeek V4 Pro — [Thunder Compute](https://www.thundercompute.com/blog/deploy-deepseek-v4-locally), [morphllm.com](https://www.morphllm.com/deepseek-v4); Kimi K3 — [buildfastwithai.com](https://www.buildfastwithai.com/blogs/run-kimi-k3-locally), [modemguides.com](https://www.modemguides.com/blogs/ai-news/run-kimi-k3-locally-hardware-reality-check), [kingy.ai](https://kingy.ai/ai/ai-guides/run-kimi-k3-locally-hardware-vram-cost/); GLM-5.3-Flash — [Spheron](https://www.spheron.network/tools/gpu-recommender/zai-org/GLM-5.3-Flash/), [Yotta Labs](https://www.yottalabs.ai/post/glm-5-3-flash-hardware-requirements-gpu-memory-2026); Qwen3.8-Max — [willitrunai.com](https://willitrunai.com/models/qwen-3.8-2.4t-a95b), [canitrun.dev](https://canitrun.dev/models/qwen3.8-2.4t-a95b/). GGUF sizes and quality figures are third-party community measurements, not vendor-published numbers — treat exact byte counts as approximate.*

### What this means in practice
- **None of these fit a homelab GPU**, even the smallest one. GLM-5.3-Flash is the closest thing to an exception, and its "single GPU" story is a $30,000+ H200 — not a card you're buying for a home server.
- **DeepSeek V4.1 Flash is the most self-hostable of the frontier-scale options** here, in the sense that a realistic prosumer/small-business setup (1×80GB card, or 2×48GB cards like a pair of RTX 6000 Adas) can actually load a quality-competitive quantization. Reported throughput on a single GPU is modest — around 2–3 tokens/sec — climbing to 24–46 tokens/sec across 3–4 GPUs depending on the serving framework. ([codersera.com](https://codersera.com/blog/deepseek-v4-vram-gpu-requirements-2026/amp/))
- **Kimi K3, Qwen3.8-Max, and DeepSeek V4 Pro are not personal-infrastructure models.** They're built for, and realistically only make sense on, rented multi-GPU cloud clusters or dedicated inference providers (OpenRouter, the vendor's own API, DeepInfra, etc.). If you self-host one of these, you're doing it as a business decision with a real infrastructure budget, not a weekend project.
- **Ollama and LM Studio mostly aren't there yet for the biggest ones.** At the time of writing, Kimi K3 support lives in an unmerged llama.cpp pull request rather than a stable release, which is also why Ollama and LM Studio can't load it — Ollama's hosted "Kimi K3" listing routes to Ollama's own cloud servers on a paid tier rather than running locally. Check current status before assuming a GGUF drop means one-command local support. ([ComputingForGeeks](https://computingforgeeks.com/run-kimi-k3-locally/))

### If you actually want to run something yourself
If self-hosting on hardware you own is the actual goal rather than a nice-to-have, none of the five models in this comparison series are the right target — they're all built for datacenter-scale serving regardless of quantization. The [best way to run a local LLM](best-way-to-run-a-local-llm.md) guide and the [local-AI picks](../README.md#-ai--local-llms) are built around a completely different tier: 7B–70B-class models that genuinely run on a single consumer GPU or a Mac mini's unified memory. That's a different trade-off (much lower ceiling on capability) for a very different payoff (it actually runs on the box sitting on your desk).

### Bottom line
If you want the closest thing to "self-hosted frontier capability" on hardware a serious homelabber could plausibly own or rent short-term, DeepSeek V4.1 Flash is the one to look at first — it's the only model in this comparison with a quantization that fits on 1–2 high-end GPUs instead of a cluster. Everything else here is a rent-it-or-API-it decision, not a self-host-it decision, no matter how tempting "open weight" sounds on the label.

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*See also: [How 2026's open-weight models actually work](how-2026-open-weight-models-actually-work.md),
[Open-weight AI licenses in 2026, actually explained](open-weight-ai-licenses-2026-explained.md), and
[Best way to run a local LLM](best-way-to-run-a-local-llm.md).*
*Part of [HomeForge](../README.md).*
