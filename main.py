import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()



def add_expense():
    title = input("Enter Expense Title: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "title": title,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\n✅ Expense Added Successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n===== All Expenses =====")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['title']} - ₹{expense['amount']}")

    print()
def delete_expense():
    if not expenses:
        print("\n❌ No expenses to delete.\n")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            save_expenses(expenses)

            print(f"\n✅ '{deleted['title']}' deleted successfully!\n")
        else:
            print("\n❌ Invalid expense number.\n")

    except ValueError:
        print("\n❌ Please enter a valid number.\n")

add_expense()
view_expenses()