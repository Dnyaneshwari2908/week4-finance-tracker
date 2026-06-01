def generate_report(expenses):

    print("\nMONTHLY REPORT")

    total = 0

    for expense in expenses:

        total += expense.amount

    print(f"Total Expenses: ₹{total}")