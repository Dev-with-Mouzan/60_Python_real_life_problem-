# Problem 1: Electricity Bill
# A power company charges Rs 10/unit for the first 100 units, Rs 15/unit for the next 100 units, and Rs 20/unit above 200 units. A 5% tax is added on the total. Take units consumed and print the final bill.
# Input 250
# Output Final Bill: Rs 3675.0



try:
    x=int(input("Enter the No of Unit: "))
    bill=0
    if x < 0 :
        print("Units cannot be negative")
    elif x <= 100 :
        bill = x * 10
    elif x > 100 and x < 200 :
        bill = 1000 + ((x-100) * 15)
    else :
        bill = 2500 + ((x-200) * 20)
      
    tax =bill * 0.05
    print("Total bill: ",bill+tax)
except Exception as e:
    print(f"the error in the code is {e}")

