# Problem 8: Voting Eligibility
# A voter registration desk needs to check age. Take birth year (current year 2026). Print age and whether the person is eligible to vote (18 or above).
# Input 2000
# Output Age: 26, Eligible


try :
    year = int(input("Enter your birth year like 2005: "))
    if year < 0 :
        print("Age cannot be negative")
    else :
        age = 2026 - year
        if age < 18 :
            print("age is ",age)
            print("You are not eligible to vote")
        else :
            print("age is ",age)
            print("You are eligible to vote")
except :
    print("error")

