# n = int(input("enter the number"))

# count = 0

# n = 0
for j in range(1,100):
    n = j
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break

    if flag == 0:
        print(f"number is prime {n}")
    else:
        pass

