import pandas as pd
import os
from datetime import datetime

file = os.path.join(os.path.dirname(__file__), "expenses.csv")

def init_file():
    if not os.path.exists(file):
        df = pd.DataFrame(columns = ["Amount", "category"])
        df.to_csv(file, index = False)

def add_expense(amount, category):
    df = pd.read_csv(file)
    date = datetime.now().strftime("%Y:%m:%d")
    new_data = {
        "Amount" : amount, 
        "Category" : category, 
        "Date" : date}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index = False)
    df = df.to_csv(file)
