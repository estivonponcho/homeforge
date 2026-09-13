# HomeForge zero-spend distribution pipeline

Turn one documented build into reusable, reviewable distribution assets without auto-posting to communities.

## Flow

1. Source: a real build, measurement, guide, or model-watch item lands in `projects/`, `guides/`, or `newsletters/`.
2. Canonical page: publish one useful page on HomeForge with one primary call to action and affiliate disclosure where relevant.
3. Repurpose: create a newsletter issue, short-video script, five Pinterest pin concepts, a GitHub checklist, and one discussion-first community draft.
4. Review queue: automations may draft and open a PR; they must not publish to Facebook, Reddit, Discord, or personal profiles.
5. Measure: use UTM links for each channel and watch Search Console, Buttondown clicks, and Amazon clicks.

## Free automation boundaries

- GitHub Actions builds/deploys the site and runs link checks.
- The existing model-watch routine drafts notable releases only when they change a real workflow.
- The existing newsletter heartbeat prepares one non-duplicate issue weekly; it never sends it.
- Buttondown delivers the scheduled newsletter sequence.
- Human approval remains required for community posts/comments, group joins, direct outreach, and paid promotion.

## Reusable asset template

For each completed project, create a canonical page, newsletter issue, 30–60 second script, five pin titles/descriptions, and one community draft with the eligible communities recorded. Keep source notes and measurements in the project or guide file.

This scales drafting and formatting while keeping HomeForge from becoming automated spam.
