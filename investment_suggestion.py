import time

def investment_section(total_expense, total_income):
    print("WELCOME TO YOUR INVESTMENT SECTION")

    total_expense = sum(total_expense)

    basic_expense = round((total_income * 70 / 100), 1)
    basic_pleasure = round((total_income * 20 / 100), 1)
    basic_savings =  round((total_income * 10 / 100), 1)

    if total_expense > total_income:
        ratio = round((total_income / total_expense * 100), 1)
    else:
        ratio = round((total_expense / total_income * 100), 1)

    print("Loading...")
    for i in range(50):
        print("")
    print("Welcome to basic investment management service")
    print("")
    print("For basic investment we always suggest")
    print("------------------------EXPENSES------------------------------------| AMOUNT ")
    print(f"Fixed / groceries / utilities -> 70% of your income ---------------| {basic_expense}")
    print(f"Pleasure expenses / clothes / food -> 20% of your income ----------| {basic_pleasure}")
    print(f"TFSA / RRSP contributions -> 10% of your income -------------------| {basic_savings}")
    print("")

    if total_expense > total_income:
        print("As per your income and expense, you have ")
        print(f"Negative ratio of {ratio}%")
        print("This could lead to problems down the line, please reduce your expenses")

    if total_income > total_expense:
        print(f"You have a positive income to expense ratio of {ratio}%")
        print("We suggest you use the above 70-20-10 split to split your income accordingly")

    ask = input("Please press enter to proceed -> ")
    if ask == "":
        ask = input("Press enter")


if __name__=='__main__':
    investment_section()