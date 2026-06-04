from gmail_auth import get_gmail_service

def read_inbox():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        # maxResults=5,
        q="is:unread from:linkedin.com"
    ).execute()

    messages = results.get("messages", [])

    for msg in messages:

        message = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = message["payload"]["headers"]

        subject = ""
        sender = ""

        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]

            if header["name"] == "From":
                sender = header["value"]

        snippet = message["snippet"]

        print("\n-------------------")
        print("From:", sender)
        print("Subject:", subject)
        print("Snippet:", snippet)