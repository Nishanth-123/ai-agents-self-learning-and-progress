# GitHub setup — single monorepo

All day projects live **inside** this repository as folders. There is only **one** GitHub repo:

**https://github.com/Nishanth-123/ai-agents-self-learning-and-progress**

---

## Clone

```bash
git clone https://github.com/Nishanth-123/ai-agents-self-learning-and-progress.git
cd ai-agents-self-learning-and-progress
```

No `git submodule` commands needed.

---

## Push changes

```bash
cd /path/to/ai-agents-self-learning-and-progress
git add .
git commit -m "Describe your change"
git push origin main
```

---

## First-time setup (new machine)

```bash
gh auth login   # optional, for gh CLI
git clone https://github.com/Nishanth-123/ai-agents-self-learning-and-progress.git
```

Per-day setup (venv, npm, Ollama, Google credentials) is documented in each folder’s `README.md`.

---

## Secrets (never commit)

- `credentials.json`, `token.pickle`, `credentials/` directories
- `.env` files with API keys

These are listed in the root `.gitignore`.

---

## Project folders

| Day | Folder |
|-----|--------|
| 1 | `ai-day1` |
| 2 | `ai-day2-structured-output` |
| 3 | `ai-day3-prompt-engineering` |
| 4 | `ai-day4-tools-with-ai` |
| 5 | `day5-agent-loop` |
| 6 | `day6-fastapi-agent` |
| 7 | `day7-ai-assistant-ui` |
| 8–9 | `day8,9-gmail-agent-learning` |
| 10 | `day10-sheets-agent-learning` |
| 11–12 | `day-11,12-email-agent` |
