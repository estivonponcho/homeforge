# Mistral Large 4 — what actually changed, and whether you should care

Mistral's new trillion-parameter flagship landed as a hosted preview this week, with the actual
downloadable weights still a promise rather than a file you can get today.

**Released:** October 6, 2026 (public API preview; weights promised "by the end of the month," not yet published) · **Maker:** Mistral AI · **Type:** multimodal (text + image in, text out), mixture-of-experts — closed preview now, open-weight planned

### The one-line take
> Europe's best shot at a frontier model yet — genuinely competitive with the top Chinese open-weight models on paper, but right now it's API-only, and the promised open weights, license, and most benchmark numbers are all still pending.

### What's new
- Mistral Large 4 is a new mixture-of-experts model, reported at roughly 1.05 trillion total
  parameters with about 49–52 billion active per token (sources disagree on the exact active
  count) plus a 1.6B-parameter vision encoder for image input.
  ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/independent-tests-rank-mistrals-new-trillion-parameter-large-4-the-best-ai-model-outside-the-u-s-and-china-but-chinese-open-weights-still-overcome-europes-best-efforts), [The New Stack via search summary](https://thenewstack.io/?p=22839432))
- Context window: 1M tokens (1,048,576), per Mistral's own model documentation — though a couple
  of third-party aggregators list smaller figures (512K–524K), so treat the exact number as
  "about 1M, unconfirmed to the token."
- It launched as an API-only public preview on October 6, 2026. There is no downloadable weight
  file yet — Mistral says weights are coming "by the end of the month," with one outlet (The New
  Stack) reporting an internal target of October 27, which Mistral itself has not confirmed
  publicly. ([letsdatascience](https://letsdatascience.com/news/mistral-debuts-large-4-open-weight-model-preview-cbf9e0b5))
- License for the eventual weight release is reported to be a new, custom license rather than the
  Apache 2.0 terms Mistral used for Large 3 — unconfirmed until Mistral actually publishes it.
- Launch pricing is a 50%-off introductory rate: about $0.68 per million input tokens and $2.09
  per million output tokens (cached input around $0.07/M), with list price roughly double that —
  $1.36/M input and $4.18/M output — once the promo ends.
- Independent-ish benchmark numbers (via Artificial Analysis, reported through
  [OrcaRouter](https://www.orcarouter.ai/blog/mistral-large-4-0-vs-deepseek-v4-pro)): Intelligence
  Index v4.3 score of 38.4, ahead of DeepSeek V4 Pro's 36.0, and a notable lead on agentic coding
  (Terminal-Bench 4.0: 26.8% vs. DeepSeek's 14.1%). DeepSeek V4 Pro still leads on open-domain
  knowledge (Humanity's Last Exam: 41.0% vs. 35.0%) and costs roughly 40% less per task. These are
  third-party aggregator figures, not numbers I've reproduced myself — treat them as directional.
- Tom's Hardware's framing is the most useful honest signal here: independent tests reportedly
  rank it the best AI model outside the U.S. and China, but say Chinese open-weight models still
  outperform it overall.

### Who it's for
- **Use it if…** you specifically want a European-trained, (eventually) open-weight frontier
  model for data-sovereignty or compliance reasons, and you're fine using it through Mistral's API
  while you wait for the actual weights.
- **Skip it if…** you need weights you can self-host today, a stable non-promotional price, or a
  benchmark track record from more than one preview week. Right now none of those exist yet for
  Large 4.

### How it compares
| | Mistral Large 4 (preview) | DeepSeek V4 Pro |
|---|---|---|
| Strength | Leads on agentic coding (Terminal-Bench 4.0), European data-sovereignty angle | Leads on open-domain knowledge (HLE), weights already open and downloadable |
| Weakness | No downloadable weights or confirmed license yet; most numbers are launch-week and self/aggregator-reported | Overall Intelligence Index trails Large 4 per Artificial Analysis's early read |
| Price | ~$0.68/M in, $2.09/M out at launch discount (list ~$1.36/$4.18) | Reported ~40% cheaper per task (via Artificial Analysis) |
| Context | ~1M tokens (1,048,576 per Mistral's docs; some trackers show less) | Varies — see our [DeepSeek V4.1 Flash write-up](model-watch-deepseek-v4-1-flash-2026-09-14.md) for that family's context specs |

### Can you run it yourself?
Not yet. This is an API-only preview — there is no weight file to download today. Mistral has
said weights are coming "by the end of the month," but hasn't published the license or confirmed
an exact date (October 27 is a third-party report, not Mistral's own commitment). At roughly 1
trillion total parameters, even with MoE sparsity this will not be a casual homelab-GPU model —
expect it to land in the same "rent cloud GPU time or use an API provider" category as other
trillion-parameter releases, not the [local-AI picks](../README.md#-ai--local-llms) built around
single-GPU or Mac mini setups. We'll revisit this section once weights and a license actually
exist.

### My hands-on notes
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

### Bottom line
> [PLACEHOLDER — Mike to add hands-on notes before publishing]

---

*Gear & tools referenced: [AI & Local LLMs picks](../README.md#-ai--local-llms).*
*Part of [HomeForge](../README.md).*
