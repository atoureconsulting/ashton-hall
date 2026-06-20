# Ashton Hall Africa Tour — Project Context

Last updated: 20 Jun 2026. Read this before doing anything on this project.

---

## What this project is

Atouré Consulting is organising a West Africa content tour for **Ashton Hall**, a US fitness/lifestyle influencer. He visits multiple African countries, does a live stream experience in each one, and the whole thing is documented/broadcast to his audience. Atouré is managing logistics, ground security, country partners, and the itinerary.

Ashton Hall is potentially from Nigeria — this is significant because it means the tour starts and ends in Lagos (not Cameroon as originally planned).

---

## Live deliverable

The itinerary page is live at:
**`atoureconsulting/website` → `ashton-hall-itinerary.html` (main branch)**

Commit `68d6f55` (20 Jun 2026): Rebuilt with Foundation/Full-route toggle. Valid HTML, 70,332 bytes. Starts with `<!doctype html>`. Do NOT use `mcp__github__create_or_update_file` to update this file — it causes double base64 encoding (see NOTES.md). Use the local git clone instead.

---

## The two itineraries (toggle on the page)

### FOUNDATION — confirmed core route
Nigeria → Ghana → Ivory Coast → Morocco (Marrakech) → Nigeria  
Starts and ends in Lagos, Nigeria. Dates: **28 Jun – 13 Jul 2026** (15 nights, 4 countries, 12 travellers)

| Leg | Country | Dates | Nights | Notes |
|-----|---------|-------|--------|-------|
| 01 | Nigeria | 28–30 Jun | 3 | Arrival leg, starts in Lagos |
| 02 | Ghana | 1–3 Jul | 3 | Accra (ACC) |
| 03 | Ivory Coast | 4–6 Jul | 3 | Abidjan (ABJ) |
| 04 | Morocco | 7–9 Jul | 3 | Marrakech (RAK) |
| 05 | Nigeria | 10–13 Jul | 3 | Return + departure leg |

### FULL ROUTE — conditional ("if countries sorted")
Nigeria → Ghana → Ivory Coast → Cameroon → Senegal → Benin → Morocco → Ethiopia → Nigeria  
Dates: **28 Jun – 21 Jul 2026** (24 nights, 8 countries)

The first 3 legs (Nigeria, Ghana, Ivory Coast) are the same confirmed dates. The remaining legs are TBC pending Thursday review:

| Leg | Country | Dates | Nights | Status |
|-----|---------|-------|--------|--------|
| 01 | Nigeria | 28–30 Jun | 3 | Confirmed |
| 02 | Ghana | 1–3 Jul | 3 | Confirmed |
| 03 | Ivory Coast | 4–6 Jul | 3 | Confirmed |
| 04 | Cameroon | 7–8 Jul | 2 | TBC |
| 05 | Senegal | 9–10 Jul | 2 | TBC |
| 06 | Benin | 11–12 Jul | 2 | TBC |
| 07 | Morocco | 13–15 Jul | 3 | TBC (Marrakech) |
| 08 | Ethiopia | 16–18 Jul | 3 | TBC |
| 09 | Nigeria | 19–21 Jul | 3 | TBC (departure) |

---

## Key route decisions (from iMessage "Baba x Ash" group)

- **Cameroon removed** from the confirmed route. Ashton Hall may actually be from Nigeria, so tour starts/ends there instead.
- **Benin removed** from confirmed stops.
- **Ethiopia removed** from confirmed stops — too far out for a mainly West Africa tour.
- **Morocco back in** — most of the group are visa-free, slots flexibly anywhere. City: Marrakech (Agadir as optional add-on if time/budget).
- **Senegal added** to the full route (TBC).
- Thursday is the review day for the conditional countries.
- Morocco ground partner (same person as before) was supposed to send confirmed details to **Dontae**. If they don't come in → Morocco may be pushed or dropped.

---

## Key people

- **Ashton Hall** — the talent/influencer. Potentially Nigerian.
- **Dontae** — receives Morocco ground partner details.
- **Billy Ashton Hall** — in the iMessage group, communicated the route changes.
- **Morocco ground partner** — same person as a previous arrangement, details TBC.
- **Atouré Consulting** — organiser. Email: atoureconsulting@gmail.com

---

## Open items (priority order)

1. Thursday review: confirm/drop Cameroon, Senegal, Benin, Morocco, Ethiopia
2. Morocco ground partner to send confirmed details (Marrakech; Agadir optional)
3. Hotel per country (all TBC)
4. Ground security team and local contact per country
5. Experience/stream content per country
6. Flight legs — nothing booked, all TBC
7. Plan for open days (Day 3 in 3-night stops)
8. Agadir add-on decision for Morocco

---

## Daily schedule template

Every country follows the same structure:
- **Day 1** — Arrival: flight lands ~20:00, airport pickup 21:00, hotel check-in 22:00, team debrief 22:30, rest 23:30
- **Day 2** — Stream: 06:00 wake, 07:30 breakfast, 10:00 briefing, 14:00 depart for location, 15:00 stream starts (~3–5 hrs), 20:00 ends, 22:00 rest
- **Day 3** (if 3-night stay) — Open day: TBC (second stream / rest / secondary activation)
- **Final country** — Day 3 is departure: same as stream day but ends with 22:00+ departure flight

SIM cards distributed on arrival at each country. New ground security team briefed each arrival night.

---

## Other project assets

- **`build_itinerary.py`** (in this repo) — Python 3 script that generates `itinerary_v5.html`. Reads the Atouré logo from `/home/user/itinerary_v4.html` (or whichever HTML file is at SRC). See NOTES.md for how to run it.
- **`build_tiers.py`** (at `/home/user/build_tiers.py` in the Claude session) — Builds sponsor tier slides (SILVER 10M / GOLD 15M / PLATINUM 25M FCFA) for CIV EN/FR Canva decks. Not yet committed to a repo.
- Atouré logo is base64-embedded in the itinerary HTML (not a separate file).
- Fonts: Cormorant Garamond + Jost from Google Fonts.

---

## Media generation preference

- For **images**: FLUX.2 [dev] on Hugging Face — https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
- For **videos**: Wan2.1 — https://huggingface.co/spaces/Wan-AI/Wan2.1
- User's laptop has Intel Iris Xe graphics (no NVIDIA GPU) — cannot run these models locally. Always use the cloud Spaces.
- See NOTES.md for the full link list.
