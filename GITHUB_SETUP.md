# GitHub setup — parent repo + submodules

This workspace is designed as **one parent repository** and **one GitHub repo per day** (git submodules).

**Suggested parent name:** `ai-agents-self-learning-and-progress`

---

## 1. First-time local setup (on your machine)

From the `ai` folder root:

```bash
chmod +x scripts/*.sh
./scripts/init-local-repos.sh
```

This will:

- Remove the old parent `.git` setup
- Remove per-day `sync.sh` scripts (replaced by this workflow)
- Initialize each day folder as its own git repo (with `.gitignore` / README)
- Register each folder as a **submodule** in the parent (local `file://` URLs until you publish)

---

## 2. Publish to GitHub (automated)

1. Install and log in to GitHub CLI:

```bash
brew install gh   # if needed
gh auth login
```

2. Set your username and run the publisher:

```bash
export GITHUB_USER=your-github-username
./scripts/publish-to-github.sh
```

The script will:

- Create each **day repo** under `github.com/$GITHUB_USER/<repo-slug>`
- Push submodule code
- Create the **parent** repo `ai-agents-self-learning-and-progress`
- Rewrite `.gitmodules` from `file://` to `https://github.com/...`
- Push the parent

---

## 3. Publish manually (if you prefer the UI)

For **each** row in `scripts/submodules.env`:

1. Create an empty repo on GitHub (e.g. `day01-ollama-chatbot`).
2. Inside the local folder:

```bash
cd ai-day1
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/day01-ollama-chatbot.git
git push -u origin main
```

3. After all day repos exist, at parent root:

```bash
# If parent not initialized yet:
./scripts/init-local-repos.sh

# Replace file:// URLs in .gitmodules with https://github.com/... URLs, then:
git add .gitmodules
git commit -m "Point submodules to GitHub remotes"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress.git
git push -u origin main
```

---

## 4. Clone later (another machine)

```bash
git clone --recurse-submodules https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress.git
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

---

## 5. Day-to-day git workflow

**Inside a day project:**

```bash
cd day5-agent-loop
git checkout -b feature/my-change
# edit, test
git add .
git commit -m "Describe change"
git push origin main
```

**Update parent pointer:**

```bash
cd ../..
git add day5-agent-loop
git commit -m "Update day5 submodule: describe change"
git push origin main
```

---

## 6. Secrets (important)

Never commit:

- `credentials.json`, `token.pickle`, `credentials/` folders
- `.env` files with API keys

Each submodule `.gitignore` excludes these. Use local copies only.

---

## Submodule ↔ GitHub repo map

| Folder | GitHub repo slug |
|--------|------------------|
| `ai-day1` | `day01-ollama-chatbot` |
| `ai-day2-structured-output` | `day02-structured-output` |
| `ai-day3-prompt-engineering` | `day03-prompt-engineering-email-writer` |
| `ai-day4-tools-with-ai` | `day04-tool-calling` |
| `day5-agent-loop` | `day05-agent-loop` |
| `day6-fastapi-agent` | `day06-fastapi-ollama-backend` |
| `day7-ai-assistant-ui` | `day07-react-chat-ui` |
| `day8,9-gmail-agent-learning` | `day08-09-gmail-api` |
| `day10-sheets-agent-learning` | `day10-google-sheets-api` |
| `day-11,12-email-agent` | `day11-12-email-agent` |

Edit `scripts/submodules.env` if you rename repos.
