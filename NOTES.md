# Notes — Ashton Hall Africa Tour

---

## Technical: how to update the itinerary page

### The right way (local git clone)
The itinerary HTML is 70KB. The only reliable way to push it is via the local git clone that exists in Claude Code sessions:

```bash
# 1. The clone is at /home/user/website — check the remote port first
git -C /home/user/website remote -v
# (port changes each session — always check)

# 2. Run the builder
cd /home/user && python3 build_itinerary.py
# This writes /home/user/itinerary_v5.html

# 3. Copy and push
cp /home/user/itinerary_v5.html /home/user/website/ashton-hall-itinerary.html
git -C /home/user/website add ashton-hall-itinerary.html
git -C /home/user/website commit -m "Update itinerary"
git -C /home/user/website push -u origin main
```

### The builder script needs the v4 file for the logo
The script (`build_itinerary.py`) reads the Atouré logo from `SRC = "/home/user/itinerary_v4.html"`.  
If that file doesn't exist, do this first:
```bash
cp /home/user/website/ashton-hall-itinerary.html /home/user/itinerary_v4.html
```
(The logo is embedded in the current live file — any version works as the source.)

### NEVER do this
```
mcp__github__create_or_update_file  ← DO NOT USE for large HTML files
```
This tool internally base64-encodes the content before sending to the GitHub API. If you pass pre-encoded base64 to it, GitHub stores the intermediate base64 string as the file literal — the page renders as raw base64 text. This happened twice and required an emergency fix each time. Always use the git clone method above.

---

## Itinerary toggle (technical)

The page uses a pure-CSS toggle (no JavaScript) — two hidden radio inputs + CSS `~` sibling selectors:  
- `#vf:checked ~ .view-foundation { display: block }` 
- `#vs:checked ~ .view-sorted { display: block }`

This means the toggle works in any browser and when the file is saved/emailed as a standalone HTML.

---

## Itinerary version history

| Commit | What it was |
|--------|-------------|
| `79f384d` | First itinerary with fixed leg IDs (Nigeria=02, Ghana=03), days→nights, hourly timings, logo. Stored as base64 (broken). |
| `543af1c` | Emergency fix — restored valid HTML. Old route: Cameroon→Ghana→Nigeria→Benin→CIV→Ethiopia→Cameroon |
| `675a5c0` | Same fix from another session |
| `68d6f55` | **Current** — Rebuilt v5 with Foundation/Full toggle. New route: Nigeria→Ghana→CIV→Morocco→Nigeria (+ conditional full route) |

---

## Route history (what changed and why)

**Original route (pre-20 Jun):** Cameroon → Nigeria → Ghana → Benin → Ivory Coast → Ethiopia → Cameroon  
**Updated route (20 Jun, from iMessage):**
- Cameroon OUT as a destination (Ashton Hall may be Nigerian → starts/ends in Nigeria)
- Benin OUT (confirmed)
- Ethiopia OUT (too far for a West Africa tour)
- Morocco IN (visa-free for most of the group, flexible slot, Marrakech)
- Senegal added to conditional full route

**Confirmed base:** Nigeria → Ghana → Ivory Coast  
**Conditional (TBC Thursday):** + Cameroon, Senegal, Benin, Morocco, Ethiopia  

---

## Airport codes used

| Country | City | Airport | Code |
|---------|------|---------|------|
| Nigeria | Lagos | Murtala Muhammed International | LOS |
| Ghana | Accra | Kotoka International | ACC |
| Ivory Coast | Abidjan | Félix-Houphouët-Boigny International | ABJ |
| Morocco | Marrakech | Marrakesh Menara Airport | RAK |
| Cameroon | Douala | Douala International | DLA |
| Senegal | Dakar | Blaise Diagne International | DSS |
| Benin | Cotonou | Cadjehoun Airport | COO |
| Ethiopia | Addis Ababa | Bole International | ADD |

---

## Image / video generation (free, browser-based)

- **FLUX.2 [dev]** ⭐ (best quality) — https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
- FLUX.1 [schnell] (fastest) — https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell
- FLUX.1 [dev] — https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev
- **Wan2.1** (video, official) — https://huggingface.co/spaces/Wan-AI/Wan2.1
- Wan2.1 (video, fffiloni) — https://huggingface.co/spaces/fffiloni/Wan2.1
- Hugging Face MCP setup: https://huggingface.co/mcp

Note: user's laptop has Intel Iris Xe (no NVIDIA GPU) → cannot run these locally. Use the cloud Spaces.
