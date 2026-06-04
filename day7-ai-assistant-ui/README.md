# Day 7 — React Chat UI + Conversational Architecture

Chat frontend (React + TypeScript + Tailwind + Vite) talking to the Day 6 FastAPI backend.

Part of [ai-agents-self-learning-and-progress](https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress).

## What I learned

- Vite dev server, HMR, and how it compares to Metro (React Native)
- Chat UI: messages, input, loading states
- **Stateful conversational AI**: frontend keeps `messages[]` and sends full history to backend (like OpenAI chat APIs)
- AI apps as event-driven conversation systems, not simple CRUD

## Prerequisites

- Node.js 18+
- Day 6 backend running on port 8000 (CORS enabled)

## Run

**Terminal 1 — backend (Day 6):**

```bash
cd ../day6-fastapi-agent
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 — frontend:**

```bash
cd day7-ai-assistant-ui
npm install
npm run dev
```

Open the URL Vite prints (usually http://localhost:5173).

## Key files

| File | Role |
|------|------|
| `src/App.tsx` | Chat state, send handler |
| `src/services/api.ts` | `POST /chat` to backend |
| `src/types/chat.ts` | `Message` role types |

## Architecture

```text
Browser (messages[])
    → POST /chat
    → FastAPI
    → Agent / Ollama
    → Assistant reply
```

## Future improvements

- Streaming tokens (SSE / WebSocket)
- Tool-call UI and step indicators
- Persist threads (DB / local storage)
