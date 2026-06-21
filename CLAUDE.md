# Ashton Hall Africa Tour — Project Context

Last updated: 20 Jun 2026. Read this before doing anything on this project.

---

## What this project is

Atouré Consulting is organising a West Africa content tour for **Ashton Hall**, a US fitness/lifestyle influencer. He visits multiple African countries, does a live stream experience in each one, and the whole thing is documented/broadcast to his audience. Atouré manages logistics, ground security, country partners, and the itinerary.

Ashton Hall is potentially from Nigeria — the tour starts and ends in Lagos.

---

## Live deliverable

The itinerary page is live at:
**`atoureconsulting/website` → `ashton-hall-itinerary.html` (main branch)**

Current commit: `919d9ca` (20 Jun 2026). Valid HTML, ~82 KB. Three-tab page (see below).

**CRITICAL: Do NOT use `mcp__github__create_or_update_file` for this file.** It double-encodes the base64 logo and the page renders as raw text. Always deploy through the local git clone at `/home/user/website`. See NOTES.md.

---

## The page = 3 tabs (pure-CSS toggle, no JS)

Every leg and route stop shows **nights + days**, where days = nights + 1
(1 night = 2 days, 2 nights = 3 days). All stays are 2 nights unless marked.

### Tab 1 — FOUNDATION (10 nights, 28 Jun – 7 Jul, 4 countries)
Nigeria → Ghana → Ivory Coast → Morocco (Marrakech) → Nigeria

| Leg | Country | Dates | Nights |
|-----|---------|-------|--------|
| 01 | Nigeria | 28–29 Jun | 2 |
| 02 | Ghana | 30 Jun–1 Jul | 2 |
| 03 | Ivory Coast | 2–3 Jul | 2 |
| 04 | Morocco | 4–5 Jul | 2 |
| 05 | Nigeria | 6–7 Jul | 2 (departure) |

### Tab 2 — WITH BENIN (12 nights, 28 Jun – 9 Jul, 5 countries)
Nigeria → Ghana → Ivory Coast → Benin → Morocco (Marrakech) → Nigeria

| Leg | Country | Dates | Nights |
|-----|---------|-------|--------|
| 01 | Nigeria | 28–29 Jun | 2 |
| 02 | Ghana | 30 Jun–1 Jul | 2 |
| 03 | Ivory Coast | 2–3 Jul | 2 |
| 04 | Benin | 4–5 Jul | 2 |
| 05 | Morocco | 6–7 Jul | 2 |
| 06 | Nigeria | 8–9 Jul | 2 (departure) |

### Tab 3 — EXTENDED (14 nights, 28 Jun – 11 Jul, 7 countries)
Nigeria → Ghana → Ivory Coast → Benin (1n) → Senegal → Cameroon (1n) → Ethiopia → Nigeria

| Leg | Country | Dates | Nights |
|-----|---------|-------|--------|
| 01 | Nigeria | 28–29 Jun | 2 |
| 02 | Ghana | 30 Jun–1 Jul | 2 |
| 03 | Ivory Coast | 2–3 Jul | 2 |
| 04 | Benin | 4 Jul | 1 |
| 05 | Senegal | 5–6 Jul | 2 |
| 06 | Cameroon | 7 Jul | 1 |
| 07 | Ethiopia | 8–9 Jul | 2 |
| 08 | Nigeria | 10–11 Jul | 2 (departure) |

---

## Per-country day structure

- **Day 1** (arrival): flight lands ~20:00, pickup 21:00, hotel check-in 22:00, debrief 22:30, rest 23:30
- **Day 2** (stream): 06:00 wake, 07:30 breakfast, 10:00 briefing, 14:00 depart, 15:00 stream (~3–5 hrs), 20:00 ends, 22:00 rest
- **Final country**: last day is the departure (same as stream but ends with 22:00+ flight home)
- **1-night hops** (Benin, Cameroon in Extended): arrival card only; onward travel the next day

SIM cards distributed on arrival. New ground security team briefed each arrival night.

---

## Route decision history (from iMessage “Baba x Ash” group)

- Tour **starts and ends in Nigeria** (Ashton Hall potentially Nigerian)
- Stays moved from 3 nights → **2 nights** each
- **Cameroon**: dropped from confirmed, returns only in the Extended tab (1-night hop)
- **Morocco**: Marrakech. Visa-free for most of the group. In Foundation & With Benin; NOT in Extended. Ground partner (same as before) to send details to **Dontae**.
- **Benin**: optional — 2 nights in the With Benin tab, 1-night hop in Extended
- **Senegal, Ethiopia**: appear only in the Extended tab

---

## Key people

- **Ashton Hall** — talent/influencer. Potentially Nigerian.
- **Dontae** — receives Morocco ground partner details.
- **Billy Ashton Hall** — communicated route changes via iMessage.
- **Morocco ground partner** — same person as a previous arrangement, details TBC.
- **Atouré Consulting** — organiser. Email: atoureconsulting@gmail.com

---

## Open items

1. Morocco ground partner to confirm details (Marrakech; Agadir add-on possible)
2. Hotels per country (all TBC)
3. Ground security team and local contact per country
4. Experience/stream content per country
5. Flight legs — nothing booked, all TBC
6. Extended tab: confirm 1-night hops (Benin, Cameroon) are workable; tight Cameroon→Ethiopia→Nigeria end sequence

---

## Other project assets

- **`build_itinerary.py`** (in this repo) — Python 3 generator for the page. See NOTES.md to run/deploy.
- **`build_tiers.py`** (local Claude session only) — Sponsor tier slides (SILVER 10M / GOLD 15M / PLATINUM 25M FCFA) for CIV EN/FR Canva decks.
- Atouré logo is base64-embedded in the HTML. Fonts: Cormorant Garamond + Jost (Google Fonts).

---

## Media generation preference

- **Images**: FLUX.2 [dev] — https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
- **Videos**: Wan2.1 — https://huggingface.co/spaces/Wan-AI/Wan2.1
- User’s laptop: Intel Iris Xe (no NVIDIA GPU) — cannot run locally. Use the cloud Spaces.
- Full link list in NOTES.md.
