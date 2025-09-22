# print("hello world")

# print("my name is zeel")

# Write a Python program that demonstrates the correct use of indentation, comments, and
# variables following PEP 8 guidelines.
# ============================================================================================
# for i in range(1,5):  indentation
#     print(i)

# a = 10
# print(a)  comment single line

# a = 10
# A_10 = "Hello"  variable

# Practical Example 1: How does the Python code structure work?

# a = 10

#  Practical Example 2: How to create variables in Python?

# id = 101
# name = "jhon"
# age = 25

# print(id,name,age)

# Practical Example 3: How to take user input using the input() function

# a = input("enter the value of a")
# print(a)

# Practical Example 4: How to check the type of a variable dynamically using type()

# a = 10
# name = "jhon"
# b = 10.10

# print(type(a))
# print(type(name))
# print(type(b))

# Practical Example 5: Write a Python program to find greater and less than a number using
# if_else.

# num1 = int(input("enter the number1"))
# num2 = int(input("enter the number1"))

# if num1 > num2:
#     print(f"{num1} number1 is greater {num2}")
# else:
#     print(f"{num1}number is less than{num2}")

# Practical Example 6: Write a Python program to check if a number is prime using if_else.

# n = int(input("enter the number"))
# i = 2
# c = 0

# if n<=1:
#     print("number is not prime")
# else:
#     while i<n:
#         if n%i==0:
#             print(n)
#             c=1
#             i+=1
#         else:
#             pass

# if c==0:
#     print("number is prime")
# else:
#     print("number is not prime")

# Practical Example 7: Write a Python program to calculate grades based on percentage using
# if-else ladder.

# per = float(input("enter the marks"))

# if per>90 and per<100:
#     print("Grade A+")
# elif per>80 and per<90:
#     print("Grade A")
# elif per>70 and per<80:
#     print("Grade B+")
# elif per>60 and per<70:
#     print("Grade B")
# elif per>50 and per<60:
#     print("Grade C")
# elif per>40 and per<50:
#     print("Grade D")
# else:
#     print("Fail")

# Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.

# age = int(input("enter the age"))

# if age>18:
#     print("you can go to donate")
#     if age>=18:
#         print("you are eligible to donate blood")
# else:
#     print("you are not eligible to donate a blood")

# Practical Example 1: Write a Python program to print each fruit in a list using a simple for
# loop. List1 = ['apple', 'banana', 'mango']

# list1 = ['apple','banana','mango']
# for i in range(1):
#     print(list1)

# Practical Example 2: Write a Python program to find the length of each string in List1

# list1 = ['apple','banana']
# for word in list1:
#     print(f"length of {word} is {len(word)}")

# Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.

# fruit = ['apple', 'banana', 'mango']
# search = input("enter the string: ") 

# for item in fruit:
#     if item == search:
#         print("string is in a list")
#         break
# else:
#     print("string is not in a list")

# Practical Example 4: Print this pattern using nested for loop:
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)

# Practical Example: 1) Write a Python program to print "Hello" using a string
# def h1():
#     print("hello")
# h1()

# Practical Example: 2) Write a Python program to allocate a string to a variable and print it.
# s = "hello world"
# print(s)

# • Practical Example: 3) Write a Python program to print a string using triple quotes.
# s = '''hello my world'''
# print(s)

# Practical Example: 4) Write a Python program to access the first character of a string using
# index value.
# s = "hello world"
# print(s[:1])

# Practical Example: 5) Write a Python program to access the string from the second position
# onwards using slicing
# s = "hello world"
# print(s[1:])

# Practical Example: 6) Write a Python program to access a string up to the fifth character
# s = "hello world from jhon"
# print(s[0:6])

# Practical Example: 7) Write a Python program to print the substring between index values 1
# and 4.
# s = "hello world"
# s1 =s[1:4]
# print(s1)


# Practical Example: 8) Write a Python program to print a string from the last character.
# s = "hello world"
# print(s[-1:])

# Practical Example: 9) Write a Python program to print every alternate character from the
# string starting from index 1.

# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']

# list1 = ['apple', 'banana', 'mango']
# for i in list1:
#     if i == 'banana':
#         continue
#     print(i)

# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
# the break statement.
# for i in list1:
#     if i == 'banana':
#        break
#     print(i)

# Write a Python program to demonstrate string slicing
# l = "hello world from python and jhon"
# print(l[0:6])
# print(l[1:4])
# print(l[5:])
# print(l[:5])
# print(l[-5:])
# print(l[-5:-7])

# • Write a Python program that manipulates and prints strings using various string methods.
str1 = "hello everyone welcome to the c.b.patel campus from us"
# print(len(str1))
# print(str1.casefold())
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
# print(str1.title())
# print(str1.strip())
# print(str1.replace('c','D',31))
# print(str1.find("everyone"))
# print(str1.startswith("h"))
# print(str1.endswith("s"))
# print(str1.split(" ",3))
# print("good morning".join("str1"))
# print(str1.isalnum())
# print(str1.isalpha())
# print(str1.isascii())
# print(str1.isdecimal())
# print(str1.isdigit())
# print(str1.zfill(10))
# print("str1".center(21,"*"))

# • Write a Python program to apply the map() function to square a list of numbers.
l = [10,20,30,40]
# def square(a):
#     return a*a
# s = map(lambda a: a*a,l)
# print(list(s))

# • Write a Python program that uses reduce() to find the product of a list of numbers.
# from functools import reduce
# s = reduce(lambda a,b:a*b,l)
# print(s) 

# • Write a Python program that filters out even numbers using the filter() function.
# s = filter(lambda a: a%2==0 ,l)
# print(list(s))

# Write a generator function that generates the first 10 even numbers. 
# • Write a Python program that uses a custom iterator to iterate over a list of integers
# l1 = [10,20,30,40]
# k = iter(l1)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))


# def even():
#     n = 1
#     count = 0
#     while count < 10:
#         yield n * 2
#         n += 1
#         count += 1

# for num in even():
#     print(num)

# Create a mini-project where students combine conditional statements, loops, and functions 
# to create a basic Python application, such as a simple calculator or a grade management 
# system. 

# print("1. for addition")
# print("2. for substraction")
# print("3. for multiplication")
# print("4. for division")

# def add(a,b):
#     return a+b

# def sub(a,b):
#       return a-b

# def multi(a,b):
#       return a*b

# def div(a,b):
#       return(a/b)

# ch = int(input("enter the choice"))
# a = int(input("enter the number 1"))
# b = int(input("enter the number 2"))

# if ch == 1:
#      print(f"addition of two number are add{(a+b)}")

# elif ch == 2:
#     print(f"substraction of two numbers are sub{(a-b)}")

# elif ch == 3:
#     print(f"multiplication of two numbers are multi{(a*b)}")

# elif ch == 4:
#     print(f"division of two number are div{(a/b)}")

# else:
#     print("invalid choice")

# =============== grade =================
marks = int(input("enter the marks"))
if marks >= 91 and marks <= 100:
        print("grade A")
elif marks >= 71 and marks <= 90:
        print("grade B")
elif marks >= 51 and marks <= 70:
      print("grade C")
elif marks >= 35 and marks <= 50:
      print("grade D")
elif marks >= 0 and marks <= 34:
      print("fail")
else:
      print("invalid input, marks is out of range(0-100)")