import csv
import math
from pathlib import Path


# Keep myExpenses1.csv in the same folder as this Python file.
FILE_NAME = Path(__file__).with_name("myExpenses1.csv")

# These names and their capitalization match your CSV file exactly.
COLUMNS = ["Date", "Item", "Amount", "Category", "Time", "day"]


def load_expenses():
    try:
        # utf-8-sig also handles the invisible marker in some Excel CSV files.
        with open(FILE_NAME, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return []

            if sorted(reader.fieldnames) != sorted(COLUMNS):
                raise ValueError(
                    "CSV headings must be: Date,Item,Amount,Category,Time,day"
                )

            expenses = []
            for row_number, expense in enumerate(reader, start=2):
                if None in expense or any(value is None for value in expense.values()):
                    raise ValueError(f"Row {row_number} has missing or extra values.")

                try:
                    amount = float(expense["Amount"])
                except ValueError:
                    raise ValueError(f"Row {row_number} has an invalid Amount.")

                if not math.isfinite(amount) or amount < 0:
                    raise ValueError(f"Row {row_number} has an invalid Amount.")

                expense["Amount"] = amount
                expenses.append(expense)

        return expenses
    except FileNotFoundError:
        print("No saved expenses yet. Starting with an empty list.")
        return []
    except (OSError, ValueError, csv.Error) as error:
        print(f"Could not load the CSV file: {error}")
        print("Please check the file and try again. Your records were not changed.")
        return None


def save_expenses(expenses):
    # Write a temporary file first so a failed save does not erase old records.
    temporary_file = FILE_NAME.with_suffix(".tmp")
    try:
        with open(temporary_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(expenses)

        temporary_file.replace(FILE_NAME)
        return True
    except (OSError, ValueError, csv.Error) as error:
        print(f"Could not save the expense: {error}")
        print("Your original CSV file has not been replaced.")
        return False


def category_name(expense):
    # Keep blank categories in the totals without changing the original record.
    return expense["Category"].strip().lower() or "uncategorized"


def add_expense(expenses):
    date = input("Enter date (DD/MM/YYYY): ").strip()
    item = input("Enter item name: ").strip()
    category = input("Enter category: ").strip().lower()
    time = input("Enter time (HH:MM, for example 14:30): ").strip()
    day = input("Enter day (for example Monday): ").strip().title()

    if not date or not item or not category or not time or not day:
        print("Please fill in every field. Choose Add New Expense to try again.")
        return

    # Ask again if the amount is not a valid number.
    while True:
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a number, such as 250 or 99.50.")
            continue

        if not math.isfinite(amount) or amount < 0:
            print("Please enter a finite number that is zero or greater.")
            continue
        break

    # Use the same keys everywhere: loading, adding, saving, and displaying.
    expense = {
        "Date": date,
        "Item": item,
        "Amount": amount,
        "Category": category,
        "Time": time,
        "day": day,
    }

    # Add to memory only after the updated list has been saved successfully.
    if save_expenses(expenses + [expense]):
        expenses.append(expense)
        print("Expense saved successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nDate | Item | Amount | Category | Time | Day")
    for expense in expenses:
        print(
            f"{expense['Date']} | {expense['Item']} | "
            f"{expense['Amount']:.2f} | {category_name(expense)} | "
            f"{expense['Time']} | {expense['day']}"
        )


def show_category_totals(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    # A set comprehension removes duplicate category names.
    categories = {category_name(expense) for expense in expenses}
    print("\nUnique categories:", ", ".join(sorted(categories)))

    for category in sorted(categories):
        total = sum(
            expense["Amount"] for expense in expenses
            if category_name(expense) == category
        )
        print(f"{category}: {total:.2f}")


def main():
    expenses = load_expenses()

    # Stop if loading failed, so existing records cannot be overwritten.
    if expenses is None:
        return

    while True:
        print("\n--- Institute Expense Tracker ---")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_category_totals(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed.")
