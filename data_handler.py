import pandas as pd
import os

file = expenses.csv

def init_file():
    if not os.path.exists(file):
        df = pd.DataFrame(columns = ["Amount", "category"])
        df.to_csv(file, index = False)

def add_expense(amount, category):
    df = pd.read_csv(file)
    new_data = {"Amount" : amount, "Category" : category}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index = False)
    df = pd.to_csv(file)
