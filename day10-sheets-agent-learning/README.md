# Day 10 — Google Sheets API (Agent Storage Tool)

Read and append rows in Google Sheets using a **service account** — the storage layer for spreadsheet-driven agents.

Part of [ai-agents-self-learning-and-progress](https://github.com/YOUR_GITHUB_USERNAME/ai-agents-self-learning-and-progress).

## What I learned

- **User OAuth** vs **service account** (machine identity for agents)
- `gspread` hierarchy: Credentials → Client → Spreadsheet → Worksheet
- Drive scope required for `gspread.open()` (403 without Drive API)
- Generic pattern: **Agent → Auth → Tool → Read/Write → Structured result**

## Project structure

```text
day10-sheets-agent-learning/
├── tools/
│   └── sheets_tool.py   # read_google_sheet, update_google_sheet
├── credentials/         # service account JSON (local, gitignored)
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Google Cloud: Sheets API + Drive API enabled
- Service account JSON in `credentials/credentials.json`
- Share your spreadsheet with the service account email

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Place service account key at credentials/credentials.json
```

## Run

```bash
python3 main.py
```

Update spreadsheet name / sheet name in `main.py` to match yours (e.g. `Jobs Tracker`).

## Functions

| Function | Purpose |
|----------|---------|
| `read_google_sheet(name, worksheet)` | Returns rows as list of dicts |
| `update_google_sheet(name, values)` | Appends one row |

## Next

Wire Sheets + Gmail into a prompt-driven Email Agent with tool calling and an agent loop.
