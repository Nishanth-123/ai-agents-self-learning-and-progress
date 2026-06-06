from tools.sheets_tool import read_google_sheet

def read_sheet():
    records = read_google_sheet(
        "Jobs Tracker",
        "Sheet2"
    )
    return records

def get_pending_contacts():
    records = read_sheet()

    return [
        record
        for record in records
        if record["Status"].strip().lower() == "pending"
    ]