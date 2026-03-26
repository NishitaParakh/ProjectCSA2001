import matplotlib.pyplot as plt
def show_graph(cat_total):
    cat_total.plot(kind = "bar")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()
