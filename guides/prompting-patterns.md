# Prompting patterns that actually work

*Not "magic prompts." Reusable structures you can apply to any model, any task.
Learn these six and you'll rarely need to copy someone else's prompt again.*

> Original writing, informed by hands-on use and formal AI coursework. The goal is
> to teach the underlying pattern, not hand you a fish.

---

## 1. Role + Goal + Context + Format (the workhorse)

The backbone of a good prompt has four parts:

- **Role** — who the model should act as ("You are a meticulous copy editor").
- **Goal** — the actual outcome you want, stated as a result, not a topic.
- **Context** — the material and constraints the task needs.
- **Format** — the exact shape of the output you'll use.

Miss any one and quality drops. Most bad output is a missing *format* or a vague
*goal*.

## 2. One good example beats a paragraph of description (few-shot)

Instead of describing the style you want, **show one example** of input → output.
Models pattern-match far better than they follow adjectives. One worked example is
worth three sentences of "make it professional but friendly."

## 3. Ask for the thinking, then the answer

For anything with reasoning — analysis, debugging, math, planning — tell the model
to **work through it step by step before giving the final answer.** You get better
answers *and* a visible chain you can check. For a clean final deliverable, ask it
to think first, then put the final result in its own clearly-marked section.

## 4. Separate instructions from data

When your prompt contains both instructions *and* content to act on, mark the
boundary so the model never confuses the two:

```
<instructions>Summarize the report below in 5 bullets.</instructions>
<report>
...paste the report...
</report>
```

This is the single most reliable fix for "it answered my example instead of doing
the task." (It's also a basic prompt-injection defense — untrusted content stays
in the data slot.)

## 5. Critique-and-revise, not re-roll

Don't just regenerate and hope. **Tell the model what's wrong and ask for a
specific revision:** "The intro is too long and the tone is stiff — cut the intro
to two sentences and make it conversational." You converge on what you want in two
or three passes instead of gambling on a fresh roll.

## 6. Give it an out

Tell the model what to do when it doesn't know: "If the answer isn't in the
provided text, say 'not found' rather than guessing." This is the cheapest way to
cut confident-but-wrong answers (hallucinations).

---

## Putting it together

A strong prompt is usually: **a role, a concrete goal, the context marked off from
instructions, one example of the output, and a clear format — plus permission to
say "I don't know."** Everything else is refinement.

---

> **[Your take — from coursework]**
> A great addition here: a short section connecting these patterns to *why* they
> work under the hood (tokens, context windows, attention, instruction-tuning) —
> the kind of thing your AI coursework covers. That "here's the mechanism, not just
> the trick" angle is what separates this from every other prompt-tips post. Point
> me at your notes and I'll draft it.

---

*Part of [HomeForge](../README.md). See also:
[Managing Claude & ChatGPT](managing-claude-and-chatgpt.md).*
