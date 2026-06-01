from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses
from finance_tracker.reports import generate_report
from finance_tracker.utils import validate_amount

class FinanceTracker:

    def __init__(self):

        self.manager = ExpenseManager()

    def add_expense(self):

        print("\nADD EXPENSE")

        date = input("Date: ")

        while True:

            amount = input("Amount: ")

            if validate_amount(amount):
                amount = float(amount)
                break

            print("Invalid amount.")

        category = input("Category: ")
        description = input("Description: ")

        expense = Expense(
            date,
            amount,
            category,
            description
        )

        self.manager.add_expense(expense)

        save_expenses(self.manager.expenses)

        print("Expense Added Successfully!")

    def menu(self):

        while True:

            print("\n" + "=" * 50)
            print("PERSONAL FINANCE TRACKER")
            print("=" * 50)

            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Generate Report")
            print("0. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.manager.view_expenses()

            elif choice == "3":
                generate_report(
                    self.manager.expenses
                )

            elif choice == "0":

                print("Thank you for using Finance Tracker!")

                break

            else:

                print("Invalid Choice")