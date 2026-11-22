# Problem 7: Salary Slip
# An employee gets HRA 20% and medical 10% of basic salary. Tax is 5% of gross salary. Take basic salary and print gross, tax and net salary.
# Input 50000
# Output Gross: 65000.0, Tax: 3250.0, Net: 61750.0


try :
    salary = int (input("Enter the salary: "))
    if salary < 0 :
        print("Salary cannot be negative")
    else:
        hra=0.2*salary
        med = 0.1*salary
        salary = salary + hra + med
        print("GROSS salary: ",salary)
        tax = 0.05 * salary
        print("TAX: ",tax)
        net_salary = salary - tax
        print("NET salary: ",net_salary)
except :
    print("error")
