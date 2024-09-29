import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount" : amount})
    print(f"Added expense: {description}, Amount: {amount}")

def get_sum_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_sum_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"\nTotal budget: {budget}\n")
    print("Expenses:\n")
    for expense in expenses:
        print(f"{expense['description']}: {expense['amount']}")
    print(f"\nSum expenses: {get_sum_expenses(expenses)}")
    print(f"\nRemaining budget: {get_balance(budget, expenses)}")

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


def main():
    print("Welcomne to your own Budget App!")
    filepath = 'budget_data.json' #Defines my way to the JSON file
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("Enter initial budget amount"))
    budget = initial_budget

    while True:
        print("\nWhat would you like to do with the budget?\n1. Add an expense\n2. Show budget details\n3. Exit")
        choice = int(input("Enter your choice (1/2/3): "))

    
        if choice == 1:
            description = input("Enter kind of expense:")
            amount = float(input("Enter expense amount:"))
            if(amount <= get_balance(budget, expenses)):
                add_expense(expenses, description, amount)
            else:
                print("You dont have enough money")
        
        elif choice == 2:
            show_budget_details(budget, expenses)
        
        elif choice == 3:
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting budget application.")
            break

        else:
            print("Invalid choice, choose again")

if __name__ == "__main__":
    main()
