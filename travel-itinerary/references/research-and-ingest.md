# Research & Ingest

Two ways a trip gets populated: research you do from scratch, and raw material the traveler drops in. Both end the same way, with facts slotted into the brief and the dashboard regenerated.

## Upfront research (starting from scratch)

When the traveler has a destination and dates but not much else, do the homework before building. Research, then propose, then build a first draft they can react to.

What to figure out:

- **The right bases.** For the number of nights, how many places should they stay and where? Avoid one-night hops unless unavoidable. Propose a stay split (e.g. "4 nights west coast, 3 nights interior, 2 nights capital").
- **Seasonality and timing.** Weather for those dates, crowd levels, what is open or closed, festivals or closures, daylight hours. Flag anything that should reshape the plan (a town that sleeps in winter, a beach trip in the windy month).
- **Getting around.** Whether to rent a car, rely on trains, hire drivers, or take ferries between legs. This shapes the whole logistics philosophy.
- **What must be pre-booked.** The experiences and restaurants that sell out (a famous tasting menu, a permit, a popular boat day) versus what can be walk-in. This seeds the Book-now list with the right urgency order.
- **A handful of marquee experiences** worth building days around, plus standout food per base.

Then write a first brief from the research, build the dashboard, and present it. Be explicit about what is a researched suggestion versus a fixed fact. Seeing a rendered first draft is what pulls the traveler's real preferences out.

If a deep-research capability is available, use it for the destination scan. Otherwise do focused searches. Either way, prefer recent sources and sanity-check seasonal claims against the actual travel dates.

## Ingesting raw inputs (the drop zone)

A traveler often has a pile of material before they have a plan: a hotel confirmation, a forwarded operator email, bookmarked links, a screenshot of a restaurant, scribbled notes. Let them dump all of it, in the chat or into the trip's `_inbox/` folder. Turn the pile into structure.

### Process

1. **Read everything** the traveler provides: pasted text, attached files, links, or the `_inbox/` folder. Open PDFs and images; read confirmation emails fully.
2. **Extract the hard facts.** For each item, pull out the structured details (see the field list below).
3. **Slot each fact into the brief.** A lodging confirmation populates Lodging; a flight or transfer goes to Transfers; a restaurant link becomes a Food entry; a "things to do" article seeds Activities; a date anchors the day-by-day.
4. **Flag conflicts and gaps.** Watch for a checkout that does not line up with a flight, two bookings that overlap, a missing transfer between two bases, a reservation in the wrong city, a cancellation cutoff that is approaching.
5. **Regenerate the dashboard** so the new facts appear, and report in one line what changed and what is still open.
6. **Never delete the originals.** The `_inbox/` material is the receipt; the brief is the extracted truth.

### What to extract, by input type

- **Hotel / lodging confirmation:** property name and address, check-in and check-out dates and times, confirmation number, rate and total, loyalty program/points, whose name it is under, cancellation deadline, included extras (breakfast, transfer).
- **Flight confirmation:** airline, flight number, record locator/PNR, departure and arrival airports, dates, times, seat/cabin, baggage, who is on the booking.
- **Train / ferry / car rental:** operator, route, date and time, confirmation number, pickup/return location, price, terms.
- **Restaurant confirmation or link:** name, location, the meal and time if booked, whether a reservation is needed, cuisine, price band, any tasting-menu-only constraint.
- **Tour / experience:** operator, what it is, date and time, private vs shared, duration, price, deposit, cancellation policy, meeting point, weather backup.
- **A link with no booking yet:** capture the name and why it is interesting, and add it to the right section as a candidate, not a confirmed item.

### Handling messy or partial inputs

Extract what is clearly there, and mark the rest TBD rather than guessing. If a date is ambiguous (9/1 could be Jan 9 or Sep 1), note the ambiguity and confirm with the traveler instead of assuming. If two sources disagree (an email says €40, a later one says €60), surface the discrepancy in the brief and flag it.

The goal: the traveler dumps, you organize, and within one pass they have a brief that reflects everything they handed you and a dashboard that looks intentional.
