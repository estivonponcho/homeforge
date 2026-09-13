# Facebook group research

Status: not started. This is the next autonomous distribution task.

## Initial read-only findings (2026-09-13)

These were inspected while logged into Mike's Facebook account. No group was joined and nothing was posted.

| Candidate | Visible fit/activity | Current read |
|---|---|---|
| [Home Assistant](https://www.facebook.com/groups/HomeAssistant/) | Public; about 550.8K members. The discussion feed visibly contains real troubleshooting and project posts. About page describes it as the official Facebook group for Home Assistant. | Highest reach, but treat as a place to contribute a real build or answer a question—not to paste the affiliate directory. No explicit rules were visible on the public About page; inspect the join/member rules before any action. |
| [Home Assistant Ideas, Projects and Solutions](https://www.facebook.com/groups/652178389264909/) | Public; about 162.7K members and visible active discussion. The feed showed a current thermostat question with substantive replies. | Best thematic fit for a documented room build or automation project. Inspect group rules before joining or linking. |
| [HASS / Home Assistant](https://www.facebook.com/groups/1216209051846537/) | Public; about 17K members in Facebook search results. | Smaller test community; research rules and recent post style before considering it. |

The search did not return a useful homelab/self-hosting group for the exact query `homelab self hosting`, so that lane needs a second search pass using terms such as `Proxmox`, `NAS`, `self hosted`, and `home server`.

## Recommended order

Start with **Home Assistant Ideas, Projects and Solutions** once there is a finished, photographed Home Assistant build. It aligns with the current content strategy and is less overwhelming than the 550K-member official group. The first post should explain the build and invite feedback; the HomeForge link should be a secondary reference only if group rules allow it. Do not lead with affiliate picks or the Starter Kit.

Separately, the [Home Assistant Community forum](https://community.home-assistant.io/) has an explicit **Share your Projects!** category with thousands of topics; it is a strong fit for a detailed build log, but forum rules and account history still need to be respected.

For Hacker News, do not submit HomeForge's landing page or curated list as Show HN. [Official guidance](https://news.ycombinator.com/showhn.html) says Show HN is for something people can try, and specifically excludes landing pages, newsletters, and lists. A future Show HN would require a genuinely runnable HomeForge tool or open-source build.

## Guardrails

- Do not post to Mike's personal profile.
- Do not join groups, post, comment, message admins, or submit membership questions without action-time approval.
- Do not create, boost, or fund an ad campaign. Mike is not ready to spend money.
- Read and quote the current rules for each candidate group before recommending it.
- Prefer a completed build or useful checklist over a generic affiliate-site promotion.
- Disclose affiliate links clearly whenever a destination page contains them.
- Never claim hands-on testing unless the repo documents it.

## Candidate record

For each candidate, capture:

| Field | What to record |
|---|---|
| Group/post | Exact public name and URL |
| Audience fit | Which HomeForge pillar and why |
| Activity | Visible recent posting/comment activity; do not invent metrics |
| Promotion rules | Exact rule summary and where it was found |
| Link policy | Links allowed, restricted, or unclear |
| Best contribution | A build, checklist, comparison, or answer that fits naturally |
| Recommendation | Use, participate first, ask an admin, or avoid |

## First-pass search order

1. Home Assistant and local smart-home groups — lead with the one-reliable-room build.
2. Homelab/self-hosting groups — lead with the documented Quadra low-power node.
3. Functional 3D-printing groups — lead with a photographed bench or homelab fix once built.
4. Local-AI groups — lead with a measured Ollama/Open WebUI experiment, not model hype.

## Zero-spend measurement

Before any approved post, create a campaign-specific URL with UTM parameters such as:

`https://estivonponcho.github.io/homeforge/?utm_source=facebook&utm_medium=organic&utm_campaign=<group-or-topic>`

Use distinct campaign values so clicks and newsletter signups can be attributed without paying for ads.
