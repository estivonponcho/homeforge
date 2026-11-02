# Gemini 4 Carbon — what actually changed, and whether you should care

**Released:** October 28, 2026 · **Maker:** Google DeepMind · **Type:** closed, cybersecurity-focused frontier model

### The one-line take
> A genuinely new, cybersecurity-specialized frontier model with striking benchmark numbers — all of them Google's own, and all of them currently unverifiable because almost nobody can use it yet.

### What's new
- Google DeepMind's next frontier model after Gemini 4 Argon (announced September 30, 2026),
  positioned as state-of-the-art on cybersecurity and long-horizon agentic tasks rather than as
  a general-purpose upgrade. ([blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Google DeepMind on X](https://x.com/GoogleDeepMind/status/2115489356437651654))
- Google-reported benchmarks: 88.2% on SEC-bench Pro (finding real vulnerabilities), and figures
  cited around 54.8% on ExploitGym and 71% on CWE-bench. Google also says Carbon more than
  doubled Argon's success rate at generating secure code in internal testing, and the Chrome
  team reported patches it called meaningfully better than a large frontier model from another
  lab. Treat all of these as vendor-reported until independently reproduced.
  ([Help Net Security](https://www.helpnetsecurity.com/2026/10/29/google-gemini-4-carbon-model/), [The Register](https://www.theregister.com/ai-and-ml/2026/10/29/googles-gemini-4-carbon-looks-like-a-diamond-in-the-rough/5306149))
- Third-party aggregator Artificial Analysis puts Carbon at the top of its Intelligence Index at
  a score of 59, with a reported cost of $7.76 per Intelligence Index task — about 23% cheaper
  than their figure for Claude Opus 5.5 (max) at $10.04. This is an independent benchmark run,
  not a Google number, but it still reflects Google's hosted model under Artificial Analysis's
  own test harness, not a fully neutral reproduction.
- Pricing is unconfirmed and conflicting. One report cites introductory API pricing matching
  Argon's — $2 per million input tokens, $10 per million output tokens — while Artificial
  Analysis lists $4.00/$20.00 per million tokens for input/output. As of October 29, Carbon
  reportedly wasn't yet listed on Google's own API pricing page. Mark pricing as **unconfirmed**
  until Google publishes it directly.
- Context window: commonly reported as 1M tokens, but at least one source notes Google had not
  published an official context window, output limit, or knowledge cutoff for Carbon as of
  launch. Mark as **unconfirmed**.
- Access is deliberately narrow: Carbon is limited to a vetted group of cyber defenders through
  Google's Fairwind Program, with Google saying it plans a staged expansion to developers,
  businesses, and consumers later. There's no public API key you can get today.
  ([Help Net Security](https://www.helpnetsecurity.com/2026/10/29/google-gemini-4-carbon-model/))
- Safety stack: reportedly reuses Argon's layered defenses (prompt-injection resilience,
  chain-of-thought monitoring), and is said to have resisted every attack on Gray Swan's indirect
  prompt-injection benchmark — a claim worth tracking but not yet independently confirmed outside
  that one benchmark run.

### Who it's for
- **Use it if…** you're part of a vetted security team already inside Google's early-access
  cyber defender program and want AI-assisted vulnerability discovery and patch generation —
  this is explicitly built for that workflow, not general use.
- **Skip it if…** you're looking for something to actually use this week. It isn't publicly
  available, the pricing page doesn't fully reflect it yet, and the headline benchmark numbers
  are either Google's own or run on Google's hosted model by a third party — not independently
  reproduced.

### How it compares
| | Gemini 4 Carbon | Gemini 4 Argon (predecessor) |
|---|---|---|
| Strength | Cybersecurity-specific benchmarks (vendor-reported), tops Artificial Analysis Index at 59 | General frontier model, broader public availability |
| Weakness | Restricted access; context window and pricing not fully published | Less specialized for security workloads |
| Price | Reported $2/$10 per million tokens (unconfirmed) vs. Artificial Analysis's $4/$20 figure | ~$2 input / $10 output per million tokens (introductory) |
| Context | Commonly cited as 1M tokens (unconfirmed by Google) | 1M tokens |

### Can you run it yourself?
No. This is a closed, cloud-hosted model with no open weights, and access itself is gated to a
vetted cyber-defender cohort under Google's Fairwind Program. There's nothing here for the
[local-AI picks](../README.md#-ai--local-llms) — this is the opposite end of the spectrum from a
self-hosted model.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
