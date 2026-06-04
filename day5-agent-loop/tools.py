# tools.py

def calculate_expenses(expenses):

    total = sum(expenses.values())

    highest_item = max(expenses, key=expenses.get)

    return {
        "expenses": expenses,
        "total": total,
        "highest_spending": {
            "title": highest_item,
            "amount": expenses[highest_item]
        }
    }


def categorize_expenses(expenses):

    categories = {
        "food": {},
        "transport": {},
        "entertainment": {},
        "other": {}
    }

    for name, amount in expenses.items():

        lower = name.lower()

        if lower in ["food", "coffee", "restaurant"]:
            categories["food"][name] = amount

        elif lower in ["uber", "bus", "train"]:
            categories["transport"][name] = amount

        elif lower in ["movies", "games"]:
            categories["entertainment"][name] = amount

        else:
            categories["other"][name] = amount

    return categories


def save_report(report):

    with open("expense_report.txt", "w") as file:
        file.write(report)

    return {
        "status": "success",
        "file": "expense_report.txt"
    }