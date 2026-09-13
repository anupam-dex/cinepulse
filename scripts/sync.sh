#!/usr/bin/env bash
# CinePulse Auto-Commit & GitHub Sync Script

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

# Check if there are changes to commit
if [[ -z $(git status --porcelain) ]]; then
  echo "✅ Working tree clean. No changes to commit."
  exit 0
fi

# Determine commit message from argument or generate milestone message
MESSAGE="$1"
if [[ -z "$MESSAGE" ]]; then
  CHANGED_FILES=$(git status --porcelain | wc -l | tr -d ' ')
  MESSAGE="chore: milestone auto-sync ($CHANGED_FILES files updated on $(date +'%Y-%m-%d %H:%M'))"
fi

echo "📦 Staging and committing changes..."
git add .
git commit -m "$MESSAGE"

# Check if remote origin exists
if git remote | grep -q "^origin$"; then
  echo "🚀 Pushing to GitHub (origin/main)..."
  git push origin main
  echo "✨ Successfully synced to GitHub!"
else
  echo "⚠️ Remote 'origin' not configured yet."
  echo "Run: git remote add origin https://github.com/anupam-dex/<REPO_NAME>.git"
fi
