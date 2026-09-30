# Grok 4.7 — what actually changed, and whether you should care

Elon Musk billed Grok 4.7 as roughly on par with Claude Opus 5.0. Independent
benchmarks put it just behind Opus 5 and Fable 5.1 instead, and early users are
flagging a real problem: its "xhigh" reasoning setting can burn more than double
the tokens of the previous model for the same task.

**Released:** September 21, 2026 · **Maker:** xAI · **Type:** closed, multimodal (text + image input, text-only output), coding/agentic

### The one-line take
> Real gains on agentic coding benchmarks, but the hype-to-reality gap and a token-hungry "xhigh" mode make this one to test carefully before you trust the cost estimate.

### What's new
- Released September 21, 2026, positioned by xAI as a frontier model for coding,
  agentic tasks, and knowledge work. Available same-day in Cursor, Grok Build,
  the Grok API, and various third-party coding harnesses and model routers.
  ([evolink.ai](https://evolink.ai/blog/grok-4-7-release-date))
- Context window: 500K tokens, text and image input, text-only output, reasoning
  effort levels of low/medium/high(default)/xhigh — noticeably smaller than the
  1M+ windows several rivals now ship.
  ([llm-stats.com](https://llm-stats.com/models/grok-4.7))
- Pricing: $2 input / $0.50 cached input / $6 output per million tokens below
  200K prompt tokens; $4 / $1 / $12 above that threshold.
  ([llm-stats.com](https://llm-stats.com/models/grok-4.7))
- On Artificial Analysis's AA-Briefcase benchmark (realistic professional work
  tasks), Grok 4.7 scores 1657 Elo — just behind Claude Opus 5 and Fable 5.1, not
  ahead of them as Musk's "roughly on par with Opus 5.0" framing suggested. Its
  clearest gains are on agentic coding benchmarks like the Artificial Analysis
  Coding Agent Index and DeepSWE.
  ([Artificial Analysis](https://artificialanalysis.ai/articles/benchmarking-grok-4-7))
- The real controversy: at "xhigh" effort, Grok 4.7 reportedly uses roughly
  81,000 output tokens per task versus about 38,000 for Grok 4.6 on identical
  tasks — more than double. That's pushed real-world operating cost above even
  GPT-6 Astra in some reported cases, undercutting the "cheaper agentic coding"
  pitch.
  ([The New Stack](https://thenewstack.io/grok-4-7-agent-stamina/))
- Early user reports include complaints about weak frontend/UI generation and
  no meaningful 3D generation capability — take these as anecdotal until you've
  tested your own use case.
  ([Stork.AI](https://www.stork.ai/blog/xais-grok-47-is-a-deceptive-upgrade))

### Who it's for
- **Use it if…** your workload is specifically agentic coding and you're willing
  to closely monitor token spend at "xhigh" effort — the coding-benchmark gains
  are real, just budget for the token usage before you commit.
- **Skip it if…** you need a large context window (500K is now on the small side),
  need reliable frontend/UI or 3D generation, or you're choosing based on Musk's
  "Opus-class" framing rather than the independent numbers.

### How it compares
| | Grok 4.7 | Previous / rival |
|---|---|---|
| Strength | Real gains on agentic coding benchmarks (Coding Agent Index, DeepSWE) | Claude Opus 5 / Fable 5.1: ahead on AA-Briefcase overall |
| Weakness | "xhigh" effort can use 2x+ the tokens of Grok 4.6 for the same task, inflating real cost | — |
| Price | $2/$6 per M in/out below 200K tokens; $4/$12 above | Comparable-tier rivals often cheaper at high context |
| Context | 500K tokens | Several rivals now ship 1M+ |

### Can you run it yourself?
No — closed, API-only model, not open-weight, so it's not a fit for the
[local-AI picks](../README.md#-ai--local-llms). It's available through the Grok
API, Cursor, Grok Build, and select third-party routers/cloud platforms.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
