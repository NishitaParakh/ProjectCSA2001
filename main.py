from M1data_handler import init_file, add_expense
from M2analysis import analyse_data
from M3ai_features import ai_suggestions

init_file()

print("-----------------------------------------------")
print("---------- AI-BASED EXPENSE ANALYZER ----------")
print("-----------------------------------------------")

print("\n===========EXPENSE TRACKER MENU==============")
print("1. Add Expense")
print("2. View Analysis")
print("3. Exit")

choose = int(input("Enter choice(1/2/3): "))

while True:
    if (choose == 1):
        print("\n============== ADD EXPENSES =================")
        while True:
            amount = float(input("Enter Amount spended: "))
            category = input("Enter Category(Food/Travel/Other): ")
            if (category == "Other"):
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
        print("Thank You!.....Have a nice day!")
        print("---------Exiting program---------")
        break
    else:
        print("Invalid choice... Enter again")
    c1 = input("Do you want to run again?(Y/N): ")
    if (c1.lower() == "n"):
        break
if (choose == 1 or choose == 2):
    print("========== AI REPORT===========")
    



