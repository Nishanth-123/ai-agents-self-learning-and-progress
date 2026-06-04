import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials/credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)


def update_google_sheet(
    spreadsheet_name,
    values,
    worksheet_name="Sheet1"
):
    spreadsheet = client.open(
        spreadsheet_name
    )

    worksheet = spreadsheet.worksheet(
        worksheet_name
    )

    worksheet.append_row(values)

    return "Row added successfully"
    
def read_google_sheet(
    spreadsheet_name,
    worksheet_name="Sheet1"
):
    spreadsheet = client.open(
        spreadsheet_name
    )

    worksheet = spreadsheet.worksheet(
        worksheet_name
    )

    return worksheet.get_all_records()