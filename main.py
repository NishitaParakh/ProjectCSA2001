from M1data_handler import init_file, add_expense
from M2analysis import analyse_data
from M3ai_features import ai_suggestions
from M4graph import show_graph

init_file()

amount = float(input("Enter Amount spended:"))
category = input("Enter Category(Food/Travel/Other):")
if (category == "Other"):
    category = input("Enter Category: ")

add_expense(amount, category)
print("Expense added!")

sum_total, cat_total, max_cat, max_val = analyse_data()
ai_suggestions(sum_total, cat_total, max_cat, max_val)
show_graph(cat_total)

