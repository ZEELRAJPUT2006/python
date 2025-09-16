l = [10,20,30,40,50]

# def square(a):
#     return a*a
# s = []
# for i in l:
#     # print(i)
#     k = square(i)
#     s.append(k)
# print(s)

def square(a):
    return a*a
# s = map(square,l)
s = map(lambda a: a*a,l)
print(list(s))







































.