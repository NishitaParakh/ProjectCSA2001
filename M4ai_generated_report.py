import pandas as pd
def ai_report():
    df = pd.read_csv("expenses.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    total = df['Amount'].sum()
    top_cat = df.groupby("Category")['Amount'].sum().idxmax()
    max_spend = df.groupby("Category")['Amount'].sum().max()

    days = df['Date'].nunique()

    if (days > 0):
        avg_per_day = total / days
    else:
        avg_per_day = 0
    
    print("\n    AI REPORT SUMMARY    ")
    print("---------------------------")
    print("\n*Total Spending: ", total)
    print("\n*Spent Highest on ", top_cat, ": ", max_spend)
    print("\n*Active days: ", days)
    print("\n*Spending daily on an average: ", round(avg_per_day, 2))

    if avg_per_day > 500:
        print("HIGH spending pattern detected!!")
    else:
        print("Spending is under control..")
    
    print("----------------------------")
    