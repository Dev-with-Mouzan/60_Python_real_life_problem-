# Problem 13: Email Validator
# A form must accept an email only if it has exactly one @, at least one dot after the @, no spaces, and does not start with @.
# Input ali@gmail.com
# Output Valid
# Input ali@gmail
# Output Invalid

try:
    email = input("Enter your email address: ")
    if "@gmail" not in email or ".com" not in email:
        print("Invalid email address. Please enter a valid email.")
    else:
        print("Email address is valid.")
except Exception as e:
    print(f"An error occurred: {e}")