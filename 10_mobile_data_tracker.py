# Problem 10: Mobile Data Tracker
# A user's data usage for 7 days (in MB) is given. Print total, daily average and the day number with highest usage.
# Input 200 350 120 500 90 410 300
# Output Total: 1970, Average: 281.43, Highest: Day 4

try :
    data = []
    total = 0
    avg = 0
    for i in range(0,7):
        data.append(int(input(f"Enter the data for day {i+1}:")))


    print("Data for 7 days: ",sum(data))
    print("Avg for 7 days: ",round(sum(data)/7,2))
    print("max data use at ",data.index(max(data))+1)

except Exception as e:
    print(e)
