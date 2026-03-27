import pandas as pd
import os

file = os.path.join(os.path.dirname(__file__), "expenses.csv")

def init_file():
    if not os.path.exists(file):
        df = pd.DataFrame(columns = ["Amount", "category"])
        df.to_csv(file, index = False)

def add_expense(amount, category):
    df = df.read_csv(file)
    new_data = {"Amount" : amount, "Category" : category}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index = False)
    df = df.to_csv(file)
