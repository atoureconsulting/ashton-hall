# Notes — Ashton Hall Africa Tour

---

## Technical: how to update the itinerary page

### The right way (local git clone)

```bash
# 1. Check the remote port (changes each session)
git -C /home/user/website remote -v

# 2. Prep the source file (used only to extract the embedded Atoure logo)
cp /home/user/website/ashton-hall-itinerary.html /home/user/itinerary_v4.html

# 3. Run the builder from this repo
cd /home/user && python3 build_itinerary.py    # writes /home/user/itinerary_v5.html

# 4. Deploy
cp /home/user/itinerary_v5.html /home/user/website/ashton-hall-itinerary.html
git -C /home/user/website add ashton-hall-itinerary.html
git -C /home/user/website commit -m "Update itinerary"
git -C /home/user/website pull --rebase origin main
git -C /home/user/website push -u origin main
```

### NEVER do this (causes double base64 encoding → page shows raw text)
```
mcp__github__create_or_update_file   ← DO NOT USE for the large HTML file
```
It internally base64-encodes before the GitHub API call; with the embedded logo this gets double-encoded. Happened twice. Use the git clone above.

---

## How the builder is structured

`build_itinerary.py` defines three itinerary lists — `foundation`, `benin_it`, `ext_it` —
each a list of legs: `(country, [dates], [day-kinds], nights_label, tbc)`.
- day-kinds: `"arr"` (arrival), `"stream"`, `"depart"` (final day), `"open"` (unused now)
- `nights_label` like `"2 nights"`; the renderer auto-appends days = nights + 1
- To change a route: edit the relevant list, rerun, redeploy. To add a 4th tab: add a list,
  a `*_view` block, a `<label class="tg tg-?">`, an `<input id="v?">`, and CSS `#v?:checked~.view-?`.

### nights + days rule
Every leg meta and route stop shows nights AND days, days = nights + 1
(1 night = 2 days, 2 nights = 3 days). Handled centrally in `render_leg` and `route_strip`.

---

## Toggle CSS (no JavaScript)

Three hidden radio inputs (`#vf` Foundation, `#vs` With Benin, `#vx` Extended) + sibling selectors:
```css
#vf:checked ~ .view-foundation { display:block }
#vs:checked ~ .view-benin      { display:block }
#vx:checked ~ .view-ext        { display:block }
```
Works in any browser and when the file is saved/emailed as a standalone HTML.

---

## Itinerary version history

| Commit | Date | What changed |
|--------|------|--------------|
| `79f384d` | 20 Jun | First rebuild. Stored as base64 — broken. |
| `543af1c` | 20 Jun | Emergency fix — valid HTML. |
| `68d6f55` | 20 Jun | Foundation/Full toggle, 3 nights each. |
| `b38e1df` | 20 Jun | 2 nights/country. Foundation (10n) vs With Benin (12n). |
| `919d9ca` | 20 Jun | **Current** — added Extended tab (14n, Ethiopia after Cameroon); nights+days labels on all 3 tabs. |

---

## Airport codes

| Country | City | Airport | Code |
|---------|------|---------|------|
| Nigeria | Lagos | Murtala Muhammed International | LOS |
| Ghana | Accra | Kotoka International | ACC |
| Ivory Coast | Abidjan | Félix-Houphouët-Boigny International | ABJ |
| Morocco | Marrakech | Marrakesh Menara Airport | RAK |
| Benin | Cotonou | Cadjehoun Airport | COO |
| Senegal | Dakar | Blaise Diagne International | DSS |
| Cameroon | Douala | Douala International | DLA |
| Ethiopia | Addis Ababa | Bole International | ADD |

---

## Image / video generation (free, browser-based)

- **FLUX.2 [dev]** ⭐ — https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
- FLUX.1 [schnell] — https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell
- FLUX.1 [dev] — https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev
- **Wan2.1** (video) — https://huggingface.co/spaces/Wan-AI/Wan2.1
- Wan2.1 (fffiloni) — https://huggingface.co/spaces/fffiloni/Wan2.1
- HF MCP setup: https://huggingface.co/mcp

User’s laptop: Intel Iris Xe (no NVIDIA GPU) — cannot run locally.
