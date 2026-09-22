# Restore your Home Assistant backup before you need it

A green backup status proves that Home Assistant created an archive. It does not prove that you still have the encryption material, that the archive exists away from the failed machine, or that you can restore the services your home depends on.

*Last checked September 22, 2026 · HomeForge*

This guide turns a backup into a recovery test. Use spare or disposable hardware when possible. A restore overwrites the selected parts of the target system.

## What a Home Assistant backup contains

Home Assistant's current backup documentation says a full backup can contain `config`, `share`, manually installed apps, `ssl`, and `media`. Automatic backups can run on a schedule, retain a chosen number of versions, and write to configured locations. Backups are encrypted; the emergency kit is required to restore them.

Large media and shared folders can make backups and restores slower. Decide whether they belong in the Home Assistant archive or in a separate media-backup process.

## The restore drill

### 1. Record the recovery target

Write down what must work after recovery:

- You can sign in.
- Core integrations load.
- One local light or test entity changes state.
- One important automation runs with a harmless test input.
- Add-ons or apps required by the system start.
- Historical data you chose to preserve is available.

Do not use a production door lock, alarm, garage door, heater, or other consequential device as the first test.

### 2. Export what the failed host cannot provide

Keep at least one backup away from the Home Assistant host. Store the matching emergency kit separately and test that you can locate it without relying on the failed machine.

Record the backup date, Home Assistant version, installation type, archive location, and emergency-kit location. Do not put secrets into a public checklist.

### 3. Prepare a disposable target

Install a fresh supported Home Assistant image on spare hardware or a temporary test environment appropriate for your installation. Isolate the target from production automations until the restore is complete.

During onboarding, choose the restore option and provide the archive and required key. Home Assistant notes that a large restore can take around 45 minutes because Core and apps are reinstalled.

### 4. Verify in layers

| Layer | Check | Evidence |
|---|---|---|
| Access | Sign in with the restored credentials | Successful login |
| Configuration | Expected integrations and helpers exist | Screenshot or checklist |
| Services | Required apps start without repeated errors | App status and logs |
| Devices | A harmless local test entity responds | State change and timestamp |
| Automations | A test automation reaches the expected result | Trace or log |
| History | Required long-term data is present | Known date range |

### 5. Record recovery time and failures

Measure from starting the restore to the first verified useful automation. List missing credentials, unavailable backup locations, incompatible hardware, app failures, and manual steps. These are the real recovery plan.

## Pass or fail

Pass only when a fresh target reaches the written recovery outcome. A completed backup job, readable archive, or successful login is useful evidence but not the whole result.

Repeat the drill after major installation changes, moving storage, changing encryption material, or adding a service that matters to household operation.

## Sources

- [Home Assistant: backups and restores](https://www.home-assistant.io/common-tasks/general/)
- [Home Assistant: restore from full backup action](https://www.home-assistant.io/actions/hassio.restore_full/)

