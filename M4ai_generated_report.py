import pandas as pd
def ai_report():
    df = pd.read_csv("expenses.csv")
    df['date'] = pd.to_datetime(df['date'])

    total = df['amount'].sum()
    top_cat = df.groupby("category")['amount'].sum().idxmax()
    max_spend = df.groupby("category")['amount'].sum.max()

    days = df['date'].nunique()

    if (days > 0):
        avg_per_day = total / days
    else:
        avg_per_day = 0
    
    print("\n    AI REPORT SUMMARY    ")
    print("---------------------------")
    print("*Total Spending: ", total)
    print("*Spent Highest on ", top_cat, ": ", max_spend)
    print("*Active days: ", days)
    print("*Spending daily on an average: ", round(avg_per_day), 2)

    if avg_per_day > 500:
        print("HIGH spending pattern detected!!")
    else:
        print("Spending is under control..")
    
    print("----------------------------")
    