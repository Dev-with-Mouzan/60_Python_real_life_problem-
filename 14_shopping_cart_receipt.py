# Problem 14: Shopping Cart Receipt
# Take items as (name, price, quantity) until the user types done. Print a receipt with each line total and a grand total.
# Input Rice 350 2, Oil 500 1, done
# Output Rice 2 x 350 = 700, Oil 1 x 500 = 500, Total: 1200

try:
    while True:
        name = input("Enter your name of the item : ")
        price = int ( input ("Enter the price of the item : "))
        quantity = int ( input ("Enter the quantity of the item : "))
        if price < 0 or quantity < 0:
            print("Price and quantity must be non-negative.")
        else:
            total = price * quantity
            print(f"Total cost for {name}: {quantity}  X {price} is: ${total}")
        
except :
    print("Invalid input. Please enter valid values for name, price, and quantity.")