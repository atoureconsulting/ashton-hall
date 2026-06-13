#!/bin/bash
# SessionStart hook: ensure the Wan2.1 source tree is available in every session.
#
# Wan2.1 is a large external GPU model. This hook only makes the *source code*
# present so it can be read/used/extended from any Claude Code session. Actually
# running video generation additionally requires an NVIDIA GPU and the model
# weights, which are NOT installed here (see the deps block below to enable on a
# GPU-equipped environment).
set -euo pipefail

REPO_URL="https://github.com/Wan-Video/Wan2.1.git"
DEST="${CLAUDE_PROJECT_DIR:-$(pwd)}/Wan2.1"

if [ -d "$DEST/.git" ]; then
  echo "[session-start] Wan2.1 already present at $DEST — skipping clone."
else
  echo "[session-start] Cloning Wan2.1 into $DEST ..."
  git clone --depth 1 "$REPO_URL" "$DEST"
fi

# --- Optional: install Python deps + run on a GPU-equipped environment ---------
# Disabled by default: torch is large and flash_attn only builds against CUDA,
# so this would fail/timeout in a standard (GPU-less) web session. Uncomment on
# an environment that has an NVIDIA GPU.
#
# if command -v nvidia-smi >/dev/null 2>&1; then
#   pip install -r "$DEST/requirements.txt"
# fi

echo "[session-start] Wan2.1 is ready at $DEST"
