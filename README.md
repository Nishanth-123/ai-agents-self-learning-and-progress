# AI Agents — Self Learning & Progress

A **60-day, project-first** journey from LLM basics to production prompt-driven agents (Email Agent, LinkedIn Agent, RAG, memory, deployment).

> **Repo name:** `ai-agents-self-learning-and-progress`  
> Each day is a **separate Git submodule** with its own repository, so daily work stays isolated and the parent repo only tracks progress + pointers.

---

## Mental model

```text
LLM = Brain
Tools = Hands
Agent = LLM controlling tools
```

```text
Prompt → LLM reasons → Chooses tools → Executes tools → Observes results → Repeats → Done
```

---

## What I am building toward

| Agent | Examples |
|-------|----------|
| **Email Agent** | Personalized bulk email from Sheets, summarize inbox, draft recruiter replies, 7-day follow-ups |
| **LinkedIn Agent** | Job search, recruiter discovery, profile scraping, outreach generation, export to Sheets/DB |

**Not the goal:** ML research, training, fine-tuning, or deep learning theory.  
**The goal:** Practical AI systems engineering — tool calling, workflows, RAG, memory, deployment.

---

## Learning order (fundamentals → frameworks)

```text
OpenAI API → Tool Calling → Build Tools → Agent Loops
→ Email Agent → LinkedIn Agent → RAG → Memory
→ Production → LangGraph / CrewAI → Multi-Agent
```

---

## Progress tracker

| Day | Submodule folder | Topic | Status |
|-----|------------------|-------|--------|
| 1 | [ai-day1](./ai-day1) | Ollama chat, conversation memory | Done |
| 2 | [ai-day2-structured-output](./ai-day2-structured-output) | Structured JSON / resume parser | Done |
| 3 | [ai-day3-prompt-engineering](./ai-day3-prompt-engineering) | Role prompts, constraints, email writer | Done |
| 4 | [ai-day4-tools-with-ai](./ai-day4-tools-with-ai) | Tool schemas, weather/time tools | Done |
| 5 | [day5-agent-loop](./day5-agent-loop) | Observe → think → act loop, `MAX_STEPS` | Done |
| 6 | [day6-fastapi-agent](./day6-fastapi-agent) | FastAPI + Ollama backend layers | Done |
| 7 | [day7-ai-assistant-ui](./day7-ai-assistant-ui) | React chat UI, `messages[]` history | Done |
| 8–9 | [day8,9-gmail-agent-learning](./day8,9-gmail-agent-learning) | Gmail send/read, MIME, OAuth | Done |
| 10 | [day10-sheets-agent-learning](./day10-sheets-agent-learning) | Google Sheets read/write, service account | Done |
| 11–12 | [day-11,12-email-agent](./day-11,12-email-agent) | Prompt-driven Email Agent | Planned |

---

## Repository layout

```text
ai-agents-self-learning-and-progress/   ← this repo (parent)
├── README.md                           ← journey overview (you are here)
├── GITHUB_SETUP.md                     ← clone, submodule, publish steps
├── scripts/
│   ├── submodules.env                  ← folder ↔ GitHub repo mapping
│   ├── init-local-repos.sh             ← init parent + all submodules locally
│   └── publish-to-github.sh            ← create GitHub repos and push (needs gh)
├── ai-day1/                            ← submodule
├── ai-day2-structured-output/
├── …
└── day-11,12-email-agent/
```

---

## Quick start (clone with submodules)

```bash
git clone --recurse-submodules https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress.git
cd ai-agents-self-learning-and-progress
git submodule update --init --recursive
```

Pick a day, open its README, and follow run instructions there.

**Example — Day 1:**

```bash
cd ai-day1
pip install ollama
ollama serve          # separate terminal
ollama pull llama3.2
python3 app.py
```

---

## Working on a day (typical flow)

1. `cd <submodule-folder>`
2. Make changes, commit **inside that submodule** (its own git repo).
3. Push the submodule repo to GitHub.
4. Back at parent root: `git add <submodule-folder>` and commit the updated submodule pointer.
5. Push the parent repo.

See [GITHUB_SETUP.md](./GITHUB_SETUP.md) for first-time publish and `gh` automation.

---

## Prerequisites (most days)

- Python 3.9+
- [Ollama](https://ollama.com/) with `llama3.2` for local LLM days
- Node.js 18+ for Day 7 (React)
- Google Cloud project for Days 8–10 (Gmail / Sheets) — credentials stay local, never committed

---

## 60-day roadmap (remaining highlights)

- Foundations: OpenAI API, structured outputs, tool calling, agent loops, FastAPI
- Integrations: Gmail, Sheets, Playwright, PostgreSQL
- Agents: Email, LinkedIn, job search
- Memory: embeddings, vector DB, RAG
- Production: Redis, async jobs, scheduling, Docker, observability
- Later: LangGraph, CrewAI, multi-agent workflows

---

## License

MIT — learning and portfolio use.
