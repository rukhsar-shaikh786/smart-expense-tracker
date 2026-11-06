# SMART EXPENSE TRACKER

expenses = []

def load_expenses():
    """Load saved expenses from the text file."""
    try:
        file = open("expenses.txt", "r")
        for line in file:
            details = line.strip().split("|")
            if len(details) == 3:
                category = details[0]
                description = details[1]
                amount = float(details[2])

                expense = {
                    "category": category,
                    "description": description,
                    "amount": amount
                }
                expenses.append(expense)
        file.close()
    except FileNotFoundError:
        # The file will be created when the first expense is added.
        pass


def add_expense():
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount in rupees: "))

    expense = {
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    file = open("expenses.txt", "a")
    file.write(category + "|" + description + "|" + str(amount) + "\n")
    file.close()

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\n------ YOUR EXPENSES ------")
        for expense in expenses:
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount: Rs.", expense["amount"])
            print("---------------------------")


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Your total expenses are: Rs.", total)


# Load previously saved expenses when the program starts.
load_expenses()

while True:
    print("\n================================")
    print("       SMART EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you for using Smart Expense Tracker!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
