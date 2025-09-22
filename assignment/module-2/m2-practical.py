# Write a Python program to create a list with elements of multiple data types (integers, 
# strings, floats, etc.). 

l = ["hello",12,13.5]
# print(l)

# • Write a Python program to access elements at different index positions. 
# print(l[0])
# print(l[1])
# print(l[2])

# Write a Python program to find the length of a list using the len() function. 
# print(len(l))

# • Write a Python program to add elements to a list using insert() and append(). 
# l.append("world")
# l.insert(2,"python")
# print(l)

# • Write a Python program to remove elements from a list using pop() and remove(). 
# print(l.pop(2))
# l.remove("hello")
# print(l)

#  3) Write a Python program to update a list using insert() and 
# append(). 4) Write a Python program to remove elements from a list using pop() and 
# remove().
# l.insert(2,"python")
# l.append("world")

# l.pop(2)
# l.remove("hello")
# print(l)

# Write a Python program to iterate over a list using a for loop. 
# • Write a Python program to sort a list using both sort() and sorted().

# for i in l:
#     print(i)

# l1 = [10,20,30,40]
# l1.sort(reverse=True)
# l2 = sorted(l1)
# print(l2)

# Practical Examples: 5) Write a Python program to iterate through a list and print each 
# element. 6) Write a Python program to insert elements into an empty list using a for loop and 
# append(). 

# for i in l:
#     print(i)

# l1 = []
# for i in range(1):
#     l1.append("hello")
# print(l1)

# Write a Python program to create a tuple with multiple data types. 
# • Write a Python program to concatenate two tuples.

t = ("hello",12,13.33,15,16,17,18)
# t1 = ("world",13)
# print(t + t1)
# print(t1)    

# 7) Write a Python program to convert a list into a tuple. 8) Write a 
# Python program to create a tuple with multiple data types. 9) Write a Python program to 
# concatenate two tuples into one. 10) Write a Python program to access the value of the first 
# index in a tuple.

# t1 = tuple(l)
# print(t1)

# t1 = ("hello",12,13.2)
# print(t1)

# t1 = ("hello",13,14)
# t2 = ("world",15,16)
# t3 = t1 + t2
# print(t3)

# print(t[:1])

# Write a Python program to access values between index 1 and 5 in a tuple. 
# print(t[1:5])

# # • Write a Python program to access alternate values between index 1 and 5 in a tuple. 
# print(t[1:5:2])

#  11) Write a Python program to access values between index 1 and 5 in 
# a tuple. 12) Write a Python program to access the value from the last index in a tuple.

# print(t[1:5])
# print(t[-1:])

# Write a Python program to create a dictionary with 6 key-value pairs.
d = {"name":"jhon" , "age": 25, "lan":"hindi", "sub":"english", "std":8,"div":3}
# print(d)

# • Write a Python program to access values using dictionary keys. 
# print(d.keys())

# 14) Write a Python program to access values using keys from a dictionary.
# print(d["name"])

# Write a Python program to update a value in a dictionary.
# d.update({"name":"bob"})
# print(d)

# • Write a Python program to merge two lists into one dictionary using a loop. 
# l1 = ["hello","world","python"]
# l2 = ["java","RDBMS","C"]
# d1 = []
# for i,j in d.items():
#     print(i,j)

# 15) Write a Python program to update a value at a particular key in a 
# dictionary. 
# d.update({"age":18})
# print(d)

# 16) Write a Python program to separate keys and values from a dictionary using 
# keys() and values() methods.
# print(d.keys())
# print(d.values())

#  17) Write a Python program to convert two lists into one 
# dictionary using a for loop. 
# l1 = ["hello","world","python"]
# l2 = ["java","RDBMS","C"]
# d1 = []
# for i,j in d.items():
#     print(i,j)


# 18) Write a Python program to count how many times each 
# character appears in a string.
# count = 0
# for i in d:
#     print(len(i))
#     count += 1

# Write a Python program to create a function that takes a string as input and prints it.
# def st():
#     st = input("enter the string")
#     print(st)
# st()

# Write a Python program to create a calculator using functions. 
# def calc(a,b):
#     print(f"addition of {a} and {b} is : {a+b}")
#     print(f"multiplication of {a} and {b} is : {a*b}")
#     print(f"substraction of {a} and {b} is : {a-b}")
#     print(f"division of {a} and {b} is : {a/b}")
# calc(10,5)

#  19) Write a Python program to print a string using a function
# def st():
#     st = ("hello world")
#     print(st)
# st()

# 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum.
# def sum(a,b):
#     print(f"sum of two arguments are {a} and {b} is : {a+b}")
# sum(10,5)

# 21) Write a Python program to create a lambda function with one expression. 
# sq = lambda a : a*a
# print(sq(5))

# 22) Write a Python program to create a lambda function with two expressions.
# add = lambda a,b : a+b
# print(add(10,5))

# Write a Python program to import the math module and use functions like sqrt(), ceil(), 
# floor(). 

# import math
# sq = print(math.sqrt(4))
# ce = print(math.ceil(1.5))
# fl = print(math.floor(7.9))

import random
# Write a Python program to generate random numbers using the random module.
# n = random.randint(1,100)
# print(n)

#  23) Write a Python program to demonstrate the use of functions from the math module.
import math
# sqrt = print(math.sqrt(25)) 
# print(math.ceil(7.9))
# print(math.factorial(5))
# print(math.floor(6.99))

# 24) Write a Python program to generate random numbers between 1 and 100 using the random module.
# n = random.randint(1,100)
# print(n)

