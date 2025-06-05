''' THIS FUNCTION HELPS TO ADD EXPENSE. IT CATEGORIZES EXPENSE BASED ON THE THE PURPOSE'''
import time

def add_expenses():
    print("WELCOME TO THE EXPENSE SECTION")
    proceed = input("Press enter to proceed -> ")
    if proceed == "":
        print("loading...")
    grocery = []
    fixed = []
    food = []
    other = []


    print("For every expense category we have a key selected.")
    print("G -> Groceries")
    print("S -> For fixed expenses like phoe bills / rent / insurance and bills which you cannot change")  
    print("F -> for food. This could be in a restaurant or order from apps")
    print("and O -> For all other expenses such as subscriptions, clothes, etc.")
    print("")

    expense_type = input(f"What type of expense do you want to add (G / S / F / O) -> ")
    expense_type = expense_type.lower()
    while expense_type != "":
        while expense_type not in ("g", "f", "o", "s"):
            expense_type = input(f"Please enter a valid expense type from (G / S / F / O) -> ")
        expense_type = expense_type.lower()


        if expense_type == "g":
            expense = float(input("Please enter expense in digit without special charecter -> "))
            grocery.append(expense)
            expense_type = input(f"What type of expense do you want to add (G / S / F / O) -> ")


        if expense_type == "s":
            expense = float(input("Please enter expense in digit without special charecter -> "))
            fixed.append(expense)
            expense_type = input(f"What type of expense do you want to add (G / S / F / O) -> ")

        
        if expense_type == "f":
            expense = float(input("Please enter expense in digit without special charecter -> "))
            food.append(expense)
            expense_type = input(f"What type of expense do you want to add (G / S / F / O) -> ")


        if expense_type == "o":
            expense = float(input("Please enter expense in digit without special charecter -> "))
            other.append(expense)
            expense_type = input(f"What type of expense do you want to add (G / S / F / O) -> ")


    print("")
    time.sleep(2)
    print("Your expenses have been recorded")
    print("")

    total_expense = grocery + fixed + food + other
    total = sum(total_expense)
            
    print(f" Your total expenses are ${total}")
    for i in range(50):
        print("")

    return total_expense, grocery, fixed, food, other
    
if __name__=='__main__':
    add_expenses()





