import time


def main():
    name = input("What is your name ? -> ")

    print(f"Welcome {name}. This finance tracker can do the following")
    print("1-> Add income")
    print("2-> Add expense")
    print("3-> Generate expense report")
    print("4-> investment suggestions")
    print("5 -> exit")

    command = int(input("Please select one from the options -> 1-4 or option -> 5 to exit-> "))

    while command != 5:
        
        if command == 1:
            print("loading..")
            for i in range(10):
                print("")
            from add_income import add_income
            total_income = add_income()
            print(f"Welcome {name}. This finance tracker can do the following")
            print("1-> Add income")
            print("2-> Add expense")
            print("3-> Generate expense report")
            print("4-> investment suggestions")
            print("5 -> exit")
            command = int(input("Please select one from the options -> 1-4 or option -> 5 to exit-> "))
            




        elif command == 2:
            print("loading..")
            for i in range(50):
                print("")
            from add_expense import add_expenses
            total_expense, grocery, fixed, food, other = add_expenses()
            print(f"Welcome {name}. This finance tracker can do the following")
            print("1-> Add income")
            print("2-> Add expense")
            print("3-> Generate expense report")
            print("4-> investment suggestions")
            print("5 -> exit")
            command = int(input("Please select one from the options -> 1-4 or option -> 5 to exit-> "))

            
        elif command == 3:
            print("loading..")
            for i in range(50):
                print("")
            from expense_report import expense_report
            report = expense_report(total_expense, grocery, fixed, food, other)
            print(f"Welcome {name}. This finance tracker can do the following")
            print("1-> Add income")
            print("2-> Add expense")
            print("3-> Generate expense report")
            print("4-> investment suggestions")
            print("5 -> exit")
            command = int(input("Please select one from the options -> 1-4 or option -> 5 to exit-> "))



        elif command == 4:
            print("loading..")
            for i in range(50):
                print("")
            from investment_suggestion import investment_section
            investment = investment_section(total_expense, total_income)
            print(f"Welcome {name}. This finance tracker can do the following")
            print("1-> Add income")
            print("2-> Add expense")
            print("3-> Generate expense report")
            print("4-> investment suggestions")
            print("5 -> exit")
            command = int(input("Please select one from the options -> 1-4 or option -> 5 to exit-> "))



    print("Exiting..")
    time.sleep(2)
    print("")        
    print(f"THANK YOU FOR USING OUR SERVICES {name}")



if __name__ == "__main__":
    main()

