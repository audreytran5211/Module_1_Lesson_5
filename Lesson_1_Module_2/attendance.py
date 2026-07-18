medical_cause = input("did you have a medical cause?(Y/n): ").strip().lower()
if medical_cause == "y":
    print("you are allowed to attend the exam")
else:
    attendance = int(input("enter your attendance percentage:"))
    if attendance >= 75:
        print("allowed")
    else:
        print("not allowed")
        