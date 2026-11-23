# Problem 11: Attendance Shortage
# A university needs 75% attendance. Take total classes held and classes attended. Print percentage and, if short, how many classes the student must attend in a row to reach 75%.
# Input 40 28
# Output 70.0%, Short. Attend next 8 classes

# try :
#     total_attandance = int (input("Enter the total attandance: "))
#     attended_class = int (input("Enter the attended class: "))
#     if total_attandance < 0 or attended_class < 0 :
#         print("Input cannot be negative")
#     percentage = (attended_class / total_attandance) * 100
#     if percentage < 75 :
#         print("You are not allowed to sit in the exam attent next ",((0.75*total_attandance)-attended_class)/0.25," classes")

# except :
#     print("error")



import math

def check_attendance(classes_held, classes_attended):
    current_percentage = (classes_attended / classes_held) * 100
    print(f"Current Attendance: {current_percentage:.2f}%")
    if current_percentage >= 75:
        print("Your attendance is sufficient. You are good to go!")
    else:
        needed = math.ceil((0.75 * classes_held - classes_attended) / 0.25)
        print(f"Attendance short! You must attend the next {needed} classes in a row to reach 75%.")


try:
    held_class = int(input("Enter the No of held Classes: "))
    attented_classes=int(input("ENter the No of attended classes: "))
    if held_class <= 0 and attented_classes <= 0:
        print("invalid input")
    check_attendance(classes_held=held_class, classes_attended=attented_classes)
except Exception as e:
    print(e)