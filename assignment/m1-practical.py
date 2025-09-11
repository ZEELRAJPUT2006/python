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
# markdown
# Copy code
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)