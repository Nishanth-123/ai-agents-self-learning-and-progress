from datetime import datetime, timedelta, timezone

from models import EmailMessage, SentEmail


emails = [
    SentEmail(
        thread_id="thread_1",
        recipient_name="Alice",
        recipient_email="alice@acme.com",
        company_name="Acme",
        subject="Frontend Engineer Application",
        original_body="""
Hi Alice,

I came across the Frontend Engineer opening at Acme and wanted to reach out.

I have experience building high-performance React Native and full-stack applications,
and I believe my background aligns well with the role.

I've attached my resume and would love the opportunity to discuss further.

Best,
Nishanth
""",
        thread_messages=[
            EmailMessage(
                role="user",
                sender="Nishanth",
                sent_at=datetime.now() - timedelta(days=10),
                body="""
Hi Alice,

I came across the Frontend Engineer opening at Acme and wanted to reach out.

I have experience building high-performance React Native and full-stack applications,
and I believe my background aligns well with the role.

I've attached my resume and would love the opportunity to discuss further.

Best,
Nishanth
""",
            ),
        ],
        sent_at=datetime.now() - timedelta(days=10),
        replied=False,
        role_applied="Frontend Engineer",
        your_name="Nishanth",
    )
]


def get_sent_recruiter_emails():
    return emails


def get_followup_candidates(sent_emails):
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)

    return [
        email
        for email in sent_emails
        if not email.replied and email.sent_at <= cutoff
    ]
