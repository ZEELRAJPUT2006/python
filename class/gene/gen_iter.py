def square(a):
    for i in range(1,a+1):
        yield i*i
a = iter(square(5))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
    