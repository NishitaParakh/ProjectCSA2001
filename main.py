from M1data_handler import init_file, add_expense
from M2analysis_by_ai import analyse_data, ai_suggestions
from M3time_analysis import time_analyzer
from M4ai_generated_report import ai_report

init_file()

print("-----------------------------------------------")
print("---------- AI-BASED EXPENSE ANALYZER ----------")
print("-----------------------------------------------")


choose = int(input("Enter choice(1/2/3/4/5): "))

while True:
    print("\n===========EXPENSE TRACKER MENU================")
    print("1. Add Expense")
    print("2. View Analysis")
    print("3. View Time-based Analysis")
    print("4. View AI-generated Report")
    print("5. Exit")
    print("===============================================")
    if (choose == 1):
        print("\n============== ADD EXPENSES =================")
        while True:
            amount = float(input("Enter Amount spended: "))
            category = input("Enter Category(Food/Travel/Other): ")
            if (category.lower() == "other"):
                category = input("Enter Category: ")

            add_expense(amount, category)
            print("Expense added!")

            choice = input("Add another(Y/N): ")
            if (choice.lower() == "n"):
                break
    elif (choose == 2):
        print("\n=============== ANALYSIS ===================")
        sum_total, cat_total, max_cat, max_val = analyse_data()
        ai_suggestions(sum_total, cat_total, max_cat, max_val)
    elif (choose == 3):
        time_analyzer()
    elif (choose == 4):
        ai_report()
    elif (choose == 5):
        print("Thank You!.....Have a nice day!")
        print("---------Exiting program---------")
        break
    else:
        print("Invalid... Enter choice again..")


    



