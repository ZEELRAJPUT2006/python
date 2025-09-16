def square(a):
    print(a*a)
    a += 1
    if a<50:
        square(a)
square(5)
