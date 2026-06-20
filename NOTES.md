# Notes — Ashton Hall Africa Tour

---

## Technical: how to update the itinerary page

### The right way (local git clone)

```bash
# 1. Check the remote port (changes each session)
git -C /home/user/website remote -v

# 2. Prepare source file for logo extraction
cp /home/user/website/ashton-hall-itinerary.html /home/user/itinerary_v4.html

# 3. Clone this ashton-hall repo and run the builder
cd /home/user && python3 build_itinerary.py
# writes /home/user/itinerary_v5.html

# 4. Deploy
cp /home/user/itinerary_v5.html /home/user/website/ashton-hall-itinerary.html
git -C /home/user/website add ashton-hall-itinerary.html
git -C /home/user/website commit -m "Update itinerary"
git -C /home/user/website push -u origin main
```

### NEVER do this (causes double base64 encoding)
```
mcp__github__create_or_update_file  ← DO NOT USE for large HTML files
```
This tool internally base64-encodes before sending to GitHub API. If content already contains embedded base64 (like the logo), GitHub stores the intermediate string literally — the page renders as raw text. Happened twice.

---

## Itinerary version history

| Commit | Date | What changed |
|--------|------|--------------|
| `79f384d` | 20 Jun | First rebuild (leg IDs, nights, timings, logo). Stored as base64 — broken. |
| `543af1c` | 20 Jun | Emergency fix — valid HTML. Old route: Cam→Gh→Ng→Ben→CIV→Eth→Cam |
| `68d6f55` | 20 Jun | Foundation/Full toggle (3 nights each). Nigeria start/end. Sorted route had Cameroon/Senegal/Benin/Ethiopia TBC. |
| `b38e1df` | 20 Jun | **Current** — 2 nights per country. Toggle: Foundation (10n, 28 Jun–7 Jul) vs With Benin (12n, 28 Jun–9 Jul). |

---

## Toggle CSS (no JavaScript)

The page uses pure-CSS toggle — two hidden radio inputs + sibling selectors:
```css
#vf:checked ~ .view-foundation { display: block }
#vs:checked ~ .view-benin     { display: block }
```
Works in any browser and when saved/emailed as a standalone HTML file.

---

## Airport codes

| Country | City | Airport | Code |
|---------|------|---------|------|
| Nigeria | Lagos | Murtala Muhammed International | LOS |
| Ghana | Accra | Kotoka International | ACC |
| Ivory Coast | Abidjan | Félix-Houphouët-Boigny International | ABJ |
| Morocco | Marrakech | Marrakesh Menara Airport | RAK |
| Benin | Cotonou | Cadjehoun Airport | COO |
| Cameroon | Douala | Douala International | DLA |
| Senegal | Dakar | Blaise Diagne International | DSS |
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
