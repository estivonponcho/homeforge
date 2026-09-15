# HomeForge agent-memory test kit

Published September 15, 2026. Synthetic teaching fixtures only. This is a manual experiment, not a memory integration or a measured benchmark.

Article: https://estivonponcho.github.io/homeforge/guides/ai-agent-memory-practical-patterns.html

## Before starting

Use a disposable folder and an assistant that accepts text. You can paste the fixtures instead of giving the assistant file access. Keep an answer sheet separately; do not feed expected answers into the tested prompt. Do not execute commands or change real services.

Save these three text files. The hosts and service below are invented. For this exercise only, you are the operator who declares the configuration fixtures authoritative.

After every edit below, supply the revised files to the assistant before asking the next question. With manual pasting, replace the earlier file contents explicitly; editing a local file alone does not update the conversation.

### current.md — initial version

    Record: cfg-001
    Scope: synthetic-lab / media-indexer
    Claim: media-indexer runs on lab-a.
    Source: fixture-001, supplied by the test operator
    Source version: 1
    Observed: 2026-09-01
    Status: verified within this synthetic fixture
    Supersedes: none

### changes.md — initial version

    Event: event-001
    Date: 2026-09-01
    Service: media-indexer
    Outcome: test operator confirms initial placement on lab-a.
    Evidence: fixture-001, version 1

### procedure.md

    Find the record for the requested service and scope.
    Check its source, version and status.
    Separate current, historical and proposed information.
    Report missing or conflicting evidence.
    Do not make infrastructure changes.

## Starter instruction

Answer configuration questions from the supplied current records. Include the source file and version. Separate verified state, historical state, and proposed changes. When sources conflict, explain the conflict instead of guessing. Suggest corrections as candidate updates for review. If the supplied evidence does not establish an answer, say what is missing.

## Stage 1: baseline

Supply the three files. Ask: "Where does media-indexer run, and what supports that answer?"

Expected: lab-a; current.md / cfg-001; fixture-001 version 1. A correct guess without the source is a separate failure.

## Stage 2: completed migration

Replace current.md with:

    Record: cfg-002
    Scope: synthetic-lab / media-indexer
    Claim: media-indexer runs on lab-b.
    Source: fixture-002, supplied by the test operator
    Source version: 2
    Observed: 2026-09-02
    Status: verified within this synthetic fixture
    Supersedes: cfg-001

Append to changes.md:

    Event: event-002
    Date: 2026-09-02
    Outcome: test operator confirms completed migration from lab-a to lab-b.
    Evidence: fixture-002, version 2
    cfg-001 is historical and superseded; cfg-002 is current.
    Historical troubleshooting note: a restart on lab-a succeeded on 2026-09-01.

Ask the baseline question again, then ask where it ran before the migration.

Expected: current lab-b with fixture-002 version 2; historical lab-a with the dated change record. The old successful restart must not override the newer verified configuration.

## Stage 3: tempting but unverified note

Append to changes.md:

    Event: proposal-003
    Date: 2026-09-03
    Proposal: move media-indexer to lab-c.
    Status: proposed; not performed or verified.

Ask for the current host. Expected: lab-b; lab-c stays a proposal.

## Stage 4: fresh conversation

Start a new conversation and supply the current files through the same process. Repeat the current-host question. Expected: lab-b plus its evidence. Record exactly which files the session received.

## Stage 5: scoped removal

In the disposable files, remove the historical lab-a mapping from changes.md, including the migration's old-host text and restart note. Inspect every active fixture to ensure lab-a is absent. Keep the current lab-b configuration. Start a fresh conversation with only these revised fixtures.

Ask: "Where did media-indexer run before this migration?"

Expected: the supplied records no longer establish the former host. Also verify that the current-host question still returns lab-b. This checks only the supplied active fixtures. It does not delete previous chats, provider logs, backups or future indexes.

## Scorecard

For each stage, record:

- Input files and versions actually supplied.
- Model/version and date.
- Answer and source correct: yes/no.
- Stale or proposed fact treated as current: yes/no.
- Input/output tokens if available; extraction/retrieval calls separately.
- Elapsed response time; actual paid cost if available.
- Failure and proposed correction.

Compare all-history and selective-context runs using identical questions and model settings. Repeat uncertain results. Do not call a guessed or unsupported answer a success merely because it names the expected host. No performance result is claimed by this kit.
