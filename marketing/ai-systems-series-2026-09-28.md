# HomeForge AI systems series — article and social copy

Status: **Prepared locally; not submitted**

## 1. Prompt injection is a path, not a sentence

Article: `https://estivonponcho.github.io/homeforge/guides/prompt-injection-source-sink-checklist.html`

### Facebook / Instagram

The dangerous part of a prompt injection is not the sentence hidden in a webpage.

It is the action an AI agent can take after reading it.

Here is the 5-part map I would build before connecting an agent to email, cloud storage, browsers, or MCP tools:

1 -> SOURCES

List every place an outsider can influence what the agent reads: webpages, email, shared documents, repository files, tool results, and persistent memory.

2 -> SINKS

List every capability that can create harm: send, publish, delete, spend, change permissions, run code, or transmit private data.

3 -> PATHS

Draw the shortest path from each source to each sink. Raw outside text should not be able to choose a sensitive tool call.

4 -> BOUNDARIES

Use schemas, narrow permissions, network rules, and tool-level policy. A model instruction can reduce risk; a hard boundary limits what happens when the model is persuaded anyway.

5 -> RECEIPTS

Record the exact approved action and the external result. If a submission is ambiguous, reconcile it before trying again.

The useful question is not “Can my filter recognize every malicious prompt?”

It is “What can the agent do if one gets through?”

Full source-backed checklist:
https://estivonponcho.github.io/homeforge/guides/prompt-injection-source-sink-checklist.html?utm_source=facebook&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=source_sink

Original HomeForge illustration. Educational systems guidance; no claim of perfect detection. Some HomeForge links may be affiliate links; purchases may earn a commission at no extra cost to you.

### Short post

Prompt injection becomes dangerous when untrusted content can reach a sensitive action. Map the source, the sink, the path, the hard boundary, and the receipt. Full checklist: https://estivonponcho.github.io/homeforge/guides/prompt-injection-source-sink-checklist.html?utm_source=instagram&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=source_sink_short

## 2. Another permission popup will not contain your agent

Article: `https://estivonponcho.github.io/homeforge/guides/ai-agent-containment-vs-approval-fatigue.html`

### Facebook / Instagram

If an AI agent asks for approval every thirty seconds, users eventually stop reviewing and start clicking.

That is approval fatigue, and it can turn a safety feature into a reflex test.

Build four containment layers instead:

layer 1 -> WORKSPACE

Let the agent write inside one project. Keep unrelated files outside the boundary.

layer 2 -> NETWORK

Start with no outbound access. Add only the destinations the task needs. Public research does not automatically need your signed-in email session.

layer 3 -> IDENTITY

Use narrow scopes and short-lived credentials. Reading one repository should not grant organization administration.

layer 4 -> APPROVAL

Reserve review for actions that still matter inside the boundary: publish, send, delete, spend, deploy, or change access.

Containment decides what the agent can do. Model instructions and classifiers influence what it tends to do. You want both layers.

Full source-backed guide:
https://estivonponcho.github.io/homeforge/guides/ai-agent-containment-vs-approval-fatigue.html?utm_source=facebook&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=containment

Original HomeForge illustration. Educational systems guidance; results cited from vendor engineering reports are not universal benchmarks. Some HomeForge links may be affiliate links; purchases may earn a commission at no extra cost to you.

### Short post

A confusing approval popup is not meaningful oversight. Bound the workspace, network, and identity first; reserve human review for the actions whose consequences still matter. https://estivonponcho.github.io/homeforge/guides/ai-agent-containment-vs-approval-fatigue.html?utm_source=instagram&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=containment_short

## 3. MCP is the connection, not the policy

Article: `https://estivonponcho.github.io/homeforge/guides/mcp-2026-authorization-checklist.html`

### Facebook / Instagram

An MCP server can work perfectly in a demo and still have an authorization problem.

The protocol standardizes how an AI host talks to tools. Your application still owns trust, identity, scope, approval, isolation, and proof.

Before connecting an MCP server, check seven things:

1 -> who operates it and how it updates

2 -> which tools are public and which require authorization

3 -> whether tokens are validated for the correct issuer and resource

4 -> whether read, write, publish, delete, and admin use separate scopes

5 -> whether tool results are treated as untrusted content

6 -> whether consequential actions pause for exact review

7 -> whether the destination provides a real receipt

The July 28, 2026 MCP specification also changed the transport, added routing headers, strengthened authorization, moved Tasks into an extension, and deprecated several older features.

Full practical checklist:
https://estivonponcho.github.io/homeforge/guides/mcp-2026-authorization-checklist.html?utm_source=facebook&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=mcp_auth

Original HomeForge illustration. Educational implementation guidance; verify the current MCP specification and your identity provider before production use. Some HomeForge links may be affiliate links; purchases may earn a commission at no extra cost to you.

### Short post

MCP standardizes the connection between an AI host and a tool server. It does not decide which tools an agent should call. Check identity, scope, approval, isolation, and receipts: https://estivonponcho.github.io/homeforge/guides/mcp-2026-authorization-checklist.html?utm_source=instagram&utm_medium=organic_social&utm_campaign=hf_ai_systems_sep28&utm_content=mcp_auth_short

