from finance_tracker.expense import Expense

expense = Expense(
    "01-01-2026",
    100,
    "Food",
    "Lunch"
)

print(expense.to_dict())