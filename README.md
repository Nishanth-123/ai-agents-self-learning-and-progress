# AI Agents — Self Learning & Progress

A **60-day, project-first journey** into building production-grade AI agents, covering tool calling, workflows, RAG, memory, deployment, and multi-agent systems.

The focus is **not** on training models or AI research. Instead, it is on **engineering reliable AI systems** that combine LLMs with APIs, tools, workflows, memory, retrieval, and automation.

> **One repository.** Every day's work lives inside this repository as an individual folder with its own implementation and notes.

---

# Engineering Mental Model

```text
LLM = Brain
Tools = Hands
Agent = LLM + Tools + Control Loop
Workflow = Multiple Tool Calls + State + Logic
```

```text
          User Prompt
                │
                ▼
        ┌─────────────────┐
        │       LLM       │
        │   (Reasoning)   │
        └─────────────────┘
                │
      Decides which tool to call
                │
                ▼
        ┌─────────────────┐
        │     Tools       │
        │ Gmail, Sheets   │
        │ APIs, Search    │
        └─────────────────┘
                │
        Returns structured data
                │
                ▼
        ┌─────────────────┐
        │       LLM       │
        │  Interprets     │
        │  & Synthesizes  │
        └─────────────────┘
                │
                ▼
          Final User Output
```

---

# What I'm Building Toward

| Agent                  | Capabilities                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| **Email Agent**        | Personalized outreach, recruiter communication, inbox summarization, follow-up automation |
| **LinkedIn Agent**     | Recruiter discovery, profile analysis, job search automation                              |
| **Job Search Agent**   | Find openings, filter opportunities, generate tailored applications                       |
| **RAG Agent**          | Chat with documents and company-specific knowledge bases                                  |
| **Productivity Agent** | Calendar, Sheets, reminders, workflow automation                                          |
| **Production Agents**  | Memory, scheduling, observability, deployment, multi-agent orchestration                  |

---

# Learning Philosophy

Rather than relying on frameworks from day one, this roadmap builds everything from first principles:

```text
Local LLMs
      ↓
Structured Outputs
      ↓
Prompt Engineering
      ↓
Tool Calling
      ↓
Agent Loops
      ↓
API Integrations
      ↓
Workflow Automation
      ↓
Real AI Agents
      ↓
Memory
      ↓
RAG
      ↓
Production Systems
      ↓
LangGraph / CrewAI
      ↓
Multi-Agent Architectures
```

---

# Progress Tracker

| Day   | Project                | Concepts                                            | Status |
| ----- | ---------------------- | --------------------------------------------------- | ------ |
| 1     | Ollama Fundamentals    | Local LLMs, conversation memory                     | ✅      |
| 2     | Structured Outputs     | JSON generation, parsing                            | ✅      |
| 3     | Prompt Engineering     | Roles, constraints, reusable prompts                | ✅      |
| 4     | Tool Calling           | Tool schemas, deterministic functions               | ✅      |
| 5     | Agent Loop             | Observe → Think → Act architecture                  | ✅      |
| 6     | FastAPI Agent          | Backend architecture for AI systems                 | ✅      |
| 7     | React AI UI            | Chat interface and conversation state               | ✅      |
| 8–9   | Gmail Integration      | OAuth, Gmail API, MIME parsing                      | ✅      |
| 10    | Google Sheets          | Read/write automation                               | ✅      |
| 11–12 | Email Agent            | Sheets → LLM → Gmail workflow                       | ✅      |
| 13–14 | Inbox Summarizer Agent | LLM tool calling, Gmail search, inbox summarization | ✅      |
| 15–16 | Follow-Up Agent        | Gmail threads, context engineering, workflow automation, drafts  | ✅      |
---

# Completed Projects

## Email Agent (Day 11–12)

Built a complete workflow:

```text
Google Sheets
        │
        ▼
Read pending contacts
        │
        ▼
Generate personalized email (LLM)
        │
        ▼
Validate structured output
        │
        ▼
Send through Gmail API
        │
        ▼
Update spreadsheet status
```

### Concepts Practiced

* Tool orchestration
* Structured outputs
* Prompt engineering
* Context engineering
* Gmail API integration
* Google Sheets integration
* Workflow automation
* Error handling
* State management

---

## Inbox Summarizer Agent (Day 13–14)

Built an AI agent capable of summarizing Gmail conversations using **LLM-driven tool calling**.

Architecture:

