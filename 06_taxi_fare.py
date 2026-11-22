# Problem 6: Taxi Fare
# A taxi charges Rs 100 base fare covering the first 2 km, then Rs 35 per extra km. Night rides (after 10 PM) cost 20% extra. Take km and ride time (day/night), print fare.
# Input 10 night
# Output Fare: Rs 456.0


try :
    distance= int (input("Enter the distance in km: "))
    time = input("Enter situation (day/night): ").lower()
    if distance < 0 :
        print("Distance cannot be negative")
    elif distance <= 2:
        fare = 100
    else:
        fare = 100 + (distance - 2) * 35
    if time == "night":
        extra_cost = fare * 0.2

    print("Total fare: ",fare + extra_cost)
except :
    print("error")