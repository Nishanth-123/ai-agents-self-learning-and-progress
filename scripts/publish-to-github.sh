#!/usr/bin/env bash
# Create GitHub repos for each day + parent, push all, fix .gitmodules URLs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

source "$ROOT/scripts/submodules.env"

if [[ "$GITHUB_USER" == "YOUR_GITHUB_USERNAME" ]]; then
  echo "Set your GitHub username first:"
  echo "  export GITHUB_USER=your-github-username"
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install: https://cli.github.com/"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Run: gh auth login"
  exit 1
fi

echo "==> Publishing as $GITHUB_USER"
echo ""

# Ensure local repos exist
if [[ ! -f "$ROOT/.gitmodules" ]]; then
  echo "Running init-local-repos.sh first..."
  "$ROOT/scripts/init-local-repos.sh"
fi

# Push each submodule
for entry in "${SUBMODULES[@]}"; do
  IFS='|' read -r folder slug label <<< "$entry"
  path="$ROOT/$folder"

  if [[ ! -d "$path/.git" ]]; then
    echo "SKIP (no git): $folder"
    continue
  fi

  echo "--- $slug"
  cd "$path"

  if ! git rev-parse HEAD >/dev/null 2>&1; then
    echo "    No commits in $folder — skip"
    cd "$ROOT"
    continue
  fi

  remote="https://github.com/${GITHUB_USER}/${slug}.git"

  if git remote get-url origin >/dev/null 2>&1; then
    git remote set-url origin "$remote"
  else
    git remote add origin "$remote"
  fi

  if ! gh repo view "${GITHUB_USER}/${slug}" >/dev/null 2>&1; then
    gh repo create "${GITHUB_USER}/${slug}" --public --description "$label — AI agents learning"
  fi

  git push -u origin main
  cd "$ROOT"
done

# Fix .gitmodules: file:// → https://
if [[ -f .gitmodules ]]; then
  sed -i '' "s|file://${ROOT}/|https://github.com/${GITHUB_USER}/|g" .gitmodules 2>/dev/null || \
  sed -i "s|file://${ROOT}/|https://github.com/${GITHUB_USER}/|g" .gitmodules

  # file:// paths may not include full ROOT in all cases — also fix by slug
  for entry in "${SUBMODULES[@]}"; do
    IFS='|' read -r folder slug _ <<< "$entry"
    submodule_url="https://github.com/${GITHUB_USER}/${slug}.git"
    git config -f .gitmodules "submodule.${folder}.url" "$submodule_url"
  done

  git submodule sync
  git add .gitmodules
  git commit -m "Point submodules to GitHub remotes" || true
fi

# Parent repo
parent_remote="https://github.com/${GITHUB_USER}/${PARENT_REPO}.git"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$parent_remote"
else
  git remote add origin "$parent_remote"
fi

if ! gh repo view "${GITHUB_USER}/${PARENT_REPO}" >/dev/null 2>&1; then
  gh repo create "${GITHUB_USER}/${PARENT_REPO}" --public \
    --description "60-day AI agent engineering learning journey (submodules per day)"
fi

git push -u origin main

echo ""
echo "Published:"
echo "  Parent: https://github.com/${GITHUB_USER}/${PARENT_REPO}"
echo "  Clone:  git clone --recurse-submodules ${parent_remote}"
