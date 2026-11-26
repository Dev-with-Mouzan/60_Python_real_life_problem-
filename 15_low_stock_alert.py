# Problem 15: Low Stock Alert
# A shop keeps stock in a dictionary {item: quantity}. Print all items with quantity below 5 so the owner can reorder them.
# Input {'Soap': 3, 'Milk': 20, 'Tea': 1}
# Output Reorder: Soap, Tea

stock = {"milk": 50, "oil": 3, "apple": 2, "tea": 4, "sugar": 10, "salt": 1}

for i in stock:
    if stock[i] < 5:
        print(f"Stock for {i} is low: {stock[i]} units left.")
