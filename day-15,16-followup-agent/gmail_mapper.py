from datetime import datetime
from email.utils import parseaddr

from models import EmailMessage, SentEmail


class GmailMapper:
    def __init__(self, gmail_tool):
        self.gmail = gmail_tool

    def thread_to_sent_email(self, thread):

        messages = thread["messages"]

        thread_messages = []

        first_message = messages[0]

        first_headers = first_message["payload"]["headers"]

        subject = self.gmail.get_header(first_headers, "Subject")

        recipient = self.gmail.get_header(first_headers, "To")

        recipient_name, recipient_email = parseaddr(recipient)

        original_sent_at = None
        original_body = ""

        replied = False

        for index, message in enumerate(messages):

            payload = message["payload"]
            headers = payload["headers"]

            sender = self.gmail.get_header(headers, "From")
            sender_name, sender_email = parseaddr(sender)

            date = self.gmail.get_header(headers, "Date")

            try:
                sent_at = datetime.strptime(
                    date,
                    "%a, %d %b %Y %H:%M:%S %z",
                )
            except ValueError:
                # Gmail sometimes uses a different date format
                sent_at = datetime.now()

            body = self.gmail.decode_body(payload)

            role = (
                "user"
                if sender_email.lower() != recipient_email.lower()
                else "recruiter"
            )

            if role == "recruiter":
                replied = True

            thread_messages.append(
                EmailMessage(
                    role=role,
                    sender=sender_name or sender_email,
                    sent_at=sent_at,
                    body=body,
                )
            )

            if index == 0:
                original_sent_at = sent_at
                original_body = body

        return SentEmail(
            thread_id=thread["id"],
            recipient_name=recipient_name or recipient_email,
            recipient_email=recipient_email,
            company_name="Unknown",
            subject=subject,
            original_body=original_body,
            thread_messages=thread_messages,
            sent_at=original_sent_at,
            replied=replied,
            role_applied=None,
            your_name="Nishanth",
        )

    def fetch_sent_emails(self, max_results=10):

        threads = self.gmail.fetch_sent_threads(max_results)

        sent_emails = []

        for thread in threads:
            sent_emails.append(
                self.thread_to_sent_email(thread)
            )

        return sent_emails