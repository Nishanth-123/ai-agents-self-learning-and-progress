# Day 6 — FastAPI + Ollama Backend

First **AI backend service**: FastAPI exposes Ollama through layered routes (API → agent → LLM).

Part of [ai-agents-self-learning-and-progress](https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress).

## What I learned

- Virtual environments and isolated dependencies
- FastAPI routing, Pydantic models, CORS, Swagger at `/docs`
- Layered backend: `main.py` (routes) → `agent.py` → `llm.py`
- Difference between a **script** and a **system** (HTTP API for agents)

## Project structure

```text
day6-fastapi-agent/
├── app/
│   ├── main.py      # Routes: /, /agent, /chat, /summarize
│   ├── models.py    # Request/response schemas
│   ├── agent.py     # Orchestration
│   └── llm.py       # Ollama client
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9+
- Ollama running with `llama3.2`

## Run

```bash
cd day6-fastapi-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama serve   # separate terminal
uvicorn app.main:app --reload --port 8000
```

- API: http://127.0.0.1:8000  
- Docs: http://127.0.0.1:8000/docs  

**Example — chat:**

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}]}'
```

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/` | Health check |
| POST | `/agent` | Single prompt agent |
| POST | `/chat` | Multi-turn `messages[]` |
| POST | `/summarize` | Summarize text |

## Next (Day 7)

React frontend consumes `/chat` with full conversation history.
