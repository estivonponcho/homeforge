# Model-Watch write-up template

*A repeatable format for covering each new model release (Claude, GPT, Gemini,
Llama, local models). Fill the blanks, publish same-day, rank for the query
"[model name] review / what's new."*

Copy this file, rename it `model-watch-<model>-<date>.md`, and fill it in.

---

## [Model name] — what actually changed, and whether you should care

**Released:** [date] · **Maker:** [company] · **Type:** [chat / reasoning / open-weight / multimodal]

### The one-line take
> [Your honest verdict in a sentence. This is the quote people share.]

### What's new
- [Capability / benchmark / context window / price change — the real deltas, not
  the marketing bullet points.]
- [If it's an incremental bump, say so. Credibility comes from not overhyping.]

### Who it's for
- **Use it if…** [the concrete situations where this is now the right pick]
- **Skip it if…** [when the previous model or a competitor is still better]

### How it compares
| | This model | Previous / rival |
|---|---|---|
| Strength | | |
| Weakness | | |
| Price | | |
| Context | | |

### Can you run it yourself?
[For open-weight models: what hardware it needs, and whether it runs on the
[local-AI picks](../README.md#-ai--local-llms). For closed models: API notes.]

### My hands-on notes
[Two or three things you noticed actually using it — the stuff benchmarks miss.
This is the part readers can't get from the press release, and it's why they'll
come back to you.]

### Bottom line
[Buy / wait / ignore, and what you personally switched to or didn't.]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*

---

## Why this format works

- **Same-day + specific** = it ranks while everyone's searching the model name.
- **The comparison table** is what people screenshot and share.
- **"My hands-on notes"** is the moat — anyone can rewrite the announcement; only
  you have your actual experience.
- Keep it **honest about incremental releases.** Calling a minor update minor is
  what makes people trust you when you say something's a big deal.

> **Automation idea:** this is a perfect candidate for a scheduled agent that
> drafts a first pass when a new model drops, leaving you to add the hands-on
> notes and hit publish. Ask HomeForge's maintainer (you) to wire it up.
