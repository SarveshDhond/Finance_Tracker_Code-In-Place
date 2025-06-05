import time

def expense_report(total_expense, grocery, fixed, food, other):

    print("WELCOME TO YOUR EXPENSE REPORT")
    print("")
    print("loading..")
    time.sleep(2)


    total_grocery = sum(grocery)
    total_fixed = sum(fixed)
    total_food = sum(food)
    total_other = sum(other)
    total_expense = sum(total_expense)



    print("Please select following options for reports")
    print(" 1 -> Category based expense report")
    print(" 2 -> Trends / Maximum spend / Minimum spend")
    print(" 3 -> Individual expenses based on categories")
    print(" 4 -> All in one report")
    print(" 4 -> Exit")

    option = int(input("Which select option 1 - 5 -> "))
    while option not in (1, 2, 3, 4, 5):
        option = input("Please select a valid option")
    
    while option != 5:
        if option == 1:
            print("Printing category based report...")
            print("")
            time.sleep(2)
            print("-----------CATEGORIES------------------------------------------| AMOUNT")
            print("-------------------------------------------------------------------------------------|")
            print(f"| Total spent on groceries------------------------------------| {total_grocery}")
            print(f"| Total spent on fixed expenses-------------------------------| {total_fixed}")
            print(f"| Total spent on food-----------------------------------------| {total_food}")
            print(f"| Miscellaneous expenses--------------------------------------| {total_other}")
            print("-------------------------------------------------------------------------------------|")
            print(f"|---------TOTAL-----------------------------------------------| {(total_expense)}")

            print("")
            option = input("Do you want to check any other report or press enter 5 to exit -> ")
            option = int(option)
            for i in range(50):
                print("")
        
    
        if option == 2:
            print("Printing trend report")
            print("")
            time.sleep(2)
            print("-----------CATEGORIES--------------------------------------------| AMOUNT")
            print("-------------------------------------------------------------------------------------|")
            print(f"| Maximum amount spent on groceries one-time--------------------| {max(grocery)}")
            print(f"| Maximum amount spent on fixed expenses one-time---------------| {max(fixed)}")
            print(f"| Maximum amount spend on food one-time-------------------------| {max(food)}")
            print(f"| Maximum amount spent on miscellaneous expenses one-time-------| {max(other)}")

            print("")
            option = input("Do you want to check any other report or press enter 5 to exit -> ")
            option = int(option)
            for i in range(50):
                print("")

        if option == 3:

            print("YOUR EXPENSES FOR GROCERIES ARE")
            print(*grocery)
            print("")
            print("YOUR EXPENSES FOR FIXED EXPENSES ARE")
            print(*fixed)
            print("")
            print("YOUR EXPENSES FOR FOOD ARE")
            print(*food)
            print("")
            print("YOUR OTHER / MISCELLANEOUS EXPENSES ARE")
            print(*other)

            option = input("Do you want to check any other report or press enter 5 to exit -> ")
            option = int(option)
            for i in range(50):
                print("")
    

        if option == 4:
            print("Loading....")
            time.sleep(4)
            print("-----------CATEGORIES--------------------------------------------| AMOUNT")
            print("-------------------------------------------------------------------------------------|")
            print(f"| Total spent on groceries--------------------------------------| {sum(grocery)}")
            print(f"| Total spent on fixed expenses---------------------------------| {sum(fixed)}")
            print(f"| Total spent on food-------------------------------------------| {sum(food)}")
            print(f"| Miscellaneous expenses----------------------------------------| {sum(other)}")
            print("-------------------------------------------------------------------------------------|")
            print(f"|---------TOTAL-------------------------------------------------| {(total_expense)}")

            print("")

            print("-----------CATEGORIES--------------------------------------------| AMOUNT -----------|")
            print("-------------------------------------------------------------------------------------|")
            print(f"| Maximum amount spent on groceries one-time--------------------| {max(grocery)} ---|")
            print(f"| Maximum amount spent on fixed expenses one-time---------------| {max(fixed)} -----|")
            print(f"| Maximum amount spend on food one-time-------------------------| {max(food)} ------|")
            print(f"| Maximum amount spent on miscellaneous expenses one-time-------| {max(other)} -----|")

            print("")

            print("-----------CATEGORIES--------------------------------------------| AMOUNT")
            print("-----------------------------------------------------------------------------------|")
            print(f"| All grocery expenses are as follows---------------------------| {(grocery)}")
            print(f"| All fixed expenses are as follows-----------------------------| {fixed}")
            print(f"| All food related expenses are as follows----------------------| {food}")
            print(f"| All other expenses are as follows-----------------------------| {other}")

            print("")
            option = input("Do you want to check any other report or press enter 5 to exit -> ")
            option = int(option)

        break

    for i in range(50):
        print("")


if __name__=='__main__':
    expense_report()

