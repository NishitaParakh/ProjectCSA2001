import pandas as pd

file = expenses.csv

def analyse_data():
    df = pd.read_csv(file)
    sum_total = df(["amount"]).sum()
    cat_total = df.groupby("category")["amount"].sum()

    #Total and Category-wise Spending
    print("Total Spending:", sum_total)
    print("Category-wise Spending:", cat_total)

    for cat in cat_total:
        print(cat, ":", cat_total[cat])
    
    #Highest Category
    max_cat = cat_total.idxmax()
    max_val = cat_total.max()
    print("Highest spending in Category:", max_cat)

    return sum_total, cat_total, max_cat, max_val
    



