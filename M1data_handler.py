import pandas as pd
import os
from datetime import datetime

file = os.path.join(os.path.dirname(__file__), "expenses.csv")

def init_file():
    if not os.path.exists(file):
        df = pd.DataFrame(columns = ["Amount", "Category", "Date"])
        df.to_csv(file, index = False)

def add_expense(amount, category):
    df = pd.read_csv(file)
    date = datetime.now().strftime("%Y-%m-%d")
    new_data = {
        "Amount" : amount, 
        "Category" : category, 
        "Date" : date}
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index = True)
    df.to_csv(file, index = "False")
