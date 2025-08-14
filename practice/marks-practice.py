marks = int(input("enter your marks"))
if marks >= 91 and marks <= 100:
    print("grade A")
elif marks >= 71 and marks <= 90:
    print("grade B")
elif marks >= 51 and marks <= 70:
    print("grade C")
elif marks >= 35 and marks <= 50:
    print("grade D")
elif marks >= 0 and marks <= 35:
    print("fail")
else:
    print("invalid input, marks is out of range(0-100)")