# Problem 18: Hotel Booking
# A hotel has Standard (Rs 5000), Deluxe (Rs 8000) and Suite (Rs 12000) per night. Stays longer than 5 nights get 10% off. Take room type and nights, print total.
# Input Deluxe 7
# Output Total: Rs 50400.0

try:
    t=input("which type of room you want to book? (single/double/suite): ").lower()
    n=int(input("Enter the number of nights you want to stay: "))
    if n <= 0:
        print("Number of nights must be greater than zero.")
    elif t == "single":
        price = 5000 * n
        if n > 5:
            discount = price * 0.1
            print(f"Total cost for {n} nights in a single room is: ${price - discount:.2f} (including a discount of ${discount:.2f})")
        else:
            print(f"Total cost for {n} nights in a single room is: ${price:.2f}")
    elif t == "double":
        price = 8000 * n
        if n > 5:
            discount = price * 0.1
            print(f"Total cost for {n} nights in a single room is: ${price - discount:.2f} (including a discount of ${discount:.2f})")
        else:
            print(f"Total cost for {n} nights in a single room is: ${price:.2f}")
    elif t == "suite":
        price = 12000 * n
        if n > 5:
            discount = price * 0.1
            print(f"Total cost for {n} nights in a single room is: ${price - discount:.2f} (including a discount of ${discount:.2f})")
        else:
            print(f"Total cost for {n} nights in a single room is: ${price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid room type and number of nights.")