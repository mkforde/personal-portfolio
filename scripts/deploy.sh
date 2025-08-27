#!/bin/bash
set -euo pipefail

# ----------------------------
# CONFIGURATION
# ----------------------------
REMOTE_USER="root"
REMOTE_HOST="caddy"
REMOTE_BASE="/etc/caddy/site-data/portfolio"
LOCAL_PUBLIC="../public"

# Number of old releases to keep
KEEP=3

# Timestamped release folder
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
RELEASE_DIR="${REMOTE_BASE}/releases/${TIMESTAMP}"

# ----------------------------
# DEPLOY
# ----------------------------

echo "Starting deploy to ${REMOTE_HOST}..."

# 1. Sync local public/ to remote timestamped release
rsync -avz --delete "${LOCAL_PUBLIC}/" "${REMOTE_USER}@${REMOTE_HOST}:${RELEASE_DIR}/"

# 2. Update the 'current' symlink atomically
ssh "${REMOTE_USER}@${REMOTE_HOST}" "ln -sfn ${RELEASE_DIR} ${REMOTE_BASE}/current"

# 3. Optional: clean up old releases
ssh "${REMOTE_USER}@${REMOTE_HOST}" "
  cd ${REMOTE_BASE}/releases && \
  ls -dt */ | tail -n +$((KEEP+1)) | xargs -r rm -rf
"

echo "Deploy complete. Live site updated to ${TIMESTAMP}."
