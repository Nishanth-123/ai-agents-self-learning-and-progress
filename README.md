# AI Agents — Self Learning & Progress

A **60-day, project-first** journey from LLM basics to production prompt-driven agents (Email Agent, LinkedIn Agent, RAG, memory, deployment).

> **One repository.** All daily projects live as folders in this repo — no submodules, no separate GitHub repos per day.

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

| Day | Folder | Topic | Status |
|-----|--------|-------|--------|
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
ai-agents-self-learning-and-progress/
├── README.md                 ← journey overview (you are here)
├── GITHUB_SETUP.md           ← clone and push instructions
├── ai-day1/                  ← Day 1 project code
├── ai-day2-structured-output/
├── …
└── day-11,12-email-agent/
```

Each folder has its own `README.md` with run instructions for that day.

---

## Quick start

```bash
git clone https://github.com/Nishanth-123/ai-agents-self-learning-and-progress.git
cd ai-agents-self-learning-and-progress
```

Pick a day folder and follow its README. **Example — Day 1:**

```bash
cd ai-day1
pip install ollama
ollama serve          # separate terminal
ollama pull llama3.2
python3 app.py
```

---

## Git workflow (single repo)

```bash
# edit code in any day folder
git add .
git commit -m "Day 5: improve agent loop"
git push origin main
```

No submodule pointers to update — everything is in one commit history.

---

## Prerequisites (most days)

- Python 3.9+
- [Ollama](https://ollama.com/) with `llama3.2` for local LLM days
- Node.js 18+ for Day 7 (React)
- Google Cloud project for Days 8–10 — credentials stay local, never committed

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
