# Open-weight AI licenses in 2026: the fine print, actually explained

"Open weight" tells you the download link works. It tells you nothing about what you're allowed to do with what you download — and in 2026, the four biggest open-weight releases split cleanly into two groups: two with no strings attached, and two with real commercial thresholds buried in otherwise MIT-flavored text. Here's what each license actually says, not what the headline "open-source!" coverage implied.

> **Not legal advice.** This is a plain-English summary of publicly reported license terms for context, not a substitute for reading the actual license file before you build a commercial product on any of these. Links to the primary source are below for each one — read them yourself.

### The genuinely no-strings group: DeepSeek and GLM
**DeepSeek V4.1 Flash and DeepSeek V4 Pro** both ship under a plain, unmodified **MIT license** — full stop. No revenue thresholds, no branding requirements, no carve-outs found in any source for this piece. MIT grants use, copy, modify, merge, publish, distribute, sublicense, and sell, with no strings beyond keeping the copyright notice. Once weights are public under MIT, DeepSeek has no technical or legal mechanism to later restrict how they're used. ([Hugging Face LICENSE file](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/LICENSE))

**GLM-5.3-Flash** is the same story: plain MIT, released by Zhipu/Z.ai on Hugging Face on August 26, 2026. No commercial restrictions turned up anywhere in this research. If your priority is "the fewest possible legal questions before I ship," these two are it. ([testingcatalog.com](https://www.testingcatalog.com/z-ai-launches-glm-5-3-flash-under-mit-license/))

### The "MIT until you're a real business" group: Kimi K3 and Qwen3.8-Max
Both of these read like MIT for most of their length — the same broad grant to use, copy, modify, distribute, sublicense, sell, deploy, fine-tune, and build derivative works — and then attach conditions plain MIT doesn't have.

**Kimi K3 License** ([full text on GitHub](https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE)) has two thresholds:
1. **The Model-as-a-Service (MaaS) clause.** If you run a business that gives third parties inference or fine-tuning access with meaningful control over inputs, parameters, or training data, and your revenue — combined across you and your affiliates, not limited to money earned from Kimi K3 specifically — crosses **$20 million over any trailing 12 months**, you have to sign a separate agreement with Moonshot before continuing.
2. **The branding clause.** Any commercial product or service with more than **100 million monthly active users**, or more than **$20 million in monthly revenue**, has to display "Kimi K3" prominently in its interface.
3. **Exemptions:** purely internal use (not exposing the model, its outputs, or its capabilities to third parties), and use accessed through Moonshot's own official products or certified inference partners, are carved out of both clauses.

**Qwen3.8-Max License** ([full text on Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE), for the open-weights release specifically — the hosted API is a separate commercial product) has a structurally similar but differently-scoped pair of thresholds:
1. **The attribution clause.** More than **100 million monthly active users** or more than **$20 million in monthly revenue** → you must display the model name prominently in your UI.
2. **The separate-license clause.** If you're running a **"Model-as-a-Service" or "AI Work Assistant" business** — Alibaba specifically defines "AI Work Assistant" as an independent AI product primarily for AI-assisted coding or office productivity (its own examples: Qoder, QwenWork) — and your trailing-12-month aggregate revenue including affiliates exceeds **$50 million**, you need a separate paid license before commercial use. The definition explicitly excludes single-purpose tools (an AI translator, say), assistants for a different domain (Alibaba's own examples: a shopping assistant, a maps chat feature), or a coding/office feature bolted onto a product whose primary purpose is something else.
3. **Exemption:** purely internal use that never exposes the model to third parties.

### Side by side
| | DeepSeek (both) | GLM-5.3-Flash | Kimi K3 | Qwen3.8-Max (open weights) |
|---|---|---|---|---|
| Base license | MIT | MIT | Modified MIT | Modified MIT |
| Revenue/scale threshold | None | None | $20M/12mo (MaaS) · 100M MAU or $20M/mo (branding) | $50M/12mo (MaaS/AI Work Assistant) · 100M MAU or $20M/mo (attribution) |
| What happens above the threshold | N/A | N/A | Separate agreement required, or display "Kimi K3" in UI | Separate paid license required, or display model name in UI |
| Internal-use exemption | N/A (unrestricted anyway) | N/A (unrestricted anyway) | Yes | Yes |

### What this actually means for you
If you're a homelab hobbyist, an indie developer, or a small startup, **none of these four thresholds affect you today** — they're all denominated in tens of millions of dollars of revenue or hundreds of millions of monthly users. This is squarely aimed at large platforms and well-funded AI startups building a product on top of the weights, not at anyone reading a HomeForge guide about self-hosting a model. The practical read: build, ship, and scale freely on any of these four — but if your product is on a trajectory toward real scale, put a reminder on your calendar to actually read the license you're building on before you cross into "successful enough that it matters" territory, because by then it's a much more expensive conversation.

The other honest note: these terms are new, none has been tested in a real dispute yet, and the exact wording matters more than any summary (including this one) — always confirm against the license file linked above before you make a business decision on it.

### Bottom line
DeepSeek and GLM-5.3-Flash are the closest thing to genuinely unconditional open weights in this comparison — pick either one if avoiding any future licensing conversation is a priority. Kimi K3 and Qwen3.8-Max are still extremely permissive in practice for the vast majority of use, but they're not unconditional MIT, and the difference only shows up once you're operating at a scale most projects never reach — which is exactly why it's worth knowing about now rather than discovering it later.

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*See also: [How 2026's open-weight models actually work](how-2026-open-weight-models-actually-work.md),
[What it actually takes to self-host a 2026 open-weight model](what-it-takes-to-self-host-a-2026-open-weight-model.md), and
[DeepSeek V4.1 Flash vs. the other open-weight giants of 2026](deepseek-v4-1-flash-vs-open-weight-rivals-2026.md).*
*Part of [HomeForge](../README.md).*