```text
User Prompt
      │
      ▼
LLM (Ollama)
      │
      ▼
read_inbox(query, max_results)
      │
      ▼
Gmail API
      │
      ▼
Structured Email Objects
      │
      ▼
LLM Summarization
      │
      ▼
Actionable Summary
```

### Major Learnings

* The LLM should **reason**, not implement API logic.
* Tools should perform **deterministic actions**.
* Simpler tool interfaces produce better tool calls.
* Returning normalized objects to the LLM is preferable to exposing raw API payloads.
* Gmail search syntax (`is:unread`, `from:...`, `label:...`) maps naturally to agent tool design.
* Tool outputs should be validated before further processing.

---

## Follow-Up Agent (Day 15–16)

Built an AI agent that identifies recruiter conversations requiring follow-up, generates personalised follow-up emails using a local LLM, and creates Gmail drafts for human review.

Architecture:

```text
Sent Mail
      │
      ▼
Fetch Gmail Threads
      │
      ▼
Normalize → SentEmail Model
      │
      ▼
Filter Unreplied Conversations (>7 days)
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Generate Structured Follow-Up
      │
      ▼
Create Gmail Draft
```

### Concepts Practiced

* Gmail thread parsing
* OAuth token refresh handling
* Domain modelling (`SentEmail`)
* Context engineering using full email threads
* Structured JSON generation
* Gmail Draft API
* Workflow orchestration
* Separation of reasoning and business logic
* Human-in-the-loop AI workflows

# Key Engineering Learnings

## Agent Engineering

* LLMs generate text, not executable business logic.
* Tool execution should remain deterministic.
* Keep reasoning inside the LLM and execution inside tools.
* Design tools with simple, stable interfaces.

---

## Context Engineering

* Better context consistently outperforms better prompting.
* Structured inputs improve reasoning quality.
* Explicit facts are preferable to implicit assumptions.

---

## Reliability Engineering

* Never blindly trust model outputs.
* Validate structured responses before execution.
* Build and verify components independently before orchestration.
* Normalize external API responses before exposing them to the LLM.
* Design domain models to isolate business logic from external APIs.

---

## Tool Design Lessons

* Simpler tool signatures improve model performance.
* Prefer one expressive parameter (e.g., Gmail query syntax) over multiple tightly coupled arguments.
* Tools should return normalized data rather than provider-specific payloads.
* The LLM decides **when** and **how** to use tools; the tool performs the action.

---

# Repository Structure

```text
ai-agents-self-learning-and-progress/
│
├── README.md
├── ai-day1/
├── ai-day2-structured-output/
├── ai-day3-prompt-engineering/
├── ai-day4-tools-with-ai/
├── day5-agent-loop/
├── day6-fastapi-agent/
├── day7-ai-assistant-ui/
├── day8-9-gmail-agent-learning/
├── day10-sheets-agent-learning/
├── day11-12-email-agent/
└── day13-14-inbox-summarizer/
├── day15-16-followup-agent/
```

Each project is self-contained and documents its own setup, implementation, and learnings.

---

# Tech Stack

* Python
* Ollama
* Local LLMs (Llama / Qwen family)
* FastAPI
* React
* Gmail API
* Google Sheets API
* JSON Schema
* REST APIs
* Gmail Draft API
* OAuth 2.0
* MIME Email Processing

---

# Current Focus

Building practical AI systems capable of:

* Tool calling
* Workflow orchestration
* Agent memory
* Retrieval (RAG)
* Long-running agents
* Multi-agent collaboration
* Production deployment

---

# Upcoming Roadmap

## Intelligent Agents

* LinkedIn Job Search Agent
* Recruiter Outreach Agent
* Automated Follow-up Agent
* Calendar & Productivity Agent

## Knowledge Systems

* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)

## Production Engineering

* PostgreSQL
* Redis
* Background Workers
* Scheduling
* Docker
* Monitoring
* Observability

## Advanced Orchestration

* LangGraph
* CrewAI
* Multi-Agent Systems

---

# Philosophy

The objective of this repository is to understand **how modern AI agents are engineered in production**, by incrementally building every layer:

* Local LLMs
* Tool calling
* Agent loops
* External integrations
* Workflows
* Memory
* Retrieval
* Production deployment
* Multi-agent orchestration

The emphasis is on **engineering robust, maintainable AI systems**, leveraging prior experience in designing scalable software rather than treating LLMs as standalone components.

---

# License

MIT — Open for learning, experimentation, and portfolio use.
