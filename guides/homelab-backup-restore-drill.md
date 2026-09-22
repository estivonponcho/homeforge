# A homelab backup is not finished until you restore it

A copied folder is useful. A recovery plan identifies every service dependency, restores it to a clean target, and proves that the service works with representative data.

*Last checked September 22, 2026 · HomeForge*

## Inventory by service

Do not start with disks. Start with what must return.

| Service | Definition | Persistent data | Secrets | External dependency | Recovery target |
|---|---|---|---|---|---|
| Example app | Compose file | Volume/database | Environment file | DNS name | Spare host |

Separate reproducible application files from irreplaceable data. Container images can often be downloaded again; a family photo library or original configuration cannot.

## Keep recovery material off the host

If the only backup is mounted by the failed server, one host or credential failure can take both copies away. Keep an independent copy and document how to reach it from a clean machine. Encrypt sensitive backups and protect the recovery key separately.

The familiar 3-2-1 pattern—three copies, two types of storage, one copy away from the primary site—is a useful starting structure. It is not proof of recoverability.

## Run a clean-target drill

1. Choose one bounded service.
2. Prepare a blank spare system or isolated virtual machine.
3. Restore definitions, data, and secrets from documented locations.
4. Start the service without reading from the production host.
5. Test sign-in, a representative record, one write, and one export.
6. Measure time and record every undocumented step.
7. Destroy the disposable target when the evidence is saved.

Do not connect a restored automation system to consequential devices until its identities, schedules, and outputs are reviewed.

## Test the awkward cases

- The newest backup is corrupt.
- The database version changed.
- DNS points to the old address.
- The backup key is unavailable.
- A container definition exists but its volume does not.
- The restore completes but the application cannot open its data.

## Recovery scorecard

Record recovery-point objective, recovery-time objective, newest usable backup, actual recovery time, data lost, failed checks, and the next corrective action. Repeat after major upgrades and storage changes.

Pair the drill with the [homelab maintenance workflow](ai-workflow-homelab-maintenance.html) and choose hardware using the [mini-PC decision guide](best-mini-pc-for-a-homelab.html).

## Source

- [CISA: Back Up Business Data](https://www.cisa.gov/news-events/news/back-business-data)

