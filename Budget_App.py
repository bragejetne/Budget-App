import json

def get_float_input(prompt):
    #makes sure the input is an eligble float
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")



def add_expense(expenses):
    #adds an expense to the budget
    description = input("Enter kind of expense: ")
    amount = get_float_input("Enter expense amount: ")
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")


def get_sum_expenses(expenses):
    #returns the sum of all expenses
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    #returns balance
    return budget - get_sum_expenses(expenses)

def show_budget_details(budget, expenses):
    #shows details from the budget
    print(f"\nTotal budget: ${budget:.2f}\n")
    print("Expenses:\n")
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']:.2f}")
    print(f"\nSum of expenses: ${get_sum_expenses(expenses):.2f}")
    print(f"Remaining budget: ${get_balance(budget, expenses):.2f}")


def load_budget_data(filepath):
    #loads the data from the budget from json-file
    try: 
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] #Returns empty budget 

def save_budget_details(filepath, initial_budget, expenses):
    #saves the details to json-file
    data = {
        'initial_budget': initial_budget,
        'expenses' : expenses
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def reset_budget_data(filepath):
    #resets budget
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

    # Check if budget is not set, and ask the user to input the budget
    if initial_budget == 0:
        initial_budget = get_float_input("Please set your initial budget: ")
        save_budget_details(filepath, initial_budget, expenses)  # Save the budget right after setting it
    
    while True:
        print("\nWhat would you like to do with the budget?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Reset budget data")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            add_expense(expenses)  # Add an expense

        elif choice == 2:
            show_budget_details(initial_budget, expenses)  # Show budget details

        elif choice == 3:
            reset_budget_data(filepath)  # Reset the budget data

            initial_budget = 0.0
            expenses = []

        elif choice == 4:
            save_budget_details(filepath, initial_budget, expenses)  # Save the budget and expenses
            print("Exiting budget application.")
            break

        else:
            print("Invalid choice, please choose again.")



if __name__ == "__main__":
    main()
