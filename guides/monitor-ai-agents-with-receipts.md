# How to Monitor AI Agents With Actions, Traces, and Receipts

**Last checked:** September 22, 2026

When an AI agent can use tools, the practical safety question is whether you can reconstruct what it did, stop a risky action before it runs, and investigate a failure afterward. A green dashboard is less useful than a record that answers those three questions.

Anthropic’s [2026 account of its internal agent platform](https://www.anthropic.com/institute/measuring-pace-of-ai-development) offers a concrete example. As of August, it reported about 30,000 research and engineering agents operating concurrently on its most-used internal platform. Anthropic rated 26% of its AI R&D work at “AI leads,” over 90% at “AI collaborates” or higher, and none at the fully autonomous level. These are self-reported measurements for one organization, not a universal agent benchmark.

## Two monitors have different jobs

Anthropic describes an **online monitor** that checks each agent action before execution. In more than a billion decisions analyzed for August 2026, it reported blocking 0.002%, or about one in 47,000. The purpose of an online gate is to stop or redirect a consequential action before it has an external effect.

Its **offline monitor** reads completed activity afterward. Anthropic reported roughly 100,000 flagged transcripts per week, filtered down to about 50 high-priority human reviews. This second layer can spot patterns that a single tool call hides: repeated retries, expanding scope, unexplained changes, or a chain of actions that became risky as a whole.

The two layers answer different questions: “Should this next action run?” and “What happened across the whole task?” A small HomeForge workflow needs both questions even if it runs only one agent.

## What a useful action record contains

For every external action, save enough detail that someone else could replay the reasoning without replaying the action:

1. A stable agent, task, and attempt identifier.
2. The approved goal, scope, destination, and expiration time.
3. The exact tool request and important source records.
4. The policy or preflight result, including human approval when required.
5. The external receipt: a public permalink, commit, message ID, purchase confirmation, or device response.
6. Any timeout, retry, moderation state, or unresolved outcome.

The receipt is the difference between “the assistant says it posted” and “the platform shows the exact post at this URL.” If the result is ambiguous, mark it for reconciliation before trying again. A duplicate post can be worse than a missed one.

## Three numbers that can mislead

**Coverage is not accuracy.** Anthropic reports full online and offline coverage for this platform, but also notes limits to what its monitors may detect. It used Claude to help assemble its R&D task list and another Claude judge to rate automation levels. Related models can share blind spots, so independent review matters.

**A low block rate needs context.** One in 47,000 tells you how often this particular monitor blocked a decision. It does not tell you how many bad actions were missed, how severe the blocked actions were, or whether “decision” means the same thing in another system.

**Human escalation needs an action path.** A flagged transcript matters only if a reviewer can pause the agent, revoke access, correct the record, or change a policy. Record when the case was resolved and what changed.

## A small-team implementation

Start with a task manifest: owner, goal, allowed tools, destinations, stop conditions, and the exact actions requiring review. Put a pre-action gate in front of publishing, spending, deployment, credential use, and home-device control. Log tool calls and source evidence. Then review completed and failed sessions on a schedule, sampling allowed actions as well as blocked ones.

For HomeForge content, a simple scorecard is enough: percentage of posts with verified permalinks, ambiguous submissions awaiting reconciliation, duplicate submissions, and time to resolve a failed attempt. For a smart-home agent, add device state before and after an action and a safe rollback path. For an AI research assistant, track source verification and corrected claims.

This builds on our [guide to keeping AI handoff summaries from becoming instructions](ai-agent-compaction-summary-security.html). Monitoring works best when an agent's memory, approval, action, and receipt are distinct records.

## The finish line

An agent workflow is reviewable when you can say what it was allowed to do, what it attempted, what actually happened, and how to recover. Monitoring is not a promise of perfect detection. It is a way to catch consequential mistakes sooner and make the rest diagnosable.

## Source

- [Anthropic: Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development) (August 2026 measurements and methodology)
