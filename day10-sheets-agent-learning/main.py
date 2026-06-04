from tools.sheets_tool import read_google_sheet
from tools.sheets_tool import update_google_sheet

records = read_google_sheet(
    "Jobs Tracker",
    "Sheet1"
)

print(records)

result = update_google_sheet(
    "Jobs Tracker",
    ["Microsoft", "SDE-2", "Applied"]
)

print(result)