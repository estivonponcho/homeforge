# Managing Claude & ChatGPT: the practical guide

*Most people use these tools like a search box and wonder why the output is
mediocre. The people who get real work out of them treat them like a junior
teammate you brief well and manage tightly. Here's how.*

> This guide is original writing informed by hands-on use and formal AI
> coursework. It teaches the *how*, not any one course's material.

---

## The one mental model that fixes everything

An LLM has no memory of you and no access to your intent beyond the words in its
context window. **Everything good comes from controlling that context.** Vague in,
vague out. The skill isn't "knowing the magic words" — it's consistently giving
the model the right role, the right constraints, the right examples, and the right
information, every time.

Three levers do most of the work:

1. **Role & standing instructions** — who the model should be, every time, without
   you re-typing it.
2. **Context** — the specific material the task needs (the doc, the data, the
   examples), and *nothing that distracts*.
3. **Output contract** — exactly what shape you want back, and how you'll judge it.

---

## Claude

### Standing instructions that persist
- **Projects** (claude.ai) hold a persistent set of instructions + reference
  files that apply to every chat in the project. Use one project per recurring
  job (e.g. "Newsletter drafting," "Home Assistant configs"). This is the single
  biggest upgrade over one-off chats.
- **Styles** let you save a writing voice and reuse it. Define your voice once.
- In [Claude Code](../README.md#-ai--local-llms), a `CLAUDE.md` file is the
  equivalent — durable project memory the model reads every session.

### Structure prompts with tags
Claude responds especially well to lightly-structured prompts. Wrapping the parts
of your request in simple tags removes ambiguity about what's instruction vs.
data:

```
<role>You are my copy editor.</role>
<task>Tighten the draft below without changing meaning.</task>
<constraints>Keep it under 200 words. Preserve the headings.</constraints>
<draft>
...paste the draft...
</draft>
```

This isn't superstition — separating *instruction* from *content* is what stops
the model from "answering" text that was meant to be edited.

### Work in the right surface
- **Artifacts** — for anything you'll iterate on (a document, a tool, a page).
  You get a live, editable result instead of a wall of chat text.
- **Claude Code** — for building, editing files, and automating real work on your
  machine. The power-user tier.
- **Long context** — Claude handles large inputs well; paste the whole doc rather
  than a lossy summary when the detail matters.

### Manage the context window
Long chats drift and pick up cruft. When a conversation gets muddy, **start a
fresh chat and re-state the goal** — cheaper and better than fighting a polluted
context. Keep one chat to one task.

---

## ChatGPT

### The three features that change everything
- **Custom instructions** — your standing "about me" + "how to respond." Set these
  once (what you do, your tools, your preferences, how blunt you want it). Every
  chat inherits them.
- **Projects** — group chats with shared files and instructions, like Claude's.
- **Memory** — it remembers facts across chats. Useful, but **audit it** — wrong
  or stale memories quietly degrade answers. Know how to view and prune it.

### GPTs and tools
- Custom **GPTs** are reusable, pre-briefed assistants for a repeated task — worth
  it only if you actually reuse them.
- Turn on the right **tools** for the job (web, code/data analysis, image) and
  turn them off when they add noise.

---

## Prompting that works on both

The durable patterns live in [prompting-patterns.md](prompting-patterns.md). The
short version:

- **Give a role and a goal**, not just a question.
- **Show one example** of the output you want (one good example beats three
  paragraphs of description).
- **State the constraints** (length, format, audience, what to avoid).
- **Ask for the format you'll actually use** (table, JSON, bullet list, a doc).
- **Iterate deliberately** — critique the output and ask for a specific revision,
  rather than re-rolling and hoping.

---

## Which model, when

A rough, honest heuristic (models change monthly — see the
[model-watch template](model-watch-template.md)):

| You want to… | Reach for |
|---|---|
| Build, edit files, automate real work | Claude Code |
| Long, careful writing / editing | Claude (Projects + Styles) |
| Quick answers with web + data tools | ChatGPT |
| Keep everything private / offline | A [local model](../README.md#-ai--local-llms) via Ollama |
| Learn a topic deeply | Either, in "explain like I'm skeptical" mode |

Don't be loyal to one. The pros keep two or three open and route by task.

---

## Running your own (the self-hosted angle)

You don't have to rent every token. For private, offline, or high-volume work,
run an open model locally — [Ollama](https://ollama.com/) is the one-command
on-ramp, [Open WebUI](https://openwebui.com/) gives it a ChatGPT-style face, and
on Apple Silicon a [Mac mini](../README.md#-ai--local-llms) is a shockingly
capable, quiet box for it. See the [AI & Local LLMs picks](../README.md#-ai--local-llms).

---

> **[Your take — from coursework/projects]**
> This is where your MIT AI cert and course learnings make the guide *yours*:
> a section on how these tools map to what you learned about how LLMs actually
> work (tokens, context, attention, RLHF), why the "context is everything" model
> is true under the hood, and one worked example from your own projects. Tell me
> the angle and I'll draft it from your private notes.

---

*Part of [HomeForge](../README.md) — own your home, your servers, and your AI.*
