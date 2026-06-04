# Day 8–9 — Gmail API (Read, Send, Agent Tools)

Gmail as an **action tool** for agents: OAuth, read messages, send RFC822 via API.

Part of [ai-agents-self-learning-and-progress](https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress).

## What I learned

- Gmail API: `messages().send()`, search with `q=`
- MIME / `MIMEText`, headers, Base64 payload encoding (not the same as body encoding)
- Agent pattern: **Read → Reason → Act**
- Wrapping Gmail in reusable functions/classes for future `GmailTool`

## Project structure

```text
day8,9-gmail-agent-learning/
├── gmail_auth.py    # OAuth flow, token.pickle
├── gmail_reader.py  # Search / read
├── gmail_sender.py  # send_email()
├── main.py
└── README.md
```

## Prerequisites

- Google Cloud project with Gmail API enabled
- OAuth desktop credentials → `credentials.json` (local only, not committed)
- Python 3.9+

## Setup

1. Download OAuth client JSON from Google Cloud Console.
2. Save as `credentials.json` in this folder (gitignored).
3. Install deps:

```bash
python3 -m venv venv
source venv/bin/activate
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

4. Run once to complete OAuth and create `token.pickle`:

```bash
python3 main.py
```

## Security

Never commit `credentials.json` or `token.pickle`. They are listed in `.gitignore`.

## Agent perspective

| Tool | Role |
|------|------|
| `gmail_reader` | Observe inbox |
| `gmail_sender` | Act (send email) |
| LLM | Reason, draft, decide when to call tools |

## Next

Combine with Sheets (Day 10) and agent loop for the Email Agent (Days 11–12).
