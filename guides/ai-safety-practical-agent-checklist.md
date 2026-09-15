# Before you give an AI agent access: a practical safety checklist

You do not need to settle the debate about superintelligence to reduce the damage an everyday automation can cause.

**Published and reviewed: September 14, 2026.** HomeForge implementation advice, not a certification or guarantee of safety.

## Start with permissions, not promises

[OWASP's excessive-agency guidance](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) identifies unnecessary functions, permissions and autonomy as sources of risk. It recommends minimizing access, checking authorization outside the model, requiring approval for high-impact actions, and logging and limiting activity.

Telling a model to be careful is not the same as preventing its account from deleting a file or sending a message.

## A small checklist for a real workflow

The examples below are HomeForge's proposed operating rules. They are not claims that our projects have already passed an audit.

- **Define the task.** Write down what the agent may read, create and change. Also state what it must never do.
- **Begin read-only.** A newsletter researcher needs sources, not access to payments or your whole inbox.
- **Separate preparation from execution.** Drafting a post and publishing it should be different operations. Approval should cover the exact content and destination, and expire if either changes.
- **Use a limited account.** Restrict folders, services and credentials to the job. Keep unrelated personal and customer data out.
- **Treat retrieved content as evidence, not authority.** A web page, email or document can contain instructions aimed at the agent. It does not get to change your rules.
- **Limit repeated actions.** Set a maximum number of sends, retries and purchases. Stop on an unexpected result rather than repeating blindly.
- **Make recovery possible.** Keep version history or backups, and test a restore using disposable files.
- **Record outcomes.** Keep enough information to explain what ran and whether it succeeded, without filling logs with secrets.
- **Provide a stop control.** Know how to disable the schedule and revoke access. Test this before unattended operation.

## Three examples close to home

**Content publishing:** approve the exact draft, destination and attached link. Check whether it already posted before retrying. A failed confirmation is not proof that nothing was published.

**Personal information assistant:** begin with a small selected folder. Decide what can leave the device and how long copies and logs remain. Running the model locally does not automatically make every connected service local.

**Home automation:** start with low-consequence suggestions or light controls. Keep safety-critical devices outside experimental agent control, and retain a manual way to operate the home.

## A useful first test

For the evidence behind these recommendations and the limits of each control, see the [deep research report](ai-safety-deep-research-departures-risks-mitigations.md).

Use dummy files and an account that cannot affect real customers. Try a normal request, a duplicate request, a missing-data case, and a document that tells the assistant to ignore its instructions. Check both the output and the actions actually taken. A passing small test reduces uncertainty; it does not prove universal safety.

For the broader debate, read [what is confirmed in the September frontier discussion](ai-safety-frontier-debate-september-2026.md). This guide contains no affiliate links.
