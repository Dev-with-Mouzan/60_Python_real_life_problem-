# Problem 2: Shopping Mall Discount
# A mall gives 10% discount if the bill is above Rs 5000 and 20% discount if above Rs 10000. Take the bill amount and print discount and payable amount.
# Input 12000
# Output Discount: 2400.0, Payable: 9600.0


try :
    x = int(input("Enter the Amount to pay : "))
    if x < 0 :
        print("Amount cannot be negative")
    elif x > 5000 and x < 10000 :
        discount = x * 0.1
    else :
        discount = x * 0.2
    print("Discount : ",discount)
    print("Amount to pay : ",x-discount)

except Exception as e:
    print("The code terminated due to {e}")