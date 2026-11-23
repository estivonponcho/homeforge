# GPT-6.2 Astra & Sol — what actually changed, and whether you should care

OpenAI's mid-November refresh of its flagship pair trims prices, claims a solid
jump on coding benchmarks, and — per at least one report — pushed Astra over a
new internal safety threshold on the way out the door.

**Released:** November 17, 2026 · **Maker:** OpenAI · **Type:** chat / reasoning (two-tier flagship pair)

### The one-line take
> A real, if incremental, upgrade to OpenAI's top two models — cheaper per task than their predecessors, but independent benchmarks still put Claude Fable 5.2 ahead on raw intelligence.

### What's new
- Two models shipped together: **GPT-6.2 Astra**, OpenAI's frontier model "for your
  hardest projects," and **GPT-6.2 Sol**, the cheaper, faster everyday model —
  continuing the two-tier naming OpenAI introduced with GPT-6 Astra/Sol.
  ([OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol))
- Pricing: Astra is $8 per million input tokens / $40 per million output tokens —
  about 20% below GPT-6 Astra's rate. Sol holds at $2/$10 per million tokens,
  unchanged from GPT-6.1 Sol. ([Requesty](https://www.requesty.ai/blog/gpt-6-2-sol-astra-pricing-benchmarks))
- On Cognition's FrontierCode 2.0 coding benchmark, reports put Sol at roughly
  43.8–44.2% — within half a point of Astra — while costing about a fifth as
  much per run (~$1.29 vs. ~$5.97). Figures vary slightly between outlets, so
  treat the exact decimals as approximate. ([Requesty](https://www.requesty.ai/blog/gpt-6-2-sol-astra-pricing-benchmarks), [OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol))
- Independent third-party scoring from Artificial Analysis's Intelligence Index
  reportedly places Astra at 62 and Sol at 57 — both behind Claude Fable 5.2's 65.
  Treat this as one aggregator's methodology, not a universal ranking.
  ([llm-stats.com](https://llm-stats.com/blog/research/gpt-6-2-astra-sol-launch))
- One report says GPT-6.2 Astra is the first model OpenAI has deployed externally
  that it assessed as meeting the "High" threshold under its Preparedness
  Framework for AI self-improvement, while Sol falls below that line. This is
  from a single secondary source — worth confirming against OpenAI's own system
  card before treating it as settled. ([GCN](https://gcn.com/?p=23366))
- OpenAI says it's pairing the launch with tighter safeguards around
  higher-risk cybersecurity assistance. ([OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol))
- Available now in ChatGPT Work, Codex, and the API as `gpt-6.2-astra` and
  `gpt-6.2-sol`. ([TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis/))
- Context window and max-output figures are reported inconsistently across
  outlets (some say ~1.05M tokens, others cite different Codex defaults for
  Astra vs. Sol) — unconfirmed pending OpenAI's own documentation, so this
  write-up doesn't lock in a number.

### Who it's for
- **Use it if…** you're already on OpenAI's stack and want a cheaper coding/agent
  workhorse — Sol's benchmark-to-cost ratio is the actual headline here, not
  Astra's modest top-line gains.
- **Skip it if…** you're picking a model purely on third-party intelligence
  benchmarks. By Artificial Analysis's numbers, Claude Fable 5.2 still leads
  both Astra and Sol — this release narrows the gap on cost and coding, not on
  raw capability.

### How it compares
| | GPT-6.2 Astra / Sol | Previous / rival |
|---|---|---|
| Strength | Sol gets near-Astra coding scores at ~1/5 the per-task cost | Claude Fable 5.2: higher Artificial Analysis Intelligence Index score |
| Weakness | Reported to cross a "High" self-improvement safety threshold (Astra only, single-source) | — |
| Price | Astra $8/$40 per M tokens (in/out); Sol $2/$10 per M tokens | GPT-6 Astra: ~20% higher; GPT-6.1 Sol: same as Sol today |
| Context | Unconfirmed — reports disagree | — |

### Can you run it yourself?
No — these are closed, API-only models. If you're already building on OpenAI's
API, swapping in `gpt-6.2-sol` for routine agent or coding tasks is the
low-risk move given the reported cost-to-score ratio; reach for `gpt-6.2-astra`
only for the harder tasks where the marginal quality actually matters, since
it costs roughly 4x more per run on the coding benchmark above.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
