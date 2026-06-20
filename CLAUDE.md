# Ashton Hall Africa Tour — Project Context

Last updated: 20 Jun 2026. Read this before doing anything on this project.

---

## What this project is

Atouré Consulting is organising a West Africa content tour for **Ashton Hall**, a US fitness/lifestyle influencer. He visits multiple African countries, does a live stream experience in each one, and the whole thing is documented/broadcast to his audience. Atouré is managing logistics, ground security, country partners, and the itinerary.

Ashton Hall is potentially from Nigeria — this is significant because the tour starts and ends in Lagos.

---

## Live deliverable

The itinerary page is live at:
**`atoureconsulting/website` → `ashton-hall-itinerary.html` (main branch)**

Commit `b38e1df` (20 Jun 2026): Foundation vs With Benin toggle. Valid HTML, 55,267 bytes.

**CRITICAL: Do NOT use `mcp__github__create_or_update_file` to push this file.** It double-encodes the base64, making the page render as raw text. Always use the local git clone. See NOTES.md.

---

## The two itineraries (toggle on the page)

### FOUNDATION — 10 nights, 28 Jun – 7 Jul
Nigeria → Ghana → Ivory Coast → Morocco (Marrakech) → Nigeria  
All 2-night stays. 4 countries. 12 travellers.

| Leg | Country | Dates | Nights |
|-----|---------|-------|--------|
| 01 | Nigeria | 28–29 Jun | 2 |
| 02 | Ghana | 30 Jun–1 Jul | 2 |
| 03 | Ivory Coast | 2–3 Jul | 2 |
| 04 | Morocco | 4–5 Jul | 2 |
| 05 | Nigeria | 6–7 Jul | 2 (departure) |

### WITH BENIN — 12 nights, 28 Jun – 9 Jul
Nigeria → Ghana → Ivory Coast → Benin → Morocco (Marrakech) → Nigeria  
All 2-night stays. 5 countries. 12 travellers.

| Leg | Country | Dates | Nights |
|-----|---------|-------|--------|
| 01 | Nigeria | 28–29 Jun | 2 |
| 02 | Ghana | 30 Jun–1 Jul | 2 |
| 03 | Ivory Coast | 2–3 Jul | 2 |
| 04 | Benin | 4–5 Jul | 2 |
| 05 | Morocco | 6–7 Jul | 2 |
| 06 | Nigeria | 8–9 Jul | 2 (departure) |

---

## Per-country day structure (2-night stays)

- **Day 1** (arrival): flight lands ~20:00, airport pickup 21:00, hotel check-in 22:00, team debrief 22:30, rest 23:30
- **Day 2** (stream): 06:00 wake, 07:30 breakfast, 10:00 briefing, 14:00 depart for location, 15:00 stream starts (~3–5 hrs), 20:00 ends, 22:00 rest
- **Final country Day 2**: same schedule but ends with 22:00+ departure flight home

SIM cards distributed on arrival. New ground security team briefed each arrival night.

---

## Key route decisions (from iMessage “Baba x Ash” group)

- Tour **starts and ends in Nigeria** (Ashton Hall potentially Nigerian)
- All stays are **2 nights** (not 3)
- **Cameroon**: removed from the route
- **Senegal, Ethiopia**: removed
- **Benin**: optional add-on (toggle: “With Benin” adds 2 nights and shifts Morocco + Nigeria return by 2 days)
- **Morocco**: Marrakech. Visa-free for most of the group. Ground partner same as before — was to send confirmed details to **Dontae**.

---

## Key people

- **Ashton Hall** — the talent/influencer. Potentially Nigerian.
- **Dontae** — receives Morocco ground partner confirmed details.
- **Billy Ashton Hall** — communicated route changes via iMessage.
- **Morocco ground partner** — same person as a previous arrangement, details TBC.
- **Atouré Consulting** — organiser. Email: atoureconsulting@gmail.com

---

## Open items

1. Morocco ground partner to send confirmed details (Marrakech; Agadir add-on possible)
2. Hotel per country (all TBC)
3. Ground security team and local contact per country
4. Experience/stream content per country
5. Flight legs — nothing booked, all TBC
6. Benin leg confirmation: hotel + ground contact in Cotonou

---

## Other project assets

- **`build_itinerary.py`** (in this repo) — Python 3 script to rebuild the HTML. See NOTES.md.
- **`build_tiers.py`** (local Claude session only) — Sponsor tier slides (SILVER 10M / GOLD 15M / PLATINUM 25M FCFA) for CIV EN/FR Canva decks.
- Atouré logo is base64-embedded in the HTML. Fonts: Cormorant Garamond + Jost (Google Fonts).

---

## Media generation preference

- For **images**: FLUX.2 [dev] — https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
- For **videos**: Wan2.1 — https://huggingface.co/spaces/Wan-AI/Wan2.1
- User’s laptop: Intel Iris Xe (no NVIDIA GPU) — cannot run locally. Use cloud Spaces.
- See NOTES.md for full link list.
