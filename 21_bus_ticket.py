# Problem 21: Bus Ticket
# A bus ticket is Rs 500. Children under 5 travel free, ages 5 to 12 and 60+ pay half, others pay full. Take a list of passenger ages and print the total fare.
# Input [3, 10, 25, 65]
# Output Total: Rs 1000

try:
    age_list=[]
    total_fare=0
    p_No=int(input("Enter the number of passengers: "))
    if p_No <= 0:
        print("Number of passengers must be greater than zero.")
    else :
        for i in range(0,p_No):
            age=int(input(f"Enter the age of passenger {i+1}: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                break
            age_list.append(age)
            if age < 5:
                total_fare +=0
            if age >= 5 and age <= 12 or age >= 60:
                total_fare += 250
            if age > 12 and age < 60:
                total_fare += 500
    print("Total fare: ",total_fare)

except ValueError:
    print("Invalid input. Please enter a valid number.")
