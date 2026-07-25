from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
import pickle
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.compose",
]

def get_gmail_service():

    creds = None

    # Load existing token if available
    if os.path.exists("token.pickle"):

        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If no token exists, login with Google
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            try:
                creds.refresh(Request())

            except RefreshError:
                creds = None

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/gmail_credentials.json",
                SCOPES,
            )

            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    # Build Gmail service
    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service