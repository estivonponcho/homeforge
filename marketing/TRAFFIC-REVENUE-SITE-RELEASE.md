# Traffic and revenue site release review

Status: locally built and reviewed on September 25, 2026; not deployed.

## What changes

- Add page-scoped GoatCounter click events to tagged Amazon links. Existing affiliate URLs and disclosures remain in place. The builder checks the parsed hostname and `tag` parameter and will not add the event attribute twice.
- Add a short, optional Field Notes signup after generated guides and projects. Keep the free Starter Kit available without subscribing. Source tags distinguish homepage, guide, project, and Starter Kit forms.
- Update the homepage's ZBT-1 pick to ZBT-2 for a new Home Assistant network, and label Amazon destinations as Amazon rather than another affiliate program.

## Local verification

- `python scripts/build_site.py` regenerated 32 guides, 5 builds, and 11 Model Watch pages successfully.
- `git diff --check` passed.
- Parsed all 59 local HTML pages: 101 tagged Amazon links, all 101 with click event attributes; 50 Buttondown forms. Home, Starter Kit, and presence guide forms use the intended endpoint and tags.
- Inspected the rendered beginner guide and its form in a local browser. No email was submitted.

## Release and measurement gates

1. Review the diff and deploy through the normal HomeForge site release path only after a separate deployment decision.
2. Read back the public home, Starter Kit, one guide, and picks page. Confirm tagged Amazon links retain their disclosures and click attributes.
3. Use an owner-controlled address once to verify Buttondown submission, source tag, confirmation, and unsubscribe behavior. Buttondown's tag feature may depend on the account plan; confirm in the account before relying on tag reports.
4. Confirm a click event in the HomeForge GoatCounter dashboard. Do not infer live events from local markup alone.
5. Record weekly guide landings and tagged retailer clicks alongside merchant-reported orders and commission. Mark inaccessible metrics `unknown`, not zero.

No paid promotion, newsletter send, or new Page post is part of this release review.
