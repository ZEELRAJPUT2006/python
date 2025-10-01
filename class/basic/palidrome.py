n = 123321
temp = n
sum = 0

while n != 0:
    rem = n%10
    sum = sum * 10 + rem
    n = n//10
if(sum == temp):
    print("number is palidrome")
else:
    print("number is not palidrome")
    