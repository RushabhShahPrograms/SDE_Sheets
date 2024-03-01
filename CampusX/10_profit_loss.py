'''
Write a program that will take user input of cost price and selling
price and determines whether its a loss or a profit
'''

def calculate_profit_loss(cost_price, selling_price):
    if selling_price == cost_price:
        return "No profit nor loss."
    elif selling_price > cost_price:
        profit = selling_price - cost_price
        return f"Profit of ${profit:.2f}"
    else:
        loss = cost_price - selling_price
        return f"Loss of ${loss:.2f}"


cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
result = calculate_profit_loss(cost_price, selling_price)
print(result)