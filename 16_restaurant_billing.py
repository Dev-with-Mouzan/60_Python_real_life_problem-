# Problem 16: Restaurant Billing
# A restaurant has a menu dictionary with prices. Keep taking orders (item, qty) until done. Add 10% service tax and print the final bill. Show an error if the item is not on the menu.
# Input Burger 2, Fries 1, done
# Output Subtotal, Tax and Total printed

manu ={
    "pizza_midum" : 500,
    "pizzea_large" : 800,
    "pizza_small" : 300,
    "pizza_xlarge" : 1000,
    "burger" : 200,
    "fries" : 100,
    "drinks" : 100,
    "chicken" : 400,
    "nugets" : 300,
}

try :
    item = input("Enter the item you want to order: ")
    quantity = int(input("Enter the quantity of the item: "))
    if item not in manu:
        print("Item not found in the menu.")
    if quantity < 0:
        print("Quantity cannot be negative")
    elif item in manu:
        price = manu[item]
        total = price * quantity
        service_charge = total * 0.1
        total_with_service_charge = total + service_charge
        print(f"Total cost for {item}: {quantity} X {price} is: ${total_with_service_charge:.2f} (including service charge of ${service_charge:.2f})")
except ValueError:
    print("Invalid input. Please enter a valid quantity.")