import base64

from email.mime.text import MIMEText
from gmail_auth import get_gmail_service


class GmailTool:
    def __init__(self):
        self.service = get_gmail_service()

    # ----------------------------
    # Message APIs
    # ----------------------------

    def list_sent_messages(self, max_results=10):
        response = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                labelIds=["SENT"],
                maxResults=max_results,
            )
            .execute()
        )

        return response.get("messages", [])

    def get_message(self, message_id):
        return (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=message_id,
                format="full",
            )
            .execute()
        )

    # ----------------------------
    # Thread APIs
    # ----------------------------

    def get_thread(self, thread_id):
        return (
            self.service.users()
            .threads()
            .get(
                userId="me",
                id=thread_id,
                format="full",
            )
            .execute()
        )

    def fetch_sent_threads(self, max_results=10):
        messages = self.list_sent_messages(max_results)

        threads = []
        seen = set()

        for message in messages:
            thread_id = message["threadId"]

            if thread_id in seen:
                continue

            seen.add(thread_id)

            threads.append(self.get_thread(thread_id))

        return threads

    def create_draft(self, to, subject, body):

        message = MIMEText(body)

        message["to"] = to
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        draft = {
            "message": {
                "raw": raw_message
            }
        }

        return (
            self.service.users()
            .drafts()
            .create(
                userId="me",
                body=draft,
            )
            .execute()
        )    

    # ----------------------------
    # Helpers
    # ----------------------------

    @staticmethod
    def get_header(headers, name):
        for header in headers:
            if header["name"].lower() == name.lower():
                return header["value"]

        return None

    @staticmethod
    def decode_body(payload):
        if "parts" in payload:

            for part in payload["parts"]:

                if part["mimeType"] == "text/plain":

                    data = part["body"].get("data")

                    if data:
                        return base64.urlsafe_b64decode(data).decode("utf-8")

        else:
            data = payload.get("body", {}).get("data")

            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8")

        return ""