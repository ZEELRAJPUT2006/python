# from functools import reduce
l = [10,20,30,40,50,4,9]
# k = reduce(lambda a,b:a-b,l)
# k = reduce(min,l)
# print(k)

# k = reduce(lambda a,b:a+b,l)
# ave = k/len(l)
# print(ave)

# s = filter(l)
s = filter(lambda a: (a**0.5)**2==a,l)
print(list(s))

