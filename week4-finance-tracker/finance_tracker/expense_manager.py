from finance_tracker.expense import Expense

class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:

            print(
                expense.date,
                expense.amount,
                expense.category,
                expense.description
            )