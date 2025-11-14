#q.1 Write a Python program to print a formatted string using print() and f-string
# name = "jhon"
# print(name)
# print(f"my name is {name}.")

# q.2 Write a Python program to print “Hello, World!” on the screen.
# print("Hello, World!")

# q.3 Write a Python program to read a name and age from the user and print a formatted output.
# name = input("enter the name")
# age = int(input("enter the age"))
# print(f"my name is {name} and i am {age} year old.")

# q.4 Write a Python program to read a string, an integer, and a float from
# the keyboard and display them
# datatype = int(input("enter the data in integer"))
# datatype1 = float(input("enter the data"))
# print(f"this is the int datatype = {datatype} and this is a float datatype = {datatype1}")

# q.5 Write a Python program to open a file in write mode, write some text, and then close it.
# f = open("test.txt",'w')
# f.write("hello world")
# f.close()

# q.6 Write a Python program to create a file and write a string into it.
# f = open("write.txt",'w')
# f.write("hello, my name is jhon")
# f.close()

# q.7 Write a Python program to read the contents of a file and print them on the console.
# f = open("test.txt",'r')
# data = f.read()
# print(data)

# q.8 Write a Python program to write multiple strings into a file.
# f = open("test.txt",'a')
# f.write("""\n hello india
#            \n hello gujrat
#            \n hello surat 
#         """)
# f.close()

# q.9 Write a Python program to create a file and print the string into the
# file. 
# f = open("lab.txt",'w')
# f.write("hello world from jhon")
# f.close()

# q.10 Write a Python program to read a file and print the data on the console
# f = open("lab.txt",'r')
# data = f.read()
# print(data)

# q.11 Write a Python program to check the current position of the file cursor using tell().
# f = open("test.txt",'r')
# print(f.tell())

# --------------------------------- exception handling----------------------------------
# q.12 Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
# input)


# try:
#     num1 = int(input("enter the number 1"))
#     num2 = int(input("enter the number 2"))
#     print("enter the choice in between this +, -, *, /")
#     choice =  input("enter your choice")
#     if choice == '+':
#         print(f"addition of two number {num1+num2}")

#     elif choice == '-':
#         print(f"substraction of two number {num1-num2}")

#     elif choice == '*':
#         print(f"multiplication of two number {num1*num2}")

#     elif choice == '/':
#         if  num2 == 0:
#             print("number is not divisible by zero")
#         else:
#             print(f"division of two number are {num1/num2}")

#     else:
#         print("invalid choice")
# except Exception as e:
#     print("an error occured", e)


# q.13 Write a Python program to demonstrate handling multiple exceptions
# try:
#     number = [10,20,30]
#     num = int(input("enter the number : "))
#     if num in number:
#          print("your guessing is correct, your number in this list")
#     else:
#          print("your number is not in this list")

# except Exception as e:
    #   print(e)

# try:
#     num1 = int(input("enter the number"))
#     num2 = int(input("enter the number 2"))
#     result = num1/num2
#     if num1 == 0:
#             print("number is not divisible by zero")
#     else:
#         print(f"division is {result}")

# except Exception as e:
#     print(e)

# try:
#     a = 10
#     print(b)
# except Exception as e:
#     print(e)

# try:
#     a = "abc"
#     b = int(a)
#     print(b)
# except Exception as e:
#     print(e)

# try:
#     number = [10,20,30]
#     num = int(input("enter the number : "))
#     if num in number:
#          print("your guessing is correct, your number in this list")
#     else:
#         print(f"number is not in {number} ")
    

#     num1 = int(input("enter the number"))
#     num2 = int(input("enter the number 2"))
#     result = num1/num2
#     print(f"division is {result}")

#     a = 10
#     print(b)

#     a = "abc"
#     b = int(a)


# except ZeroDivisionError:
#     print("sorry, 0 is not divisible")

# except NameError:
#     print("sorry the name is other define")

# except ValueError:
#     print("sorry, string is not cnvert in int")

# except Exception as e:
#     print(e)

# q.14  Write a Python program to handle exceptions in a calculator

# try:
#     num1 = int(input("enter the number1"))
#     num2 = int(input("enter the number2"))

#     print("+,-,/,*")
#     choice = input("enter the choice")

#     if choice == '+':
#         print(f"addition is {num1+num2}")

#     elif choice == '-':
#         print(f"substraction is {num1-num2}")

#     elif choice == '*':
#         print(f"multiplication is {num1*num2}")

#     elif choice == '/':
#         print(f"division is {num1/num2}")
    
#     else:
#         print("invalid choice")

# except ZeroDivisionError:
#     print("number is not divisible by zero")

# except Exception as e:
#     print(e)

# q.15 Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
# try:
#     num1 = int(input("enter the number 1:"))
#     num2 = int(input("enter the number 2:"))

#     result = num1/num2
#     print(result)

#     filename = input("enter the file name")

#     f = open(filename,'r')
#     data = f.read()
#     print(data)
#     f.close()


# except ZeroDivisionError:
#     print("0 is not divisible")

# except FileNotFoundError:
#     print("this file is not found")

# except Exception as e:
#     print(e)

# q.16 Write a Python program to handle file exceptions and use the finally block for closing
# the file.
# try:
#     filename = input("enter the filename")
#     f = open(filename,'r')
#     data = f.read()
#     print("----------file content----------")
#     print(data)

# except FileNotFoundError:
#     print("file not found")

# except Exception as e:
#     print(e)

# finally:
#     print("program executed")

# q.17 Write a Python program to print custom exceptions.

# class invalidpasswordException(Exception):
#    def __init__(self, msg):
#        super().__init__(msg)

