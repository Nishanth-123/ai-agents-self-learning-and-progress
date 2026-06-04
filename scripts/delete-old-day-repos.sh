#!/usr/bin/env bash
# One-time cleanup: delete the old per-day GitHub repos (submodule era).
# Requires: gh auth refresh -h github.com -s delete_repo
set -euo pipefail

GITHUB_USER="${GITHUB_USER:-Nishanth-123}"

REPOS=(
  day01-ollama-chatbot
  day02-structured-output
  day03-prompt-engineering-email-writer
  day04-tool-calling
  day05-agent-loop
  day06-fastapi-ollama-backend
  day07-react-chat-ui
  day08-09-gmail-api
  day10-google-sheets-api
  day11-12-email-agent
)

if ! gh auth status >/dev/null 2>&1; then
  echo "Run: gh auth login"
  exit 1
fi

for repo in "${REPOS[@]}"; do
  if gh repo view "${GITHUB_USER}/${repo}" >/dev/null 2>&1; then
    echo "Deleting ${GITHUB_USER}/${repo}..."
    gh repo delete "${GITHUB_USER}/${repo}" --yes
  else
    echo "Already gone: ${repo}"
  fi
done

echo "Done. Keep: ${GITHUB_USER}/ai-agents-self-learning-and-progress"
