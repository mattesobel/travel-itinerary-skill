# Integrations (present and future)

This skill works entirely by hand today: the traveler talks, pastes, and forwards; the skill researches, drafts, and builds. It is also designed to plug into travel connectors as they appear, without changing how anything works for people who have none. The rule is simple: **a connector is an accelerant, never a requirement. Never block on one.**

## How to use a connector when one is present

At the start of a session, notice what is connected. If a relevant travel or productivity connector is available (an airline, a hotel group, a booking platform, a maps service, a calendar, or an email account), prefer it for the jobs below, then write whatever it returns into the brief exactly as if the traveler had pasted it. Always show the traveler what was pulled or what action you intend to take before taking it.

### Reading (low-risk, do freely once connected)
- **Pull reservation details** from a flight, hotel, or booking connector instead of asking the traveler to type them. Populate Lodging and Transfers automatically.
- **Check flight status, schedules, and seat maps** when an airline connector exists.
- **Read loyalty balances and program details** to inform booking decisions.
- **Pull a calendar** to anchor the trip dates and spot conflicts.
- **Read inbound vendor emails** from a connected email account and log them in `Emails.md`.

### Writing and booking (higher-risk, always confirm first)
- **Send vendor emails** through a connected email account, but only after showing the draft and getting a go-ahead.
- **Book or hold reservations** (flights, hotels, restaurants, experiences) where a connector supports it, only after presenting the exact details, price, and cancellation terms, and getting explicit approval. Then record the confirmation in the brief and move the item off the Book-now list.
- **Add events to a calendar** for flights, check-ins, and reservations once they are confirmed.

## What to look for

The kinds of connectors that map onto this skill, as they become available:

- **Airlines** (e.g. Delta, United, and others): flight search, status, reservations, loyalty.
- **Hotel groups and booking platforms:** reservation lookup, availability, booking.
- **Restaurant reservation platforms:** availability and booking.
- **Maps / places services:** addresses, travel times between bases, opening hours.
- **Calendar:** trip dates, conflicts, adding confirmed events.
- **Email:** reading vendor replies, sending drafted vendor emails.

If the traveler asks for something that clearly needs a connector that is not installed (for example, "book this flight on United"), do not fail silently. Suggest the relevant connector, and in the meantime do the part you can: produce the exact booking details, the price to expect, and a draft or step list so the traveler can complete it themselves.

## Guardrails

- Never take a booking or send a message without showing the traveler exactly what will happen and getting approval.
- Always capture confirmation numbers and cancellation terms the moment a booking is made.
- Treat connector output as input to the brief, so the trip folder stays the single portable source of truth even if connectors change.
