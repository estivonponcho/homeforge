# HomeForge newsletter signup traction

Status: site changes prepared locally; not deployed. No subscriber addresses or emails were sent.

## Offer and placement

The signup promise is **HomeForge Field Notes**: one practical build, buying lesson, or AI workflow each week, with steps and checks a reader can use in about five minutes. The free Starter Kit remains readable without subscribing. This avoids presenting a freely accessible resource as an email-only reward.

The home page form now carries the `homepage` source tag. Each generated guide and project page has a short inline form after the article, tagged `guide-reader` or `project-reader`. The Starter Kit form carries `starter-kit`. All forms use Buttondown's standard HTML endpoint and `embed=1`, so Buttondown can handle validation and any verification step in its own response. Do not replace form submission with a JavaScript `fetch` call.

## Measurement before promotion

1. Record a baseline: unique visits to the home page, guides, projects and Starter Kit in GoatCounter; current Buttondown subscriber total; and the last four weeks of new subscribers. Keep totals aggregated, never export addresses to this repository.
2. After deployment, check that the three page types visibly render their forms and send a **single controlled test using an owner-controlled address**. Confirm that Buttondown records the expected tag and that unsubscribe/confirmation behavior works. Do not use a made-up or third-party address.
3. Compare weekly visits and new subscribers by the four source tags. Treat this as directional, since an existing subscriber may submit another form and receive a new tag without becoming a new subscriber.
4. If guide readers visit but rarely subscribe, try a concrete sample of a recent issue near the guide form. If visits are scarce, improve topic-specific links from the existing HomeForge Page posts and approved video descriptions instead of multiplying generic social posts.

## Promotion draft for later review

Page post, HomeForge identity, after the site change is live and the Page ledger/cadence check passes:

> If a HomeForge guide helped you choose the next step, Field Notes is the short follow-up: one practical build, buying lesson, or AI workflow each week. Each issue gives you steps and checks you can use, without daily email. The Starter Kit is free to read without signing up. Subscribe here if you want the next note: https://estivonponcho.github.io/homeforge/

This is a draft, not a submitted Page action. Keep group discussions self-contained and do not insert signup links where group rules prohibit promotion.

## Source notes

- Buttondown: [standard HTML form and verification behavior](https://docs.buttondown.com/building-your-subscriber-base).
- Buttondown: [embedded-form tags and returning subscribers](https://docs.buttondown.com/tags).
