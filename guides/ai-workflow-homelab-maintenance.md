# An AI workflow for safer homelab maintenance and change planning

A homelab usually breaks during a reasonable change made with incomplete context. This workflow uses AI to assemble the context, expose dependencies, prepare a rollback, and turn the result into a reusable runbook.

Use it for upgrades, container migrations, storage changes, reverse-proxy edits, and moving a service between machines.

## Build a service card first

Create a compact record for the service you plan to touch:

| Field | Example |
|---|---|
| Service | AdGuard Home |
| Host | Low-power ARM utility node |
| Runtime | Container or system service |
| Data | Configuration directory and local database |
| Network | IP, ports, DNS role, proxy dependencies |
| Dependents | Router, clients, monitoring |
| Backup | Location, date, and restore test |
| Recovery access | Local console, SSH, or alternate DNS |

Do not send passwords, private keys, tokens, or public IP addresses to the model. Replace them with labels such as `[REDACTED_TOKEN]`.

## Ask for dependency discovery

```
Act as a conservative homelab change reviewer.

Change goal:
[Describe one change.]

Current service card:
[Paste the redacted card.]

Relevant configuration and command output:
<evidence>
[Paste only the necessary excerpts.]
</evidence>

Identify:
1. Direct dependencies.
2. Hidden dependencies I may have overlooked.
3. What must be backed up.
4. How I can retain recovery access.
5. Checks that must pass before the change begins.

Separate facts supported by the evidence from assumptions. Ask for missing
evidence instead of inventing details.
```

The most important output is often the overlooked dependency, not the command sequence.

## Generate a change plan with stop points

Once the inventory is correct, request a plan shaped like this:

```
Create a maintenance runbook with these sections:
- Preconditions
- Backup and restore verification
- Commands or actions, one small step at a time
- Validation after each step
- Stop conditions
- Rollback procedure
- Final health checks

Do not combine destructive and validation steps. Flag any command that deletes,
overwrites, migrates, or recursively changes files. Do not assume the backup works
unless the evidence includes a restore test.
```

Keep the generated plan as a draft until you verify commands against current documentation and your actual environment.

## Use a three-window maintenance setup

Keep three things visible:

1. The runbook.
2. A terminal or management interface where you execute one step.
3. Monitoring or a simple health-check page.

Paste results back into the conversation after each checkpoint. If the output differs from the expected result, stop and update the plan before continuing.

## Make rollback boring

A rollback should say exactly:

- What condition triggers it.
- Which service to stop.
- Which file, snapshot, or container image to restore.
- How to restore network access if DNS or routing fails.
- How to confirm the old version is healthy.

“Restore from backup” is not a rollback plan unless the backup location and restoration procedure are known.

## Finish with a change record

Ask for a compact summary based only on the session evidence:

```
Create a change record with: purpose, start state, actions taken, validation
results, problems encountered, final state, rollback status, and follow-up work.
If a fact is not present in the evidence, mark it unknown.
```

Save that record beside the service card. The next maintenance session starts with better context, and a future AI assistant does not have to reconstruct the system from scratch.

## Where AI should stop

Keep human approval at commands that delete data, change firewall or routing rules, rotate credentials, modify storage layouts, or affect services other people rely on. AI can prepare and review the work. Accountability stays with the operator.

*Related: [The Quadra low-power homelab node](../projects/quadra-homelab-node.md) and the [HomeForge homelab picks](../picks.html#homelab).*
