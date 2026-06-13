# Project notes for Claude

## Media generation preference
- For generating **images**, use **FLUX.2 [dev]** on the Hugging Face website:
  https://huggingface.co/spaces/black-forest-labs/FLUX.2-dev
  (Best quality for this user; supports uploading a reference image + text prompt.)
- For generating **videos**, use the **Wan2.1** Hugging Face Space:
  https://huggingface.co/spaces/Wan-AI/Wan2.1
- The user's laptop has **Intel Iris Xe graphics (no NVIDIA GPU)**, so these models
  CANNOT run locally — always point to the free browser Spaces above, not a local install.
- FLUX.2-dev is NOT available as a Claude/MCP connector (HF disabled it). Do not try to
  add it as an MCP tool; use the website. See NOTES.md for the full link list.

## Saved links
See `NOTES.md` for all saved image/video generation links.
