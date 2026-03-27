import pandas as pd
import os

file = os.path.join(os.path.dirname(__file__), "expenses.csv")

def analyse_data():
    df = pd.read_csv(file)
    sum_total = df["Amount"].sum()
    cat_total = df.groupby("Category")["Amount"].sum()

    #Total and Category-wise Spending
    print("Total Spending:", sum_total)
    print("Category-wise Spending:")

    for cat in cat_total.index:
        print(cat, ":", cat_total[cat])
    
    #Highest Category
    max_cat = cat_total.idxmax()
    max_val = cat_total.max()
    print("Highest spending in Category:", max_cat)

    return sum_total, cat_total, max_cat, max_val

def ai_suggestions(sum_total, cat_total, max_cat, max_val):

    #Overspending warning
    if (max_val > 5000):
        print("You are spending too much on", max_cat, "..")
    
    if (sum_total > 15000):
        print("You are overspending!!....Try to reduce your overall expenses")

    print("----------------------------------------------")   
    if sum_total < 2000:
        level = "LOW"
    elif 2000 <= sum_total <= 5000:
        level = "MEDIUM"
    else:
        level = "HIGH!"
    
    print("Spending level: ", level)

    #Simple Prediction
    count = len(cat_total)
    if (count > 0):
        avg = sum_total / count
        future_spend = avg * 30
        print("----------------------------------------------")
        print("Estimated Monthly Spending:", int(future_spend))
    
    #Pattern detection
    if "Food" in cat_total and "Travel" in cat_total:
        if (cat_total["Food"] > cat_total["Travel"]):
            print("You are spending more on Food than Travel")
        else:
            print("You are spending more on Travel than Food")
    



