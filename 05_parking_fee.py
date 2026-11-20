# Problem 5: Parking Fee
# A parking lot charges Rs 50 for the first hour and Rs 30 for every extra hour. Maximum charge per day is Rs 300. Take hours parked and print the fee.
# Input 5
# Output Fee: Rs 170


try :
    h = int(input("Enter the hours: "))
    if h < 0 :
        print("Input cannot be negative")
    elif h == 1:
        fee = 50
    elif h >= 2 and h <10:
        fee = 50 + (h-1) * 30
    else:
        fee = 300

    print("Total fee: ",fee)
except :
    print("error")