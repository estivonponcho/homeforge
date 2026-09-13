# Facebook group research

Status: not started. This is the next autonomous distribution task.

## Initial read-only findings (2026-09-13)

These were inspected while logged into Mike's Facebook account. No group was joined and nothing was posted.

Update after Mike's action: the Facebook UI now shows **Joined** for the official Home Assistant group. The Ideas/Projects group shows a participation request pending approval, so posting there may not be available yet.

| Candidate | Visible fit/activity | Current read |
|---|---|---|
| [Home Assistant](https://www.facebook.com/groups/HomeAssistant/) | Public; about 550.8K members. The feed visibly contains real ESP32 troubleshooting and automation projects. The UI shows Mike as Joined. | Highest reach, but lead with a genuinely useful answer or finished build. The visible feed supports project/help posts; it does not justify pasting the affiliate directory. |
| [Home Assistant Ideas, Projects and Solutions](https://www.facebook.com/groups/652178389264909/) | Public; about 162.7K members and active discussion. The feed showed a thermostat question and Zigbee/coordinator discussions. Mike's participation request is currently pending approval. | Best thematic fit for a documented room build or automation project once approved. Do not attempt to post while pending. |
| [HASS / Home Assistant](https://www.facebook.com/groups/1216209051846537/) | Public; about 17K members in Facebook search results. | Smaller test community; research rules and recent post style before considering it. |

Facebook's related-group panel surfaced **Home Server Setups** (public, about 424K members, 10 posts/day), **Homelabs and Home Servers** (public, about 34K members, 10 posts/day), and **UniFi Network Official** (private, about 202K members, 10 posts/day). These are discovery leads only; inspect each group's rules before joining. The exact search `homelab self hosting` returned no results.

### Other relevant Facebook searches

- **3D Printing Community** — public, about 530K members, 90+ posts/day: https://www.facebook.com/groups/482533505156388/
- **3D Printing Makers Group | STL, 3MF & Projects** — public, about 96K members, 90+ posts/day: https://www.facebook.com/groups/573138351904168/
- **3D Printing For Beginners** — public, about 138K members, 90+ posts/day: https://www.facebook.com/groups/3041147622853548/
- **MakerWorld Projects** — public, about 26K members, 10+ posts/day: https://www.facebook.com/groups/1004868172239980/
- **Bambu Lab MakerWorld Creators** — public, about 55K members, 8 posts/day: https://www.facebook.com/groups/790217239721779/
- **B2B AI Automation Network (n8n, Claude, CRM Bots)** — public, about 139K members, 10+ posts/day: https://www.facebook.com/groups/1364459958209699/
- **Claude AI Community (Anthropic)** — public, about 88K members, 9 posts/day: https://www.facebook.com/groups/aiplanetx/
- **OpenClaw | Automation: n8n, Make | Codex | AI Agents | Claude AI** — public, about 99K members, 20+ posts/day: https://www.facebook.com/groups/1050679009595609/
- **Agentic AI (Hermes, OpenClaw, Claude, Cowork, Google ADK, LangFlow, n8n, LangGraph)** — public, about 9.7K members, 30+ posts/day: https://www.facebook.com/groups/agentics/

The AI search also surfaced many tiny groups and several “make money with AI” groups. Those are lower priority: HomeForge should lead with a real tool, workflow, or measured local-AI build—not affiliate marketing.

**Best next candidates to inspect before joining:** 3D Printing Makers Group (project/tutorial fit), MakerWorld Projects (model/build fit), and Agentic AI (technical workflow fit). Check rules and recent posts first; do not join all of them at once.

## Recommended order

Start with the **official Home Assistant group** only after Mike has a genuinely useful, finished build or can answer a real question from personal experience. The Ideas/Projects group is the better first showcase once its pending approval clears. The first post should explain the build and invite feedback; the HomeForge link should be a secondary reference only if group rules allow it. Do not lead with affiliate picks or the Starter Kit.

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
