#!/usr/bin/env bash
# Initialize parent repo + per-day submodule repos (local file:// URLs).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

source "$ROOT/scripts/submodules.env"

echo "==> AI Agents learning repo — local init"
echo "    Root: $ROOT"
echo ""

# Remove old parent git and legacy sync scripts
rm -rf "$ROOT/.git"
find "$ROOT" -maxdepth 2 -name 'sync.sh' -type f -delete 2>/dev/null || true

init_child_repo() {
  local dir="$1"
  local label="$2"
  local path="$ROOT/$dir"

  if [[ ! -d "$path" ]]; then
    echo "SKIP (missing): $dir"
    return 0
  fi

  echo "--- $label ($dir)"
  rm -rf "$path/.git"

  git -C "$path" init -b main
  git -C "$path" add -A

  if git -C "$path" diff --cached --quiet; then
    echo "    (empty — skipping commit)"
    return 0
  fi

  git -C "$path" commit -m "Initial commit: $label"
}

# 1) Init each day as standalone repo
for entry in "${SUBMODULES[@]}"; do
  IFS='|' read -r folder slug label <<< "$entry"
  init_child_repo "$folder" "$label"
done

# 2) Init parent and attach submodules
git init -b main

for entry in "${SUBMODULES[@]}"; do
  IFS='|' read -r folder slug label <<< "$entry"
  path="$ROOT/$folder"

  if [[ ! -d "$path/.git" ]]; then
    continue
  fi

  if git config -f .gitmodules --get "submodule.${folder}.path" >/dev/null 2>&1; then
    echo "Already submodule: $folder"
    continue
  fi

  git submodule add "file://${path}" "$folder"
done

# Parent commit (docs + submodule pointers)
git add .gitignore README.md GITHUB_SETUP.md scripts .gitmodules 2>/dev/null || true
for entry in "${SUBMODULES[@]}"; do
  IFS='|' read -r folder _ _ <<< "$entry"
  [[ -d "$folder" ]] && git add "$folder" 2>/dev/null || true
done

if ! git diff --cached --quiet; then
  git commit -m "Initialize learning journey repo with day submodules"
fi

echo ""
echo "Done. Next: set GITHUB_USER and run ./scripts/publish-to-github.sh"
echo "Or follow manual steps in GITHUB_SETUP.md"
