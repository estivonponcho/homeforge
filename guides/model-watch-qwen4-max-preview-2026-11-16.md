# Qwen4-Max-Preview — what actually changed, and whether you should care

**Released:** November 11, 2026 (preview) · **Maker:** Alibaba · **Type:** chat / reasoning / agentic coding (closed preview, text/image/video input)

### The one-line take
> Alibaba is showing off its next flagship, but this is a time-boxed preview with no benchmark table, no model card, and no weights — there's not enough here yet to judge it on anything but the spec sheet.

### What's new
- Alibaba opened a **time-limited preview** of Qwen4-Max — not a general release. Per Alibaba's own Model Studio documentation, the window runs from 10:00 on November 11 to 24:00 on November 25, 2026 (UTC+8), after which the model is retired.
  ([Alibaba Model Studio docs](https://help.aliyun.com/en/model-studio/qwen-max), [FourWeekMBA](https://fourweekmba.com/ai-alibaba-opens-a-350-hour-qwen4-max-preview-with-1m-context/))
- Access is subscription-only during the preview: pay-as-you-go API access is **not supported** — it's gated behind Alibaba's Token Plan.
  ([Xenospectrum](https://xenospectrum.com/en/qwen4-max-preview-specs-limitations/))
- Context window: **1M tokens**, with up to 393,216 output tokens shared between the model's internal "thinking" budget and its final answer. Input reportedly supports text, image, and video.
  ([ai-tldr.dev](https://ai-tldr.dev/releases/qwen-qwen4-max-preview/), [Xenospectrum](https://xenospectrum.com/en/qwen4-max-preview-specs-limitations/))
- Alibaba is positioning it for software development and long-running agent workflows — described by coverage as "agent-first coding" — but that's the vendor's framing, not a measured result.
  ([AlphaSignal](https://alphasignal.ai/news/alibaba-launches-qwen4-max-with-agent-first-coding-and-1m-token-support), [AIBusiness](https://aibusiness.com/generative-ai/alibaba-unveils-most-powerful-ai-model-yet))
- What's genuinely missing at launch: **no benchmark table, no model card, no published parameter count, no license, and no downloadable weights.** Several outlets specifically flag this gap. One report also notes the smaller Qwen4-27B tier is considered the likelier candidate for an eventual open-weight release, not Max.
  ([Xenospectrum](https://xenospectrum.com/en/qwen4-max-preview-specs-limitations/))

### Who it's for
- **Use it if…** you're already inside Alibaba's Model Studio ecosystem on a Token Plan and want to kick the tires on the 1M-token context and agentic-coding claims before the preview window closes on November 25.
- **Skip it if…** you need pay-as-you-go API access, a license you can plan around, or any independently verified benchmark before committing engineering time — none of that exists yet for this release.

### How it compares
| | Qwen4-Max-Preview | Previous / rival |
|---|---|---|
| Strength | 1M-token context, large shared thinking+answer output budget (393,216 tokens) | Qwen3.6 Max Preview: ~262K context, $1.04/M input · $6.24/M output (third-party aggregator figures) |
| Weakness | No benchmarks, model card, license, or weights published; subscription-only access | — |
| Price | Not published for Qwen4-Max-Preview (Token Plan only, no PAYG) | Qwen3.6 Max Preview pricing above is for the prior generation, not confirmed for this one |
| Context | 1M tokens in / up to 393,216 tokens out | — |

### Can you run it yourself?
Not right now. There are no published weights, and even API access during the preview requires Alibaba's Token Plan rather than ordinary pay-as-you-go keys. If Alibaba follows its usual pattern, a smaller tier (reportedly Qwen4-27B) is the more likely candidate for an eventual open-weight drop that would fit the [local-AI picks](../README.md#-ai--local-llms) — but that's speculation, not a confirmed plan.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
