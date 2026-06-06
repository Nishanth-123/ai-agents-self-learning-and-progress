# AI Agents — Self Learning & Progress

A **60-day, project-first** journey from LLM fundamentals to production-grade AI agents, covering tool calling, workflows, RAG, memory, deployment, and multi-agent systems.

> **One repository.** All daily projects live inside this repo as folders — no submodules, no separate repositories.

---

## Mental Model

```text
LLM = Brain
Tools = Hands
Agent = LLM controlling tools
```

```text
Prompt
   ↓
LLM reasons
   ↓
Chooses tools
   ↓
Executes tools
   ↓
Observes results
   ↓
Repeats until done
```

---

## What I Am Building Toward

| Agent                 | Examples                                                                            |
| --------------------- | ----------------------------------------------------------------------------------- |
| **Email Agent**       | Personalized outreach, recruiter replies, inbox summarization, follow-up automation |
| **LinkedIn Agent**    | Job search, recruiter discovery, profile analysis, outreach generation              |
| **RAG Agent**         | Chat over documents, knowledge retrieval, company-specific assistants               |
| **Production Agents** | Scheduled jobs, memory, observability, deployment, multi-agent workflows            |

**Not the goal:** ML research, model training, fine-tuning, or deep learning theory.

**The goal:** Practical AI Systems Engineering — building reliable agents that combine LLMs, tools, APIs, workflows, memory, and automation.

---

## Learning Order

```text
Ollama / LLM Fundamentals
        ↓
Structured Outputs
        ↓
Prompt Engineering
        ↓
Tool Calling
        ↓
Agent Loops
        ↓
FastAPI Agents
        ↓
Agent UI
        ↓
Gmail Integration
        ↓
Google Sheets Integration
        ↓
End-to-End Email Agent
        ↓
LinkedIn Agent
        ↓
RAG
        ↓
Memory
        ↓
Production Systems
        ↓
LangGraph / CrewAI
        ↓
Multi-Agent Systems
```

---

## Progress Tracker

| Day   | Folder                                                       | Topic                                                         | Status |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------- | ------ |
| 1     | [ai-day1](./ai-day1)                                         | Ollama chat, conversation memory                              | ✅ Done |
| 2     | [ai-day2-structured-output](./ai-day2-structured-output)     | Structured JSON, resume parser                                | ✅ Done |
| 3     | [ai-day3-prompt-engineering](./ai-day3-prompt-engineering)   | Role prompts, constraints, email writer                       | ✅ Done |
| 4     | [ai-day4-tools-with-ai](./ai-day4-tools-with-ai)             | Tool schemas, weather/time tools                              | ✅ Done |
| 5     | [day5-agent-loop](./day5-agent-loop)                         | Observe → Think → Act loop                                    | ✅ Done |
| 6     | [day6-fastapi-agent](./day6-fastapi-agent)                   | FastAPI agent architecture                                    | ✅ Done |
| 7     | [day7-ai-assistant-ui](./day7-ai-assistant-ui)               | React AI chat UI, conversation history                        | ✅ Done |
| 8–9   | [day8,9-gmail-agent-learning](./day8,9-gmail-agent-learning) | Gmail API, OAuth, MIME messages                               | ✅ Done |
| 10    | [day10-sheets-agent-learning](./day10-sheets-agent-learning) | Google Sheets read/write operations                           | ✅ Done |
| 11–12 | [day-11,12-email-agent](./day-11,12-email-agent)             | End-to-end Email Agent (Sheets → LLM → Gmail → Status Update) | ✅ Done |

---

## Completed Milestones

✅ Local LLMs with Ollama

✅ Structured JSON Outputs

✅ Prompt Engineering Fundamentals

✅ Tool Calling & Tool Schemas

✅ Agent Loops

✅ FastAPI Agent Backend

✅ React-Based AI Chat UI

✅ Gmail API Integration

✅ Google Sheets Integration

✅ End-to-End Email Agent

---

## Key Learnings So Far

### Agent Engineering

* LLMs generate text, not Python objects.
* Never trust LLM output blindly.
* Validate, clean, and parse outputs before executing actions.
* Agents are orchestration systems connecting tools, APIs, workflows, and AI.

### Context Engineering

* Better context produces better outputs.
* Context quality often matters more than prompt wording.
* Explicit facts outperform model assumptions.

### Reliability Engineering

* Build components independently before composing workflows.
* Verify integrations separately before creating agent pipelines.
* Reliability is often more important than model intelligence.

### Practical Lessons

* Structured output frequently requires cleanup and validation.
* Tool integration creates more engineering challenges than LLM calls.
* Most agent complexity comes from state management, workflows, and external systems.

---

## Featured Project

### Email Agent (Day 11–12)

Built an end-to-end Email Agent that:

```text
Google Sheets
      ↓
Read Pending Contacts
      ↓
Generate Personalized Email (Ollama)
      ↓
Parse Structured Output
      ↓
Send via Gmail API
      ↓
Update Sheet Status
```

**Key Concepts Practiced**

* Tool orchestration
* Structured outputs
* Gmail API integration
* Google Sheets integration
* Agent state management
* Prompt engineering
* Context engineering
* Workflow automation
* Error handling and output validation

---

## Repository Layout

```text
ai-agents-self-learning-and-progress/
├── README.md
├── GITHUB_SETUP.md
├── ai-day1/
├── ai-day2-structured-output/
├── ai-day3-prompt-engineering/
├── ai-day4-tools-with-ai/
├── day5-agent-loop/
├── day6-fastapi-agent/
├── day7-ai-assistant-ui/
├── day8,9-gmail-agent-learning/
├── day10-sheets-agent-learning/
└── day-11,12-email-agent/
```

Each project folder contains its own README with setup instructions and implementation notes.

---

## Quick Start

```bash
git clone https://github.com/Nishanth-123/ai-agents-self-learning-and-progress.git

cd ai-agents-self-learning-and-progress
```

Choose a day folder and follow its README.

Example:

```bash
cd ai-day1

pip install ollama

ollama serve

ollama pull llama3.2

python3 app.py
```

---

## Git Workflow

```bash
git add .

git commit -m "Day 12: Complete Email Agent"

git push origin main
```

Everything lives in a single repository and a single commit history.

---

## Prerequisites

* Python 3.9+
* Ollama with a local model (Llama 3.2 or equivalent)
* Node.js 18+ (React projects)
* Google Cloud Project (Gmail & Sheets integrations)
* Gmail API credentials (kept local, never committed)

---

## Remaining Roadmap Highlights

### Agents

* LinkedIn Job Search Agent
* Recruiter Outreach Agent
* Follow-up Automation Agent

### Knowledge Systems

* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)

### Production Engineering

* PostgreSQL
* Redis
* Async Workers
* Scheduling
* Docker
* Observability
* Monitoring

### Advanced Agent Frameworks

* LangGraph
* CrewAI
* Multi-Agent Systems

---

## License

MIT — Learning, experimentation, and portfolio use.
