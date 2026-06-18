from gmail_auth import get_gmail_service
import base64
from typing import Optional

def read_inbox(
    max_results: int = 10,
    query: Optional[str] = None,
):
    """
    Read emails from Gmail.

    Returns:
        List[dict] with keys:
        - id
        - from
        - subject
        - body
        - received_at
    """
    service = get_gmail_service()
    
    # 1. Build the search query dynamically based on arguments
    query_parts = []
    if query:
        query_parts.append(query)
        
    q_string = " ".join(query_parts) if query_parts else None

    # 2. Fetch the list of message summaries
    results = service.users().messages().list(
        userId="me",
        q=q_string,
        maxResults=max_results
    ).execute()
    
    messages_summary = results.get("messages", [])
    emails_list = []

    # 3. Retrieve and parse details for each message
    for msg in messages_summary:
        message = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full" # Ensures we get headers and body payload
        ).execute()
        
        headers = message.get("payload", {}).get("headers", [])
        
        # Extract metadata from headers
        email_from = next((h["value"] for h in headers if h["name"].lower() == "from"), "Unknown")
        subject = next((h["value"] for h in headers if h["name"].lower() == "subject"), "(No Subject)")
        received_at = next((h["value"] for h in headers if h["name"].lower() == "date"), "Unknown")
        
        # Extract body text
        body = ""
        payload = message.get("payload", {})
        parts = payload.get("parts", [])
        
        # Simple body extraction for plain text or multipart emails
        if "body" in payload and payload["body"].get("data"):
            body_data = payload["body"]["data"]
            body = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
        elif parts:
            for part in parts:
                if part.get("mimeType") == "text/plain" and part.get("body", {}).get("data"):
                    body_data = part["body"]["data"]
                    body = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
                    break

        emails_list.append({
            "id": message["id"],
            "from": email_from,
            "subject": subject,
            "body": body.strip(),
            "received_at": received_at
        })

    return emails_list