from sheets_client import get_pending_contacts
from gmail_client import generate_email
from gmail_sender import send_email
from tools.sheets_tool import update_cell

def main():
    records = get_pending_contacts()
    print(records)

    for index, record in enumerate(records, start=2):
        email = generate_email(record)
        print(type(record))
        print(record)

        print(type(email))
        print(email)
        send_email(record["Email"], email["subject"], email["body"])
        print(index)
        update_cell("Jobs Tracker", "Sheet2", index, 4, "Sent")
        print(f"Email sent to {record['Name']} at {record['Company']} for the role of {record['Role']}")

if __name__ == "__main__":
    main()