# class password:

#     def passwordcheck(self):
#         password1 = input("enter the password")
#         if len(password1) < 8:
#             raise invalidpasswordException("password must be 8 digit")
#         else:
#             print("password is correct")
# try:
#     p = password()
#     p.passwordcheck()
# except Exception as e:
#     print(e)

# --------------------------------- class and object -------------------------------------------
# q.18 Write a Python program to create a class and access its properties using an object
# class animaal:

#     def dog(self):
#         print("dog is barked")

#     def cat(self):
#         print("cat is eat loaf")

# a = animaal()
# a.dog()
# a.cat()

# q.19 Write a Python program to create a class and access the properties
# of the class using an object. 

# class pen:
#     type = "flair"
#     price = 10

#     def display(self):
#         print(f"my pen name is {self.type} and its price is {self.price}")

# p = pen()
# p.display()


# q.20 Write a Python program to demonstrate the use of local and
# global variables in a class.

# a = 10

# class sum:
#     b = 20
#     def display(self):
#         print("local variable is",self.b)
#         print("global variable is",a)

#     def total(self):
#         a= 10
#         a += 20
#         print(a)

# s = sum()
# s.display()
# s.total()

# ------------------------------------- inheritance ----------------------------------------
# q.21 Write a Python program to show single inheritance
# child class derived from one parent class
# class A:
    
#     a = 10
#     b = 20
# class B(A):

#     def sum(self):
#         print(f"sum of {self.a} and {self.b} is {self.a+self.b}")

# s = B()
# s.sum()

# q.22 Write a Python program to show multilevel inheritance. 
# child class derived from another derived class is known as a multilevel inheritance

# class person:
#     def name(self):
#         self.name = "jhon"
#         print(f"my name is {self.name}.")

# class emp(person):

#     def age(self):
#         self.age = 25
#         print(f"my age is {self.age}")

# class salary(emp):

#     def sal(self):
#         self.sal = 45000
#         print(f"my name is {self.name} and i am {self.age}, my salary is {self.sal}")

# s = salary()
# s.sal()
# s.name()
# s.age()

# child class derived from two or more parent class

# class notebook:
#     def purchase(self):
#         print("i am buysing notebook")

# class pencil:
#     def type(self):
#         print("i am purchasing doms pencil")

# class stationary(notebook,pencil):
#     def display(self):
#         print("i am purchasing notebook and pencil from abc stationary shop")

# s = stationary()
# s.purchase()
# s.type()
# s.display()

# Hierarchical Inheritance: multiple child class inherits from one single parent class
# class A:
#     def student(self):
#         print("there are 75 students in class A division")

# class B(A):
#     def boys(self):
#         print("there are 38 boys in class A")

# class C(A):
#     def girls(self):
#         print("there are 37 girls in class A")

# a = A()
# a.student()

# b = B()
# b.boys()

# c = C()
# c.girls()

# Hybrid Inheritance: A combination of two or more types of inheritance.
# class A:
#     def student(self):
#         print("there are 75 students in class A division")

# class B(A):
#     def boys(self):
#         print("there are 38 boys in class A")

# class C(A):
#     def girls(self):
#         print("there are 37 girls in class A")

# a = A()
# a.student()

# b = B()
# b.boys()

# c = C()
# c.girls()

# q.23 Write a Python program to show single inheritance.
# class girl:
#     def display(self):
#         print("i am girl")

# class student(girl):
#     def show(self):
#         print("i am a girl and i am student of standard 6")

# s = student()
# s.show()
# s.display()

# q.24 Write a Python program to show multilevel inheritance. 
# class grandparent:
#     def grandparent_method(self):
#         print("this is a grand parent class")

# class parnet(grandparent):
#     def parent_method(self):
#         print("this is a parent class")

# class child(parnet):
#     def child_method(self):
#         print("this is a child class")

# c = child()
# c.child_method()
# c.parent_method()
# c.grandparent_method()

# q.25 Write a Python program to show multiple inheritance
# class father:
#     def father_method(self):
#         print("this is a father class")

# class mother:
#     def mother_method(self):
#         print("this is a mother class")

# class child(father,mother):
#     def child_method(self):
#         print("this is a child class")

# c = child()
# c.father_method()
# c.mother_method()
# c.child_method()

# q.26 Write a Python program to show hierarchical inheritance.
# class vehicle:
#     def v_method(self):
#         print("this is a vehicale method")

# class car(vehicle):
#     def c_method(self):
#         print("this is a car class method")

# class bike(vehicle):
#     def b_method(self):
#         print("this is a bike class")

# b = bike()
# b.v_method()
# b.b_method()

# c = car()
# c.c_method()
# c.v_method()

# q.27 Write a Python program to show hybrid inheritance.
# class Employee:
#     def work(self):
#         print("Employee works.")

# class TeamLead(Employee):
#     def lead(self):
#         print("TeamLead manages team work.")

# class Developer(Employee):
#     def code(self):
#         print("Developer writes code.")

# class Manager(TeamLead, Developer):  # Hybrid Inheritance
#     def manage(self):
#         print("Manager oversees everything.")
        
# m = Manager()
# m.work()
# m.lead()
# m.code()
# m.manage()

# q.28  Write a Python program to demonstrate the use of super() in inheritance.
# class parent:
#     def show(self):
#         print("this is a parent class")

# class child(parent):
#     def show(self):
#         super().show()
#         print("this is a child class method")

# c = child()
# c.show()

# ------------------------------------ method overloading and overridding ------------------------
# q.29 Write Python programs to demonstrate method overloading and method overriding

