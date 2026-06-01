import json

def save_expenses(expenses):

    data = [expense.to_dict() for expense in expenses]

    with open("data/expenses.json", "w") as file:

        json.dump(data, file, indent=4)

def load_expenses():

    try:

        with open("data/expenses.json", "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return []