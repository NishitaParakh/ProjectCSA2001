import pandas as pd

def time_analyzer():
    df = pd.read_csv("expenses.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    print("\n---------DAILY SPENDING----------")
    daily_spend = df.groupby(df['Date'].dt.date)['Amount'].sum()
    print(daily_spend)

    print("\n---------WEEK-DAY SPENDING----------")
    weekday_spend = df.groupby(df['Date'].dt.day_name())['Amount'].sum()
    print(weekday_spend)

    print("\n---------MONTHLY SPENDING----------")
    monthly_spend = df.groupby(df['Date'].dt.month)['Amount'].sum()
    print(monthly_spend)

    
    