# AGENTS.md

This repository contains the **Travel Itinerary Skill**: a reusable set of instructions that turns any AI assistant or coding agent into a thoughtful travel planner. It builds a beautiful, self-contained HTML itinerary dashboard for a trip, drafts warm emails to hotels and restaurants, and organizes booking confirmations as they come in.

This file is the universal entry point. Codex, Cursor, GitHub Copilot, and other agents read `AGENTS.md` automatically, so any of them can use this skill straight from the repo with no extra setup.

## How to use this skill

The skill lives in the [`travel-itinerary/`](travel-itinerary/) folder. To use it:

1. Read [`travel-itinerary/SKILL.md`](travel-itinerary/SKILL.md) and follow it. That file is the full guide: how to run the planning interview, build the dashboard, ingest booking confirmations, and draft vendor emails.
2. Start from the templates in `travel-itinerary/assets/` (the dashboard HTML, the trip brief, and the email log).
3. Consult the deeper guides in `travel-itinerary/references/` (imagery, the email playbook, research-and-ingest) only when a task needs them.
4. Use `travel-itinerary/scripts/embed_images.py` to produce the shareable, single-file version of the dashboard.

## When to use it

When someone mentions planning a trip, a vacation, a getaway, or an itinerary, or names a destination they're traveling to, treat it as a request to use this skill. Begin from `travel-itinerary/SKILL.md` and build a first draft dashboard even if they only have a few details. Capture what they have now and fill in the rest over time. Never block on missing information.

## Good to know

- Everything here is plain Markdown plus one small Python script. There's nothing to install or build.
- The skill works best when you can search the web (for destination research and real photos) and write files (to create the dashboard and save images).
- See a finished example in [`examples/sicily-family-trip.html`](examples/sicily-family-trip.html).
