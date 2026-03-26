def ai_suggestions(sum_total, cat_total, max_cat, max_val):

    #Overspending warning
    if (max_val > 2000):
        print("You are spending too much on ", max_cat, "!!")
    
    if (sum_total > 5000):
        print("You are overspending!!")
        print("Try to reduce your overall expenses")
    
    #Classification(Low/Medium/High)
    if (sum_total < 2000):
        level = "Low"
        print("You are going great...")
    elif (sum_total in (2000, 5000)):
        level = "Medium"
        print("Good enough")
    else:
        level = "High"
        print("You are spending TOO MUCH")
    
    print("Spending Level:", level)

    #Simple Prediction
    count = len(cat_total)
    if (count > 0):
        avg = sum_total / count
        future_spend = avg * 30
        print("Estimated Monthly Spending:", int(future_spend))
    
    #Pattern detection
    if "Food" in cat_total and "Travel" in cat_total:
        if (cat_total["Food"] > cat_total["Travel"]):
            print("You are spending more on Food than Travel")
        else:
            print("You are spending more on Travel than Food")
    
    



