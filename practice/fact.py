def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num=1)
    
number = 5
print("factorial of",number,"is",factorial(number))