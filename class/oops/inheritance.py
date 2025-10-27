# class pen:
#     price = 10
#     color = "red"
#     company = "chello"

#     def display(self):
#         print(self.price,self.color,self.company)

# class notebook(pen):
#     pages = 200

#     def show(self):
#         print(self.pages,self.price,self.color,self.company)

# class beg(notebook): === multilevel
# class bag(pen) : === herachical
# class bag(pen,notebook): == multiple

# p = pen()
# p.display()
# n = notebook()
# n.show()

# class clg:
#     def __init__(self,id,name,email):
#         self.id = id
#         self.name = name
#         self.email = email

#     def display(self):
#         print(self.id,self.name,self.email)

# class student(clg):
 
    # def __init__(self, id, name, email):
        # super().__init__(id, name, email)
        # self.id = id
        # self.name = name
        # self.email = email

#     def show(self):
#         print(self.id,self.name,self.email)

# # c= clg(101,"zeel","zeel@gmail.com")
# # c.display()

# s = student(101,"tisha","tisha@gmail.com")
# s.show()
# s.display()

# class animal:

#     def __init__(self,name):
#         self.name = name

#     def sleep(self):
#         print("animal is sleeping")

#     def eat(self):
#         print("animal is eating")

# class dog(animal):

#     def __init__(self, name, bread):
#         super().__init__(name)
#         self.bread = bread

#     def bark(self):
#         print(f"the dog {self.name} of bread {self.bread} is barking")

# d = dog("bob","german shephered")
# d.bark()
# d.sleep()
# d.sleep()

class a:
    def __init__(self):
        print("A constructor is called")

class b(a):
    def __init__(self):
        super().__init__()
        print("B construcutor is called")

b1 = b()
