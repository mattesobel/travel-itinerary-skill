# Travel Itinerary Skill

Plan a trip and get a beautiful, living itinerary you'll actually want to share.

This is an [agent skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that turns any AI assistant into a thoughtful travel planner. Tell it where you're going and it researches the destination, builds a gorgeous self-contained dashboard with a photo for every day, drafts the emails to your hotels and restaurants, and keeps everything up to date as your plans firm up. Drop in your booking confirmations and it files them for you.

It works with any agent that supports skills, and it's designed to plug into airline and hotel connectors as those become available, so one day it can pull your reservations and book for you directly.

---

## What you get

- **A beautiful dashboard for each trip.** A single HTML page with a photographic hero, a route strip showing each stop, and a color-coded day-by-day timeline. Re-themed to the destination so it looks bespoke, not templated. Open it, share it, feel excited about your trip.
- **A real photo for every day.** A hero image of the destination, plus a photo of where you'll actually be each day, framed and captioned. This is the part people love.
- **Email help that saves hours.** Drafts clear, warm notes to hotels, restaurants, drivers, and guides, and keeps a running log of what you asked and what they confirmed.
- **Upfront research.** Starting from scratch? It scopes the right bases, the season, how to get around, and what needs booking first, then builds you a first draft to react to.
- **A drop zone for your stuff.** Paste booking confirmations, forwarded emails, or links to hotels and restaurants. It pulls out the dates, confirmation numbers, and prices and slots them into your plan.
- **Two ways to share.** A lightweight working version, and a fully self-contained version with every image embedded so it travels as one file over email or AirDrop.

## How a trip is stored

Everything for a trip lives in one portable folder, so it works anywhere with any tool:

```
My Trip/
├── Brief.md                    # the source of truth (all the details, including TBDs)
├── Dashboard.html              # the beautiful living dashboard
├── Dashboard (Shareable).html  # self-contained version with images embedded
├── Emails.md                   # vendor email drafts + confirmations log
├── itinerary-images/           # the hero photo + one per day
└── _inbox/                     # optional: drop confirmations, links, screenshots here
```

## Install

### Claude (Cowork or Claude Code)

Download [`travel-itinerary.skill`](./travel-itinerary.skill) and install it:

- **Cowork:** open the `.skill` file and click **Save skill**.
- **Claude Code / other Claude surfaces:** place the `travel-itinerary/` folder in your skills directory (for Claude Code, that's `~/.claude/skills/`). See the [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for the current location.

### From source (any agent that supports skills)

Clone the repo and point your agent at the `travel-itinerary/` folder:

```bash
git clone https://github.com/<your-username>/travel-itinerary-skill.git
```

The skill is just Markdown plus a few template files and one small Python script. There's nothing to build and no dependencies to install. Any assistant that can read a `SKILL.md` and follow it can use it.

## Use it

Once installed, just talk to your assistant naturally:

- "Help me plan a week in Sicily in June."
- "Here's my hotel confirmation — add it to my Japan trip." *(paste it)*
- "Draft an email to the hotel asking about an airport transfer."
- "Add a day in Cefalù and rebuild the dashboard."
- "Make a shareable version I can email my family."

You don't have to have all the details. Give it what you have; it builds a first draft and pulls the rest out of you over time.

## Make the shareable version

The working dashboard links to your `itinerary-images/` folder. To get one self-contained file with every image baked in:

```bash
python3 travel-itinerary/scripts/embed_images.py "My Trip/Dashboard.html"
```

This writes `My Trip/Dashboard (Shareable).html` — one file you can email or AirDrop to anyone, no folder and no internet required. (Standard library only; no dependencies.)

## What's inside the skill

```
travel-itinerary/
├── SKILL.md                       # the instructions the agent follows
├── assets/
│   ├── dashboard-template.html    # the beautiful, re-themeable dashboard
│   ├── brief-template.md          # the source-of-truth structure
│   └── vendor-emails-template.md  # the email log structure
├── references/
│   ├── imagery.md                 # hero + per-day photos: sourcing, framing, licensing
│   ├── email-playbook.md          # how to draft + track vendor emails
│   ├── research-and-ingest.md     # upfront research + parsing dropped-in inputs
│   └── integrations.md            # future airline/hotel connector hooks
└── scripts/
    └── embed_images.py            # builds the self-contained shareable dashboard
```

## Roadmap: connectors and direct booking

The skill works entirely by hand today. It's also built so that when travel connectors (MCP servers, airline and hotel APIs) become available, it can pull live reservation data, check flight status, and even book directly, with your approval, then file the results into your trip automatically. A connector is always an accelerant, never a requirement, so everything keeps working with or without one. See `travel-itinerary/references/integrations.md`.

## A note on photos

The skill sources real, openly-licensed images (Wikimedia Commons, Unsplash, Pexels, and similar) and keeps a credits block on every dashboard. If you're building a dashboard just for yourself, you can of course use any images you like.

## License

MIT. See [LICENSE](./LICENSE). Use it, fork it, build on it.

---

Built by Matt Sobel. If you make something cool with it, I'd love to see it.
