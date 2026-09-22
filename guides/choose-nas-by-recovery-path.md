# Choose a NAS by failure and recovery, not bay count

Drive bays tell you how many disks fit. They do not tell you whether your applications can be restored, how long a rebuild takes, or where the independent backup lives.

*Last checked September 22, 2026 · HomeForge*

## Start with workloads

List the jobs separately:

- File sharing and documents.
- Photos and media.
- Application databases and container volumes.
- Computer backups.
- Surveillance recording.
- Virtual-machine storage.

For each one, estimate current data, annual growth, performance needs, downtime tolerance, and whether another copy exists.

## Calculate usable capacity

Raw capacity is not usable capacity. Redundancy, filesystem overhead, snapshots, free-space requirements, and reserved growth reduce what is available. Use the vendor or filesystem calculator for the exact layout and confirm drive-size constraints.

RAID or parity protects service availability during some drive failures. It does not protect against deletion, corruption, theft, fire, credential compromise, or every controller and filesystem failure.

## Ask the recovery questions

1. Can the data be read without the vendor account?
2. Can configuration and application data be exported?
3. Where is the independent backup?
4. How is the backup encrypted and how is its key recovered?
5. What happens if the NAS hardware, not a drive, fails?
6. How long will restore or rebuild take at the actual data size?
7. Which checks prove files and applications are usable?

## Compare the complete system

Include the enclosure, supported drives, additional memory, network adapters, backup destination, UPS, replacement parts, and electricity. More bays can improve layout choices but also increase cost, heat, and rebuild exposure.

## A simple acceptance test

Before moving the only copy of anything important, create synthetic files, record checksums, back them up to the independent destination, delete the working copy from a test share, and restore it. Confirm names, timestamps where required, contents, and permissions.

For an application, restore its database and configuration into an isolated instance and open representative records. A storage pool reporting healthy is different from the service being recoverable.

Use the [homelab restore drill](homelab-backup-restore-drill.html) to document the result.

## Sources

- [TrueNAS documentation](https://www.truenas.com/docs/)
- [CISA: Back Up Business Data](https://www.cisa.gov/news-events/news/back-business-data)

