import json

def get_float_input(input):
    while True:
        try:
            value = float(input(input))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense(expenses):
    description = input("Enter kind of expense: ")
    amount = get_float_input("Enter expense amount: ")
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")


def get_sum_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_sum_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"\nTotal budget: ${budget:.2f}\n")
    print("Expenses:\n")
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']:.2f}")
    print(f"\nSum of expenses: ${get_sum_expenses(expenses):.2f}")
    print(f"Remaining budget: ${get_balance(budget, expenses):.2f}")


def load_budget_data(filepath):
    try: 
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] #Returns empty budget 

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses' : expenses
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def reset_budget_data(filepath):
    data = {
        'initial_budget': 0.0,
        'expenses': []
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print("Budget data has been reset to zero.")



def main():
    print("Welcome to your own Budget App!")
    filepath = 'budget_data.json'

    initial_budget, expenses = load_budget_data(filepath)
    
    while True:
        print("\nWhat would you like to do with the budget?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Reset budget data")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            description = input("Enter kind of expense: ")
            amount = float(input("Enter expense amount: "))
            if amount <= get_balance(initial_budget, expenses):
                add_expense(expenses, description, amount)
            else:
                print("You don't have enough money.")

        elif choice == 2:
            show_budget_details(initial_budget, expenses)

        elif choice == 3:
            reset_budget_data(filepath)
            initial_budget = 0.0
            expenses = []
        
        elif choice == 4:
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting budget application.")
            break

        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main()
