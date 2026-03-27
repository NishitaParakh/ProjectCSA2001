import pandas as pd

def time_analyzer():
    df = pd.read_csv("expenses.csv")
    df['date'] = pd.to_datetime(df['date'])

    print("\n---------DAILY SPENDING----------")
    daily_spend = df.groupby(df['date'].dt.date)['amount'].sum()
    print(daily_spend)

    print("\n---------WEEK-DAY SPENDING----------")
    weekday_spend = df.groupby(df['date'].dt.day_name)['amount'].sum()
    print(weekday_spend)

    print("\n---------MONTHLY SPENDING----------")
    monthly_spend = df.groupby(df['date'].dt.month)['amount'].sum()
    print(monthly_spend)

    
    