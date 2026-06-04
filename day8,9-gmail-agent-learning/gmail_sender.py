from gmail_auth import get_gmail_service

from email.mime.text import MIMEText
import base64

def send_email(to, subject, body):

    service = get_gmail_service()

    message = MIMEText(body)

    message["to"] = to
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={
            "raw": raw_message
        }
    ).execute()

    print("Email sent successfully!")

