'''THIS FUNCTION ASK FOR INCOME. IT WILL ASK AGAIN IF NO INTEGER IS ENTERED AND RETURNS TOTAL INCOME'''
import time

def add_income():
    print(" WELCOME TO INCOME SECTION ")
    proceed = input("Please press enter to proceed -> ")
    if proceed == "":
        print("loading.....")

    how_many = input("How many income sources do you have? -> ")
    while how_many.isdigit() == False:
        how_many = input("Please enter a valid number of how many income sources do you have? -> ")
    how_many = int(how_many)
    print("")

    total_income = 0

    for i in range(how_many):
        income = input("Please enter amount in $ (do not enter special charecters)-> ")
        while income.isdigit() == False:
            income= input("Please enter a valid amount in $ (do not enter special charecters)-> ")
        income = float(income)
        total_income += income
    print("")
    time.sleep(2)
    
    print(f"Your total income of ${total_income} is recorded")
    return total_income


if __name__=='__main__':
    add_income()