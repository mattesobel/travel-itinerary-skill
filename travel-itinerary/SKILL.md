---
name: travel-itinerary
description: Plan and maintain a beautiful, living travel itinerary for any trip. Use whenever someone mentions planning a trip, a vacation, a getaway, a honeymoon, a family trip, a city break, or an itinerary; names a destination they are traveling to ("help me plan Japan", "what should we do in Lisbon", "our trip to Sicily"); wants to add to or refine an existing itinerary; pastes in booking confirmations, hotel links, or travel research to organize; or wants help writing emails to hotels, restaurants, drivers, or tour operators. The core deliverable is a single, gorgeous, self-contained HTML dashboard per trip, backed by a plain-text brief and an email log. Trigger even if the word "itinerary" is never said. Any travel-planning intent counts.
---

# Travel Itinerary

This skill builds and maintains a **beautiful, living itinerary dashboard** for any trip, for anyone. The dashboard is the core asset: a single, polished HTML page the traveler can open, share with their partner or family, and feel excited about. It should look like a designer made it for this specific trip, not a generic template.

Four jobs, in priority order:

1. **Build the dashboard.** A re-themeable, self-contained HTML page with a photographic hero, a route strip, and a color-coded day-by-day timeline where the travel components (flights, transfers, lodging, marquee experiences) are clearly called out, and where each day is paired with a real photo of where they'll be. The imagery is a big part of what makes it feel special. See `references/imagery.md`.
2. **Ingest whatever the traveler drops in.** Booking confirmations, forwarded hotel emails, links to hotels and restaurants, screenshots, half-formed notes. Parse them and slot the facts into the right place. See `references/research-and-ingest.md`.
3. **Help write and track vendor emails.** Drafting clear, warm notes to hotels, restaurants, drivers, and guides, and keeping a running log of what was asked and confirmed. See `references/email-playbook.md`.
4. **Do the upfront research.** When the traveler is starting from scratch, research the destination, the right bases, seasonality, and what needs to be pre-booked, then turn it into a first draft. See `references/research-and-ingest.md`.

Two principles drive everything:

- **The dashboard is the product.** Make it bespoke to the destination, not templated. The single highest-leverage move is re-theming the palette to evoke the place.
- **It fills in over time.** You hold the full picture of every section a trip needs, but the traveler rarely has all of it at once. Capture what they have now, leave graceful placeholders for the rest, and keep updating the same files as details land. Never block on missing information, and never demand it all upfront.

## How a trip is stored

Each trip lives in its own **portable folder**, named for the trip. This works on any file system, with any agent, no special vault or app required. Inside:

- `Brief.md` — the **source of truth**. Plain-text data for every section, including TBDs. Read and update this first; the dashboard is generated from it. Start from `assets/brief-template.md`.
- `Dashboard.html` — the **beautiful living dashboard**, regenerated from the brief. Built from `assets/dashboard-template.html`. Fully self-contained: open it by double-clicking, email it as one file, no internet needed beyond Google Fonts.
- `Emails.md` — the **vendor email log**: drafts to send and a record of what each vendor confirmed. Start from `assets/vendor-emails-template.md`. Only create this once the traveler starts contacting vendors.
- `itinerary-images/` — the destination photos used by the dashboard (hero shot + one per day). The working `Dashboard.html` links to these; for sharing, also produce a self-contained copy with the images embedded (see Imagery below).
- `_inbox/` (optional) — a drop folder for raw inputs the traveler pastes or saves: confirmation PDFs, forwarded emails, screenshots, links. You read from here, extract the facts into the brief, and never delete the originals.

Keep the brief and dashboard in sync. The brief is where details accumulate; the dashboard is the rendered view. When new information arrives, update the brief first, then regenerate the affected part of the dashboard. After creating or updating files, tell the traveler in one line what changed and what the next most useful thing to nail down is.

## The section checklist (your running knowledge)

A complete itinerary covers the sections below. Hold all of them in mind at all times. At any point some will be rich and some empty. That is expected. Your job is to know what is still missing and gently pull it out over time.

