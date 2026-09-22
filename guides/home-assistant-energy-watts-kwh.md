# Home Assistant energy monitoring: watts, kWh, counters, and resets

A plug showing 25 watts now and 500 watt-hours accumulated is answering two different questions. Power is the current rate. Energy is the amount transferred over time.

*Last checked September 22, 2026 · HomeForge*

## Audit the entities first

Open the device in Home Assistant and record every power or energy entity.

| Entity | Unit | Device class | State class | Resets? |
|---|---|---|---|---|
| Live power | W or kW | `power` | `measurement` | May fluctuate |
| Cumulative energy | Wh or kWh | `energy` | `total` or `total_increasing` | Model-dependent |

Home Assistant's Energy dashboard accepts appropriate power and energy sensors. A power sensor can be converted to estimated energy with the integral integration, but the result depends on the sampling interval and available readings.

## Test four behaviors

1. Run a known load and confirm live watts respond.
2. Leave it running long enough for cumulative energy to change.
3. Reboot or unplug the smart plug and check whether the energy counter resets or jumps.
4. Review Settings → Tools → Statistics for unit or sum errors.

Record missing periods. A device can report live power accurately while losing cumulative history during a reboot.

## Avoid inflated totals

Home Assistant warns that summing sensors which reset at slightly different times can create a temporary false value that is then stored in long-term statistics. Add cumulative sources separately when possible instead of combining resetting meters first.

Long-term statistics keep hourly aggregates. Measurement entities store mean, minimum, and maximum; metered totals maintain a sum. That makes metadata and reset behavior part of the data contract.

## Turn readings into decisions

Use live power for questions such as “is the appliance currently running?” Use accumulated energy for cost and consumption over a period. Before automating a cutoff, verify false-off conditions, startup surges, and the consequence of an incorrect decision.

## Sources

- [Home Assistant energy management](https://www.home-assistant.io/docs/energy)
- [Home Assistant energy FAQ](https://www.home-assistant.io/docs/energy/faq/)
- [Home Assistant long-term statistics](https://data.home-assistant.io/docs/statistics/)

