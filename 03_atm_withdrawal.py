# Problem 3: ATM Withdrawal
# An ATM has balance Rs 10000. It only gives amounts in multiples of 500 and the amount cannot exceed balance. Take withdraw amount and print the result.
# Input 2500
# Output New balance: 7500
# Input 2300
# Output Invalid amount

try:
    amount = int(input("Enter the amount to withdraw: "))
    if amount <=0 and amount > 10000:
        print("Invalid amount")
    else:
        if amount % 500 == 0:
            print("New blance:",10000-amount)
        else:
            print("Invalid Amount")
except Exception as e:
    print(e)