1. **Trip identity** — name, who is going (couple? family? friends? solo? who specifically), the occasion or vibe in one line, destination(s).
2. **Dates & shape** — depart/return, total nights, and the stay split (how many nights in each base, in order). This is the backbone of both the route graphic and the day-by-day.
3. **Lodging** — where they are staying each leg, booked or candidate, with confirmation details when booked (conf #, loyalty program/points, check-in/out, cancellation cutoff, whose name it is under).
4. **Transfers & internal travel** — flights between legs, airport pickups, cross-leg drives, rental car or no car, trains, ferries. Target windows when not yet booked.
5. **Day by day** — for each day: which leg/location, an evocative headline, and the flow (morning / midday / afternoon / evening), plus where to eat and what to pre-book. This is the heart of it.
6. **Activities & experiences** — the marquee things (a boat day, a winery, a museum, a hike), with booking notes and weather/seasonal contingencies.
7. **Food** — standout restaurants per leg, which meal, and whether a reservation is needed.
8. **Book-now list** — everything still to reserve, roughly in order of urgency, with cancellation cutoffs flagged.
9. **Open decisions** — the choices still on the traveler (hotel A vs B, this day or that), each with your recommendation.
10. **Good to know** — the handful of orienting notes: the rhythm of the trip, seasonal realities (heat, wind, crowds), logistics philosophy (e.g. "no driving").

When something new arrives, slot it into the right section, then note out loud what the next most useful thing to nail down is. The usual order: lock the stay split, then fill days, then book the time-sensitive activities.

## Running the interview

For a brand-new trip with little information, start the interview. Ask for what is most load-bearing and missing, in small natural batches, never a wall of questions. Good first-pass questions:

- Who is going, and what is the occasion or feel you are after?
- Destination and rough dates (or just the month)?
- Any places within the destination you already want to base in, and roughly how the nights split?
- Anything already booked: flights, hotels?
- The non-negotiables: experiences, restaurants, or moments this trip has to include?

Then build a first dashboard from whatever you have, even if half of it is "TBD." Seeing it rendered is what pulls the rest of the details out of the traveler. On later sessions, skip the interview preamble. Take the new info, update the brief, refresh the dashboard, and report what changed and what is still open.

Adapt the weighting to the trip: for family trips, weight kid-friendliness, pace, naps, and logistics; for a couples trip, weight romance and downtime; for a friends trip, weight nightlife and shared experiences; for solo, weight flexibility and safety.

## Ingesting raw inputs

A traveler will often have a pile of stuff before they have a plan: a hotel booking confirmation, a forwarded email from a tour operator, a few links to places they bookmarked, a screenshot of a restaurant. Let them dump it. Your job is to turn the pile into structure.

When the traveler pastes or points you at raw material:

1. Read everything (use the `_inbox/` folder, pasted text, or attached files).
2. Extract the hard facts: dates, confirmation numbers, addresses, prices, cancellation policies, contact emails, check-in/out times.
3. Slot each fact into the right section of the brief. A booking confirmation populates Lodging or Transfers; a restaurant link becomes a Food entry; a "things to do" article seeds Activities.
4. Flag conflicts and gaps you notice (a hotel checkout that does not line up with a flight, a missing transfer between two bases).
5. Regenerate the dashboard so the new facts show up.

Full guidance, including how to parse common confirmation formats, is in `references/research-and-ingest.md`.

## Building the dashboard

Read `assets/dashboard-template.html` and adapt it. The template gives you a hero, a wave divider, a "The Journey" route strip showing each base and its nights, a color-coded day-by-day timeline, a "Good to Know" notes block, and a footer. It is fully commented to show what to change.

What makes it feel bespoke rather than templated:

- **Give it a photographic hero.** The top of the page is a single beautiful, wide shot of the destination behind the title, with a soft gradient wash over it so the text stays readable. This is the first thing the traveler sees and it sets the mood instantly. Pick the most iconic, evocative image of the trip.
- **Pair every day with a real photo.** Each day card gets a photo of where they'll actually be that day (the harbor town, the volcano, the piazza), framed with the positioning helpers so the subject is centered. This is one of the most loved parts; it turns a plan into a preview of the trip. Full sourcing, framing, captioning, and licensing guidance is in `references/imagery.md`.
- **Re-theme the palette to the destination.** Pick 4 to 6 CSS variables that evoke the place and set them at the top. Greek islands lean Aegean blue, terracotta, and gold. Sicily leans sun-baked ochre, sea blue, lemon, and volcanic charcoal. Tuscany leans olive, stone, and wine. Japan in spring leans blossom pink, ink, and pale wood. Iceland leans glacier blue, basalt, and moss. This single change does most of the work of making each dashboard distinct.
- **Color-code the legs.** Each base location gets its own accent color, used consistently in the route strip and the day cards, so the eye can follow the trip's structure.
- **Tag and headline every day.** A short tag (location or theme) and an evocative 3 to 6 word headline, then 1 to 2 warm sentences on the flow. Mark special days (an anniversary, a birthday, a marquee experience) with the gold "feature" treatment.
- **Call out the travel components clearly.** Flights, transfers, and check-ins get the "travel" card style so logistics are visible at a glance without crowding the page.
- **Keep placeholders graceful.** If a day or hotel is not decided, render it as an honest, pretty "still deciding" card rather than leaving a hole. The dashboard should look complete and intentional at every stage of planning.

Google Fonts only (a serif display + a clean sans). Responsive, soft shadows, rounded cards. No external scripts beyond fonts. No localStorage.

**Two output modes for the dashboard:**

- **Working version** (`Dashboard.html`) links to the `itinerary-images/` folder. This is lighter and easy to keep editing as the plan evolves.
- **Shareable version** (`Dashboard (Shareable).html`) has every image embedded as a base64 data URI, so it is one fully self-contained file the traveler can email or AirDrop to anyone and have it just work with no folder and no internet. Generate it with `scripts/embed_images.py` (it reads the working HTML + the images folder and writes the embedded copy). Always produce this when the traveler wants to share the dashboard.

## Imagery

The photos are a signature part of this dashboard, not decoration. Read `references/imagery.md` for the full workflow. In short:

- **Hero image:** one wide, iconic shot of the destination sits behind the title with a gradient wash over it for legibility. Set it on `header.hero` via a layered `linear-gradient(...) , url("itinerary-images/your-hero.jpg")`.
- **One photo per day:** each day card gets a real photo of where they'll be, in a `.day-photo` figure with a short caption. Use the `.pos-top` / `.pos-mid` / `.pos-low` / `.pos-left` / `.pos-right` helper classes to frame the subject well.
- **Source real, openly-licensed images** (Wikimedia Commons, Unsplash, Pexels, or similar), save them into `itinerary-images/` with descriptive kebab-case names (`taormina-isola-bella.jpg`), and keep a short credits block at the bottom of the dashboard.
- **Always write meaningful `alt` text** and lazy-load day photos (`loading="lazy"`).

## Detail vs. dashboard

The dashboard is the shareable, beautiful, partner-and-family-facing view. The brief is the operational layer. If the traveler wants a deep hour-by-hour operational walkthrough (exact timings, pre-book urgency, weather contingencies, reservation logistics), keep that depth in the brief or a companion `Detailed Day-by-Day.md`, and keep the dashboard clean and inviting. Do not crowd the dashboard with logistics.

## When booked details arrive

As reservations get confirmed, record the hard details in the brief's Lodging/Transfers sections (confirmation numbers, loyalty programs, cancellation cutoffs, whose name it is under) and move the item off the Book-now list. On the dashboard, a booked hotel can simply read as confirmed; the dashboard does not need to show confirmation numbers.

## Future: connectors and direct booking

This skill is built so it can plug into travel connectors (MCP servers, airline and hotel APIs) as they become available, without changing how it works today. See `references/integrations.md`. When a relevant connector is present, prefer pulling live data (flight status, reservation details, loyalty balances) and, where supported, taking booking actions, then write the results into the brief exactly as if the traveler had pasted them. When no connector is present, everything still works by hand. Never block on an integration.
