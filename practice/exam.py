# a = 10
# b = str(a)
# print(type(b))

# ------------- airthmethic operator --------------------
# a = 10
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)

# ---------------- assignment operator -----------------
# a = 10
# a += 5
# a -= 5
# a *= 10
# a /= 5
# a //= 5
# a **= 5
# print(a==10)
# print(a)

# -------------- logical operator ----------------------
# a = 10
# b = 5
# print(a>b and b<a)
# print(a>b and b>a)
# print(a<b and b<a)
# print(a<b and b<a)

# print(a>b or b<a)
# print(a>b or b>a)
# print(a<b or b>a)

# print(a != b)

# --------------------- relational operator -------------------
# a = 10
# b = 5
# print(a == b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# ------------------------ identity openrator -----------------
# a = [10,20,30]
# b = a
# print(a is b)
# print(a is not b)

# ------------------------ membership operator ---------------
# print("a" in "azad")
# print("a" not in "banana")
# print([1,2] is [1,2])

# ------------------------- string -------------------------
string = "hello world"
# print(string[1])
# print(string[5:])
# print(string[1:5])
# print(string[:1])
# print(string[-1])
# print(string[-5:-1])
#  print(string)

# print(string.capitalize())
# print(string.casefold())
# print(string.title())
# print(string.center(4,"*"))
# print(string.count("o"))
# print(string.encode())
# print(string.endswith("d"))
# print(string.startswith("h"))
# print("abc".isalnum())
# print("abc123".isalpha())
# print(string.isascii())
# print(string.isdecimal())
# print(string.isdigit())
# print(string.islower())
# print(string.upper())
# print(string.lower())
# print(string.isupper())
# print(string.split(","))
# print(string.zfill(50))

# --------------------------  list ------------------------------------------
# list = ["abc","xyz",12,52,"@",5,5]
# print(list)
# list.append("hello")
# list.extend("world")
# list.insert(5,"india")
# c1 = list.copy()
# print(c1)
# print(list)
# print(list.count("abc"))
# list.reverse()
# list.pop()
# list.remove("abc")
# list.clear()
# del list
# list1 = ["q","e","r"]
# list1.sort()
# list.index(5)
# print(list)

# -------------------------- tuple ---------------------
# tuple = (1,"hello","@",5.6,"hello")
# [a,b,c,d,e] = tuple
# print(tuple *2)
# print(len(tuple))
# tuple = type(list)
# print(list)
# print(tuple)

# ------------------------ set -------------------------
# set = {1,"anc","@",85.6,85.6}
# set.add("hello")
# set.update("world")
# set.remove(1)
# set.discard(1)
# set.pop()
# set.clear()
# set1 = set.copy()
# print(set)
# print(set)

s = {1,2,3,4}
s1 = {4,5,6,2}
# print(s1.difference(s))
# print(s1.difference_update())-----------
# print(s1.union(s))
# print(s1.intersection(s))
# print(s1.intersection_update(s))
# print(s1.isdisjoint(s))
# print(s1.issubset(s))
# print(s1.issuperset(s))

# ------------ decorater ------------
# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# l1 = [1,2,3]
# l2 = l1
# print(l2)


# --------------------------------- amstrong number ----------------------------
# n = int(input("enter the number"))
# temp = n
# sum = 0
# while n!=0:
#     rem = n%10
#     sum += rem ** 3
#     n = n//10

# if sum == temp:
#     print("number is amstrong")
# else:
#     print("number is not amstrong")

# for i in range(100,1000):
#     n = i
#     temp = n
#     sum = 0

#     while n != 0:
#         rem = n%10
#         sum += rem ** 3
#         n = n//10

#     if sum == temp:
#         print(temp,"number is amstrong")
    # else:
    #     print(temp,"number is not amstrong")


# ---------------------------------- prime number ---------------------------------------
# n = int(int(input("enter the number")))
# for j in range(3,100):
#     n = j
#     flag = 0
#     for i in range(2,n):
#         if n % i == 0:
#             flag = 1
#             break

#     if (flag == 0):
#         print(n,"number is prime")
    # else:
    #     print(n,"number is not prime")

# ------------------------------------- factorial ------------------------------------------
# n = int(input("enter the number"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     print(fact)
    
# ----------------------------------- fibonnaci series ----------------------------------------
# n = int(input("enter the data"))
# a = 0
# b = 1
# for i in range(0,n):
#     c = a + b
#     print(c)
#     a = b
#     b = c


