from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class EmailMessage:
    role: str  # "user" or "recruiter"
    sender: str
    sent_at: datetime
    body: str


@dataclass
class SentEmail:
    thread_id: str

    recipient_name: str
    recipient_email: str
    company_name: str

    subject: str

    # Initial outreach email
    original_body: str

    # Entire conversation in chronological order
    thread_messages: list[EmailMessage]

    # Metadata
    sent_at: datetime
    replied: bool

    # Optional context
    role_applied: Optional[str] = None
    your_name: str = "Nishanth"
