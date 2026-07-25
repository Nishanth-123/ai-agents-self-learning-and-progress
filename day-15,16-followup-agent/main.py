from agent import generate_followup
import json
from tools import (
    get_followup_candidates,
    get_sent_recruiter_emails,
)
from gmail_mapper import GmailMapper
from pprint import pprint
from gmail_tools import GmailTool

gmail = GmailTool()
mapper = GmailMapper(gmail)

sent = mapper.fetch_sent_emails(20)
candidates = get_followup_candidates(sent)

for email in candidates:
    output = generate_followup(email)
    draft = json.loads(output)
    gmail.create_draft(
        to=email.recipient_email,
        subject=draft["subject"],
        body=draft["body"],
    )

    print(f"Draft created for {email.recipient_email}")
