# Problem 12: Password Validator
# A signup page accepts a password only if it has at least 8 characters, one uppercase, one lowercase, one digit and one special character (@#$%&*). Print Valid or the missing rule(s).
# Input Hello@123
# Output Valid
# Input hello123
# Output Missing: uppercase, special character

try:
    password = input("Enter your password: ")
    error=[]
    num =0
    up=0
    lw =0
    sp =0
    if len(password) < 8:
        error.append("Password must be at least 8 characters long.")

    for i in password:
        if i.isupper():
            up +=1
    for i in password:
        if  i.islower():
            lw +=1
    for i in password:
        if i.isdigit():
            num +=1
    for i in password:
        if i in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~":
            sp +=1

    if up == 0:
        error.append("Password must contain at least one uppercase letter.")
    if lw == 0:
        error.append("Password must contain at least one lowercase letter.")
    if num == 0:
        error.append("Password must contain at least one digit.")
    if sp == 0:
        error.append("Password must contain at least one special character.")
    if error:
        for i in error:
            print(i)
    else:
        print("Password is valid.")

except Exception as e:
    print(f"An error occurred: {e}")


    
    # if not any(char.isdigit() for char in password):
    #     error.append("Password must contain at least one digit.")
    # if not any(char.isupper() for char in password):
    #     error.append("Password must contain at least one uppercase letter.")
    # if not any(char.islower() for char in password):
    #     error.append("Password must contain at least one lowercase letter.")
    # if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
    #     error.append("Password must contain at least one special character.")
    # if error:
    #     print("Password is not valid:")
    #     for e in error:
    #         print(f"- {e}")

    # else:
    #     print("Password is valid.")

# except Exception as e:
#     print(f"An error occurred: {e}")