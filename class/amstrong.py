
# while n != 0:
#     rem = n%10
#     sum += rem ** 3
#     # print(rem)
#     n = n//10


# if sum == temp:
#     print("number is amstrong")
# else:
#     print("number is not amstrong")

for i in range(100,1000):
    n = temp
    temp = n
 
    while i != 0:
        rem = i%10
        sum += rem ** 3
        i = i//10
        # print(sum)


if sum == temp:
    print(f"{temp} : amstrong number")
else:
    pass