# Problem 17: Hospital Token System
# Patients arrive and get tokens. Normal patients are served in order, but emergency patients are always served first. Take a list of (name, type) and print the serving order.
# Input [('Ali','normal'), ('Sara','emergency'), ('Omar','normal')]
# Output Sara, Ali, Omar

patient=[]
try :
    for i in range(5):
        p_name = input("Enter patient name: ").lower()
        P_condition = input("Enter patient condition:(normal/serious) ").lower()
        patient.append((p_name, P_condition))

    print("serious patient list: ",end = "")
    for p in patient:
          if p[1] == "serious":
            print(p[0],end = " ")

except Exception as e:
    print(f"An error occurred: {e}")