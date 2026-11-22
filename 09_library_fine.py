# Problem 9: Library Fine
# A library allows keeping a book for 14 days. After that the fine is Rs 5 per day. Take days kept and print the fine.
# Input 20
# Output Fine: Rs 30


try :
    take_day=int(input("Enter the number of days you have taken the book: "))
    if take_day < 0 :
        print("Input cannot be negative")
    elif take_day <= 14:
        print("No fine the library allow to keep the book for 14 days")
    else:
        fine = 5*(take_day-14)
        print("Total fine: ",fine)
except :   
    print("error")