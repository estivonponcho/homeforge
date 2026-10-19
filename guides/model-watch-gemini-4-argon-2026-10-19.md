# Gemini 4 Argon — what actually changed, and whether you should care

**Released:** First announced September 30, 2026 (restricted preview via Google's Fairwind Program for vetted cyber defenders); made generally available October 13, 2026. · **Maker:** Google DeepMind · **Type:** chat / reasoning, frontier closed model

### The one-line take
> Google's real answer to GPT-6 Astra and Claude Opus 5.5 — and the first Gemini in a while that independent testers are actually arguing about, instead of shrugging at.

### What's new
- Google positions Argon around sustained, long-horizon reasoning rather than a single
  headline benchmark: its own launch copy describes it as "built to sustain deep
  reasoning across complex, long-horizon workflows," targeting real-world software
  engineering, enterprise knowledge work (the examples given are legal and finance),
  and cyber-defense work.
  ([Google AI on X](https://x.com/GoogleAI/status/2105388478683119904), [Google DeepMind on X](https://x.com/GoogleDeepMind/status/2105388084154056939))
- Google's own launch post calls out an "industry-leading 1M token output limit" —
  note this is specifically an *output* ceiling, not just a large input context window,
  which is the unusual claim here.
  ([Google on X](https://x.com/Google/status/2105388143902175529))
- Rollout happened in two stages: a restricted preview starting September 30 limited to
  vetted cybersecurity defenders through Google's "Fairwind Program," reportedly alongside
  a voluntary U.S. government pre-release safety review, followed by global general
  availability on October 13 "for developers and enterprises via the API in AI Studio and
  Gemini platform."
  ([Google DeepMind on X](https://x.com/GoogleDeepMind/status/2110039274922131792))
- Consumer access on GA day: Google AI Ultra and Pro subscribers get it in the Gemini app
  and in AI Mode in Search; Ultra subscribers also get it in Google Antigravity, per
  secondary coverage of the GA post (unconfirmed against Google's own pricing page, which
  wasn't reachable for this write-up).
- **Pricing and benchmark numbers are contested — treat as unconfirmed.** Third-party
  trackers report API pricing anywhere from $2 input / $10 output per million tokens to a
  lower introductory rate, with a separate batch-tier figure around $1 input / $5 output;
  one tracker says the price rises after an introductory period, another says it stays
  matched to a rival's list price until December. Reported benchmark figures (DeepSWE 1.1,
  Vibe Code Bench, Terminal-Bench 4.0 scores, and a claim of beating GPT-6 Astra and Claude
  Opus 5.5 on "12 of 18" published tests) all come from aggregator sites and non-English
  secondary coverage, not Google's own benchmark card, and independent early testing is
  reportedly mixed rather than one-sided. None of these figures are repeated here as fact.

### Who it's for
- **Use it if…** you're already on Google's stack (Vertex AI / AI Studio / Workspace) and
  want to try a frontier model built around very long agentic or document-heavy workflows —
  especially anything that needs a large *output*, not just a large prompt, like generating
  long reports, long refactors, or multi-step tool-use traces in one pass.
- **Skip it if…** you need confirmed pricing or benchmark numbers before committing budget.
  This is days old, the official benchmark card and pricing page weren't accessible while
  writing this, and the numbers floating around the web disagree with each other.

### How it compares
| | Gemini 4 Argon | Previous / rival |
|---|---|---|
| Strength | Long-horizon reasoning, unusually large *output* token limit (Google claims 1M) | GPT-6 Astra / Claude Opus 5.5: longer track record, benchmark claims vs. Argon disputed |
| Weakness | Launched days ago; pricing and benchmarks still inconsistent across sources | — |
| Price | Reported ~$2/M input, ~$10/M output (unconfirmed, may be introductory) | Varies — see [frontier pricing guide](frontier-model-api-pricing-comparison-2026.md) |
| Context | ~1M tokens reported for input; 1M token *output* limit confirmed by Google | Most rivals cap output far lower even at similar input context sizes |

### Can you run it yourself?
No — this is a closed, API/subscription-only model from Google, not open-weight. Access is
via the Gemini API in AI Studio, Vertex AI for enterprise, or the consumer Gemini app on
paid Ultra/Pro tiers. If you want something you can actually self-host, see the
[local-AI picks](../README.md#-ai--local-llms) and the
[self-hosting guide](what-it-takes-to-self-host-a-2026-open-weight-model.md) instead.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
