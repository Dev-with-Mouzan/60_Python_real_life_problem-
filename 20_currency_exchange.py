# Problem 20: Currency Exchange
# An exchange booth uses these rates: 1 USD = 280 PKR, 1 EUR = 305 PKR, 1 SAR = 75 PKR. Take amount in PKR and target currency, print converted amount.
# Input 28000 USD
# Output 100.0 USD

rates = {'USD': 280, 'EUR': 305, 'SAR': 75}

try:
    amount, currency = input().split()
    amount = float(amount)
    converted = round(amount / rates[currency], 2)
    print(f"{converted} {currency}")
except:
    print("error")