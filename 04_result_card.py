# Problem 4: Result Card
# A student has marks of 5 subjects (out of 100). Print percentage and grade: A (80+), B (70+), C (60+), D (50+), else F.
# Input 90 80 70 60 50
# Output 70.0% Grade B


try :
    No_subjects = int(input("Enter the number of subjects: "))
    if No_subjects < 0 :
        print("Input cannot be negative")
    else:
        total_marks = 0
        for i in range(No_subjects):
            marks = int(input(f"Enter the marks for subject {i+1}: "))
            if marks < 0 or marks > 100:
                print("Invalid marks. Please enter marks between 0 and 100.")
                continue
            
            total_marks += marks
        percentage = (total_marks / (No_subjects * 100)) * 100
        if percentage >= 80:
            print(f"your total marks are {total_marks} and percentage is {percentage:.2f}. Grade: A")
        elif percentage >= 70 and percentage < 80:
            print(f"your total marks are {total_marks} and percentage is {percentage:.2f}. Grade: B")
        elif percentage >= 60 and percentage < 70:
            print(f"your total marks are {total_marks} and percentage is {percentage:.2f}. Grade: C")

        else :
            print(f"your total marks are {total_marks} and percentage is {percentage:.2f}. Grade: D")
except :
    print("error")